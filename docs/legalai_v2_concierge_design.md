# LegalAI V2 — End-to-End Legal Concierge Flow

> **Status:** Design — August 2026
> **Author:** LegalAI Thailand Team
> **Version:** concierge-v1-design

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Current State Analysis (V1)](#2-current-state-analysis-v1)
3. [Concierge Architecture Overview](#3-concierge-architecture-overview)
4. [The 8 Phases — Revenge Porn Walkthrough](#4-the-8-phases--revenge-porn-walkthrough)
   - [Phase 1: UNDERSTAND (Free)](#phase-1-understand)
   - [Phase 2: ANALYZE RIGHTS (Free)](#phase-2-analyze-rights)
   - [Phase 3: CHOOSE PATH (Free)](#phase-3-choose-path)
   - [Phase 4: JURISDICTION (Action Pack ฿299)](#phase-4-jurisdiction)
   - [Phase 5: DOCUMENTS (Action Pack ฿299)](#phase-5-documents)
   - [Phase 6: PREPARE (Case Plus ฿999)](#phase-6-prepare)
   - [Phase 7: FILE (Case Plus ฿999)](#phase-7-file)
   - [Phase 8: FOLLOW-UP (Case Plus ฿999)](#phase-8-follow-up)
5. [Generalization — All 12 Categories](#5-generalization--all-12-categories)
6. [Monetization & Package Gates](#6-monetization--package-gates)
7. [Technical Architecture](#7-technical-architecture)
8. [Data Models](#8-data-models)
9. [API Design](#9-api-design)
10. [AI Prompt Architecture](#10-ai-prompt-architecture)
11. [UI Component Library](#11-ui-component-library)
12. [Migration Path (V1 → V2)](#12-migration-path-v1--v2)
13. [Risks & Mitigations](#13-risks--mitigations)

---

## 1. Executive Summary

LegalAI V1 is a **diagnosis tool** — users answer questions, AI analyzes rights, and gets an action plan. It stops at "here's what you should do."

LegalAI V2 transforms into an **end-to-end legal concierge** that guides users from the moment something happens all the way through actual court filing, case tracking, and resolution.

### The Core Shift

| Dimension | V1 (Current) | V2 (Concierge) |
|-----------|-------------|----------------|
| Scope | Diagnosis only | Problem → Court filing |
| Depth | Rights summary + action plan | Document generation, court navigation, filing |
| Monetization | Single free tier + packages | Phase-gated (Free → ฿299 → ฿999) |
| User journey | 3-min wizard → analysis page | Guided 8-phase journey over days/weeks |
| Jurisdiction | Generic "Thailand" | Province → district → specific court/counter |
| Documents | Templates only | AI-generated, court-ready with filing instructions |
| Psychology | Basic drive detection | Per-phase emotional framing, loss-aversion hooks |
| Lawyer integration | Browse-only marketplace | Embedded: self-file vs lawyer decision engine |

### The Concierge Promise

> "Tell us what happened. We'll take you all the way to the courthouse door — and beyond."

---

## 2. Current State Analysis (V1)

### What V1 Does Well (KEEP)

1. **Drive detection engine** (`lib/legal/drive-detection.ts`) — 22 human drives, keyword matching, tone-mapped responses. Battle-tested and psychologically sound.
2. **Anti-hallucination source registry** (`lib/legal/sources.ts`) — 30+ vetted Thai legal sources, validated citations only.
3. **Category drive profiles** (`lib/legal/category-drives.ts`) — Emotional framing per category with gain/loss messaging.
4. **Package tier system** (`lib/packages/definitions.ts`) — Free/Action Pack/Case Plus/SME Starter with feature gates.
5. **Evidence readiness** — Explainable ratio (never a "win probability").

### What V1 Is Missing (BUILD)

1. **No jurisdiction awareness** — Says "file at labor office" but not WHICH one. No province/district mapping.
2. **No document generation pipeline** — Templates exist but no AI-powered fill, review, or court-formatting.
3. **No filing instructions** — No counter numbers, officer roles, fee schedules, or day-of guides.
4. **No case tracking** — Timeline is static mock data, not a living case management system.
5. **No path selection** — No structured self-file vs lawyer vs mediation decision engine.
6. **No phase-gated monetization** — Packages exist but aren't woven into the user journey.
7. **Static content** — Category pages are hardcoded. No per-phase dynamic content generation.

### Architectural Gaps

```
V1 Flow:
  Categories → Diagnosis Wizard → AI Analysis → Static Action Plan
  (3 minutes, 1 session)

V2 Flow:
  Incident → Understand → Rights → Choose Path → [PAYWALL]
  Jurisdiction → Documents → Prepare → File → Follow-up
  (Multi-session, days to weeks, state-persisted)
```

---

## 3. Concierge Architecture Overview

### The 8-Phase Journey

```
┌─────────────────────────────────────────────────────────────┐
│                    LEGALAI V2 CONCIERGE                      │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │ PHASE 1  │→│ PHASE 2  │→│ PHASE 3  │  FREE TIER         │
│  │UNDERSTAND│  │  RIGHTS  │  │CHOOSE PATH│ (diagnosis+)     │
│  └──────────┘  └──────────┘  └─────┬────┘                  │
│                                     │                        │
│              ┌──────────────────────┼──────────────────┐    │
│              │   SELF-FILE     │    LAWYER    │ MEDIATION│   │
│              └────────┬────────┘              │          │    │
│                       │                       │          │    │
│  ═════════════════════╪═══════════════════════╪═══════════  │
│  ║  PAYWALL ฿299     ↓                       ↓          ║   │
│  ║  ┌──────────┐  ┌──────────┐                          ║   │
│  ║  │ PHASE 4  │→│ PHASE 5  │  ACTION PACK             ║   │
│  ║  │JURISDICTN│  │ DOCUMENTS│                           ║   │
│  ║  └──────────┘  └────┬─────┘                          ║   │
│  ═══════════════════════╪═════════════════════════════════   │
│  ║  PAYWALL ฿999        ↓                                 ║  │
│  ║  ┌──────────┐  ┌──────────┐  ┌──────────┐            ║  │
│  ║  │ PHASE 6  │→│ PHASE 7  │→│ PHASE 8  │ CASE PLUS  ║  │
│  ║  │ PREPARE  │  │   FILE   │  │FOLLOW-UP │            ║  │
│  ║  └──────────┘  └──────────┘  └──────────┘            ║  │
│  ═══════════════════════════════════════════════════════    │
└─────────────────────────────────────────────────────────────┘
```

### State Machine

```
States:  INTAKE → UNDERSTANDING → RIGHTS_EXPLORED → PATH_CHOSEN
         → JURISDICTION_SET → DOCUMENTS_LISTED → PREPARING
         → READY_TO_FILE → FILED → TRACKING → RESOLVED

Transitions driven by user completing each phase.
State persisted in ConciergeSession (see Data Models §8).
```

### Key Design Principles

1. **Micro-step, never overwhelm** — Each phase has 3-7 micro-steps. User always knows where they are and what's next.
2. **Psychology-first, then law** — Every phase starts with drive-aware emotional framing before presenting legal content.
3. **Explainable, never predictive** — Never say "you'll win." Say "here's what the law says you can do, here's what you need."
4. **Jurisdiction-native** — Every actionable output (court, counter, officer) is specific to the user's actual location.
5. **Monetization at the value cliff** — Free phases build trust and demonstrate value. Paywall hits exactly when action becomes concrete (jurisdiction lookup, document generation, filing).

---

## 4. The 8 Phases — Revenge Porn Walkthrough

> **Template Case:** "แนน" (Nan), 24, discovers her ex-boyfriend posted intimate photos on Facebook and a Telegram group without consent. She wants them removed and wants to take legal action.

### Phase 1: UNDERSTAND

**Status:** FREE — entry point for all users.

#### Purpose
Transform a raw, emotional narrative into a structured legal case with category mapping and psychological profile.

#### Micro-Steps

**Step 1.1: Safety First (Drive: Survival)**
```
┌─────────────────────────────────────────┐
│ 🛡️ Before we begin — are you safe?      │
│                                         │
│ ○ I'm safe, let's proceed               │
│ ○ I'm not safe — I need help now        │
│   → Emergency contacts: 191, 1300       │
│   → OSCC hotline: 1300                  │
│   → Women's Foundation: 02-277-0491     │
└─────────────────────────────────────────┘
```

**Step 1.2: Narrative Intake (DeepSeek-powered)**
Instead of checkbox questions, use a guided narrative form:
- "Tell us what happened, in your own words"
- AI parses the narrative to extract: actors, platforms, timeline, content type, emotional state
- Follow-up clarifying questions generated by AI based on gaps

**Step 1.3: Category Confirmation**
AI proposes: "This sounds like **revenge porn / การเผยแพร่ภาพส่วนตัวโดยไม่ยินยอม** which falls under multiple legal frameworks:"
- Criminal: Computer Crime Act §16 (เผยแพร่ภาพอนาจารโดยไม่ยินยอม)
- Criminal: Criminal Code §326-328 (หมิ่นประมาท)
- Civil: Damages under Civil Code §420 (ละเมิด)
- Data: PDPA B.E. 2562
- User confirms or adjusts

**Step 1.4: Drive Profile Detection**
Reuse existing `detectDrives()` engine. For revenge porn:
- Primary: **avoid_shame** (0.95) + **revenge** (0.82) + **fairness** (0.78)
- Tone: "soothe" → "validate"
- Loss hook: "ถ้าไม่รีบจัดการ ภาพอาจแพร่กระจายวงกว้าง — จัดการอย่างเงียบๆ เรารักษาความลับของคุณ"

**Step 1.5: Urgency Triage**
```
┌─────────────────────────────────────────┐
│ ⚡ Urgency Assessment                    │
│                                         │
│ Images are still online: YES ⚡          │
│ Being shared actively: UNKNOWN          │
│ Identifiable in images: ASK             │
│ → Priority: HIGH — immediate takedown   │
│   + preservation of evidence            │
└─────────────────────────────────────────┘
```

**Step 1.6: Phase Summary**
```
📋 Case Profile Created:
   Category: Revenge Porn / Non-Consensual Intimate Images
   Primary Laws: Computer Crime Act §16, Criminal Code §326-328, PDPA
   Urgency: HIGH — images still online
   Your State: Angry, embarrassed, want justice
   
   Ready for Phase 2: Your Legal Rights →
```

#### Output Artifacts
- `ConciergeSession` created with `caseId`, `phase: "understanding"`
- Narrative stored (encrypted)
- Drive profile attached
- Category mapped (primary: defamation/revenge-porn, secondary: crime)

---

### Phase 2: ANALYZE RIGHTS

**Status:** FREE — builds trust and demonstrates legal depth.

#### Purpose
Show the user EXACTLY what the law allows them to do. This is the "knowledge is power" phase.

#### Micro-Steps

**Step 2.1: Your Rights Dashboard**

```
┌─────────────────────────────────────────────────────────────┐
│ ⚖️ YOUR LEGAL RIGHTS                                         │
│                                                              │
│ 🔴 CRIMINAL RIGHTS (Government prosecutes)                   │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ① File criminal complaint for Computer Crime Act §16    │ │
│ │    Penalty: Up to 5 years imprisonment, ฿100,000 fine   │ │
│ │    You need: Evidence of posting without consent         │ │
│ │    Against: The person who posted (ex-boyfriend)         │ │
│ │                                                         │ │
│ │ ② File criminal complaint for Defamation §326/328       │ │
│ │    Penalty: Up to 2 years + ฿200,000 fine (§328)        │ │
│ │    Statute of limitations: 3 MONTHS ⚡                   │ │
│ │    Against: The person who posted                       │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ 🟢 CIVIL RIGHTS (You sue for damages)                        │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ③ Sue for damages under Civil Code §420 (Tort)          │ │
│ │    You can claim:                                        │ │
│ │    - Actual damages (lost income, therapy costs)         │ │
│ │    - Moral damages (emotional distress)                  │ │
│ │    - Court costs                                          │ │
│ │    Typical range: ฿50,000 - ฿500,000                     │ │
│ │    Statute of limitations: 1 year from knowing           │ │
│ │                                                         │ │
│ │ ④ Sue under PDPA for data rights violation              │ │
│ │    - Right to erasure                                    │ │
│ │    - Right to damages                                    │ │
│ │    - PDPC complaint option                               │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ 🟡 PLATFORM RIGHTS (Immediate action)                        │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ⑤ Request takedown via platform (Facebook, Telegram)     │ │
│ │    - Facebook: Report → Non-consensual intimate images   │ │
│ │    - StopNCII.org: Global hash-blocking for NCII         │ │
│ │    - Telegram: Report → Violent/sexual content           │ │
│ │ ⑥ Request platform to preserve evidence before removal   │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Step 2.2: What You CAN Actually Do (Practical Rights)**
```
This phase filters "legal rights on paper" → "what you can actually achieve":
- ✅ Get images removed (within 24-48 hrs via platform tools + StopNCII.org)
- ✅ File criminal complaint at police station (requires evidence package)
- ✅ Sue for civil damages (requires lawyer or self-file)
- ⚠️ Get criminal conviction (depends on evidence quality, police diligence)
- ❌ Guarantee conviction (not in your control)
```

**Step 2.3: Timeline of Rights (Statute of Limitations)**
```
⏰ YOUR DEADLINES:
┌──────────────────────────────────────┐
│ TODAY      → StopNCII.org hash       │
│ 24 HOURS   → Report to platforms     │
│ 7 DAYS     → Preserve all evidence   │
│ 1 MONTH    → Consult lawyer (if using)│
│ 3 MONTHS ⚡ → FILE defamation case    │
│              (statute of limitations!) │
│ 1 YEAR     → File civil damages      │
│ 5 YEARS    → Computer Crime Act §16  │
└──────────────────────────────────────┘
```

**Step 2.4: Damage Calculator (Preliminary)**
```
🧮 ESTIMATED DAMAGES:
   Moral damages: ฿50,000 - ฿200,000
   Actual losses: _____ (your input)
   Legal costs: ฿5,000 - ฿50,000
   ───────────────────────────
   Estimated range: ฿55,000 - ฿250,000+

   ⚠️ This is an estimate, not a guarantee.
   Actual amounts determined by the court.
```

**Step 2.5: Phase Summary**
```
📊 RIGHTS ANALYSIS COMPLETE:
   5 rights identified across 3 domains (criminal, civil, platform)
   Strongest path: Computer Crime Act §16 (criminal) + Civil damages
   Time pressure: 3-month defamation deadline approaching
   
   Ready for Phase 3: Choose Your Path →
```

#### Output Artifacts
- `RightsAnalysis` object with categorized rights
- Statute of limitations calendar events
- Damage estimate range

---

### Phase 3: CHOOSE PATH

**Status:** FREE — the decision gate. Last free phase before paywall.

#### Purpose
Help the user choose between self-filing, hiring a lawyer, or mediation — with honest pros/cons, costs, and time estimates for each path.

#### Micro-Steps

**Step 3.1: Path Options Presentation**

```
┌─────────────────────────────────────────────────────────────┐
│ 🧭 CHOOSE YOUR PATH                                          │
│                                                              │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 🥋 PATH A: SELF-FILE (ดำเนินคดีด้วยตัวเอง)               │ │
│ │                                                         │ │
│ │ Cost: ฿0 - ฿5,000 (court fees only)                     │ │
│ │ Time: 10-20 hours of your time                          │ │
│ │ Complexity: Medium — we guide you step by step          │ │
│ │ Best if: You're comfortable with paperwork,             │ │
│ │          budget is tight, case is straightforward       │ │
│ │                                                         │ │
│ │ LegalAI Support:                                         │ │
│ │ ✅ AI-generated court documents                         │ │
│ │ ✅ Step-by-step filing instructions                     │ │
│ │ ✅ Evidence organization tools                          │ │
│ │ ✅ Court/counter location lookup                        │ │
│ │ ❌ No legal representation in court                     │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 👨‍⚖️ PATH B: LAWYER-ASSISTED (ใช้ทนายความ)               │ │
│ │                                                         │ │
│ │ Cost: ฿5,000 - ฿50,000+ depending on scope             │ │
│ │ Time: 2-5 hours of your time (lawyer does most work)    │ │
│ │ Complexity: Low — lawyer handles everything             │ │
│ │ Best if: You want professional representation,          │ │
│ │          case is complex, emotional distance needed     │ │
│ │                                                         │ │
│ │ LegalAI Support:                                         │ │
│ │ ✅ Matched to verified revenge porn specialists         │ │
│ │ ✅ Fixed-price service scopes (no surprise bills)       │ │
│ │ ✅ Document sharing with lawyer                         │ │
│ │ ✅ Case timeline tracking                               │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 🤝 PATH C: MEDIATION (ไกล่เกลี่ย)                        │ │
│ │                                                         │ │
│ │ Cost: ฿0 - ฿2,000 (mediation center fees)              │ │
│ │ Time: 1-3 sessions, 1-2 months                         │ │
│ │ Complexity: Low-Medium                                  │ │
│ │ Best if: You want to avoid court,                       │ │
│ │          ex-partner is willing to negotiate,            │ │
│ │          primary goal is image removal + apology        │ │
│ │                                                         │ │
│ │ LegalAI Support:                                         │ │
│ │ ✅ Mediation request letter template                    │ │
│ │ ✅ Preparation guide                                    │ │
│ │ ✅ Settlement agreement template                        │ │
│ │ ❌ No guarantee other party participates                │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Step 3.2: Guided Recommendation (AI-powered)**

Based on case details, AI generates a personalized recommendation:
```
🤖 OUR ASSESSMENT FOR YOUR CASE:

   Your case factors:
   - Images are explicit and identifiable → HIGH SEVERITY
   - Poster is identifiable (ex-boyfriend) → TRACEABLE
   - He refuses to remove → HOSTILE PARTY
   - Criminal act involved → STATE INTEREST

   Recommendation: PATH A (Self-File Criminal) + PATH B elements
   Start with criminal complaint. Add lawyer if police unresponsive.

   Why: Criminal charges carry serious penalties and police
   are obligated to investigate. Combine with civil damages
   once criminal case is filed.
```

**Step 3.3: Lawyer Marketplace (if Path B selected)**

```
👨‍⚖️ REVENGE PORN SPECIALISTS:

┌─────────────────────────────────────────┐
│ ทนายพิมพ์ชนก รัตนกุล ⭐ 5.0 (186 reviews)│
│ Specialty: Cyber crime, defamation      │
│ Experience: 15 years                    │
│ Languages: Thai, English                │
│                                         │
│ 📦 Scope: ปรึกษา + ตรวจเอกสาร + ยื่นฟ้อง  │
│ 💰 ฿15,000 (fixed, no hidden fees)      │
│ 📅 Available: This week                 │
│ [VIEW PROFILE] [REQUEST CONSULT]        │
├─────────────────────────────────────────┤
│ ทนายณัฐพงษ์ ศรีสวัสดิ์ ⭐ 4.8 (214)      │
│ Specialty: Criminal defense, cyber law  │
│ Experience: 9 years                     │
│ 💰 ฿8,000                               │
│ [VIEW PROFILE] [REQUEST CONSULT]        │
└─────────────────────────────────────────┘
```

**Step 3.4: Commitment**
```
📝 PATH SELECTED: Self-File
   
   By choosing self-file, LegalAI will:
   ✅ Find the correct court for your location
   ✅ List every document you need
   ✅ Generate your court documents
   ✅ Guide you through filing step-by-step
   ✅ Track your case deadlines
   
   Phases 1-3 complete (free). 
   Phases 4-8 require Action Pack (฿299) or Case Plus (฿999).
   
   [UNLOCK FULL CONCIERGE →]
```

#### Output Artifacts
- `PathChoice` recorded on `ConciergeSession`
- Lawyer match (if Path B)
- Package upsell trigger

---

### ═══════ PAYWALL: Action Pack ฿299 ═══════

**What the user sees:**

```
┌─────────────────────────────────────────────┐
│ 🔓 UNLOCK FULL LEGAL CONCIERGE               │
│                                              │
│ You've completed your free diagnosis.        │
│ To continue to court filing, you'll need:    │
│                                              │
│ ┌─────────────────────────────────────────┐  │
│ │ 🚀 ACTION PACK — ฿299 (one-time)        │  │
│ │                                         │  │
│ │ ✅ Phase 4: Jurisdiction Lookup          │  │
│ │ ✅ Phase 5: Complete Document List       │  │
│ │ ✅ Court-specific guidance               │  │
│ │ ✅ Evidence checklist with sources       │  │
│ │                                         │  │
│ │ Or get everything with:                  │  │
│ │                                         │  │
│ │ 💎 CASE PLUS — ฿999 (one-time)          │  │
│ │                                         │  │
│ │ ✅ Everything in Action Pack             │  │
│ │ ✅ Phase 6: AI Document Generation       │  │
│ │ ✅ Phase 7: Filing Day Guide             │  │
│ │ ✅ Phase 8: Case Tracking + Reminders    │  │
│ │ ✅ Priority support + document review    │  │
│ │ ✅ 3 lawyer consultations                │  │
│ └─────────────────────────────────────────┘  │
│                                              │
│ [GET ACTION PACK ฿299]  [GET CASE PLUS ฿999] │
│ [CONTINUE WITH FREE (limited)]               │
└─────────────────────────────────────────────┘
```

---

### Phase 4: JURISDICTION

**Status:** Action Pack (฿299) or Case Plus (฿999).

#### Purpose
Determine the EXACT court, police station, or filing venue based on the user's physical location and the nature of the case.

#### Micro-Steps

**Step 4.1: Location Intake**
```
📍 WHERE DID THIS HAPPEN?

   Important: Your case must be filed in the correct jurisdiction.
   We need to know:

   ① YOUR current province: [___________] ▼
      (กรุงเทพมหานคร, เชียงใหม่, ขอนแก่น, ...)
   
   ② YOUR district/เขต: [___________] ▼
      (depends on province selection)

   ③ Where did the posting happen?
      ○ I know the poster's location
      ○ I don't know — same as my location
      ○ The platform is based outside Thailand
   
   ④ Where are YOU located?
      ○ Same as where it happened
      ○ Different province (specify: ___________)

💡 For revenge porn: You can file at your local police station
   even if the poster is in another province. If you know where
   the poster is, you may also file there.
```

**Step 4.2: Jurisdiction Rules Engine**

For revenge porn, the jurisdiction engine applies these rules:
```typescript
// Jurisdiction rules for Computer Crime Act §16 cases:
// Rule 1: File where the victim resides (common practice)
// Rule 2: File where the crime occurred (poster's location)
// Rule 3: File where the content was accessed (victim's location at time of access)
// Rule 4: Cyber Crime Investigation Bureau (CCIB) for cross-province cases
// Rule 5: Technology Crime Suppression Division (TCSD) for serious cases
```

**Step 4.3: Court/Station Determination**

```
🏛️ YOUR FILING VENUES:

   Based on: กรุงเทพมหานคร, เขตจตุจักร

   ┌─────────────────────────────────────────────┐
   │ 🚔 POLICE STATION (Criminal Complaint)       │
   │                                              │
   │ สถานีตำรวจนครบาลพหลโยธิน                       │
   │ 📍 123 ถนนพหลโยธิน แขวงจตุจักร เขตจตุจักร        │
   │    กรุงเทพมหานคร 10900                        │
   │ 📞 02-513-XXXX                               │
   │ 🕐 Open: 24 hours                             │
   │                                              │
   │ OR (specialized cyber unit):                 │
   │ กองบังคับการปราบปรามการกระทำความผิด              │
   │ เกี่ยวกับอาชญากรรมทางเทคโนโลยี (บก.ปอท.)        │
   │ 📍 ศูนย์ราชการฯ ถนนแจ้งวัฒนะ หลักสี่ กทม.         │
   │ 📞 02-142-XXXX (Cyber crime hotline)          │
   │ 🕐 Mon-Fri 08:30-16:30                        │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ ⚖️ CRIMINAL COURT (After police investigation) │
   │                                              │
   │ ศาลอาญา                                        │
   │ 📍 ถนนรัชดาภิเษก แขวงจตุจักร เขตจตุจักร กทม.      │
   │ 📞 02-512-XXXX                               │
   │ 🕐 Mon-Fri 08:30-16:30                        │
   │ 💰 Filing fee: ฿200 (criminal complaint)      │
   └─────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────┐
   │ 💰 CIVIL COURT (Damages lawsuit)             │
   │                                              │
   │ ศาลแพ่ง                                        │
   │ 📍 ถนนรัชดาภิเษก แขวงจตุจักร เขตจตุจักร กทม.      │
   │ 📞 02-511-XXXX                               │
   │ 💰 Filing fee: 2% of claimed amount           │
   │    (max ฿200,000 for claims up to ฿50M)      │
   └─────────────────────────────────────────────┘
```

**Step 4.4: Venue-Specific Notes**
```
📝 LOCAL NOTES — ศาลอาญา รัชดา:
   • Most criminal cases accepted at counter 1-5
   • Bring 3 copies of all documents
   • Photocopy service available at basement (฿2/page)
   • Parking: Building B, ฿20/hour
   • Best time: 08:30-10:00 (less crowded)
   • Public transport: MRT พหลโยธิน station, exit 3
```

#### Output Artifacts
- `JurisdictionResult` with court/station details
- `FilingVenue` objects (police, criminal court, civil court)
- Local notes (venue-specific tips)
- Fee schedule

---

### Phase 5: DOCUMENTS

**Status:** Action Pack (฿299) or Case Plus (฿999).

#### Purpose
List EVERY document the user needs, exactly how to get each one, in the correct format and number of copies. This is the "shopping list" for legal readiness.

#### Micro-Steps

**Step 5.1: Complete Document Checklist**

```
📋 YOUR DOCUMENT CHECKLIST — REVENGE PORN CASE

   ╔═══════════════════════════════════════════════════════╗
   ║  PART 1: CRIMINAL COMPLAINT (แจ้งความ)                  ║
   ╠═══════════════════════════════════════════════════════╣
   ║  #   DOCUMENT              COPIES   HOW TO GET       ║
   ║ ──────────────────────────────────────────────────── ║
   ║ 1.1  บัตรประชาชน            3      Your wallet       ║
   ║ 1.2  สำเนาบัตรประชาชน        3      Photocopy shop    ║
   ║ 1.3  บันทึกประจำวัน (ถ้ามี)    3      Police station    ║
   ║ 1.4  หลักฐานภาพ/คลิป         3 sets Printed + USB     ║
   ║ 1.5  Screenshots (dated)    3 sets Print all          ║
   ║ 1.6  URL/links list         3      Copy from browser  ║
   ║ 1.7  พยานบุคคล (ชื่อ-ที่อยู่)   1      Ask friends       ║
   ║ 1.8  บันทึกการแจ้งแพลตฟอร์ม   1      Email from FB/TG  ║
   ╚═══════════════════════════════════════════════════════╝

   ╔═══════════════════════════════════════════════════════╗
   ║  PART 2: CIVIL LAWSUIT (ฟ้องแพ่ง) — Optional           ║
   ╠═══════════════════════════════════════════════════════╣
   ║ 2.1  คำฟ้องคดีแพ่ง         3+1      AI generates      ║
   ║ 2.2  บัญชีพยานหลักฐาน        3+1      AI generates      ║
   ║ 2.3  ใบรับรองแพทย์ (จิตใจ)    1      Hospital/Clinic   ║
   ║ 2.4  หลักฐานรายได้ที่เสียไป    1      Employer/payslip  ║
   ║ 2.5  ใบเสร็จค่ารักษา         1      Hospital/Clinic   ║
   ╚═══════════════════════════════════════════════════════╝

💡 TIP: "3 copies" means 1 original + 2 copies
   "3+1" means 3 for court + 1 to keep for yourself
```

**Step 5.2: How to Get Each Document (Acquisition Guide)**

For each document type, provide specific instructions:

```
📄 DOCUMENT 1.4: หลักฐานภาพ/คลิป (Evidence Images/Videos)

   HOW TO PREPARE:
   ① Take screenshots showing:
      - The image/video clearly visible
      - The URL/date/time visible
      - The poster's name/account visible
      - The platform interface visible

   ② Print in COLOR (3 copies, 4 images per page)
   
   ③ Save to USB drive with folder structure:
      USB:\evidence\
        ├── facebook_posts\ (screenshots)
        ├── telegram_posts\ (screenshots)
        ├── urls.txt (all links)
        └── timeline.pdf (chronological record)

   ④ Use StopNCII.org BEFORE removing content
      - This creates a hash fingerprint
      - Prevents re-upload across platforms
      - Provides timestamp evidence

   ⚠️ DO NOT just screenshot on your phone.
   Courts prefer printed, dated, organized evidence.
```

**Step 5.3: Evidence Preservation Timeline**
```
⏰ PRESERVATION CALENDAR:

   NOW ⚡
   ├── Take full-page screenshots (include URL bar, date/time)
   ├── Save all URLs to a text file
   ├── Use StopNCII.org to hash images
   └── Download copies of all posted content

   24 HOURS
   ├── Report to all platforms where content appears
   ├── Save confirmation emails/reference numbers
   └── Screenshot the report confirmations

   48 HOURS
   ├── Print all screenshots (color, 4/page)
   ├── Organize in chronological order
   └── Prepare USB drive with digital copies

   72 HOURS
   ├── NOTARIZE screenshots if possible (optional but strong)
   │   → Any law firm can do this (฿500-1,000)
   └── Prepare witness list (names, contact, what they saw)

   7 DAYS
   └── READY TO FILE — all evidence preserved
```

**Step 5.4: Document Templates Available**
```
📄 AVAILABLE AI-GENERATED DOCUMENTS (requires Case Plus ฿999):

   ┌─────────────────────────────────────────────────┐
   │ 📝 บันทึกประจำวัน (Daily Record)                   │
   │    → Template: report_daily_record_v2             │
   │    → Status: AI-ready, requires your details      │
   │    → [UPGRADE TO GENERATE]                        │
   │                                                   │
   │ 📝 คำร้องทุกข์ (Criminal Complaint)                │
   │    → Template: criminal_complaint_ncii_v1         │
   │    → Status: AI-ready                             │
   │    → [UPGRADE TO GENERATE]                        │
   │                                                   │
   │ 📝 คำฟ้องคดีแพ่ง (Civil Complaint)                 │
   │    → Template: civil_complaint_defamation_v1      │
   │    → Status: AI-ready                             │
   │    → [UPGRADE TO GENERATE]                        │
   │                                                   │
   │ 📝 บัญชีพยานหลักฐาน (Evidence List)                │
   │    → Template: evidence_list_standard_v1          │
   │    → Status: AI-ready                             │
   │    → [UPGRADE TO GENERATE]                        │
   │                                                   │
   │ 📝 หนังสือขอให้เก็บรักษาพยานหลักฐาน                   │
   │    (Evidence Preservation Request)                │
   │    → Template: evidence_preservation_v1           │
   │    → Status: AI-ready                             │
   └─────────────────────────────────────────────────┘
```

#### Output Artifacts
- `DocumentChecklist` array (all required documents)
- `AcquisitionGuide` for each document type
- `PreservationTimeline`
- `TemplateAvailability` map

---

### ═══════ PAYWALL: Case Plus ฿999 ═══════

*(If user only bought Action Pack, this is the second paywall. If they bought Case Plus initially, phases 6-8 unlock seamlessly.)*

---

### Phase 6: PREPARE

**Status:** Case Plus (฿999).

#### Purpose
Generate all court documents with AI, organize evidence, review everything, and prepare the user for filing day.

#### Micro-Steps

**Step 6.1: AI Document Generation Suite**

```
🤖 GENERATING YOUR COURT DOCUMENTS

   ┌─────────────────────────────────────────────┐
   │ 📝 Criminal Complaint (คำร้องทุกข์)           │
   │                                              │
   │ Status: GENERATING... ✓                       │
   │ AI using: DeepSeek v4-pro                     │
   │ Sources cited: Computer Crime Act §16,        │
   │   Criminal Code §326-328                      │
   │                                              │
   │ Preview:                                      │
   │ ┌─────────────────────────────────────────┐  │
   │ │ คำร้องทุกข์                               │  │
   │ │                                         │  │
   │ │ วันที่ ______ เดือน ______ พ.ศ. ______     │  │
   │ │                                         │  │
   │ │ ข้าพเจ้า น.ส. แนน ____ อายุ 24 ปี         │  │
   │ │ อยู่บ้านเลขที่ ___ แขวง ___ เขต ___       │  │
   │ │ กทม. ____ ขอแจ้งความร้องทุกข์ต่อ          │  │
   │ │ พนักงานสอบสวน สน. พหลโยธิน ดังนี้:       │  │
   │ │                                         │  │
   │ │ 1. เมื่อวันที่ ___ ผู้ต้องหาคือ           │  │
   │ │ นาย ___ (แฟนเก่า) ได้นำภาพถ่าย            │  │
   │ │ อนาจารของข้าพเจ้าไปเผยแพร่ทาง             │  │
   │ │ Facebook และ Telegram...                  │  │
   │ │                                         │  │
   │ │ [Continue reading — 2 more pages]       │  │
   │ └─────────────────────────────────────────┘  │
   │                                              │
   │ [EDIT DOCUMENT] [REGENERATE] [DOWNLOAD .docx] │
   └─────────────────────────────────────────────┘
```

**Step 6.2: AI Document Review**
```
🔍 AI DOCUMENT REVIEW

   Scanning your criminal complaint for issues...

   ✅ Legal basis correct: Computer Crime Act §16 cited properly
   ✅ Facts chronologically ordered
   ✅ Names/addresses in correct Thai legal format
   ⚠️ MISSING: Poster's full name and address (if known)
      → Suggestion: Add ID card number of ex-boyfriend if known
   ⚠️ UNCLEAR: Date of first posting
      → Please clarify exact date
   ✅ Evidence referenced correctly (6 items listed)
   ✅ Jurisdiction: สน.พหลโยธิน is correct for เขตจตุจักร

   Overall Score: 85/100 — ready with minor fixes
```

**Step 6.3: Evidence Vault**
```
📁 EVIDENCE VAULT — Organized for Filing

   ┌─────────────────────────────────────────────┐
   │ ✅ Screenshots (Facebook) — 12 images        │
   │    [VIEW] [REORDER] [DELETE]                 │
   │                                              │
   │ ✅ Screenshots (Telegram) — 4 images         │
   │    [VIEW] [REORDER] [DELETE]                 │
   │                                              │
   │ ✅ URL List — 8 URLs                        │
   │    [VIEW] [ADD URL]                          │
   │                                              │
   │ ⚠️ Medical Certificate — MISSING            │
   │    [ADD] [SKIP — not critical]              │
   │                                              │
   │ ⚠️ Platform Report Confirmations — MISSING  │
   │    [ADD] [USE TEMPLATE REQUEST]             │
   │                                              │
   │ ✅ Witness Contact List — 2 witnesses        │
   │    [VIEW] [ADD WITNESS]                     │
   └─────────────────────────────────────────────┘

   📊 READINESS: 4/6 evidence types complete (67%)
```

**Step 6.4: Witness Statement Builder**
```
👤 WITNESS STATEMENTS

   Witness 1: เพื่อนสนิท — เห็นภาพในกลุ่ม Telegram
   ┌─────────────────────────────────────────────┐
   │ 🤖 AI-generated draft:                       │
   │                                              │
   │ "ข้าพเจ้า น.ส. ___ อายุ ___ ปี อยู่บ้านเลขที่___│
   │ เมื่อวันที่ ___ เวลาประมาณ ___ น. ข้าพเจ้าได้   │
   │ เข้าใช้แอปพลิเคชัน Telegram และพบภาพของ       │
   │ คุณแนน ซึ่งเป็นเพื่อนของข้าพเจ้า ถูกโพสต์ใน    │
   │ กลุ่ม ___ โดยผู้ใช้ชื่อ ___ ..."                │
   │                                              │
   │ [EDIT] [SEND TO WITNESS FOR REVIEW]          │
   └─────────────────────────────────────────────┘
```

**Step 6.5: Filing Day Prep Checklist**
```
🎒 FILING DAY KIT:

   □ All documents printed (3+1 copies)
   □ USB drive with digital evidence
   □ Your ID card + copies
   □ Evidence envelope (organized, labeled)
   □ Court fee cash (exact amount: ฿200)
   □ Notebook + pen
   □ Phone (charged) + power bank
   □ Water bottle
   □ Snack (may take 2-4 hours)
   □ Comfortable clothes (no shorts/sleeveless)
   □ This guide (printed or on phone)

   📍 MEETING POINT: สน.พหลโยธิน, counter 3
   🕐 BEST TIME: Tuesday-Thursday, 08:30
   ⏱️ EXPECTED DURATION: 2-4 hours
```

#### Output Artifacts
- Complete set of AI-generated court documents (.docx + .pdf)
- Evidence vault with readiness score
- AI document review report
- Witness statements
- Filing day checklist

---

### Phase 7: FILE

**Status:** Case Plus (฿999).

#### Purpose
The exact, micro-step guide for filing day — what to do, where to go, who to talk to, what to say, and what to expect.

#### Micro-Steps

**Step 7.1: Pre-Filing Final Check**
```
✅ FINAL CHECK — Before You Leave Home

   □ All 3+1 document copies printed
   □ Evidence USB + printed evidence
   □ ID card + 3 copies
   □ ฿200 court fee (cash)
   □ Phone charged
   □ Know your case reference number: not yet assigned

   ⚠️ FINAL REMINDERS:
   • Dress modestly (no shorts, no tank tops, no flip-flops)
   • Leave valuables at home
   • Arrive 15 minutes before counter opens (08:15)
   • You CAN bring a support person (friend/family)
   • You CANNOT bring weapons, food, or large bags inside
```

**Step 7.2: Journey Guide (Turn-by-Turn)**
```
🗺️ YOUR FILING DAY JOURNEY:

   STEP 1: Travel to สน.พหลโยธิน
   ├── 🚇 MRT: พหลโยธิน station, Exit 3
   ├── 🚗 Drive: Building B parking, ฿20/hr
   └── Walk 200m to main entrance

   STEP 2: Enter the building
   ├── Security check at entrance (bag scan)
   ├── Tell guard: "มาแจ้งความครับ/ค่ะ"
   └── Get visitor badge

   STEP 3: Find the complaint counter
   ├── Go to 2nd floor
   ├── Counter 1-5: Criminal complaints
   ├── Look for sign: "รับแจ้งความ"
   └── Take queue number from machine

   STEP 4: When your number is called
   ├── Say: "ผม/ดิฉัน ต้องการแจ้งความร้องทุกข์
   │   คดีตาม พ.ร.บ. คอมพิวเตอร์ มาตรา 16"
   ├── Hand over: Criminal complaint document
   ├── Hand over: ID card + copies
   ├── Hand over: Evidence packet
   └── Officer will ask questions — answer honestly

   STEP 5: During the interview
   ├── The officer will type your statement
   ├── Read it carefully before signing
   ├── Ask to add anything missing
   ├── You'll sign each page
   └── Get your copy stamped

   STEP 6: After filing
   ├── Receive: Case number / เลขคดี
   ├── Receive: Investigating officer's name
   ├── Ask: "จะติดตามความคืบหน้าได้อย่างไร?"
   ├── Get officer's direct contact if possible
   └── Receive: Summons date (if applicable)

   STEP 7: Exit
   ├── Return visitor badge
   ├── Save case number in your phone
   └── Done! 🎉 You've officially filed.

   ⏱️ Total time: 2-4 hours
```

**Step 7.3: What to Say (Script)**
```
🗣️ FILING SCRIPT — What to Say

   OPENING:
   "สวัสดีครับ/ค่ะ ผม/ดิฉันต้องการแจ้งความร้องทุกข์
   คดีเผยแพร่ภาพอนาจารโดยไม่ยินยอม
   ตามพระราชบัญญัติคอมพิวเตอร์ มาตรา 16"

   WHEN ASKED "เกิดอะไรขึ้น":
   "เมื่อวันที่ [date] แฟนเก่าของผม/ดิฉัน ชื่อ [name]
   ได้นำภาพ [describe type] ของผม/ดิฉันไปโพสต์ใน [platform]
   โดยไม่ได้รับความยินยอม ทำให้ผม/ดิฉันได้รับความอับอาย
   และเสียหาย"

   WHEN ASKED "มีหลักฐานอะไร":
   "ผม/ดิฉันมีหลักฐานดังนี้:
   1. ภาพหน้าจอจาก Facebook จำนวน 12 ภาพ
   2. ภาพหน้าจอจาก Telegram จำนวน 4 ภาพ
   3. รายการ URL ทั้งหมด
   4. พยานบุคคล 2 คน
   ทั้งหมดพิมพ์และบันทึกใน USB นี้"

   WHEN ASKED "ต้องการให้ดำเนินการอย่างไร":
   "ต้องการให้ดำเนินคดีกับผู้โพสต์ตามกฎหมาย
   และขอให้มีการลบภาพออกจากทุกแพลตฟอร์ม"

   ⚠️ TIPS:
   • Speak clearly and calmly
   • Stick to facts, not emotions
   • If officer seems dismissive: politely reference
     Computer Crime Act §16 — this IS a crime
   • If asked "แน่ใจเหรอจะเอาเรื่อง":
     "ค่ะ/ครับ ดิฉัน/ผมต้องการดำเนินคดี"
```

**Step 7.4: What Could Go Wrong (Contingency Plans)**
```
⚠️ CONTINGENCY PLANS:

   SCENARIO A: Officer refuses to accept complaint
   → Politely ask for supervisor
   → Reference: "ตามประมวลกฎหมายวิธีพิจารณาความอาญา
     มาตรา 123 พนักงานสอบสวนต้องรับคำร้องทุกข์"
   → If still refused: Go to บก.ปอท. directly

   SCENARIO B: Officer says "ไม่น่ามีปัญหา"
   → "ถึงแม้จะเป็นเรื่องส่วนตัว แต่การเผยแพร่ภาพอนาจาร
     โดยไม่ยินยอมเป็นความผิดอาญา ตาม พ.ร.บ.คอมพิวเตอร์
     มาตรา 16 มีโทษจำคุกสูงสุด 5 ปี"

   SCENARIO C: Asked to "come back tomorrow"
   → Ask for specific time and officer name
   → Ask: "สามารถยื่นคำร้องทิ้งไว้ก่อนได้ไหม?"

   SCENARIO D: Evidence format rejected
   → Offer to provide additional copies
   → Photocopy service: basement, ฿2/page
   → Offer USB as alternative

   SCENARIO E: Language barrier (if filing outside Bangkok)
   → Use this Thai phrase: "ดิฉัน/ผมไม่ใช่คนไทย
     ขอความกรุณาช่วยอธิบายช้าๆ"
   → LegalAI generates documents in Thai
   → Bring a Thai-speaking friend if possible
```

**Step 7.5: Confirmation & Next Steps**
```
✅ FILING CONFIRMED!

   Case Number: คดีอาญาที่ ___/2569
   Police Station: สน.พหลโยธิน
   Investigating Officer: ร.ต.อ. ___
   Filing Date: [date]
   Next Expected Contact: Within 7-14 days

   📋 NEXT STEPS:
   ① Wait for police to summon the accused
   ② Police will interview both parties
   ③ Case forwarded to prosecutor (อัยการ)
   ④ Prosecutor files with Criminal Court
   ⑤ Court sets hearing date

   LegalAI will track all deadlines and remind you.
   
   [VIEW CASE TIMELINE →]
```

#### Output Artifacts
- Filing confirmation record
- Case number + officer details
- Timeline events created

---

### Phase 8: FOLLOW-UP

**Status:** Case Plus (฿999) — ongoing.

#### Purpose
Living case dashboard that tracks everything after filing — court dates, deadlines, contacts, and documents.

#### Micro-Steps

**Step 8.1: Living Case Dashboard**
```
┌─────────────────────────────────────────────────────────────┐
│ 📊 CASE: Revenge Porn — Computer Crime Act §16              │
│ Case #: คดีอาญาที่ ___/2569                                 │
│ Filed: 15 August 2569  |  Status: UNDER INVESTIGATION       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ⏱️ CASE TIMELINE                                            │
│                                                              │
│ ✅ 15 Aug  | Filed criminal complaint | สน.พหลโยธิน        │
│ ⏳ 22 Aug  | Police 1st follow-up call | CALL THEM           │
│ ⏳ 29 Aug  | Expected: Summons issued                        │
│ ⏳ ~15 Sep | Expected: Accused interview                     │
│ ⏳ ~30 Sep | Expected: Case to prosecutor                    │
│ ⏳ TBD     | Court hearing date                              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 📞 YOUR CONTACTS                                            │
│                                                              │
│ Investigating Officer: ร.ต.อ. ___                          │
│ 📱 08x-xxx-xxxx (call Mon-Fri 09:00-16:00)                 │
│                                                              │
│ Police Station: สน.พหลโยธิน                                 │
│ 📞 02-513-XXXX                                              │
│                                                              │
│ Your Lawyer: (none — self-filing)                           │
│ [FIND A LAWYER IF NEEDED]                                   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ ⚡ UPCOMING DEADLINES                                       │
│                                                              │
│ 🔴 22 Aug — เสียชีวิต: Call police for update               │
│    If no response by 22 Aug:                                │
│    → Call สน.พหลโยธิน                                       │
│    → Ask: "คดีหมายเลข ___ คืบหน้าอย่างไร"                   │
│                                                              │
│ 🟡 ~29 Aug — Expected summons issued                        │
│    → Prepare for possible confrontation with accused        │
│    → Review: Safety plan (see resources)                    │
│                                                              │
│ ⚪ ~15 Sep — Possible accused interview                     │
│    → You may be called to give additional statement         │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 📄 DOCUMENT STATUS                                          │
│                                                              │
│ ✅ Criminal complaint — FILED                               │
│ ✅ Evidence package — SUBMITTED                             │
│ ⚠️ Medical certificate — STILL MISSING (recommended)       │
│ □ Civil complaint — NOT YET FILED (deadline: 1 year)       │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 📝 CASE NOTES                                               │
│                                                              │
│ [15 Aug] Filed at counter 3. Officer was professional.      │
│ Took about 3 hours. Received case number immediately.       │
│                                                              │
│ [+ ADD NOTE]                                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Step 8.2: Deadline Reminders (LINE/Email/In-App)**
```
📱 REMINDER SYSTEM:

   Channels:
   ✅ In-app notifications
   ✅ Email (opt-in)
   ✅ LINE OA (opt-in, requires Case Plus)

   Reminder types:
   - 7 days before deadline: "⏰ เตรียมตัว..."
   - 3 days before deadline: "⚠️ ใกล้ถึงกำหนด..."
   - 1 day before deadline: "🔴 พรุ่งนี้! ..."
   - Day of: "📌 วันนี้! ..."
   - 1 day past: "⚠️ เลยกำหนด — ต้องดำเนินการ..."
```

**Step 8.3: Case Update Log**
```
📝 UPDATE YOUR CASE

   When something happens, log it here:

   ┌─────────────────────────────────────────┐
   │ Type: [Police Contact] [Court Date Set] │
   │       [Document Received] [Other]       │
   │                                         │
   │ Date: [___________]                     │
   │                                         │
   │ Notes:                                   │
   │ ┌─────────────────────────────────────┐ │
   │ │                                     │ │
   │ │                                     │ │
   │ └─────────────────────────────────────┘ │
   │                                         │
   │ Attach: [UPLOAD DOCUMENT/PHOTO]         │
   │                                         │
   │ [SAVE UPDATE]                           │
   └─────────────────────────────────────────┘
```

**Step 8.4: Escalation Triggers**
```
🚨 ESCALATION ASSISTANCE:

   If any of these happen, LegalAI guides you:

   ○ Police unresponsive > 14 days
     → Template: Follow-up letter to police
     → Escalate to: Police superintendent
     → Escalate to: บก.ปอท.

   ○ Accused counter-files
     → Urgent: Contact lawyer
     → Document all interactions
     → Do NOT respond directly

   ○ New images appear online
     → Immediate: StopNCII.org again
     → Report to platforms
     → Add to evidence
     → Update police

   ○ Court hearing scheduled
     → Phase 7-style courtroom guide
     → Witness preparation
     → Cross-examination tips

   ○ Prosecutor drops case
     → Alternative: Civil lawsuit
     → Alternative: Appeal to Attorney General
     → Alternative: File directly with court (§28)
```

**Step 8.5: Resolution & Closure**
```
🏁 CASE RESOLUTION

   When your case reaches resolution (any outcome):
   
   □ Criminal: Verdict received
   □ Civil: Judgment or settlement
   □ Platform: All content removed
   □ Emotional: Feeling resolved enough

   [MARK CASE AS RESOLVED]
   
   After resolution:
   ├── Final case report (PDF)
   ├── Document archive (encrypted)
   ├── Reflection: What would you tell others?
   └── Resource: Share your experience (anonymized, optional)
```

#### Output Artifacts
- `CaseDashboard` (live state)
- `ReminderSchedule`
- `CaseUpdateLog`
- `EscalationPath` triggers
- `ResolutionReport`

---

## 5. Generalization — All 12 Categories

### Category-to-Concierge Mapping

Each category has a unique concierge configuration that drives all 8 phases.

```typescript
type ConciergeCategoryConfig = {
  category: LegalCategory;
  
  // Phase 1: What narrative prompts to use
  narrativePrompts: string[];
  
  // Phase 2: Legal framework mapping
  legalFrameworks: {
    criminal: LawReference[];    // Criminal laws applicable
    civil: LawReference[];       // Civil laws applicable
    administrative: LawReference[]; // Admin/regulatory remedies
    platform: PlatformAction[];  // Takedown/report actions
  };
  
  // Phase 3: Path recommendations
  pathMatrix: {
    selfFile: PathOption;
    lawyer: PathOption;
    mediation: PathOption;
  };
  
  // Phase 4: Jurisdiction rules
  jurisdictionRules: JurisdictionRule[];
  
  // Phase 5: Required documents
  requiredDocuments: DocumentRequirement[];
  
  // Phase 6: AI document templates
  documentTemplates: DocumentTemplateRef[];
  
  // Phase 7: Filing procedures
  filingProcedures: FilingProcedure[];
  
  // Phase 8: Follow-up timeline defaults
  defaultTimeline: TimelineEvent[];
};
```

### Category-Specific Configurations

#### 1. LABOUR (แรงงาน)
```
Phase 1: "ถูกเลิกจ้าง? บังคับลาออก? ค้างค่าจ้าง?"
Phase 2: Labour Protection Act, Labour Court Act, Social Security Act
Phase 4: Jurisdiction = Labour Court in employee's work province
         OR Labour Protection Office (พนักงานตรวจแรงงาน)
Phase 5: Employment contract, payslips, termination letter, bank statements
Phase 7: Labour Court (ศาลแรงงาน) — no court fees for employees
```

#### 2. CONSUMER (ผู้บริโภค)
```
Phase 1: "ซื้ออะไร? จากไหน? จ่ายไปเท่าไหร่?"
Phase 2: Consumer Protection Act, Consumer Case Procedure Act
Phase 4: Consumer Court OR OCPB (สคบ.) — no court fees for consumers
Phase 5: Receipt, product photos, chat with seller, platform listing
Phase 7: Consumer Court — streamlined procedure, no lawyer required
```

#### 3. DEBT (หนี้สิน)
```
Phase 1: "เป็นเจ้าหนี้หรือลูกหนี้? จำนวนเท่าไหร่? ถูกทวงแบบไหน?"
Phase 2: Debt Collection Act, Civil Code (Debtor-Creditor), Bankruptcy Act
Phase 4: Civil Court where debtor resides
Phase 5: Loan agreement, transfer receipts, collection records
Phase 7: Civil Court — 2% filing fee on claim amount
```

#### 4. HOUSING (ที่อยู่อาศัย)
```
Phase 1: "เช่าหรือเป็นเจ้าของ? ปัญหาอะไร?"
Phase 2: Civil Code (Hire of Property / Property), Condominium Act
Phase 4: Civil Court where property is located
Phase 5: Lease agreement, rent receipts, photos, correspondence
```

#### 5. FAMILY (ครอบครัว)
```
Phase 1: "หย่า? มรดก? บุตร? ความรุนแรง?"
Phase 2: Civil Code Book V (Family), Book VI (Inheritance), Domestic Violence Act
Phase 4: Juvenile and Family Court (ศาลเยาวชนและครอบครัว)
         OR Civil Court for inheritance
Phase 5: Marriage certificate, birth certificates, will, property documents
```

#### 6. ACCIDENT (อุบัติเหตุ)
```
Phase 1: "เกิดอะไรขึ้น? เมื่อไหร่? ใครขับ?"
Phase 2: Traffic Act, Civil Code (Tort), Insurance Act
Phase 4: Police station where accident occurred
         OR Civil Court for damages
Phase 5: Police report, photos, insurance policy, medical certificate
```

#### 7. ONLINE FRAUD (ภัยออนไลน์)
```
Phase 1: "ถูกหลอกแบบไหน? โอนเงินไปเท่าไหร่? เมื่อไหร่?"
Phase 2: Criminal Code §341 (Fraud), Computer Crime Act, AMLO Act
Phase 4: Police station where victim resides
         OR CCIB (บก.ปอท.) for cross-province
         OR AOC 1441 (24-hour hotline)
Phase 5: Transfer slips, chat records, URLs, bank account numbers
Phase 7: CRITICAL — 1441 hotline within 24 hours for account freezing
```

#### 8. CRIME (เหยื่ออาชญากรรม)
```
Phase 1: "ปลอดภัยไหม? เกิดอะไรขึ้น?"
Phase 2: Criminal Code (various sections), Victim Compensation Act
Phase 4: Police station where crime occurred
Phase 5: Medical certificate, photos, witness statements
Phase 7: Police complaint → Investigation → Prosecutor → Criminal Court
```

#### 9. GOVERNMENT (ราชการ)
```
Phase 1: "หน่วยงานไหน? ปัญหาอะไร?"
Phase 2: Administrative Court Act, Government Liability Act
Phase 4: Administrative Court (ศาลปกครอง)
         OR Ombudsman (ผู้ตรวจการแผ่นดิน)
         OR Damrongtham Center (ศูนย์ดำรงธรรม 1567)
Phase 5: Filed requests, rejection letters, correspondence records
```

#### 10. INSURANCE (ประกันภัย)
```
Phase 1: "ประกันอะไร? ปฏิเสธเคลมเพราะอะไร?"
Phase 2: Insurance Act, Life Insurance Act, OIC Act
Phase 4: OIC (คปภ.) complaint first → Civil Court if not resolved
Phase 5: Policy document, claim form, rejection letter, medical records
```

#### 11. DEFAMATION (หมิ่นประมาท) — includes Revenge Porn
```
(Detailed above in §4 — the template case)
Primary sub-types:
  - Revenge porn / NCII → Computer Crime Act §16 + Criminal Code §326-328
  - Online defamation → §326-328 + Computer Crime Act
  - Data privacy breach → PDPA
  - Insults / harassment → §393 + §397
```

#### 12. PROPERTY (ที่ดิน/ทรัพย์สิน)
```
Phase 1: "ที่ดินแบบไหน? โฉนดหรือไม่? ปัญหาอะไร?"
Phase 2: Land Code, Civil Code Book IV (Property), Condominium Act
Phase 4: Civil Court where property is located
         OR Land Department (สำนักงานที่ดิน)
Phase 5: Title deed, survey documents, photos, boundary evidence
```

### Cross-Cutting Patterns

Every category shares these patterns:

1. **Safety Check** (Phase 1, Step 1) — Domestic violence, immediate danger, medical emergencies
2. **Statute of Limitations** (Phase 2) — Every category has time-critical deadlines
3. **Evidence Preservation** (Phase 5) — Screenshots, physical evidence, witness contacts
4. **Fee Transparency** (Phase 4, 7) — Exact costs, never hidden fees
5. **Escalation Paths** (Phase 8) — What to do when things go wrong

---

## 6. Monetization & Package Gates

### Package Structure (Extends V1)

```typescript
// Updated from lib/packages/definitions.ts
export type PackageId = "free" | "action_pack" | "case_plus" | "sme_starter";

// NEW: Concierge-phase feature gates
export const CONCIERGE_FEATURE_GATES: Record<string, PackageId> = {
  // Phase 1: Free
  "concierge:understand": "free",
  "concierge:safety_check": "free",
  "concierge:narrative_intake": "free",
  "concierge:drive_detection": "free",
  
  // Phase 2: Free
  "concierge:rights_analysis": "free",
  "concierge:damage_calculator": "free",
  "concierge:statute_reminders": "free",
  
  // Phase 3: Free
  "concierge:path_selection": "free",
  "concierge:lawyer_browse": "free",
  "concierge:path_recommendation": "free",
  
  // Phase 4: Action Pack
  "concierge:jurisdiction_lookup": "action_pack",
  "concierge:court_finder": "action_pack",
  "concierge:fee_calculator": "action_pack",
  
  // Phase 5: Action Pack
  "concierge:document_checklist": "action_pack",
  "concierge:acquisition_guide": "action_pack",
  "concierge:preservation_timeline": "action_pack",
  
  // Phase 6: Case Plus
  "concierge:document_generation": "case_plus",
  "concierge:ai_review": "case_plus",
  "concierge:evidence_vault": "case_plus",
  "concierge:witness_builder": "case_plus",
  
  // Phase 7: Case Plus
  "concierge:filing_guide": "case_plus",
  "concierge:filing_script": "case_plus",
  "concierge:contingency_plans": "case_plus",
  
  // Phase 8: Case Plus
  "concierge:case_dashboard": "case_plus",
  "concierge:deadline_reminders": "case_plus",
  "concierge:line_notifications": "case_plus",
  "concierge:escalation_assistance": "case_plus",
};
```

### The Paywall Experience

```
PHASE TRANSITION UX:

Free → Free → Free (build trust, demonstrate value)
         │
         ├── Natural break: "You've learned your rights
         │   and chosen a path. Ready to get specific?"
         │
         ▼
   PAYWALL 1 — Action Pack (฿299)
   "To find your exact court and get your document checklist..."
   ├── [UNLOCK FOR ฿299]
   ├── [GET CASE PLUS ฿999 — includes everything below]
   └── [CONTINUE WITH FREE (limited guidance)]

Action Pack → Action Pack (jurisdiction + documents)
         │
         ├── Natural break: "You know where to file
         │   and what you need. Ready to prepare?"
         │
         ▼
   PAYWALL 2 — Case Plus (฿999)
   "To generate your court documents and get filing guidance..."
   ├── [UPGRADE TO CASE PLUS ฿999]
   │   (already paid ฿299? Only ฿700 more)
   └── [STICK WITH ACTION PACK]

Case Plus → Case Plus → Case Plus (prepare → file → track)
```

### Pricing Psychology

| Principle | Implementation |
|-----------|---------------|
| **Anchoring** | Show ฿999 first, then ฿299 feels cheap |
| **Foot-in-door** | Free phases 1-3 create commitment |
| **Loss aversion** | "You've invested time. Don't stop now." |
| **Fairness** | "฿299 is less than 1 hour of lawyer time (฿800-1,500)" |
| **Social proof** | "X users filed their case this month with LegalAI" |
| **Urgency** | Statute of limitations countdown in UI |
| **Bundle value** | Case Plus includes lawyer consultation worth ฿2,400 |

### Revenue Model

```
Funnel (per 100 users):
  100 → Start Phase 1 (free)
   70 → Complete Phase 3 (free)
   25 → Purchase Action Pack (฿299)    → ฿7,475
   12 → Upgrade to Case Plus (฿700)    → ฿8,400
    8 → Purchase Case Plus directly    → ฿7,992
   ─────────────────────────────────────────
   Total: ~฿23,867 per 100 users
   ARPU: ~฿239
```

---

## 7. Technical Architecture

### Route Structure

```
/concierge/
├── page.tsx                         # Landing / resume session
├── [sessionId]/
│   ├── page.tsx                     # Session dashboard (redirects to current phase)
│   ├── phase-1-understand/
│   │   └── page.tsx                 # Narrative intake + drive detection
│   ├── phase-2-rights/
│   │   └── page.tsx                 # Rights analysis dashboard
│   ├── phase-3-path/
│   │   └── page.tsx                 # Path selection + lawyer matching
│   ├── phase-4-jurisdiction/
│   │   └── page.tsx                 # Location input + court finder
│   ├── phase-5-documents/
│   │   └── page.tsx                 # Document checklist + acquisition
│   ├── phase-6-prepare/
│   │   ├── page.tsx                 # Document generation hub
│   │   ├── documents/
│   │   │   └── [documentId]/page.tsx # Individual document editor
│   │   └── evidence/
│   │       └── page.tsx             # Evidence vault
│   ├── phase-7-file/
│   │   └── page.tsx                 # Filing guide + day-of prep
│   └── phase-8-followup/
│       └── page.tsx                 # Case dashboard + timeline
```

### API Routes

```
/api/concierge/
├── sessions/
│   ├── route.ts                     # POST (create), GET (list)
│   └── [sessionId]/
│       ├── route.ts                 # GET, PATCH, DELETE
│       ├── narrative/
│       │   └── route.ts             # POST — AI narrative analysis
│       ├── rights/
│       │   └── route.ts             # POST — AI rights analysis
│       ├── path/
│       │   └── route.ts             # POST — Path recommendation
│       ├── jurisdiction/
│       │   └── route.ts             # POST — Court/police lookup
│       ├── documents/
│       │   ├── checklist/
│       │   │   └── route.ts         # GET — Document checklist
│       │   └── generate/
│       │       └── route.ts         # POST — AI document generation
│       ├── evidence/
│       │   └── route.ts             # POST/GET evidence items
│       ├── filing/
│       │   └── route.ts             # POST — Filing guide, GET — status
│       └── followup/
│           ├── timeline/
│           │   └── route.ts         # GET/POST timeline events
│           └── reminders/
│               └── route.ts         # GET/POST reminder config
```

### Directory Structure (New Files)

```
lib/concierge/
├── types.ts                         # ConciergeSession, Phase data types
├── config/
│   ├── phases.ts                    # Phase definitions + ordering
│   ├── categories/                  # Per-category concierge configs
│   │   ├── defamation-revenge-porn.ts
│   │   ├── labour.ts
│   │   ├── consumer.ts
│   │   ├── debt.ts
│   │   ├── housing.ts
│   │   ├── family.ts
│   │   ├── accident.ts
│   │   ├── online-fraud.ts
│   │   ├── crime.ts
│   │   ├── government.ts
│   │   ├── insurance.ts
│   │   └── property.ts
│   └── index.ts                     # getConciergeConfig(category)
├── jurisdiction/
│   ├── thailand-courts.ts           # Court database (province → courts)
│   ├── police-stations.ts           # Police station database
│   ├── rules.ts                     # Jurisdiction rules engine
│   └── fees.ts                      # Court fee schedules
├── documents/
│   ├── templates/                   # Document templates (.docx base)
│   │   ├── criminal-complaint/
│   │   ├── civil-complaint/
│   │   ├── evidence-list/
│   │   ├── witness-statement/
│   │   └── mediation-request/
│   ├── generator.ts                 # AI document generation orchestrator
│   ├── review.ts                    # AI document review
│   └── merge-engine.ts             # Template + user data → filled doc
├── ai/
│   ├── narrative-parser.ts          # Phase 1: narrative → structured data
│   ├── rights-analyzer.ts           # Phase 2: case → legal rights
│   ├── path-advisor.ts             # Phase 3: case → path recommendation
│   ├── document-generator.ts       # Phase 6: AI document creation
│   └── filing-assistant.ts         # Phase 7: venue-specific guidance
├── packages/
│   └── concierge-gate.ts           # Phase access control
└── state/
    └── session-store.ts             # ConciergeSession persistence
```

---

## 8. Data Models

### ConciergeSession

```typescript
export type ConciergePhase =
  | "understand"
  | "rights"
  | "path"
  | "jurisdiction"
  | "documents"
  | "prepare"
  | "file"
  | "followup";

export type ConciergeSession = {
  id: string;
  userId: string;
  category: LegalCategory;
  
  // Phase tracking
  currentPhase: ConciergePhase;
  completedPhases: ConciergePhase[];
  phaseProgress: Record<ConciergePhase, number>; // 0-100 per phase
  
  // Phase 1: Understand
  narrative?: {
    rawText: string;
    aiSummary: string;
    actors: Actor[];
    timeline: NarrativeEvent[];
    categoryConfirmation: CategoryConfirmation;
    driveProfile: DriveProfile;
    urgencyLevel: "low" | "medium" | "high" | "critical";
  };
  
  // Phase 2: Rights
  rightsAnalysis?: {
    criminalRights: LegalRight[];
    civilRights: LegalRight[];
    platformRights: LegalRight[];
    statuteDeadlines: StatuteDeadline[];
    damageEstimate: DamageEstimate;
  };
  
  // Phase 3: Path
  pathChoice?: {
    selectedPath: "self_file" | "lawyer" | "mediation";
    lawyerMatch?: LawyerMatch;
    aiRecommendation: string;
    confidenceLevel: number;
  };
  
  // Phase 4: Jurisdiction
  jurisdiction?: {
    userProvince: string;
    userDistrict: string;
    venue: FilingVenue[];
    applicableRules: JurisdictionRule[];
  };
  
  // Phase 5: Documents
  documentPlan?: {
    checklist: DocumentRequirement[];
    acquisitionGuides: Record<string, AcquisitionGuide>;
    preservationTimeline: PreservationStep[];
    availableTemplates: TemplateRef[];
  };
  
  // Phase 6: Prepare
  preparation?: {
    generatedDocuments: GeneratedDocument[];
    evidenceVault: EvidenceItem[];
    witnessStatements: WitnessStatement[];
    aiReviewReport: DocumentReview[];
    filingKit: FilingKitItem[];
  };
  
  // Phase 7: File
  filing?: {
    filingDate?: string;
    caseNumber?: string;
    investigatingOfficer?: string;
    policeStation?: string;
    filingConfirmation: FilingConfirmation;
  };
  
  // Phase 8: Follow-up
  followUp?: {
    timeline: CaseTimelineEvent[];
    reminders: ReminderConfig[];
    contacts: CaseContact[];
    updates: CaseUpdate[];
    escalationTriggers: EscalationTrigger[];
  };
  
  // Metadata
  packageTier: PackageId;
  createdAt: string;
  updatedAt: string;
  resolvedAt?: string;
};
```

### Key Supporting Types

```typescript
export type LegalRight = {
  id: string;
  type: "criminal" | "civil" | "platform" | "administrative";
  title: string;
  description: string;
  lawReference: LegalSource;
  penaltyRange?: string;        // e.g. "Up to 5 years, ฿100,000 fine"
  statuteOfLimitations?: string; // e.g. "3 months"
  actionableBy: "self" | "police" | "lawyer" | "platform";
  difficulty: "easy" | "medium" | "hard";
  estimatedTime: string;
};

export type FilingVenue = {
  type: "police_station" | "criminal_court" | "civil_court" | 
        "administrative_court" | "labour_court" | "consumer_court" |
        "juvenile_court" | "specialized_unit";
  name: string;
  address: string;
  phone: string;
  hours: string;
  counterInfo: string;
  fees: FeeSchedule;
  localNotes: string;
  transportGuide: string;
};

export type DocumentRequirement = {
  id: string;
  title: string;
  description: string;
  copiesNeeded: number;
  format: string;           // "physical" | "digital" | "both"
  critical: boolean;        // Can't file without this
  acquisitionMethod: string;
  templateAvailable: boolean;
  templateId?: string;
};

export type FilingGuide = {
  steps: FilingStep[];      // Turn-by-turn instructions
  script: string;            // What to say
  contingencyPlans: ContingencyPlan[];
  kit: FilingKitItem[];
  duration: string;          // Expected time
};
```

---

## 9. API Design

### Narrative Analysis (Phase 1)

```
POST /api/concierge/sessions/:sessionId/narrative

Request:
{
  "narrative": "แฟนเก่าโพสต์รูปลับของฉันใน Facebook และ Telegram...",
  "category": "defamation"
}

Response:
{
  "summary": "Your ex-boyfriend posted intimate photos without consent...",
  "detectedCategory": "defamation",  // AI-confirmed
  "subCategory": "revenge_porn",
  "actors": [
    { "role": "victim", "name": "คุณ", "relationship": null },
    { "role": "perpetrator", "name": "แฟนเก่า", "relationship": "ex-partner" }
  ],
  "platforms": ["Facebook", "Telegram"],
  "timeline": [
    { "event": "First posting", "date": "2026-08-10", "certainty": "high" }
  ],
  "driveProfile": {
    "primary": "avoid_shame",
    "scores": { "avoid_shame": 0.95, "revenge": 0.82, "fairness": 0.78 },
    "labels": ["😰 หลีกเลี่ยงความอับอาย", "🔥 แก้แค้น/ทวงคืน", "⚖️ ยุติธรรม/ถูกต้อง"],
    "tone": "soothe",
    "lossHook": "ถ้าไม่รีบจัดการ ภาพอาจแพร่กระจาย..."
  },
  "urgency": "high",
  "clarifyingQuestions": [
    "คุณรู้ชื่อ-นามสกุลจริงของแฟนเก่าหรือไม่?",
    "ภาพยังออนไลน์อยู่ตอนนี้หรือไม่?"
  ]
}
```

### Rights Analysis (Phase 2)

```
POST /api/concierge/sessions/:sessionId/rights

Request:
{
  "narrativeData": { ... },  // From Phase 1
  "category": "defamation",
  "subCategory": "revenge_porn"
}

Response:
{
  "rights": [
    {
      "id": "criminal-computer-crime-16",
      "type": "criminal",
      "title": "แจ้งความดำเนินคดีอาญา ตาม พ.ร.บ.คอมพิวเตอร์ มาตรา 16",
      "description": "เผยแพร่ภาพอนาจารโดยไม่ยินยอม เป็นความผิดอาญา...",
      "lawReference": { "id": "computer-crime-act-16", ... },
      "penaltyRange": "จำคุกสูงสุด 5 ปี ปรับสูงสุด 100,000 บาท",
      "statuteOfLimitations": "5 ปี",
      "actionableBy": "police",
      "difficulty": "medium",
      "estimatedTime": "1-6 เดือน (จนถึงศาล)"
    },
    // ... more rights
  ],
  "statuteDeadlines": [
    { "rightId": "civil-defamation", "deadline": "2026-11-10", "daysRemaining": 82 },
    { "rightId": "criminal-defamation-328", "deadline": "2026-11-10", "daysRemaining": 82 }
  ],
  "damageEstimate": {
    "moralDamages": { "min": 50000, "max": 200000 },
    "actualLosses": { "min": 0, "max": 0 },
    "legalCosts": { "min": 5000, "max": 50000 },
    "totalRange": { "min": 55000, "max": 250000 }
  }
}
```

### Jurisdiction Lookup (Phase 4)

```
POST /api/concierge/sessions/:sessionId/jurisdiction

Request:
{
  "province": "กรุงเทพมหานคร",
  "district": "เขตจตุจักร",
  "caseType": "revenge_porn",
  "pathChoice": "self_file"
}

Response:
{
  "venues": [
    {
      "type": "police_station",
      "name": "สถานีตำรวจนครบาลพหลโยธิน",
      "address": "123 ถนนพหลโยธิน แขวงจตุจักร เขตจตุจักร กรุงเทพมหานคร 10900",
      "phone": "02-513-XXXX",
      "hours": "24 ชั่วโมง",
      "counterInfo": "เคาน์เตอร์ 1-5 รับแจ้งความ",
      "fees": { "complaint": 0, "copies": "฿2/page" },
      "localNotes": "ที่จอดรถ: อาคาร B ฿20/ชม. MRT พหลโยธิน ทางออก 3",
      "transportGuide": "🚇 MRT พหลโยธิน ทางออก 3 → เดิน 200m"
    },
    {
      "type": "specialized_unit",
      "name": "กองบังคับการปราบปรามการกระทำความผิดเกี่ยวกับอาชญากรรมทางเทคโนโลยี (บก.ปอท.)",
      ...
    }
  ],
  "applicableRules": [
    "ผู้เสียหายสามารถแจ้งความได้ที่สถานีตำรวจท้องที่ที่ตนอยู่",
    "คดีคอมพิวเตอร์สามารถแจ้งที่ บก.ปอท. ได้โดยตรง"
  ]
}
```

### Document Generation (Phase 6)

```
POST /api/concierge/sessions/:sessionId/documents/generate

Request:
{
  "templateId": "criminal-complaint-ncii-v1",
  "userData": {
    "fullName": "น.ส. แนน ...",
    "address": "...",
    "incidentDate": "2026-08-10",
    "perpetratorName": "นาย ...",
    "platforms": ["Facebook", "Telegram"],
    "evidenceList": [...]
  }
}

Response:
{
  "documentId": "doc-xyz",
  "status": "generated",
  "title": "คำร้องทุกข์ — คดีเผยแพร่ภาพอนาจาร",
  "format": "docx",
  "downloadUrl": "/api/documents/doc-xyz/download",
  "previewHtml": "<p>คำร้องทุกข์...</p>",
  "aiReview": {
    "score": 85,
    "issues": [
      { "severity": "warning", "message": "MISSING: Poster's full name" }
    ],
    "suggestions": [
      "Add ID card number of perpetrator if known"
    ]
  },
  "sourcesCited": ["computer-crime-act-16", "criminal-code-326"]
}
```

---

## 10. AI Prompt Architecture

### Prompt Strategy

Each concierge phase has a dedicated AI prompt with:
1. **Role definition** — What the AI is in this phase
2. **Input context** — What the AI receives
3. **Output schema** — Structured JSON response format
4. **Constraints** — Legal boundaries, anti-hallucination, no outcome predictions
5. **Drive awareness** — Tone instructions from detected drive profile

### Phase 1: Narrative Parser Prompt

```
System: คุณเป็นนักกฎหมายไทยผู้เชี่ยวชาญการรับฟังเรื่องราว
หน้าที่ของคุณ:
- อ่านเรื่องราวที่ผู้ใช้เล่าและสกัดข้อมูลสำคัญ
- จัดหมวดหมู่ทางกฎหมายที่เกี่ยวข้อง
- ประเมินความเร่งด่วน
- ถามคำถามที่จำเป็นเพื่อเติมข้อมูลที่ขาด
- ห้ามตัดสินหรือแสดงความคิดเห็นส่วนตัว
- ห้ามให้คำมั่นว่าจะชนะคดี

Input: narrative text + category hint + drive profile

Output: {
  "summary": "สรุป 2-3 ประโยค",
  "detectedCategory": "legal category",
  "subCategory": "specific sub-type",
  "actors": [{role, description, relationship}],
  "platforms": ["platform names involved"],
  "timeline": [{event, date, certainty}],
  "urgency": "low|medium|high|critical",
  "clarifyingQuestions": ["questions needed"]
}
```

### Phase 2: Rights Analyzer Prompt

```
System: คุณเป็นที่ปรึกษากฎหมายไทยของ LegalAI
หน้าที่:
- วิเคราะห์สิทธิทางกฎหมายที่ผู้ใช้มี จากข้อเท็จจริงที่ให้
- แบ่งสิทธิเป็น: อาญา, แพ่ง, ปกครอง, แพลตฟอร์ม
- ระบุกฎหมายที่เกี่ยวข้อง (ใช้เฉพาะ sources ที่กำหนด)
- คำนวณกรอบค่าเสียหายเบื้องต้น
- เตือนอายุความที่สำคัญ
- ห้ามบอกว่าผู้ใช้จะชนะคดี
- ห้ามประเมินโอกาสทางคดีเป็นเปอร์เซ็นต์

Input: narrative data + category + drive profile

Output: {
  "rights": [{type, title, description, lawReference, penaltyRange, 
              statuteOfLimitations, actionableBy, difficulty, estimatedTime}],
  "statuteDeadlines": [{rightId, deadline, daysRemaining}],
  "damageEstimate": {moralDamages, actualLosses, legalCosts, totalRange}
}
```

### Phase 6: Document Generator Prompt

```
System: คุณเป็นนักกฎหมายไทยผู้เชี่ยวชาญการร่างเอกสารศาล
หน้าที่:
- ร่างเอกสารทางกฎหมายตามแม่แบบที่กำหนด
- ใช้ข้อมูลที่ผู้ใช้ให้มาอย่างถูกต้อง
- อ้างอิงกฎหมายที่เกี่ยวข้องให้ถูกต้อง
- จัดรูปแบบตามมาตรฐานศาลไทย
- ใช้ภาษาไทยทางการที่ถูกต้อง
- แสดงผลเป็น markdown ที่สามารถแปลงเป็น .docx ได้
- ห้ามแต่งข้อมูลที่ผู้ใช้ไม่ได้ให้

Document templates per category stored in lib/concierge/documents/templates/
```

### Safety Constraints (All Phases)

Every AI prompt includes these constraints:

```
- ❌ ห้ามให้คำมั่นว่าจะชนะคดี
- ❌ ห้ามประเมินโอกาสชนะเป็นตัวเลขหรือเปอร์เซ็นต์
- ❌ ห้ามอ้างกฎหมายหรือแหล่งอ้างอิงที่ไม่มีในระบบ
- ❌ ห้ามให้คำแนะนำที่ผิดกฎหมาย
- ❌ ห้ามสนับสนุนให้ใช้ความรุนแรง
- ✅ แนะนำให้ปรึกษาทนายความสำหรับเคสซับซ้อน
- ✅ ใช้ "ความพร้อมของข้อมูล/หลักฐาน" แทนคำว่ามีโอกาสชนะ
- ✅ ระบุข้อจำกัดของ AI อย่างชัดเจนทุกครั้ง
- ✅ แสดงข้อความ "นี่ไม่ใช่คำปรึกษาทางกฎหมาย" ในทุกเฟส
```

---

## 11. UI Component Library

### New Components Needed

```
components/concierge/
├── PhaseIndicator.tsx         # Visual progress through 8 phases
├── PhaseContainer.tsx         # Wrapper for each phase with consistent layout
├── NarrativeInput.tsx         # Free-text narrative intake (Phase 1)
├── SafetyCheck.tsx            # Safety-first prompt (Phase 1, Step 1)
├── DriveProfileCard.tsx       # Shows detected drives + emotional framing
├── UrgencyBadge.tsx           # Critical/High/Medium/Low urgency indicator
├── RightsCard.tsx             # Individual legal right display
├── RightsDashboard.tsx        # Phase 2: full rights overview
├── StatuteCountdown.tsx       # Live countdown to statute of limitations
├── DamageCalculator.tsx       # Interactive damage estimate (Phase 2)
├── PathSelector.tsx           # Phase 3: self-file vs lawyer vs mediation
├── LawyerMatchCard.tsx        # Lawyer recommendation card
├── LocationPicker.tsx         # Province → District cascading picker (Phase 4)
├── CourtCard.tsx              # Court/police station info card (Phase 4)
├── DocumentChecklist.tsx      # Phase 5: interactive document checklist
├── AcquisitionGuide.tsx       # How to get each document
├── PreservationTimeline.tsx   # Evidence preservation countdown
├── DocumentEditor.tsx         # Phase 6: AI-generated document editor
├── EvidenceVault.tsx          # Drag-drop evidence organizer
├── WitnessBuilder.tsx         # Witness statement generator
├── FilingGuide.tsx            # Phase 7: turn-by-turn filing instructions
├── FilingScript.tsx           # Interactive "what to say" script
├── ContingencyPanel.tsx       # What-if scenarios
├── CaseDashboard.tsx          # Phase 8: living case dashboard
├── CaseTimeline.tsx           # Visual timeline with status
├── ReminderConfig.tsx         # Deadline reminder settings
├── EscalationAssistant.tsx    # Guided escalation paths
├── PaywallGate.tsx            # Phase-locked content with upsell
└── ConciergeProgress.tsx      # Overall journey progress bar
```

### Design System Extensions

```css
/* Concierge-specific design tokens */
:root {
  --concierge-phase-active: #3B82F6;
  --concierge-phase-complete: #10B981;
  --concierge-phase-locked: #9CA3AF;
  --concierge-urgency-critical: #EF4444;
  --concierge-urgency-high: #F59E0B;
  --concierge-urgency-medium: #3B82F6;
  --concierge-urgency-low: #6B7280;
  --concierge-paywall-border: #F59E0B;
  --concierge-paywall-bg: rgba(245, 158, 11, 0.05);
}
```

---

## 12. Migration Path (V1 → V2)

### Phase 1: Foundation (Weeks 1-2)
- [ ] Create `lib/concierge/` directory structure
- [ ] Define `ConciergeSession` types
- [ ] Build `PhaseIndicator` and `PhaseContainer` components
- [ ] Implement `ConciergeProgress` component
- [ ] Set up `/concierge/` route structure (scaffolding)

### Phase 2: Free Tier (Weeks 3-5)
- [ ] Build Phase 1: Narrative intake + safety check + drive detection
- [ ] Build Phase 2: Rights analysis — migrate from existing diagnosis
- [ ] Build Phase 3: Path selection + lawyer matching
- [ ] Build `PaywallGate` component
- [ ] Connect to existing AI pipeline (`lib/ai/diagnosis.ts`)

### Phase 3: Action Pack (Weeks 6-8)
- [ ] Build Thailand court database (`lib/concierge/jurisdiction/`)
- [ ] Build Phase 4: Jurisdiction lookup with location picker
- [ ] Build Phase 5: Document checklist + acquisition guides
- [ ] Integrate with existing package gate (`lib/packages/`)
- [ ] Payment integration (PromptPay / credit card)

### Phase 4: Case Plus (Weeks 9-12)
- [ ] Build document template engine (`lib/concierge/documents/`)
- [ ] Build Phase 6: AI document generation + review + evidence vault
- [ ] Build Phase 7: Filing guide, scripts, contingency plans
- [ ] Build Phase 8: Case dashboard, timeline, reminders, escalation

### Phase 5: Launch & Iterate (Weeks 13-16)
- [ ] Complete per-category concierge configs (all 12 categories)
- [ ] LINE OA integration for reminders
- [ ] Lawyer marketplace integration
- [ ] Analytics + conversion tracking
- [ ] User testing + iteration

---

## 13. Risks & Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| **AI hallucinates court procedures** | HIGH | Every venue-specific detail validated against court database. AI only fills user-specific fields. |
| **Wrong jurisdiction advice** | HIGH | Jurisdiction rules engine is rule-based, not AI. AI only formats output. Database curated by Thai lawyers. |
| **User misunderstands self-file complexity** | MEDIUM | Phase 3 clearly states complexity + time commitment. Prominent "consider a lawyer" nudge for complex cases. |
| **Statute of limitations missed** | HIGH | Multiple redundant reminders (in-app, email, LINE). Countdown timer visible in dashboard. LegalAI cannot guarantee user will act. |
| **Document generated with legal errors** | MEDIUM | AI document review pass before download. Disclaimer: "Not a substitute for lawyer review." Case Plus includes 3 lawyer consultations. |
| **Payment friction kills conversion** | MEDIUM | Free phases 1-3 build commitment before paywall. Multiple payment methods (PromptPay, card, mobile banking). ฿299 is 1/3 of 1-hour lawyer cost. |
| **Scope creep — too many categories** | MEDIUM | Launch with revenge porn + online fraud + labour (3 highest-traffic). Add remaining 9 incrementally. |
| **Legal liability for AI-generated advice** | HIGH | Every output carries legal disclaimer. AI cites only validated sources. All documents watermarked "DRAFT — AI GENERATED." Consult-a-lawyer button always visible. |
| **Police/court data becomes outdated** | LOW | Court database versioned. Quarterly review cycle. User feedback mechanism for corrections. |

---

## Appendix A: Revenge Porn — Complete Legal Framework (Thailand)

### Applicable Laws

| Law | Section | Offense | Penalty | Statute |
|-----|---------|---------|---------|---------|
| Computer Crime Act (No.2) B.E. 2560 | §16 | Disseminating obscene/sexual content of another person without consent | Up to 5 years imprisonment, ฿100,000 fine | 5 years from offense |
| Criminal Code | §326 | Defamation (general) | Up to 1 year, ฿20,000 fine | 3 months from knowledge |
| Criminal Code | §328 | Defamation by publication | Up to 2 years, ฿200,000 fine | 3 months from knowledge |
| Criminal Code | §397 | Harassment/annoyance | Up to 1 month, ฿10,000 fine | 1 year |
| Civil Code | §420 | Tort (wrongful act causing damage) | Damages as determined | 1 year from knowledge + damages |
| PDPA B.E. 2562 | §27-28 | Processing sensitive personal data without consent | Administrative fine up to ฿5M + civil damages | 2 years |

### Filing Venues

1. **Police Station** (local or where crime occurred)
2. **Technology Crime Suppression Division (บก.ปอท.)** — specialized cyber unit
3. **Criminal Court** — after police investigation/prosecutor filing
4. **Civil Court** — for damages lawsuit
5. **PDPC (สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล)** — PDPA complaints

### Key Resources

- **StopNCII.org** — Global hash database for NCII prevention
- **AOC 1441** — Cyber crime hotline (for online fraud, also handles NCII)
- **OSCC 1300** — One Stop Crisis Center (sexual violence)
- **Women's Foundation** — 02-277-0491
- **Cyber Crime Investigation Bureau** — www.thaipoliceonline.com

---

## Appendix B: Document Templates Catalog

| Template ID | Title (Thai) | Category | Format | Merge Fields |
|-------------|-------------|----------|--------|--------------|
| `criminal-complaint-ncii-v1` | คำร้องทุกข์ — เผยแพร่ภาพอนาจาร | defamation | .docx | name, address, date, perpetrator, platforms, evidence |
| `civil-complaint-defamation-v1` | คำฟ้องคดีแพ่ง — หมิ่นประมาท/ละเมิด | defamation | .docx | name, address, defendant, damage amount, evidence |
| `evidence-list-standard-v1` | บัญชีพยานหลักฐาน | universal | .docx | evidence items, dates, descriptions |
| `witness-statement-v1` | คำให้การพยาน | universal | .docx | witness name, address, testimony |
| `mediation-request-v1` | คำร้องขอไกล่เกลี่ย | universal | .docx | parties, dispute description, desired outcome |
| `police-followup-v1` | หนังสือติดตามคดี | universal | .docx | case number, officer name, days elapsed |
| `evidence-preservation-v1` | หนังสือขอให้เก็บรักษาพยานหลักฐาน | universal | .docx | platform name, URLs, content description |

---

## Appendix C: Thailand Court Database Schema

```typescript
type CourtEntry = {
  id: string;
  name: string;                    // Thai name
  nameEn: string;                  // English name
  type: CourtType;
  province: string;                // Province code
  district: string;                // District code
  address: string;
  phone: string;
  fax?: string;
  website?: string;
  hours: string;
  counters: CounterInfo[];
  fees: FeeSchedule;
  publicTransport: string;
  parking: string;
  notes: string;
  lastVerified: string;            // ISO date
};

type CourtType = 
  | "civil_court"
  | "criminal_court"
  | "provincial_court"             // ศาลจังหวัด
  | "municipal_court"              // ศาลแขวง
  | "labour_court"
  | "juvenile_court"
  | "administrative_court"
  | "consumer_court"               // (same building as civil court)
  | "police_station"
  | "specialized_unit";            // บก.ปอท., DSI, etc.
```

---

*End of Design Document — LegalAI V2 Concierge Flow*
*Version: concierge-v1-design | August 2026*
