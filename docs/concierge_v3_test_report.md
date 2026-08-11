# 🧭 LegalAI Concierge V3 — Test Report + Implementation Checklist

> **Report Date:** 11 สิงหาคม 2569
> **Scope:** V2 → V3 Court Guide Integration — 15 enhancement sections across 47 flows
> **Sources:**
> - V2 Concierge Flows: `concierge_v2_cat1_6.md` (47 flows, 7,054 lines) + `concierge_v2_cat7_12.md` (5,637 lines)
> - Court Guide Integration Plan: `concierge_court_guide_integration.md` (15 sections)
> - Real User Questions: `qa_135_real_questions.md` (135 questions, 12 categories)
> - Gold Standard: `concierge_format_test.md` (revenge porn walkthrough)

---

## SECTION A: IMPLEMENTATION CHECKLIST

> **Status Key:** ✅ DONE | ⚠️ PARTIAL | ❌ NOT STARTED | 🔜 PLANNED

### Priority 1: Universal Template Insertions (HIGH impact, LOW effort)

| # | Improvement | Phase | Status | Evidence |
|---|------------|-------|--------|----------|
| 1 | **Court Behavior Rules** — ห้ามนำอาวุธ/ยาเสพติด, ห้ามอัดเสียง/ถ่ายรูป, ห้ามใช้มือถือในศาล | Phase 7 | ❌ | V2 flows have NO court behavior rules anywhere. Integration plan Section 1 specifies insertion into Phase 7 template |
| 2 | **Blue-Shirt Receptionists (เสื้อฟ้า)** — มองหาพนักงานต้อนรับเมื่อถึงศาล, บอกเคาน์เตอร์/ชั้น/ขั้นตอน | Phase 4 + 7 | ❌ | Zero mentions of "พนักงานต้อนรับ" or "เสื้อฟ้า" in any V2 flow. Integration plan Section 2 |
| 3 | **10 Tips for Hiring Lawyers** — Checklist จ้างทนาย 10 ข้อ: เช็คใบอนุญาต, ถามส่วนได้เสีย, สัญญาว่าความ, เก็บสำเนา | Phase 3 (Path B) | ❌ | V2 Path B says "ใช้ทนาย" with price range but ZERO vetting guidance. Integration plan Section 8 |
| 4 | **Mediation 4 Benefits (ไกล่เกลี่ย)** — ฟรี/ไม่เป็นทางการ/กำหนดผลเอง/เป็นความลับ + ศูนย์ไกล่เกลี่ย contact | Phase 3 (Path C) | ❌ | V2 Path C just says "ไกล่เกลี่ย — ฟรี (ถ้าทำได้)" with no benefits explanation. Integration plan Section 12 |

### Priority 2: Category-Specific Blocks (HIGH impact, MEDIUM effort)

| # | Improvement | Phase | Status | Evidence |
|---|------------|-------|--------|----------|
| 5 | **Consumer Cases FREE Filing** — ยกเว้นค่าฤชาธรรมเนียมทั้งหมด, ฟ้องด้วยวาจาได้, ฟ้องที่ศาลที่ผู้บริโภคอยู่ | Phase 2+4+7 (consumer flows) | ⚠️ | V2 mentions "คดีผู้บริโภค — ไม่ต้องมีทนาย" but MISSING: FREE fees, oral complaint, consumer's home court choice. Integration plan Section 13 |
| 6 | **Criminal Case Rights + Legal Aid (ทนายขอแรง)** — สิทธิผู้ต้องหา, ศาลตั้งทนายให้ในคดีอัตราโทษสูง, จำเลยไม่ต้องจ่าย | Phase 2+7 (crime flows) | ❌ | Zero mentions of "ทนายขอแรง" or defendant rights. Integration plan Section 14 |
| 7 | **Bail Application (ปล่อยชั่วคราว)** — 11 ประเภทหลักประกัน, 7 ขั้นตอน, ประกันภัยอิสรภาพ, คำเตือนนายประกัน | Phase 7 (crime flows) | ❌ | No bail content in any flow. Integration plan Section 15 |
| 8 | **Courtroom Etiquette** — แต่งกายสุภาพ, ลุกขึ้นทำความเคารพ, ห้ามนั่งไขว่ห้าง/ใส่แว่นดำ/นั่งหลับ, ต้องยืนพูด | Phase 7 (all court-appearance flows) | ❌ | No etiquette guidance. Integration plan Section 3 |
| 9 | **Court Summons Type Guide** — หมายนัด/หมายเรียก/คำสั่งเรียกเอกสาร/หมายเรียกพยาน, ต้องทำอะไรแต่ละประเภท | Phase 1+7 (debt/crime/defamation/accident) | ⚠️ | V2 mentions "หมายเรียก" in procedure steps but NO type identification guide. Integration plan Section 4 |
| 10 | **Court Taxonomy** — ศาลจังหวัด vs ศาลแขวง vs ศาลชำนัญพิเศษ (แรงงาน/ผู้บริโภค/เยาวชน/ภาษี/ล้มละลาย/IP) | Phase 4 (all flows) | ⚠️ | V2 mentions "ศาลจังหวัด" and "แผนกคดีผู้บริโภค" but NO taxonomy explaining WHY that court. Integration plan Section 9 |

### Priority 3: Situational / Trigger-Based (MEDIUM impact, MEDIUM effort)

| # | Improvement | Phase | Status | Evidence |
|---|------------|-------|--------|----------|
| 11 | **Witness Summons Process** — ตรวจสอบหมาย, ไปศาลตามนัด (ขัดขืน=หมายจับ+คดีอาญา), สิ่งที่ต้องนำไป, สาบานตน | Phase 5+7 (crime/accident/defamation) | ❌ | No witness summons guidance. Integration plan Section 5 |
| 12 | **Testimony Guidance** — เบิกความคืออะไร, พูดเฉพาะที่รู้, ห้ามอ่านจากกระดาษ, บอก"จำไม่ได้"ได้, ตรวจสอบบันทึกคำเบิกความ | Phase 7 (testimony flows) | ❌ | No testimony process explanation. Integration plan Section 6 |
| 13 | **Perjury Warning** — โทษจำคุกไม่เกิน 5 ปี (คดีทั่วไป) / 7 ปี (คดีอาญา), ปรับ 10,000-14,000 บาท, ผิดแม้ยังไม่ได้สาบานตน | Phase 2+7 (all flows) | ❌ | Zero perjury warnings in any V2 flow. Integration plan Section 7 |
| 14 | **Who Can File (ผู้มีสิทธิฟ้อง)** — บุคคลธรรมดา, ผู้เยาว์ (ต้องมีผู้แทน), นิติบุคคล, กลุ่มที่ฟ้องไม่ได้ (กองมรดก/ชมรมไม่จดทะเบียน) | Phase 2+4 (inheritance/family/consumer) | ❌ | No standing-to-sue guidance. Integration plan Section 10 |
| 15 | **Appeals Process** — อุทธรณ์/ฎีกา, กำหนด 1 เดือน, เงื่อนไขทุนทรัพย์ (50K/200K), ยื่นที่ศาลชั้นต้น | Phase 8 (all flows) | ⚠️ | V2 mentions "อุทธรณ์" in insurance context (appeal to insurance company, not court appeals). Integration plan Section 11 |

### Summary: Implementation Status

| Priority | Total Sections | ✅ Done | ⚠️ Partial | ❌ Missing | Completion |
|----------|:---:|:---:|:---:|:---:|:---:|
| P1 (Universal) | 4 | 0 | 0 | 4 | **0%** |
| P2 (Category) | 6 | 0 | 3 | 3 | **25%** |
| P3 (Situational) | 5 | 0 | 1 | 4 | **10%** |
| **TOTAL** | **15** | **0** | **4** | **11** | **13%** |

> 🔴 **CRITICAL FINDING:** Court Guide integration has **NOT been applied** to any V2 flow. The 15-section integration plan is fully documented in `concierge_court_guide_integration.md` with detailed BEFORE/AFTER examples for each section, but zero content has been inserted into the actual flow files. Current V2 flows represent the "BEFORE" state in every integration section.

---

## SECTION B: GAP ANALYSIS — What's STILL Missing After This Round

### B1. Structural Gaps (Court Guide Content)

These are the gaps identified by comparing V2 flows against the 15-section court guide integration plan:

| # | Gap | Severity | User Impact |
|---|-----|----------|-------------|
| G1 | **No court navigation guidance** | 🔴 CRITICAL | First-time court visitors don't know: where to go inside, what to bring (weapons = contempt), what NOT to do (recording, phones, smoking). Risk of self-inflicted legal problems |
| G2 | **No receptionist information** | 🔴 CRITICAL | Most Thais are intimidated by courts — blue-shirt receptionists are the #1 anxiety reducer. 0 mentions in 47 flows |
| G3 | **No lawyer vetting checklist** | 🔴 CRITICAL | Users hire lawyers blindly — no license check, no conflict-of-interest question, no written fee agreement. Risk of fraud/incompetent counsel |
| G4 | **No courtroom etiquette** | 🟠 HIGH | Sitting while addressing court, wearing sunglasses, or crossing legs can = contempt. Self-represented litigants need this most |
| G5 | **No perjury warnings** | 🟠 HIGH | Perjury = 5-7 years prison. Users emotionally invested in "winning" may embellish. Zero warnings in any flow |
| G6 | **Mediation under-explained** | 🟠 HIGH | Path C just says "ไกล่เกลี่ย — ฟรี" — doesn't explain it's confidential, free, gives parties control, preserves relationships |
| G7 | **No bail process** | 🟠 HIGH | 0 guidance on 11 security types, liberty insurance (ประกันภัยอิสรภาพ), or 7-step bail process. Critical for crime flow users |
| G8 | **No defendant rights / legal aid** | 🟠 HIGH | Users don't know court MUST appoint free lawyer in serious cases (ทนายขอแรง). Leads to unfair guilty pleas |
| G9 | **No appeals process** | 🟡 MEDIUM | 1-month absolute deadline not communicated. Capital threshold rules (50K/200K) missing. Users miss appeal windows |
| G10 | **Court taxonomy missing** | 🟡 MEDIUM | Users don't understand WHY they go to a specific court. Specialized courts (labor, consumer, juvenile) are invisible |
| G11 | **No court summons type guide** | 🟡 MEDIUM | Users panic when receiving ANY court document. Don't know หมายนัด vs หมายเรียก (ignoring หมายเรียก = automatic default judgment) |
| G12 | **Consumer FREE filing under-emphasized** | 🟡 MEDIUM | Consumer cases are completely free + can file orally — but V2 flows just say "ไม่ต้องมีทนาย" without these game-changing details |
| G13 | **No witness summons process** | 🟡 MEDIUM | Ignoring witness summons = arrest warrant + criminal charge (6 months jail). Users don't know this |
| G14 | **No testimony guidance** | 🟡 MEDIUM | First-time witnesses don't know they can say "I don't remember," can't read from notes, can check/correct transcript |
| G15 | **No who-can-file rules** | 🟡 MEDIUM | Users try to file on behalf of estates (กองมรดก) or unregistered groups — cases get dismissed for lack of standing |

### B2. Coverage Gaps (New Flows Needed — from V2 Test)

These are identified from the V2 test results (`concierge_v2_test_results.md`) — real questions with NO matching flow:

| # | Gap | Real Questions Affected | Severity |
|---|-----|------------------------|----------|
| G16 | **Phishing / SMS Scam Flow** (Flow 1.6) | Q1.3#1: Clicked fake SMS link, lost 200K. Bank says user consented | 🔴 CRITICAL |
| G17 | **Bribery / Corruption Flow** (Flow 5.4) | Q5.1#1: Official demands 100K bribe. Q5.1#2: Customs "special service" | 🔴 CRITICAL |
| G18 | **Condo Juristic Person Disputes** (Flow 10.4) | Q10.2#1-3: Forced fees, noisy neighbor, opaque finances | 🟠 HIGH |
| G19 | **Right of Way / Easement** (Flow 10.5) | Q10.4#1,3: Private road blocked, landlocked property | 🟠 HIGH |
| G20 | **Social Security / Workmen's Comp** (Flow 7.5) | Q7.3#1-3: Commute injury denied, coverage lapsed, employer didn't pay | 🟠 HIGH |
| G21 | **Contract Termination / Cooling-Off** (Flow 8.5) | Q8.3#1-3: Gym cancellation, car deposit, clinic surgery | 🟡 MEDIUM |
| G22 | **Criminal Liability from Accidents** | Q12.5#1-3: Fatal accident charges, worker death, electric shock | 🟡 MEDIUM |

### B3. Content Quality Gaps (V2 Flow Weaknesses)

| # | Gap | Affected Flows | Impact |
|---|-----|---------------|--------|
| G23 | **Phase 3 Path B lacks any lawyer guidance** beyond price | All 47 flows | Users pick lawyers blindly |
| G24 | **Phase 3 Path C under-sells mediation** | All 47 flows | Users skip best option because they don't understand it |
| G25 | **Phase 4 lacks court taxonomy** | All 47 flows | Users go to court but don't know why THAT court |
| G26 | **Phase 7 lacks day-of-court guidance** | All court-appearance flows | Users show up unprepared |
| G27 | **Phase 8 lacks appeals + what-comes-after-judgment** | All 47 flows | Users finish the journey without knowing next steps |
| G28 | **No "Thainess" contextual guidance** | All 47 flows | Missing: แต่งกายสุภาพ, ไหว้, cultural court norms that Thai judges expect |

---

## SECTION C: TEST RESULTS — 36 Questions Against V2 Flows (Pre-Integration Baseline)

> **Methodology:** 3 real user questions per category × 12 categories = 36 tests
> **Source Questions:** `qa_135_real_questions.md`
> **Flows Tested:** `concierge_v2_cat1_6.md` + `concierge_v2_cat7_12.md` (47 V2 flows)
> **Verdict Scale:** ✅ MATCH (handles completely) | ⚠️ PARTIAL (handles but missing details) | ❌ MISS (no flow or major gap)

---

### Category 1: ONLINE FRAUD (ฉ้อโกงออนไลน์)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 1.1 | "สั่งกระเป๋าแบรนด์เนม 35K จาก FB — ถูกบล็อก" | Flow 1.1 ซื้อของไม่ได้ของ — compound: ฉ้อโกง+พ.ร.บ.คอมพ์, 3 paths, jurisdiction, 9 docs, online filing | ✅ MATCH |
| 1.2 | "TikTok iPhone 15 Pro 18K — ปิดเพจหนี มีเลขบัญชี" | Flow 1.1 covers: platform-agnostic fraud, account tracing, AOC 1441 | ✅ MATCH |
| 1.3 | "SMS ปลอมให้คลิกลิงก์ — เงินหาย 200K" | No V2 flow for phishing/SMS scam. Flow 1.2 (Call Center) doesn't cover SMS links or bank liability | ❌ MISS |

**Category Verdict:** 2/3 ✅ · 0/3 ⚠️ · 1/3 ❌ — **67% coverage**

---

### Category 2: CRIME (อาชญากรรม)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 2.1 | "เพื่อนบ้านชกหน้า — เย็บ 5 เข็ม มีกล้องวงจรปิด" | Flow 2.1 ทำร้ายร่างกาย — compound: ทำร้าย+บุกรุก, police+medical+prosecution path, 4 charges | ✅ MATCH |
| 2.2 | "กลับจากต่างจังหวัด — บ้านโดนงัด ทองหายครึ่งล้าน" | Flow 2.2 ลักทรัพย์ — compound: ลักทรัพย์+บุกรุก+ทำให้เสียทรัพย์, forensic evidence, insurance claim | ✅ MATCH |
| 2.3 | "เบอร์แปลกขู่กรรโชก 500K — รู้รายละเอียดชีวิต" | Flow 2.4 ข่มขู่/กรรโชก — compound: กรรโชก+พ.ร.บ.คอมพ์, digital evidence, restraining order | ✅ MATCH |

**Category Verdict:** 3/3 ✅ — **100% coverage** (best category)

---

### Category 3: DEFAMATION (หมิ่นประมาท)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 3.1 | "เอารูปเราโพสต์กลุ่ม 'สาวขายตัว' พร้อมเบอร์โทร" | Flow 3.1 หมิ่นประมาทออนไลน์ — compound: หมิ่น+พ.ร.บ.คอมพ์, StopNCII.org, digital evidence | ✅ MATCH |
| 3.2 | "หัวหน้าส่งเมลเวียนทั้งบริษัท — กล่าวหาทุจริต 2 ล้าน" | Flow 3.3 ถูกกล่าวหาเท็จ — compound: หมิ่น+แจ้งความเท็จ, workplace context, internal investigation rights | ✅ MATCH |
| 3.3 | "คนปลอมเฟสเรา — โพสต์ด่าสถาบัน" | Flow 1.3 (แฮกบัญชี) — identity theft + defamation angle partially covered, but 112 context creates unique urgency | ⚠️ PARTIAL |

**Category Verdict:** 2/3 ✅ · 1/3 ⚠️ — **83% coverage**

---

### Category 4: INSURANCE (ประกันภัย)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 4.1 | "ประกันชีวิต 15 ปี — สามีเสียชีวิตมะเร็ง, บริษัทปฏิเสธอ้างปกปิดโรคกระเพาะ" | Flow 4.1 ประกันไม่จ่ายตามกรมธรรม์ — compound: ผิดสัญญา+คดีผู้บริโภค, appeal process, OIC complaint | ⚠️ PARTIAL |
| 4.2 | "ซื้อประกันอุบัติเหตุ — ตัวแทนบอกคุ้มครองทุกกรณี แต่ไม่คุ้มมอไซค์" | Flow 4.2 ปัญหาเงื่อนไขกรมธรรม์ — covers misrepresentation but needs stronger "unfair contract terms" angle | ⚠️ PARTIAL |
| 4.3 | "กู้บ้านแบงก์เขียว — บังคับซื้อประกันถึงได้ดอกเบี้ยพิเศษ" | Flow 4.3 ถูกบังคับขายประกัน — tied-selling, สคบ., Bank of Thailand complaint | ✅ MATCH |

**Category Verdict:** 1/3 ✅ · 2/3 ⚠️ — **67% coverage**

---

### Category 5: GOVERNMENT (ราชการและรัฐ)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 5.1 | "ข้าราชการเรียกรับ 100K — ค่าอำนวยความสะดวกขอใบอนุญาตก่อสร้าง" | **No flow exists.** Flow 5.2 (รัฐละเมิด) covers damage by state, NOT active bribery/solicitation | ❌ MISS |
| 5.2 | "ทำพาสปอร์ต 4 เดือนยังไม่ได้ — เสียโอกาสงานสิงคโปร์" | Flow 5.1 ปัญหาเอกสารราชการล่าช้า — covers delay, complaint escalation to ombudsman, admin court | ✅ MATCH |
| 5.3 | "ครูอยากย้ายกลับบ้าน — ผอ.เขตไม่เซ็นเพราะไม่เข้าชมรมการเมือง" | Flow 5.3 ถูกปฏิบัติไม่เป็นธรรม — covers administrative discretion abuse, Civil Service Commission, admin court | ⚠️ PARTIAL |

**Category Verdict:** 1/3 ✅ · 1/3 ⚠️ · 1/3 ❌ — **50% coverage**

---

### Category 6: PROPERTY (ที่ดินและทรัพย์สิน)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 6.1 | "ที่ดินยาย — น.ส.3 จะออกโฉนด แต่ทับซ้อนกับคนอื่น" | Flow 6.1 ปัญหาโฉนดที่ดิน — covers title deed disputes, Land Department objection, survey verification | ✅ MATCH |
| 6.2 | "เพื่อนบ้านสร้างรั้วล้ำ 1.5 เมตร × 20 เมตร" | Flow 6.2 ข้อพิพาทแนวเขต — covers boundary encroachment, adverse possession defense, survey evidence | ✅ MATCH |
| 6.3 | "กลับจากต่างประเทศ 10 ปี — มีคนปลูกบ้านบนที่ดิน" | Flow 6.3 ถูกบุกรุกที่ดิน — compound: บุกรุก+ทำให้เสียทรัพย์, adverse possession defense, criminal + civil paths | ✅ MATCH |

**Category Verdict:** 3/3 ✅ — **100% coverage**

---

### Category 7: LABOUR (แรงงาน)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 7.1 | "ทำงาน 10 ปี — โดนเลิกจ้างลอยๆ ปรับโครงสร้าง" | Flow 7.1 เลิกจ้างไม่เป็นธรรม — covers severance, notice pay, unfair dismissal damages, 2-year deadline | ✅ MATCH |
| 7.2 | "ร้านอาหาร — ทำงาน 10:00-22:00 6 วัน ไม่มี OT" | Flow 7.2 ค่าจ้าง/OT — covers minimum wage, OT rates (1.5x/3x), holiday pay, 2-year back claim | ✅ MATCH |
| 7.3 | "อุบัติเหตุเดินทางไปทำงาน — ประกันสังคมไม่คุ้มครอง" | Flow 7.4 covers labor contracts, not SSO/WCF. No flow for social security disputes | ⚠️ PARTIAL |

**Category Verdict:** 2/3 ✅ · 1/3 ⚠️ — **83% coverage**

---

### Category 8: CONSUMER (ผู้บริโภค)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 8.1 | "มือถือ 25K — เครื่องดับ 12 วัน ซ่อม 2 รอบไม่หาย" | Flow 8.1 สินค้าชำรุด — covers warranty, refund/replace rights, สคบ. complaint. MISSING: implied warranty, "สินค้าบกพร่อง" burden shift | ⚠️ PARTIAL |
| 8.2 | "คอร์สเรียน 50K — โฆษณาได้งาน 100% แต่เนื้อหาพื้นๆ" | Flow 8.2 โฆษณาเกินจริง — covers false advertising, สคบ., Consumer Case Procedures Act | ✅ MATCH |
| 8.3 | "ซื้อคอร์สฟิตเนส 30K — ขอยกเลิกหลัง 1 เดือนเพราะย้ายจังหวัด" | No specific flow for contract termination/cooling-off. Flow 8.4 (ข้อสัญญาไม่เป็นธรรม) partially covers | ⚠️ PARTIAL |

**Category Verdict:** 1/3 ✅ · 2/3 ⚠️ — **67% coverage**

---

### Category 9: DEBT (หนี้สิน)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 9.1 | "บัตรเครดิต 200K — ทวงวันละ 10-20 สาย, โทรหาญาติ" | Flow 9.1 ทวงหนี้ผิดกฎหมาย — covers Debt Collection Act violations, BOT complaint, criminal charges for harassment | ✅ MATCH |
| 9.2 | "หนี้นอกระบบ 50K — ดอก 20%/เดือน, จ่ายดอกเกินเงินต้นแล้ว" | Flow 9.2 หนี้นอกระบบ — covers usury (ดอกเบี้ยเกิน 15%/year), loan sharking, criminal charges | ✅ MATCH |
| 9.3 | "เซ็นค้ำประกันให้เพื่อนซื้อรถ — เพื่อนหนี ไฟแนนซ์เรียก 200K" | Flow 9.3 การค้ำประกัน — covers surety obligations, right of recourse, new Civil Code amendments | ⚠️ PARTIAL |

**Category Verdict:** 2/3 ✅ · 1/3 ⚠️ — **83% coverage**

---

### Category 10: HOUSING (ที่อยู่อาศัย)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 10.1 | "เช่าคอนโดหมดสัญญา — จ่ายค่าเช่าต่อเนื่อง 6 เดือน แล้วโดนไล่ออก 15 วัน" | Flow 10.1 เช่าทรัพย์/เช่าซื้อ — covers lease renewal, eviction notice periods, deposit return | ✅ MATCH |
| 10.2 | "คอนโด — นิติฯ เก็บค่าซ่อมลิฟต์ห้องละ 80K ทั้งที่อยู่ชั้น 3" | **No flow exists** for condo juristic person disputes. No coverage of common fee obligations, committee authority | ❌ MISS |
| 10.3 | "ซื้อที่ดินเปล่า 10 ปี — จะปลูกบ้าน เจอคนปลูกเพิงอยู่ อ้างครอบครองปรปักษ์" | Flow 6.3 (บุกรุกที่ดิน) cross-references — covers adverse possession, eviction, criminal trespass | ⚠️ PARTIAL |

**Category Verdict:** 1/3 ✅ · 1/3 ⚠️ · 1/3 ❌ — **50% coverage**

---

### Category 11: FAMILY (ครอบครัว)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 11.1 | "แต่งงาน 8 ปี — สามีนอกใจ, สินสมรสในชื่อสามีทั้งหมด" | Flow 11.1 หย่า/แบ่งสินสมรส — covers division, dissipation presumption, infidelity damages (ค่าทดแทน) | ✅ MATCH |
| 11.2 | "หย่าแล้ว — สามีไม่จ่ายค่าอุปการะ 5,000/เดือน 2 ปี" | Flow 11.2 ค่าอุปการะ/อำนาจปกครอง — covers enforcement, contempt, modification of support orders | ✅ MATCH |
| 11.3 | "สามีขี้เมาทำร้าย — ขวดเบียร์ฟาดหัวเย็บ 5 เข็ม ลูกเห็นเหตุการณ์" | Flow 11.3 ความรุนแรงในครอบครัว — compound: ทำร้าย+DV Act, protection orders, shelter referral | ✅ MATCH |

**Category Verdict:** 3/3 ✅ — **100% coverage**

---

### Category 12: ACCIDENT (อุบัติเหตุ)

| # | 🔴 Question | 🟢 V2 Flow Match | Verdict |
|---|------------|------------------|---------|
| 12.1 | "มอไซค์ — รถเก๋งเปิดประตูกะทันหันชนล้ม แขนหัก" | Flow 12.1 อุบัติเหตุทางถนน — covers fault determination, insurance claim, civil damages, medical evidence | ✅ MATCH |
| 12.2 | "โรงงาน — นิ้วถูกเครื่องจักรตัด 3 นิ้ว, กองทุนประเมินความพิการ 20%" | Flow 7.3 partially covers (ประกันสังคม) — but MISSING Workmen's Compensation Fund appeal process, disability re-assessment | ⚠️ PARTIAL |
| 12.3 | "เพื่อนบ้านต่อเติม — ชายคายื่นล้ำ น้ำฝนใส่ผนังบ้านเสียหาย" | Flow 12.3 ละเมิด/เรียกค่าเสียหาย — covers trespass, nuisance, damages calculation | ✅ MATCH |

**Category Verdict:** 2/3 ✅ · 1/3 ⚠️ — **83% coverage**

---

### 📊 Test Results Summary

| Category | ✅ Match | ⚠️ Partial | ❌ Miss | Coverage |
|----------|:---:|:---:|:---:|:---:|
| 1. Online Fraud | 2 | 0 | 1 | 67% |
| 2. Crime | 3 | 0 | 0 | **100%** |
| 3. Defamation | 2 | 1 | 0 | 83% |
| 4. Insurance | 1 | 2 | 0 | 67% |
| 5. Government | 1 | 1 | 1 | 50% |
| 6. Property | 3 | 0 | 0 | **100%** |
| 7. Labour | 2 | 1 | 0 | 83% |
| 8. Consumer | 1 | 2 | 0 | 67% |
| 9. Debt | 2 | 1 | 0 | 83% |
| 10. Housing | 1 | 1 | 1 | 50% |
| 11. Family | 3 | 0 | 0 | **100%** |
| 12. Accident | 2 | 1 | 0 | 83% |
| **TOTAL** | **23** | **10** | **3** | **75%** |

| Verdict | Count | % |
|----------|:---:|:---:|
| ✅ MATCH | 23/36 | 64% |
| ⚠️ PARTIAL | 10/36 | 28% |
| ❌ MISS | 3/36 | 8% |

> **Compared to V2 test results:** Same 75% overall coverage. Court guide integration would mainly impact the ⚠️ PARTIAL cases by adding depth to court-related phases, but would not change the ❌ MISS cases (those need NEW flows).

---

## SECTION D: PROCESS CHECK — What พี่ณัฐ Asked For vs What We Delivered

### D1. What พี่ณัฐ Asked For

Based on the project trajectory documented across key files:

| Requirement | Source | Status |
|------------|--------|--------|
| 47 concierge flows covering all 12 categories | `legalai_v2_concierge_design.md` | ✅ Done — 47 V2 flows exist |
| 8-phase flow structure (Understand → Rights → Path → Jurisdiction → Docs → Prepare → File → Follow-up) | `concierge_format_test.md` Gold Standard | ✅ Done — All 47 flows follow 8-phase structure |
| Court Guide Integration — 15 sections | `concierge_court_guide_integration.md` | ❌ NOT DONE — Plan documented but zero content applied |
| Test against 135 real questions | `qa_135_real_questions.md` | ⚠️ Partially — 36/135 tested in V2 test, needs full 135 |
| Monetization gates working (Free → ฿299 → ฿999) | Design specification | ✅ Present in all flows |
| Compound case detection | Format test | ✅ Present in most flows |
| Human drive integration | Consumer insight report | ✅ Present in many flows |

### D2. What We Have (Current State)

✅ **47 V2 Flows** — 7,054 + 5,637 = 12,691 lines across 2 files
✅ **8-Phase Structure** — Consistent format, all phases present in every flow
✅ **Legal Citations** — Penal Code, Civil Code, specific Acts in every flow
✅ **3-Path Architecture** — 🅰️ Self / 🅱️ Lawyer / 🅲️ Mediation
✅ **Monetization Gates** — Phase 3 gate (฿299), Phase 6 upsell (฿999)
✅ **Document Checklists** — Per-flow document requirements
✅ **Jurisdiction** — Court references with real addresses (but all generic "ศาลจังหวัดขอนแก่น")
✅ **Timeline** — Phase 8 follow-up with estimated durations
✅ **Court Guide Integration Plan** — Complete 15-section plan with detailed BEFORE/AFTER

### D3. What's Still Missing

❌ **Court Guide Content (100% missing):**
- No court behavior rules (weapons, phones, recording)
- No blue-shirt receptionists
- No lawyer vetting checklist (10 tips)
- No mediation benefits explanation
- No courtroom etiquette
- No perjury warnings
- No bail process
- No defendant rights / legal aid
- No appeals process
- No court taxonomy
- No court summons type guide
- No witness summons process
- No testimony guidance
- No who-can-file rules
- Consumer FREE filing under-emphasized

❌ **New Flows Needed (from test gaps):**
- Flow 1.6: Phishing / SMS Scam
- Flow 5.4: Bribery / Corruption
- Flow 7.5: Social Security / Workmen's Comp
- Flow 8.5: Contract Termination / Cooling-Off
- Flow 10.4: Condo Juristic Person Disputes
- Flow 10.5: Right of Way / Easement

❌ **Quality Issues:**
- All jurisdictions hardcoded to "ขอนแก่น" (no province customization)
- Phase 3 Path B is identical boilerplate across all 47 flows
- Phase 3 Path C is identical boilerplate across all 47 flows
- No dynamic per-category tailoring of court guide content

### D4. What To Do Next 🔜

| Priority | Action | Effort | Impact |
|:---:|--------|:---:|:---:|
| 🔴 P0 | **Apply Court Guide Integration** — Insert 15 sections into V2 flow templates per the integration plan | Medium | **TRANSFORMATIVE** — this is the V3 upgrade |
| 🔴 P0 | **Fix Universal Templates First** (P1: 4 sections) — Court behavior, receptionists, lawyer checklist, mediation benefits → all 47 flows get better in one pass | Low (1 change each, template-based) | HIGH — affects every flow |
| 🟠 P1 | **Category-Specific Blocks** (P2: 6 sections) — Consumer FREE filing, criminal rights, bail, courtroom etiquette, summons guide, court taxonomy | Medium | HIGH — critical for crime/consumer/defamation flows |
| 🟡 P2 | **Situational Content** (P3: 5 sections) — Witness summons, testimony, perjury, who-can-file, appeals | Medium | MEDIUM — fills remaining gaps |
| 🟡 P2 | **Create Missing Flows** — 6 new flows (phishing, bribery, SSO, cooling-off, condo association, easement) | High (new content creation) | HIGH — closes critical test gaps |
| ⚪ P3 | **Full 135-Question Test** — Test all 135 real questions against V3 (post-integration) flows | Medium | MEDIUM — validation |
| ⚪ P3 | **Province Customization** — Replace hardcoded "ขอนแก่น" with dynamic jurisdiction mapping | High (needs geo data) | MEDIUM — UX improvement |

---

## 📊 FINAL VERDICT

### V3 Court Guide Integration Status: **0% IMPLEMENTED**

The integration plan (`concierge_court_guide_integration.md`) is thorough and ready — 15 sections, detailed BEFORE/AFTER examples, implementation priorities, cross-flow patterns, and a verification checklist. But **none of it has been applied** to the actual flow files.

### Next Step: Execute Priority 1 Universal Template Insertions

These 4 changes alone will improve ALL 47 flows:
1. **Phase 7**: Add court behavior rules (เรือนจำ — ห้ามนำอาวุธ, ห้ามอัดเสียง, ห้ามใช้มือถือ)
2. **Phase 4**: Add blue-shirt receptionists (พนักงานต้อนรับเสื้อฟ้า — บริการด้วยรอยยิ้ม จากใจศาล)
3. **Phase 3 Path B**: Add 10-tip lawyer checklist (10 ประการแต่งตั้งทนายความ)
4. **Phase 3 Path C**: Add mediation 4 benefits (4 ประโยชน์การไกล่เกลี่ย + ศูนย์ไกล่เกลี่ย contact)

**Estimated effort:** ~3,500 words of net new content insertion
**Estimated impact:** Transforms V2 (legal-only) → V3 (legal + practical court navigation)

---

> 📚 **Sources:** คู่มือติดต่อราชการศาลยุติธรรม ฉบับประชาชน · 135 Real User Questions · 47 V2 Concierge Flows
> 🏛️ **Prepared for:** LegalAI V3 Concierge — พี่ณัฐ review
> 📅 **Report Date:** 11 สิงหาคม 2569
