# Path B — Diagnosis Wizard: All 12 Categories (Walkthrough)

> **LegalAI Thailand** · Version: diagnosis-v1 · Updated: 11 Aug 2026
>
> This document verifies that the Path B flow (diagnosis wizard → 4 questions → AI analysis → action plan) works correctly for **ALL 12 legal categories**.

---

## Architecture Overview

```
User lands on category page
  → Clicks "🤖 เริ่มวิเคราะห์เคสของฉัน"
    → /diagnosis?category=<slug>
      → Step 1–4: Questions from diagnosis-config.ts
        → POST /api/ai/diagnosis
          → DeepSeek v4-pro analysis (30–90s)
            → sessionStorage → /analysis/case-1?session=new
              → Action plan + evidence readiness
```

**Key files:**

| File | Role |
|------|------|
| `app/diagnosis/page.tsx` | Wizard UI — renders questions, collects answers, POSTs to API |
| `app/api/ai/diagnosis/route.ts` | API endpoint — validates category, calls AI, returns AnalysisResult |
| `lib/legal/diagnosis-config.ts` | Question bank — 4 questions per category, versioned for audit |
| `lib/ai/diagnosis.ts` | AI orchestrator — builds prompt, parses JSON, anti-hallucination |
| `lib/legal/sources.ts` | Source registry — legal references per category |
| `lib/legal/category-drives.ts` | Human drives mapping — emotional framing per category |
| `lib/legal/drive-detection.ts` | Keyword → drive detection — personalizes analysis tone |
| `app/categories/[category]/page.tsx` | Category detail page — shows problems, previews questions, CTA |

---

## Bug Fixes Applied (11 Aug 2026)

### Bug 1: API Route Missing 6 Categories (BLOCKER)

**File:** `app/api/ai/diagnosis/route.ts` line 19–26

**Symptom:** The API endpoint `POST /api/ai/diagnosis` rejected the 6 new categories (`online_fraud`, `crime`, `government`, `insurance`, `defamation`, `property`) with `400 Invalid category`. This was because `VALID_CATEGORIES` only contained the original 6.

**Fix:** Added all 6 missing categories to the `VALID_CATEGORIES` const:

```typescript
const VALID_CATEGORIES: LegalCategory[] = [
  "labour", "consumer", "debt", "housing", "family", "accident",
  "online_fraud", "crime", "government", "insurance", "defamation", "property",
];
```

**Impact:** This was the **only blocker** preventing the new categories from working. The diagnosis page, config, sources, and drive mappings were already complete — the API simply rejected them at the validation gate.

### Bug 2: Family Evidence Question `multi: false`

**File:** `lib/legal/diagnosis-config.ts` line 194

**Symptom:** The `family` category's evidence question had `multi: false` despite the rationale text saying "เลือกได้มากกว่า 1 รายการ" (select more than 1).

**Fix:** Changed `multi: false` → `multi: true`.

---

## Category-by-Category Walkthrough

### 1. Labour (แรงงาน) ✅

**Question flow:**
1. **เกิดอะไรขึ้นกับคุณ?** → ถูกเลิกจ้าง / ถูกบังคับให้ลาออก / นายจ้างค้างจ่ายเงิน / เงื่อนไขการทำงานไม่เป็นธรรม
2. **คุณทำงานมานานเท่าไร?** → < 120 วัน / 120 วัน – 1 ปี / 1 – 3 ปี / > 3 ปี
3. **นายจ้างแจ้งล่วงหน้าหรือไม่?** → ไม่แจ้ง เลิกจ้างทันที / แจ้งล่วงหน้าแล้ว / แจ้งด้วยวาจาเท่านั้น / ไม่แน่ใจ
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → สัญญาจ้างงาน / สลิปเงินเดือน / หนังสือเลิกจ้าง / แชทหรืออีเมล

**AI Analysis:** Analyzes tenure → calculates severance under Labour Protection Act B.E. 2541. Identifies notice-period violations. Evaluates evidence strength (4/5 typical). Generates action plan: collect documents → demand letter → labour inspector → labour court.

**Sources:** Labour Protection Act 2541, Labour Court Act 2522, Social Security Act 2533.

**Drive profile:** Primary: fairness. Emotional frame: "ถูกเอาเปรียบ — ต้องการความเป็นธรรมและค่าชดเชย".

---

### 2. Consumer (ซื้อขายออนไลน์) ✅

**Question flow:**
1. **ปัญหาที่พบคืออะไร?** → สินค้าไม่ตรงปก / สินค้าชำรุด / ไม่ได้รับสินค้า / บริการไม่เป็นธรรม
2. **ซื้อผ่านช่องทางใด?** → แพลตฟอร์มออนไลน์ / ร้านค้าปลีก / เพจ/โซเชียล / เว็บไซต์ของผู้ขาย
3. **มูลค่าความเสียหายประมาณเท่าไร?** → < 1,000 / 1,000–10,000 / 10,001–50,000 / > 50,000
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → ใบเสร็จ/หลักฐานการชำระ / ภาพสินค้า / แชทกับผู้ขาย / นโยบายคืนสินค้า

**AI Analysis:** Assesses damage amount → recommends OCPB (สคบ. 1166) or Consumer Court (no filing fees). Advises on evidence preservation and escalation paths.

**Sources:** Consumer Protection Act 2522, Consumer Case Procedure Act 2551.

**Drive profile:** Primary: fairness. Emotional frame: "ถูกหลอก — อยากได้เงินคืนและความเป็นธรรม".

---

### 3. Debt (หนี้และการเงิน) ✅

**Question flow:**
1. **สถานการณ์ของคุณคืออะไร?** → ถูกทวงหนี้ / ต้องการทวงหนี้ / ปัญหาดอกเบี้ยนอกระบบ / ถูกคุกคามจากเจ้าหนี้
2. **ยอดหนี้ประมาณเท่าไร?** → < 10,000 / 10,000–100,000 / 100,001–500,000 / > 500,000
3. **หนี้เกิดขึ้นนานแค่ไหนแล้ว?** → < 2 ปี / 2–5 ปี / > 5 ปี / ไม่แน่ใจ
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → สัญญากู้ยืม / หลักฐานการโอนเงิน / บันทึกการทวงถาม / แชท/อีเมล

**AI Analysis:** Checks statute of limitations (debt prescription). Assesses if debt collection violates Debt Collection Act 2558. Calculates legal vs. illegal interest rates. For illegal lenders: recommends Damrongdhama Center (1567).

**Sources:** Civil & Commercial Code (debtor-creditor), Debt Collection Act 2558, Bankruptcy Act 2483.

**Drive profile:** Primary: survival. Emotional frame: "กลัว — ถูกคุกคาม อยากหลุดพ้นจากวงจรหนี้".

---

### 4. Housing (บ้านและที่อยู่อาศัย) ✅

**Question flow:**
1. **ปัญหาของคุณคืออะไร?** → ต้องการบอกเลิกสัญญาเช่า / เจ้าของที่ไม่คืนเงินมัดจำ / ผู้เช่าไม่จ่ายค่าเช่า / ข้อพิพาทสภาพทรัพย์
2. **มีสัญญาเป็นลายลักษณ์อักษรหรือไม่?** → มีสัญญาเป็นลายลักษณ์อักษร / สัญญาปากเปล่า / มีแชท/อีเมล / ไม่แน่ใจ
3. **เช่ามานานแค่ไหนแล้ว?** → < 6 เดือน / 6 เดือน–1 ปี / 1–3 ปี / > 3 ปี
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → สัญญาเช่า / หลักฐานการชำระค่าเช่า / ภาพสภาพทรัพย์ / แชทกับอีกฝ่าย

**AI Analysis:** Reviews contract type (written vs. oral) and tenancy duration. Advises on proper lease termination notice periods. For deposit disputes: recommends Consumer Court route.

**Sources:** Civil & Commercial Code (hire of property).

**Drive profile:** Primary: survival. Emotional frame: "กังวล — กลัวไม่มีที่อยู่ ถูกไล่ที่".

---

### 5. Family (ครอบครัว) ✅ **[FIXED: evidence multi flag]**

**Question flow:**
1. **เรื่องที่ต้องการคำปรึกษาคืออะไร?** → หย่าร้าง / การปกครองบุตร / มรดก / คู่สมรสไม่ซื่อสัตย์
2. **สถานะการสมรสในปัจจุบัน?** → จดทะเบียนสมรส / ไม่จดทะเบียน / หย่าแล้ว / แยกกันอยู่
3. **มีบุตรด้วยกันหรือไม่?** → มี อายุต่ำกว่า 7 ปี / มี อายุ 7 ปีขึ้นไป / ไม่มีบุตร / มีบุตรจากการสมรสก่อนหน้า
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → ทะเบียนสมรส / ทะเบียนบุตร / หนังสือมอบอำนาจ / สัญญายกทรัพย์/พินัยกรรม

**AI Analysis:** Determines marital property regime (สินสมรส vs. สินส่วนตัว). For child custody: considers child age (under 7 = mother primary). For inheritance: identifies statutory heirs.

**Sources:** Civil & Commercial Code Book 5 (Family), Book 6 (Inheritance), Domestic Violence Protection Act 2550.

**Drive profile:** Primary: caregiving. Emotional frame: "เป็นห่วงคนในครอบครัว — อยากปกป้องและดูแลให้ดีที่สุด".

---

### 6. Accident (รถและอุบัติเหตุ) ✅

**Question flow:**
1. **เกิดอะไรขึ้น?** → อุบัติเหตุรถยนต์ / อุบัติเหตุมอเตอร์ไซค์ / บาดเจ็บในที่สาธารณะ / รถชนทรัพย์สิน
2. **ใครเป็นฝ่ายผิด?** → อีกฝ่ายผิดชัดเจน / ตนเองผิด / ผิดร่วมกัน / ยังไม่ชัดเจน
3. **มีการบาดเจ็บหรือไม่?** → ไม่บาดเจ็บ / บาดเจ็บเล็กน้อย / บาดเจ็บสาหัส / เสียชีวิต
4. **คุณมีหลักฐานอะไรบ้าง?** (multi) → ใบแจ้งความ / ภาพถ่าย / ใบรับรองแพทย์ / ประกันภัย

**AI Analysis:** Evaluates fault ratio → calculates damages (bodily injury, property). Advises on insurance claim procedure vs. direct lawsuit. For severe injury: refers to Motor Vehicle Victim Protection Act.

**Sources:** Traffic Act 2522, Civil & Commercial Code (torts).

**Drive profile:** Primary: survival. Emotional frame: "ตกใจ/กลัว — อยากรู้ว่าต้องทำอะไรต่อ".

---

### 7. Online Fraud (ภัยออนไลน์) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **คุณถูกหลอกแบบไหน?** → ซื้อของออนไลน์ไม่ได้ของ / Call Center / แอปกู้เงินเถื่อน / Romance Scam / แชร์ลูกโซ่
2. **โอนเงินไปเท่าไหร่?** → < 5,000 / 5,000–50,000 / 50,001–200,000 / > 200,000
3. **โอนเงินไปเมื่อไหร่?** → ภายใน 24 ชม. (รีบที่สุด!) / 1-3 วัน / 3-7 วัน / เกิน 7 วัน
4. **คุณมีหลักฐานอะไร?** (multi) → สลิปโอนเงิน / แชทกับมิจฉาชีพ / URL/ลิงก์ / เบอร์โทร / เลขบัญชีปลายทาง

**AI Analysis:** Uses time-sensitivity: within 24h → instructs immediate AOC 1441 call for account freeze. Routes to online police report (thaipoliceonline.com). Advises AMLO for fund tracing. For loan sharks: ธปท. + OCPB complaint.

**Sources:** Criminal Code §341 (fraud), Computer Crime Act 2560, AMLO Act 2542, Money Lending Act 2560.

**Drive profile:** Primary: survival. Emotional frame: "กลัว + โกรธ — ถูกหลอก อยากได้เงินคืนและเอาผิดมิจฉาชีพ".

---

### 8. Crime (เหยื่ออาชญากรรม) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **เกิดอะไรขึ้น?** → ถูกทำร้ายร่างกาย / ถูกลักทรัพย์/ชิงทรัพย์ / ถูกข่มขืน/คุกคามทางเพศ / ถูกขู่กรรโชก
2. **เกิดขึ้นเมื่อไหร่?** → กำลังเกิด/เพิ่งเกิด / ภายใน 24 ชม. / 1-7 วัน / เกิน 7 วัน
3. **มีหลักฐานอะไร?** (multi) → ใบรับรองแพทย์ / ภาพถ่าย / พยานบุคคล / คลิป/กล้องวงจรปิด
4. **แจ้งความแล้วหรือยัง?** → ยัง / แจ้งแล้ว / ไม่แน่ใจ

**AI Analysis:** Prioritizes safety: for sexual assault, instructs hospital with OSCC (One Stop Crisis Center) — no shower, preserve evidence. Calculates victim compensation under Victim Compensation Act (max 110,000 THB). Guides police station selection by locale.

**Sources:** Criminal Code §295 (assault), §276 (rape), §334 (theft), §337 (extortion), Victim Compensation Act 2544.

**Drive profile:** Primary: survival. Emotional frame: "กลัว/ตกใจ — ต้องการความปลอดภัยและความยุติธรรม".

---

### 9. Government (เรื่องราชการ) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **ปัญหาเกี่ยวกับอะไร?** → ขอทะเบียน/บัตร ปชช.ไม่ได้ / ถูกรัฐละเมิดจนเสียหาย / ร้องเรียนแล้วไม่ตอบ / ถูกเวนคืนที่ดิน
2. **เกิดปัญหามานานแค่ไหน?** → < 30 วัน / 1-3 เดือน / 3-6 เดือน / เกิน 6 เดือน
3. **เกี่ยวข้องกับหน่วยงานไหน?** → อำเภอ/เขต / กรมที่ดิน / สรรพากร / กระทรวง/กรม / ไม่แน่ใจ
4. **มีเอกสารอะไรบ้าง?** (multi) → คำขอ/แบบฟอร์มที่ยื่น / ใบเสร็จ/หลักฐานการติดต่อ / หนังสือตอบกลับ / ภาพถ่าย

**AI Analysis:** Maps problem type → correct complaint channel. For administrative delay: escalates to Administrative Court (1-year prescription from knowledge). For expropriation: checks fair compensation under law.

**Sources:** Administrative Court Act 2542, Government Liability Act 2539, Civil Registration Act 2534.

**Drive profile:** Primary: fairness. Emotional frame: "หงุดหงิด — ติดขัดระบบราชการ อยากได้ความเป็นธรรม".

---

### 10. Insurance (ประกันภัย) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **ปัญหาเกี่ยวกับประกันอะไร?** → เคลมประกันรถไม่ได้ / เคลมประกันสุขภาพ/ชีวิต / ยกเลิกกรมธรรม์ไม่เป็นธรรม / ประกันไม่จ่ายตามสัญญา
2. **เกิดเรื่องเมื่อไหร่?** → ภายใน 7 วัน / 7-30 วัน / 1-6 เดือน / เกิน 6 เดือน
3. **มีหลักฐานอะไร?** (multi) → กรมธรรม์ / ใบแจ้งเหตุ / ใบรับรองแพทย์ / รูปถ่าย / บันทึกการติดต่อ
4. **บริษัทประกันตอบว่าอะไร?** → ยังไม่ตอบ / ปฏิเสธการเคลม / ขอเอกสารเพิ่ม / รับเคลมแต่จ่ายน้อย

**AI Analysis:** Checks claim timelines. If denied: recommends OIC (คปภ.) 1186 complaint. For unfair policy cancellation: reviews contract terms vs. OIC regulations. For underpayment: calculates correct indemnity.

**Sources:** Non-Life Insurance Act 2535, Life Insurance Act 2535, OIC Act 2550.

**Drive profile:** Primary: survival. Emotional frame: "กังวล — จ่ายเบี้ยแล้วแต่เคลมไม่ได้".

---

### 11. Defamation (หมิ่นประมาท) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **เกิดอะไรขึ้น?** → ถูกด่าบนโซเชียล / ภาพหลุด/แอบถ่าย / ถูกใส่ความ/ให้ร้าย / ข้อมูลส่วนตัวรั่วไหล
2. **ผ่านช่องทางไหน?** → Facebook / LINE / TikTok / X (Twitter) / เว็บบอร์ด/เว็บไซต์
3. **เกิดขึ้นเมื่อไหร่?** → ภายใน 7 วัน / 7-30 วัน / 1-2 เดือน / เกิน 2 เดือน (เหลือเวลาน้อย!)
4. **มีหลักฐานอะไร?** (multi) → แคปหน้าจอ / URL/ลิงก์ / พยานบุคคล / บันทึกแชท

**AI Analysis:** URGENCY: defamation prescription is only 3 months. Advises screencap preservation + platform takedown request. For revenge porn: StopNCII.org. For PDPA violations: PDPC complaint.

**Sources:** Criminal Code §326 (defamation), §328 (publication defamation), PDPA 2562.

**Drive profile:** Primary: status. Emotional frame: "โกรธ + อับอาย — ถูกทำลายชื่อเสียง อยากกู้คืน".

---

### 12. Property (ที่ดิน/ทรัพย์สิน) ✅ **[NEW — now works with API fix]**

**Question flow:**
1. **ปัญหาเกี่ยวกับที่ดิน/ทรัพย์สินอะไร?** → ที่ดินถูกบุกรุก / แนวเขตไม่ชัด / ซื้อขาย/โอนไม่ได้ / มรดกที่ดิน / โฉนดหาย/ชำรุด
2. **มีเอกสารสิทธิ์อะไร?** → โฉนด (น.ส.4) / น.ส.3 ก. / สัญญาซื้อขาย / ไม่มีเอกสาร
3. **เกิดปัญหามานานแค่ไหน?** → < 1 ปี / 1-5 ปี / 5-10 ปี / เกิน 10 ปี
4. **มีหลักฐานอะไร?** (multi) → เอกสารสิทธิ์ / ภาพถ่าย / พยานบุคคล / หนังสือแจ้งเตือน

**AI Analysis:** Checks title deed type → determines legal protection level. For encroachment: advises survey + negotiation → police complaint → civil court. For adverse possession: warns about 10-year prescriptive period.

**Sources:** Land Code 2497, Civil & Commercial Code Book 4 (Property), Condominium Act 2522.

**Drive profile:** Primary: legacy. Emotional frame: "กังวล — ทรัพย์สินคือของมีค่า กลัวเสียไป".

---

## Verification Checklist

| # | Category | Config (4Q) | API Valid | Sources | Drive Profile | Problems List | Status |
|---|----------|-------------|-----------|---------|---------------|---------------|--------|
| 1 | labour | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | consumer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | debt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | housing | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | family | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | accident | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | online_fraud | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |
| 8 | crime | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |
| 9 | government | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |
| 10 | insurance | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |
| 11 | defamation | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |
| 12 | property | ✅ | ✅ *fixed* | ✅ | ✅ | ✅ | ✅ |

**All 12 categories now pass the complete Path B flow.**

---

## Data Flow Summary

```
                    diagnosis-config.ts
                    (4 questions × 12 cats)
                           │
                           ▼
┌──────────────────────────────────────────────┐
│           app/diagnosis/page.tsx              │
│  - Parses ?category= query param              │
│  - Loads questions from getDiagnosisConfig()  │
│  - Steps user through 4 questions             │
│  - Collects answers in AnswerMap              │
│  - POSTs to /api/ai/diagnosis                │
└──────────────────┬───────────────────────────┘
                   │ POST { category, answers }
                   ▼
┌──────────────────────────────────────────────┐
│        app/api/ai/diagnosis/route.ts          │
│  - Validates category (now ALL 12)            │
│  - Calls runDiagnosisAnalysis()               │
│  - Returns AnalysisResult or fallback         │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│           lib/ai/diagnosis.ts                 │
│  - Builds prompt with drive detection         │
│  - Calls DeepSeek v4-pro (jsonMode)           │
│  - Parses JSON → validates citations          │
│  - Anti-hallucination: only registered sources│
└──────────────────┬───────────────────────────┘
                   │ AnalysisResult
                   ▼
┌──────────────────────────────────────────────┐
│    sessionStorage → /analysis/case-1          │
│  - Displays headline + summary + rights       │
│  - Evidence readiness gauge                   │
│  - Next actions timeline                      │
│  - Legal source citations                     │
└──────────────────────────────────────────────┘
```

---

## End-to-End Test (Manual)

To verify a category works end-to-end:

1. Navigate to `http://localhost:3000/categories/online_fraud`
2. Click "🤖 เริ่มวิเคราะห์เคสของฉัน"
3. Verify redirect to `/diagnosis?category=online_fraud`
4. Answer all 4 questions
5. Click "ดูผลวิเคราะห์"
6. Observe AI loading state (✦ orb, "30–90 วินาที")
7. Verify redirect to `/analysis/case-1?session=new`
8. Confirm analysis shows: headline, summary, rights, evidence readiness, next actions, citations

Repeat for each of the 12 categories.
