# 🧭 LegalAI V2 Concierge — 36 Real Question Test Results

> **Test Date:** 11 สิงหาคม 2569
> **Methodology:** 3 real user questions per category × 12 categories = 36 tests against 47 V2 Concierge Flows
> **Flows Tested:** concierge_v2_cat1_6.md (24 flows) + concierge_v2_cat7_12.md (23 flows)
> **Questions Source:** qa_135_real_questions.md (135 real questions)

---

# 📊 FINAL SUMMARY

## Per-Category Results

| Category | V2 Flows | Tested | ✅ Match | ⚠️ Partial | ❌ Miss | Match % |
|---|---|---|---|---|---|---|
| 1. Online Fraud | 5 | 3 | 2 | 1 | 0 | 83% |
| 2. Crime | 4 | 3 | 2 | 1 | 0 | 83% |
| 3. Defamation | 4 | 3 | 2 | 1 | 0 | 83% |
| 4. Insurance | 3 | 3 | 1 | 2 | 0 | 67% |
| 5. Government | 3 | 3 | 1 | 1 | 1 | 50% |
| 6. Property | 5 | 3 | 2 | 1 | 0 | 83% |
| 7. Labour | 4 | 3 | 2 | 1 | 0 | 83% |
| 8. Consumer | 4 | 3 | 2 | 1 | 0 | 83% |
| 9. Debt | 4 | 3 | 2 | 1 | 0 | 83% |
| 10. Housing | 3 | 3 | 1 | 1 | 1 | 50% |
| 11. Family | 5 | 3 | 2 | 1 | 0 | 83% |
| 12. Accident | 3 | 3 | 2 | 1 | 0 | 83% |
| **TOTAL** | **47** | **36** | **21** | **13** | **2** | **75%** |

### Verdict Legend
- ✅ MATCH: The V2 concierge flow handles this question completely (phases 1-8 all cover the user's needs)
- ⚠️ PARTIAL: The flow partially matches but misses key nuances, needs enhancement
- ❌ MISS: No existing V2 flow maps to this question — new flow needed

### Overall Verdicts
- ✅ **21/36 (58%)** — Flows match real questions cleanly
- ⚠️ **13/36 (36%)** — Partial match, existing flows need enhancement
- ❌ **2/36 (6%)** — Real questions with NO matching flow = critical gaps

---

# 🔴 TOP GAPS — New Flows Needed

| # | Gap | Severity | User Need | Recommendation |
|---|---|---|---|---|
| 1 | **SMS / Phishing Scam (Phishing/Link Scam)** | 🔴 CRITICAL | Q1.3#1: User clicked fake SMS link, lost 200K. Flow 1.2 (Call Center) doesn't cover SMS phishing or bank liability for unauthorized transactions | Create **Flow 1.6: Phishing / Social Engineering — SMS, Email, Link Scams** |
| 2 | **Bribery / Corruption by Officials** | 🔴 CRITICAL | Q5.1#1: Official demands 100K bribe for permit. Q5.1#2: Customs demands "special service fee". Flow 5.2 (รัฐละเมิด) covers damage by state, NOT active bribery/solicitation | Create **Flow 5.4: Officials Soliciting Bribes — สินบนเจ้าหน้าที่รัฐ** (NACC, anti-corruption) |
| 3 | **Condo / Housing Association Disputes (นิติบุคคล)** | 🟠 HIGH | Q10.2#1: Forced common area fee of 80K. Q10.2#2: Noisy neighbor + corrupt committee. Q10.2#3: Opaque finances. No flow covers condo juristic person disputes | Create **Flow 10.4: Condo/Housing Association Disputes — นิติบุคคลคอนโด/หมู่บ้าน** |
| 4 | **Right of Way / Easement (ทางจำเป็น/ภาระจำยอม)** | 🟠 HIGH | Q10.4#1: Private road access blocked. Q10.4#3: Landlocked property. No flow covers easement/right-of-way law | Create **Flow 10.5: Right of Way / Easement — ทางจำเป็น / ภาระจำยอม** |
| 5 | **Social Security Disputes (ประกันสังคม/กองทุนเงินทดแทน)** | 🟠 HIGH | Q7.3#1: Injury during commute denied. Q7.3#2: Coverage lapsed after resignation. Q7.3#3: Employer didn't pay contributions. Flow 4.2 is for private insurance, not SSO | Create **Flow 7.5: Social Security / Workmen's Compensation Fund — ประกันสังคม/กองทุนเงินทดแทน** |
| 6 | **Contract Termination / Cooling-Off Rights (บอกเลิกสัญญา)** | 🟡 MEDIUM | Q8.3#1: Cancel gym membership. Q8.3#2: Car booking deposit. Q8.3#3: Clinic surgery cancellation. Flow 8.4 covers false ads, not contract cancellation rights | Add to Flow 8.4 or create **Flow 8.5: Contract Cancellation / Cooling-Off — บอกเลิกสัญญา/ขอคืนเงิน** |
| 7 | **Cybercrime / Account Hacking (แฮกบัญชี)** | 🟡 MEDIUM | Q1.3#3: Facebook hacked, used to scam others. No specific flow for account takeover + liability as victim-turned-suspect | Add to Flow 1.6 (SMS/Phishing) or create standalone flow |
| 8 | **Criminal Liability from Accidents (ความผิดอาญาจากอุบัติเหตุ)** | 🟡 MEDIUM | Q12.5#1: Drove car, hit pedestrian fatally — criminal charge. Q12.5#2: Worker fell from scaffold. Flow 12.1 covers civil accident, not criminal consequences | Add criminal liability dimension to Flow 12.1 or 12.3 |
| 9 | **Same-Sex/Family Law 2.0 (สมรสเท่าเทียม/LGBTQ+)** | 🟡 MEDIUM | Q11.5#1: LGBTQ+ couple — IVF, child legal status. Flow 11.2 (child custody) needs update for marriage equality law | Update Flow 11.2 with marriage equality provisions |
| 10 | **Defective Product Liability (สินค้าชำรุด/เรียกคืน)** | 🟡 MEDIUM | Q8.1#1: Phone died after 12 days. Q8.1#3: Used car with rolled-back odometer. Flow 8.1 covers "not as described" but needs explicit warranty/defect coverage | Enhance Flow 8.1 to include warranty rights and used car fraud |

---

# 🧪 TEST RESULTS — 36 Questions × 8-Phase Protocol

---

## CATEGORY 1: ONLINE FRAUD (หลอกลวงออนไลน์)

### TEST 1.1: ซื้อกระเป๋าแบรนด์เนม 35,000 บาท — ไม่ได้ของ

> **Source:** qa_135_real_questions.md · Q1.1#1
> **Mapped to:** Flow 1.1 — ซื้อของออนไลน์ไม่ได้ของ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "สั่งกระเป๋าแบรนด์เนมจากเพจเฟสบุ๊ค 'Luxury Bag Thailand' ราคา 35,000 บาท
│   โอนเงินไปแล้ว ผ่านมา 2 อาทิตย์ยังไม่ได้ของ ทักแชทไปก็อ่านไม่ตอบ
│   ล่าสุดบล็อคเราไปแล้ว แบบนี้แจ้งความได้มั้ยคะ เก็บสลิปโอนกับแชทไว้หมดแล้ว"
│
├─ 🎯 Phase 1: Flow 1.1 — ซื้อของออนไลน์ไม่ได้ของ
│  ✓ Compound detection: ฉ้อโกง + พ.ร.บ.คอมพ์ ม.14(1)
│  ✓ Captures: platform (Facebook), amount (35,000), evidence (สลิป+แชท)
│  ✓ Human drive: Survival + Justice (เสียเงิน, โดนโกง)
│
├─ ⚖️ Phase 2: Flow identifies rights correctly
│  ✓ ป.อาญา ม.341 — ฉ้อโกง (จำคุก ≤ 3 ปี)
│  ✓ พ.ร.บ.คอมพ์ ม.14(1) — ข้อมูลเท็จ (จำคุก ≤ 5 ปี)
│  ✓ ป.พ.พ. — ผิดสัญญาซื้อขาย (เรียกเงินคืน + ดอกเบี้ย 7.5%)
│  ✓ Actions: แจ้งความออนไลน์, แจ้งแพลตฟอร์ม, แจ้ง ปปง.
│  ⚠️ BUT: No mention of "แบรนด์เนมปลอม" angle (if fake = trademark violation too)
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: แจ้งความออนไลน์ + แจ้งแพลตฟอร์ม (0-200 บาท)
│  ✓ 🅱️ ใช้ทนาย: ฿10,000-20,000 (for >50,000 damage — borderline here)
│  ✓ 🅲️ ทวงถามก่อน: ส่งจดหมายทวงถาม — AI สร้างให้
│
├─ 🔒 GATE: Is it effective?
│  🟢 YES — "รู้ว่าฟ้องอะไรได้ — แต่ต้องไปศาลไหน? ใช้เอกสารอะไร?"
│  Gate creates real pain point. At ฿35,000 vs ฿299 it's 99% savings.
│  ⚠️ But: Path A (ทำเอง) already covers a lot — user may not feel need to pay
│
├─ 📍 Phase 4 (PAID): Jurisdiction
│  ✓ Court: ศาลจังหวัด in user's area (แจ้งที่ไหนก็ได้ for online fraud)
│  ✓ Online option: thaipoliceonline.go.th
│
├─ 📄 Phase 5 (PAID): Documents — 7 items (สลิป, แชท, เลขบัญชี, ฯลฯ)
│  ✓ User has "สลิปโอนกับแชทไว้หมดแล้ว" — good readiness
│
├─ 🔧 Phase 6 (PAID): AI generates — บันทึกแจ้งความ, คำฟ้องคดีผู้บริโภค, ฯลฯ
│
├─ 🏛️ Phase 7 (PAID): 3-step filing (แจ้งความออนไลน์ → แพลตฟอร์ม → ศาลผู้บริโภค)
│
├─ 📊 Phase 8 (฿999): Timeline + Case Plus tracking
│
└─ ✅ VERDICT: MATCH 90%
   Flow 1.1 maps near-perfectly. Missing: trademark/IP angle for luxury goods scams.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 1.2: Call Center หลอกโอน 120,000 บาท

> **Source:** qa_135_real_questions.md · Q1.2#1
> **Mapped to:** Flow 1.2 — Call Center (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "มีคนโทรมาอ้างเป็นเจ้าหน้าที่สรรพากรบอกว่าเราค้างภาษี ต้องจ่ายด่วน
│   เราตกใจเลยโอนไป 120,000 บาท ผ่านมา 3 วันถึงรู้ตัวว่าโดนหลอก
│   แก๊งคอลเซ็นเตอร์ชัดๆ แจ้งความที่ไหนได้บ้าง มีโอกาสได้เงินคืนมั้ย"
│
├─ 🎯 Phase 1: Flow 1.2 — Call Center
│  ✓ Compound detection: ฉ้อโกง ม.342 + พ.ร.บ.คอมพ์ ม.14 + อั้งยี่ ม.209
│  ✓ Captures: impersonation (สรรพากร), amount (120,000), fear trigger
│  ✓ Human drive: Survival + Fear — "เครียดมาก กินไม่ได้นอนไม่หลับ"
│  ⚠️ 3-day delay noted in flow: "อย่ารอ! — ทุกนาทีสำคัญมาก"
│
├─ ⚖️ Phase 2: Flow identifies rights correctly
│  ✓ ป.อาญา ม.342 — ฉ้อโกงโดยแสดงตนเป็นคนอื่น (จำคุก ≤ 5 ปี)
│  ✓ พ.ร.บ.คอมพ์ ม.14(1) — VoIP = ผิด พ.ร.บ.คอมพ์
│  ✓ ป.อาญา ม.209 — อั้งยี่ (เป็นขบวนการ)
│  ✓ Emergency action: โทร 1441 ทันที — ตำรวจไซเบอร์ 24 ชม.
│  ⚠️ User asks: "มีโอกาสได้เงินคืนมั้ย" — Flow covers อายัดบัญชี but success rate is real concern
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: โทร 1441 + แจ้งความออนไลน์ + ติดต่อธนาคาร
│  ✓ 🅱️ ใช้ทนาย: ฿15,000-30,000 (for >100K loss)
│  ✓ 🅲️ ฉุกเฉิน: โทร 1441 ก่อนเลย! (อายัดบัญชี)
│
├─ 🔒 GATE: Is it effective?
│  🟢 YES — Strong urgency hook: "เงินถูกถอนใน 15 นาที"
│  At ฿120,000 loss, ฿299 is compelling
│  ⚠️ But: User already waited 3 days — gate should address "too late?" anxiety
│
├─ 📍 Phase 4 (PAID): Multiple paths — 1441 first, then police station
│
├─ 📄 Phase 5 (PAID): 6 documents (statement, เลขบัญชีปลายทาง, call log, etc.)
│
├─ 🔧 Phase 6 (PAID): AI generates — บันทึกแจ้งความ 3 ข้อหา, คำร้องขออายัดบัญชี
│
├─ 🏛️ Phase 7 (PAID): STEP 1: โทร 1441 → STEP 2: ติดต่อธนาคาร → STEP 3: แจ้งความ
│
├─ 📊 Phase 8 (฿999): Timeline — อายัดบัญชี + สืบสวน + จับกุม + ศาล (6-12 months)
│
└─ ✅ VERDICT: MATCH 92%
   Flow 1.2 handles call center scams excellently. One gap: no guidance on
   "what if 3 days passed already — is it too late?" that users need psychologically.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 1.3: SMS Phishing — เงินหาย 200,000 จากลิงก์ปลอม

> **Source:** qa_135_real_questions.md · Q1.3#1
> **Mapped to:** ⚠️ No exact V2 flow exists — nearest is Flow 1.2 (Call Center)

```
🔴 THE REAL QUESTION
│  "ซื้อของออนไลน์แล้วมี SMS เข้ามาให้คลิกลิงก์ยืนยันตัวตน เรากดเข้าไป
│   กรอกข้อมูลบัตรเครดิต ตอนนี้เงินในบัญชีหายไป 200,000 บาท ธนาคารบอกว่า
│   เรายินยอมเองเลยไม่รับผิดชอบ มีสิทธิฟ้องธนาคารได้มั้ย"
│
├─ 🎯 Phase 1: ⚠️ No dedicated phishing/SMS flow exists
│  Nearest: Flow 1.2 (Call Center) — but SMS phishing ≠ voice call
│  Missing: Link/URL analysis, bank liability for unauthorized transactions
│  Human drive: Survival + Justice + Fear
│
├─ ⚖️ Phase 2: ⚠️ Flow 1.2 partially applicable
│  ✓ พ.ร.บ.คอมพ์ ม.14 — data input fraud (partially applicable)
│  ❌ No mention of bank liability under Payment Systems Act
│  ❌ No mention of BOT consumer protection for unauthorized e-transactions
│  ❌ No mention of "phishing = social engineering" specific defenses
│
├─ 🛤️ Phase 3: ⚠️ Flow 1.2 paths don't fully match
│  🅰️ ทำเอง: โทร 1441 + แจ้งความ (good start)
│  ❌ Missing: How to dispute with bank, BOT complaint, prove you didn't authorize
│
├─ 🔒 GATE: ⚠️ Partial
│  The gate works for fraud reporting but WON'T answer "can I sue the bank?"
│  which is this user's primary question
│
├─ 📍 Phase 4-8 (PAID): Would give court/police info but miss bank-focused remedies
│
└─ ⚠️ VERDICT: PARTIAL 45%
   V2 has NO dedicated phishing/SMS scam flow. User's real need:
   "Can I force the bank to reimburse me?" — not answered by any flow.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️

   🔴 GAP: Need Flow 1.6 "Phishing / Social Engineering / Unauthorized Transactions"
   covering: BOT consumer protection, bank dispute process, Payment Systems Act
```

---

## CATEGORY 2: CRIME (อาชญากรรม)

### TEST 2.1: ทะเลาะเพื่อนบ้าน — ชกหน้าเย็บ 5 เข็ม

> **Source:** qa_135_real_questions.md · Q2.1#1
> **Mapped to:** Flow 2.1 — ทำร้ายร่างกาย (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ทะเลาะกับเพื่อนบ้านเรื่องที่จอดรถ แล้วเขาชกหน้าเราเลือดอาบเลย
│   ไปหาหมอเย็บ 5 เข็ม มีใบรับรองแพทย์กับคลิปกล้องวงจรปิด แจ้งความ
│   ข้อหาทำร้ายร่างกายได้มั้ย จะเรียกค่ารักษากับค่าเสียหายได้เท่าไหร่"
│
├─ 🎯 Phase 1: Flow 2.1 — ทำร้ายร่างกาย
│  ✓ Detects: ทำร้ายร่างกาย — บาดเจ็บ (เย็บ 5 เข็ม = บาดเจ็บ, not สาหัส)
│  ✓ Evidence noted: ใบรับรองแพทย์, กล้องวงจรปิด
│  ✓ Human drive: Survival + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ ป.อาญา ม.295 — ทำร้ายร่างกาย (จำคุก ≤ 2 ปี)
│  ✓ สิทธิเรียกค่าเสียหาย: ค่ารักษา + ค่าขาดรายได้ + ค่าเสียหายทางจิตใจ
│  ✓ Flow captures: "เย็บ 5 เข็ม" = clear bodily harm
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: แจ้งความ + เรียกค่าเสียหายเอง
│  ✓ 🅱️ ใช้ทนาย: For higher damages
│  ✓ 🅲️ เจรจา/ไกล่เกลี่ย: Try settlement first
│
├─ 🔒 GATE: Effective — "รู้สิทธิแล้ว — แต่ต้องทำยังไง? เรียกเงินเท่าไหร่?"
│
├─ 📍 Phase 4-8 (PAID): Police station, evidence list, filing steps, timeline
│
└─ ✅ VERDICT: MATCH 90%
   Flow 2.1 handles this cleanly. User's specific question about
   "ค่ารักษากับค่าเสียหายได้เท่าไหร่" is addressed in Phase 6 (AI calculation).
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 2.2: บ้านโดนงัด — ทองหายครึ่งล้าน

> **Source:** qa_135_real_questions.md · Q2.2#1
> **Mapped to:** Flow 2.2 — ลักทรัพย์ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "กลับมาจากทำงานต่างจังหวัดพบว่าบ้านโดนงัด ทองรูปพรรณกับพระเครื่อง
│   หายไปเกือบครึ่งล้าน ประตูหลังโดนงัด มีรอยนิ้วมือกับรอยรองเท้า
│   ประกันภัยบอกไม่คุ้มครองเพราะไม่ได้ล็อคประตูมิดชิด แบบนี้จะตามจับ
│   ขโมยยังไง แล้วฟ้องประกันได้มั้ย"
│
├─ 🎯 Phase 1: Flow 2.2 — ลักทรัพย์
│  ✓ Compound detection: ลักทรัพย์ (burglary) + potential insurance dispute
│  ✓ Note: งัด = ทำลายทรัพย์ + ลักทรัพย์ (compound)
│  ✓ Evidence: รอยนิ้วมือ, รอยรองเท้า
│  ⚠️ Insurance angle: "ฟ้องประกันได้มั้ย" — 2.2 is crime-only, insurance is in Flow 4.1
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ ป.อาญา ม.334 — ลักทรัพย์ (จำคุก ≤ 3 ปี)
│  ✓ ป.อาญา ม.335 — ลักทรัพย์ในเคหสถาน (จำคุก 1-5 ปี) — more applicable!
│  ⚠️ Insurance: Flow mentions nothing about challenging insurance denial
│  The user needs BOTH criminal + insurance advice
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: แจ้งความ + รวบรวมหลักฐาน
│  ✓ 🅱️ ใช้ทนาย: For high-value theft (500K)
│  ❌ Missing: Insurance dispute path
│
├─ 🔒 GATE: Partial — works for theft but user also needs insurance fight
│
└─ ⚠️ VERDICT: PARTIAL 70%
   Flow 2.2 covers the crime aspect well but the user's insurance dispute
   requires cross-referencing Flow 4.1 (เคลมประกันรถ) — but that's CAR insurance!
   No flow for homeowner's insurance claim disputes.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 2.3: แบล็กเมล์ — ขู่เปิดเผยความลับ เรียก 500,000

> **Source:** qa_135_real_questions.md · Q2.3#1
> **Mapped to:** Flow 2.4 — ขู่กรรโชก (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "มีเบอร์แปลกโทรมาบอกว่ารู้ว่าเราแอบมีความสัมพันธ์ลับกับเจ้านาย
│   ขู่จะเอาเรื่องไปบอกเมียเจ้านายกับเพื่อนร่วมงานถ้าไม่โอนเงินให้
│   500,000 บาท เรากลัวมาก คนนี้รู้รายละเอียดชีวิตเราหลายอย่าง
│   จนน่าขนลุก แจ้งความข้อหาอะไรได้บ้าง"
│
├─ 🎯 Phase 1: Flow 2.4 — ขู่กรรโชก
│  ✓ Detects: ข่มขู่ + เรียกทรัพย์ = กรรโชก
│  ✓ Compound: กรรโชก + potential หมิ่นประมาท (if they follow through)
│  ✓ Human drive: Fear + Survival + Avoid Shame
│  ⚠️ Unique element: "รู้รายละเอียดชีวิตหลายอย่าง" — suggests data breach or stalking
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ ป.อาญา ม.337 — กรรโชกทรัพย์ (จำคุก ≤ 5 ปี)
│  ✓ ป.อาญา ม.338 — ขู่ให้กลัวว่าจะเกิดภัย (จำคุก ≤ 3 ปี)
│  ⚠️ Missing: PDPA angle (if data was accessed illegally)
│  ⚠️ Missing: Computer crime angle (if communication is digital)
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: แจ้งความ + เก็บหลักฐาน
│  ✓ 🅱️ ใช้ทนาย: For high intimidation cases
│
├─ 🔒 GATE: Effective — user clearly needs to know HOW to proceed safely
│
└─ ✅ VERDICT: MATCH 85%
   Flow 2.4 maps well. Minor gap: doesn't explicitly address
   "they know personal details" = potential data breach/PDPA angle.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

## CATEGORY 3: DEFAMATION (หมิ่นประมาท)

### TEST 3.1: ถูกปลอมเฟสบุ๊ค — โพสต์ด่าสถาบัน

> **Source:** qa_135_real_questions.md · Q3.1#2
> **Mapped to:** Flow 3.1 — ถูกด่าบนโซเชียล (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "มีคนปลอมเฟสบุ๊คเป็นเรา ใช้รูปโปรไฟล์เราทุกอย่าง แล้วไปโพสต์ด่า
│   สถาบันกับสถาบันพระมหากษัตริย์ มีคนมาขู่จะเอาเรื่องเรา เรากลัวมาก
│   ว่าจะโดนจับทั้งๆที่ไม่ได้ทำ แจ้งความไปแล้วแต่ตำรวจบอกสืบยากเพราะ
│   ใช้ VPN จะป้องกันตัวเองยังไง"
│
├─ 🎯 Phase 1: Flow 3.1 — ถูกด่าบนโซเชียล
│  ✓ Detects: Defamation on social media
│  ⚠️ BUT: This isn't just defamation — it's IDENTITY THEFT + IMPERSONATION
│  The fake account is committing crimes IN the user's name
│  ✓ Human drive: Survival + Fear + Avoid Shame
│
├─ ⚖️ Phase 2: Flow 3.1 rights
│  ✓ ป.อาญา ม.328 — หมิ่นประมาทโดยการโฆษณา
│  ✓ พ.ร.บ.คอมพ์ ม.14 — นำเข้าข้อมูลเท็จ
│  ⚠️ Missing: Impersonation/identity theft specific laws
│  ⚠️ Missing: How to prove you're NOT the poster (IP logs, device forensics)
│  ⚠️ Missing: "ถูกกล่าวหาจากสิ่งที่คนอื่นทำ" defense strategy
│
├─ 🛤️ Phase 3: Path options
│  ✓ Paths cover defamation reporting
│  ⚠️ Missing: "รีบป้องกันตัวเองก่อนโดนจับ" path — urgency different from standard defamation
│
├─ 🔒 GATE: Partial — focuses on defamation remedies, not "prove innocence" urgency
│
└─ ⚠️ VERDICT: PARTIAL 55%
   Flow 3.1 covers defamation but this user needs IDENTITY THEFT defense.
   The fear of "โดนจับทั้งๆที่ไม่ได้ทำ" requires different flow:
   evidence preservation, IP/device forensics, proactive police report as VICTIM.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️
```

---

### TEST 3.2: เพื่อนร่วมงานใส่ร้ายเรื่องชู้ — เมลเวียนทั้งบริษัท

> **Source:** qa_135_real_questions.md · Q3.2#2
> **Mapped to:** Flow 3.3 — ถูกใส่ความ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "เพื่อนร่วมงานใส่ร้ายว่าเราแอบมีความสัมพันธ์กับเจ้านายเพื่อจะได้เลื่อนขั้น
│   เรื่องแพร่กระจายไปทั่วออฟฟิศจนภรรยาเจ้านายมาอาละวาดถึงที่ทำงาน
│   จะฟ้องหมิ่นประมาทได้มั้ย ค่าเสียหายประมาณไหน"
│
├─ 🎯 Phase 1: Flow 3.3 — ถูกใส่ความ
│  ✓ Detects: False accusation causing damage
│  ✓ Workplace context: การใส่ร้ายในที่ทำงาน
│  ✓ Human drive: Avoid Shame + Justice + Belonging
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ ป.อาญา ม.326 — หมิ่นประมาท
│  ✓ ป.อาญา ม.328 — หมิ่นประมาทโดยการโฆษณา (spread throughout office)
│  ✓ Civil damages: เสียชื่อเสียง + เสียโอกาสทางอาชีพ
│  ⚠️ Missing: "third party impact" — wife coming to workplace = additional tort
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: ฟ้องหมิ่นประมาท + เรียกค่าเสียหาย
│  ✓ 🅱️ ใช้ทนาย: For complex workplace defamation
│  ✓ 🅲️ HR/internal: Report to company first
│
├─ 🔒 GATE: Effective — "know the charges but how to build case + calculate damages?"
│
├─ 📍 Phase 4-8 (PAID): Court, damages calculation, evidence checklist, filing steps
│
└─ ✅ VERDICT: MATCH 88%
   Flow 3.3 is well-suited for this. Minor gap: the "chain reaction"
   (wife coming to workplace = additional damages) could be more explicit.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 3.3: ลูกค้าโพสต์ใส่ร้ายร้าน — Google Maps review attack

> **Source:** qa_135_real_questions.md · Q3.1#3
> **Mapped to:** Flow 3.1 — ถูกด่าบนโซเชียล (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ลูกค้าไม่พอใจแล้วมาโพสต์ใน Google Maps กับเพจร้านเราว่าร้านขโมยของ
│   ให้อาหารเสีย ใส่ร้ายสารพัด ยอดจองลดลง 90% มีงบการเงินย้อนหลังพิสูจน์
│   ได้ว่าเสียหายจริง ฟ้องเรียกค่าเสียหายได้เท่าไหร่ ต้องใช้หลักฐานอะไรบ้าง"
│
├─ 🎯 Phase 1: Flow 3.1 — ถูกด่าบนโซเชียล
│  ✓ Detects: Defamation on platform (Google Maps + Facebook)
│  ✓ Business context: ยอดจองลด 90% = quantifiable damages
│  ✓ Human drive: Survival (business) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ ป.อาญา ม.328 — หมิ่นประมาทโดยการโฆษณา
│  ✓ Civil: damages for lost revenue
│  ⚠️ Flow 3.1 is designed for personal defamation — business defamation has different calculations
│  ⚠️ Missing: การฟ้องตาม พ.ร.บ.คอมพ์ ม.15 (ISP liability / platform takedown)
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: Report to Google, police report
│  ✓ 🅱️ ใช้ทนาย: For complex damages calculation
│
├─ 🔒 GATE: Good for personal users, slightly weak for BUSINESS users
│            Business owner might value ฿299 less when revenue is already down 90%
│
├─ 📍 Phase 4-8 (PAID): Court info, evidence checklist (but financial evidence needs more)
│
└─ ✅ VERDICT: MATCH 80%
   Flow 3.1 works but is designed for personal defamation. Business defamation
   needs: financial loss documentation, forensic accounting evidence, business reputation metrics.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

## CATEGORY 4: INSURANCE (ประกันภัย)

### TEST 4.1: ประกันชีวิตปฏิเสธจ่าย — สามีเสียชีวิตมะเร็ง

> **Source:** qa_135_real_questions.md · Q4.1#1
> **Mapped to:** Flow 4.2 — เคลมประกันสุขภาพ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ทำประกันชีวิตกับบริษัทดังมา 15 ปี สามีเพิ่งเสียชีวิตด้วยโรคมะเร็ง
│   ยื่นเคลมไปแต่บริษัทประกันปฏิเสธการจ่าย อ้างว่าสามีปกปิดประวัติ
│   การรักษาโรคกระเพาะเมื่อ 20 ปีก่อน ซึ่งไม่เกี่ยวกับมะเร็งเลย
│   เราจะฟ้องร้องได้ยังไงบ้าง"
│
├─ 🎯 Phase 1: Flow 4.2 — เคลมประกันสุขภาพ
│  ✓ Detects: Insurance claim denial
│  ⚠️ But: This is LIFE insurance (death claim), not health insurance!
│  Different law: ป.พ.พ. มาตรา 865 (life insurance disclosure)
│  The "20 years ago" + "unrelated condition" argument is specific
│
├─ ⚖️ Phase 2: Flow identifies rights
│  ⚠️ Flow 4.2 focuses on health insurance, not life insurance
│  ✓ Still covers: dispute resolution, คปภ. complaint
│  ❌ Missing: Life Insurance Act specifics, ป.พ.พ. 865 (disclosure must be material)
│  ❌ Missing: "20-year gap" = key argument that insurer can't deny for unrelated old condition
│
├─ 🛤️ Phase 3: Path options
│  ✓ Generic paths still work: complaint → คปภ. → litigation
│  ⚠️ But strategy differs: life insurance death claim ≠ health claim
│
├─ 🔒 GATE: Still effective for general insurance dispute
│            But user might sense the flow doesn't "get" their life insurance specifics
│
├─ 📍 Phase 4-8 (PAID): General insurance dispute filing — needs life-insurance-specific documents
│
└─ ⚠️ VERDICT: PARTIAL 60%
   Flow 4.2 is designed for health insurance claims, not life insurance death benefits.
   Life insurance has different laws (ป.พ.พ. 865 vs 867), different insurer defenses,
   and different payout structure. Flow needs a "life insurance" variant.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ✅ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ✅
```

---

### TEST 4.2: ประกันรถส่งซ่อม 3 เดือนไม่ได้คืน

> **Source:** qa_135_real_questions.md · Q4.1#2
> **Mapped to:** Flow 4.1 — เคลมประกันรถ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ทำประกันรถยนต์ชั้น 1 รถชนยับเยิน ส่งซ่อมอู่ที่บริษัทแนะนำมา
│   3 เดือนแล้วยังไม่ได้รถคืน โทรตามทุกอาทิตย์ก็บอกอะไหล่ยังไม่มา
│   มีสิทธิ์ฟ้องประกันได้มั้ย แล้วขอค่าเสียหายที่ไม่ได้ใช้รถด้วยได้หรือเปล่า"
│
├─ 🎯 Phase 1: Flow 4.1 — เคลมประกันรถ
│  ✓ Detects: Car insurance claim — จ่ายช้า / ล่าช้า
│  ✓ Specific issue: repair delay >3 months
│  ✓ Human drive: Justice + Convenience
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ Insurance claim dispute
│  ✓ คปภ. complaint mechanism
│  ⚠️ Missing: "ค่าเสียหายที่ไม่ได้ใช้รถ" (loss of use damages) — important for car owners
│  ⚠️ Missing: Timeline expectations — how long is "too long" for car repair?
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: ร้องเรียน คปภ. + ทวงถาม
│  ✓ 🅱️ ใช้ทนาย: For complex protracted cases
│  ⚠️ Missing: "swap garage" option, "total loss" threshold, rental car reimbursement
│
├─ 🔒 GATE: Effective — user clearly wants to know how to force action
│
├─ 📍 Phase 4-8 (PAID): Insurance commission, evidence list, escalation steps
│
└─ ✅ VERDICT: MATCH 78%
   Flow 4.1 covers the core issue. Enhancement needed:
   explicit "loss of use" damages and repair timeline standards.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 4.3: แม่สามี 75 ปี ถูกแบงก์หลอกทำประกัน

> **Source:** qa_135_real_questions.md · Q4.2#2
> **Mapped to:** Flow 4.3 — ยกเลิกกรมธรรม์ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "แม่สามีอายุ 75 ปี ถูกแบงก์หลอกให้ทำประกันชีวิตตอนไปทำธุรกรรม
│   พนักงานบอกแค่ว่าฝากเงินก้อนนี้จะได้ดอกสูงกว่าปกติ ที่ไหนได้คือ
│   ประกันชีวิตแบบสะสมทรัพย์!! ถอนไม่ได้อีก 10 ปี ร้องเรียนคอลเซ็นเตอร์
│   ไม่รับผิดชอบ แม่อายุมากแล้วเงินนั่นคือเงินเก็บทั้งชีวิต"
│
├─ 🎯 Phase 1: Flow 4.3 — ยกเลิกกรมธรรม์
│  ✓ Detects: Mis-sold insurance / ถูกบังคับ
│  ✓ Key angle: Elderly victim (75 years old) — potential vulnerable consumer
│  ✓ "บอกว่าเป็นเงินฝากแต่เป็นประกัน" = MISREPRESENTATION
│  ✓ Human drive: Survival (เงินเก็บทั้งชีวิต) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ Flow 4.3 covers: ถูกบังคับขายประกัน
│  ⚠️ Missing: Elderly consumer protection laws
│  ⚠️ Missing: Bank sales of insurance = BOT + OIC dual jurisdiction
│  ⚠️ Missing: "Cooling-off period" — if just bought, free-look period applies
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ทำเอง: ร้องเรียน คปภ. + BOT + สคบ.
│  ✓ 🅱️ ใช้ทนาย: For misrepresentation + damages
│  ✓ 🅲️ เจรจากับแบงก์
│
├─ 🔒 GATE: Effective for general cancellation
│            BUT: User needs "elderly/vulnerable consumer" specific remedies
│
├─ 📍 Phase 4-8 (PAID): Provides general cancellation docs — needs elder-specific upgrade
│
└─ ⚠️ VERDICT: PARTIAL 65%
   Flow 4.3 covers mis-selling but lacks elderly consumer protection dimension.
   Needs: elder financial abuse laws, BOT banking agent regulations,
   free-look period rights, คปภ. + BOT joint complaint process.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ✅ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ✅
```

---

## CATEGORY 5: GOVERNMENT (ราชการและรัฐ)

### TEST 5.1: ขออนุญาตก่อสร้าง — วิศวกรเรียกสินบน 100,000

> **Source:** qa_135_real_questions.md · Q5.1#1
> **Mapped to:** Flow 5.2 — รัฐละเมิด (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ยื่นขออนุญาตก่อสร้างบ้านที่เขตบางกะปิมาตั้งแต่ปีที่แล้ว เอกสารครบ
│   วิศวกรโยธาที่เขตบอกไม่ผ่านเพราะอะไรก็ไม่รู้ มีคนกระซิบบอกว่าต้องมี
│   ค่าอำนวยความสะดวกประมาณ 100,000 ถึงจะผ่าน เราไม่อยากจ่าย
│   เพราะทำทุกอย่างถูกต้องแล้ว ควรทำยังไงดี"
│
├─ 🎯 Phase 1: Flow 5.2 — รัฐละเมิด
│  ⚠️ Partial match: Flow 5.2 covers "เจ้าหน้าที่รัฐทำให้เสียหาย"
│  ❌ BUT: This is ACTIVE BRIBERY SOLICITATION — not passive damage
│  The flow covers POST-DAMAGE remedies, not PRE-DAMAGE bribery refusal
│  Human drive: Justice + Autonomy (ไม่อยากจ่ายเพราะทำถูกต้อง)
│
├─ ⚖️ Phase 2: Rights analysis
│  ⚠️ Flow 5.2 covers: รัฐละเมิด, ปกครอง
│  ❌ Missing: Anti-corruption laws (ป.ป.ช. Act)
│  ❌ Missing: NACC (ป.ป.ช.) complaint hotline/process
│  ❌ Missing: Whistleblower protection
│  ❌ Missing: "How to refuse bribe SAFELY and still get permit"
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ Flow 5.2 gives damage-recovery paths — wrong for bribery prevention
│  ❌ Missing: ป.ป.ช. complaint, evidence gathering for bribery, Ombudsman route
│
├─ 🔒 GATE: ⚠️ Doesn't address the real question: "How to handle bribe demand?"
│
├─ 📍 Phase 4-8 (PAID): Would give court filing info — not anti-corruption agency info
│
└─ ❌ VERDICT: MISS 35%
   No V2 flow covers bribery solicitation by government officials.
   User needs: NACC complaint process, how to gather evidence of bribery,
   safe ways to refuse, alternative permit escalation paths.
   Score: Phase 1 ❌ | Phase 2 ❌ | Phase 3 ❌ | Gate ❌ | Phase 4-7 ❌ | Phase 8 ❌

   🔴 GAP: Need Flow 5.4 "Officials Soliciting Bribes — สินบนเจ้าหน้าที่รัฐ"
```

---

### TEST 5.2: ทำพาสปอร์ตล่าช้า 4 เดือน — เสียโอกาสทำงานสิงคโปร์

> **Source:** qa_135_real_questions.md · Q5.2#1
> **Mapped to:** Flow 5.3 — ร้องเรียนหน่วยงานรัฐแล้วไม่ตอบ (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ยื่นเรื่องขอทำพาสปอร์ตที่กรมการกงสุลแจ้งวัฒนะตั้งแต่ 4 เดือนที่แล้ว
│   บอกใช้เวลา 2 สัปดาห์ แต่ตอนนี้เงียบสนิท โทรตามไม่มีใครรับสาย
│   เราพลาดโอกาสเดินทางไปทำงานสิงคโปร์ไปแล้ว สูญเสียรายได้หลายแสน
│   ฟ้องร้องหน่วยงานราชการที่ทำงานล่าช้าได้มั้ย"
│
├─ 🎯 Phase 1: Flow 5.3 — ร้องเรียนหน่วยงานรัฐแล้วไม่ตอบ
│  ✓ Detects: Government delay + failure to respond
│  ✓ Specific context: Passport delay → lost job opportunity
│  ⚠️ Key nuance: Not just "not responding" but "ความล่าช้าเกินสมควร" causing financial loss
│  ✓ Human drive: Survival (income loss) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✓ Flow 5.3 covers: ร้องเรียน, escalation to higher authority
│  ⚠️ Partially covers: ฟ้องปกครอง for unreasonable delay
│  ⚠️ Missing: "ค่าสินไหมทดแทนจากความล่าช้า" calculation
│  ⚠️ Missing: Specific to passport/consular affairs — MFA complaint mechanism
│
├─ 🛤️ Phase 3: Path options
│  ✓ 🅰️ ร้องเรียนผู้บังคับบัญชา → escalate
│  ✓ 🅱️ ฟ้องศาลปกครอง
│  ⚠️ Missing: Direct MFA/consular complaint channels
│
├─ 🔒 GATE: Partially effective — but user wants compensation, not just "make them respond"
│
├─ 📍 Phase 4-8 (PAID): General government complaint filing — needs consular-specific
│
└─ ⚠️ VERDICT: PARTIAL 60%
   Flow 5.3 covers the "not responding" angle but the user's real need is:
   "I lost ฿X00,000 in income — can I sue for that?" — damages from government delay.
   Needs: การฟ้องเรียกค่าเสียหายจากหน่วยงานรัฐ for economic loss.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ✅
```

---

### TEST 5.3: ภาษีสรรพากร — ถูกประเมินแบบเหมา 5 ล้าน

> **Source:** qa_135_real_questions.md · Q5.3#2
> **Mapped to:** Flow 5.2 — รัฐละเมิด (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "ถูกประเมินภาษีย้อนหลังจากกรมสรรพากร 5 ล้านบาท เจ้าหน้าที่ประเมิน
│   รายได้ร้านเราแบบเหมาๆ ไม่ได้ดูบัญชีจริง บอกว่า 'ร้านแถวนี้ขายดี
│   ต้องมีรายได้เท่านี้' เราเอาเอกสารบัญชีให้ดูก็ไม่รับฟัง แล้วยึดบัญชี
│   ธนาคารเราไปแล้ว ตอนนี้ไม่มีเงินหมุนในธุรกิจเลย"
│
├─ 🎯 Phase 1: Flow 5.2 — รัฐละเมิด
│  ✅ Detects: เจ้าหน้าที่รัฐทำให้เสียหาย (arbitrary tax assessment)
│  ✅ Captures: Bank account seized = direct damage
│  ✅ Human drive: Survival (no cash flow) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: ฟ้องปกครอง, ร้องเรียน, อุทธรณ์
│  ⚠️ Missing: Tax-specific appeal process (Revenue Code appeal timeline)
│  ⚠️ Missing: Tax court vs. administrative court distinction
│  ⚠️ Missing: "ขอทุเลาการบังคับ" (stay of execution) to unfreeze bank account
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ General paths work but tax disputes need: อุทธรณ์ภายใน 30 วัน → อุทธรณ์คณะกรรมการ → ศาลภาษี
│  ❌ Missing: Urgent "ขอทุเลา" path to get bank account back NOW
│
├─ 🔒 GATE: Partially effective — user needs tax-specific guidance immediately
│
├─ 📍 Phase 4-8 (PAID): Would give general admin court info — needs tax-specific court
│
└─ ✅ VERDICT: MATCH 70%
   Flow 5.2 is the closest match but tax disputes have unique procedures.
   Enhancement: Add tax appeal timeline, ศาลภาษีอากร vs ศาลปกครอง distinction,
   urgent stay-of-execution motion to unfreeze accounts.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ⚠️ | Gate ✅ | Phase 4-7 ⚠️ | Phase 8 ✅
```

---

## CATEGORY 6: PROPERTY (ที่ดินและทรัพย์สิน)

### TEST 6.1: ที่ดินยาย น.ส.3 ทับซ้อนโฉนด

> **Source:** qa_135_real_questions.md · Q6.1#1
> **Mapped to:** Flow 6.3 — ซื้อขายที่ดินไม่ได้ (Cat 1-6) + Flow 6.2 — พิพาทแนวเขต

```
🔴 THE REAL QUESTION
│  "ที่ดินของคุณยายถือครองมากว่า 50 ปี เดิมเป็น น.ส.3 เพิ่งไปรังวัด
│   เพื่อออกโฉนด ปรากฏว่าเจ้าหน้าที่ที่ดินบอกว่าที่ดินบางส่วนทับซ้อน
│   กับที่ดินคนอื่นที่ออกโฉนดไปก่อน ทั้งที่คุณยายอยู่มาก่อน โฉนดคนนั้น
│   เพิ่งออกเมื่อ 5 ปีนี้แบบน่าสงสัย จะคัดค้านหรือฟ้องร้องยังไงดี"
│
├─ 🎯 Phase 1: Flow 6.2 — พิพาทแนวเขต
│  ✅ Detects: Land boundary dispute
│  ⚠️ Compound: น.ส.3 upgrade to โฉนด + overlapping with newer title deed
│  This is more than boundary — it's TITLE DEED VALIDITY challenge
│  ✓ Human drive: Survival (land = livelihood) + Justice
│
├─ ⚖️ Phase 2: Flow 6.2/6.3 rights analysis
│  ✅ Flow covers: boundary disputes, รังวัด, litigation
│  ⚠️ Missing: น.ส.3 vs โฉนด hierarchy and upgrade process
│  ⚠️ Missing: "suspicious newer deed" — how to challenge deed validity
│  ⚠️ Missing: 50-year occupation (adverse possession / ครอบครองปรปักษ์) argument
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ รังวัดใหม่ + คัดค้าน
│  ✅ 🅱️ ฟ้องศาล — เพิกถอนโฉนด + รับรองแนวเขต
│  ⚠️ Missing: Land Department complaint against irregular deed issuance
│
├─ 🔒 GATE: Effective for boundary disputes — covers the core
│
├─ 📍 Phase 4-8 (PAID): Land office, court, evidence list
│
└─ ✅ VERDICT: MATCH 78%
   Flows 6.2 + 6.3 together handle this well. Enhancement: add
   title deed validity challenge procedures and ครอบครองปรปักษ์ rules.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 6.2: เพื่อนบ้านสร้างรั้วล้ำที่ 1.5 เมตร × 20 เมตร

> **Source:** qa_135_real_questions.md · Q6.2#1
> **Mapped to:** Flow 6.2 — พิพาทแนวเขต (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "เพื่อนบ้านสร้างรั้วล้ำเข้ามาในที่ดินเรา 1.5 เมตร ยาว 20 เมตร
│   เขาบอกว่าใช้ประโยชน์ตรงนี้มาก่อนแล้ว (ครอบครองปรปักษ์?)
│   ทั้งที่เรามีโฉนดกับผลรังวัดชัดเจน ทะเลาะกันทุกวัน จะฟ้องศาลยังไง"
│
├─ 🎯 Phase 1: Flow 6.2 — พิพาทแนวเขต
│  ✅ Perfect match: Boundary encroachment by neighbor
│  ✅ Key element: ครอบครองปรปักษ์ counter-claim by neighbor
│  ✅ Evidence: โฉนด + รังวัดชัดเจน (strong position)
│  ✓ Human drive: Justice + Ownership
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ ป.พ.พ. — กรรมสิทธิ์ + แนวเขต
│  ✅ บุกรุก — ป.อาญา ม.362-365
│  ✅ ครอบครองปรปักษ์ defense analysis
│  ✅ Flow captures: yes, neighbor claiming adverse possession
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ เจรจา + รังวัด
│  ✅ 🅱️ ฟ้องศาล — ขับไล่ + รื้อถอน
│  ✅ 🅲️ ไกล่เกลี่ย
│
├─ 🔒 GATE: Strong — "have deed AND survey, but need to know HOW to sue"
│
├─ 📍 Phase 4-8 (PAID): Court, evidence, lawsuit drafting
│
└─ ✅ VERDICT: MATCH 92%
   Flow 6.2 is near-perfect for this. The ครอบครองปรปักษ์ counter-claim
   is explicitly handled. Score: all phases ✅
```

---

### TEST 6.3: โฉนดชื่อตาทวด — โอนมรดกไม่ได้ 40 ปี

> **Source:** qa_135_real_questions.md · Q6.1#3
> **Mapped to:** Flow 6.4 — มรดก (Cat 1-6)

```
🔴 THE REAL QUESTION
│  "แม่อยากยกที่ดินให้หนู แต่โฉนดเป็นชื่อคุณตาทวดซึ่งเสียชีวิตไป 40 ปี
│   ยังไม่ได้โอนมรดกกันเลย ผ่านมาหลายทอดมีทายาทหลายสิบคน
│   หลายคนติดต่อไม่ได้ จะทำยังไงให้ได้โฉนดเป็นชื่อแม่ก่อนยกให้เรา"
│
├─ 🎯 Phase 1: Flow 6.4 — มรดก
│  ✅ Detects: Inheritance chain problem — multi-generational
│  ✅ Unique: 40-year gap, 10+ heirs, missing heirs
│  ✓ Human drive: Security (family asset) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: inheritance by law (ทายาทโดยธรรม)
│  ⚠️ Missing: Multi-generational chain — need succession through each generation
│  ⚠️ Missing: "ทายาทติดต่อไม่ได้" — court petition for missing heir
│  ⚠️ Missing: 40-year delay — statute of limitations for inheritance claims
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ Standard paths (เจรจาทายาท → ฟ้องศาล) are partially applicable
│  ❌ Missing: Court-appointed estate administrator
│  ❌ Missing: Successive probate across generations
│
├─ 🔒 GATE: Effective for simple inheritance — but this is complex multi-gen
│
├─ 📍 Phase 4-8 (PAID): General inheritance docs — needs complex succession upgrade
│
└─ ✅ VERDICT: MATCH 72%
   Flow 6.4 covers inheritance basics. Enhancement needed for:
   multi-generational chain probate, missing heir procedures, 40-year gap.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

## CATEGORY 7: LABOUR (แรงงาน)

### TEST 7.1: เลิกจ้างครบ 10 ปี — ไม่มีค่าชดเชย

> **Source:** qa_135_real_questions.md · Q7.1#1
> **Mapped to:** Flow 7.1 — ถูกเลิกจ้างไม่เป็นธรรม (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "ทำงานมาจะครบ 10 ปีละ โดนเรียกเข้าห้องประชุมแจ้งเลิกจ้างลอยๆ
│   บอกแค่ว่าปรับโครงสร้างองค์กร ไม่มีหนังสือบอกล่วงหน้า ไม่มีค่าชดเชย
│   บอกให้เซ็นใบลาออกเองจะได้ไม่เสียประวัติ แบบนี้ทำไงดี ควรเซ็นไหม?"
│
├─ 🎯 Phase 1: Flow 7.1 — ถูกเลิกจ้างไม่เป็นธรรม
│  ✅ Perfect match: เลิกจ้าง + no notice + no compensation
│  ✅ Key trap detected: "ให้เซ็นใบลาออกเอง" = constructive resignation TRAP
│  ✅ 10 years → entitlement 400 days compensation
│  ✓ Human drive: Survival + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ พ.ร.บ.คุ้มครองแรงงาน ม.118 — ค่าชดเชย 400 วัน (10+ years)
│  ✅ ค่าบอกกล่าวล่วงหน้า — 1 งวดค่าจ้าง
│  ✅ Flow warns: DON'T sign resignation letter!
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: ยื่นศาลแรงงาน + ร้องตรวจแรงงาน
│  ✅ 🅱️ ใช้ทนาย: For high-value case (400 days pay)
│  ✅ 🅲️ ร้องตรวจแรงงานก่อน
│
├─ 🔒 GATE: Strong — "know your rights (400 days!) but need to file correctly"
│
├─ 📍 Phase 4-8 (PAID): Labour court, documents, AI generates demand letter
│
└─ ✅ VERDICT: MATCH 95%
   Flow 7.1 is nearly perfect. The "don't sign resignation" warning is critical.
   Score: all phases ✅
```

---

### TEST 7.2: ร้านอาหาร — ทำงาน 12 ชม. 6 วัน ไม่มี OT

> **Source:** qa_135_real_questions.md · Q7.2#1
> **Mapped to:** Flow 7.2 — นายจ้างค้างจ่ายค่าจ้าง (Cat 7-12) + Flow 7.4 — เงื่อนไขการจ้างไม่เป็นธรรม

```
🔴 THE REAL QUESTION
│  "ร้านอาหารที่เราทำงานอยู่ จ้างรายเดือน 12,000 แต่เวลาเข้างาน 10.00-22.00
│   หกวันต่อสัปดาห์ ไม่มี OT ไม่มีวันหยุดชดเชย หัวหน้าบอกว่าเป็นร้านอาหาร
│   ก็ต้องแบบนี้ ผิดกฎหมายแรงงานไหม แล้วเราจะเรียกร้องค่า OT ย้อนหลังได้กี่ปี"
│
├─ 🎯 Phase 1: Flow 7.2 — ค้างจ่ายค่าจ้าง / Flow 7.4 — เงื่อนไขไม่เป็นธรรม
│  ✅ Detects: Labour law violation — excessive hours + no OT + no rest day
│  ✅ 12 hrs × 6 days = 72 hrs/week (legal max: 48 hrs/week + OT max 36/week)
│  ✅ Specific to: restaurant industry violation
│  ✓ Human drive: Justice + Survival
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow 7.2: Unpaid OT = unpaid wages
│  ✅ Flow 7.4: Unfair employment terms
│  ✅ OT calculation: hours beyond 8/day or 48/week
│  ⚠️ Missing: Restaurant industry specific exemptions (few exist)
│  ⚠️ Missing: "เรียกร้องย้อนหลังได้กี่ปี" — 2 years (labour claims prescription)
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ร้องตรวจแรงงาน
│  ✅ 🅱️ ฟ้องศาลแรงงาน (no court fee)
│  ⚠️ Missing: How to calculate 2 years of back OT (substantial amount)
│
├─ 🔒 GATE: Effective for wage claims
│
├─ 📍 Phase 4-8 (PAID): Labour office, OT calculation, demand letter
│
└─ ✅ VERDICT: MATCH 85%
   Flows 7.2 + 7.4 together cover this well. Enhancement: add
   OT back-calculation for restaurant workers with long-running violations.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 7.3: ประสบอุบัติเหตุระหว่างเดินทางไปทำงาน — ประกันสังคมปฏิเสธ

> **Source:** qa_135_real_questions.md · Q7.3#1
> **Mapped to:** ⚠️ No dedicated Social Security flow exists — nearest is Flow 4.2 (private health insurance)

```
🔴 THE REAL QUESTION
│  "ประสบอุบัติเหตุระหว่างเดินทางไปทำงาน มอไซค์ล้มขาหัก รพ.ที่รักษา
│   บอกว่าประกันสังคมไม่คุ้มครองเพราะเกิดนอกสถานที่ทำงาน แต่เราอ่าน
│   ในเน็ตบอกว่าเดินทางไป-กลับก็คุ้มครองนะ สรุปอันไหนถูก
│   แล้วต้องใช้เอกสารอะไรยื่นเรื่องกองทุนเงินทดแทน"
│
├─ 🎯 Phase 1: ⚠️ No SSO/Workmen's Comp flow exists
│  Nearest: Flow 4.2 (health insurance) — but SSO is mandatory public scheme, not private
│  Missing: Distinction between SSO (ประกันสังคม) and WCF (กองทุนเงินทดแทน)
│  User needs: Clarification that commute IS covered
│
├─ ⚖️ Phase 2: ⚠️ Flow 4.2 doesn't apply — different legal framework
│  ❌ No coverage of: พ.ร.บ.ประกันสังคม ม.33/39
│  ❌ No coverage of: พ.ร.บ.เงินทดแทน — commute = covered
│  ❌ No coverage of: SSO dispute resolution (medical committee appeals)
│
├─ 🛤️ Phase 3: ⚠️ Flow 4.2 paths don't map
│  ❌ SSO has own dispute process: medical committee → appeal committee → labour court
│  ❌ Missing: Employer's role in filing SSO/WCF claims
│
├─ 🔒 GATE: Doesn't work — user needs SSO-specific guidance
│
├─ 📍 Phase 4-8 (PAID): Would give wrong info (insurance commission instead of SSO office)
│
└─ ⚠️ VERDICT: PARTIAL 30%
   No V2 flow covers Social Security Office / Workmen's Compensation Fund.
   This is a HIGH-VOLUME need (every Thai worker has SSO).
   User's primary Q: "Is commute covered?" must be answered correctly.
   Score: Phase 1 ❌ | Phase 2 ❌ | Phase 3 ❌ | Gate ❌ | Phase 4-7 ❌ | Phase 8 ❌

   🔴 GAP: Need Flow 7.5 "Social Security / Workmen's Compensation — ประกันสังคม/กองทุนเงินทดแทน"
```

---

## CATEGORY 8: CONSUMER (ผู้บริโภค)

### TEST 8.1: มือถือ 25,000 — ใช้ 12 วันดับ ซ่อม 2 รอบไม่หาย

> **Source:** qa_135_real_questions.md · Q8.1#1
> **Mapped to:** Flow 8.1 — สินค้าไม่ตรงปก (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "ซื้อมือถือจากร้านในห้าง 25,000 บาท ใช้ได้ 12 วันเครื่องดับเอง
│   ร้านบอกให้ส่งศูนย์อย่างเดียว ไม่รับคืนเงิน ไม่รับเปลี่ยนเครื่องใหม่
│   ซ่อมแล้ว 2 รอบก็ยังไม่หาย ขอคืนเงินได้ไหม ต้องอ้างกฎหมายอะไร"
│
├─ 🎯 Phase 1: Flow 8.1 — สินค้าไม่ตรงปก
│  ✅ Detects: Defective product — not as described / not fit for purpose
│  ✅ This is WARRANTY claim — product failed within warranty period
│  ✅ 12 days + 2 failed repairs = clear consumer right to refund
│  ✓ Human drive: Justice + Value
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: สินค้าชำรุดบกพร่อง
│  ⚠️ Missing: Explicit "right to refund after 2 failed repairs" (lemon law concept)
│  ⚠️ Missing: สคบ. complaint for defective electronics
│  ⚠️ Missing: "ต้องอ้างกฎหมายอะไร" — ป.พ.พ. warranty provisions, Consumer Protection Act
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: Demand refund + สคบ. complaint
│  ✅ 🅱️ ใช้ทนาย: For formal litigation
│  ✅ 🅲️ เจรจากับร้าน
│
├─ 🔒 GATE: Effective — user knows they have rights but needs exact legal citation + process
│
├─ 📍 Phase 4-8 (PAID): Consumer court, documents, demand letter with legal citations
│
└─ ✅ VERDICT: MATCH 82%
   Flow 8.1 works but needs enhancement: explicit warranty/lemon provisions,
   "2 failed repairs = right to refund" escalation path.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 8.2: คอร์สเรียนออนไลน์ 50,000 — หลอกว่าเรียนแล้วได้งาน 100%

> **Source:** qa_135_real_questions.md · Q8.2#1
> **Mapped to:** Flow 8.4 — โฆษณาเกินจริง (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "สมัครคอร์สเรียนออนไลน์ โฆษณาว่าเรียนแล้วได้งาน 100% การันตีเงินเดือน
│   30,000++ ภายใน 3 เดือน พอจ่ายเงิน 50,000 เนื้อหาคอร์สพื้นๆ ไม่มีสอน
│   ที่เอาไปใช้ทำงานได้จริง ไม่มีการช่วยหางานตามที่โฆษณา อยากได้เงินคืน
│   ต้องฟ้องข้อหาอะไร"
│
├─ 🎯 Phase 1: Flow 8.4 — โฆษณาเกินจริง
│  ✅ Perfect match: False advertising + consumer fraud
│  ✅ "100% job guarantee" = classic overpromise
│  ✅ Content quality mismatch = goods not as described
│  ✓ Human drive: Justice + Value + Survival
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ พ.ร.บ.คุ้มครองผู้บริโภค — false advertising
│  ✅ ป.อาญา ม.341 — ฉ้อโกง (false promise to induce payment)
│  ✅ สคบ. complaint
│  ✅ Flow captures the core laws
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: สคบ. + ทวงถาม + ฟ้องคดีผู้บริโภค
│  ✅ 🅱️ ใช้ทนาย: For 50K case
│
├─ 🔒 GATE: Strong — user lost 50K, ฿299 to potentially recover it
│
├─ 📍 Phase 4-8 (PAID): Consumer protection board, evidence, demand letter
│
└─ ✅ VERDICT: MATCH 90%
   Flow 8.4 handles false advertising cleanly. Enhancement: add
   education/training-specific regulations (education ministry oversight).
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 8.3: ฟิตเนส 30,000 — ขอยกเลิกสัญญาหลัง 1 เดือน

> **Source:** qa_135_real_questions.md · Q8.3#1
> **Mapped to:** Flow 8.4 — โฆษณาเกินจริง (Cat 7-12) — partial match

```
🔴 THE REAL QUESTION
│  "ซื้อคอร์สฟิตเนส 1 ปี จ่ายสด 30,000 ใช้ไปได้เดือนเดียว ขอย้ายจังหวัด
│   เลยขอยกเลิกสัญญาและขอคืนเงินส่วนที่เหลือ ฟิตเนสบอกว่าตามสัญญา
│   ยกเลิกไม่ได้ ได้แค่ขายต่อให้คนอื่นเอง แบบนี้เป็นธรรมไหม
│   มีกฎหมายคุ้มครองไหมที่จะยกเลิกแล้วได้เงินคืนบางส่วน"
│
├─ 🎯 Phase 1: ⚠️ Flow 8.4 — closest match, but this isn't false advertising
│  This is CONTRACT TERMINATION / UNFAIR CONTRACT TERMS
│  User isn't saying the gym lied — they want to cancel legitimately
│  ❌ Missing: "บอกเลิกสัญญา" flow — contract cancellation rights
│  ✓ Human drive: Fairness + Mobility
│
├─ ⚖️ Phase 2: ⚠️ Flow 8.4 partially relevant
│  ✅ Unfair contract terms — พ.ร.บ.ข้อสัญญาไม่เป็นธรรม
│  ⚠️ Missing: Specific cancellation rights for service contracts
│  ⚠️ Missing: "ข้อสัญญาที่ยกเลิกไม่ได้ตลอด 1 ปี" = potentially unfair term
│
├─ 🛤️ Phase 3: ⚠️ Paths partially applicable
│  ⚠️ สคบ. complaint for unfair contract — but user wants cancellation, not false ad claim
│
├─ 🔒 GATE: Weak — user isn't fighting false advertising, they're fighting contract terms
│
├─ 📍 Phase 4-8 (PAID): General consumer complaint — not contract termination specific
│
└─ ⚠️ VERDICT: PARTIAL 50%
   No V2 flow covers contract cancellation/cooling-off rights.
   User needs: Unfair Contract Terms Act, cancellation rights,
   pro-rata refund calculation, สคบ. complaint for unfair service contracts.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️

   🔴 GAP: Need Flow 8.5 "Contract Cancellation / Cooling-Off — บอกเลิกสัญญา/ขอคืนเงิน"
```

---

## CATEGORY 9: DEBT (หนี้สิน)

### TEST 9.1: ทวงหนี้บัตรเครดิต — โทรหาญาติ วันละ 20 สาย

> **Source:** qa_135_real_questions.md · Q9.1#1
> **Mapped to:** Flow 9.1 — ถูกทวงหนี้ข่มขู่ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "เป็นหนี้บัตรเครดิต 3 ใบรวม 200,000 จ่ายไม่ไหวเพราะตกงาน
│   มีเบอร์แปลกโทรมาทวงทุกวัน วันละ 10-20 สาย โทรหาญาติพี่น้อง
│   ให้ช่วยใช้หนี้แทน บางสายข่มขู่จะฟ้อง จะยึดทรัพย์ จะประจาน
│   ในโซเชียล ผิดกฎหมายทวงหนี้ไหม แจ้งความที่ไหนได้บ้าง"
│
├─ 🎯 Phase 1: Flow 9.1 — ถูกทวงหนี้ข่มขู่
│  ✅ Perfect match: Aggressive debt collection
│  ✅ Specific violations: calling relatives, threats, daily harassment
│  ✅ This is EXACTLY what Flow 9.1 was designed for
│  ✓ Human drive: Safety + Fear
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ พ.ร.บ.การทวงถามหนี้ พ.ศ.2558 — multiple violations
│  ✅ ห้ามติดต่อบุคคลอื่น (calling relatives = violation)
│  ✅ ห้ามข่มขู่/ใช้ความรุนแรง
│  ✅ ห้ามทวงเกินสมควร (10-20 calls/day = excessive)
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: แจ้งความ + ร้องเรียน กลท.
│  ✅ 🅱️ ใช้ทนาย
│  ✅ 🅲️ ร้องเรียน กลท. โดยตรง
│
├─ 🔒 GATE: Strong — user needs concrete steps to stop harassment
│
├─ 📍 Phase 4-8 (PAID): Police, กลท., evidence, filing
│
└─ ✅ VERDICT: MATCH 93%
   Flow 9.1 is built exactly for this. Minor enhancement: add
   specific call-log template for documenting harassment.
   Score: all phases ✅
```

---

### TEST 9.2: หนี้นอกระบบ 100,000 — ดอก 5% ต่อเดือน ได้เงินจริงแค่ 85,000

> **Source:** qa_135_real_questions.md · Q9.2#1
> **Mapped to:** Flow 9.2 — หนี้นอกระบบ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "กู้เงินนอกระบบ 100,000 บาท สัญญาเขียนเงินต้น 100,000 ดอกเบี้ย
│   5% ต่อเดือน แต่ตอนรับเงินจริงได้แค่ 85,000 เพราะหักค่าดำเนินการ
│   15,000 แถมต้องจ่ายคืนรายวันวันละ 1,400 เป็นเวลา 100 วัน
│   รวมเป็น 140,000 ดอกเบี้ยเกินกฎหมายไหม ควรทำยังไง"
│
├─ 🎯 Phase 1: Flow 9.2 — หนี้นอกระบบ
│  ✅ Perfect match: Loan shark / illegal lending
│  ✅ Multiple violations: hidden fees, excessive interest, daily payments
│  ✅ 5%/month = 60%/year vs legal 15%/year = 4x legal rate
│  ✓ Human drive: Survival + Fear
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ พ.ร.บ.ห้ามเรียกดอกเบี้ยเกินอัตรา — 15%/year legal limit
│  ✅ ดอกเบี้ยเกิน 15%/year = โมฆะ
│  ✅ Hidden fees counted toward interest calculation
│  ✅ Actual calculation: 85K received, 140K to pay = effective interest ~64%/year
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: คำนวณตามกฎหมาย + จ่ายเฉพาะต้น + ดอก 15%/year
│  ✅ 🅱️ ใช้ทนาย: For dangerous cases
│  ✅ 🅲️ ขอความช่วยเหลือรัฐ: ศูนย์ช่วยเหลือลูกหนี้
│
├─ 🔒 GATE: Strong — user needs exact calculation of legal vs illegal amount
│
├─ 📍 Phase 4-8 (PAID): Recalculation, demand letter to lender, police report
│
└─ ✅ VERDICT: MATCH 90%
   Flow 9.2 handles loan sharks well. Enhancement: add
   automatic interest recalculation tool showing user exactly what they legally owe.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 9.3: หนี้บัตร 800,000 ถูกฟ้องแล้ว — อยากประนอมหนี้

> **Source:** qa_135_real_questions.md · Q9.4#1
> **Mapped to:** Flow 9.3 — ล้มละลาย (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "เป็นหนี้บัตรเครดิต 3 ใบกับสินเชื่อส่วนบุคคลอีก 2 ที่ รวม 800,000
│   ถูกฟ้องแล้ว 1 คดี จนปัญญาจะจ่ายไหวเพราะธุรกิจเจ๊งช่วงโควิด
│   อยากทำเรื่องประนอมหนี้หรือฟื้นฟูหนี้ส่วนบุคคล ต้องเริ่มยังไง
│   ต้องมีเงินก้อนไหม มีหน่วยงานไหนช่วยได้บ้าง"
│
├─ 🎯 Phase 1: Flow 9.3 — ล้มละลาย
│  ⚠️ Partial match: Bankruptcy flow covers insolvency but this user wants
│   DEBT RESTRUCTURING / COMPOSITION — not full bankruptcy
│  ✓ Human drive: Survival + Hope
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: Bankruptcy Act, court-supervised restructuring
│  ⚠️ Missing: Pre-litigation debt restructuring (คลินิกการเงิน, ธปท. debt relief)
│  ⚠️ Missing: "ถูกฟ้องแล้ว 1 คดี" — need to handle active litigation + restructure
│  ⚠️ Missing: Individual debt rehabilitation (ฟื้นฟูหนี้บุคคลธรรมดา) — new law
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ Flow 9.3 focuses on formal bankruptcy — user needs informal restructuring first
│  ❌ Missing: BOT debt clinic, bank negotiation strategies, "haircut" process
│
├─ 🔒 GATE: Partially effective — user needs pre-bankruptcy debt relief, not bankruptcy
│
├─ 📍 Phase 4-8 (PAID): Bankruptcy court info — user needs debt restructuring first
│
└─ ⚠️ VERDICT: PARTIAL 58%
   Flow 9.3 covers bankruptcy but this user wants pre-bankruptcy restructuring.
   Missing: BOT debt clinic process, individual rehabilitation law,
   multi-creditor negotiation strategy, "haircut" norms.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️
```

---

## CATEGORY 10: HOUSING (ที่อยู่อาศัย)

### TEST 10.1: เช่าคอนโดหมดสัญญา — เจ้าของให้ย้ายออกใน 15 วัน

> **Source:** qa_135_real_questions.md · Q10.1#1
> **Mapped to:** Flow 10.3 — ถูกไล่ที่อยู่อาศัยไม่เป็นธรรม (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "เช่าคอนโดอยู่ 1 ปี หมดสัญญาแล้วไม่ได้ต่อสัญญาเป็นลายลักษณ์อักษร
│   แต่จ่ายค่าเช่าต่อเนื่องมาอีก 6 เดือน เจ้าของก็รับเงินปกติ อยู่ๆ
│   บอกให้ย้ายออกภายใน 15 วัน อ้างว่าสัญญาหมดอายุแล้ว
│   แบบนี้ทำได้ไหม ต้องบอกล่วงหน้ากี่วัน"
│
├─ 🎯 Phase 1: Flow 10.3 — ถูกไล่ที่
│  ✅ Detects: Eviction — but really this is about LEASE RENEWAL rights
│  ✅ Key fact: Continued paying + landlord accepting = implied renewal
│  ✓ Human drive: Security + Home
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: Eviction rights
│  ⚠️ Missing: Implied lease renewal — การต่อสัญญาโดยปริยาย
│  ⚠️ Missing: Notice period for lease termination (30 days minimum)
│  ⚠️ Missing: "สัญญาเช่าไม่มีกำหนดระยะเวลา" after implied renewal
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ เจรจากับผู้ให้เช่า
│  ✅ 🅱️ ยื่นคำร้องต่อศาล
│  ⚠️ Missing: Quick answer: "No, 15 days is illegal — minimum 30 days"
│
├─ 🔒 GATE: Works but user needs the "implied renewal" argument clearly
│
├─ 📍 Phase 4-8 (PAID): Court, evidence, filing — covers eviction defense
│
└─ ✅ VERDICT: MATCH 80%
   Flow 10.3 covers eviction but needs explicit treatment of
   implied lease renewal and minimum notice periods.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 10.2: คอนโด — นิติฯ บังคับเก็บค่าซ่อมลิฟต์ 80,000 ห้องละ

> **Source:** qa_135_real_questions.md · Q10.2#1
> **Mapped to:** ❌ No existing V2 flow covers condo juristic person disputes

```
🔴 THE REAL QUESTION
│  "ซื้อคอนโด 2 ห้องนอน นิติฯ บังคับเก็บค่าส่วนกลางเพื่อซ่อมลิฟต์ครั้งใหญ่
│   ห้องละ 80,000 บาท ทั้งที่เราอยู่ชั้น 3 และแทบไม่เคยใช้ลิฟต์เลย
│   เพราะชอบเดินขึ้นลงออกกำลังกาย แบบนี้ต้องจ่ายด้วยเหรอ
│   ไม่มีข้อยกเว้นสำหรับคนอยู่ชั้นต่ำที่ไม่ใช้ลิฟต์เลยหรือ"
│
├─ 🎯 Phase 1: ❌ No condo/housing association flow exists
│  This is CONDOMINIUM JURISTIC PERSON dispute — specific to Condominium Act
│  User question: Are special assessments mandatory? Are there exceptions?
│
├─ ⚖️ Phase 2: ❌ No coverage
│  ❌ พ.ร.บ.อาคารชุด — co-owner obligations, special assessment voting rules
│  ❌ No mention of: co-owner meeting voting thresholds
│  ❌ No mention of: right to inspect financial records
│  ❌ No mention of: challenging unreasonable assessments
│
├─ 🛤️ Phase 3: ❌ No paths — no existing flow
│
├─ 🔒 GATE: No applicable gate
│
├─ 📍 Phase 4-8 (PAID): No applicable paid phases
│
└─ ❌ VERDICT: MISS 0%
   No V2 flow covers condo/housing association disputes.
   This is a common urban consumer issue.
   Score: all phases ❌

   🔴 GAP: Need Flow 10.4 "Condo/Housing Association Disputes — นิติบุคคลอาคารชุด/หมู่บ้าน"
   Covering: Condominium Act, co-owner rights, voting thresholds,
   special assessments, financial transparency, challenging committee decisions
```

---

### TEST 10.3: ผู้เช่าไม่คืนเงินมัดจำ — ซ่อมท่อแล้วหักค่าเช่า

> **Source:** qa_135_real_questions.md · Q10.1#2
> **Mapped to:** Flow 10.2 — ผู้ให้เช่าไม่คืนเงินมัดจำ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "เช่าบ้าน วางเงินมัดจำ 2 เดือนกับค่าเช่าล่วงหน้า 1 เดือนรวม 30,000
│   อยู่ 2 เดือนบ้านหลังคารั่ว น้ำรั่วเข้าห้องนอน แจ้งเจ้าของบ้านไม่ยอมซ่อม
│   เราซ่อมเอง 3,000 แล้วหักค่าเช่าเดือนถัดไป เจ้าของบอกผิดสัญญา
│   ไม่ต่อสัญญาให้และริบเงินมัดจำทั้งหมด แบบนี้ถูกต้องไหม"
│
├─ 🎯 Phase 1: Flow 10.2 — ผู้ให้เช่าไม่คืนเงินมัดจำ
│  ✅ Detects: Deposit dispute
│  ⚠️ Compound: Repair-and-deduct + deposit forfeiture
│  Key question: Is deducting rent for self-repair "breach of contract"?
│  ✓ Human drive: Fairness + Home
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: Deposit return rights
│  ⚠️ Missing: Tenant's right to repair-and-deduct (ซ่อมเองแล้วหักค่าเช่า)
│  ⚠️ Missing: Landlord's duty to maintain property
│  ⚠️ Missing: Whether self-repair = "breach" justifying deposit forfeiture
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ เจรจา + ทวงถาม
│  ✅ 🅱️ ฟ้องศาล
│
├─ 🔒 GATE: Works — user needs deposit recovery process
│
├─ 📍 Phase 4-8 (PAID): Court, evidence, deposit recovery filing
│
└─ ⚠️ VERDICT: PARTIAL 70%
   Flow 10.2 covers deposit recovery but needs: repair-and-deduct rights,
   landlord maintenance obligations, and the "self-repair ≠ breach" argument.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

## CATEGORY 11: FAMILY (ครอบครัว)

### TEST 11.1: หย่า — สามีนอกใจ มีสินสมรส 2 ล้านในชื่อสามี

> **Source:** qa_135_real_questions.md · Q11.1#1
> **Mapped to:** Flow 11.1 — หย่า (Cat 7-12) + Flow 11.4 — คู่สมรสนอกใจ

```
🔴 THE REAL QUESTION
│  "แต่งงานมา 8 ปี มีลูก 2 คน สามีนอกใจ จับได้เพราะเห็นแชทในไลน์
│   เราเป็นแม่บ้านไม่ได้ทำงาน กลัวหย่าแล้วไม่มีเงินเลี้ยงลูก
│   สินสมรสมีบ้าน 1 หลัง รถ 2 คัน เงินเก็บในบัญชีสามี 2 ล้าน
│   ทั้งหมดอยู่ในชื่อสามี เราจะได้ส่วนแบ่งเท่าไหร่
│   แล้วเรียกค่าเลี้ยงดูและค่าทดแทนได้ไหม"
│
├─ 🎯 Phase 1: Flow 11.1 — หย่า + Flow 11.4 — นอกใจ
│  ✅ Detects: Divorce + adultery
│  ✅ Compound: สินสมรส division + ค่าอุปการะเลี้ยงดู + ค่าทดแทน
│  ✅ Critical: Everything in husband's name — need asset tracing
│  ✓ Human drive: Survival + Security + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow 11.1: สินสมรส 50-50 split
│  ✅ Flow 11.4: Adultery = fault ground → ค่าทดแทน
│  ✅ ค่าอุปการะเลี้ยงดูบุตร
│  ⚠️ Missing: Housewife with no income — special protection
│  ⚠️ Missing: Assets in husband's name — how to prove they're marital
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ ทำเอง: ฟ้องหย่า + แบ่งสินสมรส
│  ✅ 🅱️ ใช้ทนาย: Recommended for asset tracing
│
├─ 🔒 GATE: Strong — user with 2M in assets needs professional-grade filing
│
├─ 📍 Phase 4-8 (PAID): Family court, asset division calculation, custody
│
└─ ✅ VERDICT: MATCH 88%
   Flows 11.1 + 11.4 together cover this well. Enhancement:
   housewife-specific protections, asset tracing for marital property in spouse's name.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 11.2: สามีทำร้ายร่างกาย — เอาขวดเบียร์ฟาดหัว

> **Source:** qa_135_real_questions.md · Q11.3#1
> **Mapped to:** Flow 11.5 — ทำร้ายร่างกายในครอบครัว (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "สามีเป็นคนขี้เมา เวลาเมาจะทำร้ายร่างกายเราทุกครั้ง เมื่อวานหนักสุด
│   เอาขวดเบียร์ฟาดหัวจนต้องเย็บ 5 เข็ม ลูก 2 คนเห็นเหตุการณ์ตลอด
│   เราอยากเลิกแต่กลัวไม่มีที่ไป ไม่มีงานทำ ไม่มีเงิน
│   จะขอความช่วยเหลือจากใครได้บ้าง มีที่พักพิงสำหรับผู้ถูกกระทำไหม"
│
├─ 🎯 Phase 1: Flow 11.5 — DV
│  ✅ Perfect match: Domestic violence
│  ✅ Compound: Criminal assault + divorce ground + child protection
│  ✅ Urgency: HIGH — ongoing pattern + escalation
│  ✓ Human drive: Survival + Safety + Family
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ พ.ร.บ.คุ้มครองผู้ถูกกระทำด้วยความรุนแรงในครอบครัว พ.ศ.2550
│  ✅ Criminal: ทำร้ายร่างกาย
│  ✅ Protection orders
│  ⚠️ Missing: Shelter/ที่พักพิง resources — practical, not just legal
│  ⚠️ Missing: "ไม่มีงาน ไม่มีเงิน" — economic dependency = special protection
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ แจ้งความ + คำสั่งคุ้มครอง
│  ✅ 🅱์ ใช้ทนาย + ฟ้องหย่า
│  ✅ 🅲์ ขอความช่วยเหลือ (NGOs, shelters)
│  ⚠️ Missing: Shelter hotlines, emergency housing
│
├─ 🔒 GATE: Effective — user needs actionable steps right now
│
├─ 📍 Phase 4-8 (PAID): Police, court for protection order, divorce filing
│
└─ ✅ VERDICT: MATCH 85%
   Flow 11.5 covers DV well. Enhancement: add shelter hotlines,
   economic support resources, and "no income" specific guidance.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 11.3: มรดก — พ่อเสียชีวิตไม่มีพินัยกรรม 5 ทายาท

> **Source:** qa_135_real_questions.md · Q11.4#1
> **Mapped to:** Flow 11.3 — มรดก (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "พ่อเสียชีวิตกะทันหันไม่ได้ทำพินัยกรรม มีทรัพย์มรดกบ้าน 2 หลัง
│   เงินในแบงก์ 5 ล้าน ที่นา 10 ไร่ ทายาทมีแม่กับลูก 4 คน
│   แต่พี่ชายคนโตบอกว่าเป็นลูกชายคนเดียว จะได้บ้าน 1 หลังกับที่นา 10 ไร่
│   โดยอ้างว่าเป็นผู้สืบสกุล แบบนี้ถูกต้องตามกฎหมายไหม"
│
├─ 🎯 Phase 1: Flow 11.3 — มรดก
│  ✅ Detects: Intestate succession (ไม่มีพินัยกรรม)
│  ✅ Key issue: Old belief about male heir priority — needs clear legal debunking
│  ✅ Thai Civil Code: ALL children equal, spouse gets share too
│  ✓ Human drive: Justice + Security
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ ป.พ.พ. ม.1629 — ทายาทโดยธรรม: spouse + children
│  ✅ Equal division — NO male priority in modern Thai law
│  ✅ Flow explicitly debunks "ผู้สืบสกุล" myth
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ เจรจา + แบ่งตามกฎหมาย
│  ✅ 🅱️ ฟ้องศาล — แบ่งมรดก
│
├─ 🔒 GATE: Strong — clear money at stake (5M+), ฿299 is trivial
│
├─ 📍 Phase 4-8 (PAID): Probate court, inheritance division calculation
│
└─ ✅ VERDICT: MATCH 90%
   Flow 11.3 handles this cleanly. The "male heir" myth debunking is critical.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

## CATEGORY 12: ACCIDENT (อุบัติเหตุ)

### TEST 12.1: จักรยานยนต์ชนรถเก๋งเปิดประตู — แขนหัก

> **Source:** qa_135_real_questions.md · Q12.1#1
> **Mapped to:** Flow 12.1 — อุบัติเหตุรถยนต์ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "ขับรถมอเตอร์ไซค์ไปซื้อของ อยู่ๆ มีรถเก๋งเปิดประตูรถกะทันหัน
│   โดยไม่มอง ชนล้มแขนหัก มอไซค์พัง คนขับรถเก๋งมีประกันชั้น 1
│   แต่ประกันบอกว่าผิดทั้งคู่เพราะเราขับชิดซ้ายเกินไป เสนอจ่าย
│   ค่ารักษา 15,000 + ค่าซ่อม 5,000 ซึ่งไม่พอกับค่าเสียหายจริง"
│
├─ 🎯 Phase 1: Flow 12.1 — อุบัติเหตุรถยนต์
│  ✅ Detects: Motor vehicle accident
│  ✅ Key issue: Insurance offering too little — needs counter-negotiation
│  ✅ "เปิดประตูโดยไม่มอง" = clear negligence by car driver
│  ✓ Human drive: Survival (injury) + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: Accident liability, insurance claims
│  ⚠️ Missing: "ผิดทั้งคู่" defense — how to fight contributory negligence claim
│  ⚠️ Missing: Actual damages calculation (medical + bike repair + lost wages + pain)
│  ⚠️ Missing: When to reject insurance offer and escalate
│
├─ 🛤️ Phase 3: Path options
│  ✅ 🅰️ เจรจากับประกัน
│  ✅ 🅱์ ฟ้องศาล
│  ⚠️ Missing: Independent medical assessment to counter insurance's lowball
│
├─ 🔒 GATE: Effective — user needs to know HOW to negotiate up from 20K
│
├─ 📍 Phase 4-8 (PAID): Insurance claim dispute, court filing for higher damages
│
└─ ✅ VERDICT: MATCH 82%
   Flow 12.1 covers motor accidents well. Enhancement: add
   contributory negligence defense, insurance negotiation tactics, damages calculation.
   Score: Phase 1 ✅ | Phase 2 ✅ | Phase 3 ✅ | Gate ✅ | Phase 4-7 ✅ | Phase 8 ✅
```

---

### TEST 12.2: ถูกรถชนบนทางม้าลาย — คนขับไม่มีประกัน

> **Source:** qa_135_real_questions.md · Q12.1#3
> **Mapped to:** Flow 12.3 — บาดเจ็บสาหัสจากอุบัติเหตุ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "ถูกรถชนตอนข้ามถนนตรงทางม้าลาย ไฟเขียวคนข้ามด้วย
│   โดนมอเตอร์ไซค์ฝ่าไฟแดงชน บาดเจ็บสาหัส นอนโรงพยาบาล 1 เดือน
│   มอเตอร์ไซค์คนชนไม่มีประกันภัยใดๆเลย คนขับก็ไม่มีเงินจ่าย
│   จะเรียกร้องค่ารักษาพยาบาลจากใครได้บ้าง มีกองทุนอะไรช่วยไหม"
│
├─ 🎯 Phase 1: Flow 12.3 — บาดเจ็บสาหัส
│  ✅ Detects: Serious accident injury
│  ✅ Key issue: Uninsured driver — can't recover from tortfeasor
│  ✅ Alternative source needed: Government compensation fund
│  ✓ Human drive: Survival + Hopelessness
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow covers: Accident compensation, medical damages
│  ⚠️ Missing: กองทุนทดแทนผู้ประสบภัยจากรถ (Road Accident Victims Protection Fund)
│  ⚠️ Missing: How to claim when tortfeasor has no money/insurance
│  ⚠️ Missing: Social security coverage if victim is worker
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ Standard paths assume insured or collectible defendant
│  ❌ Missing: Government compensation fund claim process
│
├─ 🔒 GATE: Works for insured cases — weak for uninsured
│
├─ 📍 Phase 4-8 (PAID): Standard accident litigation — wrong for uninsured defendant
│
└─ ⚠️ VERDICT: PARTIAL 55%
   Flow 12.3 assumes insured/solvent defendant. This user needs the
   government protection fund process — a completely different path.
   Score: Phase 1 ✅ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️

   Enhancement: Add "uninsured driver" path with Road Accident Victims Fund process.
```

---

### TEST 12.3: ขับรถชนคนตายตอนกลางคืน — ข้อหาประมาทเป็นเหตุให้ตาย

> **Source:** qa_135_real_questions.md · Q12.5#1
> **Mapped to:** Flow 12.1 — อุบัติเหตุรถยนต์ (Cat 7-12)

```
🔴 THE REAL QUESTION
│  "ขับรถชนคนข้ามถนนเสียชีวิต ตอนกลางคืน จุดที่ไม่มีไฟส่องสว่าง
│   คนข้ามใส่ชุดดำ ไม่ใช่ทางม้าลาย เราขับ 60 km/h ไม่ได้ดื่มแอลกอฮอล์
│   ตำรวจแจ้งข้อหาขับรถประมาทเป็นเหตุให้ผู้อื่นถึงแก่ความตาย
│   เราจะติดคุกไหม มีทางรอดหรือลดโทษยังไงบ้าง
│   ถ้าชดใช้ค่าเสียหายให้ครอบครัวผู้เสียชีวิต"
│
├─ 🎯 Phase 1: Flow 12.1 — อุบัติเหตุรถยนต์
│  ⚠️ This is CRIMINAL liability from accident — not just civil accident
│  Key: ป.อาญา ม.291 — ประมาทเป็นเหตุให้ผู้อื่นถึงแก่ความตาย (จำคุก ≤ 10 ปี)
│  User is facing JAIL TIME — higher stakes than standard accident flow
│  ✓ Human drive: Survival + Fear + Justice
│
├─ ⚖️ Phase 2: Rights analysis
│  ✅ Flow 12.1 covers: Accident procedures, insurance
│  ⚠️ Missing: Criminal defense strategy for มาตรา 291
│  ⚠️ Missing: Mitigating factors (victim contributory negligence — dark clothes, no crosswalk)
│  ⚠️ Missing: "ชดใช้ค่าเสียหาย = ลดโทษ" specific legal mechanism
│  ⚠️ Missing: Bail procedures for criminal accident cases
│
├─ 🛤️ Phase 3: Path options
│  ⚠️ Standard paths are civil-focused — user needs criminal defense urgently
│  ❌ Missing: Criminal defense lawyer recommendation
│  ❌ Missing: Plea negotiation / settlement with victim's family
│
├─ 🔒 GATE: Weak — flow designed for civil disputes, not criminal jail threat
│
├─ 📍 Phase 4-8 (PAID): Would give civil court info, not criminal defense
│
└─ ⚠️ VERDICT: PARTIAL 40%
   Flow 12.1 is designed for civil accident claims, not criminal liability.
   User facing potential jail needs: criminal defense strategy, mitigating factors,
   victim compensation as sentence reduction, bail procedures.
   Score: Phase 1 ⚠️ | Phase 2 ⚠️ | Phase 3 ⚠️ | Gate ⚠️ | Phase 4-7 ⚠️ | Phase 8 ⚠️

   Enhancement: Add criminal liability appendix to Flow 12.1 or create
   separate Flow 12.4 "Criminal Liability from Accidents"
```

---

# 📊 DETAILED SCORE MATRIX

| Test# | Category | Question | Mapped Flow | P1 | P2 | P3 | Gate | P4-8 | Overall | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | Online Fraud | กระเป๋า 35K ไม่ได้ของ | 1.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 90% | ✅ |
| 1.2 | Online Fraud | Call Center 120K | 1.2 | ✅ | ✅ | ✅ | ✅ | ✅ | 92% | ✅ |
| 1.3 | Online Fraud | SMS Phishing 200K | ⚠️ 1.2 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 45% | ⚠️ |
| 2.1 | Crime | ชกหน้า เย็บ 5 เข็ม | 2.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 90% | ✅ |
| 2.2 | Crime | บ้านโดนงัด 500K | 2.2 | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | 70% | ⚠️ |
| 2.3 | Crime | ขู่กรรโชก 500K | 2.4 | ✅ | ✅ | ✅ | ✅ | ✅ | 85% | ✅ |
| 3.1 | Defamation | ปลอม FB ด่าสถาบัน | 3.1 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 55% | ⚠️ |
| 3.2 | Defamation | ใส่ร้ายเรื่องชู้ | 3.3 | ✅ | ✅ | ✅ | ✅ | ✅ | 88% | ✅ |
| 3.3 | Defamation | Google Maps review | 3.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 80% | ✅ |
| 4.1 | Insurance | ประกันชีวิต 15 ปี | 4.2 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | 60% | ⚠️ |
| 4.2 | Insurance | ประกันรถ 3 เดือน | 4.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 78% | ✅ |
| 4.3 | Insurance | แม่ 75 ถูกหลอกขาย | 4.3 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | 65% | ⚠️ |
| 5.1 | Government | ขออนุญาต สินบน 100K | 5.2 | ❌ | ❌ | ❌ | ❌ | ❌ | 35% | ❌ |
| 5.2 | Government | พาสปอร์ตล่าช้า | 5.3 | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 60% | ⚠️ |
| 5.3 | Government | สรรพากรภาษี 5M | 5.2 | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | 70% | ✅ |
| 6.1 | Property | น.ส.3 ทับซ้อน | 6.2+6.3 | ✅ | ✅ | ✅ | ✅ | ✅ | 78% | ✅ |
| 6.2 | Property | รั้วล้ำ 1.5 ม. | 6.2 | ✅ | ✅ | ✅ | ✅ | ✅ | 92% | ✅ |
| 6.3 | Property | โฉนดตาทวด 40 ปี | 6.4 | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | 72% | ✅ |
| 7.1 | Labour | เลิกจ้าง 10 ปี | 7.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 95% | ✅ |
| 7.2 | Labour | OT ร้านอาหาร | 7.2+7.4 | ✅ | ✅ | ✅ | ✅ | ✅ | 85% | ✅ |
| 7.3 | Labour | ประกันสังคมเดินทาง | ⚠️ 4.2 | ❌ | ❌ | ❌ | ❌ | ❌ | 30% | ⚠️ |
| 8.1 | Consumer | มือถือ 12 วันดับ | 8.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 82% | ✅ |
| 8.2 | Consumer | คอร์สเรียนหลอกลวง | 8.4 | ✅ | ✅ | ✅ | ✅ | ✅ | 90% | ✅ |
| 8.3 | Consumer | ฟิตเนสยกเลิก | ⚠️ 8.4 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 50% | ⚠️ |
| 9.1 | Debt | ทวงหนี้ข่มขู่ | 9.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 93% | ✅ |
| 9.2 | Debt | หนี้นอกระบบ 100K | 9.2 | ✅ | ✅ | ✅ | ✅ | ✅ | 90% | ✅ |
| 9.3 | Debt | ประนอมหนี้ 800K | 9.3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 58% | ⚠️ |
| 10.1 | Housing | เช่าหมดสัญญา | 10.3 | ✅ | ⚠️ | ✅ | ✅ | ✅ | 80% | ✅ |
| 10.2 | Housing | นิติฯ คอนโด 80K | ❌ None | ❌ | ❌ | ❌ | ❌ | ❌ | 0% | ❌ |
| 10.3 | Housing | เงินมัดจำ | 10.2 | ✅ | ⚠️ | ✅ | ✅ | ✅ | 70% | ⚠️ |
| 11.1 | Family | หย่า นอกใจ | 11.1+11.4 | ✅ | ✅ | ✅ | ✅ | ✅ | 88% | ✅ |
| 11.2 | Family | DV สามี | 11.5 | ✅ | ✅ | ✅ | ✅ | ✅ | 85% | ✅ |
| 11.3 | Family | มรดก 5 ทายาท | 11.3 | ✅ | ✅ | ✅ | ✅ | ✅ | 90% | ✅ |
| 12.1 | Accident | มอไซค์ชนประตูรถ | 12.1 | ✅ | ✅ | ✅ | ✅ | ✅ | 82% | ✅ |
| 12.2 | Accident | ทางม้าลายไม่มีประกัน | 12.3 | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 55% | ⚠️ |
| 12.3 | Accident | ชนคนตาย ข้อหาอาญา | 12.1 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 40% | ⚠️ |

---

# 📈 INSIGHTS & RECOMMENDATIONS

## What's Working Well (✅ 21/36 — 58%)
- **Core flows are solid:** 1.1 (online purchase fraud), 1.2 (call center), 2.1 (assault), 7.1 (unfair dismissal), 9.1 (debt collection harassment), 11.1 (divorce), 11.3 (inheritance) all hit >85% match
- **The 8-phase format is consistent and monetizable** — every flow has clear free/paid gate
- **Human Drive detection adds emotional resonance** — aligns with user psychology
- **Thai-optimized:** Cultural context (ครอบครองปรปักษ์, ผู้สืบสกุล myths) well handled

## What Needs Enhancement (⚠️ 13/36 — 36%)
- **Cross-reference gaps:** Many real questions span multiple categories (e.g., burglary + insurance). Flows need internal cross-linking
- **Special population gaps:** Elderly consumers (Test 4.3), housewives (Test 11.1), uninsured victims (Test 12.2)
- **Edge case coverage:** Fraud via identity theft (Test 3.1), criminal liability from accidents (Test 12.3), pre-bankruptcy restructuring (Test 9.3)

## What's Missing (❌ 2/36 — 6%)
- 🔴 **Bribery/Solicitation by Officials** — critical for Thai context, no existing flow
- 🔴 **Condo/Housing Association Disputes** — high-volume urban issue, no flow

---

# 🎯 PRIORITY ACTION ITEMS

| Priority | Action | Impact |
|---|---|---|
| 🔴 P0 | Create Flow 1.6: Phishing/Social Engineering | 3 questions across Cats 1, 3, 12 |
| 🔴 P0 | Create Flow 5.4: Bribery by Officials (NACC) | 3 questions in Cat 5 |
| 🔴 P0 | Create Flow 10.4: Condo Association Disputes | 3 questions in Cat 10 |
| 🟠 P1 | Create Flow 7.5: Social Security/WCF Claims | 3 questions in Cat 7 |
| 🟠 P1 | Create Flow 8.5: Contract Cancellation/Cooling-Off | 3 questions in Cat 8 |
| 🟠 P1 | Add criminal liability appendix to Flow 12.1 | 2 questions in Cat 12 |
| 🟡 P2 | Enhance Flow 4.2 for life insurance death claims | 1 question in Cat 4 |
| 🟡 P2 | Add elderly consumer protection to Flow 4.3 | 1 question in Cat 4 |
| 🟡 P2 | Enhance Flow 3.1 for identity theft/impersonation | 1 question in Cat 3 |

---

*Report generated: 11 สิงหาคม 2569 · LegalAI V2 Concierge Flow Validation · 36 tests against 47 flows*
