# LegalAI Citizen — Gap Analysis: Codebase vs. Comprehensive Consumer Legal Fears

> **Date:** 9 สิงหาคม 2569  
> **Scope:** Analysis of `legalai-thailand-citizen` codebase (`diagnosis-config.ts`) vs. research-driven comprehensive legal problems framework  
> **Key Artifact:** `D:\legalai-citizen-check\lib\legal\diagnosis-config.ts`  
> **Research Basis:** 12 categories, 45 problems, 22 Human Drives, detailed victim-centric guides across 7 documents

---

## Executive Summary

The LegalAI citizen codebase currently supports **6 legal categories with 4 generic questions each** (24 questions total). Our comprehensive research defines **12 categories with 45 distinct problem types**, each mapped to specific human drives, emotional fears, and actionable victim-centered workflows. 

**The gap is 50% category coverage and ~80% subcategory coverage.** More critically, the current diagnosis asks "what happened?" but never asks "what are you afraid of?" — missing the psychological drivers that push citizens from anxiety to action. Without surfacing fear and urgency, the product cannot prioritize cases or guide citizens through the most time-sensitive steps.

### Gap Dimensions (6 Axes)

| Dimension | Codebase | Research | Gap |
|-----------|----------|----------|-----|
| **Categories** | 6 | 12 | **-6 categories** (50% coverage) |
| **Problem Subtypes** | ~6 (1 per category) | 45 | **-39 subtypes** (~13% coverage) |
| **Fear/Urgency Signals** | None | 4 negative drives | **Missing entirely** |
| **Human Drive Mapping** | None | 22-drive framework | **Missing entirely** |
| **Temporal Urgency** | None | Time-critical steps (e.g., freeze account in 24h) | **Missing entirely** |
| **Emotional Language** | Neutral/clinical | Fear-aware, empathetic | **Missing entirely** |

---

## 1. Missing Categories (6 Categories, 21 Problems)

The codebase supports: `labour`, `consumer`, `debt`, `housing`, `family`, `accident`.

**6 entire categories are missing from the diagnosis system.** These are critical consumer legal fears — some are the most commonly searched legal problems in Thailand:

### 1.1 Online Fraud / Cybercrime (5 problems) — 🔴 HIGHEST PRIORITY

> **Why it matters:** Online fraud is the #1 fastest-growing legal problem in Thailand (AOC 1441 reported 300,000+ cases annually). It's the most common entry point for a citizen seeking legal help.

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 1.1 | ถูกหลอกซื้อของออนไลน์ — โอนเงินแล้วไม่ได้ของ | ⚡ Within 24-72h for account freeze | Loss of money + shame of being fooled |
| 1.2 | Call Center Scam — หลอกให้โอนเงิน | ⚡ Within 1-3h for emergency freeze | Survival fear (life savings wiped) |
| 1.3 | Social Media Account Hacking | 🟡 1-7 days | Loss of identity + privacy violation |
| 1.4 | Online Investment Fraud / แชร์ลูกโซ่ | ⚡ Evidence collection window | Loss + shame + betrayal |
| 1.5 | Phishing / Identity Theft | 🟡 1-7 days | Fear of cascading damage |

**Key Human Drives Activated:**
- **Drive 19: Avoid Shame** — "ฉันโง่เองที่หลงเชื่อ" (self-blame prevents reporting)
- **Drive 20: Avoid Loss** — Fear of losing money with no way to recover
- **Drive 1: Survival & Safety** — Life savings wiped, can't pay rent/bills

**What's Missing in Codebase:** No `online_fraud` category. No time-urgent triage. A citizen who just transferred 50,000 THB to a scammer has no path — they'd have to pick "consumer" (wrong) or get lost entirely.

---

### 1.2 Criminal Victim (4 problems) — 🔴 HIGH PRIORITY

> **Why it matters:** Physical safety threats create the highest fear urgency. These users need immediate protection + legal guidance.

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 8.1 | ถูกทำร้ายร่างกาย (Physical Assault) | ⚡ Within 24-72h (statute: 3 months) | Survival + fear of repeat |
| 8.2 | ถูกลักทรัพย์ / ถูกขโมย (Theft/Burglary) | ⚡ Preserve crime scene immediately | Loss + feeling violated in home |
| 8.3 | ถูกข่มขู่ / กรรโชกทรัพย์ (Extortion/Blackmail) | ⚡ Immediate — safety first | Survival fear + powerlessness |
| 8.4 | ถูกฉ้อโกง (Criminal Fraud — offline) | 🟡 Within 3 months of discovery | Loss + betrayal |

**Key Human Drives Activated:**
- **Drive 1: Survival & Safety** — Primary: "ชีวิตต้องไม่พัง"
- **Drive 19: Avoid Shame** — Victims often blame themselves
- **Drive 14: Need for Justice** — "มันต้องได้รับโทษ"

**What's Missing in Codebase:** No `criminal_victim` category. Accident category exists for traffic but there's no path for a citizen who was assaulted.

---

### 1.3 Government Services (3 problems) — 🟡 MEDIUM PRIORITY

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 9.1 | การขอเอกสารราชการล่าช้า/ถูกปฏิเสธ | 🟡 | Powerlessness against bureaucracy |
| 9.2 | การขอสัญชาติ / สถานะบุคคล (Citizenship) | 🟡 3-12 months | Existential identity crisis |
| 9.3 | การขอรับเงินสงเคราะห์/สวัสดิการรัฐ (Welfare) | 🟡 15-60 days | Survival — can't afford basic needs |

**Key Human Drives Activated:**
- **Drive 1: Survival** — Welfare denial = can't survive
- **Drive 14: Need for Justice/Fairness** — "ทำไมเขาถึงไม่ให้สิทธิฉัน"
- **Drive 9: Need for Autonomy/Freedom** — Bureaucracy = loss of control

---

### 1.4 Insurance (3 problems) — 🟡 MEDIUM PRIORITY

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 11.1 | บริษัทประกันไม่จ่ายค่าสินไหม (Claim Denial) | 🟡 Within 30 days | Betrayal — "จ่ายเบี้ยมาตลอด แต่ไม่ได้อะไร" |
| 11.2 | ประกันยกเลิกกรมธรรม์ไม่เป็นธรรม (Unfair Cancellation) | 🟡 | Loss of safety net |
| 11.3 | ตัวแทนประกันขายไม่ตรงปก (Mis-Selling) | ⚡ Free Look: 15-30 days | Being cheated by "trusted" agent |

**Key Human Drives Activated:**
- **Drive 20: Avoid Loss** — Paid premiums for nothing
- **Drive 21: Revenge/Retribution** — "ฉันจ่ายเบี้ยทุกเดือนแล้วไม่จ่ายคืน?"
- **Drive 1: Survival** — Insurance was the safety net

---

### 1.5 Defamation / Privacy (4 problems) — 🟡 MEDIUM PRIORITY

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 12.1 | ถูกหมิ่นประมาททางโซเชียล (Online Defamation) | ⚡ 3-month statute for criminal | Shame — public humiliation |
| 12.2 | การละเมิดข้อมูลส่วนบุคคล (PDPA Violation) | 🟡 | Loss of control over personal data |
| 12.3 | ถูกแอบถ่าย/เผยแพร่ภาพ (Non-Consensual Images) | ⚡ Take down ASAP | Extreme shame + violation |
| 12.4 | การหมิ่นประมาทโดยการพูด/เขียน (Libel/Slander) | ⚡ 3-month statute | Reputation destruction |

**Key Human Drives Activated:**
- **Drive 19: Avoid Shame** — PRIMARY: public humiliation is devastating in Thai culture
- **Drive 4: Status & Prestige** — "เสียหน้า" = loss of social standing
- **Drive 5: Belonging & Connection** — Fear of being ostracized
- **Drive 21: Revenge/Retribution** — "ต้องทำให้มันได้รับโทษ"

---

### 1.6 Property / Land (3 problems) — 🟡 MEDIUM PRIORITY

| # | Problem | Urgency | Core Fear |
|---|---------|---------|-----------|
| 5.1 | ที่ดินถูกรุกล้ำ (Land Encroachment) | 🟡 File within 1 year | Loss of ancestral land |
| 5.2 | ปัญหาแนวเขตที่ดิน (Boundary Dispute) | 🟡 6-24 months | Ongoing conflict with neighbors |
| 5.3 | ซื้อคอนโด/บ้านไม่ได้ตามสัญญา (Developer Breach) | 🟡 | Life savings stuck in unfinished project |

**Note:** The codebase has `housing` (rental-focused) but no `property` (land ownership). These are distinct legal domains — housing covers tenant-landlord; property covers land title disputes, boundary issues, and real estate purchase fraud.

---

## 2. Missing Subcategories Within Existing 6 Categories

The current diagnosis offers exactly **one problem per category** via a single multi-choice question. But each category in our research has 3-5 distinct sub-problems, each with different legal pathways.

### 2.1 Labour (Codebase: 1 scenario → Research: 4 scenarios)

| Codebase Question | What It Covers | What's Missing from Research |
|-------------------|---------------|------------------------------|
| "เกิดอะไรขึ้นกับคุณ?" → "ถูกเลิกจ้าง" | Unfair dismissal only | |
| | ❌ Missing | **2.2 นายจ้างไม่จ่ายค่าจ้าง/ค่าชดเชย** — Different legal path; needs wage claim, not dismissal appeal |
| | ❌ Missing | **2.3 ถูกละเมิดสิทธิขั้นพื้นฐาน** — Overtime pay, minimum wage, working hours violations |
| | ❌ Missing | **2.4 การคุกคามในที่ทำงาน** — Harassment/discrimination; involves criminal law, not just labour law |

**Example Gap:** A worker whose boss hasn't paid wages for 3 months selects "ถูกเลิกจ้าง" even though they weren't fired — because that's the closest option. The AI analysis would then give wrong compensation calculations.

---

### 2.2 Consumer (Codebase: 1 scenario → Research: 4 scenarios)

| Codebase Question | What It Covers | What's Missing from Research |
|-------------------|---------------|------------------------------|
| "ปัญหาที่พบคืออะไร?" → "สินค้าไม่ตรงปก" | Defective product only | |
| | ❌ Missing | **4.2 ถูกเอาเปรียบจากสัญญาไม่เป็นธรรม** — Unfair contracts; different law (พ.ร.บ. ข้อสัญญาที่ไม่เป็นธรรม 2540) |
| | ❌ Missing | **4.3 อาหาร/ยาไม่ได้มาตรฐาน** — Food/drug safety; involves FDA (อย.), not OCPB |
| | ❌ Missing | **4.4 โฆษณาเกินจริง/หลอกลวง** — False advertising; involves multiple agencies (สคบ., กสทช., อย.) |

**Example Gap:** A citizen who bought expired medicine doesn't fit "สินค้าไม่ตรงปก" — the safety urgency is higher and involves different authorities (อย. 1556, not สคบ. 1166).

---

### 2.3 Debt (Codebase: 1 scenario → Research: 4 scenarios)

| Codebase Question | What It Covers | What's Missing from Research |
|-------------------|---------------|------------------------------|
| "สถานการณ์ของคุณคืออะไร?" → options mix creditor/debtor | Confusing — mixes sides | |
| | ❌ Missing | **3.1 ถูกทวงหนี้ผิดกฎหมาย** — Specific time/conduct violations under พ.ร.บ. ทวงถามหนี้ 2558 |
| | ❌ Missing | **3.2 หนี้นอกระบบ/ดอกเบี้ยโหด** — Illegal lending; criminal + civil paths; involves ศูนย์ดำรงธรรม 1567 |
| | ❌ Missing | **3.3 ติดแบล็คลิสต์เครดิตบูโร** — Credit repair path; NCB process |
| | ❌ Missing | **3.4 ถูกฟ้องล้มละลาย** — Bankruptcy defense; urgent court deadlines |

**Critical Issue:** The current debt question mixes creditor perspective ("ต้องการทวงหนี้") and debtor perspective ("ถูกทวงหนี้") in one question, but these require entirely different legal workflows. A debtor being harassed by loan sharks needs criminal protection, not civil debt collection advice.

---

### 2.4 Housing (Codebase: Rental-only → Research: Rental 3 + Property 3)

The codebase treats `housing` as rental only. Research splits into Housing/Rental (เช่า) and Property/Land (ที่ดิน) as separate categories.

Within rental, the codebase offers 4 options covering both sides. But missing depth:

- ❌ **Eviction timeline by type** — No differentiation between lease-end eviction, non-payment eviction, and breach eviction. The legal notice periods differ.
- ❌ **Deposit dispute specifics** — No question about pre/post move-in inspection evidence, which is the decisive factor in deposit cases.
- ❌ **Property ownership issues** — The 3 land-related problems (encroachment, boundary, developer breach) have no path.

---

### 2.5 Family (Codebase: Mixed → Research: 5 scenarios)

| Codebase Question | What It Covers | What's Missing from Research |
|-------------------|---------------|------------------------------|
| "เรื่องที่ต้องการ..." | 4 options | |
| | ✅ | 6.1 หย่าร้าง |
| | ✅ | 6.3 สิทธิการเลี้ยงดูบุตร |
| | ❌ Missing | **6.2 การแบ่งสินสมรส** — Distinct from divorce; can happen separately |
| | ❌ Missing | **6.4 ข้อพิพาทเรื่องมรดก** — Inheritance disputes; different court (not family court), different laws |
| | ❌ Missing | **6.5 การรับบุตรบุญธรรม / จดทะเบียนรับรองบุตร** — Administrative process, not dispute |

---

### 2.6 Accident (Codebase: 4 scenarios → Research: 3 scenarios)

The accident category has the best coverage of the existing 6 — the 4 options for "เกิดอะไรขึ้น?" roughly match the research. However:

- ❌ **No insurance triage question** — The evidence question asks about "ประกันภัย" but doesn't ask WHETHER they have insurance or what type (พ.ร.บ. mandatory vs. voluntary). This is crucial for claim timelines.
- ❌ **No hit-and-run specific path** — Research problem 7.3 (ชนแล้วหนี) has different procedures (กองทุนทดแทนผู้ประสบภัย) than standard accidents.

---

## 3. Missing Fear/Urgency Signals

The current diagnosis flow is purely factual: "What happened? How long? Do you have evidence?" This is legally useful but **psychologically incomplete**. Citizens with legal problems are experiencing one or more of 4 negative drives (fear-based motivations from the 22 Human Drives framework):

### 3.1 The Four Fear Drives (Drives 19-22)

| Drive | Description | How It Manifests in Legal Problems | Diagnostic Question Missing |
|-------|-------------|-----------------------------------|-----------------------------|
| **19. Avoid Shame** | "ไม่ได้อยากชนะ — แต่กลัวเสียหน้ามากที่สุด" | Victim blames self, delays reporting, hides problem from family | "คุณรู้สึกอายหรือกลัวคนอื่นรู้เรื่องนี้ไหม?" |
| **20. Avoid Loss** | "การสูญเสียเจ็บกว่าการได้สิ่งใหม่" (Loss Aversion) | Fear of losing money, property, relationships, status | "อะไรคือสิ่งที่คุณกลัวจะสูญเสียมากที่สุด?" |
| **21. Revenge/Retribution** | "ฉันถูกทำร้าย — และฉันจะเอาคืน" | Anger drives action; wants punishment, not just resolution | "คุณต้องการให้อีกฝ่ายได้รับโทษ หรือแค่ขอเงินคืน?" |
| **22. Prove Oneself** | "ฉันจะทำให้พวกเขาเห็น!" | Motivated by past humiliation; needs validation | "มีใครบอกคุณว่า 'ทำอะไรไม่ได้หรอก' ไหม?" |

### 3.2 Time-Critical Urgency Not Surfaced

The current diagnosis never asks **WHEN** things happened, only "how long has this been going on?" This misses the most critical piece of legal triage:

| Category | Time-Critical Action | Window | Current Detection |
|----------|---------------------|--------|-------------------|
| Online Fraud | Freeze scammer bank account | 1–3 hours (AOC 1441) | ❌ Not asked |
| Online Fraud | File police report online | 24–72 hours | ❌ Not asked |
| Criminal Victim | File complaint (อายุความร้องทุกข์) | 3 months from discovery | ❌ Not asked |
| Insurance | Free Look cancellation | 15–30 days from receiving policy | ❌ Not asked |
| Defamation | Criminal complaint filing | 3 months from knowing the act | ❌ Not asked |
| Labour | File complaint with labour inspector | 2 years | ❌ Only asks tenure, not "when did this happen?" |
| Accident | Report to police + insurer | 24 hours | ❌ Not asked |

### 3.3 Severity/Impact Not Assessed

The current diagnosis asks "มูลค่าความเสียหายประมาณเท่าไร?" (how much damage?) only in consumer and debt categories. But financial loss is only one dimension:

- ❌ **Physical injury severity** — Only asked in accident (injury level). Missing from criminal victim entirely.
- ❌ **Emotional/psychological impact** — Never assessed.
- ❌ **Social impact** — Reputation damage, family strain, job loss from legal problems.
- ❌ **Cascading risk** — "If you don't resolve this in 7 days, what else will fail?" (can't pay rent → eviction → homelessness)

---

## 4. Missing Psychology: Human Drive Mapping

The 22 Human Drives Framework provides a systematic way to understand WHY a citizen seeks help and WHAT emotional outcome they truly want. The current diagnosis has zero mapping to drives.

### 4.1 Drive-to-Category Mapping

Here's how the 22 drives map to legal problem categories — this is the missing "why" behind every "what":

| # | Drive | Primary Legal Categories Activated | Diagnostic Value |
|---|-------|-----------------------------------|-----------------|
| 1 | Survival & Safety | All categories (universal) | "Are you afraid for your safety right now?" |
| 2 | Benefit & Value | Consumer, Insurance, Debt | "Is this about getting your money's worth?" |
| 3 | Recognition & Praise | — | Less relevant for crisis; relevant for reporting success |
| 4 | Status & Prestige | Defamation, Family, Property | "Are you worried about losing face/status?" |
| 5 | Belonging & Connection | Family, Defamation | "Are you afraid of being cut off from family/community?" |
| 6 | Love & Deep Connection | Family (divorce, custody) | "Is this about protecting someone you love?" |
| 7 | Power & Control | Labour, Housing, Government | "Do you feel powerless against the other side?" |
| 8 | Mastery & Competence | — | Less relevant |
| 9 | Autonomy & Freedom | Labour (forced resignation), Criminal, Debt | "Do you feel trapped with no way out?" |
| 10-13 | (Growth, Curiosity, Order, Novelty) | — | Less relevant for crisis legal help |
| 14 | Justice & Fairness | ALL categories (universal) | "Do you feel this is fundamentally unfair?" |
| 15 | Nurturance & Contribution | Family (custody), Criminal (protecting others) | "Are you trying to protect someone else?" |
| 16 | Identity & Self-Consistency | Defamation, Family | "Does this situation threaten who you are?" |
| 17-18 | (Purpose, Legacy) | Property, Inheritance | "Is this about something that should outlast you?" |
| **19** | **Avoid Shame** | **Online Fraud, Defamation, Debt** | **FEAR DRIVE — Most common barrier to seeking help** |
| **20** | **Avoid Loss** | **All categories** | **FEAR DRIVE — Core motivator for action** |
| **21** | **Revenge/Retribution** | **Criminal Victim, Defamation, Fraud** | **FEAR DRIVE — Drives reporting but can misdirect** |
| **22** | **Prove Oneself** | **Labour, Consumer (standing up to big company)** | **FEAR DRIVE — Turns victims into fighters** |

### 4.2 Drive-Based Triage Questions (Not Currently Asked)

A psychology-aware diagnosis would include at least one "fear calibration" question after initial fact-finding:

```typescript
// Example: Fear Calibration Questions (to add after any category diagnosis)
const fearCalibrationQuestions = [
  {
    id: "fear_primary",
    title: "สิ่งที่คุณกังวลมากที่สุดในตอนนี้คืออะไร?",
    rationale: "เราเข้าใจว่าเรื่องกฎหมายน่ากลัว บอกเราได้เลยว่าคุณกลัวอะไรที่สุด",
    multi: false,
    options: [
      "กลัวเสียเงินแล้วไม่ได้คืน",           // Drive 20: Avoid Loss
      "กลัวความปลอดภัยของตัวเอง/ครอบครัว",  // Drive 1: Survival
      "กลัวอาย/เสียหน้า/คนอื่นรู้",          // Drive 19: Avoid Shame
      "กลัวไม่มีใครช่วย/ถูกทิ้งให้สู้คนเดียว", // Drive 5: Belonging
      "โกรธ — อยากให้อีกฝ่ายได้รับโทษ",     // Drive 21: Revenge
      "กังวลเรื่องเวลา — กลัวทำไม่ทัน",      // Urgency signal
    ],
  },
  {
    id: "fear_urgency",
    title: "เรื่องนี้เพิ่งเกิดหรือเกิดมานานแล้ว?",
    rationale: "บางเรื่องต้องรีบทำภายใน 24 ชั่วโมง — เราจะช่วยให้คุณรู้ว่าต้องรีบแค่ไหน",
    multi: false,
    options: [
      "เพิ่งเกิดวันนี้/เมื่อกี้",            // ⚡ CRITICAL
      "ภายใน 1-3 วันที่ผ่านมา",            // ⚡ URGENT
      "ภายใน 1 สัปดาห์",                   // 🟡 IMPORTANT
      "เกิน 1 เดือนแล้ว",                   // 🟢 ROUTINE
    ],
  },
  {
    id: "fear_impact",
    title: "ถ้าแก้ปัญหานี้ไม่ได้ใน 1 เดือน จะเกิดอะไรขึ้น?",
    rationale: "ช่วยให้เราเข้าใจความรุนแรงและจัดลำดับความสำคัญให้คุณ",
    multi: false,
    options: [
      "จะเสียเงินจำนวนมาก",                 // Financial cascade
      "อาจถูกฟ้อง/ถูกจับ",                  // Legal cascade
      "ครอบครัวจะเดือดร้อน",               // Family impact
      "เสียชื่อเสียง/หน้าที่การงาน",         // Social impact
      "ไม่แน่ใจ — แค่อยากให้จบๆ",           // Unclear but anxious
    ],
  },
];
```

---

## 5. Source Registry Gap

The codebase has only **6 legal sources** (in `sources.ts`), and two categories (`family`, `accident`) have **zero sources**:

| Category | Sources Available | Sources Needed from Research |
|----------|------------------|------------------------------|
| labour | 2 | +3 (Social Security Act, Workers Compensation Act, Gender Equality Act) |
| consumer | 1 | +3 (Unfair Contract Terms Act, Food Act, Drug Act) |
| debt | 1 | +4 (Debt Collection Act, Anti-Loan Shark Decree, Bankruptcy Act, Credit Bureau Act) |
| housing | 1 | +3 (Land Code, Condominium Act, Land Allocation Act) |
| family | **0** ❌ | +5 (Civil Code Book 5 on Family, Book 6 on Inheritance, Child Protection Act, Adoption Act, Gender Equality Act) |
| accident | **0** ❌ | +3 (Road Accident Victim Protection Act, Land Traffic Act, Criminal Code s.390-391) |
| online_fraud | **No category** | +4 (Computer Crime Act, Criminal Code s.341-348, Anti-Money Laundering Act, Emergency Tech Crime Decree) |
| criminal_victim | **No category** | +4 (Criminal Code, Criminal Procedure Code, Victim Compensation Act, Witness Protection Act) |
| government | **No category** | +3 (Official Information Act, Administrative Procedure Act, Nationality Act) |
| insurance | **No category** | +3 (Civil Code Insurance Title, Life Insurance Act, Non-Life Insurance Act) |
| defamation | **No category** | +3 (Criminal Code s.326-333, Computer Crime Act, PDPA) |

**Total sources needed: ~38** (vs. 6 currently registered).

---

## 6. Concrete Recommendations

### Priority Matrix

| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 🔴 P0 | Add "Online Fraud" category with time-critical triage | Highest search volume; highest fear urgency; most time-sensitive legal actions | Medium |
| 🔴 P0 | Add urgency/fear calibration questions to ALL existing categories | Every case benefits; immediate UX improvement | Low |
| 🟡 P1 | Expand each existing category from 1→4 sub-problem types | Vastly more accurate AI analysis | Medium |
| 🟡 P1 | Add "Criminal Victim" and "Defamation" categories | High fear; drives immediate action | Medium |
| 🟢 P2 | Add "Insurance," "Government Services," "Property/Land" categories | Important but lower search volume | Medium |
| 🟢 P2 | Expand source registry from 6→~38 sources with proper citations | Anti-hallucination; builds trust | Medium-High |
| 🔵 P3 | Add human drive mapping behind each question for AI prompt enrichment | Better AI empathy; better prioritization | Low |

### 6.1 Implementation Path for Diagnosis Config

**Phase 1: Add Fear Layer (Week 1)**

Insert fear calibration questions between the category intake and the category-specific questions. This gives immediate psychology-aware triage without changing existing question flows.

```typescript
// New: Universal fear calibration added to EVERY category's question array
// as questions[0-2], pushing existing Q1-Q4 to Q3-Q6
const FEAR_CALIBRATION: DiagnosisQuestion[] = [
  {
    id: "fear_urgency",
    title: "เรื่องนี้เกิดขึ้นเมื่อไร?",
    rationale: "บางเรื่องต้องรีบดำเนินการภายใน 24 ชั่วโมง — คำตอบของคุณช่วยให้เราจัดลำดับความเร่งด่วนให้",
    multi: false,
    options: ["วันนี้/ภายใน 24 ชม.", "1-3 วันที่ผ่านมา", "ภายใน 1 สัปดาห์", "เกิน 1 สัปดาห์", "เกิน 1 เดือน"],
  },
  {
    id: "fear_drive",
    title: "คุณรู้สึกอย่างไรกับสถานการณ์นี้มากที่สุด?",
    rationale: "เราเข้าใจว่าเรื่องกฎหมายทำให้รู้สึกหลายอย่าง — บอกเราได้เลย",
    multi: false,
    options: [
      "กลัว — กังวลเรื่องความปลอดภัยหรือเงิน", 
      "อาย/เสียหน้า — ไม่อยากให้ใครรู้", 
      "โกรธ — อยากให้อีกฝ่ายได้รับผิด", 
      "สับสน — ไม่รู้ว่าต้องเริ่มตรงไหน",
      "กังวลเรื่องเวลา — กลัวทำไม่ทัน",
    ],
  },
  {
    id: "fear_impact",
    title: "อะไรจะเกิดขึ้นถ้าคุณไม่แก้เรื่องนี้?",
    rationale: "ช่วยให้เราประเมินความรุนแรงและแนะนำขั้นตอนที่เหมาะสม",
    multi: true,
    options: [
      "เสียเงินที่จ่ายไปแล้ว",
      "อาจต้องเสียเงินเพิ่ม",
      "ความปลอดภัยของผม/ครอบครัว",
      "เสียชื่อเสียงหรือหน้าที่การงาน",
      "ครอบครัว/คนรอบข้างจะเดือดร้อน",
      "อาจถูกฟ้องร้องหรือถูกดำเนินคดี",
    ],
  },
];
```

**Phase 2: Expand Categories (Weeks 1-2)**

Add 6 new categories and expand existing ones. Example for the highest-priority new category:

```typescript
online_fraud: {
  version: DIAGNOSIS_CONFIG_VERSION,
  category: "online_fraud",
  questions: [
    ...FEAR_CALIBRATION, // Universal fear layer
    {
      id: "fraud_type",
      title: "คุณถูกหลอกในรูปแบบไหน?",
      rationale: "แต่ละรูปแบบมีขั้นตอนการแก้ไขต่างกัน",
      multi: false,
      options: [
        "ซื้อของออนไลน์ — โอนเงินแล้วไม่ได้ของ",
        "Call Center — มีคนโทรมาแอบอ้างแล้วให้โอนเงิน",
        "ถูกแฮ็กบัญชีโซเชียล/Facebook/LINE",
        "ถูกหลอกลงทุน/แชร์ลูกโซ่",
        "ถูกหลอกให้กรอกข้อมูลส่วนตัว (Phishing)",
      ],
    },
    {
      id: "transfer_timing",
      title: "คุณโอนเงินไปเมื่อไร?",
      rationale: "ถ้าเพิ่งโอนภายใน 1-3 ชม. — เร่งอายัดบัญชีก่อน!",
      multi: false,
      options: [
        "ภายใน 1-3 ชม. ที่ผ่านมา (รีบที่สุด!)",
        "ภายใน 24 ชม.",
        "1-3 วันที่ผ่านมา",
        "เกิน 3 วันแล้ว",
      ],
    },
    {
      id: "has_receipt",
      title: "คุณมีหลักฐานการโอนเงินหรือไม่?",
      rationale: "สลิปโอนเป็นหลักฐานสำคัญในการอายัดบัญชี",
      multi: false,
      options: [
        "มี — สลิปโอน/Statement",
        "มีแต่ไม่ครบ — จำเลขบัญชีปลายทางได้",
        "โอนผ่านพร้อมเพย์ — ไม่รู้เลขบัญชีปลายทาง",
        "ไม่มีหลักฐานเลย",
      ],
    },
    {
      id: "evidence",
      title: "คุณมีหลักฐานอื่นอะไรอีก?",
      rationale: "เลือกได้มากกว่า 1 รายการ",
      multi: true,
      options: [
        "แคปหน้าจอแชท/การสนทนา",
        "URL/ลิงก์ของโพสต์หรือเว็บไซต์",
        "โปรไฟล์/Bัญชีผู้ขายหรือคนร้าย",
        "มีพยาน/คนอื่นที่ถูกหลอกด้วย",
        "แจ้งความไว้แล้ว",
      ],
    },
  ],
},
```

**Phase 3: Source Registry Expansion (Weeks 2-3)**

Add legal sources for all 12 categories. This enables the anti-hallucination citation system to work across all categories.

### 6.2 Quickest Wins (Can Ship This Week)

1. **Add `fear_urgency` question to all 6 existing categories** — Just asks "เมื่อไร?" with time brackets. The AI prompt can then inject "⚠️ This happened TODAY — prioritize urgent steps like account freeze over long-term legal action."

2. **Add `fear_drive` question** — "คุณรู้สึกอย่างไร?" — The AI can then tailor its response tone. A "โกรธ" user gets validation + channel-to-action messaging. An "อาย" user gets reassurance + privacy emphasis.

3. **Split Debt category** — Separate debtor and creditor paths. Currently mixing "ถูกทวงหนี้" (victim) and "ต้องการทวงหนี้" (enforcer) in one flow creates dangerous confusion.

4. **Add Online Fraud as category #7** — It's the single highest-volume missing category. Even a basic implementation catches the most common entry point.

### 6.3 Sample Fear-Aware AI Prompt Enhancement

Current prompt (from `runDiagnosisAnalysis`): Fact-based only.

Enhanced prompt fragment (injecting fear calibration results):

```
User Context:
- Legal Category: ${category}
- Time Since Incident: ${answers.fear_urgency} ${urgency === 'critical' ? '⚠️ CRITICAL — prioritize time-sensitive actions like account freeze (AOC 1441)' : ''}
- Primary Fear: ${answers.fear_drive} ${fear === 'shame' ? '— Use reassuring, non-judgmental tone. Emphasize privacy and that many people face this.' : ''} ${fear === 'anger' ? '— Validate their anger but channel it toward effective legal action, not retaliation.' : ''}
- Impact if Unresolved: ${answers.fear_impact}
- Primary Human Drives: ${mapFearToDrives(answers.fear_drive)} 
  ${drives.includes('survival') ? '— Frame actions as protecting what matters most' : ''}
  ${drives.includes('avoid_loss') ? '— Emphasize what they stand to LOSE by not acting vs. GAIN by acting' : ''}
  ${drives.includes('avoid_shame') ? '— Use language that removes self-blame: "สิ่งนี้เกิดกับคนจำนวนมาก คุณไม่ได้ผิดที่ถูกหลอก"' : ''}
```

---

## 7. Summary: What's Missing vs. What Exists

### Codebase Reality

```
diagnosis-config.ts
├── labour     (4 generic questions)
├── consumer   (4 generic questions)
├── debt       (4 generic questions — mixes creditor/debtor)
├── housing    (4 generic questions — rental only)
├── family     (4 generic questions)
└── accident   (4 generic questions)
 ─────────────────────────────────
 TOTAL: 6 categories, 24 questions, 0 fear signals
```

### Research Reality

```
Comprehensive Framework
├── 1. Online Fraud      (5 problems) ← MISSING
├── 2. Labour            (4 problems) ← EXISTS (surface only)
├── 3. Debt              (4 problems) ← EXISTS (confusing)
├── 4. Consumer          (4 problems) ← EXISTS (surface only)
├── 5. Property          (3 problems) ← MISSING
├── 6. Family            (5 problems) ← EXISTS (2 sub-types missing)
├── 7. Traffic/Accident  (3 problems) ← EXISTS (best coverage)
├── 8. Criminal Victim   (4 problems) ← MISSING
├── 9. Government        (3 problems) ← MISSING
├── 10. Rental/Housing   (3 problems) ← EXISTS (rental only)
├── 11. Insurance        (3 problems) ← MISSING
└── 12. Defamation       (4 problems) ← MISSING
────────────────────────────────────
TOTAL: 12 categories, 45 problems
+ 22 Human Drives mapped
+ Fear/urgency calibration
+ Time-critical triage
```

### Bottom Line

The codebase covers about **13% of the problem space** and **0% of the psychological space**. Adding the fear layer, expanding categories, and mapping human drives will transform the diagnosis from a legal fact-collector into a fear-aware triage system that meets citizens where they actually are: scared, confused, and unsure if the law can help them.

---

## Appendix: Files Referenced

| File | Location | Lines |
|------|----------|-------|
| `diagnosis-config.ts` | `D:\legalai-citizen-check\lib\legal\diagnosis-config.ts` | 237 |
| `sources.ts` | `D:\legalai-citizen-check\lib\legal\sources.ts` | 80 |
| `types.ts` | `D:\legalai-citizen-check\domain\types.ts` | 219 |
| `legal_problems_master_list.md` | `D:\hermes-bess-project\docs\` | 797 |
| `legal_problems_detailed_part1.md` | `D:\hermes-bess-project\docs\` | 1,096 |
| `legal_problems_detailed_part2.md` | `D:\hermes-bess-project\docs\` | 1,693 |
| `legal_problems_detailed_part3_crime.md` | `D:\hermes-bess-project\docs\` | 915 |
| `legal_problems_detailed_part3_gov_rental.md` | `D:\hermes-bess-project\docs\` | 883 |
| `legal_problems_detailed_part3_ins_def.md` | `D:\hermes-bess-project\docs\` | 1,842 |
| `22_แรงขับมนุษย์_คู่มือฉบับสมบูรณ์.md` | `D:\hermes-bess-project\docs\` | 1,004 |
