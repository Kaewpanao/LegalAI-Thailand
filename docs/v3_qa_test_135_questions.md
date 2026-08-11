# 🧭 LegalAI V3 Concierge — QA Test Report: 135 Real Questions vs. 47 V3 Flows

> **Generated:** 11 สิงหาคม 2569 | **Method:** Manual flow-response mapping + gap analysis  
> **Sources:** `qa_135_real_questions.md` (135 questions, 12 categories, 45 sub-problems)  
> **V3 Flows:** `concierge_v3_cat1_6.md` (24 flows) + `concierge_v3_cat7_12.md` (23 flows) = **47 flows total**

---

## 🔬 Test Methodology

For each of the 12 categories, we pick **2–3 representative real user questions** and test them against the V3 concierge flows:

1. 🔴 **Show the real question** (from the 135 QA bank)
2. 🟢 **Show which V3 flow it maps to** (with flow number)
3. 🟢 **Show what Phase 1–3 (FREE) delivers** — actual flow content
4. 🔒 **Show the monetization gate** — what's gated
5. 🔵 **Show what Phase 4–8 (฿299) delivers** — actual flow content
6. ✅/⚠️/❌ **Verdict** — does the flow adequately handle this question?

---

## หมวด 1: ออนไลน์และหลอกลวง (ONLINE FRAUD) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name | Maps To |
|------|------|---------|
| 1.1 | ซื้อของออนไลน์ไม่ได้ของ — ฉ้อโกง | 1.1 |
| 1.2 | Call Center — แก๊งคอลเซ็นเตอร์ | 1.2 |
| 1.5 | แชร์ลูกโซ่ — หลอกลงทุน | 1.2 Q3 |

---

### 🧪 Test 1A: Q1.1 #1 — กระเป๋าแบรนด์เนม 35,000 บ. ไม่ได้ของ

#### 🔴 Real Question
> "คือเราสั่งกระเป๋าแบรนด์เนมจากเพจเฟสบุ๊คชื่อ 'Luxury Bag Thailand' ราคา 35,000 บาท โอนเงินไปเรียบร้อยแล้ว แต่ผ่านมา 2 อาทิตย์ยังไม่ได้ของเลยค่ะ ทักแชทไปก็อ่านไม่ตอบ ล่าสุดบล็อคเราไปแล้วด้วย แบบนี้แจ้งความได้มั้ยคะ แล้วต้องทำยังไงบ้าง เราเก็บสลิปโอนกับแชทไว้หมดแล้ว"

#### 🟢 Flow: **1.1 — ซื้อของออนไลน์ไม่ได้ของ (ฉ้อโกง)**

#### 🟢 Phase 1 (FREE) — UNDERSTAND:
```
🎯 Compound Case Detected!
→ 💰 ฉ้อโกง (ป.อาญา ม.341) — สั่งของแล้วไม่ส่ง
→ 🌐 พ.ร.บ.คอมพิวเตอร์ ม.14(1) — หลอกลวงทางออนไลน์
📋 Key questions: แพลตฟอร์ม? (Facebook) · จำนวนเงิน? (35,000) · ผู้ขาย? (Luxury Bag Thailand)
🎯 Human Drive: Survival + Justice — "เสียเงิน" "โดนโกง"
```

#### 🟢 Phase 2 (FREE) — RIGHTS:
```
📜 Laws: ป.อาญา ม.341 (จำคุก ≤3 ปี, ปรับ ≤60,000) · พ.ร.บ.คอมพ์ ม.14(1) (จำคุก ≤5 ปี, ปรับ ≤100,000) · ป.พ.พ. สัญญาซื้อขาย
🛡️ Actions: แจ้งความออนไลน์ (thaipoliceonline.go.th) · แจ้งแพลตฟอร์ม · แจ้ง ปปง. · ฟ้องคดีผู้บริโภค · แจ้งแบงก์ชาติ (บัญชีม้า)
⚠️ ห้าม: ลบแชท · รอนาน (อายุความฉ้อโกง 3 เดือน!) · ไปทวงเองรุนแรง
⏰ ความเร่งด่วน: สูง — ต้องแจ้งความภายใน 3 เดือน!
```

#### 🟢 Phase 3 (FREE) — CHOOSE PATH:
```
🅰️ ทำเอง — ฟรี: แจ้งความออนไลน์ · แจ้งแพลตฟอร์ม · ตรวจสอบ Blacklistseller · ฟ้องผู้บริโภค (ไม่ต้องมีทนาย)
🅱️ ใช้ทนาย — ฿10,000-20,000: จัดการทั้งหมด · ฟ้องอาญา+แพ่ง
🅲️ ทวงถามก่อน — ฟรี: ส่งจดหมาย · รอ 7 วัน · ถ้าไม่ตอบ → 🅰️/🅱️
📚 + Lawyer Checklist 10 ข้อ · + Mediation Benefits · + Court Taxonomy
```

#### 🔒 MONETIZATION GATE:
```
🆓 คุณรู้แล้ว: ข้อหา · โทษ · แนวทาง
🤔 แต่: ต้องไปศาลไหน? เอกสารอะไร? เขียนคำฟ้องยังไง?
💡 LegalAI ฿299: บอกทุกขั้นตอนจนฟ้องเองได้
⚖️ จ้างทนาย ฿10,000-20,000 · LegalAI ฿299 · ประหยัด 98%
📦 Action Pack: 📍ศาล · 📄เอกสาร · 🔧คำฟ้อง · 🏛️ขั้นตอน
```

#### 🔵 Phase 4 (฿299) — JURISDICTION:
```
📍 Court: แจ้งความที่ไหนก็ได้ (คดีออนไลน์)
🏛️ สภ. + ศาลจังหวัด local · หรือแจ้งออนไลน์ (แนะนำ!)
🔵 Blue-Shirt Receptionists · Court Taxonomy
```

#### 🔵 Phase 5-7 (฿299) — DOCUMENTS · PREPARE · FILE:
```
📄 เอกสาร 7 รายการ: บัตรประชาชน · สลิปโอน · แคปแชท · โปรไฟล์ผู้ขาย · โพสต์ขาย · เลขบัญชี · Statement
🔧 AI สร้าง: บันทึกแจ้งความ 2 ข้อหา · คำร้องเปิดเผยบัญชี · จดหมายทวงถาม · ฟ้องผู้บริโภค · คำร้องอายัดบัญชี
🏛️ ขั้นตอน: แจ้งออนไลน์ (20-30 นาที) → ระบุข้อหา → รับหมายเลขคดี → ตำรวจติดต่อ 7-14 วัน
💡 Tip: แจ้ง ปอท. เพิ่ม (1441)
```

#### 🔵 Phase 8 (฿999 Case Plus):
```
📊 Timeline: วันนี้แจ้งความ → +1 วันแพลตฟอร์มระงับบัญชี → +7-14 ตร.ติดต่อ → +30 ธนาคารให้ข้อมูล → +3-6 เดือนอัยการฟ้อง → +6-12 เดือนศาลพิพากษา
⭐ Case Plus: AI ติดตามอัตโนมัติ · แจ้งเตือนทุกกำหนด · ปรึกษาทนาย 3 ครั้ง
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> The flow perfectly addresses this question — identifies both criminal charges, provides free DIY path, explains urgency (3-month deadline), covers all evidence types, and gives step-by-step filing instructions. The question is a textbook match for flow 1.1.

---

### 🧪 Test 1B: Q1.2 #3 — Golden Trade แชร์ลูกโซ่ 1 ล้าน+

#### 🔴 Real Question
> "ลงทุนในแพลตฟอร์มเทรดหุ้นออนไลน์ที่เพื่อนแนะนำมา ชื่อ 'Golden Trade' ตอนแรกถอนเงินได้จริงนะคะ เลยลงเพิ่มไปอีกเป็นล้าน สุดท้ายถอนไม่ได้แล้ว ผู้ดูแลระบบหายไปเลย เพิ่งรู้ว่ามันคือแชร์ลูกโซ่ ตอนนี้เป็นหนี้หลายแสน ร้องไห้ทุกวันเลย จะฟ้องร้องได้ยังไงบ้างคะ มีหลายคนโดนเหมือนกันเป็นร้อยคน"

#### 🟢 Flow: **1.5 — แชร์ลูกโซ่ (หลอกลงทุน)**

#### 🟢 Phase 1 (FREE) — UNDERSTAND:
```
🔴 Compound Case Detected!
→ 📊 ฉ้อโกงประชาชน (ป.อาญา ม.343) · 💰 พ.ร.ก.กู้ยืมเงินฉ้อโกงประชาชน พ.ศ.2527 · 🌐 พ.ร.บ.คอมพ์ ม.14
📋 Flags: ผลตอบแทนสูงผิดปกติ (10-30%/เดือน) · จ่ายช่วงแรกให้ตายใจ → ระดมเพิ่ม → ปิดหนี
🎯 Human Drive: Security + Growth — "อยากรวย" "เพื่อนแนะนำ" "ลงทุนเพิ่ม"
```

#### 🟢 Phase 2 (FREE) — RIGHTS:
```
📜 Laws: ป.อาญา ม.343 (จำคุก ≤5 ปี) · พ.ร.ก.กู้ยืมเงิน (จำคุก 5-10 ปี ปรับ 500,000-1,000,000) · พ.ร.บ.คอมพ์
🛡️ Actions: แจ้งความ · แจ้ง ปปง. (อายัดทรัพย์) · แจ้ง กลต. · ฟ้องแพ่งเรียกเงินคืน · รวมกลุ่มผู้เสียหาย (Class Action)
⚠️ ห้าม: ลงทุนเพิ่ม · ลบหลักฐาน · ไปทวงเอง
⏰ อายุความ: 10 ปี (อาญา) / 5 ปี (พ.ร.ก.)
```

#### 🟢 Phase 3 (FREE) — CHOOSE PATH:
```
🅰️ ทำเอง — ฟรี: แจ้งความ · แจ้ง ปปง. · รวมกลุ่มผู้เสียหาย
🅱️ ใช้ทนาย — ฿20,000-50,000: ฟ้อง Class Action · ติดตามอายัดทรัพย์ทั่วประเทศ
🅲️ รวมกลุ่มก่อน — ฟรี: หาผู้เสียหายคนอื่น · แจ้งพร้อมกัน (ตร.ให้ความสำคัญกว่า)
```

#### 🔒 MONETIZATION GATE:
```
🆓 You know: 3 charges · penalties · path chosen
🤔 But: which court? what docs? how to draft complaint?
💡 ฿299: Step-by-step from court selection to filing
📦 Action Pack: 📍Court · 📄Checklist · 🔧Complaint drafts · 🏛️Procedures
```

#### 🔵 Phase 4-7 (฿299):
```
📍 Court: ศาลอาญาคดีทุจริต / ศาลจังหวัด (ตามที่อยู่จำเลยหรือเกิดเหตุ)
📄 Checklist: หลักฐานโอน · Statement · แคปแพลตฟอร์ม · รายชื่อผู้เสียหาย · หลักฐานโปรไฟล์คนชวน
🔧 AI Drafts: คำฟ้อง ม.343 · คำร้อง ปปง. · Class Action filing · คำร้องอายัดทรัพย์
🏛️ Filing: แจ้ง บก.ปอท. → ยื่น ปปง. → ฟ้องศาลอาญา → ฟ้องแพ่งเรียกเงินคืน
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 1.5 was built exactly for this: Ponzi/pyramid schemes with multiple victims. Covers criminal complaint + AMLO asset freeze + class action. The user's mention of "ร้อยคน" (100+ victims) is specifically addressed by Path 🅲️.

---

### 🧪 Test 1C: Q1.3 #1 — SMS phishing 200,000 บ.

#### 🔴 Real Question
> "กำลังจะซื้อของออนไลน์แล้วมี SMS เข้ามาให้คลิกลิงก์ยืนยันตัวตน เรากดเข้าไปกรอกข้อมูลบัตรเครดิตไป ตอนนี้เงินในบัญชีหายไป 200,000 บาทเลยครับ เพิ่งมารู้ทีหลังว่ามันคือลิงก์ปลอม ธนาคารบอกว่าเรายินยอมเองเลยไม่รับผิดชอบ แบบนี้ต้องทำยังไงต่อ มีสิทธิฟ้องธนาคารได้มั้ย"

#### 🟢 Flow: **1.2 — Call Center (mapped as fraud-by-deception)** + partially mapped to 1.3 (แอปกู้เงินเถื่อน — not exact)

> ⚠️ This question has a UNIQUE element: **bank liability dispute** (ธนาคารปฏิเสธความรับผิดชอบ). No V3 flow specifically addresses suing the BANK for negligence in phishing cases.

#### 🟢 Phase 1 (FREE — via Flow 1.2):
```
Detects: ฉ้อโกง ม.342 (แสดงตนเป็นคนอื่น) + พ.ร.บ.คอมพ์ ม.14 + อั้งยี่ ม.209
⚠️ Flow 1.2 focuses mainly on phone-based Call Center scams, NOT SMS phishing links
```

#### 🟢 Phase 2 (FREE — via Flow 1.2):
```
Actions: โทร 1441 · แจ้งความ · อายัดบัญชีปลายทางทันที · แจ้งเบอร์
⚠️ Missing: "ฟ้องธนาคาร" is NOT addressed — this is a bank-customer dispute under consumer protection law
```

#### ⚠️ VERDICT: **⚠️ PARTIAL MATCH**
> Flow 1.2 covers the CRIMINAL side (report fraud, freeze accounts) but the user's core question — *can I sue the bank for not protecting me?* — has no dedicated V3 flow. This touches consumer protection law (bank's duty of care) and possibly PDPA violation, which would need a cross-flow: 1.2 (fraud report) + 4.2/4.3 (insurance-like claim dispute logic) + 8.4 (unfair contract terms). A dedicated "ธนาคารปฏิเสธความรับผิด" flow is missing.

---

### 📊 Cat 1 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 1A: กระเป๋า 35,000 | 1.1 ฉ้อโกงออนไลน์ | ✅ Full | ✅ Full | ✅ |
| 1B: Golden Trade | 1.5 แชร์ลูกโซ่ | ✅ Full | ✅ Full | ✅ |
| 1C: SMS phishing + ฟ้องธนาคาร | 1.2 (partial) | ⚠️ Criminal only | ⚠️ No bank-dispute | ⚠️ |

---

## หมวด 2: อาชญากรรม (CRIME) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 2.1 | ทำร้ายร่างกาย |
| 2.2 | ลักทรัพย์ |
| 2.3 | ข่มขืน/อนาจาร |
| 2.4 | ขู่กรรโชก |

---

### 🧪 Test 2A: Q2.1 #1 — เพื่อนบ้านชกหน้า เย็บ 5 เข็ม

#### 🔴 Real Question
> "ทะเลาะกับเพื่อนบ้านเรื่องที่จอดรถ แล้วเขาชกหน้าเราเลือดอาบเลยค่ะ ไปหาหมอเย็บ 5 เข็ม มีใบรับรองแพทย์กับคลิปกล้องวงจรปิดชัดเจน ตอนนี้เพื่อนบ้านไม่ยอมรับผิดชอบอะไรเลย บอกว่าเราต่างคนต่างผิด แบบนี้แจ้งความข้อหาทำร้ายร่างกายได้มั้ย จะเรียกค่ารักษากับค่าเสียหายได้เท่าไหร่"

#### 🟢 Flow: **2.1 — ทำร้ายร่างกาย**

#### 🟢 Phase 1-3 (FREE):
```
🔴 Physical Violence: ป.อาญา ม.295 (ทำร้าย) + ม.297 (สาหัส — ถ้ากระดูกหัก)
🛡️ Actions: ไปรพ. → ใบรับรองแพทย์ · แจ้งความภายใน 24-72 ชม. · ถ่ายรูปแผล · เรียกค่าเสียหายแพ่ง
⚠️ ห้าม: แก้แค้นกลับ (กลายเป็นจำเลยทั้งคู่) · รอจนแผลหาย
⏰ อายุความ: 10 ปี — แต่หลักฐานหายภายในวัน!
🅰️ ทำเอง ฟรี: รพ.+แจ้งความ · 🅱️ ทนาย ฿15,000-40,000 · 🅲️ ไกล่เกลี่ย ฟรี
⚖️ Rights: ทนายขอแรง (ถ้าไม่มีเงิน) · Bail application guidance
```

The user HAS the evidence the flow asks for: ✅ ใบรับรองแพทย์ + ✅ คลิปกล้องวงจรปิด — perfect match!

#### 🔒 GATE:
```
🆓 You know: ม.295/297 · penalties · action plan · court types
🔒 ฿299: exact court · document checklist · AI drafts (คำฟ้อง+คำร้องขอค่าสินไหม) · filing steps
```

#### 🔵 Phase 4-7 (฿299):
```
📍 Court: ศาลจังหวัด (คดีอาญา) + ฟ้องแพ่งเรียกค่าสินไหมควบได้
📄 Docs: บัตรประชาชน · ใบรับรองแพทย์ · รูปถ่ายบาดแผล · คลิป CCTV · รายการค่ารักษา
🔧 AI: คำฟ้องอาญา ม.295 · คำร้องเรียกค่าสินไหม · Timeline
🏛️ Steps: แจ้งความ → ตร.สอบสวน → อัยการสั่งฟ้อง → ศาลพิพากษา
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Perfect fit. User already has medical certificate + CCTV — exactly what Phase 5 asks for. Flow gives clear criminal + civil path with compensation calculations.

---

### 🧪 Test 2B: Q2.2 #3 — จับขโมยได้แต่โดนข้อหาใช้กำลังเกินกว่าเหตุ

#### 🔴 Real Question
> "ขโมยขึ้นบ้านตอนดึกครับ ดีที่เราตื่นมาเจอเลยจับตัวไว้ได้ แต่เขามีอาวุธมีดด้วย เลยเกิดการต่อสู้กันจนเขาบาดเจ็บ ตำรวจมาจับทั้งคู่เลย!!! บอกว่าเราใช้กำลังเกินกว่าเหตุด้วย งงมากครับ เราป้องกันตัวเองแท้ๆ แบบนี้เราจะโดนข้อหาอะไรมั้ย"

#### 🟢 Flow: **2.2 — ลักทรัพย์ + 2.1 (บางส่วน)** — ⚠️ No dedicated "ป้องกันโดยชอบด้วยกฎหมาย / ใช้กำลังเกินกว่าเหตุ" flow

#### 🟢 Phase 1-3 (FREE — via 2.2):
```
Flow 2.2 focuses on: reporting theft, documenting stolen items, police report.
🚫 DOES NOT cover: self-defense law (ป.อาญา ม.68 — ป้องกันโดยชอบด้วยกฎหมาย)
🚫 DOES NOT cover: when self-defense becomes "เกินกว่าเหตุ" (ม.69)
```

#### ⚠️ VERDICT: **⚠️ PARTIAL — MAJOR GAP**
> V3 has no flow for **self-defense / excessive force** (ป้องกันเกินสมควรกว่าเหตุ). This is a common legal question in Thailand. The user needs to understand ม.68 (justified defense) vs ม.69 (excessive defense — court may reduce penalty) vs what charges they might face. This is a significant gap.

---

### 🧪 Test 2C: Q2.3 #1 — กรรโชกทรัพย์จากเบอร์แปลก (ขู่เปิดเผยความลับ)

#### 🔴 Real Question
> "มีเบอร์แปลกโทรมาบอกว่ารู้ว่าเราแอบมีความสัมพันธ์ลับกับเจ้านายที่แต่งงานแล้ว ขู่จะเอาเรื่องไปบอกเมียเจ้านายกับเพื่อนร่วมงานถ้าไม่โอนเงินให้ 500,000 บาท เรากลัวมากเลยค่ะทั้งที่ไม่ได้ทำอะไรผิด"

#### 🟢 Flow: **2.4 — ขู่กรรโชก**

#### 🟢 Phase 1-3 (FREE):
```
🔴 Extortion/Blackmail: ป.อาญา ม.337 (กรรโชกทรัพย์) · ม.338 (รีดเอาทรัพย์)
🛡️ Actions: แจ้งความ · เก็บหลักฐาน (เบอร์โทร, แชท, บันทึกเสียง) · ห้ามจ่าย!
⏰ Age of crime: 10 years
```

#### ✅ VERDICT: **✅ MATCH**
> Flow 2.4 directly addresses blackmail/extortion. The unique element here (threat to reveal secrets) is a textbook ม.337 case. Covers criminal + evidence preservation well.

---

### 📊 Cat 2 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 2A: ชกหน้าเย็บ 5 เข็ม | 2.1 ทำร้ายร่างกาย | ✅ Full | ✅ Full | ✅ |
| 2B: จับขโมย+ป้องกันเกินกว่าเหตุ | 2.2 (partial) + None | ❌ No self-defense law | ❌ No flow | ❌ |
| 2C: ขู่กรรโชก 500,000 | 2.4 ขู่กรรโชก | ✅ Full | ✅ Full | ✅ |

---

## หมวด 3: หมิ่นประมาท (DEFAMATION) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 3.1 | ถูกด่าบนโซเชียล |
| 3.2 | ภาพหลุด/Revenge Porn |
| 3.3 | ถูกใส่ความ |
| 3.4 | PDPA ข้อมูลรั่วไหล |

---

### 🧪 Test 3A: Q3.1 #1 — เอารูปไปโพสต์ในกลุ่ม "สาวขายตัว"

#### 🔴 Real Question
> "มีคนเอารูปเราไปโพสต์ในกลุ่มเฟสบุ๊คชื่อ 'สาวขายตัวย่านรัชดา' พร้อมเบอร์โทรศัพท์เรา เราไม่เคยทำอะไรแบบนั้นเลยค่ะ มีแต่ผู้ชายโทรมาชวนไปนอนด้วยทั้งวันทั้งคืนจนต้องปิดเครื่อง เรารู้ว่าเป็นฝีมืออดีตเพื่อนร่วมงานที่อิจฉาเรา"

#### 🟢 Flow: **3.1 — ถูกด่าบนโซเชียล** + **3.3 — ถูกใส่ความ** (cross-flow)

#### 🟢 Phase 1-3 (FREE — 3.1):
```
📜 Laws: ป.อาญา ม.326 (หมิ่นประมาททางอาญา) · ม.328 (โฆษณาทางสื่อ) · พ.ร.บ.คอมพ์ ม.14(1)
🛡️ Actions: แคปหลักฐาน · แจ้งความ · แจ้งแพลตฟอร์ม (ลบโพสต์) · ฟ้องหมิ่น + ละเมิด
⏰ อายุความหมิ่นประมาท: 3 เดือน (ต้องรีบ!)
```

#### 🟢 Phase 1-3 (FREE — 3.3 additional):
```
📜 ถูกใส่ความ: ป.อาญา ม.173-175 (แจ้งความเท็จ) · ม.326-328 (หมิ่นประมาท)
🛡️ Defamation + False Accusation + Identity Theft aspects
```

> Note: This case has a gender-based harassment element (posted in sex-work group with phone number) that might benefit from the Revenge Porn flow (3.2) spiritual overlap.

#### ✅ VERDICT: **✅ MATCH (cross-flow)**
> Flow 3.1 gives defamation online basics; 3.3 adds false accusation angle. The user has identified the perpetrator (อดีตเพื่อนร่วมงาน) — this makes the case strong. Well-covered.

---

### 🧪 Test 3B: Q3.2 #2 — ภาพหลุด / Revenge Porn (แฟนเอารูปโป๊ไปโพสต์)

#### 🔴 Real Question
> "แฟนเราเอารูปโป๊ที่เราส่งให้ตอนคบกันไปโพสต์ในกลุ่มลับ Telegram หลังจากเลิกกันค่ะ เราอายมาก ไม่กล้าออกไปเจอใครเลย มีคนรู้จักทักมาว่าเห็นรูปเราในเน็ต แบบนี้แจ้งความได้ในข้อหาอะไรบ้าง ทั้งแฮกและหมิ่นประมาท?"

#### 🟢 Flow: **3.2 — ภาพหลุด / Revenge Porn** 🟡 GOLD STANDARD

#### 🟢 Phase 1-3 (FREE — 3.2):
```
🔴 Revenge Porn Detected!
📜 Laws: ป.อาญา ม.397 (กลั่นแกล้ง) · ม.326 (หมิ่น) · พ.ร.บ.คอมพ์ ม.14+16 · พ.ร.บ.คุ้มครองเด็ก (ถ้า <18)
🛡️ Actions: แจ้งความด่วน · แจ้งแพลตฟอร์ม (Telegram) ขอลบ · เก็บหลักฐาน ALL screenshots · 
   → ศูนย์ช่วยเหลือผู้เสียหายจากการถูกละเมิดทางเพศ · ฟ้องแพ่งเรียกค่าสินไหม
⏰ AGE OF CRIME: 3 months for defamation — URGENT!
```

This is flagged as 🟡 GOLD STANDARD in the V3 docs — specially crafted for exactly this scenario.

#### 🔵 Phase 4-7 (฿299):
- Court jurisdiction + document checklist (screenshots, perpetrator identity, platform take-down requests)
- AI drafts: criminal complaint + civil damages claim + platform removal request
- Victim support referrals integrated

#### ✅ VERDICT: **✅ GOLD-STANDARD MATCH**
> Flow 3.2 is the 🟡 GOLD STANDARD flow built specifically for revenge porn. Covers criminal (multiple charges), civil damages, platform takedown, and victim support. This is one of the best-matched flows in the entire V3 system.

---

### 🧪 Test 3C: Q3.3 #2 — ถูกกล่าวหาว่าทำอนาจารเด็ก (False Accusation of Serious Crime)

#### 🔴 Real Question
> "ถูกฟ้องว่าทำอนาจารเด็กในหมู่บ้านทั้งๆที่ผมไม่เคยทำเลยครับ!!! เด็กที่กล่าวหาผมอายุ 14 ปี พ่อแม่เค้าพาไปแจ้งความ ตอนนี้เพื่อนบ้านมองผมเหมือนเป็นอาชญากรทั้งที่ศาลยังไม่ตัดสิน ผมมีหลักฐานว่าในวันและเวลาที่ถูกกล่าวหาผมอยู่ต่างจังหวัด"

#### 🟢 Flow: **3.3 — ถูกใส่ความ (False Accusation)**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: ป.อาญา ม.173-175 (แจ้งความเท็จ) · ม.326-328 (หมิ่นประมาท)
🛡️ Actions: เก็บหลักฐานที่อยู่ (ตั๋วเครื่องบิน, รูป, พยาน) · ฟ้องกลับข้อหาแจ้งความเท็จ
⚠️ Special care: this is a serious criminal accusation → need BOTH defense + counter-suit
⚖️ Criminal Rights: right to attorney · right to remain silent · bail application
```

#### ⚠️ GAP NOTED:
> Flow 3.3 covers defamation/false accusation well but the question involves a **minor (14 years old)** — the flow does NOT address the special legal handling when the accuser is a minor, nor the intersection with juvenile court (ศาลเยาวชนและครอบครัว).

#### ⚠️ VERDICT: **⚠️ PARTIAL — Missing minor-law intersection**
> Good coverage of false accusation/defamation, but the flow should mention: (1) juvenile accuser special procedures, (2) the accused's rights in cases involving minors, (3) how to request the court consider the alibi evidence at the investigative stage. An additional sub-flow or appendix on "minors in criminal cases" is needed.

---

### 📊 Cat 3 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 3A: ใส่ร้ายใน FB group | 3.1 + 3.3 | ✅ Full | ✅ Full | ✅ |
| 3B: Revenge Porn | 3.2 (Gold) | ✅ Full | ✅ Full | ✅ |
| 3C: กล่าวหาเท็จ (เด็ก 14) | 3.3 | ✅ Core | ⚠️ No minor context | ⚠️ |

---

## หมวด 4: ประกันภัย (INSURANCE) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 4.1 | เคลมประกันรถ |
| 4.2 | เคลมประกันสุขภาพ |
| 4.3 | ยกเลิกกรมธรรม์ |

---

### 🧪 Test 4A: Q4.1 #1 — ประกันชีวิตไม่จ่าย (อ้างปกปิดโรคกระเพาะ 20 ปีก่อน)

#### 🔴 Real Question
> "สามีเพิ่งเสียชีวิตด้วยโรคมะเร็งเมื่อเดือนที่แล้ว เรายื่นเคลมไปแต่บริษัทประกันปฏิเสธการจ่าย โดยอ้างว่าสามีปกปิดประวัติการรักษาโรคกระเพาะเมื่อ 20 ปีก่อน ซึ่งไม่เกี่ยวกับมะเร็งเลย!!! แบบนี้มันแฟร์มั้ย เราจะฟ้องร้องได้ยังไงบ้างคะ"

#### 🟢 Flow: **4.2 — เคลมประกันสุขภาพ** (closest match — but this is LIFE insurance, not health)

#### ⚠️ MAP GAP:
> V3 has 4.1 (ประกันรถ), 4.2 (ประกันสุขภาพ), 4.3 (ยกเลิกกรมธรรม์) — **no dedicated "ประกันชีวิต (Life Insurance)" flow**. This question is about life insurance claim denial for alleged non-disclosure.

#### 🟢 Phase 1-3 (FREE — adapted from 4.2):
```
📜 Relevant: ป.พ.พ. ม.865 (ประกันภัย — เปิดเผยข้อความจริง) · ม.892 (อายุความฟ้องประกัน: 2 ปี)
Key issue: "non-disclosure of material facts" defense by insurer
BUT: disease 20 years ago unrelated to cause of death = likely unreasonable denial
🛡️ Actions: ยื่นอุทธรณ์ภายในบริษัท · ร้อง คปภ. (สำนักงาน คปภ. — hotline 1186) · ฟ้องศาล
```

The flow can handle the procedural aspects (appeal → OIC → court) but lacks life-insurance-specific law references (e.g., ป.พ.พ. ม.889 — suicide exclusion, incontestability period concepts).

#### ⚠️ VERDICT: **⚠️ ADAPTABLE — Missing life insurance specialization**
> Flow 4.2 (health insurance) can be stretched to cover life insurance claim denial procedureally (appeal → OIC → court). But the core legal argument here — that a 20-year-old gastritis diagnosis is NOT material to a cancer death — needs life-insurance-specific law citations. Recommend: expand 4.2 to cover life insurance OR create new flow "4.0 ประกันชีวิต."

---

### 🧪 Test 4B: Q4.3 #1 — ถูกบังคับซื้อประกันตอนกู้บ้าน

#### 🔴 Real Question
> "ไปกู้ซื้อบ้านกับแบงก์เขียวครับ พนักงานบอกว่าถ้าอยากได้ดอกเบี้ยพิเศษต้องซื้อประกันคุ้มครองวงเงินกู้ด้วยอีกปีละ 28,000 บาท เราบอกว่าไม่เอา เขาก็บอกว่าจะต้องยื่นเรื่องใหม่ทำให้อนุมัติยากขึ้นด้วย สุดท้ายเลยต้องซื้อทั้งที่ไม่เต็มใจ แบบนี้ผิดกฎหมายมั้ยครับ"

#### 🟢 Flow: **4.3 — ยกเลิกกรมธรรม์ (Unfair Insurance Practices)**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.คุ้มครองผู้บริโภค · พ.ร.บ.ธนาคารแห่งประเทศไทย · หลักเกณฑ์ คปภ. เรื่องการขายพ่วงประกัน
🛡️ Actions: ร้องเรียน คปภ. (hotline 1186) · ร้องเรียน สคบ. · ร้องเรียน แบงก์ชาติ
This is "tying" / "forced bundling" — illegal under BOT regulations!
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 4.3 specifically addresses forced insurance sales. The bank tying insurance to loan approval violates multiple regulations — this flow gives the right regulatory complaint channels. Excellent fit.

---

### 📊 Cat 4 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 4A: Life ins. claim denied | 4.2 (adapted) | ✅ Procedural | ⚠️ No life-ins specifics | ⚠️ |
| 4B: Forced ins. w/ loan | 4.3 ยกเลิกกรมธรรม์ | ✅ Full | ✅ Full | ✅ |

---

## หมวด 5: ราชการและรัฐ (GOVERNMENT) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 5.1 | ขอทะเบียน/บัตร ปชช. |
| 5.2 | รัฐละเมิด |
| 5.3 | ร้องเรียนไม่ตอบ |

---

### 🧪 Test 5A: Q5.1 #1 — ขออนุญาตก่อสร้างติดสินบน 100,000

#### 🔴 Real Question
> "ยื่นขออนุญาตก่อสร้างบ้านที่เขตบางกะปิมาตั้งแต่ปีที่แล้วค่ะ เอกสารทุกอย่างครบถ้วนตามกฎหมายหมด แต่วิศวกรโยธาที่เขตบอกว่ามันไม่ผ่านเพราะอะไรก็ไม่รู้ บอกให้ 'หาวิธีจัดการ'...มีคนในออฟฟิศกระซิบบอกว่าต้องมีค่าอำนวยความสะดวกประมาณ 100,000 ถึงจะผ่าน"

#### 🟢 Flow: **5.2 — รัฐละเมิด + 5.3 — ร้องเรียนไม่ตอบ** (cross-flow)

> ⚠️ This is a BRIBERY case (เรียกรับสินบน) — no dedicated anti-corruption flow in V3. Flows 5.2/5.3 cover government wrongdoing but focus on delays and damages, not active bribery demands.

#### 🟢 Phase 1-3 (FREE — adapted from 5.2 + 5.3):
```
📜 Relevant: ป.อาญา ม.149 (เจ้าพนักงานเรียกรับสินบน) · ม.157 (ปฏิบัติหน้าที่โดยมิชอบ) · พ.ร.บ.ป.ป.ช. 2561
🛡️ Actions: ร้องเรียน ป.ป.ช. · แจ้งความ ป.ป.ท. (ป้องกันและปราบปรามการทุจริต) · ร้องผู้ตรวจการแผ่นดิน
⚠️ CURRENT GAP: Flow 5.2 mentions state liability for damages but NOT bribery-specific procedures
```

#### ⚠️ VERDICT: **⚠️ PARTIAL — Missing bribery/anti-corruption flow**
> Flows 5.2 (รัฐละเมิด) and 5.3 (ร้องเรียนไม่ตอบ) partially cover government abuse but neither addresses **active bribery demands** by officials. A dedicated "เจ้าหน้าที่รัฐเรียกรับสินบน" sub-flow or new flow 5.4 is needed: where to report (ป.ป.ช. vs ป.ป.ท. vs DSI), how to safely gather evidence, whistleblower protections, and staged-operation legalities.

---

### 🧪 Test 5B: Q5.2 #1 — พาสปอร์ตล่าช้า 4 เดือน

#### 🔴 Real Question
> "ยื่นเรื่องขอทำพาสปอร์ตที่กรมการกงสุลแจ้งวัฒนะตั้งแต่เมื่อ 4 เดือนที่แล้วค่ะ บอกจะใช้เวลา 2 สัปดาห์ แต่ตอนนี้เงียบสนิท...ตอนนี้เราพลาดโอกาสเดินทางไปทำงานที่สิงคโปร์ไปแล้ว สูญเสียรายได้หลายแสน ฟ้องร้องหน่วยงานราชการที่ทำงานล่าช้าได้มั้ยคะ"

#### 🟢 Flow: **5.3 — ร้องเรียนไม่ตอบ + 5.2 — รัฐละเมิด** (cross-flow)

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.วิธีปฏิบัติราชการทางปกครอง 2539 · พ.ร.บ.ความรับผิดทางละเมิดของเจ้าหน้าที่ 2539
🛡️ Actions: ร้องเรียนผู้บังคับบัญชา · ร้องผู้ตรวจการแผ่นดิน · ฟ้องศาลปกครอง
Key: ระยะเวลาที่กฎหมายกำหนด vs delay → actionable!
💡 Strong case: opportunity loss (พลาดงานสิงคโปร์) = quantifiable damages
```

#### ✅ VERDICT: **✅ MATCH**
> Flow 5.3 specifically handles "ร้องเรียนไม่ตอบ/ล่าช้า." The user's claim of financial loss + specific delay makes this a strong administrative court case. Well-covered.

---

### 📊 Cat 5 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 5A: สินบน กทม. 100,000 | 5.2+5.3 (partial) | ⚠️ No bribery flow | ⚠️ Missing | ⚠️ |
| 5B: Passport delay 4 months | 5.3 + 5.2 | ✅ Full | ✅ Full | ✅ |

---

## หมวด 6: ที่ดินและทรัพย์สิน (PROPERTY) · 9 questions · 3 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 6.1 | บุกรุก |
| 6.2 | พิพาทแนวเขต |
| 6.3 | ซื้อขายไม่ได้ |
| 6.4 | มรดก |
| 6.5 | โฉนดหาย |

---

### 🧪 Test 6A: Q6.1 #1 — ที่ดินทับซ้อน น.ส.3 → โฉนด

#### 🔴 Real Question
> "ที่ดินของคุณยายที่ถือครองมากว่า 50 ปี แต่เดิมเป็น น.ส.3 แล้วเพิ่งไปรังวัดเพื่อออกโฉนด ปรากฏว่าเจ้าหน้าที่ที่ดินบอกว่าที่ดินบางส่วนทับซ้อนกับที่ดินคนอื่นที่ออกโฉนดไปก่อนแล้ว ทั้งๆที่คุณยายอยู่มาก่อน แถมโฉนดคนนั้นเพิ่งออกเมื่อ 5 ปีนี้เองแบบน่าสงสัยมาก"

#### 🟢 Flow: **6.5 — โฉนดหาย/ทับซ้อน + 6.2 — พิพาทแนวเขต**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: ป.ที่ดิน 2497 · น.ส.3 vs โฉนด rights · ครอบครองปรปักษ์ (ป.พ.พ. ม.1382)
🛡️ Actions: คัดค้านที่ สนง.ที่ดิน · ฟ้องศาลแพ่ง (เพิกถอนโฉนดที่ออกโดยมิชอบ) · ร้อง DSI (ถ้าเป็นขบวนการ)
Key: โฉนดออกทีหลังทับที่ดินที่ครอบครองมาก่อน = likely invalid issuance
```

#### ✅ VERDICT: **✅ MATCH (cross-flow)**
> Flow 6.5 + 6.2 together cover the procedural path: Land Office objection → civil court for title cancellation → evidence of prior possession. Good coverage.

---

### 🧪 Test 6B: Q6.2 #1 — เพื่อนบ้านสร้างรั้วล้ำ 1.5 ม.

#### 🔴 Real Question
> "เพื่อนบ้านสร้างรั้วล้ำเข้ามาในที่ดินเราครับ ประมาณ 1 เมตรครึ่ง ยาวตลอดแนว 20 เมตร เราบอกให้เขารื้อถอน เขาบอกว่าเขาใช้ประโยชน์ตรงนี้มาก่อนแล้ว (ครอบครองปรปักษ์?) ทั้งๆที่เรามีโฉนดกับผลรังวัด"

#### 🟢 Flow: **6.2 — พิพาทแนวเขต**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: ป.พ.พ. ม.1336 (กรรมสิทธิ์) · ม.1382 (ครอบครองปรปักษ์ — 10 ปีโดยสงบเปิดเผย)
⚠️ Key legal issue: Does neighbor qualify for adverse possession? (user has title deed + survey)
🛡️ Actions: เจรจา → ร้องที่ดิน → ฟ้องศาล (ขับไล่ + รื้อถอน + ค่าเสียหาย)
⏰ Important: การครอบครองปรปักษ์ต้องครบ 10 ปี + โดยสุจริต
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 6.2 directly addresses boundary disputes including the adverse possession claim. Covers the negotiation → Land Department → court escalation ladder.

---

### 📊 Cat 6 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 6A: โฉนดทับซ้อน | 6.5 + 6.2 | ✅ Full | ✅ Full | ✅ |
| 6B: รั้วล้ำ 1.5 ม. | 6.2 พิพาทแนวเขต | ✅ Full | ✅ Full | ✅ |

---

## หมวด 7: แรงงาน (LABOUR) · 12 questions · 4 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 7.1 | ถูกเลิกจ้างไม่เป็นธรรม |
| 7.2 | นายจ้างค้างจ่ายค่าจ้าง |
| 7.3 | ถูกบังคับลาออก |
| 7.4 | เงื่อนไขการจ้างไม่เป็นธรรม |

---

### 🧪 Test 7A: Q7.1 #1 — เลิกจ้างกะทันหัน 10 ปี ไม่มีค่าชดเชย

#### 🔴 Real Question
> "ทำงานมาจะครบ 10 ปีละ โดนเรียกเข้าห้องประชุมแจ้งเลิกจ้างลอยๆ บอกแค่ว่าปรับโครงสร้างองค์กร ไม่มีหนังสือบอกล่วงหน้า ไม่มีค่าชดเชยอะไรเลย บอกให้เซ็นใบลาออกเองจะได้ไม่เสียประวัติ"

#### 🟢 Flow: **7.1 — ถูกเลิกจ้างไม่เป็นธรรม**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.คุ้มครองแรงงาน ม.118 — ค่าชดเชยตามอายุงาน
   • 10 ปีขึ้นไป → 400 วัน!
   • No notice = additional 1 month pay (ม.17)
🛡️: อย่าเซ็นใบลาออกเด็ดขาด! → ร้องตรวจแรงงาน → ศาลแรงงาน (ฟรี! ไม่มีค่าธรรมเนียม)
🅰️ ทำเองฟรี · 🅱️ ทนาย ฿15,000-50,000 · 🅲️ ร้องตรวจแรงงานก่อน
⚖️ สิทธิ: Severance 400 วัน + Notice pay + Damages
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 7.1 directly addresses this, with critical advice (DON'T sign resignation!) and clear severance calculation for 10+ years.

---

### 🧪 Test 7B: Q7.2 #1 — ร้านอาหาร 10:00-22:00 ไม่มี OT

#### 🔴 Real Question
> "ร้านอาหารที่เราทำงานอยู่ จ้างเป็นรายเดือน 12,000 แต่เวลาเข้างาน 10.00-22.00 น. หกวันต่อสัปดาห์ ไม่มี OT ไม่มีวันหยุดชดเชย"

#### 🟢 Flow: **7.2 — นายจ้างค้างจ่ายค่าจ้าง** (partial — this is about OT rights, not just unpaid wages)

> ⚠️ V3 has no dedicated OT/overtime calculation flow. Flow 7.2 (ค้างจ่ายค่าจ้าง) covers unpaid wages but the user's question is also about: **working hours exceeding legal limits**, **mandatory rest days**, **OT calculation formula**.

#### 🟢 Phase 1-3 (FREE — via 7.2 adapted):
```
📜 Relevant: พ.ร.บ.คุ้มครองแรงงาน ม.23 (ทำงาน ≤8 ชม./วัน, ≤48 ชม./สัปดาห์) · ม.61 (OT 1.5-3x)
This user works 12 hrs × 6 days = 72 hrs/week — exceeds MAX 48!
🛡️: ร้องตรวจแรงงาน · เรียกร้อง OT ย้อนหลัง (อายุความ 2 ปี)
⚠️ Flow 7.2 covers wage recovery but NOT OT calculation formulas or working hours violations
```

#### ⚠️ VERDICT: **⚠️ PARTIAL — No OT/working hours violation flow**
> V3 needs a dedicated "ค่าล่วงเวลา / OT / ชั่วโมงทำงานเกินกฎหมาย" sub-flow. Current flow 7.2 covers wage recovery procedurally but the user also needs: OT rate calculations (1.5x, 2x, 3x), rest day pay rules, maximum hours violations, and how to calculate retrospective OT claims. This is one of the most common labor questions in Thailand.

---

### 🧪 Test 7C: Q7.3 #1 — อุบัติเหตุระหว่างเดินทางไปทำงาน (ประกันสังคม)

#### 🔴 Real Question
> "ประสบอุบัติเหตุระหว่างเดินทางไปทำงาน มอไซค์ล้มขาหัก รพ.ที่รักษาบอกว่าประกันสังคมไม่คุ้มครองเพราะเกิดนอกสถานที่ทำงาน แต่เราอ่านในเน็ตบอกว่าเดินทางไป-กลับก็คุ้มครองนะ"

#### 🟢 Flow: **No dedicated flow in V3 for Social Security / Workmen's Compensation!**

> ❌ V3 Cat 7 has 4 flows (7.1-7.4) — NONE cover ประกันสังคม (Social Security) or กองทุนเงินทดแทน (Workmen's Compensation Fund). This is a MAJOR gap.

#### ⚠️ VERDICT: **❌ NO FLOW — Major gap**
> The user's question is about a very common scenario: commuting accident coverage under Social Security (มาตรา 33, กองทุนเงินทดแทน). V3 has zero flows covering Social Security claims, benefits, or disputes. This affects ALL 3 questions in sub-topic 7.3.

---

### 📊 Cat 7 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 7A: เลิกจ้าง 10 ปี | 7.1 | ✅ Full | ✅ Full | ✅ |
| 7B: ทำงาน 12 ชม. ไม่มี OT | 7.2 (partial) | ⚠️ No OT calc | ⚠️ Missing | ⚠️ |
| 7C: อุบัติเหตุเดินทาง | NONE | ❌ No SSO flow | ❌ Missing | ❌ |

---

## หมวด 8: ผู้บริโภค (CONSUMER) · 12 questions · 4 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 8.1 | สินค้าไม่ตรงปก |
| 8.2 | สั่งของออนไลน์แล้วไม่ได้รับ |
| 8.3 | อาหารเป็นพิษจากร้านอาหาร |
| 8.4 | โฆษณาเกินจริง |

---

### 🧪 Test 8A: Q8.1 #1 — มือถือ 25,000 เครื่องดับ 12 วัน ซ่อม 2 รอบไม่หาย

#### 🔴 Real Question
> "ซื้อมือถือจากร้านในห้าง ราคา 25,000 ใช้ได้ 12 วันเครื่องดับเอง ร้านบอกให้ส่งศูนย์อย่างเดียว ไม่รับคืนเงิน ไม่รับเปลี่ยนเครื่องใหม่ ซ่อมแล้ว 2 รอบก็ยังไม่หาย แบบนี้เราขอคืนเงินได้ไหม"

#### 🟢 Flow: **8.1 — สินค้าไม่ตรงปก / ชำรุดบกพร่อง**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: ป.พ.พ. ม.472 (ความชำรุดบกพร่อง) · พ.ร.บ.คุ้มครองผู้บริโภค · สคบ.
🛡️: แจ้งร้านภายใน 20 วัน · ขอเปลี่ยน/คืนเงิน · ร้อง สคบ. · ฟ้องคดีผู้บริโภค
Key: ซ่อม 2 รอบไม่หาย = สินค้ามีความบกพร่องร้ายแรง → ขอคืนเงินได้!
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 8.1 covers defective goods perfectly. The 2-repair rule is a textbook consumer protection case for refund.

---

### 🧪 Test 8B: Q8.4 #1 — ประกันสะสมทรัพย์ (ถูกแบงก์หลอกขาย)

#### 🔴 Real Question
> "ซื้อประกันสะสมทรัพย์จากแบงก์ตอนไปทำธุรกรรม เซลล์บอกแค่ว่าได้ดอกเยอะกว่าฝากประจำ ที่เซ็นไปก็ไม่ได้อ่าน พอกลับมาบ้านอ่านเจอว่าต้องจ่ายเบี้ยปีละ 120,000 ยกเลิกไม่ได้ 7 ปี ถ้ายกเลิกได้เงินคืนแค่ 30%"

#### 🟢 Flow: **4.3 — ยกเลิกกรมธรรม์ (Unfair insurance)** — belongs in Cat 4 but user question is under Cat 8

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.คุ้มครองผู้บริโภค · หลักเกณฑ์ คปภ. (free-look period) · สัญญาไม่เป็นธรรม
🛡️: ขอยกเลิกภายใน Free-Look (14-30 วัน) · ร้อง คปภ. · ร้อง สคบ. · ฟ้องศาลผู้บริโภค
⚠️ CRITICAL: ถ้าเพิ่งซื้อภายใน 15-30 วัน → Free-Look cancellation (ได้เงินคืนเต็ม!)
```

#### ✅ VERDICT: **✅ MATCH (cross-category)**
> Good coverage via flow 4.3. The free-look period advice is crucial. However, this could also benefit from a cross-reference to flow 8.4 (false advertising if the bank misrepresented the product).

---

### 📊 Cat 8 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 8A: มือถือเสียซ่อมไม่หาย | 8.1 | ✅ Full | ✅ Full | ✅ |
| 8B: ถูกหลอกขายประกัน | 4.3 (cross) | ✅ Full | ✅ Full | ✅ |

---

## หมวด 9: หนี้สิน (DEBT) · 15 questions · 5 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 9.1 | ถูกทวงหนี้ข่มขู่ |
| 9.2 | หนี้นอกระบบ |
| 9.3 | ล้มละลาย |
| 9.4 | ติด Blacklist / เครดิตบูโร |

---

### 🧪 Test 9A: Q9.1 #1 — ทวงหนี้บัตรเครดิตแบบข่มขู่ (โทรหาญาติ)

#### 🔴 Real Question
> "เป็นหนี้บัตรเครดิต 3 ใบ รวมประมาณ 200,000 จ่ายไม่ไหวเพราะตกงาน มีเบอร์แปลกโทรมาทวงทุกวัน วันละ 10-20 สาย บางทีก็โทรหาญาติพี่น้องเรา บอกให้ช่วยใช้หนี้แทน"

#### 🟢 Flow: **9.1 — ถูกทวงหนี้ข่มขู่**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.ทวงถามหนี้ พ.ศ.2558 — ห้ามทวงกับบุคคลอื่น (ญาติ/เพื่อน/ที่ทำงาน!) · ห้ามข่มขู่ · ห้ามใช้ข้อความรุนแรง · ห้ามทวงก่อน 8:00/หลัง 20:00
🛡️: จดบันทึกทุกครั้ง (วัน เวลา เบอร์) · ร้องเรียน คณะกรรมการกำกับการทวงถามหนี้ กระทรวงการคลัง · แจ้งความ
บทลงโทษ: จำคุก ≤1 ปี / ปรับ ≤100,000
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 9.1 specifically covers aggressive debt collection. The พ.ร.บ.ทวงถามหนี้ prohibits calling third parties — the collector is clearly violating the law.

---

### 🧪 Test 9B: Q9.2 #1 — หนี้นอกระบบ ดอกเบี้ยโหด รับจริง 85,000 แต่สัญญา 100,000

#### 🔴 Real Question
> "กู้เงินนอกระบบมาจำนวน 100,000 บาท ทำสัญญาเขียนว่าเงินต้น 100,000 ดอกเบี้ยร้อยละ 5 ต่อเดือน แต่ตอนรับเงินจริงได้แค่ 85,000 เพราะหักค่าดำเนินการ 15,000 แถมต้องจ่ายคืนเป็นรายวัน วันละ 1,400 เป็นเวลา 100 วัน รวมเป็น 140,000"

#### 🟢 Flow: **9.2 — หนี้นอกระบบ**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.ห้ามเรียกดอกเบี้ยเกินอัตรา พ.ศ.2560 (ดอกเบี้ย ≤15%/ปี) · ป.อาญา ม.355 (เรียกดอกเบี้ยเกินอัตรา)
Real interest here: 140,000 payback on 85,000 received over 100 days = astronomical!
🛡️: แจ้งความ (ดอกเบี้ยเกินอัตรา + ฉ้อโกง) · ศูนย์ช่วยเหลือลูกหนี้ (กระทรวงยุติธรรม) · ร้อง DSI
⚠️ Money received (85,000) ≠ money on contract (100,000) = additional fraud element
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 9.2 is built for illegal lending with excessive interest. The "รับจริงไม่ตรงสัญญา" angle is a common loan-shark tactic — the flow covers this as an additional fraud charge.

---

### 🧪 Test 9C: Q9.5 #3 — รายการใช้จ่ายบัตรเครดิตที่ไม่ได้ใช้ (Fraudulent transaction dispute)

#### 🔴 Real Question
> "มีรายการใช้จ่ายที่เราไม่ได้เป็นคนใช้ ตรวจสอบแล้วเป็นรายการใช้จ่ายออนไลน์ตอนตี 3 ซึ่งเป็นเวลาที่เราหลับอยู่ ธนาคารบอกว่าเป็นรายการใช้จ่ายที่ผ่าน OTP ซึ่งเราก็ไม่เคยได้รับ SMS OTP อะไรเลย ธนาคารไม่ยอมรับผิดชอบ"

#### 🟢 Flow: **No dedicated flow for credit card fraud / unauthorized transaction dispute**

> ⚠️ The closest flows are 9.1 (debt collection — not relevant) and 9.4 (credit blacklisting — not relevant). This is a bank-customer dispute about unauthorized transactions.

#### ⚠️ VERDICT: **❌ NO FLOW — Unauthorized transactions not covered**
> V3 needs a flow for disputing unauthorized credit card/debit card transactions. This involves: Bank of Thailand regulations on cardholder liability, OTP dispute procedures, fraud investigation timelines, and the consumer's right to refuse payment for unauthorized transactions. This is a common issue affecting ALL 3 questions in sub-topic 9.5.

---

### 📊 Cat 9 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 9A: ทวงหนี้ข่มขู่ | 9.1 | ✅ Full | ✅ Full | ✅ |
| 9B: หนี้นอกระบบดอกโหด | 9.2 | ✅ Full | ✅ Full | ✅ |
| 9C: บัตรเครดิต unauthorized | NONE | ❌ No flow | ❌ Missing | ❌ |

---

## หมวด 10: ที่อยู่อาศัย (HOUSING) · 12 questions · 4 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 10.1 | ผู้เช่าไม่จ่ายค่าเช่า |
| 10.2 | ผู้ให้เช่าไม่คืนเงินมัดจำ |
| 10.3 | ถูกไล่ที่อยู่อาศัยไม่เป็นธรรม |

---

### 🧪 Test 10A: Q10.1 #1 — สัญญาเช่าหมดอายุแต่จ่ายค่าเช่าต่อเนื่อง 6 เดือน → ถูกไล่ออก 15 วัน

#### 🔴 Real Question
> "เช่าคอนโดอยู่ 1 ปี หมดสัญญาแล้วไม่ได้ต่อสัญญาเป็นลายลักษณ์อักษร แต่จ่ายค่าเช่าต่อเนื่องมาอีก 6 เดือน เจ้าของก็รับเงินตามปกติ อยู่ๆ บอกให้เราย้ายออกภายใน 15 วัน อ้างว่าสัญญาหมดอายุแล้ว"

#### 🟢 Flow: **10.3 — ถูกไล่ที่อยู่อาศัยไม่เป็นธรรม**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: ป.พ.พ. ม.564 (สัญญาเช่าที่ไม่มีกำหนดระยะเวลา) — การรับค่าเช่าต่อ = สัญญาเช่าต่อเนื่องโดยปริยาย
🛡️: การบอกเลิกสัญญาเช่าที่ไม่มีกำหนดเวลาต้องบอกล่วงหน้า 1 งวดการชำระค่าเช่า (30 วัน)
⚠️ 15 วัน = ไม่ถูกต้อง! ต้องให้ 30 วัน (1 งวดค่าเช่า)
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 10.3 covers unfair eviction well. The key legal point — acceptance of continued rent creates an indefinite-term lease requiring proper notice — is directly addressed.

---

### 🧪 Test 10B: Q10.4 #1 — ทางจำเป็นถูกปิด (ซอยส่วนบุคคล)

#### 🔴 Real Question
> "ทางเข้าบ้านเราต้องผ่านซอยส่วนบุคคล ก่อนซื้อเจ้าของเดิมบอกว่ามีภาระจำยอม สามารถใช้ทางนี้ได้ตลอด แต่ตอนนี้เจ้าของซอยกำลังจะสร้างกำแพงปิดซอย ไม่ให้เราใช้ทางเข้าออกอีก"

#### 🟢 Flow: **No dedicated "ทางจำเป็น / ภาระจำยอม" flow in V3**

> ⚠️ This is a servitude/easement (ภาระจำยอม) and right of way (ทางจำเป็น) question. V3 Housing flows (10.1-10.3) focus on rental disputes, not property rights.

#### ⚠️ VERDICT: **❌ NO FLOW — Easement/servitude not covered**
> The user's question involves ป.พ.พ. ม.1349 (ทางจำเป็น) and ม.1387 (ภาระจำยอม). V3 has NO flow for these property rights concepts. This affects ALL 3 questions in sub-topic 10.4. A flow covering servitude, right of way, and easement creation/extinguishment is needed.

---

### 📊 Cat 10 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 10A: สัญญาเช่าต่อเนื่อง | 10.3 ถูกไล่ไม่เป็นธรรม | ✅ Full | ✅ Full | ✅ |
| 10B: ทางจำเป็นถูกปิด | NONE | ❌ No servitude flow | ❌ Missing | ❌ |

---

## หมวด 11: ครอบครัว (FAMILY) · 15 questions · 5 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 11.1 | หย่า |
| 11.2 | ปกครองบุตร |
| 11.3 | มรดก |
| 11.4 | คู่สมรสนอกใจ |
| 11.5 | ทำร้ายร่างกายในครอบครัว |

---

### 🧪 Test 11A: Q11.1 #1 — หย่า แบ่งสินสมรส (แม่บ้าน 8 ปี สามีนอกใจ)

#### 🔴 Real Question
> "แต่งงานมา 8 ปี มีลูก 2 คน สามีนอกใจมีเมียน้อย จับได้เพราะเห็นแชทในไลน์ เราเป็นแม่บ้านไม่ได้ทำงาน สินสมรสมีบ้าน 1 หลัง รถ 2 คัน และเงินเก็บในบัญชีสามีประมาณ 2 ล้าน ทั้งหมดอยู่ในชื่อสามี เราจะได้ส่วนแบ่งเท่าไหร่"

#### 🟢 Flow: **11.1 — หย่า + 11.4 — คู่สมรสนอกใจ** (cross-flow)

#### 🟢 Phase 1-3 (FREE — 11.1):
```
📜 Laws: ป.พ.พ. ม.1516 (เหตุหย่า — มีชู้) · ม.1533 (แบ่งสินสมรส 50:50) · ม.1598/40 (ค่ารายได้ระหว่างสมรส)
🛡️: All assets acquired during marriage = สินสมรส = 50:50 regardless of whose name!
   + ค่าทดแทน from adulterous spouse (ม.1523) + ค่าอุปการะเลี้ยงดูบุตร
   + Court can award >50% to non-working spouse due to economic disparity
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 11.1 + 11.4 together perfectly address: divorce grounds (adultery), division of marital property (50:50 — all in husband's name doesn't matter!), alimony, child support, and moral damages for infidelity. Critical reassurance for the housewife with no income.

---

### 🧪 Test 11B: Q11.3 #1 — พ่อเสียชีวิตไม่มีพินัยกรรม ลูกชายคนโตอ้างสิทธิ์มากกว่า

#### 🔴 Real Question
> "พ่อเสียชีวิตกะทันหันโดยไม่ได้ทำพินัยกรรม มีทรัพย์มรดกคือบ้าน 2 หลัง เงินในแบงก์ 5 ล้าน และที่นา 10 ไร่ ทายาทมีแม่กับลูก 4 คน (รวมเรา) แต่พี่ชายคนโตบอกว่าเขาเป็นลูกชายคนเดียว จะได้บ้าน 1 หลังกับที่นา 10 ไร่ โดยอ้างว่าเป็นผู้สืบสกุล"

#### 🟢 Flow: **11.3 — มรดก (Inheritance)** + **6.4 — มรดก (Property)**

#### 🟢 Phase 1-3 (FREE — 11.3):
```
📜 Laws: ป.พ.พ. ม.1629 (ทายาทโดยธรรม) · ม.1635 (การแบ่งมรดก — เท่ากันทุกคน!)
🛡️: NO will = intestate succession → spouse (แม่) gets 50% · children split remaining 50% equally
   ❌ "ผู้สืบสกุล" มี NO legal standing — all children equal regardless of gender!
   💡 Action: ยื่นคำร้องขอจัดการมรดกที่ศาล · ขอตั้งผู้จัดการมรดก
```

#### ✅ VERDICT: **✅ STRONG MATCH**
> Flow 11.3 explicitly covers intestate succession. The "ลูกชายคนเดียวได้มากกว่าเพราะสืบสกุล" myth is directly debunked — modern Thai succession law (since 2478!) gives equal rights to all children.

---

### 🧪 Test 11C: Q11.5 #1 — คู่รัก LGBTQ+ สมรสเท่าเทียม ทํา IVF

#### 🔴 Real Question
> "เราเป็นคู่รัก LGBTQ+ อยู่ด้วยกันมา 10 ปี จดทะเบียนสมรสตามกฎหมายสมรสเท่าเทียมแล้ว อยากมีลูกด้วยกันโดยให้อีกฝ่ายตั้งครรภ์ผ่านการทำ IVF โดยใช้อสุจิของอีกฝ่าย ลูกที่เกิดมาทั้งคู่จะเป็นบิดามารดาตามกฎหมายเลยไหม"

#### 🟢 Flow: **No dedicated LGBTQ+ / Marriage Equality / IVF parentage flow**

> ⚠️ V3 Family flows (11.1-11.5) were built before/without specific marriage equality provisions. The equal marriage act (พ.ร.บ.สมรสเท่าเทียม) changed parentage rules for same-sex couples using assisted reproduction.

#### ⚠️ VERDICT: **❌ NO FLOW — LGBTQ+ / Marriage Equality not addressed**
> This is a forward-looking legal question about Thailand's marriage equality law. V3 needs a flow covering: (1) parentage determination under equal marriage, (2) IVF/surrogacy legal parentage for same-sex couples, (3) adoption by same-sex married couples. This affects all 3 questions in sub-topic 11.5.

---

### 📊 Cat 11 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 11A: หย่า+สินสมรส | 11.1+11.4 | ✅ Full | ✅ Full | ✅ |
| 11B: มรดกไม่มีพินัยกรรม | 11.3+6.4 | ✅ Full | ✅ Full | ✅ |
| 11C: LGBTQ+ IVF parentage | NONE | ❌ No marriage equality | ❌ Missing | ❌ |

---

## หมวด 12: อุบัติเหตุ (ACCIDENT) · 15 questions · 5 sub-topics

### V3 Flows Available:
| Flow | Name |
|------|------|
| 12.1 | อุบัติเหตุรถยนต์ |
| 12.2 | ชนแล้วหนี |
| 12.3 | บาดเจ็บสาหัสจากอุบัติเหตุ |

---

### 🧪 Test 12A: Q12.1 #1 — เปิดประตูรถชนมอไซค์ล้ม

#### 🔴 Real Question
> "ขับรถมอเตอร์ไซค์ไปซื้อของ อยู่ๆ มีรถเก๋งเปิดประตูรถกะทันหันโดยไม่มอง ชนล้มได้รับบาดเจ็บ แขนหัก มอไซค์พัง คนขับรถเก๋งมีประกันชั้น 1 แต่ประกันบอกว่าผิดทั้งคู่เพราะเราขับชิดซ้ายเกินไป"

#### 🟢 Flow: **12.1 — อุบัติเหตุรถยนต์**

#### 🟢 Phase 1-3 (FREE):
```
📜 Laws: พ.ร.บ.จราจรทางบก · พ.ร.บ.คุ้มครองผู้ประสบภัยจากรถ พ.ศ.2535 · ป.พ.พ. ม.420 (ละเมิด)
🛡️: แจ้งความ · เรียกประกัน · เรียกค่ารักษา + ค่าเสียหาย · พ.ร.บ.คุ้มครองผู้ประสบภัย (จ่ายทุกกรณี)
⚠️ Insurance "ผิดทั้งคู่" argument is disputable — opening door into traffic is PRIMARILY at fault
⏰ Report to police within 24 hours · Insurance claim within 14 days
```

#### ✅ VERDICT: **✅ MATCH**
> Flow 12.1 covers car accidents comprehensively. The insurance "shared fault" denial tactic is a common issue and the flow gives escalation paths (police report → insurance appeal → lawyer → court).

---

### 🧪 Test 12B: Q12.4 #1 — ประกันชีวิตปฏิเสธ (อ้างปกปิดดื่มเหล้า)

#### 🔴 Real Question
> "พ่อทำประกันชีวิตไว้ 10 ปี ผ่านมา 8 ปี พ่อเสียชีวิตด้วยโรคมะเร็งตับอ่อน ยื่นเคลมประกัน บริษัทประกันปฏิเสธการจ่ายเงิน โดยอ้างว่าพ่อปกปิดข้อเท็จจริงเรื่องการดื่มเหล้า ทั้งที่ตอนทำประกันภัย พ่อไม่ได้ดื่มเหล้าหนัก"

#### 🟢 Flow: **No dedicated accident/life insurance claim dispute flow in Cat 12**

> ⚠️ The closest flow is 4.2 (เคลมประกันสุขภาพ) from Cat 4. Cat 12 flows cover accident events (road accidents, hit-and-run, injuries), not insurance claim disputes.

#### ⚠️ VERDICT: **⚠️ CROSS-CATEGORY — Needs 4.2 adaptation**
> This is essentially an insurance claim denial case (like Test 4A). The user needs to go through flow 4.2 (health/life insurance claims) from Cat 4. The Cat 12 flows are for the accident EVENT, not the insurance aftermath. But sub-topic 12.4 explicitly has 3 questions about insurance claim denials. Recommendation: Add cross-references from Cat 12 flows to Cat 4 insurance flows, or create a unified insurance disputes category.

---

### 📊 Cat 12 Summary
| Question | Flow | Free Coverage | Paid Coverage | Verdict |
|----------|------|:---:|:---:|:---:|
| 12A: เปิดประตูรถชน | 12.1 อุบัติเหตุรถยนต์ | ✅ Full | ✅ Full | ✅ |
| 12B: ประกันชีวิตปฏิเสธ | 4.2 (cross) | ⚠️ Procedural | ⚠️ Needs adaptation | ⚠️ |

---

## 📊 SUMMARY: Per-Category Test Results

| Category | Questions | Tested | ✅ | ⚠️ | ❌ | % Passing |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. ONLINE FRAUD** | 9 | 3 | 2 | 1 | 0 | **67%** |
| **2. CRIME** | 9 | 3 | 2 | 0 | 1 | **67%** |
| **3. DEFAMATION** | 9 | 3 | 2 | 1 | 0 | **67%** |
| **4. INSURANCE** | 9 | 2 | 1 | 1 | 0 | **50%** |
| **5. GOVERNMENT** | 9 | 2 | 1 | 1 | 0 | **50%** |
| **6. PROPERTY** | 9 | 2 | 2 | 0 | 0 | **100%** |
| **7. LABOUR** | 12 | 3 | 1 | 1 | 1 | **33%** |
| **8. CONSUMER** | 12 | 2 | 2 | 0 | 0 | **100%** |
| **9. DEBT** | 15 | 3 | 2 | 0 | 1 | **67%** |
| **10. HOUSING** | 12 | 2 | 1 | 0 | 1 | **50%** |
| **11. FAMILY** | 15 | 3 | 2 | 0 | 1 | **67%** |
| **12. ACCIDENT** | 15 | 2 | 1 | 1 | 0 | **50%** |
| **TOTAL** | **135** | **30** | **19** | **6** | **5** | **63%** |

---

## 🔴 CRITICAL GAPS — What Real Questions Can't V3 Flows Handle?

### ❌ GAP 1: Self-Defense / Excessive Force (ป้องกันโดยชอบด้วยกฎหมาย)
- **Affects:** Q2.2 #3, and similar self-defense scenarios
- **Missing:** ป.อาญา ม.68 (justified defense) vs ม.69 (excessive defense) distinction
- **User needs:** "Am I going to be charged for fighting back against a burglar?"
- **Recommendation:** New sub-flow under Cat 2: "2.5 — ป้องกันตัว / ใช้กำลังเกินกว่าเหตุ"

### ❌ GAP 2: Social Security / Workmen's Compensation (ประกันสังคม / กองทุนเงินทดแทน)
- **Affects:** ALL 3 questions in sub-topic 7.3
- **Missing:** SSO benefits, commuting accident coverage, disability assessment appeals, employer non-payment of contributions
- **User needs:** "ประกันสังคมคุ้มครองอุบัติเหตุระหว่างเดินทางไหม?" "นายจ้างไม่จ่ายสมทบ"
- **Recommendation:** New sub-flow under Cat 7: "7.5 — ประกันสังคม / กองทุนเงินทดแทน"

### ❌ GAP 3: Bribery / Official Corruption (เจ้าหน้าที่รัฐเรียกรับสินบน)
- **Affects:** Q5.1 #1, #2, #3
- **Missing:** Anti-corruption reporting channels (ป.ป.ช. vs ป.ป.ท. vs DSI), evidence gathering for bribery, whistleblower protections
- **User needs:** "จนท.เรียกเงิน 100,000 ถึงจะเซ็นอนุมัติ" — this is NOT a standard "ร้องเรียนไม่ตอบ" case
- **Recommendation:** New sub-flow under Cat 5: "5.4 — เจ้าหน้าที่รัฐเรียกรับสินบน / ทุจริต"

### ❌ GAP 4: Servitude / Right of Way / Easement (ภาระจำยอม / ทางจำเป็น)
- **Affects:** ALL 3 questions in sub-topic 10.4
- **Missing:** ป.พ.พ. ม.1349 (ทางจำเป็น), ม.1387 (ภาระจำยอม), creation/extinguishment of easements
- **User needs:** "ทางเข้าบ้านถูกปิด" "ใช้ทางคนอื่นมา 10 ปีแล้ว"
- **Recommendation:** New sub-flow under Cat 10: "10.4 — ภาระจำยอม / ทางจำเป็น"

### ❌ GAP 5: LGBTQ+ / Marriage Equality (สมรสเท่าเทียม / สิทธิคู่ชีวิต)
- **Affects:** ALL 3 questions in sub-topic 11.5
- **Missing:** Parentage rights under equal marriage, IVF/surrogacy for same-sex couples, adoption by same-sex married couples
- **User needs:** "จดทะเบียนสมรสเท่าเทียมแล้ว — IVF ลูกจะเป็นลูกของทั้งคู่ตามกฎหมายเลยไหม?"
- **Recommendation:** New sub-flow under Cat 11: "11.6 — สมรสเท่าเทียม / สิทธิคู่ชีวิต / บุตรบุญธรรม"

### ⚠️ GAP 6: Credit Card Unauthorized Transactions (รายการใช้จ่ายบัตรที่ไม่ได้ทำเอง)
- **Affects:** ALL 3 questions in sub-topic 9.5
- **Missing:** Dispute procedures, cardholder liability under BOT regulations, OTP fraud dispute
- **User needs:** "มีรายการใช้จ่ายที่เราไม่ได้ทำ ธนาคารไม่รับผิดชอบ"
- **Recommendation:** New sub-flow under Cat 9: "9.5 — โต้แย้งรายการใช้จ่ายบัตรเครดิต / Unauthorized Transaction"

### ⚠️ GAP 7: OT / Working Hours Violations (ค่าล่วงเวลา / OT / ชั่วโมงทำงานเกิน)
- **Affects:** Q7.2 #1, #2, #3
- **Missing:** OT calculation formulas (1.5x, 2x, 3x), maximum hours violations, rest day compensation
- **User needs:** "ทำงาน 12 ชม. 6 วัน ไม่มี OT" "เงินเดือนรวม OT ผิดกฎหมาย"
- **Recommendation:** Expand flow 7.2 to include OT calculation appendix

### ⚠️ GAP 8: Life Insurance Specific Claims (ประกันชีวิต — specific law)
- **Affects:** Q4.1 #1, Q12.4 #1
- **Missing:** Life insurance-specific provisions (incontestability, suicide exclusion, beneficiary disputes)
- **User needs:** "ประกันชีวิตไม่จ่าย อ้างปกปิดข้อเท็จจริงที่ไม่เกี่ยวข้อง"
- **Recommendation:** Expand flow 4.2 to cover life insurance, or create "4.0 — ประกันชีวิต"

### ⚠️ GAP 9: Minors in Criminal Cases (เยาวชนในคดีอาญา)
- **Affects:** Q3.3 #2, Q11.3 #3
- **Missing:** Juvenile court procedures, age-of-criminal-responsibility, special protections
- **Recommendation:** Add minor-law appendix to flows 3.3 and 2.3

---

## 📈 OVERALL ASSESSMENT

| Metric | Value |
|--------|-------|
| **Total V3 Flows** | 47 |
| **Total Real Questions** | 135 |
| **Questions Mappable to Existing Flows** | ~110 (81%) |
| **Questions Requiring New Flows** | ~25 (19%) |
| **Fully Covered (✅)** | 63% |
| **Partially Covered (⚠️)** | 20% |
| **Not Covered (❌)** | 17% |
| **Critical Gaps (New Flow Needed)** | 5 (Self-Defense, SSO, Bribery, Easement, LGBTQ+) |
| **Moderate Gaps (Expansion Needed)** | 4 (OT calc, Life Insurance, Card Disputes, Minor Law) |

### 🟢 Strengths:
- Online fraud flows (1.1-1.5) are comprehensive and well-matched
- Consumer protection (Cat 8) has excellent coverage
- Property/dispute flows (Cat 6) cover the core scenarios well
- Divorce + inheritance (Cat 11) coverage is strong for traditional scenarios

### 🟡 Improvements Needed:
- Labor flows need OT/SSO expansion (Cat 7: 33% pass rate)
- Housing flows need easement/servitude coverage (Cat 10)
- Insurance flows need life insurance specialization

### 🔴 Urgent Gaps:
- Self-defense law (very common in real-world criminal cases)
- Social Security (affects all employed Thais)
- Anti-corruption/bribery (distinct from general government complaints)
- LGBTQ+ marriage equality (new law, rapidly growing demand)
- Easement/right-of-way property disputes
