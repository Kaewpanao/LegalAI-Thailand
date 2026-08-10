# 🛠️ Consumer Platform — Detailed Solutions (Sections 1-8)

> Generated: 10 August 2026 | Status: Complete design-grade solutions
> Covers: AI Diagnosis · 45 Problems · Category Pages · Search · Legal Sources · Case Management · Notifications · AI Assistant

---

## 🔴 SECTION 1: AI Diagnosis (12 หมวด — 48 คำถาม + Fear Calibration + Wizard + AI Analysis)

### 1.1–1.12: Category Diagnosis Questions (48 total)

**Approach:**
Each of the 12 categories needs exactly 4 diagnosis questions that AI asks the user. These questions serve as the intake funnel — they narrow the user's situation to a specific legal sub-problem before the AI generates analysis. The question flow uses a wizard pattern: one question at a time, with radio/checkbox answers.

**Code Strategy:**

```typescript
// types/diagnosis.ts
export type CategorySlug = 'labour' | 'consumer' | 'debt' | 'housing' | 'family'
  | 'accident' | 'online_fraud' | 'crime' | 'government' | 'insurance'
  | 'defamation' | 'property';

export interface DiagnosisQuestion {
  id: string;
  text: string;           // e.g. "คุณถูกเลิกจ้างด้วยสาเหตุใด?"
  options: string[];       // e.g. ["ถูกเลิกจ้างโดยไม่ได้รับค่าชดเชย", "ถูกบังคับให้ลาออก", ...]
  multiSelect: boolean;
}

export const DIAGNOSIS_QUESTIONS: Record<CategorySlug, DiagnosisQuestion[]> = {
  consumer: [
    {
      id: 'consumer_q1',
      text: 'คุณพบปัญหาเกี่ยวกับสินค้าหรือบริการอะไร?',
      options: ['สินค้าไม่ตรงปก/ไม่ตรงตามโฆษณา', 'สินค้าชำรุด/เสียหาย', 'ไม่ได้รับสินค้า/บริการ', 'บริการที่ไม่เป็นธรรม/เอาเปรียบ'],
      multiSelect: false,
    },
    {
      id: 'consumer_q2',
      text: 'คุณซื้อสินค้าหรือบริการจากช่องทางใด?',
      options: ['หน้าร้าน/ห้างสรรพสินค้า', 'แพลตฟอร์มออนไลน์ (Shopee/Lazada)', 'โซเชียลมีเดีย (Facebook/TikTok)', 'อื่นๆ'],
      multiSelect: false,
    },
    {
      id: 'consumer_q3',
      text: 'เหตุการณ์เกิดขึ้นเมื่อไหร่?',
      options: ['ภายใน 7 วันที่ผ่านมา', 'ภายใน 30 วัน', '1-3 เดือนที่ผ่านมา', 'มากกว่า 3 เดือน'],
      multiSelect: false,
    },
    {
      id: 'consumer_q4',
      text: 'คุณมีหลักฐานอะไรบ้าง? (เลือกได้มากกว่า 1 ข้อ)',
      options: ['ใบเสร็จ/ใบกำกับภาษี', 'รูปถ่ายสินค้า', 'แชท/ข้อความกับผู้ขาย', 'ยังไม่มีหลักฐาน'],
      multiSelect: true,
    },
  ],
  // ... 11 more categories following same pattern
};
```

**Verification:**
- Load `/diagnosis?category=consumer` → verify exactly 4 questions render
- Select each option → state updates correctly (single vs multi)
- All 12 categories × 4 questions = 48 items confirmed in `DIAGNOSIS_QUESTIONS` map
- Edge case: category not in URL → redirect to `/diagnosis` with category picker

---

### 1.13: Fear Calibration (4 Levels)

**Approach:**
Before showing AI results, gauge the user's emotional state. This affects the AI's tone — urgent cases get direct, actionable language; planning cases get educational detail. 4 levels: panic, urgent, concerned, planning.

**Code Strategy:**

```typescript
// components/DiagnosisWizard.tsx
type FearLevel = 'panic' | 'urgent' | 'concerned' | 'planning';

const fearLevelConfig: Record<FearLevel, { emoji: string; label: string; aiTone: string }> = {
  panic: {
    emoji: '🆘', label: 'ฉันเครียดมาก / ต้องการความช่วยเหลือด่วน',
    aiTone: 'direct, calming, step-by-step action items first',
  },
  urgent: {
    emoji: '⚠️', label: 'กังวล / อยากรู้ว่าต้องทำอะไรตอนนี้',
    aiTone: 'reassuring, prioritized actions, immediate next steps',
  },
  concerned: {
    emoji: '🤔', label: 'เป็นห่วง / อยากเข้าใจสิทธิของตัวเอง',
    aiTone: 'educational, thorough, full legal context',
  },
  planning: {
    emoji: '📋', label: 'อยากเตรียมตัวล่วงหน้า / ศึกษาข้อมูล',
    aiTone: 'comprehensive, preventive, all options explored',
  },
};
```

**Verification:**
- Render FearCalibration step → 4 buttons/options visible
- Select each level → state updates, `aiTone` prepended to AI prompt
- Visual: emoji + label renders correctly for each level
- Screen reader: each button has `aria-label` matching label text

---

### 1.14: Diagnosis Wizard (intake → loading → error)

**Approach:**
A 4-phase wizard component: (1) Category selection, (2) Fear calibration, (3) Q&A (dynamic per category), (4) AI analysis result. Each phase has defined loading, error, and empty states.

**Code Strategy:**

```typescript
// components/DiagnosisWizard.tsx
type WizardPhase = 'category' | 'fear' | 'questions' | 'loading' | 'result' | 'error';

export function DiagnosisWizard() {
  const [phase, setPhase] = useState<WizardPhase>('category');
  const [answers, setAnswers] = useState<Record<string, string | string[]>>({});
  const [aiResponse, setAiResponse] = useState<AnalysisResult | null>(null);

  // Phase transitions
  const advance = (nextPhase: WizardPhase) => setPhase(nextPhase);

  // Error recovery: retry button re-calls LLM
  const retry = async () => {
    setPhase('loading');
    try { /* re-fetch */ } catch { setPhase('error'); }
  };
}
```

**State Matrix:**

| Phase | Skeleton UI | User Action |
|-------|------------|-------------|
| `category` | 12-category grid | Click category |
| `fear` | 4 emotion buttons | Pick fear level |
| `questions` | Dynamic question card (typewriter animation) | Answer each question |
| `loading` | Pulsing AI-thinking skeleton: "AI กำลังวิเคราะห์กรณีของคุณ..." | Wait |
| `result` | Full analysis: citations, evidence checklist, next steps | Read / save / share |
| `error` | Error illustration + "เกิดข้อผิดพลาด — ลองใหม่?" button + "กลับไปหน้าแรก" link | Retry or go home |

**Verification:**
- Full happy path: category → fear → 4 questions → loading → result
- Loading state: skeleton animation visible for at least 800ms (UX minimum)
- Error injection: break API → error state renders with retry button → retry works
- Back button in each phase returns to previous step
- Empty state: no answers → "ยังไม่ได้ตอบคำถาม" helper text

---

### 1.15: AI Analysis (DeepSeek response, citations, evidence readiness)

**Approach:**
Send collected answers + fear level + category metadata to DeepSeek API. The prompt template includes guardrails, source requirements, and formatting instructions. Response is parsed into structured sections.

**Code Strategy:**

```typescript
// lib/ai/diagnosis.ts
interface DiagnosisInput {
  category: CategorySlug;
  fearLevel: FearLevel;
  answers: Record<string, string | string[]>;
}

interface AnalysisResult {
  summary: string;           // สรุปสถานการณ์
  legalAssessment: string;   // วิเคราะห์ทางกฎหมาย
  relevantLaws: { id: string; name: string; section: string }[];
  recommendedActions: { step: number; action: string; deadline?: string }[];
  evidenceChecklist: { item: string; required: boolean; howToObtain: string }[];
  disclaimer: string;
  readinessScore: number;    // 0-100
}

const DIAGNOSIS_PROMPT = (input: DiagnosisInput) => `
คุณเป็นที่ปรึกษากฎหมายเบื้องต้นสำหรับประชาชนไทย (ไม่ใช่ทนายความ)
ผู้ใช้กำลังเผชิญปัญหาในหมวด: ${input.category}
ระดับความกังวล: ${input.fearLevel}
คำตอบจากผู้ใช้: ${JSON.stringify(input.answers)}

กรุณาวิเคราะห์และตอบเป็น JSON:
{
  "summary": "สรุปสถานการณ์ 1-2 ประโยค",
  "legalAssessment": "วิเคราะห์ทางกฎหมาย...",
  "relevantLaws": [{"id": "consumer_protection_act", "name": "พ.ร.บ.คุ้มครองผู้บริโภค", "section": "มาตรา 4"}],
  "recommendedActions": [{"step": 1, "action": "...", "deadline": "ภายใน 30 วัน"}],
  "evidenceChecklist": [{"item": "ใบเสร็จรับเงิน", "required": true, "howToObtain": "ขอจากร้านค้า"}],
  "readinessScore": 65
}
`;
```

**Verification:**
- Submit all 12 categories × varied answers → each returns valid JSON
- Citations: every `relevantLaws[].id` exists in `LEGAL_SOURCES` registry (see Section 5)
- Readiness score: 0 when no evidence, 100 when all checklist items marked as held
- Disclaimer: always present in output, matches guardrail `disclaimer-required`
- Error handling: invalid JSON → fallback to raw text display with warning
- Guardrails: run `checkGuardrails(analysisResult)` before rendering → block if violations found

---

## 📋 SECTION 2: 45 Problems — Sub-Problem Pages

### 2.1–2.12: 45 Problem Definitions (12 Categories × 3-5 Problems Each)

**Approach:**
Each category (e.g., consumer) has 3-5 named sub-problems. Each sub-problem is a data object with: title, description, urgency badge, and link to diagnosis with pre-selected answer. These drive the problem-listing on Category Detail Pages.

**Code Strategy:**

```typescript
// data/problems.ts
export interface Problem {
  id: string;
  categorySlug: CategorySlug;
  title: string;
  description: string;
  urgency: 'high' | 'medium' | 'low';
  urgencyLabel: string;   // "ด่วนมาก", "ควรดำเนินการ", "ข้อมูลทั่วไป"
  preSelectedAnswer: string; // maps to first question option
}

export const PROBLEMS: Problem[] = [
  // consumer (4 problems — section 2.8)
  { id: 'consumer-สินค้าไม่ตรงปก', categorySlug: 'consumer', title: 'สินค้าไม่ตรงปก',
    description: 'ซื้อสินค้าแล้วได้ของไม่ตรงกับที่โฆษณาหรือตกลงไว้ เช่น สีผิด สเปคไม่ตรง',
    urgency: 'medium', urgencyLabel: 'ควรดำเนินการ',
    preSelectedAnswer: 'สินค้าไม่ตรงปก/ไม่ตรงตามโษณา' },
  { id: 'consumer-ไม่ได้รับสินค้า', categorySlug: 'consumer', title: 'ไม่ได้รับสินค้า/บริการ',
    description: 'ชำระเงินแล้วแต่ผู้ขายไม่ส่งสินค้า หรือส่งสินค้าล่าช้าเกินสมควร',
    urgency: 'high', urgencyLabel: 'ด่วนมาก',
    preSelectedAnswer: 'ไม่ได้รับสินค้า/บริการ' },
  { id: 'consumer-อาหารเป็นพิษ', categorySlug: 'consumer', title: 'อาหารเป็นพิษจากร้านอาหาร',
    description: 'ทานอาหารจากร้านแล้วเกิดอาการอาหารเป็นพิษ มีค่าใช้จ่ายในการรักษา',
    urgency: 'high', urgencyLabel: 'ด่วนมาก',
    preSelectedAnswer: 'สินค้าชำรุด/เสียหาย' },
  { id: 'consumer-โฆษณาเกินจริง', categorySlug: 'consumer', title: 'โฆษณาเกินจริง/หลอกลวง',
    description: 'สินค้าหรือบริการโฆษณาเกินจริง ทำให้เข้าใจผิดในสาระสำคัญ',
    urgency: 'medium', urgencyLabel: 'ควรดำเนินการ',
    preSelectedAnswer: 'สินค้าไม่ตรงปก/ไม่ตรงตามโษณา' },
  // ... 41 more problems across 11 categories
];
```

**Verification:**
- Count: `PROBLEMS.length === 45`
- Every problem has valid `categorySlug` in known category list
- Every `urgency` is 'high' | 'medium' | 'low'
- Every `preSelectedAnswer` appears in the corresponding `DIAGNOSIS_QUESTIONS[categorySlug][0].options`

---

### 2.13: Problem Card Component (title + description + urgency badge + link)

**Approach:**
Each sub-problem is rendered as a card with visual urgency indicator (red/yellow/green badge), title, short description, and a CTA linking to the diagnosis flow with pre-filled first answer.

**Code Strategy:**

```typescript
// components/ProblemCard.tsx
export function ProblemCard({ problem }: { problem: Problem }) {
  const urgencyColor = { high: 'bg-red-100 text-red-700', medium: 'bg-amber-100 text-amber-700', low: 'bg-green-100 text-green-700' };

  return (
    <Link href={`/diagnosis?category=${problem.categorySlug}&prefill=${encodeURIComponent(problem.preSelectedAnswer)}`}>
      <div className="card p-4 border rounded-lg hover:shadow-md transition">
        <span className={`badge ${urgencyColor[problem.urgency]} text-xs px-2 py-1 rounded-full`}>
          {problem.urgencyLabel}
        </span>
        <h3 className="font-semibold mt-2">{problem.title}</h3>
        <p className="text-sm text-gray-600 mt-1">{problem.description}</p>
        <span className="text-pink-500 text-sm mt-2 inline-block">→ เริ่มวิเคราะห์</span>
      </div>
    </Link>
  );
}
```

**Verification:**
- Render all 45 cards → each shows title, description, badge
- Click any card → navigates to `/diagnosis?category=X&prefill=Y`
- Urgency badges: red = high, amber = medium, green = low → correct colors
- Hover → shadow transition visible
- Empty state: category with 0 problems → "ไม่มีปัญหาที่พบบ่อย" with CTA to diagnosis

---

### 2.14: Diagnosis Preview (Show 4 Questions)

**Approach:**
On the category detail page, below the problem list, show a preview of "AI จะถามคุณเกี่ยวกับ..." with the 4 questions that the diagnosis wizard will ask.

**Code Strategy:**

```typescript
// components/DiagnosisPreview.tsx
export function DiagnosisPreview({ categorySlug }: { categorySlug: CategorySlug }) {
  const questions = DIAGNOSIS_QUESTIONS[categorySlug];

  return (
    <section className="bg-gray-50 rounded-lg p-6">
      <h3 className="flex items-center gap-2 text-lg font-semibold">
        <SparklesIcon /> AI จะถามคุณเกี่ยวกับ...
      </h3>
      <ol className="mt-4 space-y-3">
        {questions.map((q, i) => (
          <li key={q.id} className="flex gap-3">
            <span className="flex-shrink-0 w-6 h-6 rounded-full bg-pink-100 text-pink-600 text-sm flex items-center justify-center font-medium">
              {i + 1}
            </span>
            <div>
              <p className="font-medium">{q.text}</p>
              <p className="text-xs text-gray-500 mt-1">
                ตัวเลือก: {q.options.join(', ')}
              </p>
            </div>
          </li>
        ))}
      </ol>
      <Link href={`/diagnosis?category=${categorySlug}`} className="btn-primary mt-4 inline-block">
        เริ่มวิเคราะห์เคสของฉัน →
      </Link>
    </section>
  );
}
```

**Verification:**
- Renders exactly 4 numbered questions for each category
- "เริ่มวิเคราะห์" CTA links to correct `/diagnosis?category=X`
- All question texts and options are visible
- Responsive: collapses cleanly on mobile

---

## 📂 SECTION 3: Category Detail Pages (12 Pages)

### 3.1: `/categories` — Browse All 12 Categories

**Approach:**
A grid page showing all 12 legal categories as cards. Each card has the category name (Thai), icon, problem count, and navigates to `/categories/[slug]`.

**Code Strategy:**

```typescript
// app/categories/page.tsx
const CATEGORY_META: Record<CategorySlug, { icon: string; label: string; color: string }> = {
  consumer: { icon: '🛒', label: 'ผู้บริโภค', color: 'bg-pink-50 border-pink-200' },
  labour: { icon: '👷', label: 'แรงงาน', color: 'bg-blue-50 border-blue-200' },
  // ... 10 more
};

export default function CategoriesPage() {
  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-6">
      {Object.entries(CATEGORY_META).map(([slug, meta]) => (
        <Link key={slug} href={`/categories/${slug}`}>
          <Card className={`${meta.color} border-2 text-center p-6 hover:scale-105 transition`}>
            <span className="text-3xl">{meta.icon}</span>
            <h3 className="font-semibold mt-2">{meta.label}</h3>
            <p className="text-xs text-gray-500 mt-1">
              {PROBLEMS.filter(p => p.categorySlug === slug).length} ปัญหาที่พบบ่อย
            </p>
          </Link>
        ))}
      </div>
    );
  }
}
```

**Verification:**
- Page renders 12 category cards in a responsive grid
- Each card shows correct icon, Thai label, problem count
- Click → navigates to `/categories/consumer`, etc.
- Mobile: 2 columns → tablet: 3 → desktop: 4

---

### 3.2: `/categories/[category]` — Dynamic Route (12 Variations)

**Approach:**
A dynamic route using `generateStaticParams` for all 12 category slugs. The page renders the Problems section, AI Preview section, Legal Sources section, and sidebar.

**Code Strategy:**

```typescript
// app/categories/[slug]/page.tsx
export function generateStaticParams() {
  return Object.keys(CATEGORY_META).map(slug => ({ slug }));
}

export default function CategoryPage({ params }: { params: { slug: string } }) {
  const slug = params.slug as CategorySlug;
  const categoryProblems = PROBLEMS.filter(p => p.categorySlug === slug);
  const categorySources = LEGAL_SOURCES.filter(s => s.categories.includes(slug));

  return (
    <div className="flex gap-8 p-6">
      <main className="flex-1">
        {/* Section 3.3: Problems */}
        <ProblemsSection problems={categoryProblems} />

        {/* Section 3.4: AI Preview */}
        <DiagnosisPreview categorySlug={slug} />

        {/* Section 3.5: Legal Sources */}
        <SourcesSection sources={categorySources} />
      </main>

      {/* Sections 3.6-3.7: Sidebar */}
      <CategorySidebar currentSlug={slug} />
    </div>
  );
}
```

**Verification:**
- All 12 routes (`/categories/consumer`, etc.) render without 404
- Wrong slug → 404 page with "หมวดนี้ไม่มีในระบบ" + link back
- Content differs per category (different problems, different sources)
- `generateStaticParams` produces 12 entries

---

### 3.3: Problems Section — Card Per Problem with Urgency

**Approach:**
A section showing "ปัญหาที่พบบ่อย" with the `ProblemCard` component for each problem in the current category.

**Verification:**
- Consumer: 4 cards | Family: 5 cards | Housing: 3 cards — matches problem count
- Urgency badge color correct per problem
- Empty: category with no problems → "กำลังรวบรวมข้อมูล" placeholder

---

### 3.4: AI Question Preview Section

**Approach:**
The `DiagnosisPreview` component (from 2.14) embedded on the category page.

**Verification:**
- Shows exactly 4 questions matching the category
- Links to `/diagnosis?category=[slug]`

---

### 3.5: Legal Sources Section

**Approach:**
Lists relevant Thai laws for the category, sourced from the `LEGAL_SOURCES` registry (Section 5). Each source shows: law name, key sections, and a link to the official gazette if available.

**Verification:**
- Consumer: shows 2 sources (คุ้มครองผู้บริโภค, วิธีพิจารณาคดีผู้บริโภค)
- No fake sources — all IDs resolve via `resolveSource()`
- Each source has Thai name, key sections, and category association

---

### 3.6: Sidebar — Help Section

**Approach:**
A persistent sidebar on category pages with quick links: search, document templates, lawyer marketplace, and emergency contacts.

**Code Strategy:**

```typescript
// components/CategorySidebar.tsx
const sidebarLinks = [
  { label: '🔍 ค้นหาข้อมูลเพิ่มเติม', href: '/search' },
  { label: '📄 สร้างเอกสารทางกฎหมาย', href: '/documents' },
  { label: '👨‍⚖️ ปรึกษาทนายความ', href: '/lawyers' },
];

const emergencyContacts = [
  { label: '📞 สายด่วนคุ้มครองผู้บริโภค', number: '1166' },
  { label: '📞 สายด่วนตำรวจ', number: '191' },
];
```

**Verification:**
- Sidebar visible on all 12 category pages
- Links navigate correctly
- Emergency numbers correct (1166 = OCPB, 191 = police)
- Mobile: sidebar collapses to bottom of page or hamburger menu

---

### 3.7: Sidebar — Cross-Navigation (Other Categories)

**Approach:**
Below the help section, show "หมวดอื่นๆ" — a list of all 12 categories excluding the current one, as clickable links.

**Verification:**
- Shows 11 other categories (current excluded)
- Click → navigates to that category page
- Current category visually absent from the list

---

### 3.8: CTA — "เริ่มวิเคราะห์เคสของฉัน"

**Approach:**
A prominent button at the bottom of the main content (not sidebar) linking to `/diagnosis?category=X`. Uses the category's accent color.

**Verification:**
- CTA visible on all 12 category pages
- Click → `/diagnosis?category=consumer` (category pre-selected)
- Analytics event fires: `cta_diagnosis_start` with category slug

---

## 🔍 SECTION 4: Search AI Dynamic

### 4.1: Search Form with Query Parameter

**Approach:**
A search input on `/search` that syncs with `?q=` URL parameter. On submit, calls the AI search endpoint. Uses `useSearchParams` for SSR-safe URL sync.

**Code Strategy:**

```typescript
// app/search/page.tsx
export default function SearchPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const initialQuery = searchParams.get('q') || '';
  const [status, setStatus] = useState<'idle' | 'loading' | 'done' | 'error'>('idle');

  const handleSearch = (query: string) => {
    router.push(`/search?q=${encodeURIComponent(query)}`, { scroll: false });
    setStatus('loading');
    fetch(`/api/search?q=${encodeURIComponent(query)}`)
      .then(r => r.json())
      .then(data => { setResults(data); setStatus('done'); })
      .catch(() => setStatus('error'));
  };
}
```

**Verification:**
- Type query → URL updates to `/search?q=...`
- Empty query → idle state (no API call)
- Copy URL with `?q=X` → page loads with query prefilled + search executed
- Special characters (Thai, emoji) encoded/decoded correctly

---

### 4.2: Loading State — "AI กำลังวิเคราะห์..."

**Approach:**
While the search API call is in-flight, show a loading skeleton with animated shimmer + Thai text "AI กำลังวิเคราะห์คำถามของคุณ...". Minimum display time of 800ms to prevent flicker.

**Code Strategy:**

```typescript
function SearchLoading() {
  return (
    <div className="space-y-4 animate-pulse">
      <div className="flex items-center gap-3">
        <SparklesIcon className="w-5 h-5 text-pink-400 animate-spin-slow" />
        <p className="text-gray-500">AI กำลังวิเคราะห์คำถามของคุณ...</p>
      </div>
      {[1, 2, 3].map(i => (
        <div key={i} className="h-16 bg-gray-100 rounded-lg" />
      ))}
    </div>
  );
}
```

**Verification:**
- Loading state visible for at minimum 800ms
- Shimmer animation smooth (not janky)
- "กำลังวิเคราะห์" text visible and clearly Thai-correct
- Spinner icon present

---

### 4.3: Result State — AI Response with Citations

**Approach:**
The AI search response contains: a summary paragraph, a list of relevant topics with citations, and clickable article/article links. Each citation references a legal source from the registry.

**Code Strategy:**

```typescript
interface SearchResult {
  query: string;
  summary: string;
  citations: { sourceId: string; title: string; excerpt: string }[];
  relatedCategories: CategorySlug[];
  articles: { title: string; url: string; snippet: string }[];
  disclaimer: string;
}

function SearchResults({ result }: { result: SearchResult }) {
  return (
    <div className="space-y-6">
      <p className="text-lg">{result.summary}</p>

      <div>
        <h3 className="font-semibold mb-2">📜 กฎหมายที่เกี่ยวข้อง</h3>
        {result.citations.map(c => <CitationCard key={c.sourceId} citation={c} />)}
      </div>

      {result.articles.length > 0 && <ArticleList articles={result.articles} />}

      <Disclaimer text={result.disclaimer} />
    </div>
  );
}
```

**Verification:**
- Search "ซื้อของออนไลน์ไม่ได้ของ" → returns consumer-related results
- Citations link to real legal sources (verified by `resolveSource()`)
- Empty results → "ไม่พบข้อมูลที่เกี่ยวข้อง — ลองเปลี่ยนคำค้น หรือ เริ่มวิเคราะห์เคส"
- Thai query → Thai response (language consistency)

---

### 4.4: Error State — Fallback Message + Diagnosis Link

**Approach:**
When the AI search API fails (network error, timeout, rate limit), show: error illustration, human-readable message, "ลองใหม่" button, and "หรือ เริ่มวิเคราะห์เคสของคุณ" with a link to `/diagnosis`.

**Verification:**
- Simulate API 500 → error state renders
- "ลองใหม่" button re-triggers search
- Diagnosis link navigates to `/diagnosis`
- Error is logged (console.error + optional analytics)

---

### 4.5: Sort Dropdown — เกี่ยวข้อง/ใหม่สุด/เก่าสุด

**Approach:**
A dropdown above results allowing re-sorting of articles. Sort is client-side (articles are already loaded). Dropdown uses a native `<select>` styled with Tailwind.

**Code Strategy:**

```typescript
type SortOption = 'relevance' | 'newest' | 'oldest';

<select value={sort} onChange={e => setSort(e.target.value as SortOption)}
  className="border rounded px-3 py-1 text-sm">
  <option value="relevance">เกี่ยวข้องที่สุด</option>
  <option value="newest">ใหม่สุด</option>
  <option value="oldest">เก่าสุด</option>
</select>
```

**Verification:**
- Dropdown visible only when results exist
- Change sort → results re-order immediately (no page reload)
- Default: "เกี่ยวข้องที่สุด"
- All 3 options work and produce different orderings

---

### 4.6: Business Doc Sidebar — Matching Categories

**Approach:**
A sidebar on the search results page showing document template categories that match the search topic. Dynamically populated based on `result.relatedCategories`.

**Verification:**
- Search "ซื้อขายที่ดิน" → sidebar shows "อสังหาริมทรัพย์" document category
- Each sidebar item links to `/documents/[category]`
- No sidebar when no related categories found

---

### 4.7: Article Links — Clickable

**Approach:**
Each article in the search results is a clickable card linking to the external URL with `target="_blank"` and `rel="noopener noreferrer"`.

**Verification:**
- Click article → opens in new tab
- Link has correct security attributes
- Article title, URL snippet visible on card
- External link icon () indicator

---

### 4.8: Topic Tags — `/search?q=topic`

**Approach:**
Below the summary, show clickable topic tag pills. Each tag links to `/search?q=[tag]`, effectively triggering a new search for that topic.

**Verification:**
- Tags rendered below summary
- Click tag → navigates to `/search?q=...` and triggers new search
- Tags are relevant to the search query (not generic)

---

### 4.9: Disclaimer — "ผลค้นหาเป็นข้อมูลเบื้องต้น"

**Approach:**
A persistent disclaimer at the bottom of all search results: "ผลค้นหาเป็นข้อมูลเบื้องต้น ไม่ใช่คำแนะนำทางกฎหมาย ควรปรึกษาทนายความก่อนดำเนินการใดๆ" in a styled warning box.

**Verification:**
- Disclaimer present on every search result (including empty)
- Matches guardrail `disclaimer-required` text
- Warning box has amber/light-yellow background

---

### 4.10: Share Button — `navigator.share` / Clipboard

**Approach:**
A share button on each search result. Uses the Web Share API (`navigator.share`) when available; falls back to `navigator.clipboard.writeText` with a "คัดลอกลิงก์แล้ว!" toast.

**Code Strategy:**

```typescript
async function shareSearch(query: string) {
  const url = `${window.location.origin}/search?q=${encodeURIComponent(query)}`;
  if (navigator.share) {
    await navigator.share({ title: 'LegalAI ค้นหา', text: `ผลค้นหา: ${query}`, url });
  } else {
    await navigator.clipboard.writeText(url);
    toast.success('คัดลอกลิงก์แล้ว! 📋');
  }
}
```

**Verification:**
- Click share → Web Share API opens on mobile
- Desktop (no share API) → copies URL → toast appears
- URL format correct: includes `?q=` with encoded query
- Toast auto-dismisses after 3 seconds

---

### 4.11: Save Button — Toggle State

**Approach:**
A bookmark/save button on each search result. Toggles between "saved" and "unsaved" states with visual feedback (filled vs outline icon). Saved searches appear in the user's profile.

**Code Strategy:**

```typescript
function SaveSearchButton({ query }: { query: string }) {
  const [saved, setSaved] = useState(false);

  return (
    <button onClick={() => { setSaved(!saved); toast.success(saved ? 'ยกเลิกบันทึกแล้ว' : 'บันทึกแล้ว 📌'); }}
      aria-label={saved ? 'ยกเลิกบันทึก' : 'บันทึกการค้นหา'}>
      {saved ? <BookmarkFilledIcon className="text-pink-500" /> : <BookmarkIcon />}
    </button>
  );
}
```

**Verification:**
- Click → toggles icon + shows toast
- Re-click → toggles back
- Icon transitions smoothly
- `aria-label` changes with state for accessibility

---

## 📜 SECTION 5: 36 Legal Sources

### 5.1–5.12: Source Definitions (36 Sources Across 12 Categories)

**Approach:**
A centralized, immutable registry of all 36 legal sources. Each source has: unique ID, Thai name, key sections, associated categories, and official reference. This is the single source of truth — AI outputs and UI both reference this registry.

**Code Strategy:**

```typescript
// data/legal-sources.ts
export interface LegalSource {
  id: string;
  name: string;           // Thai full name
  shortName: string;       // Thai short name
  categories: CategorySlug[];
  keySections: string[];   // e.g. ["มาตรา 4", "มาตรา 57"]
  officialRef: string;     // Gazette URL or reference number
  lastAmended: string;     // ISO date
}

export const LEGAL_SOURCES: LegalSource[] = [
  // 5.2: Consumer (2 sources)
  {
    id: 'consumer_protection_act',
    name: 'พระราชบัญญัติคุ้มครองผู้บริโภค พ.ศ. 2522',
    shortName: 'พ.ร.บ.คุ้มครองผู้บริโภค',
    categories: ['consumer'],
    keySections: ['มาตรา 4', 'มาตรา 57', 'มาตรา 57/1'],
    officialRef: 'http://www.ratchakitcha.soc.go.th/...',
    lastAmended: '2019-05-26',
  },
  {
    id: 'consumer_case_procedure_act',
    name: 'พระราชบัญญัติวิธีพิจารณาคดีผู้บริโภค พ.ศ. 2551',
    shortName: 'พ.ร.บ.วิธีพิจารณาคดีผู้บริโภค',
    categories: ['consumer'],
    keySections: ['มาตรา 7', 'มาตรา 25'],
    officialRef: 'http://www.ratchakitcha.soc.go.th/...',
    lastAmended: '2008-08-23',
  },
  // 5.1: Labour (3 sources)
  // 5.3: Debt (3 sources)
  // 5.4: Housing (1 source)
  // 5.5: Family (3 sources)
  // 5.6: Accident (2 sources)
  // 5.7: Online Fraud (4 sources)
  // 5.8: Crime (5 sources)
  // 5.9: Government (3 sources)
  // 5.10: Insurance (3 sources)
  // 5.11: Defamation (3 sources)
  // 5.12: Property (3 sources)
  // ... 34 more entries
];
```

**Verification:**
- Total: `LEGAL_SOURCES.length === 36`
- Every `id` is unique
- Every `categories` array has at least 1 valid `CategorySlug`
- Distribution check: labour=3, consumer=2, debt=3, housing=1, family=3, accident=2, online_fraud=4, crime=5, government=3, insurance=3, defamation=3, property=3
- Every source has at least 1 `keySections` entry
- All Thai names are grammatically correct

---

### 5.13: Anti-Hallucination — `resolveSource()` Returns Null for Unknown IDs

**Approach:**
A lookup function that resolves a source ID to a `LegalSource` object. Returns `null` (not `undefined`, not a dummy object) for any ID not in the registry. This is the **only** way AI-generated source references enter the rendering pipeline.

**Code Strategy:**

```typescript
// data/legal-sources.ts
const SOURCE_MAP = new Map(LEGAL_SOURCES.map(s => [s.id, s]));

export function resolveSource(id: string): LegalSource | null {
  return SOURCE_MAP.get(id) ?? null;
}

export function resolveSources(ids: string[]): LegalSource[] {
  return ids.map(resolveSource).filter((s): s is LegalSource => s !== null);
}
```

**Verification:**
- `resolveSource('consumer_protection_act')` → returns `LegalSource` object
- `resolveSource('fake_law_123')` → returns `null`
- `resolveSource('')` → returns `null`
- `resolveSource('   ')` → returns `null`
- `resolveSources(['real', 'fake'])` → returns only real sources (1 result)
- Every AI response must pass through `resolveSources()` before rendering

**Guardrail Integration:**
```typescript
// In AI response handler:
const validSources = resolveSources(aiResponse.relevantLaws.map(l => l.id));
if (validSources.length === 0) {
  logGuardrailViolation('no-fabricated-sources', { attemptedIds: aiResponse.relevantLaws });
}
```

---

### 5.14: `LEGAL_SOURCE_VERSION = "sources-v2"`

**Approach:**
A version string attached to the legal sources registry. This enables cache-busting, migration scripts, and audit trails. When sources are added/modified, the version is bumped.

**Code Strategy:**

```typescript
export const LEGAL_SOURCE_VERSION = 'sources-v2';

// Optional: version check on app startup
if (typeof window !== 'undefined') {
  const cached = localStorage.getItem('legal_sources_version');
  if (cached !== LEGAL_SOURCE_VERSION) {
    localStorage.setItem('legal_sources_version', LEGAL_SOURCE_VERSION);
    // Invalidate any cached search results
    localStorage.removeItem('search_cache');
  }
}
```

**Verification:**
- Version string is `'sources-v2'`
- App startup logs version (dev mode)
- Source update PR must bump version → reviewer checklist item
- Mismatch between cached version and current → cache cleared

---

## 📋 SECTION 6: Case Management

### 6.1: `/cases` — Case List with Filter Tabs

**Approach:**
A case list page with 4 filter tabs: ทั้งหมด, กำลังดำเนินการ, รอเอกสาร, เสร็จสิ้น. Each tab filters the case list. Cases are rendered as cards with: case title, category badge, status indicator, last updated date, and "ดูรายละเอียด" CTA.

**Code Strategy:**

```typescript
// app/cases/page.tsx
type CaseStatus = 'ทั้งหมด' | 'กำลังดำเนินการ' | 'รอเอกสาร' | 'เสร็จสิ้น';
type CaseStatusKey = 'active' | 'pending_evidence' | 'completed';

const tabs: { label: CaseStatus; key: CaseStatusKey | 'all' }[] = [
  { label: 'ทั้งหมด', key: 'all' },
  { label: 'กำลังดำเนินการ', key: 'active' },
  { label: 'รอเอกสาร', key: 'pending_evidence' },
  { label: 'เสร็จสิ้น', key: 'completed' },
];

export default function CasesPage() {
  const [activeTab, setActiveTab] = useState<typeof tabs[number]['key']>('all');
  const cases = useCases(); // SWR/React Query

  const filtered = activeTab === 'all'
    ? cases
    : cases.filter(c => c.status === activeTab);

  return (
    <div>
      <TabBar tabs={tabs} active={activeTab} onChange={setActiveTab} />
      {filtered.length === 0
        ? <EmptyState message="ไม่มีเคสในหมวดนี้ — เริ่มวิเคราะห์เคสใหม่?" link="/diagnosis" />
        : <CaseList cases={filtered} />
      }
    </div>
  );
}
```

**Verification:**
- All 4 tabs render and are clickable
- Active tab: visually highlighted (pink underline)
- Default: "ทั้งหมด" selected, shows all cases
- Filter: "กำลังดำเนินการ" only shows active cases
- Empty state: per-tab "ไม่มีเคส" + link to `/diagnosis`
- Tab state persists in URL (`/cases?tab=active`)

---

### 6.2: `/cases/[caseId]/timeline` — Tabs + Timeline + Action Steps

**Approach:**
A case detail page with 4 sub-tabs: ภาพรวม, ไทม์ไลน์, หลักฐาน, เอกสาร. The timeline tab shows a vertical timeline of AI-recommended action steps with status indicators (done/in-progress/pending).

**Code Strategy:**

```typescript
// app/cases/[caseId]/timeline/page.tsx
interface ActionStep {
  id: string;
  step: number;
  action: string;
  deadline?: string;
  status: 'done' | 'in_progress' | 'pending';
  note?: string;
}

function TimelineTab({ steps }: { steps: ActionStep[] }) {
  return (
    <div className="relative pl-8 border-l-2 border-pink-200 space-y-6">
      {steps.map(step => (
        <div key={step.id} className="relative">
          <span className={`absolute -left-[25px] w-4 h-4 rounded-full border-2 ${
            step.status === 'done' ? 'bg-green-500 border-green-500' :
            step.status === 'in_progress' ? 'bg-pink-500 border-pink-500 animate-pulse' :
            'bg-white border-gray-300'
          }`} />
          <div className="ml-2">
            <h4 className="font-medium">{step.step}. {step.action}</h4>
            {step.deadline && <p className="text-xs text-red-500">⏰ ภายใน {step.deadline}</p>}
            {step.status === 'done' && <span className="text-xs text-green-600">✅ เสร็จสิ้น</span>}
          </div>
        </div>
      ))}
    </div>
  );
}
```

**Verification:**
- 4 sub-tabs visible on case detail page
- Timeline renders steps from AI diagnosis output
- Status indicators: green=done, pink=pulse=in_progress, gray=pending
- Steps are ordered by step number
- Deadline shows as red text with ⏰ icon
- Clicking a step toggles done/pending (interactive)

---

### 6.3: `/cases/[caseId]/evidence` — Drag-Drop Upload + Evidence Checklist

**Approach:**
The evidence tab has two components: (1) a drag-and-drop file upload zone, and (2) an evidence checklist with readiness score. Files uploaded here are linked to specific evidence requirements via the "เชื่อมโยง" button.

**Code Strategy:**

```typescript
// components/EvidenceTab.tsx
interface EvidenceRequirement {
  id: string;
  label: string;       // e.g. "ใบเสร็จรับเงิน"
  required: boolean;
  howToObtain: string;
  linkedFileId?: string;
}

function EvidenceChecklist({ items }: { items: EvidenceRequirement[] }) {
  const provided = items.filter(i => i.linkedFileId).length;
  const score = Math.round((provided / items.length) * 100);

  return (
    <div>
      <div className="flex items-center gap-4 mb-4">
        <ReadinessRing score={score} />
        <span>{provided}/{items.length} หลักฐานพร้อม</span>
      </div>
      {items.map(item => (
        <div key={item.id} className="flex items-center gap-3 py-2 border-b">
          <input type="checkbox" checked={!!item.linkedFileId} readOnly />
          <span>{item.label} {item.required && <Badge>จำเป็น</Badge>}</span>
          {item.linkedFileId ? <FileLink fileId={item.linkedFileId} /> : <span className="text-xs text-gray-400">ยังไม่มีไฟล์</span>}
        </div>
      ))}
    </div>
  );
}
```

**Verification:**
- Drag-and-drop zone: accepts files, shows blue highlight on drag
- Click-to-browse also works
- Evidence checklist populated from AI diagnosis output
- Readiness score ring renders with correct percentage
- Each item can be linked to an uploaded file
- Required items highlighted with "จำเป็น" badge

---

### 6.4: File-to-Evidence Linking — "เชื่อมโยง" Button

**Approach:**
Each uploaded file has a "เชื่อมโยง" button that opens a dropdown/popover listing all evidence requirements. Selecting a requirement links the file to that requirement. This creates the mapping between raw files and evidence categories.

**Code Strategy:**

```typescript
function LinkFileButton({ fileId, evidenceItems }: { fileId: string; evidenceItems: EvidenceRequirement[] }) {
  const [open, setOpen] = useState(false);

  return (
    <Popover open={open}>
      <PopoverTrigger onClick={() => setOpen(!open)}>
        <Button variant="outline" size="sm">🔗 เชื่อมโยง</Button>
      </PopoverTrigger>
      <PopoverContent>
        <h4>เลือกหลักฐานที่เกี่ยวข้อง</h4>
        {evidenceItems.map(item => (
          <button key={item.id} onClick={() => { linkFileToEvidence(fileId, item.id); setOpen(false); toast.success('เชื่อมโยงแล้ว!'); }}>
            {item.label}
          </button>
        ))}
      </PopoverContent>
    </Popover>
  );
}
```

**Verification:**
- "เชื่อมโยง" visible on each uploaded file card
- Click → dropdown shows all evidence requirements
- Select requirement → file linked → dropdown closes → toast
- Re-linking changes the association
- Unlinking possible via "×" on the evidence item's file link

---

### 6.5: File Validation — PDF/JPG/PNG/WebP, Max 20MB

**Approach:**
Client-side validation before upload + server-side validation after. Rejected files show an error message with the reason.

**Code Strategy:**

```typescript
// lib/upload/validate.ts
const ALLOWED_TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'image/webp'];
const MAX_SIZE_BYTES = 20 * 1024 * 1024; // 20MB

export function validateFile(file: File): { valid: true } | { valid: false; error: string } {
  if (!ALLOWED_TYPES.includes(file.type)) {
    return { valid: false, error: `ไม่อนุญาตไฟล์ประเภท ${file.type || 'ไม่รู้จัก'} กรุณาอัปโหลด PDF, JPG, PNG หรือ WebP เท่านั้น` };
  }
  if (file.size > MAX_SIZE_BYTES) {
    const sizeMB = (file.size / (1024 * 1024)).toFixed(1);
    return { valid: false, error: `ไฟล์ขนาด ${sizeMB}MB เกินขีดจำกัด 20MB กรุณาลดขนาดไฟล์` };
  }
  return { valid: true };
}
```

**Verification:**
- Upload PDF → accepted ✓
- Upload PNG → accepted ✓
- Upload WebP → accepted ✓
- Upload .docx → rejected with Thai error message
- Upload 25MB file → rejected with size error
- Server-side also validates (double-check for security)
- Error message displays inline near the drop zone

---

## 🔔 SECTION 7: Notifications

### 7.1: Filter Tabs — ทั้งหมด/เคสของฉัน/เอกสาร/ระบบ

**Approach:**
A notification center page (`/notifications`) with 4 filter tabs to categorize notifications. Uses the same TabBar component as cases for consistency.

**Code Strategy:**

```typescript
// app/notifications/page.tsx
type NotificationFilter = 'all' | 'case' | 'document' | 'system';

const filterTabs: { label: string; key: NotificationFilter }[] = [
  { label: 'ทั้งหมด', key: 'all' },
  { label: 'เคสของฉัน', key: 'case' },
  { label: 'เอกสาร', key: 'document' },
  { label: 'ระบบ', key: 'system' },
];

// Filter logic
const filtered = activeFilter === 'all' ? notifications : notifications.filter(n => n.type === activeFilter);
```

**Verification:**
- 4 tabs render horizontally
- Active tab matches URL param (`/notifications?filter=case`)
- Filter counts shown as badges (e.g., "เคสของฉัน (3)")
- Switching tabs is instant (client-side filter)
- Empty state per tab: "ไม่มีการแจ้งเตือนในหมวดนี้"

---

### 7.2: Notification Cards — Tone, Icon, Title, Body, CTA

**Approach:**
Each notification is a card with colored left-border indicating tone (amber/blue/green/gray), an icon, title, body text, timestamp, and optional CTA button linking to the relevant page.

**Code Strategy:**

```typescript
// components/NotificationCard.tsx
type NotificationTone = 'amber' | 'blue' | 'green' | 'gray';

interface Notification {
  id: string;
  type: 'case' | 'document' | 'system';
  tone: NotificationTone;
  icon: string;        // emoji as icon
  title: string;
  body: string;
  timestamp: string;
  cta?: { label: string; href: string };
  read: boolean;
}

const toneStyles: Record<NotificationTone, string> = {
  amber: 'border-l-amber-500 bg-amber-50',
  blue: 'border-l-blue-500 bg-blue-50',
  green: 'border-l-green-500 bg-green-50',
  gray: 'border-l-gray-300 bg-gray-50',
};

export function NotificationCard({ notification }: { notification: Notification }) {
  return (
    <div className={`p-4 border-l-4 rounded-r-lg ${toneStyles[notification.tone]} ${notification.read ? 'opacity-60' : ''}`}>
      <div className="flex items-start gap-3">
        <span className="text-xl">{notification.icon}</span>
        <div className="flex-1">
          <h4 className="font-medium">{notification.title}</h4>
          <p className="text-sm text-gray-600 mt-1">{notification.body}</p>
          <p className="text-xs text-gray-400 mt-2">{notification.timestamp}</p>
          {notification.cta && <Link href={notification.cta.href} className="text-pink-500 text-sm mt-2 inline-block">{notification.cta.label} →</Link>}
        </div>
        {!notification.read && <span className="w-2 h-2 rounded-full bg-pink-500 flex-shrink-0 mt-1" />}
      </div>
    </div>
  );
}
```

**Verification:**
- Cards render with correct tone color
- Amber tone: warning/system alerts → amber border + bg
- Blue tone: case updates → blue border + bg
- Green tone: completion messages → green border + bg
- Gray tone: informational → gray border + bg
- Unread: pink dot indicator + full opacity
- Read: no pink dot + 60% opacity
- CTA link navigates correctly
- Timestamp displays in Thai format (relative: "2 ชั่วโมงที่แล้ว" or absolute: "10 ส.ค. 2569")

---

### 7.3: Mark All Read Button — Toast Feedback

**Approach:**
A "อ่านทั้งหมด" button at the top of the notifications page. On click, marks all notifications as read and shows a toast: "อ่านทั้งหมดแล้ว ✅"

**Code Strategy:**

```typescript
function MarkAllReadButton() {
  const { mutate } = useMarkAllRead();

  return (
    <Button variant="ghost" onClick={() => {
      mutate();
      toast.success('อ่านทั้งหมดแล้ว ✅', { duration: 3000 });
    }}>
      📖 อ่านทั้งหมด
    </Button>
  );
}
```

**Verification:**
- Button visible when unread count > 0
- Click → all notifications marked read (opacity change, pink dots removed)
- Toast appears: "อ่านทั้งหมดแล้ว ✅"
- Toast auto-dismisses in 3 seconds
- Button hidden or disabled when all already read
- Unread count badge in tab/header updates to 0

---

## 💬 SECTION 8: AI Assistant

### 8.1: Chat Interface with DeepSeek AI

**Approach:**
A full chat UI at `/assistant` with message bubbles (user on right, AI on left), a text input at the bottom, and a send button. Messages stream from DeepSeek API. Conversation history is maintained in state and sent with each request for context.

**Code Strategy:**

```typescript
// app/assistant/page.tsx
interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  citations?: SourceCitation[];
  timestamp: string;
}

export default function AssistantPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg: Message = { id: nanoid(), role: 'user', content: input, timestamp: new Date().toISOString() };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsStreaming(true);

    // Stream AI response
    const response = await fetch('/api/assistant', {
      method: 'POST',
      body: JSON.stringify({ messages: [...messages, userMsg], category: 'general' }),
    });
    // Read stream...
  };

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map(msg => <ChatBubble key={msg.id} message={msg} />)}
        {isStreaming && <TypingIndicator />}
        <div ref={messagesEndRef} />
      </div>
      <ChatInput value={input} onChange={setInput} onSend={sendMessage} disabled={isStreaming} />
    </div>
  );
}
```

**Verification:**
- Type message → click send → user bubble appears on right → AI response streams on left
- Scroll auto-follows as new messages arrive
- Empty input → send disabled
- Long messages wrap correctly
- Mobile: full-height layout, keyboard aware
- AI responses include Thai legal context
- Message history persists within session (page refresh → clears)

---

### 8.2: Typing Indicator While AI Thinks

**Approach:**
An animated typing indicator (3 bouncing dots) shown in the AI's bubble position while the response is being streamed. This provides feedback that the system is working.

**Code Strategy:**

```typescript
function TypingIndicator() {
  return (
    <div className="flex items-start gap-3">
      <BotIcon className="w-8 h-8 rounded-full bg-pink-100 p-1" />
      <div className="bg-gray-100 rounded-2xl rounded-tl-sm px-4 py-3">
        <div className="flex gap-1">
          <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
          <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
          <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
        </div>
      </div>
    </div>
  );
}
```

**Verification:**
- Indicator appears immediately after user sends message
- 3 dots bounce sequentially (staggered animation)
- Indicator removed when AI response starts streaming
- Indicator replaced by actual AI message content as tokens arrive
- Color scheme consistent with AI bubble styling

---

### 8.3: Quick Replies in Welcome Message

**Approach:**
When the chat is empty (no messages), show a welcome message from the AI with 3 clickable quick-reply buttons. Clicking a quick reply sends that as a user message.

**Code Strategy:**

```typescript
const QUICK_REPLIES = [
  { label: 'ฉันถูกเลิกจ้างไม่เป็นธรรม', query: 'ฉันถูกเลิกจ้างไม่เป็นธรรม ต้องทำอย่างไรบ้าง?' },
  { label: 'ซื้อของออนไลน์ไม่ได้ของ', query: 'สั่งของออนไลน์แล้วไม่ได้รับสินค้า จะดำเนินการอย่างไร?' },
  { label: 'ต้องการทำพินัยกรรม', query: 'ต้องการทำพินัยกรรม มีขั้นตอนอะไรบ้าง?' },
];

function WelcomeMessage({ onQuickReply }: { onQuickReply: (query: string) => void }) {
  return (
    <div className="text-center py-8">
      <BotIcon className="w-16 h-16 mx-auto text-pink-400" />
      <h2 className="text-xl font-semibold mt-4">สวัสดี! 🎀</h2>
      <p className="text-gray-500 mt-2">ฉันคือผู้ช่วย AI ด้านกฎหมายไทย ถามฉันได้เลย!</p>
      <div className="flex flex-wrap gap-2 justify-center mt-6">
        {QUICK_REPLIES.map(qr => (
          <button key={qr.label} onClick={() => onQuickReply(qr.query)}
            className="px-4 py-2 border border-pink-200 text-pink-600 rounded-full hover:bg-pink-50 transition text-sm">
            {qr.label}
          </button>
        ))}
      </div>
    </div>
  );
}
```

**Verification:**
- Welcome message visible when messages array is empty
- 3 quick reply buttons rendered
- Click any → that query sent as user message → AI responds
- After first message, welcome section hidden (chat takes over)
- Buttons have hover effect

---

### 8.4: Suggested Prompts (3 Buttons)

**Approach:**
After the AI responds, show 3 suggested follow-up prompts below the AI message. These are contextually generated based on the conversation. Clicking one sends it as the next user message.

**Code Strategy:**

```typescript
function SuggestedPrompts({ prompts, onSelect }: { prompts: string[]; onSelect: (prompt: string) => void }) {
  if (!prompts.length) return null;

  return (
    <div className="ml-12 mt-2 space-y-1">
      <p className="text-xs text-gray-400 mb-1">💡 คำถามที่อาจสนใจ:</p>
      {prompts.map((prompt, i) => (
        <button key={i} onClick={() => onSelect(prompt)}
          className="block text-sm text-pink-600 hover:text-pink-700 hover:underline text-left">
          {prompt}
        </button>
      ))}
    </div>
  );
}
```

**AI Prompt Instruction:**
```
At the end of your response, suggest 2-3 follow-up questions the user might want to ask, formatted as:
__SUGGESTED_PROMPTS__: ["question 1", "question 2", "question 3"]
```

**Verification:**
- 2-3 suggested prompts visible below each AI response
- Prompts are contextually relevant (not the same 3 every time)
- Click → sent as user message
- Rendered in the AI bubble's column (indented)
- "คำถามที่อาจสนใจ" label is subtle (gray, small)

---

### 8.5: SourceCitation Display

**Approach:**
When the AI response includes legal citations (from `LEGAL_SOURCES` registry), display them as styled citation cards below the message. Each card shows: law name, relevant section, and a link to the source.

**Code Strategy:**

```typescript
interface SourceCitation {
  sourceId: string;
  section: string;
  excerpt: string;
}

function CitationCard({ citation }: { citation: SourceCitation }) {
  const source = resolveSource(citation.sourceId);
  if (!source) return null; // Anti-hallucination guard

  return (
    <div className="bg-gray-50 border rounded-lg p-3 text-sm">
      <div className="flex items-center gap-2">
        <BookIcon className="w-4 h-4 text-gray-500" />
        <span className="font-medium">{source.shortName}</span>
      </div>
      <p className="text-gray-600 mt-1">{citation.section}: {citation.excerpt}</p>
    </div>
  );
}
```

**Verification:**
- Citation displayed only if `resolveSource()` returns non-null (anti-hallucination)
- Citation card shows: book icon, law short name, section, excerpt
- Clicking citation could expand to show full section text
- Multiple citations render as a list
- No citation → no empty citation section shown

---

### 8.6: Disclaimer — "AI อาจให้ข้อมูลคลาดเคลื่อน"

**Approach:**
A persistent disclaimer shown at the bottom of every AI response in the chat: "⚕️ AI อาจให้ข้อมูลคลาดเคลื่อน ควรตรวจสอบกับทนายความก่อนดำเนินการ" — smaller font, gray text, always visible.

**Verification:**
- Disclaimer after every AI message (not user messages)
- Text matches guardrail `disclaimer-required` wording
- Small, gray, unobtrusive but always visible
- Present even on streaming/incomplete responses

---

### 8.7: Menu + "เปลี่ยน" Button Handlers

**Approach:**
A hamburger menu (☰) in the chat header that opens a dropdown with: "เริ่มการสนทนาใหม่" (clear chat), "เปลี่ยนหมวดกฎหมาย" (change category context), and "ดูประวัติ" (view past conversations). The "เปลี่ยน" button is a quick-access chip to change the legal category context for the AI.

**Code Strategy:**

```typescript
function AssistantMenu() {
  const [open, setOpen] = useState(false);
  const [category, setCategory] = useState<string>('general');

  const handleNewChat = () => {
    setMessages([]);
    setOpen(false);
    toast.info('เริ่มการสนทนาใหม่แล้ว');
  };

  const handleChangeCategory = (newCategory: string) => {
    setCategory(newCategory);
    setOpen(false);
    toast.success(`เปลี่ยนเป็นหมวด ${CATEGORY_META[newCategory]?.label || newCategory}`);
  };

  return (
    <div className="flex items-center gap-2">
      {/* Quick category chip */}
      <button onClick={() => setOpen(true)} className="flex items-center gap-1 px-3 py-1 bg-pink-50 text-pink-600 rounded-full text-sm">
        {CATEGORY_META[category]?.icon} {CATEGORY_META[category]?.label || 'ทั่วไป'} ↕ เปลี่ยน
      </button>

      {/* Hamburger menu */}
      <DropdownMenu open={open} onOpenChange={setOpen}>
        <DropdownMenuTrigger><MenuIcon /></DropdownMenuTrigger>
        <DropdownMenuContent>
          <DropdownMenuItem onClick={handleNewChat}>🔄 เริ่มการสนทนาใหม่</DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuLabel>เปลี่ยนหมวดกฎหมาย</DropdownMenuLabel>
          {Object.entries(CATEGORY_META).map(([slug, meta]) => (
            <DropdownMenuItem key={slug} onClick={() => handleChangeCategory(slug)}>
              {meta.icon} {meta.label}
            </DropdownMenuItem>
          ))}
          <DropdownMenuSeparator />
          <DropdownMenuItem onClick={() => router.push('/cases')}>📋 ดูประวัติ</DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  );
}
```

**Verification:**
- Hamburger menu opens dropdown with all 3 sections
- "เริ่มการสนทนาใหม่" → clears messages + toast
- "เปลี่ยนหมวดกฎหมาย" → submenu with all 12 categories
- Selecting a category → chip updates + context sent with next AI request
- "ดูประวัติ" → navigates to `/cases`
- Menu closes after any selection
- Category chip reflects current context
- "เปลี่ยน" button always visible in header

---

## 🔗 Cross-Cutting Concerns for Sections 1-8

### State Management Pattern

```typescript
// Use a lightweight approach — React Context + useReducer for complex state:
const DiagnosisContext = createContext<{
  phase: WizardPhase;
  category: CategorySlug | null;
  fearLevel: FearLevel | null;
  answers: Record<string, string | string[]>;
  result: AnalysisResult | null;
  dispatch: React.Dispatch<DiagnosisAction>;
} | null>(null);
```

### API Routes Needed

| Route | Method | Purpose | Section |
|-------|--------|---------|---------|
| `/api/diagnosis` | POST | Submit answers, get AI analysis | 1 |
| `/api/search` | GET | AI-powered legal search | 4 |
| `/api/assistant` | POST | Streaming chat with DeepSeek | 8 |
| `/api/cases` | GET/POST | List/create cases | 6 |
| `/api/cases/[id]/evidence` | POST | Upload evidence files | 6 |
| `/api/notifications` | GET | Fetch notifications | 7 |
| `/api/notifications/read-all` | POST | Mark all read | 7 |

### Guardrail Integration

Every AI response (diagnosis, search, assistant) passes through:

```typescript
import { checkGuardrails } from '@/lib/guardrails';

function validateAIResponse(response: AnalysisResult): { valid: true } | { valid: false; violations: string[] } {
  const violations = checkGuardrails(response);
  if (violations.length > 0) {
    return { valid: false, violations };
  }
  // Verify all source IDs
  const validSources = resolveSources(response.relevantLaws.map(l => l.id));
  if (validSources.length === 0 && response.relevantLaws.length > 0) {
    return { valid: false, violations: ['no-fabricated-sources: all source IDs failed resolution'] };
  }
  return { valid: true };
}
```

### Backend Tech Stack Recommendation

- **Framework:** Next.js 14+ (App Router)
- **AI SDK:** Vercel AI SDK with DeepSeek provider
- **Styling:** Tailwind CSS + shadcn/ui
- **State:** React Context + SWR for server state
- **File Upload:** UploadThing or direct S3 presigned URLs
- **DB:** PostgreSQL via Prisma or Supabase

---

## 📊 Verification Checklist Summary

| Section | Key Metric | Target |
|---------|-----------|--------|
| 1. AI Diagnosis | All 48 questions (12×4) present | 48 items in data |
| 1. AI Diagnosis | Wizard phases render correctly | 6 phases, all states |
| 2. 45 Problems | All problems defined | 45 items in data |
| 2. 45 Problems | Urgency badges correct | 3 tone levels |
| 3. Category Pages | 12 dynamic routes | No 404s |
| 3. Category Pages | Sidebar cross-nav | 11 other categories |
| 4. Search | AI-powered dynamic search | Real API response (not static) |
| 4. Search | Sort + share + save | All interactive |
| 5. Legal Sources | 36 sources | Correct count |
| 5. Legal Sources | Anti-hallucination | `resolveSource(fake)` → null |
| 6. Case Management | 4 filter tabs | Working filters |
| 6. Case Management | Evidence upload + checklist | Drag-drop + readiness score |
| 7. Notifications | 4 filter tabs + mark all read | Toast feedback |
| 7. Notifications | 4 tone levels | amber/blue/green/gray |
| 8. AI Assistant | Full chat with streaming | Real DeepSeek responses |
| 8. AI Assistant | Quick replies + suggested prompts | Interactive buttons |
