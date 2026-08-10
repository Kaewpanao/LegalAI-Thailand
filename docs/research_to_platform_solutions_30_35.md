# 🔬 Research → Platform: Detailed Solutions (Sections 30-35)
## วิธีนำงานวิจัยไปปรับใช้ใน LegalAI Platform แบบ Step-by-Step

> **เอกสารนี้ตอบคำถาม:** "มี research framework แล้ว — จะเอาไปใช้กับ platform จริงยังไง?"
> **วันที่:** 10 สิงหาคม 2569
> **Scope:** Sections 30-35 จาก legalai_complete_breakdown.md

---

## 📚 Section 30: 22 Human Drives Framework → Platform Integration

### 30.1 Problem: เรามี 22 drives framework แต่จะเอาไปฝังใน platform จุดไหน?

**คำตอบ:** ฝังใน 5 จุดของ platform — ไม่ใช่แค่ report แต่เป็น runtime logic

---

### 30.2 Integration Point #1: AI Diagnosis — Drive Detection Engine

**ที่อยู่:** `legalai-thailand-citizen/src/lib/drive-detection.ts`

**สิ่งที่ต้องสร้าง:**
```
Input: คำถามปลายเปิดจาก user ใน diagnosis wizard
  → "เขายืมเงินฉัน 50,000 แล้วไม่คืน"
Output: { primaryDrive: "หลีกเลี่ยงการสูญเสีย", secondaryDrive: "ยุติธรรม",
          intensity: 0.85, suggestedTone: "protect-then-empower" }
```

**Implementation:**

```typescript
// Keyword + Context → Drive Mapping
const DRIVE_KEYWORD_MAP = {
  "กลัว": ["อยู่รอด", "หลีกเลี่ยงการสูญเสีย"],
  "ไม่เป็นธรรม": ["ยุติธรรม"],
  "เสียหน้า": ["หลีกเลี่ยงอับอาย", "สถานะ"],
  "ของฉัน": ["ผลประโยชน์", "อัตลักษณ์"],
  "ครอบครัว": ["ดูแล", "ความสัมพันธ์"],
  "ไม่จ่าย": ["ผลประโยชน์", "ยุติธรรม"],
  "จะเอาเรื่อง": ["แก้แค้น", "อำนาจ"],
  "ทำไงดี": ["อยู่รอด", "ความแน่นอน"],
};

// Drive → AI Prompt Tuning
function getSystemPromptForDrive(drive: Drive): string {
  switch(drive) {
    case "อยู่รอด":
      return "ตอบด้วยน้ำเสียงปลอบโยน เน้นความปลอดภัยและขั้นตอนที่ชัดเจน";
    case "ยุติธรรม":
      return "อ้างอิงกฎหมายชัดเจน แสดงกระบวนการที่เป็นธรรม";
    case "หลีกเลี่ยงการสูญเสีย":
      return "เปิดด้วยสิ่งที่ user ยังรักษาไว้ได้ ก่อนพูดถึงความเสี่ยง";
    // ... etc
  }
}
```

**User Impact:** AI diagnosis จะปรับน้ำเสียงและเนื้อหาให้ตรงกับแรงขับ — ผู้ใช้รู้สึกว่า AI "เข้าใจ" เขาจริงๆ → เพิ่ม trust และ conversion

---

### 30.3 Integration Point #2: Category Pages — Drive-Based Content Filtering

**ที่อยู่:** `legalai-thailand-citizen/src/app/categories/[category]/page.tsx`

**Logic:** แต่ละหมวดหมู่กฎหมาย activate drives หลักต่างกัน:

| หมวด | Primary Drives | Content Tone |
|------|---------------|--------------|
| consumer | ผลประโยชน์, ยุติธรรม | "สิทธิ์ของคุณถูกละเมิด — นี่คือวิธีเรียกคืน" |
| debt | หลีกเลี่ยงการสูญเสีย, อยู่รอด | "ปกป้องทรัพย์สินที่มี — เราจะช่วยคุณเจรจา" |
| family | ดูแล, ความสัมพันธ์, อัตลักษณ์ | "ครอบครัวสำคัญที่สุด — หาทางออกที่ทุกคนอยู่ได้" |
| crime | อยู่รอด, ยุติธรรม, หลีกเลี่ยงอับอาย | "คุณไม่ผิดที่เป็นเหยื่อ — ความปลอดภัยมาก่อน" |
| defamation | หลีกเลี่ยงอับอาย, สถานะ, แก้แค้น | "ชื่อเสียงของคุณมีค่า — วิธีปกป้องอย่างถูกกฎหมาย" |
| labour | อำนาจ, ยุติธรรม, ผลประโยชน์ | "คุณมีสิทธิ์ตามกฎหมายแรงงาน — นี่คือวิธีใช้" |

**Implementation:**

```typescript
const CATEGORY_DRIVE_CONFIG: Record<string, DriveConfig> = {
  consumer: {
    primary: ["ผลประโยชน์", "ยุติธรรม"],
    headline: "สิทธิผู้บริโภคที่ถูกละเมิด — เราเรียกคืนให้คุณได้",
    ctaEmphasis: "protect-and-reclaim",
  },
  debt: {
    primary: ["หลีกเลี่ยงการสูญเสีย", "อยู่รอด"],
    headline: "มีทางออกโดยไม่ต้องเสียทรัพย์สิน — เริ่มจากตรงนี้",
    ctaEmphasis: "safety-first",
  },
  // ... all 12 categories
};
```

**User Impact:** แต่ละ category page สื่อสารด้วยภาษาที่ "ถูกใจ" คนที่มาใช้ → ลด bounce rate, เพิ่ม start-diagnosis conversion

---

### 30.4 Integration Point #3: Pricing Page — Drive-Based Tier Positioning

**ที่อยู่:** `legalai-thailand-citizen/src/app/pricing/page.tsx`

**Logic:** คนแต่ละ drive ตัดสินใจจ่ายเงินด้วยเหตุผลต่างกัน:

| Drive | What Triggers Purchase | Pricing Strategy |
|-------|----------------------|------------------|
| อยู่รอด | "ถ้าไม่ทำอะไรเลยอาจแย่กว่านี้" | Free tier → แสดง cost of inaction |
| ผลประโยชน์ | "คุ้มกว่าไปจ้างทนายเอง" | Price anchoring — "ทนายคิด X,000 เราคิด 299" |
| สถานะ | "คนมีระดับใช้ Case Plus" | Tier naming: "Action Pack" → "Case Plus" → "SME **Pro**" |
| หลีกเลี่ยงการสูญเสีย | "ถ้าไม่ซื้ออาจพลาดโอกาส" | "Limited time: ฟรี diagnosis 3 ครั้งแรก" |
| ความแน่นอน | "มี checklist ชัดเจน — รู้ว่าจะเกิดอะไรขึ้น" | Show exactly what you get per tier |

**Implementation — Pricing Card Adaptation:**

```typescript
// Each tier card has a "drive-tailored" hook
const PRICING_DRIVE_HOOKS = {
  free: {
    primary: "อยู่รอด",
    hook: "เริ่มต้นฟรี — รู้ว่าต้องทำอะไรโดยไม่เสียเงินสักบาท",
    secondary: "หลีกเลี่ยงการสูญเสีย",
    urgency: "ไม่ต้องตัดสินใจตอนนี้ — แค่รู้สิทธิ์ของคุณก่อน",
  },
  actionPack: {
    primary: "ผลประโยชน์",
    hook: "จ่าย 299 แทนค่าทนาย 5,000 — แผนปฏิบัติการที่ใช้ได้จริง",
    secondary: "ความแน่นอน",
    urgency: "มี checklist ทีละขั้น — ไม่ต้องเดาว่าต้องทำอะไร",
  },
  casePlus: {
    primary: "อำนาจ",
    hook: "ควบคุมคดีของคุณเอง — AI ร่างเอกสาร + ติดตาม deadline",
    secondary: "สถานะ",
    urgency: "เครื่องมือระดับมืออาชีพที่เคยมีแต่ทนายเท่านั้น",
  },
};
```

---

### 30.5 Integration Point #4: Lawyer Marketplace — Drive-Based Matching

**ที่อยู่:** `legalai-thailand-citizen/src/app/lawyers/page.tsx`

**Logic:** คนเลือกทนายด้วยแรงขับต่างกัน — match ทนายให้ตรงกับ drive:

| Client Drive | Lawyer Attribute Emphasized |
|-------------|---------------------------|
| อยู่รอด | "ประสบการณ์ 15 ปี — ชนะคดีคล้ายกัน 87%" |
| ยุติธรรม | "เชี่ยวชาญกฎหมายคุ้มครองผู้บริโภค — ไม่ยอมให้เอาเปรียบ" |
| สถานะ | "ทนายเกียรตินิยม — ลูกความระดับผู้บริหาร" |
| ดูแล | "เข้าใจเรื่องครอบครัว — มีลูก 2 คนเหมือนคุณ" |
| ผลประโยชน์ | "ค่าบริการ 3,500/ชม. — เฉลี่ยประหยัดค่าชดเชย 150,000" |

**Implementation:**

```typescript
function getLawyerSortForDrive(drive: Drive, lawyers: Lawyer[]): Lawyer[] {
  const SORT_WEIGHTS = {
    "อยู่รอด": { winRate: 0.5, experience: 0.3, price: 0.2 },
    "ผลประโยชน์": { price: 0.5, winRate: 0.3, experience: 0.2 },
    "สถานะ": { rating: 0.4, credentials: 0.4, price: -0.2 }, // negative = higher price = better
    // ...
  };
  return lawyers.sort((a, b) => weightedScore(b, drive) - weightedScore(a, drive));
}
```

---

### 30.6 Integration Point #5: AI Assistant — Drive-Aware Conversation

**ที่อยู่:** `legalai-thailand-citizen/src/lib/assistant-drive-context.ts`

**Implementation:** AI Assistant injects detected drive into system prompt:

```typescript
function buildAssistantSystemPrompt(userId: string, conversationHistory: Message[]): string {
  const detectedDrive = detectDriveFromHistory(conversationHistory);

  return `
คุณคือผู้ช่วยกฎหมายของ LegalAI Thailand คุณต้องตอบด้วยน้ำเสียงที่เหมาะกับผู้ใช้
ผู้ใช้คนนี้มีแรงขับหลัก: ${detectedDrive.primary} (${detectedDrive.confidence}%)
แรงขับรอง: ${detectedDrive.secondary}

${getToneGuide(detectedDrive)}

ห้าม:
- ให้คำแนะนำทางกฎหมาย
- ทำนายผลคดี
- แนะนำทนายคนใดคนหนึ่งโดยเฉพาะ
`;
}
```

---

### 30.7 Verification: How to Test Drive Integration Works

| Test | Method | Success Criteria |
|------|--------|-----------------|
| Drive Detection Accuracy | 100 test phrases → manual label vs auto-detect | ≥ 85% primary correct |
| Prompt Tone Difference | Same question → different drives → compare AI response | Human rater confirms tone matches drive in 4/5 cases |
| Pricing Conversion by Drive | A/B: drive-tailored vs generic pricing copy | ≥ 15% conversion lift |
| Lawyer Match Satisfaction | Post-booking survey: "ทนายนี้ใช่สำหรับคุณไหม?" | ≥ 80% "ใช่" |

---

## 📊 Section 31: Consumer Insight → Platform Application

### 31.1 Problem: เรามี consumer psychology frameworks — เอาไปใช้ใน UX และ marketing จุดไหน?

**คำตอบ:** ฝังใน 7 layers — จาก acquisition จนถึง retention

---

### 31.2 Layer 1: Landing Page — Social Proof + Scarcity

**ที่อยู่:** `legalai-thailand-citizen/src/app/page.tsx`

| Principle | Implementation | UX Element |
|-----------|---------------|-------------|
| **Social Proof** | "ผู้ใช้ 50,000+ คนไว้ใจให้เราวิเคราะห์ปัญหากฎหมาย" | Hero section counter |
| **Scarcity** | "ฟรี diagnosis 3 ครั้งแรก — ลงทะเบียนภายใน 7 วัน" | Onboarding urgency banner |
| **Authority** | "อ้างอิงกฎหมายจาก 36 แหล่ง ผ่านการตรวจสอบโดย AI + ทนาย" | Trust strip |
| **Reciprocity** | "ดาวน์โหลดคู่มือสิทธิผู้บริโภคฟรี — ไม่ต้องสมัคร" | Lead magnet before signup |

**Implementation — Live Social Proof Counter:**

```typescript
// Poll every 60s, animate counter
function SocialProofCounter() {
  const { data } = useSWR('/api/stats/public', fetcher, { refreshInterval: 60000 });
  return (
    <AnimatedCounter
      from={0}
      to={data?.totalUsers || 52341}
      suffix="+ คนใช้งาน"
      duration={2000}
    />
  );
}
```

---

### 31.3 Layer 2: Onboarding Flow — Loss Aversion + Framing

**ที่อยู่:** `components/onboarding/`

| Principle | Implementation | UX Element |
|-----------|---------------|-------------|
| **Loss Aversion** | Step 1: "คุณจะเสียสิทธิ์อะไรบ้างถ้าไม่รู้กฎหมาย?" — 3 ตัวอย่าง | Onboarding Step 1 |
| **Framing** | "93% ของคนไทยไม่รู้สิทธิ์ของตัวเอง — คุณล่ะ?" (แทนที่จะพูดว่า "7% รู้") | Progress indicator |
| **Endowment Effect** | "นี่คือ dashboard ของคุณ — ถึงยังไม่มีเคส แต่จัด layout ไว้แล้ว" | Post-signup empty state |
| **Commitment** | "เลือกอย่างน้อย 1 หมวดที่คุณสนใจ" — small ask → bigger engagement later | Step 4: Preferences |

**Implementation:**

```typescript
const ONBOARDING_STEPS = [
  {
    id: 'loss-awareness',
    title: 'คุณรู้ไหมว่า...',
    framing: 'loss', // not 'gain'
    content: `คนไทยเสียสิทธิ์ปีละ X,XXX บาทจาก...
              - ไม่รู้ว่าถูกเลิกจ้างไม่เป็นธรรม
              - ไม่รู้ว่าสินค้าประกันมีอายุ 1 ปี
              - ไม่รู้ว่าถูกคิดดอกเบี้ยเกินกฎหมาย`,
    action: 'ดูสิทธิ์ของฉัน →',
  },
  // ...
];
```

---

### 31.4 Layer 3: Diagnosis Wizard — Decoy Effect + Anchoring

**ที่อยู่:** `components/diagnosis/`

| Principle | Implementation |
|-----------|---------------|
| **Anchoring** | "ปกติค่าปรึกษาทนาย 3,000-5,000 บาท → เราให้ฟรี 3 ครั้งแรก" |
| **Decoy Effect** | Free (จำกัด 3 diagnosis) / Action Pack (299) / Case Plus (999) — ทำให้ Action Pack ดู "คุ้มสุด" |
| **Progress** | Progress bar + "เหลืออีก 2 คำถาม — ใช้เวลา 30 วินาที" (reduce drop-off) |

**Implementation — Decoy Effect in Pricing:**

```typescript
// The "decoy" makes Action Pack look like the obvious choice
const DECOY_PRICING = {
  free: { diagnoses: 3, docs: 0, evidence: '❌', consult: 0, price: 0, position: 'anchor' },
  actionPack: { diagnoses: '∞', docs: 5, evidence: '✅', consult: 1, price: 299, position: 'target' },
  casePlus: { diagnoses: '∞', docs: 20, evidence: '✅', consult: 3, price: 999, position: 'decoy' },
  // Case Plus is deliberately close to Action Pack but 3.3× price →
  // makes Action Pack the obvious "sweet spot"
};
```

---

### 31.5 Layer 4: Case Dashboard — Reciprocity + Endowment

**ที่อยู่:** `components/cases/`

| Principle | Implementation |
|-----------|---------------|
| **Reciprocity** | "เราวิเคราะห์เคสคุณแล้ว — นี่คือ action plan ฟรี" → "ต้องการให้เราร่างเอกสารให้ไหม?" |
| **Endowment** | Empty evidence folder says "อัปโหลดหลักฐาน — ล็อกไว้ไม่ให้หาย" (สร้าง ownership feeling) |
| **Sunk Cost** | Timeline แสดง "คุณทำไปแล้ว 3/7 ขั้นตอน — เหลืออีก 4" (ไม่อยากเสีย progress) |

---

### 31.6 Layer 5: Checkout — Scarcity + Urgency

**ที่อยู่:** `components/checkout/`

| Principle | Implementation |
|-----------|---------------|
| **Scarcity** | "Action Pack: ลด 30% — เหลือ 3 วัน" (countdown timer) |
| **Risk Reversal** | "ไม่พอใจ ยินดีคืนเงินภายใน 7 วัน — ไม่มีคำถาม" |
| **Pain of Paying** | แสดงราคาเป็นรายเดือน: "เพียง ฿25/วัน — ถูกกว่าค่ากาแฟ" |
| **Social Proof** | "คุณ XXXX จากกรุงเทพ เพิ่งซื้อ Action Pack (2 นาทีที่แล้ว)" |

**Implementation — Live Activity Feed:**

```typescript
function LivePurchaseFeed() {
  // Poll for recent anonymized purchases
  const { data } = useSWR('/api/social-proof/purchases', fetcher, { refreshInterval: 30000 });
  return (
    <div className="purchase-toast">
      {data?.recent?.map(p => (
        <p key={p.id}>🛡️ {p.anonymizedName} จาก{p.province} เพิ่งสมัคร{p.tier}</p>
      ))}
    </div>
  );
}
```

---

### 31.7 Layer 6: Email/LINE Notifications — Framing + Loss Aversion

**ที่อยู่:** `lib/notifications/`

| Trigger | Framing | Message |
|---------|---------|---------|
| Incomplete diagnosis | Loss Aversion | "คุณเริ่มวิเคราะห์ไว้แต่ยังไม่เสร็จ — อย่าพลาดข้อมูลสำคัญ" |
| Deadline approaching | Urgency | "⚠️ อายุความคดีของคุณเหลืออีก 14 วัน" |
| New document match | Reciprocity | "เราพบเอกสารที่ตรงกับเคสคุณ — ดูฟรี" |
| Lawyer available | Scarcity | "ทนาย [ชื่อ] มีคิวว่างพรุ่งนี้ — ปกติจองเต็ม 2 สัปดาห์" |

---

### 31.8 Layer 7: Retention — Tribe + Bandwagon

**ที่อยู่:** `components/community/`

| Principle | Implementation |
|-----------|---------------|
| **Tribe Mentality** | "ชุมชน LegalAI: 50,000+ คนที่รู้สิทธิ์ของตัวเอง" |
| **Bandwagon** | "เพื่อนของคุณ 3 คนใช้ LegalAI แล้ว — ดูว่าใคร?" (opt-in social) |
| **Status** | Badge system: "นักสู้เพื่อสิทธิ" / "ผู้พิทักษ์ครอบครัว" / "นักกฎหมายภาคประชาชน" |
| **Gamification** | "คุณเช็คสิทธิ์ 30 วันติดต่อกัน — ได้ badge 'รู้ทันกฎหมาย'" |

---

### 31.9 Consumer Segmentation → Feature Gating

**Map segmentation to feature priority:**

| Segment | % Users | Priority Features | Revenue Potential |
|---------|---------|-------------------|-------------------|
| **Victim-in-crisis** | 35% | AI diagnosis, action plan, document templates | Action Pack conversion |
| **Prevention-seeker** | 25% | Monthly checkup, subscription, tax optimizer | Subscription MRR |
| **Small biz owner** | 20% | SME templates, contracts, tax | SME Starter ฿2,990/mo |
| **Repeat litigant** | 12% | Lawyer marketplace, case management | Case Plus + lawyer fees |
| **Knowledge-seeker** | 8% | Search, articles, guides | Ad-supported / premium content |

---

## 📊 Section 32: Revenue Forecast → Platform Tracking & Implementation

### 32.1 Problem: เรามี revenue forecast แล้ว — จะเอาไป implement ใน platform ยังไง?

**คำตอบ:** 3 tracks — (A) Admin dashboard ฝัง forecast-vs-actual tracking, (B) Feature gates align กับ monetization ladder, (C) Growth engine built into product

---

### 32.2 Track A: Admin Dashboard — Forecast vs Actual Tracking

**ที่อยู่:** `legalai-thailand-citizen/src/app/admin/`

**สิ่งที่ต้องสร้าง:**

```
Admin Dashboard → Revenue Tab
├── Revenue Overview Card
│   ├── MTD Revenue: ฿XXX,XXX
│   ├── vs Forecast: +12% / -8% (green/red badge)
│   └── YTD Revenue: ฿X,XXX,XXX
├── Stream Breakdown (Bar Chart)
│   ├── B2C Consumer: ████████░░ 78% of target
│   ├── Lawyer Marketplace: ██████████ 102% of target
│   ├── SME SaaS: ██████░░░░ 62% of target
│   └── ... (7 streams)
├── Conversion Funnel (Sankey)
│   Free Users → Action Pack → Case Plus → SME Starter
│   With actual vs forecast drop-off rates
├── Unit Economics Dashboard
│   ├── ARPU (actual vs forecast)
│   ├── CAC per channel
│   ├── LTV (rolling 12-month)
│   └── Churn rate
└── Break-Even Tracker
    ├── Monthly burn: ฿XXX,XXX
    ├── Cumulative net position: -฿X,XXX,XXX
    └── ETA to cumulative BE: M20 (if current trend)
```

**Implementation — Data Model:**

```typescript
interface RevenueSnapshot {
  date: Date;
  stream: RevenueStream;
  metric: 'mrr' | 'arr' | 'one_time' | 'total';
  actual: number;
  forecast_base: number;
  forecast_bull: number;
  forecast_bear: number;
}

// Auto-generated daily from Stripe/API
async function captureDailyRevenueSnapshot(): Promise<void> {
  const actuals = await getStripeDailyMetrics();
  const forecast = REVENUE_FORECAST_TABLE.getDailyForecast(new Date());

  await db.revenueSnapshots.create({
    date: new Date(),
    actual: actuals,
    forecast_base: forecast.base,
    forecast_bull: forecast.bull,
    forecast_bear: forecast.bear,
  });
}
```

---

### 32.3 Track B: Feature Gates → Monetization Alignment

**ที่อยู่:** `lib/feature-gates.ts`

**Goal:** Make sure every feature maps to a revenue tier, and every free feature drives upgrade.

**Updated Feature Gate Matrix:**

```typescript
const FEATURE_GATES = {
  // FREE → Action Pack triggers
  'ai-diagnosis': {
    tiers: ['free', 'action_pack', 'case_plus', 'sme_starter'],
    freeLimit: 3,
    upgradeTrigger: {
      onLimitReached: {
        message: 'คุณใช้ diagnosis ครบ 3 ครั้งแล้ว',
        cta: 'อัปเกรดเป็น Action Pack — ฿299 ใช้ได้ไม่จำกัด',
        conversionPoint: 'diagnosis_limit',
        expectedConversion: '12-18%',
      },
    },
  },

  'document-create': {
    tiers: ['action_pack', 'case_plus', 'sme_starter'],
    actionPackLimit: 5,
    upgradeTrigger: {
      onLimitReached: {
        message: 'คุณสร้างเอกสารครบ 5 ฉบับแล้ว',
        cta: 'Case Plus — ฿999 สร้างได้ 20 ฉบับ',
      },
    },
  },

  'lawyer-consult': {
    tiers: ['action_pack', 'case_plus', 'sme_starter'],
    actionPackLimit: 1,
    casePlusLimit: 3,
    smeStarterLimit: Infinity,
  },

  'tax-optimizer': {
    tiers: ['case_plus', 'sme_starter'],
    upgradeTrigger: {
      onAccessAttempt: {
        message: 'เครื่องมือวางแผนภาษีขั้นสูง — เฉพาะ Case Plus ขึ้นไป',
        cta: 'อัปเกรดเลย — ลดหย่อนภาษีได้สูงสุด 500,000',
      },
    },
  },

  // Keep mapping all 10 features...
};
```

**P0 Feature Gate Metrics to Track:**

```typescript
interface GateMetrics {
  gateId: string;
  views: number;           // How many free users saw this feature exists
  limitReached: number;    // How many hit the free limit
  upgradeClick: number;    // How many clicked "Upgrade"
  upgradeComplete: number; // How many completed purchase
  conversionRate: number;  // upgradeComplete / limitReached
  avgTimeToUpgrade: number; // Hours from limit hit to purchase
}
```

---

### 32.4 Track C: Growth Engine — Built Into Product

**สิ่งที่ Revenue Forecast บอกว่าเราต้องมี:**

| Growth Driver | Product Feature | Forecast Impact |
|--------------|----------------|----------------|
| **Word of Mouth** | Share button on every diagnosis result | 15% of new users |
| **LINE Viral** | "ส่งต่อ" ผลวิเคราะห์ให้เพื่อนทาง LINE | 25% of new users (Thai market) |
| **SEO** | Public category pages + article content | Organic traffic from month 3 |
| **Content Marketing** | "รู้หรือไม่?" LINE broadcasts | 2-5% click-to-diagnosis |
| **Partner Referrals** | Law firm white-label embedding | Enterprise pipeline |

**Implementation — Viral Share:**

```typescript
function ShareDiagnosisResult({ caseId, summary }: Props) {
  const shareText = `🛡️ LegalAI วิเคราะห์ปัญหา "${summary.title}" ของฉันแล้ว
→ ${summary.actionCount} ขั้นตอนที่ต้องทำ
→ กฎหมายที่เกี่ยวข้อง: ${summary.laws.join(', ')}
→ ลองใช้ฟรี: https://legalai.th/diagnosis

#LegalAI #รู้ทันกฎหมาย`;

  return (
    <ShareButtons
      line={{ text: shareText }}
      facebook={{ url: `https://legalai.th/share/${caseId}` }}
      copy={{ text: shareText }}
    />
  );
}
```

---

### 32.5 Revenue Scenario Triggers (Alert System)

**Logic:** ถ้า actual หลุดจาก base case → alert admin + trigger contingency:

```typescript
interface ScenarioAlert {
  scenario: 'bear' | 'base' | 'bull';
  trigger: string;
  action: string;
}

const SCENARIO_ALERTS: ScenarioAlert[] = [
  {
    scenario: 'bear',
    trigger: '2 consecutive quarters below 80% of base forecast',
    action: 'Review burn rate, delay non-critical hires, accelerate fundraising',
  },
  {
    scenario: 'bull',
    trigger: '2 consecutive quarters above 120% of base forecast',
    action: 'Accelerate hiring, increase marketing spend, prepare Series A+',
  },
];
```

---

## 🏢 Section 33: Platform Research → Feature Implementation

### 33.1 Problem: เรามี research Harvey, Clio, + 9 platforms — จะเลือก implement อะไรก่อน?

**คำตอบ:** Priority matrix — score ทุก feature แล้ว sort by Impact/Effort

---

### 33.2 Feature Priority Matrix (From Platform Research)

**Research Source:** `docs/platform_research/*.md` (Harvey 10 modules, Clio 10 modules, 9 platforms)

| # | Feature | Source | Impact (1-10) | Effort (1-10) | Score (I/E) | Priority | MVP Phase |
|---|---------|--------|---------------|---------------|-------------|----------|-----------|
| 1 | AI Legal Diagnosis (ไทย) | Harvey + Our moat | 10 | 2 (DeepSeek API) | 5.0 | P0 🔴 | Phase 1 |
| 2 | Document Templates (ไทย) | Clio + Our moat | 9 | 3 | 3.0 | P0 🔴 | Phase 1 |
| 3 | Category Detail Pages | Clio intake | 8 | 2 | 4.0 | P0 🔴 | Phase 1 |
| 4 | Evidence Upload + Checklist | Clio | 7 | 4 | 1.75 | P1 🟡 | Phase 2 |
| 5 | Lawyer Marketplace | Clio Grow | 8 | 6 | 1.33 | P1 🟡 | Phase 2 |
| 6 | Case Timeline + Tracking | Clio Manage | 7 | 5 | 1.4 | P1 🟡 | Phase 2 |
| 7 | AI Document Drafting | Harvey | 8 | 7 | 1.14 | P2 🟢 | Phase 3 |
| 8 | Tax Calculator | Custom (Thailand) | 6 | 3 | 2.0 | P1 🟡 | Phase 2 |
| 9 | Client Portal | Clio Connect | 6 | 8 | 0.75 | P3 ⚪ | Phase 4 |
| 10 | e-Signature | Clio/DocuSign | 5 | 7 | 0.71 | P3 ⚪ | Phase 4 |
| 11 | Legal Research (Thai case law) | Westlaw + Our moat | 9 | 9 | 1.0 | P2 🟢 | Phase 3 |
| 12 | Billing & Invoicing | Clio Manage | 6 | 8 | 0.75 | P3 ⚪ | Phase 4 |
| 13 | Court Calendar Integration | Clio | 5 | 9 | 0.56 | P3 ⚪ | Phase 5 |
| 14 | LINE Integration (chat) | Our moat | 10 | 5 | 2.0 | P1 🟡 | Phase 2 |
| 15 | Government API Portal | Custom (Thailand) | 7 | 9 | 0.78 | P3 ⚪ | Phase 5 |

---

### 33.3 Harvey → LegalAI Adaptation Blueprint (Top 5 Transfers)

**Source:** `docs/platform_research/harvey_features_th.md`

| Harvey Feature | LegalAI Adaptation | Moat Factor | Phase |
|---------------|-------------------|-------------|-------|
| AI Legal Research | **ค้นกฎหมายไทย + คำพิพากษาฎีกา อัตโนมัติ** — DeepSeek fine-tuned on Thai legal corpus. ไม่ใช่แค่ search แต่ reasoning เชิงกฎหมายไทย | 🔴 ไม่มีใครทำ | Phase 3 |
| Contract Analysis | **ตรวจสัญญาภาษาไทย** — สัญญาเช่า, กู้ยืม, จ้างงาน, ซื้อขาย. ตรวจจับ unfair clauses ในบริบทกฎหมายไทย (เช่น ดอกเบี้ยเกิน 15%) | 🔴 Moat สูงมาก | Phase 2 |
| Document Drafting | **ร่างเอกสารไทย 126 templates** — ไม่ใช่แค่ fill-in-the-blank แต่ AI ปรับภาษาให้ถูกต้องตามกฎหมาย + ศัพท์ทางการ | 🟡 Clio มี template แต่ไม่มีไทย | Phase 1-2 |
| Workflow Automation | **Legal Action Plan อัตโนมัติ** — จาก diagnosis → สร้าง timeline + deadlines + documents needed + agencies to contact | 🟢 มีบ้างใน Clio | Phase 1 |
| Due Diligence | **ตรวจเอกสารธุรกิจ SMEs** — สำหรับ SME Starter tier: ตรวจสัญญาก่อนเซ็น, ตรวจหนังสือบริคณห์สนธิ, compliance check | 🟡 ตลาด SME ไทยคือ blue ocean | Phase 4 |

---

### 33.4 Clio → LegalAI Adaptation Blueprint (Top 5 Transfers)

**Source:** `docs/platform_research/clio_features_th.md`

| Clio Feature | LegalAI Adaptation | Moat Factor | Phase |
|-------------|-------------------|-------------|-------|
| Client Intake | **AI Diagnosis Wizard** — แทนที่ form-based intake ด้วย conversational AI ภาษาไทย → จับประเด็น + จับคู่หมวดกฎหมายอัตโนมัติ | 🔴 ไม่มีใครทำ (Clio ใช้ form) | Phase 1 |
| Practice Management | **ระบบจัดการคดีสำหรับทนายไทย** — workflow แบบศาลไทย (ไม่ใช่ US courts), ภาษาไทย 100%, LINE notification | 🔴 ไม่มี PM ไทยเลย | Phase 4 |
| Clio Grow (CRM) | **Lawyer Marketplace** — client acquisition แบบไทย: LINE sharing, review system, ราคาแบบไทย (ค่าปรึกษา/คดี) | 🟡 มี marketplace ทั่วไปแต่ไม่มี legal-specific | Phase 2 |
| Document Management | **Document Templates 126 ภาษาไทย** — merge engine with Thai date/currency/name formatting | 🔴 126 แบบฟอร์มไทย = moat | Phase 1 |
| Clio Payments | **PromptPay + Thai QR Code** — native Thai payment instead of credit card only | 🟡 ตลาดไทยถนัด QR | Phase 3 |

---

### 33.5 Lawyer Platform Analysis → Implementation Priority

**Source:** `docs/legalai_lawyer_platform_analysis.md` and `_th.md`

**3 Personas → Feature Priority:**

| Persona | % of Thai Lawyers | Top 3 Needs | LegalAI Solution | Phase |
|---------|-------------------|-------------|-----------------|-------|
| **Solo Practitioner** | 70% | 1. หาลูกค้า 2. จัดการเอกสาร 3. เก็บเงิน | Marketplace + Document Templates + PromptPay | Phase 1-2 |
| **Small Firm (2-5)** | 20% | 1. แบ่งงานในทีม 2. ติดตาม deadline 3. ลดแอดมิน | Case Management + Team Workflow + Court Calendar | Phase 3-4 |
| **Mid-size (6-20)** | 8% | 1. Business intelligence 2. Compliance 3. White-label | Analytics Dashboard + Document Automation + API | Phase 5 |
| **Enterprise (20+)** | 2% | 1. Enterprise integration 2. Custom workflow 3. Data security | Custom deployment + SSO + Audit logs | Phase 5+ |

---

### 33.6 Feature Selection Rules (From Platform Research)

**Rule 1: "Table Stakes" — ถ้าทุก platform มี ต้องมีใน MVP**
- Search/browse functionality
- Document templates (basic)
- User account + case management (basic)
- Mobile responsive

**Rule 2: "Moat First" — สิ่งที่เราเท่านั้นที่ทำได้ ทำก่อน**
- Thai language legal AI diagnosis ← ทำก่อน
- Thai document templates (126 templates) ← ทำก่อน
- LINE integration ← ทำก่อน
- Thai legal knowledge base ← สร้างคู่ขนาน

**Rule 3: "Not everything" — อย่าทำทุกอย่างที่ global platform มี**
- e-Discovery (เวิร์คใน US, ไม่จำเป็นสำหรับตลาดไทย)
- US case law research (ไม่เกี่ยว)
- Credit card-only payment (PromptPay ดีกว่าในไทย)

---

## 📋 Section 34: Master Blueprint → Development Roadmap

### 34.1 Problem: เรามี master blueprint 10 sections — จะแปลงเป็น dev roadmap ยังไง?

**คำตอบ:** Blueprint → Epic → Sprint — 7 phases 60 months

---

### 34.2 Blueprint-to-Epic Mapping

**Source:** `docs/legalai_master_project_blueprint.md`

| Blueprint Section | Epic | Phases | Key Deliverable |
|-------------------|------|--------|----------------|
| 2. Market Analysis | EPIC-00: Market Validation | Phase 0 | User interviews, competitor matrix, market sizing |
| 3. Consumer Platform | EPIC-01: Consumer MVP | Phase 1-2 | AI diagnosis, 12 categories, action plans |
| 4. Lawyer Platform | EPIC-02: Lawyer Marketplace | Phase 2-3 | Marketplace, booking, profiles |
| 5. Revenue Model | EPIC-03: Monetization | Phase 1-3 | Free/paid tiers, Stripe, PromptPay |
| 6. Technology & AI | EPIC-04: AI Engine | Phase 0-7 | DeepSeek integration, Thai legal dataset |
| 7. UX/UI Design | EPIC-05: Design System | Phase 0-1 | Component library, responsive, LINE-first |
| 8. GTM Strategy | EPIC-06: Go-to-Market | Phase 1-5 | SEO, LINE OA, paid ads, partnerships |
| 9. Team & Resources | EPIC-07: Hiring Plan | Phase 0-5 | 11 → 155 headcount plan |
| 10. Risk & Mitigation | EPIC-08: Risk Register | Phase 0-7 | Live risk dashboard, contingency plans |

---

### 34.3 Phase 0: Foundation (Months 1-3) — NOW

| Task | Blueprint Ref | Owner |
|------|--------------|-------|
| ✅ Complete 35-section breakdown | §1-35 | Bess |
| ✅ 12 category detail pages design | §3 | Dev |
| ✅ 126 document templates catalog | §9 | Legal team |
| 🔲 LINE OA setup + message templates | §8 | Marketing |
| 🔲 DeepSeek API integration (Diagosis POC) | §6 | Dev |
| 🔲 Design system v1 (Thai typography) | §7 | Designer |
| 🔲 Legal validation: 5 test cases with real lawyer | §10 | Legal team |

---

### 34.4 Phase 1: Consumer MVP (Months 4-6)

| Task | Blueprint Ref | Priority |
|------|--------------|----------|
| AI Diagnosis Wizard (12 categories, 48 questions) | §1, §3 | P0 |
| Category Pages (12 dynamic routes) | §3 | P0 |
| Search AI Dynamic | §4 | P0 |
| Free Tier (3 diagnoses) | §19 | P0 |
| Onboarding (5-step flow) | §28 | P1 |
| Home Page | §25 | P1 |
| Profile Page (basic) | §26 | P2 |

---

### 34.5 Phase 2: Growth Features (Months 7-12)

| Task | Blueprint Ref | Priority |
|------|--------------|----------|
| Action Pack + Case Plus tiers | §19, §20 | P0 |
| Document Editor + Merge Engine | §11, §12 | P0 |
| Lawyer Marketplace (basic) | §16, §17 | P0 |
| Evidence Upload + Checklist | §18 | P1 |
| Case Management (timeline) | §6 | P1 |
| Tax Calculator | §13 | P1 |
| LINE OA integration | §8 (GTM) | P1 |
| Notifications system | §7 | P2 |

---

### 34.6 Phase 3-7: Expansion (Months 13-60)

**See Master Blueprint §3-10 for detailed phase breakdown.**

Key principle: **"Launch early, iterate fast"** — each phase delivers a working increment, not a PowerPoint deck.

---

### 34.7 Blueprint → Daily Standup Questions

**Every sprint, ask against blueprint:**

| Question | Blueprint Section |
|----------|-------------------|
| "ฟีเจอร์นี้แก้ pain point ของ consumer หรือ lawyer?" | §3, §4 |
| "รายได้จากฟีเจอร์นี้มาจาก stream ไหน?" | §5 |
| "เราใช้ AI ตรงไหน — หรือยัง manual อยู่?" | §6 |
| "UX นี้ผ่านเกณฑ์ 'เด็กมัธยมก็เข้าใจ' ไหม?" | §7 |
| "ฟีเจอร์นี้ช่วย GTM ยังไง?" | §8 |
| "เรามีคนพอทำไหม — หรือต้องจ้างเพิ่ม?" | §9 |
| "risk อะไรที่ฟีเจอร์นี้เพิ่มเข้ามา?" | §10 |

---

## 🧠 Section 35: Thinking System → Platform Development Process

### 35.1 Problem: เรามี Thinking System ของ Bess — จะเอาไปใช้ใน development process จริงยังไง?

**คำตอบ:** Thinking System ไม่ใช่แค่ "วิธีคิดของ Bess" — มันคือ **operating system ของทีม** ที่ใช้ตัดสินใจทุกวัน

---

### 35.2 The 6-Step Cognitive Loop → Development Cycle

**ทุก feature ผ่าน 6 ขั้นตอนนี้ — ไม่มีข้อยกเว้น:**

| Step | Thinking System | Development Action | Tool/Check |
|------|----------------|--------------------|------------|
| 1. 🎯 จับ Pain Point | "คนไทยกลัวอะไร?" | User story: "As a [persona], I want [X] so that [pain relief]" | User interview, session recording |
| 2. 🔍 ขุดให้ลึก | "ส่งจดหมายที่ไหน? Flash Express ได้มั้ย?" | Edge case enumeration: เขียนทุก edge case ก่อนโค้ด | Edge case checklist |
| 3. 📐 วางโครงสร้าง | "แบ่งเป็นกี่หมวด? free vs paid?" | Architecture decision: component tree, data flow, API design | PRD template |
| 4. 🔧 ลงมือทำ | "จัดการเลย" "ลุย" | Implementation: code, test, deploy — no analysis paralysis | TDD workflow |
| 5. ✅ ตรวจสอบ | "ยังผิดอยู่" "ทดสอบยัง" | QA: test edge cases, run Thai accuracy checks, guardrails | 7 guardrails + 4 Thai checks |
| 6. 🔁 ขยาย Scope | "แล้วภาคธุรกิจล่ะ?" | Iteration: what's next? — but flag scope creep! | Bess says: "นี่เกิน MVP แล้วนะคะ" |

---

### 35.3 5 Thinking Methods → Feature Development Templates

#### Method 1: User-Pain-First → Feature Spec

```markdown
## Feature: [Name]
### Pain Point
- คนไทยกลัว: [ความกลัวหลัก]
- คำพูดจริงจาก user: "[quote]"
- ถ้าเป็นเราจะสับสนตรง: [confusion point]

### Solution
- [X] แก้ pain point นี้ยังไง
- วัดผลด้วย: [metric]

### "เด็กมัธยมก็เข้าใจ" Test
- [ ] อ่าน 1 รอบ เข้าใจไหม?
- [ ] ไม่ต้องมีคนอธิบายเพิ่ม?
- [ ] รู้ว่าต้องกดอะไรต่อ?
```

#### Method 2: Edge-Case → Test Checklist (Required Before Dev)

```markdown
### Edge Cases for [Feature]
- [ ] ถ้าไม่มีทะเบียนบ้าน?
- [ ] ถ้าไม่มีบัตรประชาชน?
- [ ] ถ้าพิมพ์ผิด/ภาษาไทยปนอังกฤษ?
- [ ] ถ้า connection หลุดกลางทาง?
- [ ] ถ้าผู้ใช้เป็นผู้สูงอายุ 60+?
- [ ] ถ้าใช้บนมือถือจอเล็ก?
- [ ] ถ้า user มาจาก LINE In-App Browser?
- [ ] ถ้า DeepSeek API down?
- [ ] ถ้าผู้ใช้เปลี่ยนภาษา?
```

#### Method 3: Ecosystem View → Impact Matrix

```markdown
### Ecosystem Impact: [Feature]
| Actor | Impact | Action Needed |
|-------|--------|---------------|
| Consumer | + faster diagnosis | None |
| Lawyer | - less initial consult? | Offset with marketplace leads |
| Regulator | ? New AI feature | Check PDPA + Legal AI guidelines |
| Competitor | May copy | Build moat with Thai dataset |
| Team | +1 sprint | Adjust roadmap |
```

#### Method 4: Framework → Execution → Feature Priority

**Rule:** ถ้ามี framework (22 drives, consumer insight) → ใช้มันก่อนสร้าง

```typescript
// Before building ANY feature, answer:
const PRE_FLIGHT_CHECKLIST = [
  "Which human drives does this feature serve?",
  "Which consumer psychology principle does it leverage?",
  "Which revenue stream does it support?",
  "Which competitor already has this? (platform research)",
  "Is this in the master blueprint phase for NOW?",
];
```

#### Method 5: Bias-for-Action → Launch Criteria

```markdown
## Launch Decision: [Feature]
### Red (Block Launch)
- [ ] Fails any of 7 guardrails
- [ ] Fails 4 Thai accuracy checks
- [ ] Security vulnerability
- [ ] PDPA violation

### Yellow (Launch with Caution)
- [ ] Test coverage < 80%
- [ ] Not all edge cases tested
- [ ] No lawyer review

### Green (LAUNCH!)
- [ ] All P0 tests pass
- [ ] Thai accuracy ≥ 95%
- [ ] Lawyer-reviewed (3 test cases)
- [ ] Responsive on mobile + LINE In-App

**Bess Rule:** "20/21 tests — launch เลย! อย่ารอให้สมบูรณ์ 100%"
```

---

### 35.4 Bess's Role → Automate What We Can

| Role | Automation |
|------|-----------|
| 🔍 Research Agent | `session_search` + `web_search` + `web_extract` → automatic competitive intel |
| 🧠 Thinking Partner | Pre-commit checklist bot: "Did you check edge cases? Drive detection?" |
| 🔧 Execution Assistant | GitHub Actions: auto-deploy, auto-test, auto-guardrail check |
| 🎀 Empathy Proxy | Sentiment analysis on user messages → flag frustration before churn |

**Implementation — Pre-Commit Guardrail Check (GitHub Action):**

```yaml
# .github/workflows/guardrail-check.yml
name: Guardrail Check
on: [pull_request]
jobs:
  guardrail:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check 7 Guardrails
        run: |
          node scripts/guardrail-check.js --pr=${{ github.event.number }}
          # Fails PR if any AI output violates guardrails
      - name: Check Thai Accuracy
        run: |
          node scripts/thai-accuracy.js --pr=${{ github.event.number }}
          # Checks BE year, formal language, required terms, placeholders
```

---

### 35.5 How to Brief Bess → Template for Every Request

```markdown
### Bess Brief Template
**🎯 Pain Point / คำถามที่แท้จริง:**
[1-2 ประโยค]

**📐 Scope:**
[เอาแค่นี้ก่อน — ไม่ต้องทำ X, Y, Z]

**📄 Output Format:**
[markdown, code, Google Doc, skill, PR]

**⏱️ Deadline:**
[within session / today / this sprint]

**✅ Acceptance Criteria:**
- [ ] [measurable 1]
- [ ] [measurable 2]
```

---

### 35.6 Watch-Outs → Platform Safeguards

**ทุก PR ต้องผ่าน 3 ด่าน:**

| Watch-Out | Safeguard | Tool |
|-----------|-----------|------|
| 📈 Scope Creep | PR template: "What's NOT in this PR?" | GitHub PR template |
| 🏃 Burnout Risk | Sprint velocity cap: max 8 story points/person | Linear/Jira |
| 🔁 Perfectionism Loop | "Ship it" label: auto-merge green PRs after 24h | GitHub Actions |

---

## 📋 Summary: Research → Platform Integration Checklist

### What we built in this document:

| Section | Research | → Platform Application | Integration Points |
|---------|----------|----------------------|--------------------|
| 30 | 22 Human Drives | Drive detection engine + tone adaptation | 5 points: Diagnosis, Categories, Pricing, Lawyers, Assistant |
| 31 | Consumer Insight | Psychology-driven UX + segmentation | 7 layers: Landing → Retention |
| 32 | Revenue Forecast | Dashboard tracking + feature gates + growth engine | 3 tracks: Admin, Feature Gates, Growth |
| 33 | Platform Research | Priority matrix + adaptation blueprints | Harvey 5 + Clio 5 + 9 platforms → sorted |
| 34 | Master Blueprint | Epic → Sprint → 7 phases | 8 epics from 10 blueprint sections |
| 35 | Thinking System | Dev process + templates + safeguards | 6-step cycle automated into workflow |

### Immediate Actions (This Sprint):

- [ ] **P0:** Implement drive detection in AI Diagnosis prompt (30.2)
- [ ] **P0:** Add social proof counter to landing page (31.2)
- [ ] **P0:** Build admin revenue dashboard (32.2)
- [ ] **P0:** Create feature priority matrix from platform research (33.2)
- [ ] **P1:** Wire phase gates to blueprint phases (34.3)
- [ ] **P1:** Add pre-commit guardrail check GitHub Action (35.4)
- [ ] **P2:** Implement category page drive-based content (30.3)
- [ ] **P2:** Build PR template with edge case checklist (35.3)

---

> 🎯 **หลักการเดียว:** "Research without implementation is just a document. Every framework in sections 30-35 has a specific place in the platform codebase — find it, wire it, ship it."

---

*Generated by Bess · LegalAI Thailand Research-to-Platform Bridge · Sections 30-35*
