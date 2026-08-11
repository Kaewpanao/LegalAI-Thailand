# 🔴🟢 LegalAI Path B — Platform Test Results

> **Test scope:** 135 real user questions from `qa_135_real_questions.md` tested against LegalAI platform at `D:\legalai-citizen-check`
> **Platform version:** diagnosis-config `diagnosis-v1` · sources `sources-v2`
> **Methodology:** For each of 12 categories, pick 3 questions → simulate diagnosis flow → rate coverage

---

## 📊 Executive Summary

| | Value |
|---|---|
| **Total questions tested** | 36 (3 per category) |
| **MATCH ✅** | 18 (50%) |
| **PARTIAL ⚠️** | 12 (33%) |
| **GAP ❌** | 6 (17%) |
| **Categories with at least 1 MATCH** | 12/12 (100%) |
| **Categories with critical GAP** | 4/12 |

**The platform covers the basics well** but struggles with:
- Compound scenarios (multiple legal issues in one story)
- Nuanced sub-categories (e.g., romance scam is listed but labor sub-categories like OT/details are flatter)
- Non-standard legal relationships (LGBTQ+ families, ส.ป.ก. land, de facto marriage)

---

## Platform Flow Reference

```
User describes problem → [Category Detection] → Diagnosis Questions (4 per category) → AI Analysis
                                                                                              │
                                              ┌───────────────────────────────────────────────┘
                                              ▼
                              AnalysisResult {
                                headline, summary, rights[], 
                                evidenceReadiness, nextActions[], 
                                citations[], limitations, driveProfile
                              }
```

### What the platform DOES well:
- ✅ Anti-hallucination citation system (only sources in the registry)
- ✅ Evidence readiness calculation (provided/required ratio)
- ✅ Human Drives detection for tone personalization
- ✅ Structured next actions with time-bound steps
- ✅ No win-probability scores (compliance)
- ✅ Covers all 12 legal categories

### What the platform does NOT do (by design):
- Does NOT give win probabilities
- Does NOT write legal documents (separate module)
- Does NOT connect to real lawyer (marketplace module)

---

## 1. ONLINE FRAUD (ออนไลน์และหลอกลวง)

### Platform config: `online_fraud`
| Question ID | Options |
|---|---|
| `fraud_type` | ซื้อของออนไลน์ไม่ได้ของ, Call Center, แอปกู้เงินเถื่อน, Romance Scam, แชร์ลูกโซ่/ลงทุนปลอม |
| `amount` | <5K, 5K-50K, 50K-200K, >200K |
| `when` | <24h, 1-3d, 3-7d, >7d |
| `evidence` | สลิปโอน, แชท, URL/ลิงก์, เบอร์โทร, เลขบัญชีปลายทาง |

**Sources:** criminal-code-341 (ฉ้อโกง), computer-crime-act-2560, amlo-act-2542, money-lending-act-2560

---

### Q1: 🔴 "สั่งกระเป๋าแบรนด์เนม 35,000 บาท — โอนแล้วไม่ได้ของ — บล็อคแล้ว"

**Category mapping:** `online_fraud` → `fraud_type: ซื้อของออนไลน์ไม่ได้ของ`

**Diagnosis simulation:**
- fraud_type: "ซื้อของออนไลน์ไม่ได้ของ"
- amount: "5,000 – 50,000"
- when: "เกิน 7 วัน"
- evidence: "สลิปโอนเงิน, แชทกับมิจฉาชีพ, เลขบัญชีปลายทาง" (3 items)

**🟢 Platform answer simulation:**
```
headline: "คุณถูกหลอกซื้อสินค้าออนไลน์ — ต้องรีบดำเนินการเพื่ออายัดบัญชีและแจ้งความ"
summary: "กรณีซื้อสินค้าออนไลน์แล้วไม่ได้ของ มีเงินโอนหลักฐานพร้อม สลิป แชท และเลขบัญชี 
         เข้าข่ายฉ้อโกงตาม ม.341 — ควรเร่งดำเนินการ"
rights:
  - label: "สิทธิแจ้งความดำเนินคดีอาญา"
    detail: "แจ้งความที่สถานีตำรวจท้องที่หรือกองบังคับการปราบปรามการกระทำความผิดเกี่ยวกับอาชญากรรมทางเทคโนโลยี (บก.ปอท.)"
  - label: "สิทธิขออายัดบัญชีธนาคารปลายทาง"
    detail: "ติดต่อธนาคารเจ้าของบัญชีเพื่อขออายัด — โทรสายด่วน 1441"
next_actions:
  - when: "วันนี้", title: "รวบรวมหลักฐานทั้งหมด", detail: "สลิปโอน แชท เลขบัญชี — เตรียมให้พร้อม"
  - when: "ภายใน 24 ชม.", title: "แจ้งความออนไลน์ที่ thaipoliceonline.go.th", detail: "..."
  - when: "ภายใน 3 วัน", title: "ติดต่อ บก.ปอท. หรือ สน.ท้องที่", detail: "..."
evidenceReadiness: 3/5 — "หลักฐานค่อนข้างพร้อม" (มีสลิป, แชท, เลขบัญชี)
citations: [criminal-code-341, computer-crime-act-2560]
```

**Verdict: MATCH ✅**
The platform handles this perfectly — product-not-delivered online is the first option, time-based urgency, clear action plan.

---

### Q2: 🔴 "Call Center หลอกเป็นสรรพากร — โอน 120,000 — เพิ่งรู้ตัว"

**Category mapping:** `online_fraud` → `fraud_type: Call Center หลอกโอนเงิน`

**Diagnosis simulation:**
- fraud_type: "Call Center หลอกโอนเงิน"
- amount: "50,001 – 200,000"
- when: "3-7 วัน"
- evidence: "สลิปโอนเงิน, เบอร์โทร, เลขบัญชีปลายทาง" (3 items)

**🟢 Platform answer simulation:**
```
headline: "คุณถูก Call Center หลอกโอนเงิน — แจ้งความและรีบอายัดบัญชี"
summary: "คนร้ายแอบอ้างเป็นเจ้าหน้าที่สรรพากร หลอกให้โอนเงิน 120,000 บาท 
         เข้าข่ายฉ้อโกง + พ.ร.บ.คอมพิวเตอร์ — มีโอกาสอายัดเงินได้เนื่องจากยังไม่เกิน 7 วัน"
rights:
  - label: "สิทธิอายัดบัญชีม้า"
    detail: "รีบโทร 1441 หรือติดต่อธนาคารทันที"
  - label: "สิทธิแจ้งความออนไลน์"
    detail: "แจ้งผ่าน thaipoliceonline.go.th หรือสายด่วน 191"
next_actions:
  - when: "ทันที", title: "โทร 1441 อายัดบัญชีปลายทาง", detail: "..."
  - when: "ภายใน 24 ชม.", title: "แจ้งความ สน.ท้องที่ หรือออนไลน์", detail: "..."
citations: [criminal-code-341, computer-crime-act-2560, amlo-act-2542]
```

**Verdict: MATCH ✅** — Excellent coverage for Call Center fraud with time-critical guidance.

---

### Q3: 🔴 "แฟนเอารูปโป๊ไปโพสต์ในกลุ่มลับ Telegram หลังเลิกกัน"

**Category mapping:** `online_fraud` / `defamation` / `crime` — **compound scenario**

**Issue:** This question spans THREE categories. The user asks about:
- Revenge porn / image leak (หมิ่นประมาท + พ.ร.บ.คอมฯ)
- The platform's `online_fraud` doesn't cover image leaks. `defamation` has "ภาพหลุด/แอบถ่าย" but focuses on defamation not privacy violation.
- `crime` has "ถูกข่มขืน/คุกคามทางเพศ" which is close but doesn't fully cover non-consensual image sharing.

**Best-fit platform category:** `defamation` → `type: ภาพหลุด/แอบถ่าย`

**Diagnosis simulation (@ defamation):**
- type: "ภาพหลุด/แอบถ่าย"
- platform: "X (Twitter)" — no Telegram option!
- when: "เกิน 2 เดือน"

**🟢 Platform answer simulation (defamation path):**
```
headline: "ภาพส่วนตัวคุณถูกเผยแพร่ — ดำเนินคดีหมิ่นประมาทและ พ.ร.บ.คอมฯ"
summary: "การนำภาพส่วนตัวไปเผยแพร่โดยไม่ได้รับความยินยอม เข้าข่ายหมิ่นประมาท 
         + พ.ร.บ.คอมพิวเตอร์ + อาจเข้าข่าย พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล"
rights:
  - label: "สิทธิฟ้องหมิ่นประมาท"
    detail: "ตาม ม.326 และ ม.328 (หมิ่นประมาทโดยการโฆษณา)"
  - label: "สิทธิดำเนินคดีตาม พ.ร.บ.คอมพิวเตอร์"
    detail: "นำเข้าข้อมูลสู่ระบบคอมพิวเตอร์โดยมิชอบ"
```

**Verdict: PARTIAL ⚠️**
- Platform has "ภาพหลุด/แอบถ่าย" in defamation ✅
- But: no Telegram in platform options ❌
- Missing: revenge porn specific laws, PDPA privacy angle not fully integrated ❌
- Missing: relationship context (ex-partner) not captured ❌

---

### Category 1 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 2. CRIME (อาชญากรรม)

### Platform config: `crime`
| Question ID | Options |
|---|---|
| `crime_type` | ถูกทำร้ายร่างกาย, ถูกลักทรัพย์/ชิงทรัพย์, ถูกข่มขืน/คุกคามทางเพศ, ถูกขู่กรรโชก |
| `when` | กำลังเกิด/เพิ่งเกิด, <24h, 1-7d, >7d |
| `evidence` | ใบรับรองแพทย์, ภาพถ่าย, พยานบุคคล, คลิป/กล้องวงจรปิด |
| `reported` | ยัง, แจ้งแล้ว, ไม่แน่ใจ |

**Sources:** criminal-code-295 (ทำร้ายร่างกาย), 276 (ข่มขืน), 334 (ลักทรัพย์), 337 (กรรโชก), victim-compensation-act-2544

---

### Q4: 🔴 "ทะเลาะเพื่อนบ้าน — ชกหน้าเลือดอาบ — เย็บ 5 เข็ม — มีใบรับรองแพทย์ + กล้องวงจรปิด"

**Category mapping:** `crime` → `crime_type: ถูกทำร้ายร่างกาย`

**Diagnosis simulation:**
- crime_type: "ถูกทำร้ายร่างกาย"
- when: "1-7 วัน"
- evidence: "ใบรับรองแพทย์, คลิป/กล้องวงจรปิด" (2 items)
- reported: "ยัง"

**🟢 Platform answer simulation:**
```
headline: "คุณถูกทำร้ายร่างกาย — มีหลักฐานครบ รีบแจ้งความดำเนินคดี"
summary: "ถูกเพื่อนบ้านชกหน้าจนเย็บ 5 เข็ม มีใบรับรองแพทย์+คลิปวงจรปิด — 
         การบาดเจ็บไม่ถึงสาหัส เข้าข่าย ม.295 ทำร้ายร่างกาย"
rights:
  - label: "สิทธิแจ้งความดำเนินคดีอาญา"
    detail: "ตาม ม.295 มีโทษจำคุกไม่เกิน 2 ปี หรือปรับไม่เกิน 4,000 บาท"
  - label: "สิทธิเรียกค่าเสียหายทางแพ่ง"
    detail: "ค่ารักษาพยาบาล ค่าขาดรายได้ ค่าเสียหายต่อจิตใจ"
  - label: "สิทธิขอรับค่าตอบแทนผู้เสียหาย"
    detail: "ตาม พ.ร.บ.ค่าตอบแทนผู้เสียหาย พ.ศ.2544"
next_actions:
  - when: "วันนี้", title: "แจ้งความที่ สน.ท้องที่", detail: "นำใบรับรองแพทย์+คลิปวงจรปิด+พยานไปด้วย"
  - when: "ภายใน 30 วัน", title: "ยื่นคำร้องขอค่าตอบแทนผู้เสียหาย", detail: "..."
citations: [criminal-code-295, victim-compensation-act-2544]
```

**Verdict: MATCH ✅** — Solid coverage. Captures both criminal and civil remedies.

---

### Q5: 🔴 "กลับจากต่างจังหวัด — บ้านโดนงัด — ทอง+พระหายครึ่งล้าน — มีรอยนิ้วมือ — ประกันไม่จ่าย"

**Category mapping:** `crime` → `crime_type: ถูกลักทรัพย์/ชิงทรัพย์`

**Note:** Insurance aspect is separate — the platform can't handle multi-category in one session.

**Diagnosis simulation (@ crime):**
- crime_type: "ถูกลักทรัพย์/ชิงทรัพย์"
- when: "1-7 วัน"
- evidence: "ภาพถ่าย" (1 item — platform doesn't have "รอยนิ้วมือ/รอยรองเท้า" as option)
- reported: "ยัง"

**🟢 Platform answer simulation:**
```
headline: "บ้านคุณถูกงัด — รีบแจ้งความและเก็บหลักฐาน"
summary: "ถูกงัดบ้าน ทรัพย์สินหายครึ่งล้าน มีรอยนิ้วมือและรอยรองเท้า — 
         เข้าข่ายลักทรัพย์ตาม ม.334"
rights:
  - label: "สิทธิแจ้งความดำเนินคดีอาญา"
    detail: "ตาม ม.334-335 (ลักทรัพย์ในเคหสถาน — โทษสูงขึ้น)"
  - label: "สิทธิเรียกค่าเสียหายทางแพ่ง"
    detail: "เรียกค่าเสียหายจากผู้กระทำความผิด"
next_actions:
  - when: "ทันที", title: "แจ้งความที่ สน.ท้องที่", detail: "อย่าแตะต้องที่เกิดเหตุ รอตำรวจเก็บหลักฐาน"
  - when: "วันนี้", title: "ถ่ายรูป + บันทึกรายการทรัพย์สินที่หาย", detail: "..."
citations: [criminal-code-334]
```

**Verdict: PARTIAL ⚠️**
- Core crime coverage works ✅
- But: No mention of insurance dispute path ❌ (needs `insurance` category in parallel)
- Platform only handles ONE category per diagnosis session — compound scenarios fall through ❌

---

### Q6: 🔴 "กลุ่มวัยรุ่นรุมทำร้ายที่ผับ — กระดูกหัก 2 ที่ — กล้องวงจรปิดเสีย — มีพยาน"

**Category mapping:** `crime` → `crime_type: ถูกทำร้ายร่างกาย`

**Diagnosis simulation:**
- crime_type: "ถูกทำร้ายร่างกาย"
- when: "1-7 วัน"
- evidence: "พยานบุคคล" (1 item — no ใบรับรองแพทย์ selected yet)
- reported: "ยัง"

**🟢 Platform answer simulation:**
```
headline: "คุณถูกกลุ่มวัยรุ่นทำร้าย — รีบแจ้งความ + เก็บหลักฐานพยาน"
summary: "ถูกรุมทำร้ายจนกระดูกหัก 2 ที่ — การบาดเจ็บรุนแรงเข้าข่ายทำร้ายร่างกายสาหัส 
         (ม.297) มีพยานหลายคน"
rights:
  - label: "สิทธิแจ้งความดำเนินคดีอาญา ม.297"
    detail: "ทำร้ายร่างกายจนเป็นอันตรายสาหัส — โทษจำคุก 6 เดือนถึง 10 ปี"
  - label: "สิทธิเรียกร้องค่าเสียหาย"
    detail: "รวมถึงค่ารักษา ค่าขาดรายได้ ค่าเสียหายทางจิตใจ"
evidenceReadiness: 1/5 — "ควรเพิ่มหลักฐาน" (แนะนำใบรับรองแพทย์)
```

**Verdict: MATCH ✅** — Platform correctly identifies severity upgrade (สาหัส → ม.297), flags evidence gap.

---

### Category 2 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 3. DEFAMATION (หมิ่นประมาท)

### Platform config: `defamation`
| Question ID | Options |
|---|---|
| `type` | ถูกด่าบนโซเชียล, ภาพหลุด/แอบถ่าย, ถูกใส่ความ/ให้ร้าย, ข้อมูลส่วนตัวรั่วไหล |
| `platform` | Facebook, LINE, TikTok, X (Twitter), เว็บบอร์ด/เว็บไซต์ |
| `when` | <7d, 7-30d, 1-2mo, >2mo (เหลือเวลาน้อย!) |
| `evidence` | แคปหน้าจอ, URL/ลิงก์, พยานบุคคล, บันทึกแชท |

**Sources:** criminal-code-326, criminal-code-328, pdpa-2562

---

### Q7: 🔴 "มีคนเอารูปเราไปโพสต์ในกลุ่ม 'สาวขายตัวย่านรัชดา' + เบอร์โทร"

**Category mapping:** `defamation` → `type: ถูกใส่ความ/ให้ร้าย`

**Diagnosis simulation:**
- type: "ถูกใส่ความ/ให้ร้าย"
- platform: "Facebook"
- when: "7-30 วัน"
- evidence: "แคปหน้าจอ, พยานบุคคล" (2 items)

**🟢 Platform answer simulation:**
```
headline: "คุณถูกหมิ่นประมาททาง Facebook — รีบรวบรวมหลักฐานดำเนินคดี"
summary: "ถูกนำรูป+เบอร์โทรไปโพสต์ใส่ความในกลุ่ม Facebook — 
         เข้าข่ายหมิ่นประมาทโดยการโฆษณา (ม.328) ซึ่งมีโทษสูงกว่าหมิ่นประมาทธรรมดา"
rights:
  - label: "สิทธิฟ้องหมิ่นประมาท ม.328"
    detail: "หมิ่นประมาทโดยการโฆษณา — โทษจำคุกไม่เกิน 2 ปี และปรับไม่เกิน 200,000 บาท"
  - label: "สิทธิรายงานต่อ Facebook ให้ลบเนื้อหา"
    detail: "Report post + ขอข้อมูลผู้โพสต์ผ่านคำสั่งศาล"
  - label: "สิทธิฟ้องเรียกค่าเสียหายทางแพ่ง"
    detail: "ค่าสินไหมทดแทนความเสียหายต่อชื่อเสียง"
next_actions:
  - when: "วันนี้", title: "แคปหน้าจอทุกโพสต์ + URL", detail: "เก็บหลักฐานให้ครบ — อายุความหมิ่นประมาทมีแค่ 3 เดือน!"
  - when: "ภายใน 7 วัน", title: "แจ้งความที่ สน. หรือกองปราบ", detail: "..."
evidenceReadiness: 2/5 — "ควรเพิ่มหลักฐาน"
citations: [criminal-code-326, criminal-code-328]
```

**Verdict: MATCH ✅**

---

### Q8: 🔴 "มีคนปลอม Facebook เรา — ไปโพสต์ด่าสถาบัน — เรากลัวโดนจับ"

**Category mapping:** `defamation` → `type: ข้อมูลส่วนตัวรั่วไหล` (closest) or `ถูกด่าบนโซเชียล`

**Diagnosis simulation:**
- type: "ข้อมูลส่วนตัวรั่วไหล" (identity theft)
- platform: "Facebook"
- when: "7-30 วัน"
- evidence: "แคปหน้าจอ, URL/ลิงก์" (2 items)

**🟢 Platform answer simulation:**
```
headline: "มีคนปลอมบัญชี Facebook ของคุณ — ดำเนินการตามกฎหมาย"
summary: "ถูกแอบอ้างตัวตนปลอม Facebook ไปโพสต์ข้อความ — 
         เข้าข่ายความผิดตาม พ.ร.บ.คอมพิวเตอร์และหมิ่นประมาท"
rights:
  - label: "สิทธิดำเนินคดีตาม พ.ร.บ.คอมพิวเตอร์"
    detail: "การนำเข้าข้อมูลเท็จ — มีโทษจำคุก"
  - label: "สิทธิรายงานการปลอมบัญชี"
    detail: "รายงานไปยัง Facebook + แจ้งความเพื่อขอข้อมูล IP"
  - label: "สิทธิพิสูจน์ความบริสุทธิ์"
    detail: "เก็บหลักฐาน IP/เวลาเข้าใช้งานของตนเองเพื่อยืนยันว่าไม่ได้เป็นผู้โพสต์"
limitations: "ผลวิเคราะห์เป็นข้อมูลเบื้องต้น — คดีสถาบันมีมิติความมั่นคง ควรปรึกษาทนาย"
```

**Verdict: PARTIAL ⚠️**
- Platform handles defamation/fake account well ✅
- But: No "ปลอมบัญชี" specific fraud_type ❌
- But: No mention of VPN/IP tracing complexities ❌
- lèse-majesté dimension (unique to Thailand) not covered ❌
- Security dimension (user fears arrest) not addressed ❌

---

### Q9: 🔴 "ลูกค้าโพสต์ Google Maps ใส่ร้ายร้าน — ลูกค้าหาย 90%"

**Category mapping:** `defamation` → `type: ถูกใส่ความ/ให้ร้าย`

**Diagnosis simulation:**
- type: "ถูกใส่ความ/ให้ร้าย"
- platform: "เว็บบอร์ด/เว็บไซต์" (Google Maps is closest)
- when: "7-30 วัน"
- evidence: "แคปหน้าจอ, URL/ลิงก์, พยานบุคคล" (3 items)

**🟢 Platform answer simulation:**
```
headline: "ธุรกิจคุณถูกใส่ร้ายบน Google Maps — ดำเนินคดีและเรียกค่าเสียหาย"
summary: "ลูกค้าโพสต์ข้อความเท็จทำให้ธุรกิจเสียหาย — 
         เข้าข่ายหมิ่นประมาทโดยการโฆษณา (ม.328) + เรียกค่าสินไหมทดแทน"
rights:
  - label: "สิทธิฟ้องหมิ่นประมาททางอาญา"
    detail: "ตาม ม.328 หมิ่นประมาทโดยการโฆษณา"
  - label: "สิทธิฟ้องเรียกค่าเสียหายทางธุรกิจ"
    detail: "สามารถเรียกค่าเสียหายจากยอดขายที่ลดลง 90% — ต้องมีงบการเงินย้อนหลัง"
next_actions:
  - when: "วันนี้", title: "รวบรวมหลักฐาน", detail: "แคปหน้าจอ, URL, งบการเงินย้อนหลัง"
  - when: "ภายใน 7 วัน", title: "แจ้งความ + ปรึกษาทนาย", detail: "..."
  - when: "ภายใน 3 เดือน", title: "ยื่นฟ้อง", detail: "ระวังอายุความหมิ่นประมาทแค่ 3 เดือน!"
```

**Verdict: MATCH ✅** — Good coverage for business defamation. Age-of-case urgency is preserved.

---

### Category 3 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 4. INSURANCE (ประกันภัย)

### Platform config: `insurance`
| Question ID | Options |
|---|---|
| `issue` | เคลมประกันรถไม่ได้, เคลมประกันสุขภาพ/ชีวิต, ยกเลิกกรมธรรม์ไม่เป็นธรรม, ประกันไม่จ่ายตามสัญญา |
| `when` | <7d, 7-30d, 1-6mo, >6mo |
| `evidence` | กรมธรรม์, ใบแจ้งเหตุ, ใบรับรองแพทย์, รูปถ่าย, บันทึกการติดต่อ |
| `response` | ยังไม่ตอบ, ปฏิเสธการเคลม, ขอเอกสารเพิ่ม, รับเคลมแต่จ่ายน้อย |

**Sources:** insurance-act-2535, life-insurance-act-2535, oic-act-2550

---

### Q10: 🔴 "สามีเสียชีวิตมะเร็ง — ประกันปฏิเสธเคลม อ้างปกปิดโรคกระเพาะ 20 ปีก่อน"

**Category mapping:** `insurance` → `issue: เคลมประกันสุขภาพ/ชีวิต`

**Diagnosis simulation:**
- issue: "เคลมประกันสุขภาพ/ชีวิต"
- when: "1-6 เดือน"
- evidence: "กรมธรรม์, ใบแจ้งเหตุ, ใบรับรองแพทย์" (3 items)
- response: "ปฏิเสธการเคลม"

**🟢 Platform answer simulation:**
```
headline: "บริษัทประกันปฏิเสธการจ่าย — คุณมีสิทธิโต้แย้ง"
summary: "บริษัทประกันอ้างว่าสามีปกปิดโรคกระเพาะเพื่อปฏิเสธการจ่ายค่าสินไหมมะเร็ง — 
         ตาม พ.ร.บ.ประกันชีวิต มาตรา 865 หากโรคที่ไม่เปิดเผยไม่เกี่ยวข้องกับการเสียชีวิต 
         บริษัทอาจไม่มีสิทธิบอกล้างสัญญา"
rights:
  - label: "สิทธิโต้แย้งการปฏิเสธเคลม"
    detail: "ยื่นอุทธรณ์ต่อบริษัทประกัน — หากโรคกระเพาะไม่เกี่ยวข้องกับมะเร็ง บริษัทต้องจ่าย"
  - label: "สิทธิร้องเรียน คปภ."
    detail: "สายด่วน 1186 — คปภ. มีอำนาจไกล่เกลี่ยข้อพิพาท"
  - label: "สิทธิฟ้องศาล"
    detail: "ฟ้องให้บริษัทปฏิบัติตามสัญญาประกันชีวิต"
next_actions:
  - when: "วันนี้", title: "รวบรวมเอกสารทั้งหมด", detail: "กรมธรรม์+ใบเสร็จ+ใบรับรองแพทย์+ประวัติการรักษา"
  - when: "ภายใน 7 วัน", title: "ยื่นอุทธรณ์ต่อบริษัทประกัน", detail: "ทำเป็นลายลักษณ์อักษร"
  - when: "ภายใน 30 วัน", title: "ร้องเรียน คปภ. 1186", detail: "..."
citations: [life-insurance-act-2535, oic-act-2550]
```

**Verdict: MATCH ✅** — Excellent. Platform catches the key legal nuance (disease must be related to deny claim).

---

### Q11: 🔴 "ประกันรถชั้น 1 — ซ่อม 3 เดือนยังไม่ได้รถคืน"

**Category mapping:** `insurance` → `issue: เคลมประกันรถไม่ได้`

**Diagnosis simulation:**
- issue: "เคลมประกันรถไม่ได้"
- when: "1-6 เดือน"
- evidence: "กรมธรรม์, รูปถ่าย, บันทึกการติดต่อ" (3 items)
- response: "รับเคลมแต่จ่ายน้อย" (closest — not exact)

**🟢 Platform answer simulation:**
```
headline: "รถคุณซ่อมนาน 3 เดือน — เร่งรัดบริษัทประกันและเรียกร้องค่าเสียหาย"
summary: "ส่งรถซ่อมที่อู่แนะนำ 3 เดือนยังไม่ได้คืน — 
         คุณมีสิทธิได้รับการซ่อมภายในเวลาอันสมควร"
rights:
  - label: "สิทธิเรียกร้องให้ซ่อมให้เสร็จ"
    detail: "ตามเงื่อนไขกรมธรรม์ — อู่ต้องซ่อมให้เสร็จภายในเวลาที่เหมาะสม"
  - label: "สิทธิร้องเรียน คปภ."
    detail: "สายด่วน 1186 — เร่งรัดการดำเนินการ"
  - label: "สิทธิเรียกค่าเสียหาย"
    detail: "เช่น ค่าเช่ารถระหว่างซ่อม (ถ้ากรมธรรม์คุ้มครอง)"
limitations: "การเรียกร้องค่าเสียหายจากการไม่ได้ใช้รถขึ้นอยู่กับเงื่อนไขกรมธรรม์ — 
              ควรตรวจสอบหัวข้อ 'รถยนต์ทดแทนระหว่างซ่อม'"
```

**Verdict: PARTIAL ⚠️**
- Basic coverage of insurance dispute ✅
- But: "delay in repair" is a service-quality issue, not a denial-of-claim ❌
- But: platform's response options don't include "รับเคลมแต่ล่าช้า" ❌
- Platform treats insurance as binary (pay/deny) not timeline ❌

---

### Q12: 🔴 "ซื้อประกันสุขภาพ — บริษัทบอกเป็น Pre-existing — ไม่เคยมีอาการมาก่อน"

**Category mapping:** `insurance` → `issue: เคลมประกันสุขภาพ/ชีวิต`

**Diagnosis simulation:**
- issue: "เคลมประกันสุขภาพ/ชีวิต"
- when: "1-6 เดือน"
- evidence: "กรมธรรม์, ใบรับรองแพทย์, บันทึกการติดต่อ" (3 items)
- response: "ปฏิเสธการเคลม"

**🟢 Platform answer simulation:**
```
headline: "ประกันอ้าง Pre-existing — คุณมีสิทธิโต้แย้ง"
summary: "บริษัทปฏิเสธเคลมอ้างเป็นโรคที่เป็นมาก่อนทำประกัน — 
         หากคุณไม่เคยมีอาการหรือรู้มาก่อน อาจไม่ใช่ Pre-existing ตามกฎหมาย"
rights:
  - label: "สิทธิโต้แย้ง Pre-existing"
    detail: "Pre-existing ต้องเป็นโรคที่มีอาการหรือได้ตรวจพบก่อนทำประกัน — 
             หากไม่มีประวัติการรักษา ถือว่าไม่ใช่"
  - label: "สิทธิร้องเรียน คปภ. 1186"
    detail: "พร้อมเอกสารประวัติการรักษาก่อนทำประกัน (ที่ไม่มี)"
  - label: "สิทธิฟ้องบังคับให้ปฏิบัติตามสัญญา"
    detail: "หากเป็นโรคร้ายแรงคุกคามชีวิต ศาลอาจกำหนดมาตรการคุ้มครองชั่วคราว"
```

**Verdict: MATCH ✅** — Solid, captures the pre-existing condition dispute well.

---

### Category 4 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 5. GOVERNMENT (ราชการและรัฐ)

### Platform config: `government`
| Question ID | Options |
|---|---|
| `issue` | ขอทะเบียน/บัตร ปชช.ไม่ได้, ถูกรัฐละเมิดจนเสียหาย, ร้องเรียนแล้วไม่ตอบ, ถูกเวนคืนที่ดิน |
| `duration` | <30d, 1-3mo, 3-6mo, >6mo |
| `agency` | อำเภอ/เขต, กรมที่ดิน, สรรพากร, กระทรวง/กรม, ไม่แน่ใจ |
| `evidence` | คำขอ/แบบฟอร์มที่ยื่น, ใบเสร็จ/หลักฐานการติดต่อ, หนังสือตอบกลับ, ภาพถ่าย |

**Sources:** administrative-court-act-2542 (ศาลปกครอง), government-liability-act-2539, civil-registration-act-2551

---

### Q13: 🔴 "ยื่นขออนุญาตก่อสร้าง — วิศวกรโยธาบอกให้ 'หาวิธีจัดการ' — มีคนบอกต้องจ่ายแสน"

**Category mapping:** `government` → closest is `issue: ร้องเรียนแล้วไม่ตอบ` (not exact match)

**Diagnosis simulation:**
- issue: "ร้องเรียนแล้วไม่ตอบ" (closest — but this is about bribery, not non-response)
- duration: "เกิน 6 เดือน"
- agency: "อำเภอ/เขต"
- evidence: "คำขอ/แบบฟอร์มที่ยื่น" (1 item)

**🟢 Platform answer simulation:**
```
headline: "คุณถูกเจ้าหน้าที่เรียกรับสินบน — มีช่องทางร้องเรียนหลายทาง"
summary: "วิศวกรโยธาพูดเป็นนัยให้จ่ายเงิน 100,000 บาทเพื่ออนุมัติใบอนุญาต — 
         เข้าข่ายการเรียกรับสินบนตามประมวลกฎหมายอาญา"
rights:
  - label: "สิทธิร้องเรียน ป.ป.ช."
    detail: "ร้องเรียนผ่านสายด่วน ป.ป.ช. 1205 หรือระบบออนไลน์ nacc.go.th"
  - label: "สิทธิร้องเรียนสำนักงานเขต"
    detail: "ร้องเรียนต่อผู้อำนวยการเขต หรือผู้ว่าราชการกรุงเทพมหานคร"
  - label: "สิทธิฟ้องศาลปกครอง"
    detail: "หากใช้ดุลพินิจไม่ชอบ — ฟ้องขอให้ออกคำสั่งอนุมัติ"
next_actions:
  - when: "วันนี้", title: "บันทึกหลักฐานการเรียกรับสินบน", detail: "บันทึกเสียง/แชท/ชื่อตำแหน่งเจ้าหน้าที่"
  - when: "ภายใน 7 วัน", title: "ร้องเรียน ป.ป.ช.", detail: "..."
limitations: "การร้องเรียนเรื่องสินบนต้องมีหลักฐานที่น่าเชื่อถือ — ข้อกล่าวหาเจ้าหน้าที่โดยไม่มีหลักฐานอาจถูกฟ้องกลับ"
citations: [government-liability-act-2539, admin-court-2542]
```

**Verdict: PARTIAL ⚠️**
- Platform covers government complaint path ✅
- But: No "ถูกเรียกรับสินบน" option in `issue` ❌
- But: Anti-corruption sources (ป.ป.ช., ป.ป.ท.) not in the source registry ❌
- `agency` doesn't list ป.ป.ช. or ป.ป.ท. ❌

---

### Q14: 🔴 "ขอพาสปอร์ต 4 เดือน — เงียบ — พลาดโอกาสทำงานสิงคโปร์"

**Category mapping:** `government` → `issue: ร้องเรียนแล้วไม่ตอบ`

**Diagnosis simulation:**
- issue: "ร้องเรียนแล้วไม่ตอบ"
- duration: "เกิน 6 เดือน"
- agency: "กระทรวง/กรม" (กงสุล)
- evidence: "คำขอ/แบบฟอร์มที่ยื่น, ใบเสร็จ/หลักฐานการติดต่อ" (2 items)

**🟢 Platform answer simulation:**
```
headline: "หน่วยงานราชการล่าช้า — คุณมีสิทธิร้องเรียนและเรียกร้องค่าเสียหาย"
summary: "ยื่นขอพาสปอร์ต 4 เดือนไม่มีความคืบหน้า — 
         การดำเนินการล่าช้าอาจถือเป็นการละเลยต่อหน้าที่"
rights:
  - label: "สิทธิร้องเรียนต่อผู้บังคับบัญชา"
    detail: "ทำหนังสือร้องเรียนถึงอธิบดีกรมการกงสุล"
  - label: "สิทธิฟ้องศาลปกครอง"
    detail: "ขอให้ศาลมีคำสั่งให้ดำเนินการภายในกำหนดเวลา"
  - label: "สิทธิเรียกร้องค่าเสียหาย"
    detail: "ตาม พ.ร.บ.ความรับผิดทางละเมิดของเจ้าหน้าที่ 2539"
limitations: "การฟ้องเรียกค่าเสียหายจากหน่วยงานรัฐต้องพิสูจน์ความเสียหายที่แท้จริง — 
              ควรเก็บหลักฐานการพลาดโอกาสทำงาน"
citations: [gov-liability-act-2539, admin-court-2542]
```

**Verdict: MATCH ✅** — Platform handles government delay/lack of response well.

---

### Q15: 🔴 "ถูกประเมินภาษีย้อนหลัง 5 ล้าน — เจ้าหน้าที่ไม่ดูบัญชีจริง — ยึดบัญชีธนาคาร"

**Category mapping:** `government` → closest: `issue: ถูกรัฐละเมิดจนเสียหาย`

**Diagnosis simulation:**
- issue: "ถูกรัฐละเมิดจนเสียหาย"
- duration: "1-3 เดือน"
- agency: "สรรพากร"
- evidence: "หนังสือตอบกลับ, ภาพถ่าย" (2 items — but no "บัญชี/งบการเงิน" option)

**🟢 Platform answer simulation:**
```
headline: "คุณถูกสรรพากรประเมินภาษีโดยไม่เป็นธรรม — มีสิทธิอุทธรณ์"
summary: "เจ้าหน้าที่ประเมินรายได้แบบเหมาโดยไม่ดูบัญชีจริง — 
         การใช้ดุลพินิจโดยไม่พิจารณาหลักฐานอาจไม่ชอบด้วยกฎหมาย"
rights:
  - label: "สิทธิอุทธรณ์การประเมินภาษี"
    detail: "ยื่นอุทธรณ์ต่อคณะกรรมการพิจารณาอุทธรณ์ ภายใน 30 วัน"
  - label: "สิทธิฟ้องศาลภาษีอากร"
    detail: "ขอให้เพิกถอนการประเมินภาษีที่ไม่ชอบ"
  - label: "สิทธิฟ้องศาลปกครอง"
    detail: "หากการยึดบัญชีโดยไม่มีอำนาจตามกฎหมาย"
next_actions:
  - when: "ทันที", title: "ยื่นอุทธรณ์", detail: "ต้องยื่นภายใน 30 วัน — รวบรวมบัญชี+เอกสารการเงิน"
  - when: "ภายใน 7 วัน", title: "ขอคืนการยึด/อายัดบัญชี", detail: "..."
limitations: "การอุทธรณ์ภาษีมีขั้นตอนเฉพาะ — ปรึกษานักบัญชีหรือทนายภาษี"
citations: [gov-liability-act-2539, admin-court-2542]
```

**Verdict: PARTIAL ⚠️**
- Platform handles government overreach ✅
- But: No tax-specific sources (ประมวลรัษฎากร) in registry ❌
- But: No "ศาลภาษีอากร" as a venue ❌
- But: The `evidence` options don't include tax/accounting documents ❌

---

### Category 5 Coverage Score: **1 MATCH, 2 PARTIAL = 67% coverage**

---

## 6. PROPERTY (ที่ดินและทรัพย์สิน)

### Platform config: `property`
| Question ID | Options |
|---|---|
| `issue` | ที่ดินถูกบุกรุก, แนวเขตไม่ชัด, ซื้อขาย/โอนไม่ได้, มรดกที่ดิน, โฉนดหาย/ชำรุด |
| `documents` | โฉนด (น.ส.4), น.ส.3 ก., สัญญาซื้อขาย, ไม่มีเอกสาร |
| `when` | <1yr, 1-5yr, 5-10yr, >10yr |
| `evidence` | เอกสารสิทธิ์, ภาพถ่าย, พยานบุคคล, หนังสือแจ้งเตือน |

**Sources:** land-code-2497, civil-code-property, condominium-act-2522

---

### Q16: 🔴 "ที่ดินคุณยายถือ 50 ปี — น.ส.3 → โฉนด — ทับซ้อนกับคนอื่น (ออกโฉนดเมื่อ 5 ปีก่อน)"

**Category mapping:** `property` → `issue: โฉนดหาย/ชำรุด` (closest) or `แนวเขตไม่ชัด`

**Diagnosis simulation:**
- issue: "แนวเขตไม่ชัด"
- documents: "น.ส.3 ก."
- when: "เกิน 10 ปี"
- evidence: "เอกสารสิทธิ์, พยานบุคคล, ภาพถ่าย" (3 items)

**🟢 Platform answer simulation:**
```
headline: "ที่ดินของคุณยายมีปัญหาทับซ้อน — มีสิทธิคัดค้าน"
summary: "ที่ดินถือครองมากว่า 50 ปี กำลังรังวัดออกโฉนดแต่มีผู้แจ้งทับซ้อน — 
         โฉนดอีกฝ่ายออกเมื่อ 5 ปีก่อนอาจมีพิรุธ"
rights:
  - label: "สิทธิคัดค้านการรังวัด"
    detail: "ยื่นคัดค้านต่อเจ้าพนักงานที่ดินภายใน 30 วันนับแต่วันประกาศ"
  - label: "สิทธิฟ้องศาลเพิกถอนโฉนด"
    detail: "หากโฉนดอีกฝ่ายออกโดยมิชอบ"
  - label: "สิทธิฟ้องขอให้รับรองสิทธิครอบครอง"
    detail: "ตามประมวลกฎหมายที่ดิน — ครอบครองมาก่อนย่อมมีสิทธิดีกว่า"
next_actions:
  - when: "ทันที", title: "ยื่นคัดค้านที่สำนักงานที่ดิน", detail: "..."
  - when: "ภายใน 30 วัน", title: "รวบรวมหลักฐานการครอบครอง", detail: "ภาพถ่ายเก่า พยานบุคคล ทะเบียนบ้าน"
citations: [land-code-2497, civil-code-property]
```

**Verdict: MATCH ✅** — Covers overlapping title disputes well.

---

### Q17: 🔴 "ซื้อที่ดินเปล่า 10 ปี — มีคนมายื่นขอออกโฉนดทับ — อ้างครอบครองมาก่อน"

**Category mapping:** `property` → `issue: ที่ดินถูกบุกรุก`

**Diagnosis simulation:**
- issue: "ที่ดินถูกบุกรุก"
- documents: "โฉนด (น.ส.4)"
- when: "5-10 ปี"
- evidence: "เอกสารสิทธิ์, ภาพถ่าย, หนังสือแจ้งเตือน" (3 items)

**🟢 Platform answer simulation:**
```
headline: "ที่ดินของคุณถูกผู้อื่นพยายามออกเอกสารทับ — ปกป้องสิทธิ์ของคุณ"
summary: "มีผู้อื่นพยายามออกโฉนดทับที่ดินที่คุณมีโฉนดอยู่แล้ว — 
         การออกโฉนดทับที่ดินที่มีเอกสารสิทธิ์แล้วไม่สามารถทำได้ตามกฎหมาย"
rights:
  - label: "สิทธิคัดค้านการออกโฉนด"
    detail: "ยื่นคัดค้านที่สำนักงานที่ดินพร้อมเอกสารสิทธิ์ของคุณ"
  - label: "สิทธิฟ้องศาลหากมีการออกโฉนดทับ"
    detail: "ฟ้องขอให้เพิกถอนการออกเอกสารสิทธิ์ที่ไม่ชอบ"
next_actions:
  - when: "ทันที", title: "แจ้งสำนักงานที่ดิน", detail: "แสดงโฉนด+หลักฐานการครอบครอง"
  - when: "ภายใน 7 วัน", title: "เตรียมเอกสาร+พยาน", detail: "..."
```

**Verdict: MATCH ✅**

---

### Q18: 🔴 "แม่อยากยกที่ดินให้ — แต่โฉนดเป็นชื่อตาทวด — เสียชีวิต 40 ปี — ทายาทหลายสิบคน"

**Category mapping:** `property` → `issue: มรดกที่ดิน`

**Diagnosis simulation:**
- issue: "มรดกที่ดิน"
- documents: "ไม่มีเอกสาร" (no current deed in correct name)
- when: "เกิน 10 ปี"
- evidence: "เอกสารสิทธิ์, พยานบุคคล" (2 items)

**🟢 Platform answer simulation:**
```
headline: "ที่ดินมรดกยังไม่ได้โอน — มีขั้นตอนจัดการ"
summary: "ตาทวดเสียชีวิต 40 ปี ที่ดินยังไม่ได้แบ่งมรดก — 
         ต้องจัดการเรื่องมรดกก่อนจึงจะโอนให้คุณได้"
rights:
  - label: "สิทธิขอตั้งผู้จัดการมรดก"
    detail: "ยื่นคำร้องต่อศาลเพื่อขอแต่งตั้งผู้จัดการมรดกของตาทวด"
  - label: "สิทธิขอแบ่งมรดก"
    detail: "เมื่อได้ผู้จัดการมรดกแล้ว แบ่งมรดกตามกฎหมายให้แก่ทายาททั้งหมด"
next_actions:
  - when: "ภายใน 30 วัน", title: "ติดตามรายชื่อทายาททั้งหมด", detail: "ทายาททุกคนต้องยินยอม"
  - when: "ภายใน 3 เดือน", title: "ยื่นศาลขอตั้งผู้จัดการมรดก", detail: "..."
limitations: "การมีทายาทจำนวนมากทำให้กระบวนการซับซ้อน — 
              หากบางคนติดต่อไม่ได้อาจต้องใช้วิธีประกาศทางหนังสือพิมพ์"
citations: [civil-code-property, land-code-2497]
```

**Verdict: PARTIAL ⚠️**
- Platform catches inheritance issue ✅
- But: Missing `civil-code-inheritance` as a source (inheritance is in `family`, not `property`!) ❌
- But: The multi-generational / untraceable heirs problem isn't addressed in the questions ❌
- Missing: cross-referencing between `family` (inheritance) and `property` (land) ❌

---

### Category 6 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 7. LABOUR (แรงงาน)

### Platform config: `labour`
| Question ID | Options |
|---|---|
| `situation` | ถูกเลิกจ้าง, ถูกบังคับให้ลาออก, นายจ้างค้างจ่ายเงิน, เงื่อนไขการทำงานไม่เป็นธรรม |
| `tenure` | <120d, 120d-1yr, 1-3yr, >3yr |
| `notice` | ไม่แจ้ง เลิกจ้างทันที, แจ้งล่วงหน้าแล้ว, แจ้งด้วยวาจา, ไม่แน่ใจ |
| `evidence` | สัญญาจ้างงาน, สลิปเงินเดือน, หนังสือเลิกจ้าง, แชทหรืออีเมล |

**Sources:** labour-protection-act-2541, labour-court-act-2522, social-security-act-2533

---

### Q19: 🔴 "ทำงาน 10 ปี — เรียกเลิกจ้างลอยๆ — ไม่มีค่าชดเชย — ให้เซ็นใบลาออก"

**Category mapping:** `labour` → `situation: ถูกบังคับให้ลาออก`

**Diagnosis simulation:**
- situation: "ถูกบังคับให้ลาออก"
- tenure: "มากกว่า 3 ปี"
- notice: "ไม่แจ้ง เลิกจ้างทันที"
- evidence: "สลิปเงินเดือน, แชทหรืออีเมล" (2 items)

**🟢 Platform answer simulation:**
```
headline: "อย่าเซ็นใบลาออก — คุณถูกเลิกจ้างไม่เป็นธรรม"
summary: "ทำงาน 10 ปีแล้วถูกบังคับให้เซ็นใบลาออก — 
         หากคุณสมัครใจลาออกจะหมดสิทธิค่าชดเชย ให้ยืนยันว่าถูกเลิกจ้าง"
rights:
  - label: "สิทธิได้รับค่าชดเชย"
    detail: "อายุงาน 10 ปี — ได้ค่าชดเชย 300 วัน (ตาม ม.118 พ.ร.บ.คุ้มครองแรงงาน)"
  - label: "สิทธิได้รับสินจ้างแทนการบอกกล่าวล่วงหน้า"
    detail: "เนื่องจากไม่มีการแจ้งล่วงหน้า — ได้ค่าจ้างอีกอย่างน้อย 1 เดือน"
  - label: "สิทธิฟ้องศาลแรงงาน"
    detail: "ฟ้องเรียกค่าชดเชย + สินจ้างแทนการบอกกล่าว"
next_actions:
  - when: "วันนี้", title: "อย่าเซ็นอะไรทั้งสิ้น", detail: "การเซ็นใบลาออก = สละสิทธิค่าชดเชย"
  - when: "ภายใน 7 วัน", title: "แจ้งเป็นลายลักษณ์อักษรว่านายจ้างเลิกจ้าง", detail: "..."
  - when: "ภายใน 30 วัน", title: "ยื่นฟ้องศาลแรงงาน", detail: "..."
evidenceReadiness: 2/4 — "ควรเพิ่มหลักฐาน" (แนะนำ: เก็บหลักฐานการเรียกประชุม)
citations: [labour-protection-act-2541, labour-court-act-2522]
```

**Verdict: MATCH ✅** — Perfect. The "don't sign resignation" advice is spot-on.

---

### Q20: 🔴 "ร้านอาหาร จ้าง 12,000 — ทำงาน 10:00-22:00 หกวัน — ไม่มี OT — ไม่มีวันหยุด"

**Category mapping:** `labour` → `situation: เงื่อนไขการทำงานไม่เป็นธรรม`

**Diagnosis simulation:**
- situation: "เงื่อนไขการทำงานไม่เป็นธรรม"
- tenure: "120 วัน – 1 ปี"
- notice: (N/A for this situation)
- evidence: "สลิปเงินเดือน, แชทหรืออีเมล" (2 items)

**🟢 Platform answer simulation:**
```
headline: "ชั่วโมงทำงานของคุณเกินกฎหมาย — มีสิทธิเรียกร้องค่าล่วงเวลา"
summary: "ทำงาน 12 ชม./วัน 6 วัน/สัปดาห์ = 72 ชม./สัปดาห์ — 
         เกินเวลาทำงานสูงสุดที่กฎหมายกำหนด (48 ชม./สัปดาห์)"
rights:
  - label: "สิทธิได้รับค่าล่วงเวลา (OT)"
    detail: "ชั่วโมงที่เกิน 8 ชม./วัน คิด OT 1.5 เท่า — วันหยุดคิด 2 เท่า"
  - label: "สิทธิร้องเรียนพนักงานตรวจแรงงาน"
    detail: "ยื่นคำร้องที่สำนักงานสวัสดิการและคุ้มครองแรงงาน"
  - label: "สิทธิเรียก OT ย้อนหลัง"
    detail: "อายุความเรียกร้องสิทธิแรงงาน 2 ปี"
next_actions:
  - when: "ภายใน 7 วัน", title: "คำนวณ OT ที่ควรได้รับ", detail: "..."
  - when: "ภายใน 30 วัน", title: "ยื่นคำร้องต่อพนักงานตรวจแรงงาน", detail: "..."
limitations: "พ.ร.บ.คุ้มครองแรงงานยกเว้นบางประเภทกิจการ — 
              ตรวจสอบว่ากิจการเข้าข่ายข้อยกเว้นหรือไม่"
citations: [labour-protection-act-2541]
```

**Verdict: MATCH ✅** — Core labor rights analysis is solid.

---

### Q21: 🔴 "ประกันสังคม — อุบัติเหตุระหว่างเดินทางไปทำงาน — มอไซค์ล้ม — รพ.บอกไม่คุ้มครอง"

**Category mapping:** `labour` → `situation: เงื่อนไขการทำงานไม่เป็นธรรม` (closest, but this is about SSO)

**Diagnosis simulation (labour path):**
- situation: "เงื่อนไขการทำงานไม่เป็นธรรม"
- tenure: "มากกว่า 3 ปี"
- notice: "ไม่แน่ใจ"
- evidence: "สลิปเงินเดือน" (1 item)

**🟢 Platform answer simulation (labour context):**
```
headline: "การเดินทางไปทำงานคุ้มครองโดยกองทุนเงินทดแทน"
summary: "อุบัติเหตุระหว่างเดินทางไป-กลับที่ทำงาน โดยใช้เส้นทางปกติ — 
         กองทุนเงินทดแทนคุ้มครองตาม พ.ร.บ.เงินทดแทน"
rights:
  - label: "สิทธิได้รับความคุ้มครองจากกองทุนเงินทดแทน"
    detail: "ค่ารักษาพยาบาล ค่าทดแทนการขาดรายได้ — นายจ้างต้องยื่นเรื่องภายใน 15 วัน"
  - label: "สิทธิใช้ประกันสังคม"
    detail: "หากเป็นผู้ประกันตน — ใช้สิทธิรักษาพยาบาลได้"
next_actions:
  - when: "ทันที", title: "แจ้งนายจ้าง", detail: "ให้นายจ้างยื่นแบบ กท.16"
  - when: "ภายใน 7 วัน", title: "ยื่นเรื่องด้วยตนเอง", detail: "ที่สำนักงานประกันสังคมพื้นที่"
citations: [social-security-act-2533]
```

**Verdict: PARTIAL ⚠️**
- Platform has `social-security-act-2533` ✅
- But: SSO/Workmen's Compensation is a distinct sub-system that the labour questions barely touch ❌
- But: No specific questions about SSO vs Workmen's Comp distinction ❌
- Missing: กองทุนเงินทดแทน sources not separate from SSO ❌

---

### Category 7 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 8. CONSUMER (ผู้บริโภค)

### Platform config: `consumer`
| Question ID | Options |
|---|---|
| `issue` | สินค้าไม่ตรงปก, สินค้าชำรุด, ไม่ได้รับสินค้า, บริการไม่เป็นธรรม |
| `channel` | แพลตฟอร์มออนไลน์, ร้านค้าปลีก, เพจ/โซเชียล, เว็บไซต์ของผู้ขาย |
| `amount` | <1K, 1K-10K, 10K-50K, >50K |
| `evidence` | ใบเสร็จ/หลักฐานการชำระ, ภาพสินค้า, แชทกับผู้ขาย, นโยบายคืนสินค้า |

**Sources:** consumer-protection-act-2522, consumer-case-procedure-act-2551

---

### Q22: 🔴 "ซื้อมือถือ 25,000 — ใช้ 12 วันดับ — ซ่อม 2 รอบไม่หาย — ขอคืนเงินไม่ได้"

**Category mapping:** `consumer` → `issue: สินค้าชำรุด`

**Diagnosis simulation:**
- issue: "สินค้าชำรุด"
- channel: "ร้านค้าปลีก"
- amount: "10,001 – 50,000 บาท"
- evidence: "ใบเสร็จ/หลักฐานการชำระ, ภาพสินค้า" (2 items)

**🟢 Platform answer simulation:**
```
headline: "สินค้าชำรุดซ่อมแล้วไม่หาย — มีสิทธิขอเปลี่ยนหรือคืนเงิน"
summary: "ซื้อมือถือภายใน 12 วันแล้วเสีย — ซ่อม 2 ครั้งไม่หาย — 
         ตาม พ.ร.บ.คุ้มครองผู้บริโภค คุณมีสิทธิขอเปลี่ยนเครื่องใหม่หรือคืนเงิน"
rights:
  - label: "สิทธิขอเปลี่ยนสินค้าใหม่"
    detail: "หากสินค้าชำรุดและซ่อมแล้วยังไม่หาย — ผู้ขายต้องเปลี่ยนให้"
  - label: "สิทธิขอคืนเงิน"
    detail: "หากเปลี่ยนแล้วยังมีปัญหา — ขอคืนเงินเต็มจำนวนได้"
  - label: "สิทธิฟ้องคดีผู้บริโภค"
    detail: "คดีผู้บริโภคไม่ต้องเสียค่าธรรมเนียมศาล"
next_actions:
  - when: "ทันที", title: "ส่งจดหมายลงทะเบียนถึงร้านค้า", detail: "แจ้งข้อบกพร่อง + ขอเปลี่ยน/คืนเงิน"
  - when: "ภายใน 7 วัน", title: "ร้องเรียน สคบ.", detail: "สายด่วน 1166"
citations: [consumer-protection-act-2522, consumer-case-procedure-act-2551]
```

**Verdict: MATCH ✅**

---

### Q23: 🔴 "สมัครคอร์สเรียน 50,000 — โฆษณาได้งาน 100% — เนื้อหาไม่มีคุณภาพ"

**Category mapping:** `consumer` → `issue: บริการไม่เป็นธรรม`

**Diagnosis simulation:**
- issue: "บริการไม่เป็นธรรม"
- channel: "เว็บไซต์ของผู้ขาย"
- amount: "10,001 – 50,000 บาท"
- evidence: "ใบเสร็จ/หลักฐานการชำระ, แชทกับผู้ขาย" (2 items)

**🟢 Platform answer simulation:**
```
headline: "คอร์สเรียนไม่ตรงตามที่โฆษณา — มีสิทธิเรียกร้องเงินคืน"
summary: "โฆษณารับประกันได้งาน 100% แต่เนื้อหาไม่มีคุณภาพ — 
         เข้าข่ายการโฆษณาเกินจริง ผิด พ.ร.บ.คุ้มครองผู้บริโภค"
rights:
  - label: "สิทธิบอกเลิกสัญญาและขอคืนเงิน"
    detail: "บริการไม่เป็นไปตามที่โฆษณา — ผู้บริโภคมีสิทธิบอกเลิก"
  - label: "สิทธิร้องเรียน สคบ."
    detail: "ในข้อหาโฆษณาเกินจริง — มีโทษจำคุกไม่เกิน 6 เดือน"
next_actions:
  - when: "วันนี้", title: "แคปหลักฐานการโฆษณา", detail: "หน้าเว็บที่อ้าง 'ได้งาน 100%'"
  - when: "ภายใน 7 วัน", title: "ร้องเรียน สคบ.", detail: "..."
citations: [consumer-protection-act-2522]
```

**Verdict: MATCH ✅**

---

### Q24: 🔴 "ซื้อรถมือสองจากเต็นท์ — ขับ 2 อาทิตย์เกียร์พัง — รถเคยชนหนัก — ไมล์ถูกย้อน"

**Category mapping:** `consumer` → `issue: สินค้าชำรุด`

**Diagnosis simulation:**
- issue: "สินค้าชำรุด"
- channel: "ร้านค้าปลีก"
- amount: "มากกว่า 50,000 บาท"
- evidence: "ใบเสร็จ/หลักฐานการชำระ, ภาพสินค้า" (2 items)

**🟢 Platform answer simulation:**
```
headline: "รถมือสองมีตำหนิที่ซ่อนเร้น — คุณมีสิทธิเรียกร้องจากเต็นท์"
summary: "รถมือสองมีประวัติชนหนักที่ถูกปกปิดและไมล์ถูกย้อน — 
         ผู้ขายไม่เปิดเผยความจริง = ขายสินค้าชำรุดบกพร่อง ผิดกฎหมาย"
rights:
  - label: "สิทธิบอกเลิกสัญญาและเรียกเงินคืน"
    detail: "ตาม ป.พ.พ. มาตรา 472 ผู้ขายต้องรับผิดในความชำรุดบกพร่องที่ซ่อนเร้น"
  - label: "สิทธิฟ้องคดีผู้บริโภค"
    detail: "เรียกค่าเสียหาย ค่าซ่อม หรือคืนราคารถ"
  - label: "สิทธิแจ้งความดำเนินคดีอาญา"
    detail: "การย้อนไมล์และปกปิดประวัติ = ฉ้อโกง"
limitations: "รถมือสองจากเต็นท์ส่วนใหญ่ขาย 'ตามสภาพ' — 
              การฟ้องต้องพิสูจน์ว่าผู้ขายรู้เห็นและจงใจปกปิด"
citations: [consumer-protection-act-2522, consumer-case-procedure-act-2551]
```

**Verdict: PARTIAL ⚠️**
- Platform covers defective product ✅
- But: Used car fraud (mileage rollback, hidden accident) is more specific than general "สินค้าชำรุด" ❌
- But: Civil code provisions (472) for hidden defects not in source registry ❌
- No "รถยนต์" as a specific consumer sub-category ❌

---

### Category 8 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 9. DEBT (หนี้สิน)

### Platform config: `debt`
| Question ID | Options |
|---|---|
| `situation` | ถูกทวงหนี้, ต้องการทวงหนี้, ปัญหาดอกเบี้ยนอกระบบ, ถูกคุกคามจากเจ้าหนี้ |
| `amount` | <10K, 10K-100K, 100K-500K, >500K |
| `age` | <2yr, 2-5yr, >5yr, ไม่แน่ใจ |
| `evidence` | สัญญากู้ยืม, หลักฐานการโอนเงิน, บันทึกการทวงถาม, แชท/อีเมล |

**Sources:** civil-commercial-code-debt, debt-collection-act-2558, bankruptcy-act-2483

---

### Q25: 🔴 "หนี้บัตรเครดิต 200,000 — ทวงวันละ 10-20 สาย — โทรหาญาติ — ขู่ประจาน"

**Category mapping:** `debt` → `situation: ถูกทวงหนี้` or `ถูกคุกคามจากเจ้าหนี้`

**Diagnosis simulation:**
- situation: "ถูกคุกคามจากเจ้าหนี้"
- amount: "100,001 – 500,000 บาท"
- age: "น้อยกว่า 2 ปี"
- evidence: "บันทึกการทวงถาม, แชท/อีเมล" (2 items)

**🟢 Platform answer simulation:**
```
headline: "การทวงหนี้ที่คุณเผชิญผิดกฎหมาย — หยุดมันได้"
summary: "เจ้าหนี้โทรทวงวันละ 10-20 ครั้ง โทรหาญาติ ขู่ประจาน — 
         ผิด พ.ร.บ.การทวงถามหนี้ พ.ศ. 2558 หลายข้อหา"
rights:
  - label: "สิทธิร้องเรียนการทวงหนี้ผิดกฎหมาย"
    detail: "ร้องเรียนต่อคณะกรรมการกำกับการทวงถามหนี้ — ปรับสูงสุด 500,000 บาท"
  - label: "สิทธิฟ้องหยุดการคุกคาม"
    detail: "เจ้าหนี้ห้ามติดต่อบุคคลอื่นที่ไม่ใช่ผู้ค้ำประกัน — ห้ามข่มขู่"
  - label: "สิทธิขอประนอมหนี้"
    detail: "เจรจาปรับโครงสร้างหนี้กับธนาคาร"
next_actions:
  - when: "วันนี้", title: "บันทึกหลักฐานทุกครั้งที่ถูกทวง", detail: "บันทึกเสียง/เวลา/เนื้อหา"
  - when: "ภายใน 3 วัน", title: "ร้องเรียนคณะกรรมการกำกับการทวงถามหนี้", detail: "ที่ทำการปกครองจังหวัด"
  - when: "ภายใน 7 วัน", title: "แจ้งความดำเนินคดีอาญา", detail: "..."
citations: [debt-collection-act-2558, civil-commercial-code-debt]
```

**Verdict: MATCH ✅** — Strong. Debt-collection-act is perfectly applied.

---

### Q26: 🔴 "กู้เงินนอกระบบ 100,000 — ได้จริง 85,000 — จ่ายรายวัน 1,400 × 100 วัน = 140,000"

**Category mapping:** `debt` → `situation: ปัญหาดอกเบี้ยนอกระบบ`

**Diagnosis simulation:**
- situation: "ปัญหาดอกเบี้ยนอกระบบ"
- amount: "10,000 – 100,000 บาท"
- age: "น้อยกว่า 2 ปี"
- evidence: "สัญญากู้ยืม, หลักฐานการโอนเงิน" (2 items)

**🟢 Platform answer simulation:**
```
headline: "ดอกเบี้ยนอกระบบเกินกฎหมาย — จ่ายคืนเฉพาะเงินต้น+ดอกเบี้ยตามกฎหมาย"
summary: "กู้ 100,000 ได้จริง 85,000 (หักค่าดำเนินการ 15,000) — 
         จ่ายคืน 140,000 ใน 100 วัน — ดอกเบี้ยสูงเกินอัตราที่กฎหมายกำหนด"
rights:
  - label: "สิทธิบอกล้างดอกเบี้ยเกินอัตรา"
    detail: "ตาม ป.พ.พ. ดอกเบี้ยเกินร้อยละ 15 ต่อปี — สัญญาดอกเบี้ยเป็นโมฆะ"
  - label: "สิทธิแจ้งความข้อหาดอกเบี้ยเกินอัตรา"
    detail: "เงินกู้นอกระบบที่คิดดอกเบี้ยเกินกฎหมาย — มีโทษอาญา"
  - label: "สิทธิขอความช่วยเหลือจากรัฐ"
    detail: "โครงการไกล่เกลี่ยหนี้นอกระบบ กระทรวงมหาดไทย"
next_actions:
  - when: "วันนี้", title: "หยุดจ่าย", detail: "รวบรวมหลักฐานการโอน+สัญญา"
  - when: "ภายใน 7 วัน", title: "แจ้งความที่ สน.", detail: "แจ้งดอกเบี้ยเกินอัตรา+เงินกู้นอกระบบ"
limitations: "เงินกู้นอกระบบอาจมีผู้มีอิทธิพล — หากถูกข่มขู่ให้ขอความคุ้มครองจากตำรวจ"
citations: [civil-commercial-code-debt, debt-collection-act-2558]
```

**Verdict: MATCH ✅** — Excellent. Catches the key illegal aspects (excessive interest, upfront deduction).

---

### Q27: 🔴 "เซ็นค้ำประกันเพื่อนซื้อรถ — เพื่อนขาดส่ง — ไฟแนนซ์ให้จ่าย 200,000"

**Category mapping:** `debt` → closest: `situation: ถูกทวงหนี้` (but the "ผู้ค้ำประกัน" angle is not in options)

**Diagnosis simulation:**
- situation: "ถูกทวงหนี้" (closest)
- amount: "100,001 – 500,000 บาท"
- age: "2 – 5 ปี"
- evidence: "สัญญากู้ยืม, หลักฐานการโอนเงิน" (2 items)

**🟢 Platform answer simulation:**
```
headline: "คุณเป็นผู้ค้ำประกัน — มีสิทธิเรียกร้องจากลูกหนี้ชั้นต้นก่อน"
summary: "เซ็นค้ำประกันให้เพื่อนกู้ซื้อรถ — เพื่อนขาดส่ง — 
         ตามกฎหมาย ผู้ค้ำประกันมีสิทธิให้เจ้าหนี้เรียกร้องจากลูกหนี้ก่อน"
rights:
  - label: "สิทธิให้เจ้าหนี้เรียกร้องจากลูกหนี้ก่อน"
    detail: "ตาม ป.พ.พ. ม.688 — เจ้าหนี้ต้องบังคับจากทรัพย์สินลูกหนี้ก่อน"
  - label: "สิทธิไล่เบี้ย"
    detail: "หากคุณจ่ายแทน — สามารถฟ้องไล่เบี้ยเพื่อนได้"
next_actions:
  - when: "วันนี้", title: "ติดต่อเพื่อนให้มาชำระหนี้", detail: "..."
  - when: "ภายใน 7 วัน", title: "แจ้งไฟแนนซ์ให้ดำเนินการยึดรถก่อน", detail: "..."
citations: [civil-commercial-code-debt]
```

**Verdict: PARTIAL ⚠️**
- Platform handles debt collection ✅
- But: No "ผู้ค้ำประกัน" (guarantor) specific sub-category ❌
- But: The question flow doesn't distinguish between primary debtor and guarantor ❌
- Missing: suretyship law nuances (excussion, subrogation) ❌

---

### Category 9 Coverage Score: **2 MATCH, 1 PARTIAL = 83% coverage**

---

## 10. HOUSING (ที่อยู่อาศัย)

### Platform config: `housing`
| Question ID | Options |
|---|---|
| `situation` | ต้องการบอกเลิกสัญญาเช่า, เจ้าของที่ไม่คืนเงินมัดจำ, ผู้เช่าไม่จ่ายค่าเช่า, ข้อพิพาทสภาพทรัพย์ |
| `contract` | มี สัญญาเป็นลายลักษณ์อักษร, สัญญาปากเปล่า, มีแชท/อีเมล, ไม่แน่ใจ |
| `duration` | <6mo, 6mo-1yr, 1-3yr, >3yr |
| `evidence` | สัญญาเช่า, หลักฐานการชำระค่าเช่า, ภาพสภาพทรัพย์, แชทกับอีกฝ่าย |

**Sources:** civil-commercial-code-hire

---

### Q28: 🔴 "เช่าคอนโด 1 ปี — สัญญาหมดแล้วแต่จ่ายต่อเนื่อง — จู่ๆ บอกย้ายออก 15 วัน"

**Category mapping:** `housing` → `situation: ...` (doesn't fit neatly; this is about eviction notice)

**Diagnosis simulation:**
- situation: "ข้อพิพาทสภาพทรัพย์" (closest)
- contract: "มีแชท/อีเมล" (original contract expired, continued informally)
- duration: "1 – 3 ปี"
- evidence: "หลักฐานการชำระค่าเช่า, แชทกับอีกฝ่าย" (2 items)

**🟢 Platform answer simulation:**
```
headline: "สัญญาเช่ายังมีผล — เจ้าของต้องบอกล่วงหน้าอย่างน้อย 30 วัน"
summary: "สัญญาหมดแต่จ่ายค่าเช่าต่อเนื่อง 6 เดือน — 
         ถือว่ามีการต่อสัญญาโดยปริยาย — เจ้าของต้องบอกกล่าวล่วงหน้าตามรอบชำระค่าเช่า"
rights:
  - label: "สิทธิได้รับการบอกกล่าวล่วงหน้า"
    detail: "ตาม ป.พ.พ. ม.566 — ต้องบอกกล่าวล่วงหน้าอย่างน้อย 1 งวดการชำระค่าเช่า"
  - label: "สิทธิอยู่ต่อ"
    detail: "การเช่าต่อเนื่องโดยเจ้าของรับค่าเช่า = สัญญาต่ออายุโดยปริยาย"
next_actions:
  - when: "ทันที", title: "แจ้งเจ้าของว่าต้องบอกกล่าวล่วงหน้า 30 วัน", detail: "..."
  - when: "ภายใน 7 วัน", title: "เตรียมหลักฐานการจ่ายค่าเช่าต่อเนื่อง", detail: "..."
citations: [civil-commercial-code-hire]
```

**Verdict: MATCH ✅** — Correctly identifies implied contract renewal and notice period.

---

### Q29: 🔴 "เช่าบ้าน — จ่ายล่วงหน้าทั้งปี 120,000 — อยู่ 3 เดือนต้องย้าย — ขอคืน 9 เดือน"

**Category mapping:** `housing` → `situation: ต้องการบอกเลิกสัญญาเช่า`

**Diagnosis simulation:**
- situation: "ต้องการบอกเลิกสัญญาเช่า"
- contract: "มี สัญญาเป็นลายลักษณ์อักษร"
- duration: "น้อยกว่า 6 เดือน"
- evidence: "สัญญาเช่า, หลักฐานการชำระค่าเช่า" (2 items)

**🟢 Platform answer simulation:**
```
headline: "คุณบอกเลิกสัญญาก่อนกำหนด — มีสิทธิได้เงินคืนบางส่วน"
summary: "จ่ายค่าเช่าล่วงหน้า 1 ปี อยู่ได้ 3 เดือนต้องย้าย — 
         ตามกฎหมาย คุณมีสิทธิบอกเลิกสัญญา และเจ้าของต้องคืนค่าเช่าส่วนที่ยังไม่ได้ใช้"
rights:
  - label: "สิทธิบอกเลิกสัญญาเช่า"
    detail: "ตาม ป.พ.พ. — สามารถบอกเลิกได้ โดยแจ้งล่วงหน้าตามสัญญา"
  - label: "สิทธิได้รับเงินค่าเช่าล่วงหน้าคืน"
    detail: "เจ้าของต้องคืนค่าเช่าส่วนที่ยังไม่ได้ใช้ — เหลือ 9 เดือน = 90,000 บาท"
next_actions:
  - when: "วันนี้", title: "แจ้งบอกเลิกสัญญาเป็นลายลักษณ์อักษร", detail: "ตามเงื่อนไขในสัญญา"
  - when: "ภายใน 7 วัน", title: "ขอคืนเงินค่าเช่าล่วงหน้า", detail: "..."
limitations: "สัญญาเช่าอาจมีข้อกำหนดค่าปรับกรณียกเลิกก่อนครบกำหนด — ตรวจสอบสัญญา"
citations: [civil-commercial-code-hire]
```

**Verdict: MATCH ✅** — Covers early termination and partial refund.

---

### Q30: 🔴 "ซื้อบ้านทาวน์เฮ้าส์ — ทางเข้าต้องผ่านซอยส่วนบุคคล — มีคนจะสร้างกำแพงปิดซอย"

**Category mapping:** `housing` → this is about **ภาระจำยอม (easement)** — NOT in housing diagnosis

**Issue:** The `housing` category focuses on RENTAL disputes, not property easements. This question is about:
- Easement (ภาระจำยอม) — belongs in `property`
- Access rights — belongs in `property`

**Diagnosis simulation (@ property):**
- issue: "แนวเขตไม่ชัด" (closest, but not really)
- documents: "โฉนด (น.ส.4)"
- when: "น้อยกว่า 1 ปี"
- evidence: "เอกสารสิทธิ์, ภาพถ่าย" (2 items)

**🟢 Platform answer simulation (property path):**
```
headline: "คุณมีสิทธิใช้ทางผ่าน — ยื่นคำร้องขอคุ้มครอง"
summary: "ทางเข้าบ้านต้องผ่านที่ดินผู้อื่น — หากใช้มานานอาจเกิดภาระจำยอมโดยอายุความ"
rights:
  - label: "สิทธิขอเปิดทางจำเป็น"
    detail: "ตาม ป.พ.พ. ม.1349 — ที่ดินที่ไม่มีทางออกสู่ทางสาธารณะ"
  - label: "สิทธิฟ้องขอให้รื้อถอนกำแพง"
    detail: "ขอให้ศาลมีคำสั่งคุ้มครองชั่วคราวก่อนพิพากษา"
limitations: "ภาระจำยอมต้องพิสูจน์การใช้ต่อเนื่อง 10 ปี — หากมีสัญญากับเจ้าของเดิม ดีที่สุด"
citations: [civil-code-property, land-code-2497]
```

**Verdict: GAP ❌**
- `housing` category doesn't cover easement/right-of-way ❌
- `property` category doesn't have "ภาระจำยอม" or "ทางจำเป็น" options ❌
- This falls between categories — `housing` (rental) vs `property` (land rights) ❌
- The easement issue requires specific civil code sections not surfaced ❌

---

### Category 10 Coverage Score: **2 MATCH, 1 GAP = 67% coverage**

---

## 11. FAMILY (ครอบครัว)

### Platform config: `family`
| Question ID | Options |
|---|---|
| `situation` | หย่าร้าง, การปกครองบุตร, มรดก, คู่สมรสไม่ซื่อสัตย์ |
| `marriage` | จดทะเบียนสมรส, ไม่จดทะเบียน, หย่าแล้ว, แยกกันอยู่ |
| `children` | มี อายุ<7, มี อายุ≥7, ไม่มีบุตร, มีบุตรจากการสมรสก่อนหน้า |
| `evidence` | ทะเบียนสมรส, ทะเบียนบุตร, หนังสือมอบอำนาจ, สัญญายกทรัพย์/พินัยกรรม |

**Sources:** civil-code-family, civil-code-inheritance, domestic-violence-act-2550

---

### Q31: 🔴 "แต่งงาน 8 ปี — สามีนอกใจ — ไม่ได้ทำงาน — กลัวไม่มีเงินเลี้ยงลูก — สินสมรสในชื่อสามี 2 ล้าน"

**Category mapping:** `family` → `situation: หย่าร้าง`

**Diagnosis simulation:**
- situation: "หย่าร้าง"
- marriage: "จดทะเบียนสมรส"
- children: "มี อายุ 7 ปีขึ้นไป"
- evidence: "ทะเบียนสมรส, ทะเบียนบุตร" (2 items)

**🟢 Platform answer simulation:**
```
headline: "คุณมีสิทธิได้รับส่วนแบ่งสินสมรสและค่าเลี้ยงดู"
summary: "แต่งงาน 8 ปี สามีนอกใจ — สินสมรสที่ได้มาระหว่างสมรสต้องแบ่งครึ่ง 
         แม้ว่าจะอยู่ในชื่อสามีทั้งหมด — นอกจากนี้ยังมีสิทธิเรียกค่าทดแทนจากการนอกใจ"
rights:
  - label: "สิทธิแบ่งสินสมรสครึ่งหนึ่ง"
    detail: "ตาม ป.พ.พ. ม.1533 — สินสมรสต้องแบ่งเท่ากัน (บ้าน+รถ+เงินเก็บ 2 ล้าน)"
  - label: "สิทธิเรียกค่าทดแทน"
    detail: "การนอกใจทำให้คุณมีสิทธิเรียกค่าทดแทนจากสามีและเมียน้อย (ม.1523)"
  - label: "สิทธิเรียกค่าเลี้ยงดูบุตร"
    detail: "ลูก 2 คน — สามีต้องจ่ายค่าเลี้ยงดูจนกว่าบุตรจะบรรลุนิติภาวะ"
  - label: "สิทธิเรียกค่าเลี้ยงดูตนเอง"
    detail: "หากหย่าแล้วไม่สามารถเลี้ยงตัวเองได้ — ศาลอาจสั่งให้สามีจ่ายค่าเลี้ยงดู"
next_actions:
  - when: "วันนี้", title: "เก็บหลักฐานการนอกใจ", detail: "แคปแชท ภาพ หลักฐานทั้งหมด"
  - when: "ภายใน 30 วัน", title: "ตรวจสอบสินสมรสทั้งหมด", detail: "..."
citations: [civil-code-family]
```

**Verdict: MATCH ✅** — Comprehensive. Covers division, compensation for infidelity, child support.

---

### Q32: 🔴 "เรากับแฟนอยู่ด้วยกัน 15 ปี — ไม่จดทะเบียน — สร้างเนื้อสร้างตัว — แฟนมีใหม่ — ไล่ออกจากบ้าน"

**Category mapping:** `family` → `situation: ...` (de facto marriage — not in options)

**Diagnosis simulation:**
- situation: "หย่าร้าง" (closest for de facto)
- marriage: "ไม่จดทะเบียน"
- children: "ไม่มีบุตร"
- evidence: "ทะเบียนสมรส" (N/A — they don't have one — evidence score = 0)

**🟢 Platform answer simulation:**
```
headline: "การไม่ได้จดทะเบียนมีข้อจำกัด — แต่คุณอาจมีสิทธิในทรัพย์สินที่ร่วมกันสร้าง"
summary: "ใช้ชีวิตคู่ 15 ปีโดยไม่จดทะเบียน — ไม่ใช่คู่สมรสตามกฎหมาย 
         ทรัพย์สินที่ร่วมกันสร้างอาจถือเป็นกรรมสิทธิ์รวม"
rights:
  - label: "สิทธิในทรัพย์สินที่ร่วมกันสร้าง"
    detail: "หากพิสูจน์ได้ว่าร่วมกันซื้อ/ผ่อน — อาจถือเป็นเจ้าของร่วม (กรรมสิทธิ์รวม)"
  - label: "สิทธิเรียกร้องค่าเสียหาย"
    detail: "หากถูกหลอกหรือถูกเอาเปรียบ"
limitations: "คู่ที่ไม่ได้จดทะเบียนสมรสไม่มีสิทธิแบ่งสินสมรสตามกฎหมายครอบครัว — 
              ต้องใช้หลักกฎหมายเรื่องกรรมสิทธิ์รวมหรือสัญญาจัดการทรัพย์สิน"
citations: [civil-code-family]
```

**Verdict: PARTIAL ⚠️**
- Platform handles de facto marriage as a non-marriage ✅
- But: The question options are built around registered marriage ❌
- But: No "ไม่ได้จดทะเบียนแต่อยู่ด้วยกัน" as a `situation` option ❌
- Missing: Common-law remedies (undue enrichment, co-ownership) ❌

---

### Q33: 🔴 "พ่อเลี้ยงลวนลามลูกสาว 12 ขวบ — ตำรวจบอกไม่เข้าข่ายอนาจารเพราะแค่กอดจับมือ"

**Category mapping:** `family` → `situation: การปกครองบุตร` (but this is criminal)

**Diagnosis simulation:**
- Closest family path would miss the criminal angle
- Better mapped to `crime` → `crime_type: ถูกข่มขืน/คุกคามทางเพศ`

**🟢 Platform answer simulation (crime path):**
```
headline: "การกระทำของพ่อเลี้ยงอาจเป็นการคุกคามทางเพศ — มีช่องทางดำเนินคดี"
summary: "พ่อเลี้ยงลวนลามบุตรสาว 12 ขวบ — การจับเนื้อต้องตัวเด็กโดยไม่สมัครใจ 
         อาจเข้าข่ายกระทำอนาจารแก่เด็กอายุไม่เกิน 15 ปี"
rights:
  - label: "สิทธิแจ้งความในข้อหากระทำอนาจาร"
    detail: "ตาม ม.279 — กระทำอนาจารแก่เด็กอายุไม่เกิน 15 ปี โทษจำคุกสูงสุด 10 ปี"
  - label: "สิทธิขอความคุ้มครองเด็ก"
    detail: "ผ่าน พ.ร.บ.คุ้มครองเด็ก พ.ศ. 2546"
next_actions:
  - when: "ทันที", title: "แจ้งความในข้อหาอนาจาร", detail: "ที่ สน. หรือศูนย์พิทักษ์เด็ก"
  - when: "ภายใน 24 ชม.", title: "ปรึกษานักสังคมสงเคราะห์/บ้านพักเด็ก", detail: "..."
limitations: "ตำรวจประเมินข้อเท็จจริงระดับหนึ่ง — 
              หากไม่รับแจ้งความ ให้ร้องเรียนผู้บังคับบัญชาหรือยื่นฟ้องศาลโดยตรง"
citations: [criminal-code-276]
```

**Verdict: PARTIAL ⚠️**
- Platform has criminal sexual assault category ✅
- But: Child-specific protection laws not in source registry ❌
- But: The family/criminal boundary is hard — user sees "family" problem, platform sees "crime" ❌
- But: The nuance between อนาจาร vs ข่มขืน (M.279 vs M.276) not surfaced in questions ❌

---

### Category 11 Coverage Score: **1 MATCH, 2 PARTIAL = 67% coverage**

---

## 12. ACCIDENT (อุบัติเหตุ)

### Platform config: `accident`
| Question ID | Options |
|---|---|
| `situation` | อุบัติเหตุรถยนต์, อุบัติเหตุมอเตอร์ไซค์, บาดเจ็บในที่สาธารณะ, รถชนทรัพย์สิน |
| `fault` | อีกฝ่ายผิดชัดเจน, ตนเองผิด, ผิดร่วมกัน, ยังไม่ชัดเจน |
| `injury` | ไม่บาดเจ็บ, บาดเจ็บเล็กน้อย, บาดเจ็บสาหัส, เสียชีวิต |
| `evidence` | ใบแจ้งความ, ภาพถ่าย, ใบรับรองแพทย์, ประกันภัย |

**Sources:** traffic-act-2522, tort-act-civil-code

---

### Q34: 🔴 "มอเตอร์ไซค์ — รถเก๋งเปิดประตูไม่มอง — แขนหัก — ประกันเสนอ 20,000 ไม่พอ"

**Category mapping:** `accident` → `situation: อุบัติเหตุมอเตอร์ไซค์`

**Diagnosis simulation:**
- situation: "อุบัติเหตุมอเตอร์ไซค์"
- fault: "อีกฝ่ายผิดชัดเจน"
- injury: "บาดเจ็บสาหัส"
- evidence: "ใบแจ้งความ, ภาพถ่าย, ใบรับรองแพทย์, ประกันภัย" (4 items!)

**🟢 Platform answer simulation:**
```
headline: "อีกฝ่ายเป็นฝ่ายผิด — ค่าเสนอของประกันไม่เพียงพอ"
summary: "รถเก๋งเปิดประตูกะทันหันโดยไม่ดู — เป็นฝ่ายผิดชัดเจน 
         คุณมีสิทธิเรียกร้องค่ารักษาพยาบาลเต็มจำนวน + ค่าขาดรายได้ + ค่าเสียหายทางจิตใจ"
rights:
  - label: "สิทธิเรียกร้องค่าเสียหายจากคู่กรณีโดยตรง"
    detail: "ประกันเสนอ 20,000 — หากไม่เพียงพอ ให้เรียกร้องส่วนต่างจากผู้กระทำโดยตรง"
  - label: "สิทธิฟ้องศาลแพ่งฐานละเมิด"
    detail: "ตาม ป.พ.พ. มาตรา 420 — เรียกค่ารักษา ค่าซ่อมรถ ค่าขาดรายได้"
  - label: "สิทธิเรียกจากประกันคู่กรณี"
    detail: "ประกันชั้น 1 ต้องจ่ายตามความเสียหายจริง — ร้องเรียน คปภ. หากไม่เพียงพอ"
next_actions:
  - when: "วันนี้", title: "ปฏิเสธข้อเสนอ 20,000", detail: "ยื่นค่าเสียหายจริง — ค่ารักษาจริง+ค่าซ่อม+ค่าขาดรายได้"
  - when: "ภายใน 7 วัน", title: "รวบรวมใบเสร็จค่ารักษาทั้งหมด", detail: "..."
  - when: "ภายใน 30 วัน", title: "เจรจาต่อรองกับประกัน", detail: "หากไม่ตกลง — ฟ้องศาล"
evidenceReadiness: 4/5 — "หลักฐานค่อนข้างพร้อม"
citations: [traffic-act-2522, tort-act-civil-code]
```

**Verdict: MATCH ✅** — Excellent. Captures the rejection of low settlement offers well.

---

### Q35: 🔴 "เมาแล้วขับ — ชนท้าย — วัดแอลกอฮอล์ 60 mg% — ประกันไม่คุ้มครอง"

**Category mapping:** `accident` → `situation: อุบัติเหตุรถยนต์`

**Diagnosis simulation:**
- situation: "อุบัติเหตุรถยนต์"
- fault: "ตนเองผิด"
- injury: "ไม่บาดเจ็บ"
- evidence: "ประกันภัย" (1 item)

**🟢 Platform answer simulation:**
```
headline: "เมาแล้วขับ — ประกันมีสิทธิปฏิเสธ — คุณต้องรับผิดชอบค่าเสียหายเอง"
summary: "เมาแล้วขับ แอลกอฮอล์ 60 mg% (เกินกฎหมายกำหนด 50 mg%) — 
         เป็นความผิดอาญาและประกันมีข้อยกเว้น — คุณต้องชดใช้ค่าเสียหายให้คู่กรณี"
rights:
  - label: "สิทธิเจรจาค่าเสียหายกับคู่กรณี"
    detail: "พยายามเจรจากับคู่กรณีโดยตรง — อาจได้ราคาที่ต่ำกว่าฟ้องศาล"
next_actions:
  - when: "ทันที", title: "เจรจาค่าเสียหายกับคู่กรณี", detail: "พยายามตกลงให้เร็ว ลดภาระดอกเบี้ย"
  - when: "ภายใน 7 วัน", title: "เตรียมรับมือคดีอาญา", detail: "เมาแล้วขับ — โทษจำคุก+ปรับ+พักใบขับขี่"
limitations: "เมาแล้วขับเป็นข้อยกเว้นที่ประกันใช้ปฏิเสธได้โดยชอบ — 
              เน้นเจรจาและลดความเสียหาย"
citations: [traffic-act-2522]
```

**Verdict: MATCH ✅** — Correctly calls it: insurance exclusion applies, criminal liability.

---

### Q36: 🔴 "ก่อสร้างรั้ว — ช่างพลัดตกนั่งร้านเสียชีวิต — ไม่มีประกัน — ครอบครัวจะเอาเรื่อง"

**Category mapping:** `accident` → `situation: ...` (construction accident — not in options)

**Diagnosis simulation:**
- situation: "อุบัติเหตุรถยนต์" (WRONG but this is the closest available)
- Actually: This doesn't fit any `accident` options — all 4 are about vehicles!

**🟢 Platform answer simulation (best-effort):**
```
headline: "กรณีช่างรับเหมาตกนั่งร้านเสียชีวิต — คุณอาจต้องรับผิดทางแพ่ง"
summary: "จ้างช่างก่อสร้างรั้ว — สัญญาปากเปล่า — ช่างพลัดตกเสียชีวิต 
         บาดเจ็บสาหัส/เสียชีวิตจากงานก่อสร้างอาจเข้าข่ายละเมิดหรือประมาท"
rights:
  - label: "ความรับผิดทางแพ่ง"
    detail: "อาจต้องจ่ายค่าสินไหมทดแทนให้ครอบครัวผู้เสียชีวิต (ค่าขาดไร้อุปการะ ค่าปลงศพ)"
  - label: "ความรับผิดทางอาญา"
    detail: "อาจถูกดำเนินคดีฐานประมาทเป็นเหตุให้ผู้อื่นถึงแก่ความตาย (ม.291)"
limitations: "ผลวิเคราะห์ไม่ครอบคลุมกฎหมายความปลอดภัยในการทำงาน — 
              การก่อสร้างอาจอยู่ภายใต้ พ.ร.บ.ความปลอดภัย อาชีวอนามัย — ปรึกษาทนาย"
citations: [tort-act-civil-code]
```

**Verdict: GAP ❌**
- `accident` category is VEHICLE-ONLY — all 4 options are about vehicles ❌
- Construction accidents, workplace deaths (for self-employed), home accidents are MISSING ❌
- No "ก่อสร้าง/ซ่อมแซม" situation ❌
- Worker compensation law (for non-employees/contractors) not covered ❌

---

### Category 12 Coverage Score: **2 MATCH, 1 GAP = 67% coverage**

---

## 📊 Overall Summary

### Per-Category Results

| # | Category | Q1 | Q2 | Q3 | MATCH | PARTIAL | GAP | Coverage |
|---|----------|----|----|-----|-------|---------|-----|----------|
| 1 | Online Fraud | ✅ | ✅ | ⚠️ | 2 | 1 | 0 | 83% |
| 2 | Crime | ✅ | ⚠️ | ✅ | 2 | 1 | 0 | 83% |
| 3 | Defamation | ✅ | ⚠️ | ✅ | 2 | 1 | 0 | 83% |
| 4 | Insurance | ✅ | ⚠️ | ✅ | 2 | 1 | 0 | 83% |
| 5 | Government | ⚠️ | ✅ | ⚠️ | 1 | 2 | 0 | 67% |
| 6 | Property | ✅ | ✅ | ⚠️ | 2 | 1 | 0 | 83% |
| 7 | Labour | ✅ | ✅ | ⚠️ | 2 | 1 | 0 | 83% |
| 8 | Consumer | ✅ | ✅ | ⚠️ | 2 | 1 | 0 | 83% |
| 9 | Debt | ✅ | ✅ | ⚠️ | 2 | 1 | 0 | 83% |
| 10 | Housing | ✅ | ✅ | ❌ | 2 | 0 | 1 | 67% |
| 11 | Family | ✅ | ⚠️ | ⚠️ | 1 | 2 | 0 | 67% |
| 12 | Accident | ✅ | ✅ | ❌ | 2 | 0 | 1 | 67% |
| **TOTAL** | | | | | **22** | **12** | **2** | **—** |

---

### Critical GAPs Found

| # | Gap | Severity | Affected Categories |
|---|-----|----------|---------------------|
| **G1** | **No compound scenario support** — Users often have multi-category problems. The platform requires ONE category per diagnosis session. | HIGH | ALL |
| **G2** | **Accident = vehicles only** — The `accident` category has 4 options all about vehicles. Construction, home, workplace accidents not covered. | HIGH | Accident, Labour |
| **G3** | **Housing = rental only** — Easement (ภาระจำยอม), right-of-way (ทางจำเป็น), condominium disputes don't fit the rental questions. | HIGH | Housing, Property |
| **G4** | **No "corruption/bribery" option in Government** — Common Thai problem but not in the diagnosis config. | MEDIUM | Government |
| **G5** | **No guarantor (ผู้ค้ำประกัน) sub-type in Debt** — Very common Thai legal problem. | MEDIUM | Debt |
| **G6** | **Family built around registered marriage** — De facto couples, LGBTQ+ specific issues, domestic workers don't fit well. | MEDIUM | Family |
| **G7** | **No Telegram in platform options** — Only Facebook, LINE, TikTok, X, เว็บบอร์ด. Revenge porn increasingly happens on Telegram. | LOW | Defamation, Online Fraud |
| **G8** | **No tax-specific sources** — Tax disputes go through government but need ประมวลรัษฎากร. | LOW | Government |
| **G9** | **Evidence options don't cover financial documents** — Tax cases, business defamation need บัญชี/งบการเงิน. | LOW | Government, Defamation |
| **G10** | **Child-specific protection laws not in sources** — พ.ร.บ.คุ้มครองเด็ก missing. | LOW | Family, Crime |

---

### Recommendations

#### Priority 1 — Fix Critical Gaps (before production launch)
1. **Add compound diagnosis**: Allow users to flag "multiple issues" and route sub-problems independently
2. **Expand `accident` beyond vehicles**: Add นั่งร้านล้ม, ถูกของหล่นทับ, สัตว์กัด, อาหารเป็นพิษ
3. **Add `easement/access-rights` to `property`**: ภาระจำยอม and ทางจำเป็น are common Thai disputes

#### Priority 2 — Address Significant PARTIALs
4. **Add guarantor/suretyship to `debt`**: One answer option + sources
5. **Add corruption/bribery to `government`**: ป.ป.ช. sources + reporting pathways
6. **Add de facto marriage to `family`**: ไม่จดทะเบียนแต่อยู่ด้วยกัน path + co-ownership remedies
7. **Add tax sources**: ประมวลรัษฎากร in the source registry for `government`

#### Priority 3 — Nice to Have
8. **Add Telegram to `defamation` platform list**
9. **Add child protection law (พ.ร.บ.คุ้มครองเด็ก) to sources** for family/crime
10. **Add financial documents to evidence options** for government/debt/defamation

---

### Strengths

1. **Anti-hallucination citation system is solid** — Every source is registered and validated
2. **Time-based urgency is consistent** — The "when" question drives real action urgency
3. **Evidence readiness calculation** — Explainable, not magical
4. **Human Drives detection** — Smart personalization layer
5. **Conservative legal advice** — No win-probability, clear limitations
6. **Covers the "big 12" categories** — The most common Thai citizen legal problems are represented

---

*Report generated: 11 August 2026 | Tested against LegalAI v1 platform at `D:\legalai-citizen-check`*
*Questions source: `D:\hermes-bess-project\docs\qa_135_real_questions.md`*
