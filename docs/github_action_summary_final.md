# 🔧 GitHub Action Summary — legalai-thailand-citizen

> **สรุปทุกอย่างที่ต้องแก้ไข/เพิ่มเติม** — 5 Modules, 55+ ไฟล์, ~120 ชม.

---

## 📊 ภาพรวม

| Module | ไฟล์ใหม่ | ไฟล์แก้ | ชม. | Priority |
|--------|:---:|:---:|:---:|:---:|
| 1. 🔴 Fear/Diagnosis (6→12) | 2 | 5 | 20 | P0 |
| 2. 📄 Business Documents (184) | 12 | 4 | 25 | P1 |
| 3. 💰 Tax Planning Module | 8 | 3 | 20 | P1 |
| 4. 💳 Free/Paid Tiers | 6 | 3 | 10 | P1 |
| 5. 🛡️ Guardrails & Safety | 6 | 3 | 10 | P2 |
| **รวม** | **34** | **18** | **~85** | |

---

## 1. 🔴 Fear/Diagnosis (P0 — เร็วที่สุด!)

### ไฟล์ที่ต้องแก้:

| ไฟล์ | Action | รายละเอียด |
|------|:---:|-----------|
| `domain/types.ts` | ✏️ | เพิ่ม 6 LegalCategory: `online_fraud`, `crime`, `government`, `insurance`, `defamation`, `property` |
| `lib/legal/diagnosis-config.ts` | ✏️ | เพิ่ม 6 categories + คำถามละเอียด (4 คำถาม/category) |
| `lib/legal/sources.ts` | ✏️ | 6 → 38+ legal sources (กฎหมายอ้างอิง) |
| `db/schema.ts` | ✏️ | เพิ่ม 6 ค่าใน `legal_category` enum |
| `supabase/migrations/0003_add_categories.sql` | ➕ | Migration SQL — ALTER TYPE เพิ่ม 6 ค่า |
| `lib/mock/categories.ts` | ✏️ | เพิ่ม 6 หมวดใน UI home page |
| `lib/legal/fear-calibration.ts` | ➕ | ไฟล์ใหม่ — ถามความกลัวก่อน diagnosis |

### สิ่งที่ต้องทำ:
1. ✅ เพิ่ม `online_fraud` — ถาม: ถูกหลอกแบบไหน? โอนเท่าไหร่? เมื่อไหร่?
2. ✅ เพิ่ม `crime` — ถาม: เกิดอะไร? เมื่อไหร่? มีหลักฐานอะไร? แจ้งความยัง?
3. ✅ เพิ่ม `defamation` — ถาม: เกิดอะไร? ผ่านช่องทางไหน?
4. ✅ เพิ่ม `insurance` — ถาม: ปัญหาอะไร? มีหลักฐานอะไร?
5. ✅ เพิ่ม `government` — ถาม: เรื่องอะไร? รอนานแค่ไหน?
6. ✅ เพิ่ม `property` — ถาม: ปัญหาอะไร?
7. ✅ เติม sources ให้ `family` + `accident` (ปัจจุบัน = [] — ว่าง!)
8. ✅ เพิ่ม Fear Calibration: ถาม "คุณรู้สึกยังไง? 😰 กลัวมาก / 😟 กังวล / 🤔 เป็นห่วง / 📋 วางแผน"

---

## 2. 📄 Business Documents (P1)

### ไฟล์ที่ต้องสร้างใหม่:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `lib/documents/merge-engine.ts` | ➕ Merge field engine — แทนที่ `{name}`, `{address}` ใน template |
| `lib/documents/category-registry.ts` | ➕ 13 หมวด — ชื่อ, icon, คำอธิบาย |
| `lib/documents/template-configs/` | ➕ โฟลเดอร์ — template configs แยกตามหมวด |
| `app/documents/categories/page.tsx` | ➕ หน้าเลือกหมวดเอกสาร — grid คล้าย home |
| `app/documents/categories/[cat]/page.tsx` | ➕ หน้าเลือก template ในหมวด |
| `app/documents/editor/[templateId]/page.tsx` | ➕ หน้า editor — กรอก merge fields, preview, export |
| `app/api/documents/templates/route.ts` | ➕ API — list templates by category |
| `app/api/documents/render/route.ts` | ➕ API — render template with merge data |
| `app/api/documents/export/route.ts` | ➕ API — export เป็น .docx, .pdf |
| `components/documents/template-card.tsx` | ➕ UI — card แสดง template |
| `components/documents/merge-form.tsx` | ➕ UI — form กรอก merge fields |
| `components/documents/preview-panel.tsx` | ➕ UI — live preview ขณะกรอก |

### ไฟล์ที่ต้องแก้:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `db/schema.ts` | ✏️ เพิ่ม `document_category` enum (13 ค่า) |
| `domain/types.ts` | ✏️ เพิ่ม `DocumentTemplate`, `MergeField`, types |
| `app/documents/page.tsx` | ✏️ เพิ่ม link → categories |
| `supabase/migrations/0004_document_categories.sql` | ➕ Migration |

### 184 Templates — 13 หมวด:

| หมวด | จำนวน |
|------|:---:|
| 🏠 อสังหาฯ | 14 |
| 🏢 เช่า | 17 |
| 🏛️ จดทะเบียนธุรกิจ | 10 |
| 💰 กู้ยืม/การเงิน | 8 |
| 👨‍👩‍👧 ครอบครัว | 8 |
| 👷 การจ้างงาน | 20 |
| 📋 การค้า | 16 |
| 🚗 ยานพาหนะ | 7 |
| 🏨 ท่องเที่ยว | 6 |
| 📝 ทรัพย์สินทางปัญญา | 10 |
| 💰 ภาษีและสรรพากร | 27 |
| 🏛️ Corporate Compliance | 19 |
| 📋 ใบอนุญาตธุรกิจ | 12 |
| **รวม** | **184** |

---

## 3. 💰 Tax Planning Module (P1)

### ไฟล์ที่ต้องสร้างใหม่:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `app/tax/page.tsx` | ➕ Tax home — overview + quick calculator |
| `app/tax/calculator/page.tsx` | ➕ Full calculator with sliders |
| `app/tax/optimizer/page.tsx` | ➕ AI deduction optimizer |
| `app/tax/timeline/page.tsx` | ➕ Tax calendar/timeline |
| `lib/tax/calculator.ts` | ➕ Tax calculation engine (progressive rates) |
| `lib/tax/deductions.ts` | ➕ All 30+ Thai deductions with limits |
| `lib/tax/optimizer.ts` | ➕ AI optimization algorithm |
| `components/tax/tax-slider.tsx` | ➕ UI — income slider |

### ไฟล์ที่ต้องแก้:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `app/page.tsx` | ✏️ เพิ่ม link → /tax |
| `components/layout/navigation.ts` | ✏️ เพิ่ม nav item "💰 ภาษี" |
| `domain/types.ts` | ✏️ เพิ่ม tax types |

### 8 Features:

| # | Feature | Free/Paid |
|---|---------|:---:|
| 1 | 🧮 Tax Calculator | 🆓 |
| 2 | 🎯 Deduction Optimizer | 📦 |
| 3 | 📅 Tax Timeline | 🆓 |
| 4 | 🔮 What-If Scenario | 📦 |
| 5 | 📋 Document Checklist | 🆓 |
| 6 | 📤 Filing Assistant | 📦 |
| 7 | 💡 Tax Tips | 🆓 |
| 8 | 📊 Year-Round Tracker | 📦 |

---

## 4. 💳 Free/Paid Tiers (P1)

### ไฟล์ที่ต้องสร้างใหม่:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `lib/packages/definitions.ts` | ➕ 4 tier definitions |
| `lib/packages/gate.ts` | ➕ API middleware — check package limits |
| `lib/packages/upgrade.ts` | ➕ Upgrade logic |
| `app/pricing/page.tsx` | ➕ Pricing page |
| `components/packages/upgrade-banner.tsx` | ➕ Upgrade CTA banner |
| `components/packages/feature-grid.tsx` | ➕ Feature comparison table |

### 4 Tiers:

| Tier | ราคา | Key Features |
|------|------|-------------|
| 🆓 Free | 0฿ | AI diagnosis, 1 doc download, lawyer search, basic calculator |
| 📦 Action Pack | 299฿ | Full action plan, unlimited docs, evidence upload, tax optimizer |
| ⭐ Case Plus | 999฿ | Case workspace, reminders, priority review, consultations |
| 🏢 SME Starter | 2,990/ด. | All docs, business contracts, team access, corporate tax, LINE |

---

## 5. 🛡️ Guardrails & Safety (P2)

### ไฟล์ที่ต้องสร้างใหม่:

| ไฟล์ | รายละเอียด |
|------|-----------|
| `lib/legal/guardrails.ts` | ➕ 7 "MUST NEVER" rules + banned phrase filter |
| `lib/legal/accuracy-checks.ts` | ➕ Thai legal accuracy checks (5 rules) |
| `lib/legal/version-tracker.ts` | ➕ Document/template version tracking |
| `lib/documents/review-workflow.ts` | ➕ Human review workflow |
| `components/trust/disclaimer-banner.tsx` | ➕ Disclaimer — ทุก AI result |
| `components/trust/citation-display.tsx` | ➕ Citation visibility |

### 7 "MUST NEVER" Rules:

| # | กฎ |
|---|-----|
| 1 | ❌ ห้ามให้คำแนะนำทางกฎหมาย |
| 2 | ❌ ห้ามทำนายผลคดี |
| 3 | ❌ ห้ามแนะนำทนาย "ดีที่สุด" |
| 4 | ❌ ห้ามยื่นเอกสารแทนผู้ใช้ |
| 5 | ❌ ห้ามอ้างกฎหมายที่ไม่มีจริง (anti-hallucination) |
| 6 | ❌ ห้ามเก็บข้อมูลโดยไม่มี consent |
| 7 | ❌ ห้ามใช้ข้อมูล train model |

---

## ⏱️ Timeline — 5 Weeks

| Week | Focus | ชม. |
|:---:|-------|:---:|
| 1 | 🔴 P0: 6→12 Categories + Fear Calibration + Sources | 20 |
| 2 | 📄 P1: Business Docs — Merge Engine + 3 หมวดแรก | 15 |
| 3 | 📄 P1: Business Docs — ต่ออีก 5 หมวด + UI | 15 |
| 4 | 💰 P1: Tax Module + 💳 Free/Paid | 25 |
| 5 | 🛡️ P2: Guardrails + Testing + Launch Prep | 10 |
| **รวม** | | **~85** |
