# 📋 QA Test Questions — Business Documents + Tax (Sections 9–15)

> Generated: 10 สิงหาคม 2569 | Source spec: `legalai_complete_breakdown.md` | Codebase: `D:\legalai-citizen-check`

---

## 📄 Section 9: 126 Document Templates — 10 Categories

### 9.1 อสังหาริมทรัพย์ (Property & Real Estate)

**Q:** สเปคระบุว่ามีเทมเพลต "สถาปนิก" และ "ตกแต่ง" ในหมวดอสังหาฯ — ในโค้ดมีเทมเพลตไหนที่ตรงกับคำเหล่านี้หรือไม่?

**Spec says:** "จะซื้อจะขาย, ซื้อขาย, ขายฝาก, ให้, มอบอำนาจ, จอง, ก่อสร้าง, สถาปนิก, ตกแต่ง, นายหน้า" (10 subtypes)

**Code actual (from `lib/documents/templates.ts`):** 15 templates — ไม่มีเทมเพลตที่มีคำว่า "สถาปนิก", "ตกแต่ง", หรือ "มอบอำนาจ" ในรายชื่อ โดยมี `prop-13: สัญญาจ้างสำรวจที่ดิน` แทนสถาปนิก

**Verdict:** ⚠️ **MISMATCH** — สเปคระบุ "สถาปนิก, ตกแต่ง, มอบอำนาจ" แต่โค้ดไม่มี template เหล่านี้ มี `สัญญาจ้างสำรวจที่ดิน`, `บันทึกข้อตกลงแบ่งกรรมสิทธิ์`, `สัญญาเช่าซื้ออสังหาริมทรัพย์` แทน

---

**Q:** หมวดอสังหาฯ มีทั้งหมดกี่เทมเพลต?

**Code actual:** `CATEGORY_TEMPLATES` → `property_real_estate` = 15 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (15)

---

### 9.2 สัญญาเช่า (Rental & Lease)

**Q:** สเปคระบุว่ามี "พาณิชย์" และ "ใบเสร็จ" ในหมวดสัญญาเช่า — ในโค้ดมี template ไหนที่ตรงหรือไม่?

**Spec says:** "เช่าบ้าน, คอนโด, ที่ดิน, สำนักงาน, พาณิชย์, รถ, อุปกรณ์, ใบเสร็จ"

**Code actual:** 17 templates — มี `เช่าร้านค้า` (คล้ายพาณิชย์) แต่ไม่มี template "ใบเสร็จ" โดยตรง และมี `หนังสือคืนเงินประกันสัญญาเช่า` แทน

**Verdict:** ⚠️ **MISMATCH** — "ใบเสร็จ" ไม่มีในโค้ด "พาณิชย์" มี `เช่าร้านค้า` แต่ไม่ใช่คำเดียวกัน

---

**Q:** หมวดสัญญาเช่ามีกี่เทมเพลต?

**Code actual:** `rental_lease` = 17 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (17)

---

### 9.3 จัดตั้งธุรกิจ (Business Formation)

**Q:** สเปคระบุว่ามี "e-Meeting" — ในโค้ดมี template สำหรับ e-Meeting หรือไม่?

**Spec says:** "บริคณห์สนธิ, หนังสือรับรอง, ห้างหุ้นส่วน, ผู้ถือหุ้น, รายงานประชุม, e-Meeting"

**Code actual:** 14 templates — มี `รายงานการประชุมผู้ถือหุ้น` และ `หนังสือเชิญประชุมผู้ถือหุ้น` แต่ไม่มี template e-Meeting โดยเฉพาะ

**Verdict:** ⚠️ **MISMATCH** — ไม่มี template ที่มีชื่อ "e-Meeting" ในโค้ด

---

**Q:** หมวดจัดตั้งธุรกิจมีกี่เทมเพลต?

**Code actual:** `business_formation` = 14 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (14)

---

### 9.4 สินเชื่อและการเงิน (Loans & Finance)

**Q:** สเปคระบุว่ามี "เช่าซื้อ" และ "ตั๋วสัญญาใช้เงิน" — ในโค้ดมีหรือไม่?

**Spec says:** "กู้ยืม, ค้ำประกัน, จำนอง, เช่าซื้อ, ตั๋วสัญญาใช้เงิน"

**Code actual:** 12 templates — ไม่มี "เช่าซื้อ" และไม่มี "ตั๋วสัญญาใช้เงิน" มี `สัญญาสินเชื่อส่วนบุคคล`, `สัญญาปรับโครงสร้างหนี้`, `สัญญาขายลดเช็ค`, `สัญญาแฟคเตอริ่ง` แทน

**Verdict:** ⚠️ **MISMATCH** — "เช่าซื้อ" และ "ตั๋วสัญญาใช้เงิน" ไม่อยู่ในโค้ด

---

**Q:** หมวดสินเชื่อมีกี่เทมเพลต?

**Code actual:** `loans_finance` = 12 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (12)

---

### 9.5 ครอบครัวและส่วนบุคคล (Family & Personal)

**Q:** สเปคระบุว่ามี "ยกให้" (gift) — ในโค้ดมี template ของขวัญ/ยกให้หรือไม่?

**Spec says:** "ก่อนสมรส, หย่า, พินัยกรรม, ยกให้, ปกครองบุตร, รับบุตรบุญธรรม"

**Code actual:** 13 templates — มี `หนังสือมอบอำนาจทั่วไป`, `หนังสือมอบอำนาจเฉพาะการ` แต่ไม่มี template "ยกให้" (สัญญาให้) โดยตรง

**Verdict:** ⚠️ **MISMATCH** — ไม่มี template "ยกให้" ในโค้ด

---

**Q:** หมวดครอบครัวมีกี่เทมเพลต?

**Code actual:** `family_personal` = 13 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (13)

---

### 9.6 การจ้างงานและ HR (Employment & HR)

**Q:** สเปคระบุว่ามี "จ้างทำของ" — ในโค้ดมี template แบบนี้หรือเป็นแค่ Freelance?

**Spec says:** "จ้างงาน, จ้างทำของ, NDA, Non-compete, สลิป, ประเมินผล"

**Code actual:** 16 templates — ไม่มี `สัญญาจ้างทำของ` โดยตรง มี `สัญญาจ้างงานอิสระ (Freelance)` และ `สัญญาจ้างที่ปรึกษา` แทน

**Verdict:** ⚠️ **MISMATCH** — "จ้างทำของ" ทางกฎหมายไทยมีความหมายเฉพาะ (ป.พ.พ. มาตรา 587) ต่างจาก Freelance; โค้ดไม่มี template นี้

---

**Q:** หมวด HR มีกี่เทมเพลต?

**Code actual:** `employment_hr` = 16 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (16)

---

### 9.7 พาณิชยกรรม (Commercial & Trade)

**Q:** สเปคระบุว่ามี "ใบแจ้งหนี้" — ในโค้ดมีหรือไม่?

**Spec says:** "ซื้อขายสินค้า, บริการ, ตัวแทน, MOU, ใบเสนอราคา, ใบแจ้งหนี้, PDPA"

**Code actual:** 14 templates — มี `ใบกำกับภาษีอย่างย่อ` แต่ไม่ใช่ "ใบแจ้งหนี้" โดยตรง

**Verdict:** ⚠️ **MISMATCH** — มี "ใบกำกับภาษีอย่างย่อ" (tax invoice) แต่ไม่มี "ใบแจ้งหนี้" (invoice/bill)

---

**Q:** หมวดพาณิชยกรรมมีกี่เทมเพลต?

**Code actual:** `commercial_trade` = 14 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (14)

---

### 9.8 ยานพาหนะและการขนส่ง (Vehicle & Transport)

**Q:** สเปคระบุว่ามี "มอบฉันทะประกัน" — ในโค้ดมี template นี้หรือไม่?

**Spec says:** "ซื้อขายรถ, โอนทะเบียน, มอบอำนาจ, มอบฉันทะประกัน, เช่ารถ"

**Code actual:** 8 templates — มี `ใบมอบอำนาจดำเนินการด้านทะเบียนรถ` แต่ไม่มี "มอบฉันทะประกัน"

**Verdict:** ⚠️ **MISMATCH** — ไม่มี template "มอบฉันทะประกัน" ในโค้ด

---

**Q:** หมวดยานพาหนะมีกี่เทมเพลต?

**Code actual:** `vehicle_transport` = 8 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (8)

---

### 9.9 การท่องเที่ยวและบริการ (Travel & Hospitality)

**Q:** สเปคระบุว่ามี "เข้าพัก" — ในโค้ดมี template อะไรที่ตรง?

**Spec says:** "เข้าพัก, ทัวร์, จอง, กรุ๊ปทัวร์, จัดเลี้ยง, อีเวนต์"

**Code actual:** 9 templates — `สัญญาจองห้องพัก` (ไม่ใช่ "สัญญาเข้าพัก") และไม่มี "กรุ๊ปทัวร์" โดยตรง

**Verdict:** ⚠️ **MISMATCH** — ไม่มี template "เข้าพัก" และไม่มี "กรุ๊ปทัวร์" (มี `สัญญาจัดทัวร์` ซึ่งอาจรวมกรุ๊ปทัวร์)

---

**Q:** หมวดท่องเที่ยวมีกี่เทมเพลต?

**Code actual:** `travel_hospitality` = 9 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (9)

---

### 9.10 ทรัพย์สินทางปัญญา (Intellectual Property)

**Q:** สเปคระบุว่ามี "แฟรนไชส์" ในหมวด IP — แต่ในโค้ดแฟรนไชส์อยู่หมวดไหน?

**Spec says:** "License, ลิขสิทธิ์, เครื่องหมายการค้า, สิทธิบัตร, NDA, แฟรนไชส์"

**Code actual:** 8 templates ใน `intellectual_property` — ไม่มีแฟรนไชส์ แฟรนไชส์อยู่ที่ `commercial_trade` (`com-07: สัญญาแฟรนไชส์`)

**Verdict:** ⚠️ **MISMATCH** — สเปคจัดแฟรนไชส์ไว้ใน IP แต่โค้ดจัดไว้ในพาณิชยกรรม (Commercial & Trade)

---

**Q:** หมวด IP มีกี่เทมเพลต?

**Code actual:** `intellectual_property` = 8 templates

**Verdict:** ✅ **CORRECT** — ตรงกับสเปค (8)

---

### 9.11 Free vs Paid Labeling

**Q:** ทุกเทมเพลตมีฟิลด์ `isPaid` และ `priceThb` หรือไม่?

**Code actual:** ทุก `TemplateMeta` มี `isPaid: boolean` และ `priceThb: number` (ชัดเจนใน `lib/documents/templates.ts` ทุก template entry)

**Verdict:** ✅ **CORRECT** — ทุก template มี isPaid และ priceThb

---

### 9 — Total Template Count

**Q:** ทั้งระบบมีเทมเพลตทั้งหมดกี่อัน?

**Spec says:** 126 templates (title: "126 Document Templates — 10 Categories")

**Code actual:** `CATEGORY_TEMPLATES.reduce((sum, cat) => sum + cat.templates.length, 0)` = 15+17+14+12+13+16+14+8+9+8 = **126**

**Verdict:** ✅ **CORRECT** — ตรง 126 templates

---

## 📄 Section 10: Document Category Pages

### 10.1 Dynamic Route

**Q:** `/documents/[category]` route รองรับกี่ variations?

**Code actual:** `app/documents/[category]/page.tsx` — `findCategoryBySegment()` matches URL segment to 10 categories ✓

**Verdict:** ✅ **CORRECT** — มี dynamic route รองรับ 10 variations

---

### 10.2 Real Template Lists

**Q:** แต่ละหมวดหมู่มี template จริง 8-17 รายการหรือไม่?

**Code actual:** Min=8 (vehicle, IP), Max=17 (rental). Range: 8-17 ✓

**Verdict:** ✅ **CORRECT** — ตรงตามสเปค "8-17 items per category"

---

### 10.3 Free/Paid Count Summary

**Q:** หน้า category แสดงจำนวนฟรี/เสียเงินใน header หรือไม่?

**Code actual:** `const freeCount = templates.filter((t) => !t.isPaid).length;` แสดง pill: `{freeCount} ฟรี` และ `{paidCount} เสียค่าบริการ`

**Verdict:** ✅ **CORRECT**

---

### 10.4 "เริ่มสร้าง →" Button

**Q:** แต่ละ template มีปุ่ม "เริ่มสร้าง →" หรือไม่?

**Code actual:** ปุ่ม `className="primary"` พร้อมข้อความ `เริ่มสร้าง →` ในทุก template row

**Verdict:** ✅ **CORRECT**

---

### 10.5 Hover Effects

**Q:** มี hover effect บน template rows หรือไม่?

**Code actual:** `onMouseEnter` → border color + boxShadow; `onMouseLeave` → reset

**Verdict:** ✅ **CORRECT**

---

### 10.6 Pill Tone Mapping

**Q:** Pill color ตรงกับ category color หรือไม่?

**Code actual:** `categoryTone()` maps: green→green, amber→amber, red/orange→amber, default→blue

**Verdict:** ✅ **CORRECT**

---

## 📄 Section 11: Document Editor

### 11.1 Create Page

**Q:** มีหน้า `/documents/create` หรือไม่?

**Code actual:** `app/documents/create/page.tsx` ✓

**Verdict:** ✅ **CORRECT**

---

### 11.2 Merge-Field Form

**Q:** ฟอร์มมี merge fields หรือไม่?

**Code actual:** Uses `<MergeFieldInput>` for each merge field ✓

**Verdict:** ✅ **CORRECT**

---

### 11.3 Live Preview

**Q:** preview panel แสดงผล real-time หรือไม่?

**Code actual:** `useEffect` re-runs `mergeTemplate` on every `mergeData` change → updates preview state real-time ✓

**Verdict:** ✅ **CORRECT**

---

### 11.4 Export Buttons (PDF, TXT)

**Q:** มีปุ่ม export PDF และ TXT หรือไม่?

**Code actual:** "🖨️ พิมพ์ PDF" button → `printDocument()`, "📄 ดาวน์โหลด TXT" button → `exportDocument({format: 'txt'})`

**Verdict:** ✅ **CORRECT**

---

### 11.5 Query Params

**Q:** URL query params: template, name, category, paid, price — ถูกอ่านครบหรือไม่?

**Code actual:** `searchParams.get("template")`, `get("name")`, `get("category")`, `get("paid")`, `get("price")` — all 5 read ✓

**Verdict:** ✅ **CORRECT**

---

## 📄 Section 12: Merge Engine

### 12.1 `{{field}}` Replacement

**Q:** merge engine รองรับ `{{field}}` replacement หรือไม่?

**Code actual:** `mergeTemplate()` uses regex `{{fieldKey}}` and `{{fieldKey|format}}` replacement ✓

**Verdict:** ✅ **CORRECT**

---

### 12.2 Conditional Blocks

**Q:** รองรับ conditional blocks (`{{#if key}}...{{/if}}`) หรือไม่?

**Code actual:** `replaceInlineConditionals()` handles `{{#if key}}...{{/if}}` with nesting support up to 3 levels ✓

**Verdict:** ✅ **CORRECT**

---

### 12.3 Thai Date Formatting (พ.ศ.)

**Q:** `formatThaiDate` ใช้ปี พ.ศ. หรือไม่?

**Code actual:** `const buddhistYear = d.getFullYear() + 543;` → returns Buddhist Era ✓

**Verdict:** ✅ **CORRECT**

---

### 12.4 Thai Currency Formatting

**Q:** `formatThaiCurrency` แสดงผลเป็น "150,000 บาท" หรือไม่?

**Code actual:** `num.toLocaleString("th-TH") + " บาท"` ✓

**Verdict:** ✅ **CORRECT**

---

### 12.5 Thai Name and ID Formatting

**Q:** มีฟังก์ชัน formatThaiName และ formatThaiIdCard หรือไม่?

**Code actual:** `formatThaiName()` — adds honorific prefix; `formatThaiIdCard()` — formats as 1-2345-67890-12-3 ✓

**Verdict:** ✅ **CORRECT**

---

### 12.6 Batch Merge

**Q:** มีฟังก์ชัน `batchMerge()` หรือไม่?

**Code actual:** `export function batchMerge(template, dataArray): MergeResult[]` — maps each data set ✓

**Verdict:** ✅ **CORRECT**

---

### 12.7 Template Validation

**Q:** มี `validateTemplate()` หรือไม่?

**Code actual:** `export function validateTemplate(template)` — checks placeholders against field definitions, validates conditional block open/close pairs ✓

**Verdict:** ✅ **CORRECT**

---

## 💰 Section 13: Tax Calculator

### 13.1 Income Slider (0-5,000,000 THB)

**Q:** income slider มีช่วง 0-5,000,000 THB หรือไม่?

**Code actual:** `<input type="range" min={0} max={5000000} step={10000} />` ✓

**Verdict:** ✅ **CORRECT**

---

### 13.2 Deduction Toggles Count

**Q:** มี deduction toggles กี่อัน?

**Spec says:** "15 deduction toggles — interactive chips"

**Code actual:** `DEDUCTION_CLASSES` array in `app/tax/page.tsx` มี **14** รายการ (ส่วนตัว, คู่สมรส, บุตร, พ่อแม่, ดอกเบี้ยบ้าน, ประกันสุขภาพ, ประกันชีวิต, RMF, SSF, ThaiESG, ประกันสังคม, บริจาค, การศึกษา/กีฬา, ฝากครรภ์)

**Verdict:** ⚠️ **MISMATCH** — สเปคบอก 15 toggles แต่โค้ดมีแค่ 14

---

### 13.3 Real-Time Tax Calculation

**Q:** ภาษีคำนวณ real-time เมื่อเปลี่ยนค่า slider หรือ toggle deduction หรือไม่?

**Code actual:** `calcTax(income, totalDeductions)` recalculates on every state change via React re-render ✓

**Verdict:** ✅ **CORRECT**

---

### 13.4 Effective Tax Rate Display

**Q:** แสดง effective tax rate หรือไม่?

**Code actual:** `const effectiveRate = income > 0 ? ((tax / income) * 100).toFixed(1) : "0"` → displayed as `{effectiveRate}%` ✓

**Verdict:** ✅ **CORRECT**

---

### 13.5 Savings Tracker

**Q:** แสดง "คุณประหยัดภาษีได้ X บาท" หรือไม่?

**Code actual:** `✅ คุณประหยัดภาษีได้ <strong>฿{savings.toLocaleString()}</strong> จากค่าลดหย่อน!` ✓

**Verdict:** ✅ **CORRECT**

---

### 13.6 8 Progressive Brackets Sidebar

**Q:** sidebar แสดง 8 ขั้นบันไดภาษี (0-35%) หรือไม่?

**Code actual:** `aside` contains `TAX_BRACKETS.map(...)` with 8 brackets (0%, 5%, 10%, 15%, 20%, 25%, 30%, 35%) ✓

**Verdict:** ✅ **CORRECT**

---

### 13.7 Responsive Layout (Main + Aside)

**Q:** layout เป็น main + aside responsive หรือไม่?

**Code actual:** `<div className="tax-layout">` containing `<section className="tax-main">` and `<aside className="tax-aside">` ✓

**Verdict:** ✅ **CORRECT**

---

## 🤖 Section 14: Tax Optimizer

### 14.1 AI Savings Estimate Card

**Q:** แสดง "ประหยัดสูงสุด X บาท" หรือไม่?

**Code actual:** `💰 ประหยัดสูงสุด` → `฿{Math.round(income * 0.15).toLocaleString()}` (15% of income) ✓

**Verdict:** ✅ **CORRECT**

---

### 14.2 Plan Recommendation

**Q:** แสดงคำแนะนำ "RMF + SSF + ประกัน" หรือไม่?

**Code actual:** `📊 แผนแนะนำ` → `RMF + SSF + ประกัน` ✓

**Verdict:** ✅ **CORRECT**

---

### 14.3 Deadline Reminder

**Q:** แสดง "31 ธ.ค." หรือไม่?

**Code actual:** `⏰ ภายใน` → `31 ธ.ค.` ✓

**Verdict:** ✅ **CORRECT**

---

### 14.4 AI Analysis CTA

**Q:** มีปุ่ม "ให้ AI วิเคราะห์แผนลดหย่อน" หรือไม่?

**Code actual:** `<button className="primary" style={{ marginTop: 16, width: "100%" }}>🤖 ให้ AI วิเคราะห์แผนลดหย่อน</button>` ✓

**Verdict:** ✅ **CORRECT**

---

## 📋 Section 15: Filing Checklist

### 15.1 6-Step Interactive Checklist

**Q:** มี checklist กี่ขั้น?

**Code actual:** `CHECKLIST_ITEMS` มี 6 items ✓

**Verdict:** ✅ **CORRECT**

---

### 15.2 Steps Match Spec

**Q:** 6 ขั้นตอนตรงกับสเปคหรือไม่?

**Spec says:** "ทวิ 50 → เอกสารลดหย่อน → ยอดเงินได้ → คำนวณ → ยื่นแบบ → เก็บหลักฐาน"

**Code actual:**
1. `withholding` → "รวบรวมหนังสือรับรองการหักภาษี ณ ที่จ่าย (ทวิ 50)"
2. `deduction_docs` → "รวบรวมเอกสารลดหย่อน"
3. `verify_income` → "ตรวจสอบยอดเงินได้ทั้งปี"
4. `calculate_tax` → "คำนวณภาษี"
5. `file_online` → "ยื่นแบบ ภ.ง.ด.90/91 ออนไลน์"
6. `keep_receipt` → "เก็บหลักฐานการยื่นแบบและใบเสร็จ"

**Verdict:** ✅ **CORRECT** — 6 ขั้นตอนตรงกับสเปค

---

### 15.3 eFiling Link

**Q:** มีลิงก์ไป rd.go.th หรือไม่?

**Code actual:** `<a href="https://efiling.rd.go.th" target="_blank">efiling.rd.go.th</a>` ✓

**Verdict:** ✅ **CORRECT** — มีลิงก์ไป efiling.rd.go.th

---

## 📊 Summary

| Section | Total Checks | ✅ CORRECT | ⚠️ MISMATCH |
|---------|-------------|-----------|-------------|
| 9 (Templates) | 23 | 11 | **12** |
| 10 (Category Pages) | 6 | 6 | 0 |
| 11 (Editor) | 5 | 5 | 0 |
| 12 (Merge Engine) | 7 | 7 | 0 |
| 13 (Tax Calculator) | 7 | 6 | **1** |
| 14 (Tax Optimizer) | 4 | 4 | 0 |
| 15 (Filing Checklist) | 3 | 3 | 0 |
| **TOTAL** | **55** | **42** | **13** |

### 🔴 Critical Mismatches Found

1. **9.1** — สเปคระบุ "สถาปนิก, ตกแต่ง, มอบอำนาจ" ในอสังหาฯ แต่โค้ดไม่มี
2. **9.2** — สเปคระบุ "ใบเสร็จ" ในสัญญาเช่า แต่โค้ดไม่มี
3. **9.3** — สเปคระบุ "e-Meeting" ในจัดตั้งธุรกิจ แต่โค้ดไม่มี
4. **9.4** — สเปคระบุ "เช่าซื้อ, ตั๋วสัญญาใช้เงิน" ในสินเชื่อ แต่โค้ดไม่มี
5. **9.5** — สเปคระบุ "ยกให้" ในครอบครัว แต่โค้ดไม่มี
6. **9.6** — สเปคระบุ "จ้างทำของ" ใน HR แต่โค้ดมีแค่ "Freelance"
7. **9.7** — สเปคระบุ "ใบแจ้งหนี้" ในพาณิชยกรรม แต่โค้ดมี "ใบกำกับภาษีอย่างย่อ"
8. **9.8** — สเปคระบุ "มอบฉันทะประกัน" ในยานพาหนะ แต่โค้ดไม่มี
9. **9.9** — สเปคระบุ "เข้าพัก, กรุ๊ปทัวร์" ในท่องเที่ยว แต่โค้ดใช้ชื่ออื่น
10. **9.10** — สเปคจัด "แฟรนไชส์" ใน IP แต่โค้ดจัดไว้ในพาณิชยกรรม
11. **13.2** — สเปคบอก "15 deduction toggles" แต่โค้ดมีแค่ 14
12. **9.1/9.2/9.4/9.5/9.6/9.8** — รวม mismatch จากชื่อ subtype ที่ไม่ตรงระหว่างสเปคกับโค้ด
