# 📊 LegalAI Thailand — หัวข้อหลัก + หัวข้อย่อย (Complete Breakdown)

> สถานะ: 9 สิงหาคม 2569 | 35 หัวข้อหลัก · 180+ หัวข้อย่อย

---

## 🔴 1. AI Diagnosis 12 หมวด — 48 คำถาม

- **1.1** labour — ถูกเลิกจ้าง, บังคับลาออก, ค้างจ่าย, เงื่อนไขไม่เป็นธรรม (4 คำถาม)
- **1.2** consumer — สินค้าไม่ตรงปก, ชำรุด, ไม่ได้รับ, บริการไม่เป็นธรรม (4 คำถาม)
- **1.3** debt — ถูกทวงหนี้, ต้องการทวงหนี้, ดอกเบี้ยนอกระบบ, ถูกคุกคาม (4 คำถาม)
- **1.4** housing — บอกเลิกสัญญา, ไม่คืนมัดจำ, ไม่จ่ายค่าเช่า, พิพาทสภาพทรัพย์ (4 คำถาม)
- **1.5** family — หย่า, ปกครองบุตร, มรดก, คู่สมรสนอกใจ (4 คำถาม)
- **1.6** accident — รถยนต์, มอเตอร์ไซค์, บาดเจ็บสาธารณะ, ชนทรัพย์สิน (4 คำถาม)
- **1.7** online_fraud — ซื้อของไม่ได้ของ, Call Center, แอปกู้เถื่อน, Romance Scam, แชร์ลูกโซ่ (5 ตัวเลือก)
- **1.8** crime — ทำร้าย, ลักทรัพย์, ข่มขืน, ขู่กรรโชก (4 คำถาม)
- **1.9** government — ขอทะเบียนไม่ได้, รัฐละเมิด, ร้องเรียนไม่ตอบ, เวนคืน (4 คำถาม)
- **1.10** insurance — เคลมรถ, เคลมสุขภาพ, ยกเลิกกรมธรรม์, ไม่จ่ายตามสัญญา (4 คำถาม)
- **1.11** defamation — ด่าโซเชียล, ภาพหลุด, ใส่ความ, ข้อมูลรั่วไหล (4 คำถาม)
- **1.12** property — ที่ดินบุกรุก, แนวเขต, ซื้อขายไม่ได้, มรดกที่ดิน, โฉนดหาย (5 ตัวเลือก)
- **1.13** Fear Calibration — panic/urgent/concerned/planning (4 ระดับ)
- **1.14** Diagnosis Wizard — intake → loading → error states
- **1.15** AI Analysis — DeepSeek response, citations, evidence readiness

## 📋 2. 45 ปัญหาย่อย — Category Detail Pages

- **2.1** online_fraud (5): ซื้อของไม่ได้ของ, Call Center, แอปกู้เถื่อน, Romance Scam, แชร์ลูกโซ่
- **2.2** crime (4): ทำร้าย, ลักทรัพย์, ข่มขืน, ขู่กรรโชก
- **2.3** defamation (4): ด่าโซเชียล, ภาพหลุด, ใส่ความ, PDPA
- **2.4** insurance (3): เคลมรถ, เคลมสุขภาพ, ยกเลิกกรมธรรม์
- **2.5** government (3): ขอทะเบียน, รัฐละเมิด, ร้องเรียนไม่ตอบ
- **2.6** property (5): บุกรุก, แนวเขต, ซื้อขายไม่ได้, มรดก, โฉนดหาย
- **2.7** labour (4): เลิกจ้าง, ค้างจ่าย, บังคับลาออก, เงื่อนไขไม่เป็นธรรม
- **2.8** consumer (4): ไม่ตรงปก, ไม่ได้รับ, อาหารเป็นพิษ, โฆษณาเกินจริง
- **2.9** debt (4): ทวงหนี้ข่มขู่, นอกระบบ, ล้มละลาย, Blacklist
- **2.10** housing (3): ไม่จ่ายค่าเช่า, ไม่คืนมัดจำ, ไล่ที่ไม่เป็นธรรม
- **2.11** family (5): หย่า, ปกครองบุตร, มรดก, นอกใจ, ทำร้ายครอบครัว
- **2.12** accident (3): รถยนต์, ชนแล้วหนี, บาดเจ็บสาหัส
- **2.13** แต่ละปัญหา: title + description + urgency badge + link to diagnosis
- **2.14** Diagnosis preview: แสดง 4 คำถามที่ AI จะถาม

## 📂 3. Category Detail Pages — 12 หน้า

- **3.1** /categories — browse all 12 หมวด
- **3.2** /categories/[category] — dynamic route (12 variations)
- **3.3** Section: ปัญหาที่พบบ่อย — card per problem with urgency
- **3.4** Section: AI จะถามคุณ — question preview
- **3.5** Section: กฎหมายที่เกี่ยวข้อง — sources from registry
- **3.6** Sidebar: ต้องการความช่วยเหลือ — search, documents, lawyers links
- **3.7** Sidebar: หมวดอื่นๆ — cross-navigation
- **3.8** CTA: เริ่มวิเคราะห์เคสของฉัน → /diagnosis?category=X

## 🔍 4. Search AI Dynamic

- **4.1** Search form with query parameter
- **4.2** Loading state — "AI กำลังวิเคราะห์..."
- **4.3** Result state — AI response with citations
- **4.4** Error state — fallback message + diagnosis link
- **4.5** Sort dropdown — เกี่ยวข้อง/ใหม่สุด/เก่าสุด
- **4.6** Business doc sidebar — matching categories
- **4.7** Article links — clickable
- **4.8** Topic tags — /search?q=topic
- **4.9** Disclaimer — "ผลค้นหาเป็นข้อมูลเบื้องต้น"
- **4.10** Share button — navigator.share / clipboard
- **4.11** Save button — toggle state

## 📜 5. 36 Legal Sources

- **5.1** labour: 3 sources (คุ้มครองแรงงาน, ศาลแรงงาน, ประกันสังคม)
- **5.2** consumer: 2 sources (คุ้มครองผู้บริโภค, วิธีพิจารณาคดีผู้บริโภค)
- **5.3** debt: 3 sources (ป.พ.พ., ทวงถามหนี้, ล้มละลาย)
- **5.4** housing: 1 source (เช่าทรัพย์)
- **5.5** family: 3 sources (ครอบครัว, มรดก, คุ้มครองความรุนแรง)
- **5.6** accident: 2 sources (จราจร, ละเมิด)
- **5.7** online_fraud: 4 sources (ฉ้อโกง, คอมพิวเตอร์, ปปง., สินเชื่อ)
- **5.8** crime: 5 sources (ทำร้าย, ข่มขืน, ลักทรัพย์, กรรโชก, ค่าตอบแทนผู้เสียหาย)
- **5.9** government: 3 sources (ศาลปกครอง, ละเมิดเจ้าหน้าที่, ทะเบียนราษฎร)
- **5.10** insurance: 3 sources (ประกันวินาศภัย, ประกันชีวิต, คปภ.)
- **5.11** defamation: 3 sources (หมิ่นประมาท, หมิ่นโฆษณา, PDPA)
- **5.12** property: 3 sources (ที่ดิน, ทรัพย์สิน, อาคารชุด)
- **5.13** Anti-hallucination: resolveSource() returns null for unknown IDs
- **5.14** LEGAL_SOURCE_VERSION = "sources-v2"

## 📋 6. Case Management

- **6.1** /cases — case list with filter tabs (ทั้งหมด/กำลังดำเนินการ/รอเอกสาร/เสร็จสิ้น)
- **6.2** /cases/[caseId]/timeline — tabs (ภาพรวม/ไทม์ไลน์/หลักฐาน/เอกสาร), action steps
- **6.3** /cases/[caseId]/evidence — drag-drop upload, evidence checklist, readiness score
- **6.4** File-to-evidence linking — "เชื่อมโยง" button maps files to requirements
- **6.5** File validation — PDF/JPG/PNG/WebP, max 20MB

## 🔔 7. Notifications

- **7.1** Filter tabs — ทั้งหมด/เคสของฉัน/เอกสาร/ระบบ
- **7.2** Notification cards — tone (amber/blue/green/gray), icon, title, body, CTA
- **7.3** Mark all read button — toast feedback

## 💬 8. AI Assistant

- **8.1** Chat interface with DeepSeek AI
- **8.2** Typing indicator while AI thinks
- **8.3** Quick replies in welcome message
- **8.4** Suggested prompts (3 buttons)
- **8.5** SourceCitation display
- **8.6** Disclaimer "AI อาจให้ข้อมูลคลาดเคลื่อน"
- **8.7** Menu + "เปลี่ยน" button handlers

---

## 📄 9. 126 Document Templates — 10 Categories

- **9.1** อสังหาริมทรัพย์ (15): จะซื้อจะขาย, ซื้อขาย, ขายฝาก, ให้, มอบอำนาจ, จอง, ก่อสร้าง, สถาปนิก, ตกแต่ง, นายหน้า
- **9.2** สัญญาเช่า (17): เช่าบ้าน, คอนโด, ที่ดิน, สำนักงาน, พาณิชย์, รถ, อุปกรณ์, ใบเสร็จ
- **9.3** จัดตั้งธุรกิจ (14): บริคณห์สนธิ, หนังสือรับรอง, ห้างหุ้นส่วน, ผู้ถือหุ้น, รายงานประชุม, e-Meeting
- **9.4** สินเชื่อและการเงิน (12): กู้ยืม, ค้ำประกัน, จำนอง, เช่าซื้อ, ตั๋วสัญญาใช้เงิน
- **9.5** ครอบครัวและส่วนบุคคล (13): ก่อนสมรส, หย่า, พินัยกรรม, ยกให้, ปกครองบุตร, รับบุตรบุญธรรม
- **9.6** การจ้างงานและ HR (16): จ้างงาน, จ้างทำของ, NDA, Non-compete, สลิป, ประเมินผล
- **9.7** พาณิชยกรรม (14): ซื้อขายสินค้า, บริการ, ตัวแทน, MOU, ใบเสนอราคา, ใบแจ้งหนี้, PDPA
- **9.8** ยานพาหนะและการขนส่ง (8): ซื้อขายรถ, โอนทะเบียน, มอบอำนาจ, มอบฉันทะประกัน, เช่ารถ
- **9.9** การท่องเที่ยวและบริการ (9): เข้าพัก, ทัวร์, จอง, กรุ๊ปทัวร์, จัดเลี้ยง, อีเวนต์
- **9.10** ทรัพย์สินทางปัญญา (8): License, ลิขสิทธิ์, เครื่องหมายการค้า, สิทธิบัตร, NDA, แฟรนไชส์
- **9.11** Free vs Paid labeling — per template

## 📄 10. Document Category Pages

- **10.1** /documents/[category] — dynamic route (10 variations)
- **10.2** Real template lists — 8-17 items per category
- **10.3** Free/paid count summary in header
- **10.4** "เริ่มสร้าง →" button per template → /documents/create
- **10.5** Hover effects on template rows
- **10.6** Pill tone mapping per category color

## 📄 11. Document Editor

- **11.1** /documents/create — document creation page
- **11.2** Merge-field form — แทนที่ {ชื่อ}, {ที่อยู่}, {วันที่}
- **11.3** Live preview panel — แสดงผล real-time
- **11.4** Export buttons — PDF, TXT
- **11.5** Query params: template, name, category, paid, price

## 📄 12. Merge Engine

- **12.1** {{field}} replacement
- **12.2** Conditional blocks
- **12.3** Thai date formatting (พ.ศ.)
- **12.4** Thai currency formatting
- **12.5** Thai name and ID formatting
- **12.6** Batch merge
- **12.7** Template validation

---

## 💰 13. Tax Calculator

- **13.1** Income slider — 0-5,000,000 THB
- **13.2** 15 deduction toggles — interactive chips
- **13.3** Real-time tax calculation
- **13.4** Effective tax rate display
- **13.5** Savings tracker — "คุณประหยัดภาษีได้ X บาท"
- **13.6** 8 progressive brackets (0-35%) sidebar
- **13.7** Responsive layout — main + aside

## 🤖 14. Tax Optimizer

- **14.1** AI savings estimate card — "ประหยัดสูงสุด X บาท"
- **14.2** Plan recommendation — "RMF + SSF + ประกัน"
- **14.3** Deadline reminder — "31 ธ.ค."
- **14.4** AI analysis CTA button

## 📋 15. Filing Checklist

- **15.1** 6-step interactive checklist — checkboxes
- **15.2** Steps: ทวิ 50 → เอกสารลดหย่อน → ยอดเงินได้ → คำนวณ → ยื่นแบบ → เก็บหลักฐาน
- **15.3** efiling link — rd.go.th

---

## 👨‍⚖️ 16. Lawyer Marketplace

- **16.1** /lawyers — lawyer list
- **16.2** Filter chips — ทั้งหมด/แรงงาน/ครอบครัว/อสังหา/ผู้บริโภค/ออนไลน์วันนี้
- **16.3** Lawyer cards — name, specialties, experience, rating, price, online status
- **16.4** "♡ บันทึก" button — toggle + toast

## 👨‍⚖️ 17. Lawyer Detail Page

- **17.1** /lawyers/[id] — dynamic route
- **17.2** Profile — avatar, name, specialties (Thai labels), stats (rating, reviews, price)
- **17.3** Mock reviews — 3 reviews with star ratings
- **17.4** Service scope breakdown
- **17.5** Booking widget — 3-step: select → confirm → done
- **17.6** Date picker — next 7 days
- **17.7** Time slots — 16 slots (9:00-17:00, 30-min)
- **17.8** Optional notes field
- **17.9** Confirmation summary

## 📎 18. Evidence Upload

- **18.1** Drag-and-drop zone — visual feedback (blue highlight)
- **18.2** Click-to-browse fallback
- **18.3** File validation — PDF/JPG/PNG/WebP, max 20MB
- **18.4** Uploaded files list — icon, name, size, remove
- **18.5** "เชื่อมโยง" button — map files to evidence checklist
- **18.6** Readiness score ring — X/Y items provided

---

## 💳 19. Free/Paid Tiers

- **19.1** Free — 0฿: 3 diagnoses, 1 doc, 1 consult
- **19.2** Action Pack — 299฿: unlimited diagnoses, docs, evidence, 1 consult, tax optimizer
- **19.3** Case Plus — 999฿: reminders, priority review, 3 consults, LINE
- **19.4** SME Starter — 2,990฿/mo: business docs, team 5, corporate tax, unlimited consults
- **19.5** 10 feature gates — FEATURE_GATES mapping
- **19.6** checkFeatureAccess() function
- **19.7** getNextPackage() — upgrade path
- **19.8** Limits matrix — per-tier max numbers

## 💳 20. Pricing Page

- **20.1** /pricing — pricing page
- **20.2** 4 tier cards — highlighted SME Starter
- **20.3** Feature comparison table — 11 rows
- **20.4** FAQ section — 3 questions (expandable)
- **20.5** CTA buttons — per tier

---

## 📋 21. Terms of Service

- **21.1** /terms — full page
- **21.2** 9 sections: การยอมรับ, ขอบเขต, ข้อจำกัด, การใช้เหมาะสม, ระงับบัญชี, ทรัพย์สินทางปัญญา, เปลี่ยนแปลง, กฎหมาย, ติดต่อ
- **21.3** Warning box — "ไม่ใช่คำแนะนำทางกฎหมาย"

## 🔒 22. Privacy Policy

- **22.1** /privacy — full page
- **22.2** 8 sections: ข้อมูล, AI, เก็บรักษา, เปิดเผย, สิทธิ PDPA, คุกกี้, ติดต่อ, เปลี่ยนแปลง
- **22.3** PDPA rights table — 5 rights
- **22.4** Data table — ประเภท, ตัวอย่าง, วัตถุประสงค์

---

## 🛡️ 23. 7 Guardrails

- **23.1** no-legal-advice — ห้ามให้คำแนะนำทางกฎหมาย
- **23.2** no-outcome-prediction — ห้ามทำนายผลคดี
- **23.3** no-lawyer-ranking — ห้ามจัดอันดับทนาย
- **23.4** no-court-filing — ห้ามยื่นเอกสารแทนผู้ใช้
- **23.5** no-fabricated-sources — ห้ามอ้างกฎหมายที่ไม่มีจริง
- **23.6** no-data-without-consent — PDPA compliance
- **23.7** disclaimer-required — ทุก AI result ต้องมี disclaimer
- **23.8** checkGuardrails() function
- **23.9** Banned RegExp patterns per rule

## ✅ 24. Thai Accuracy Checks

- **24.1** checkBEYear — ตรวจสอบปี พ.ศ.
- **24.2** checkFormalLanguage — ตรวจสอบภาษาทางการ
- **24.3** checkRequiredTerms — ตรวจสอบคำสำคัญ
- **24.4** checkPlaceholders — ตรวจสอบช่องว่างที่ยังไม่ได้แทนที่
- **24.5** runAll() — run all checks

---

## 🏠 25. Home Page

- **25.1** Welcome section — user greeting + date
- **25.2** Search box — with popular searches
- **25.3** Category grid — 12 หมวด → /categories/[id]
- **25.4** Action cards — 6 cards (diagnosis, documents, lawyers, tax, pricing, categories)
- **25.5** Case preview — in-progress case card
- **25.6** Trust strip — security message
- **25.7** Prototype data notice

## 👤 26. Profile Page

- **26.1** Profile card — avatar, name, email, package pill
- **26.2** Settings sidebar — 6 tabs with active state
- **26.3** Personal tab — name, surname, email, phone form
- **26.4** Notifications tab — LINE toggle, email toggle
- **26.5** Privacy tab — AI consent toggle, data export, data delete
- **26.6** Display tab — language, font size
- **26.7** Package tab — current package, upgrade CTA
- **26.8** Help tab — FAQ + contact

## 🏛️ 27. Admin Dashboard

- **27.1** Stats row — users, lawyers, cases, revenue
- **27.2** Recent cases table
- **27.3** Top lawyers list
- **27.4** Revenue overview

## 🚀 28. Onboarding

- **28.1** 5-step flow
- **28.2** Step 1: Accept terms + privacy (checkbox)
- **28.3** Step 2: Email verification (NEW)
- **28.4** Step 3: Personal info
- **28.5** Step 4: Preferences
- **28.6** Step 5: Profile setup

---

## 🐛 29. 17 Bug Fixes

- **29.1** P0: /terms page (was 404)
- **29.2** P0: /privacy page (was 404)
- **29.3** P0: Case tabs href="#" → real routes
- **29.4** P0: Profile settings tabs → useState
- **29.5** P0: AI consent toggle + data rights
- **29.6** P1: Search sort dropdown → onClick
- **29.7** P1: Search share button → navigator.share
- **29.8** P1: Search article links → clickable
- **29.9** P1: Search topic tags → /search?q=
- **29.10** P1: Filter tabs → 3 pages (cases/notifications/lawyers)
- **29.11** P1: Disclaimers → 3 pages
- **29.12** P1: Categories valid in assistant API → 6→12
- **29.13** P2: Mark all read → toast
- **29.14** P2: Save lawyer → toast
- **29.15** P2: Assistant menu → handlers
- **29.16** P2: Search static → dynamic AI-powered
- **29.17** P2: Business doc categories in search sidebar

---

## 📚 30. 22 Human Drives Framework

- **30.1** 18 positive drives — อยู่รอด, ผลประโยชน์, การยอมรับ, สถานะ, ความสัมพันธ์, ความรัก, อำนาจ, ข่ม, อิสระ, ความเก่ง, ชัยชนะ, ความแน่นอน, ตื่นเต้น, ยุติธรรม, ดูแล, อัตลักษณ์, ความหมาย, มรดก
- **30.2** 4 negative drives — หลีกเลี่ยงอับอาย, สูญเสีย, แก้แค้น, พิสูจน์ตนเอง
- **30.3** 6 แกนใหญ่ — มี, เป็น, ได้รับ, ควบคุม, หลีกหนี, ส่งต่อ
- **30.4** 6 จุดสังเกต — พูดอะไร, โกรธอะไร, กลัวเสียอะไร, ใช้เงินกับอะไร, อิจฉาใคร, ภูมิใจอะไร
- **30.5** 9 คำถามเจาะลึก — "เรื่องนี้สำคัญกับคุณเพราะอะไร?"

## 📊 31. Consumer Insight

- **31.1** Buying psychology — scarcity, social proof, anchoring, loss aversion, decoy, reciprocity, framing
- **31.2** Group psychology — herd, tribe, bandwagon
- **31.3** Consumer segmentation — demographic, psychographic, behavioral, JTBD
- **31.4** Product-market fit — SWOT, Porter, Value Proposition

## 📊 32. Revenue Forecast

- **32.1** 7 revenue streams — unit economics per stream
- **32.2** 5-year projections — Y0-Y5 (0.34M → 416M)
- **32.3** User/lawyer/client growth projections
- **32.4** Cost structure — headcount 11→155
- **32.5** Break-even analysis — monthly M16-M18, cumulative M24-M28
- **32.6** 3 scenarios — base (416M) / bull (1,030M) / bear (233M)

## 🏢 33. Platform Research

- **33.1** Harvey.ai (EN+TH) — 10 modules, 714 lines
- **33.2** Clio (EN+TH) — 10 modules, 888 lines
- **33.3** 9 Platforms (EN+TH) — MyCase, PracticePanther, Filevine, Relativity, iManage, LexisNexis, Westlaw, Smokeball, Rocket Matter
- **33.4** Lawyer Platform Analysis — 3 personas, 10 features, Thai market

## 📋 34. Master Blueprint

- **34.1** Executive Summary
- **34.2** Market Analysis
- **34.3** Consumer Platform
- **34.4** Lawyer Platform
- **34.5** Revenue Model
- **34.6** Technology & AI
- **34.7** UX/UI Design System
- **34.8** Go-to-Market Strategy
- **34.9** Team & Resources
- **34.10** Risk & Mitigation

## 🧠 35. Thinking System Skill

- **35.1** Cognitive Loop — 6 steps
- **35.2** 5 Thinking Methods — User-Pain-First, Edge-Case, Ecosystem, Framework→Execution, Bias-for-Action
- **35.3** Strengths — First-Principles, Victim-Perspective, Speed
- **35.4** Watch-Outs — Scope Creep, Burnout, Perfectionism
- **35.5** How to Brief Bess — 5 steps
- **35.6** GitHub: [nutsdevs-thinking-system](https://github.com/Kaewpanao/LegalAI-Thailand/blob/master/skills/nutsdevs-thinking-system/SKILL.md)

---

| รวม | **35 หัวข้อหลัก · 180+ หัวข้อย่อย** |
|------|:---:|
