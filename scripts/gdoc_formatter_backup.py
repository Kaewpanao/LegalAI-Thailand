#!/usr/bin/env python
"""
Google Docs Rich Formatter v3
แนวทาง: สร้างเนื้อหา text ทั้งหมดก่อน (ปัญหา index กับภาษาไทย)
แล้วค่อย apply style ทีหลังด้วย text search (ไม่นับ index เอง)
"""
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


def _get_services():
    token_path = os.environ.get(
        "GOOGLE_TOKEN_PATH",
        os.path.join(os.environ.get("HERMES_HOME", os.path.expanduser("~/.hermes")), "google_token.json")
    )
    creds = Credentials.from_authorized_user_file(token_path)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_path, 'w') as f:
            f.write(creds.to_json())
    return build('docs', 'v1', credentials=creds), build('drive', 'v3', credentials=creds)


def _rgb(hex_color):
    h = hex_color.lstrip('#')
    return {
        "rgbColor": {
            "red": int(h[0:2], 16) / 255.0,
            "green": int(h[2:4], 16) / 255.0,
            "blue": int(h[4:6], 16) / 255.0,
        }
    }


def _color_obj(hex_color):
    return {"color": _rgb(hex_color)}


class GoogleDocBuilder:
    """สร้าง Google Doc สวยๆ — แทรก text ก่อน แล้ว style ทีหลัง"""

    def __init__(self, title="Untitled"):
        self.title = title
        self._lines = []      # เก็บทั้งข้อความ + style metadata
        self._tables = []

    def heading(self, text, level=1, color=None):
        size_map = {1: 18, 2: 14, 3: 12}
        color_map = {1: "1A1A2E", 2: "16213E", 3: "0F3460"}
        self._lines.append({
            "type": "heading",
            "text": text,
            "level": level,
            "size": size_map.get(level, 14),
            "color": color or color_map.get(level, "333333"),
        })

    def paragraph(self, text, bold=False, italic=False, size=11, color=None, link=None):
        self._lines.append({
            "type": "paragraph",
            "text": text,
            "bold": bold, "italic": italic,
            "size": size, "color": color, "link": link,
        })

    def bullet(self, text, color=None, bold=False, size=11):
        self._lines.append({
            "type": "bullet",
            "text": text,
            "bold": bold, "size": size, "color": color,
        })

    def divider(self):
        self._lines.append({
            "type": "divider",
            "text": "━" * 40,
        })

    def spacer(self, n=1):
        for _ in range(n):
            self._lines.append({"type": "paragraph", "text": "", "size": 1})

    def table(self, data, header_color="2E86AB", alt_color="F0F4F8", font_size=10):
        idx = len(self._tables)
        self._tables.append({
            "data": data,
            "header_color": header_color,
            "alt_color": alt_color,
            "font_size": font_size,
        })
        # Add inline placeholder so table renders at correct position
        self._lines.append({"type": "paragraph", "text": f"\n[TABLE_{idx}]\n", "size": 1})

    def save(self, folder_id=None):
        docs_svc, drive_svc = _get_services()

        # 1. สร้างเอกสารเปล่า
        doc = docs_svc.documents().create(body={"title": self.title}).execute()
        doc_id = doc['documentId']

        # 2. รวมข้อความทั้งหมดเป็น text ยาว + สร้าง style requests
        #    เอาข้อความทั้งหมดมาต่อกัน แล้ว insert ทีเดียว
        full_text_parts = []
        for line in self._lines:
            full_text_parts.append(line["text"])
        
        # Placeholders are already inline in _lines — no need to append separately
        full_text = "\n".join(full_text_parts)

        # 3. Insert ข้อความทั้งหมดทีเดียวที่ index 1
        insert_req = [{
            "insertText": {
                "location": {"index": 1},
                "text": full_text
            }
        }]
        docs_svc.documents().batchUpdate(
            documentId=doc_id, body={"requests": insert_req}
        ).execute()

        # 4. หาตำแหน่งของแต่ละส่วนจาก document
        doc = docs_svc.documents().get(documentId=doc_id).execute()
        full_doc_text = ""
        for elem in doc.get('body', {}).get('content', []):
            if 'paragraph' in elem:
                for el in elem['paragraph'].get('elements', []):
                    if 'textRun' in el:
                        full_doc_text += el['textRun']['content']

        # 5. สร้าง style requests โดยค้นหาตำแหน่งจากเนื้อหา
        style_reqs = []
        search_pos = 0

        for line in self._lines:
            text = line["text"]
            if not text:
                search_pos += 1  # newline
                continue

            # หาตำแหน่งในเอกสารจริง
            found_pos = full_doc_text.find(text, search_pos)
            if found_pos < 0:
                continue

            start = found_pos + 1  # docs API is 1-indexed
            end = start + len(text)
            search_pos = found_pos + len(text) + 1  # +1 for newline

            if line["type"] == "heading":
                style_reqs.append({
                    "updateParagraphStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "paragraphStyle": {
                            "namedStyleType": f"HEADING_{line['level']}",
                            "spaceAbove": {"magnitude": 12, "unit": "PT"},
                            "spaceBelow": {"magnitude": 6, "unit": "PT"},
                        },
                        "fields": "namedStyleType,spaceAbove,spaceBelow"
                    }
                })
                style_reqs.append({
                    "updateTextStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "textStyle": {
                            "bold": True,
                            "fontSize": {"magnitude": line["size"], "unit": "PT"},
                            "foregroundColor": _color_obj(line["color"]),
                            "weightedFontFamily": {"fontFamily": "Sarabun"},
                        },
                        "fields": "bold,fontSize,foregroundColor,weightedFontFamily"
                    }
                })

            elif line["type"] == "paragraph":
                ts = {"weightedFontFamily": {"fontFamily": "Sarabun"}}
                fields = "weightedFontFamily"
                if line.get("bold"):
                    ts["bold"] = True; fields += ",bold"
                if line.get("italic"):
                    ts["italic"] = True; fields += ",italic"
                if line.get("size"):
                    ts["fontSize"] = {"magnitude": line["size"], "unit": "PT"}; fields += ",fontSize"
                if line.get("color"):
                    ts["foregroundColor"] = _color_obj(line["color"]); fields += ",foregroundColor"
                if line.get("link"):
                    ts["link"] = {"url": line["link"]}; fields += ",link"
                style_reqs.append({
                    "updateTextStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "textStyle": ts,
                        "fields": fields
                    }
                })

            elif line["type"] == "bullet":
                ts = {"weightedFontFamily": {"fontFamily": "Sarabun"}}
                fields = "weightedFontFamily"
                if line.get("bold"):
                    ts["bold"] = True; fields += ",bold"
                if line.get("size"):
                    ts["fontSize"] = {"magnitude": line["size"], "unit": "PT"}; fields += ",fontSize"
                if line.get("color"):
                    ts["foregroundColor"] = _color_obj(line["color"]); fields += ",foregroundColor"
                style_reqs.append({
                    "updateTextStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "textStyle": ts,
                        "fields": fields
                    }
                })
                style_reqs.append({
                    "createParagraphBullets": {
                        "range": {"startIndex": start, "endIndex": end},
                        "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"
                    }
                })

            elif line["type"] == "divider":
                style_reqs.append({
                    "updateTextStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "textStyle": {
                            "fontSize": {"magnitude": 8, "unit": "PT"},
                            "foregroundColor": _color_obj("CCCCCC"),
                            "weightedFontFamily": {"fontFamily": "Sarabun"},
                        },
                        "fields": "fontSize,foregroundColor,weightedFontFamily"
                    }
                })

        if style_reqs:
            docs_svc.documents().batchUpdate(
                documentId=doc_id, body={"requests": style_reqs}
            ).execute()

        # 6. เพิ่มตาราง — แทนที่ placeholder
        for i, t in enumerate(self._tables):
            self._create_table_at_placeholder(docs_svc, doc_id, f"[TABLE_{i}]", t)

        # 7. Move to folder
        if folder_id:
            f = drive_svc.files().get(fileId=doc_id, fields='parents').execute()
            prev = ",".join(f.get('parents', []))
            drive_svc.files().update(
                fileId=doc_id, addParents=folder_id,
                removeParents=prev, fields='id'
            ).execute()

        url = f"https://docs.google.com/document/d/{doc_id}/edit"
        print(f"✅ Created: {self.title}")
        print(f"   URL: {url}")
        return doc_id, url

    def _create_table_at_placeholder(self, svc, doc_id, placeholder, t_info):
        """หา placeholder text แล้วแทนที่ด้วยตาราง"""
        doc = svc.documents().get(documentId=doc_id).execute()
        placeholder_start = None

        for elem in doc.get('body', {}).get('content', []):
            if 'paragraph' in elem:
                for el in elem['paragraph'].get('elements', []):
                    if 'textRun' in el:
                        content = el['textRun']['content']
                        if placeholder in content:
                            placeholder_start = el['startIndex']
                            placeholder_end = el['endIndex']
                            break
            if placeholder_start:
                break

        if not placeholder_start:
            return

        reqs = []

        # Delete placeholder text
        reqs.append({
            "deleteContentRange": {
                "range": {"startIndex": placeholder_start, "endIndex": placeholder_end}
            }
        })

        # Create table at placeholder location
        rows = len(t_info["data"])
        cols = len(t_info["data"][0])

        reqs.append({
            "insertTable": {
                "rows": rows,
                "columns": cols,
                "location": {"index": placeholder_start}
            }
        })

        try:
            svc.documents().batchUpdate(
                documentId=doc_id, body={"requests": reqs}
            ).execute()
        except HttpError as e:
            print(f"⚠️ Table create: {e}")
            return

        # Fill table cells
        doc = svc.documents().get(documentId=doc_id).execute()
        table_el = None
        for elem in doc.get('body', {}).get('content', []):
            if 'table' in elem:
                table_el = elem['table']
                break

        if not table_el:
            return

        # หา table start index จาก document structure
        table_start_idx = None
        for elem in doc.get('body', {}).get('content', []):
            if 'table' in elem:
                table_start_idx = elem['startIndex']
                break

        if not table_start_idx:
            return

        # === Phase 1: Insert text ทุก cell ใน batch เดียว (reverse order) ===
        insert_reqs = []
        cell_info = []  # เก็บ (ri, ci, text, is_header, is_alt)
        for ri, row_data in enumerate(t_info["data"]):
            if ri >= len(table_el['tableRows']):
                break
            row = table_el['tableRows'][ri]
            for ci in range(min(len(row_data), len(row['tableCells']))):
                cell = row['tableCells'][ci]
                cell_start = cell['content'][0]['startIndex']
                text = str(row_data[ci])
                if not text.strip():
                    text = "—"  # Google Docs API rejects empty insertText
                insert_reqs.append({
                    "insertText": {"location": {"index": cell_start}, "text": text}
                })
                cell_info.append((ri, ci, text, ri == 0, ri > 0 and ri % 2 == 0))

        # reverse — insert จากหลังมาหน้าเพื่อ index ไม่เลื่อน
        insert_reqs.reverse()

        try:
            svc.documents().batchUpdate(
                documentId=doc_id, body={"requests": insert_reqs}
            ).execute()
        except HttpError as e:
            print(f"⚠️ Table text insert: {e}")

        # === Phase 2: อ่าน doc ใหม่ + style + background ใน batch เดียว ===
        doc2 = svc.documents().get(documentId=doc_id).execute()
        tbl2 = None
        ts_idx = None
        for elem in doc2.get('body', {}).get('content', []):
            if 'table' in elem:
                tbl2 = elem['table']
                ts_idx = elem['startIndex']
                break

        if not tbl2:
            return

        style_reqs = []
        for ri, ci, text, is_header, is_alt in cell_info:
            if ri >= len(tbl2['tableRows']):
                continue
            cell2 = tbl2['tableRows'][ri]['tableCells'][ci]
            c_start = cell2['content'][0]['startIndex']
            c_end = c_start + len(text)

            # Text style
            ts = {
                "fontSize": {"magnitude": t_info["font_size"], "unit": "PT"},
                "weightedFontFamily": {"fontFamily": "Sarabun"},
            }
            sf = "fontSize,weightedFontFamily"
            if is_header:
                ts["bold"] = True
                ts["foregroundColor"] = _color_obj("FFFFFF")
                sf += ",bold,foregroundColor"

            style_reqs.append({
                "updateTextStyle": {
                    "range": {"startIndex": c_start, "endIndex": c_end},
                    "textStyle": ts, "fields": sf
                }
            })

            # Background
            bg_hex = None
            if is_header:
                bg_hex = t_info["header_color"]
            elif is_alt:
                bg_hex = t_info["alt_color"]

            if bg_hex and ts_idx:
                style_reqs.append({
                    "updateTableCellStyle": {
                        "tableCellStyle": {"backgroundColor": _color_obj(bg_hex)},
                        "fields": "backgroundColor",
                        "tableRange": {
                            "tableCellLocation": {
                                "tableStartLocation": {"index": ts_idx},
                                "rowIndex": ri,
                                "columnIndex": ci,
                            },
                            "rowSpan": 1,
                            "columnSpan": 1,
                        }
                    }
                })

        try:
            svc.documents().batchUpdate(
                documentId=doc_id, body={"requests": style_reqs}
            ).execute()
        except HttpError as e:
            print(f"⚠️ Table style: {e}")
