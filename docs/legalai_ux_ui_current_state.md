# LegalAI Citizen — CURRENT STATE UX/UI Report

> **Generated:** 2026-08-12  
> **Source:** `D:\legalai-citizen-latest\app\` (23 page files)  
> **Framework:** Next.js App Router (React 18+ client components)  
> **Language:** Thai-primary with English mixed for legal terms  

---

## / — หน้าแรก (Home)
**File:** `app/page.tsx` | **Type:** Client component (`"use client"`)

### Section: Welcome Banner
- Element: `<Pill>` — "✦ AI ที่เข้าใจกฎหมายไทย"
- Element: `<h1>` — "สวัสดีค่ะ คุณนภัสสร 👋"
- Element: `<p>` — "วันนี้มีเรื่องกฎหมายอะไรให้เราช่วยดูแลคะ?"
- Element: Date card showing Thai weekday + day + month + "2569"
- Algorithm: `formatThaiToday()` — client-only date (avoids hydration mismatch). Uses `useState(null)` → `useEffect` to fill after mount. Thai weekday names + month names arrays.
- Data: System clock (client-side)
- Status: Working

### Section: Hero Search
- Element: `<Pill tone="white">` — "ค้นหาคำตอบได้ทันที"
- Element: `<h2>` — "เรื่องกฎหมายไม่ต้องเป็นเรื่องยากอีกต่อไป"
- Element: `<p>` — "พิมพ์คำถามด้วยภาษาของคุณ เราจะช่วยสรุปให้เข้าใจง่าย พร้อมบอกขั้นตอนที่ควรทำต่อ"
- Element: Search `<input>` — placeholder: "เช่น ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า ทำอย่างไร?"
- Element: Search `<button>` — "ค้นหา"
- Element: Quick Search buttons — "ถูกโกงออนไลน์", "นายจ้างไม่จ่ายเงิน", "ขอคืนเงิน", "สัญญาเช่า"
  - Label: "ค้นหายอดนิยม:"
- Algorithm: `search()` — default query fallback "นายจ้างเลิกจ้างโดยไม่แจ้งล่วงหน้า". `recordEvent({type:"search_submitted"})`. Routes to `/search?q=...`
- Data: Hardcoded `quickSearches` array
- Status: Working

### Section: Categories Grid ("เริ่มต้นจากเรื่องที่คุณสนใจ")
- Element: `<h3>` — "เริ่มต้นจากเรื่องที่คุณสนใจ"
- Element: `<p>` — "เลือกหมวดหมู่เพื่อดูคำแนะนำเบื้องต้น"
- Element: Link — "ดูทั้งหมด →" → `/categories`
- Element: Category cards — iterate `categories` from `@/lib/mock/categories`. Each card: icon, `<strong>`title, `<small>`hint. Links to `/categories/{id}`.
- Algorithm: `recordEvent({type:"search_submitted", category})` on click.
- Data: Mock (`categories` from `@/lib/mock/categories`)
- Status: Working

### Section: Action Grid
- Card 1: `/diagnosis` — SparklesIcon + Pill "แนะนำ" — "วิเคราะห์เคสของฉัน" / "ตอบคำถามสั้น ๆ แล้ว AI จะช่วยวิเคราะห์สิทธิ หลักฐาน และขั้นตอนถัดไป" / CTA: "เริ่มวิเคราะห์ฟรี →" / variant: "ai"
- Card 2: `/documents` — DocIcon — "สร้างเอกสารกฎหมาย" / "หนังสือทวงถาม ร้องเรียน หรือบอกเลิกสัญญา พร้อมใช้งาน" / CTA: "เลือกเอกสาร →"
- Card 3: `/lawyers` — ScaleIcon — "ปรึกษาทนายที่เหมาะกับคุณ" / "ค้นหาทนายที่ผ่านการตรวจสอบ พร้อมดูราคาและขอบเขตชัดเจน" / CTA: "ค้นหาทนาย →"
- Card 4: `/tax` — 💰 emoji — "วางแผนภาษี" / "คำนวณภาษีเงินได้บุคคลธรรมดา วางแผนลดหย่อน และประหยัดภาษีสูงสุด" / CTA: "ลองคำนวณ →" / variant: "tax"
- Card 5: `/pricing` — 💳 emoji — "อัปเกรดแพ็กเกจ" / "ปลดล็อกฟีเจอร์เพิ่ม — เอกสารไม่จำกัด ปรึกษาทนาย และ LINE แจ้งเตือน" / CTA: "ดูแพ็กเกจ →"
- Data: Hardcoded `actions` array
- Status: Working

### Section: Case Preview
- Element: `<h3>` — "เคสที่กำลังดำเนินการ"
- Element: `<p>` — "ทำต่อจากจุดที่ค้างไว้"
- Element: Link — "ดูเคสทั้งหมด →" → `/cases`
- Element: `<CaseProgressCard>` with `sampleCases[0]` → links to `/cases/case-1/timeline`
- Data: Mock (`sampleCases` from `@/lib/mock/categories`)
- Status: Working

### Section: Trust Strip
- Element: ShieldIcon + `<strong>` — "ข้อมูลของคุณได้รับการปกป้อง"
- Element: `<small>` — "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
- Element: `<PrototypeDataNotice />`
- Data: Static
- Status: Working

---

## /categories — เลือกหมวดหมู่ปัญหากฎหมาย
**File:** `app/categories/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "🔍 เลือกหมวดหมู่ปัญหากฎหมาย" / subtitle: "เลือกหมวดที่ตรงกับปัญหาของคุณ — AI จะถามคำถามทีละข้อ"
- Data: Static
- Status: Working

### Section: Category Grid
- Element: Cards for each category from `categories`. Each shows icon (fontSize 32), `<h3>` title, `<small>` hint, question preview ("N คำถาม — q1 · q2 · q3"), and "เริ่มวิเคราะห์ →" link. Links to `/diagnosis?category={id}`.
- Algorithm: `getDiagnosisConfig(cat.id)` — loads question config per category. Shows question count and titles.
- Data: Mock (`categories`, `getDiagnosisConfig`)
- Status: Working

### Section: Privacy Note
- Element: "⌾ คำตอบของคุณใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น — เราไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
- Data: Static
- Status: Working

### Section: Social Proof
- Element: `<SocialProofInline />`
- Data: Component from `@/components/trust/social-proof`
- Status: Working

---

## /categories/[category] — รายละเอียดหมวดหมู่
**File:** `app/categories/[category]/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: `"{icon} {cat.title}"` / subtitle: `{cat.hint}`
- Data: Mock (from `categories`)
- Status: Working

### Section: Drive-Aware Emotional Framing
- Element: Blue-tinted banner with 💡 icon + `{driveProfile.motivationHook}` (e.g., dynamic motivational copy per category)
- Element: `<SocialProofInline category={...}>`
- Algorithm: `getCategoryDriveProfile()`, `getCategoryDriveLabels()`, `getEmotionalFrame()`, `getLossAversionMessage()` — consumer psychology functions from `@/lib/legal/category-drives`
- Data: Mock drive profiles per category
- Status: Working

### Section: Drive Labels
- Element: Pill-style labels — `{driveLabels}` rendered as rounded gray tags
- Data: `getCategoryDriveLabels()` per category
- Status: Working

### Section: Common Problems ("📋 ปัญหาที่พบบ่อยในหมวดนี้")
- Element: Problem cards with `<strong>` title, urgency `<Pill tone="amber">`, description `<p>`
- Data: `PROBLEM_EXAMPLES` — exhaustive hardcoded map for all 12 categories (online_fraud, crime, defamation, insurance, government, property, labour, consumer, debt, housing, family, accident). Each entry has title, desc, urgency.
- Status: Working

### Section: AI Diagnosis Preview ("🤖 AI จะถามคุณ")
- Element: Numbered question list — `{i+1}` + `<strong>`q.title + optional `<small>`q.rationale
- Algorithm: `config.questions` from `getDiagnosisConfig()`
- Data: Mock diagnosis config
- Status: Working

### Section: CTA Button
- Element: Link — "🤖 เริ่มวิเคราะห์เคสของฉัน" → `/diagnosis?category={catId}`
- Element: `<p>` — "ใช้เวลาประมาณ 3 นาที • ข้อมูลของคุณปลอดภัย"
- Status: Working

### Section: Sidebar
- Loss Aversion Card: "⚠️ อย่ารอจนสาย" / `{lossMessage}` — urgent consequence messaging
- Social Proof Card: `<SocialProofCard>`
- Quick Actions: "🔍 ค้นหาคำถามที่พบบ่อย", "📄 สร้างเอกสารที่เกี่ยวข้อง", "👨‍⚖️ ปรึกษาทนายผู้เชี่ยวชาญ"
- Legal Sources: "⚖️ กฎหมายที่เกี่ยวข้อง" — iterates `sourcesForCategory()`. Labels: "กฎหมาย" / "ประกาศ" / "คำแนะนำ"
- Related Categories: "📂 หมวดอื่นๆ" — other categories linked
- Algorithm: `sourcesForCategory(catId)` for legal source lookup
- Data: Mock (sources, drive profiles)
- Status: Working

### 404 State
- Element: `<PageHead>` — "ไม่พบหมวดหมู่" / "หมวดหมู่ที่คุณค้นหาไม่มีอยู่ในระบบ"
- Element: Link — "← กลับหน้าเลือกหมวดหมู่"
- Status: Working

---

## /diagnosis — AI วิเคราะห์เคส (Diagnosis Wizard)
**File:** `app/diagnosis/page.tsx` | **Type:** Client component

### Section: Focus Layout Header
- Element: Back button `‹` → router back or `/`
- Element: `<Brand />` component
- Element: Close `×` → `/`
- Status: Working

### Section: Progress Bar
- Element: "หาเส้นทางที่เหมาะกับเรื่องของคุณ"
- Element: "ขั้นตอน {step} จาก {TOTAL}"
- Element: `<Progress value={(step/TOTAL)*100} />`
- Algorithm: `step` state (1-indexed), `TOTAL = questions.length`
- Status: Working

### Section: Question Card (Intake State)
- Element: AI orb `✦`
- Element: `<Pill>` — "ตอบเท่าที่ทราบ • กลับมาแก้ได้"
- Element: `<h1>` — `{q.title}` (current question title)
- Element: `<p>` — `{q.rationale}` (why this question matters)
- Element: Radio/checkbox options — letter-labeled (A, B, C...), with `✓` indicator
  - Single-select: radio inputs
  - Multi-select (evidence): checkbox inputs
- Element: Navigation buttons — "ย้อนกลับ" + "ถัดไป →" (last step: "ดูผลวิเคราะห์ →")
- Algorithm: `selectAnswer(option)` — single vs multi toggle. `canProceed()` validates at least one selection. `runAnalysis()` POSTs to `/api/ai/diagnosis` with `{category, answers}`. Stores result in `sessionStorage` key `legalai:latest-analysis`. Routes to `/analysis/case-1?session=new`. Records analytics events `diagnosis_started`, `diagnosis_completed`.
- Data: Real API (`POST /api/ai/diagnosis`) — DeepSeek AI backend
- Status: Working (live API)

### Section: Loading State
- Element: AI orb `✦`
- Element: `<Pill tone="blue">` — "กำลังประมวลผล"
- Element: `<h1>` — "AI กำลังวิเคราะห์เคสของคุณ..."
- Element: `<p>` — "DeepSeek ใช้เวลาพิจารณาเหตุการณ์และสิทธิของคุณ ปกติใช้เวลาประมาณ 30–90 วินาที กรุณาอย่าปิดหน้าต่างนี้"
- Element: Indeterminate `<Progress value={70} />`
- Element: Privacy note — "⌾ คำตอบของคุณถูกส่งเพื่อวิเคราะห์เท่านั้น และไม่ถูกเก็บไว้ที่อื่น"
- Algorithm: `status === "loading"` state during API call
- Data: Real API pending
- Status: Working

### Section: Error State
- Element: AI orb `⚠`
- Element: `<Pill tone="amber">` — "เกิดข้อผิดพลาด"
- Element: `<h1>` — "ไม่สามารถวิเคราะห์ได้"
- Element: `<p>` — error message (default: "ไม่สามารถวิเคราะห์ได้ในขณะนี้ กรุณาลองอีกครั้ง")
- Element: Buttons — "ย้อนกลับ" + "ลองอีกครั้ง →"
- Algorithm: `status === "error"` state. `retry()` resets to intake.
- Status: Working

### Config
- Valid categories: labour, consumer, debt, housing, family, accident, online_fraud, crime, government, insurance, defamation, property
- Default category when no query param: "labour"
- Privacy: Answers never sent to analytics

---

## /search — ผลการค้นหา
**File:** `app/search/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: Back link `‹` → `/`
- Element: `<h1>` — "ผลการค้นหา"
- Element: `<p>` — "คำแนะนำที่เข้าใจง่ายและนำไปใช้ได้จริง"
- Status: Working

### Section: Search Box (Standalone)
- Element: SearchIcon + input (placeholder: "พิมพ์ปัญหากฎหมายของคุณ...") + button "ค้นหา"
- Algorithm: `search()` — routes to `/search?q=...`. Uses `useSearchParams()` for initial query.
- Status: Working

### Section: Empty State
- Element: "🔍 พิมพ์ปัญหากฎหมายของคุณด้านบน — เช่น \"ถูกเลิกจ้าง\", \"ถูกโกงออนไลน์\", \"สัญญาเช่า\""
- Status: Working

### Section: Results (when query exists)
- Element: Sort dropdown — "เกี่ยวข้องมากที่สุด" / "ใหม่ที่สุด" / "เก่าที่สุด"
- Element: Disclaimer — "ผลค้นหาเป็นข้อมูลกฎหมายเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย"

#### AI Answer Card (loading)
- SparklesIcon + `<Pill tone="blue">` — "AI กำลังวิเคราะห์..."
- `<h2>` — "กำลังค้นหาคำตอบสำหรับ \"{query}\""
- "⏳ AI กำลังประมวลผล — กรุณารอสักครู่..."
- Algorithm: Fetches `POST /api/ai/assistant` with Thai prompt asking 3-part analysis
- Data: Real API (`/api/ai/assistant`)
- Status: Working

#### AI Answer Card (error)
- ⚠ + `<Pill tone="amber">` — "เกิดข้อผิดพลาด"
- Error text + Link "✦ วิเคราะห์เคสของฉัน" → `/diagnosis`
- Status: Working

#### AI Answer Card (success)
- SparklesIcon + `<Pill>` — "คำตอบแนะนำโดย LegalAI"
- `<h2>` — "ผลการค้นหาสำหรับ \"{query}\""
- Result text (pre-wrap)
- Disclaimer: "ⓘ ข้อมูลนี้เป็นคำแนะนำเบื้องต้น ผลลัพธ์จริงขึ้นอยู่กับรายละเอียดของแต่ละกรณี"
- Actions: "✦ วิเคราะห์เคสของฉัน" + "♡ บันทึก" toggle + "↗ แชร์"
  - Share: uses `navigator.share` or falls back to `clipboard.writeText`
- Status: Working

### Section: Recommended Steps ("ขั้นตอนที่แนะนำ")
- Static 3-step cards: "1 รวบรวมหลักฐาน" / "2 ประเมินสิทธิ" / "3 ดำเนินการตามขั้นตอน"
- Data: Static `STATIC_STEPS` array
- Status: Working

### Section: Related Articles ("บทความที่เกี่ยวข้อง")
- 3 articles: "สิทธิทางกฎหมายที่ควรรู้", "วิธีดำเนินการเบื้องต้น", "หน่วยงานที่เกี่ยวข้อง"
- Each shows DocIcon + title + "อ่าน N นาที • ตรวจสอบโดยทนาย"
- Algorithm: `handleArticleClick()` — shows toast notification only (not navigable)
- Data: Static
- Status: Partial (toast-only, no article pages)

### Section: Sidebar
- AI CTA Card: SparklesIcon + "อยากได้คำตอบที่ตรงกับเคสของคุณ?" / "ตอบคำถามเพียง 4 ข้อ ใช้เวลาประมาณ 3 นาที" / Link "เริ่มวิเคราะห์ฟรี"
- Document Category Card: "📄 เอกสารธุรกิจที่เกี่ยวข้อง" — shows `suggestCategory()` result + `DOCUMENT_CATEGORIES` matches
  - "📋 ดูเอกสารทั้งหมด 126+ รายการ →"
  - Algorithm: `suggestCategory(initial)` from `@/lib/documents/categories`
- Data: Mock (document categories)
- Status: Working

---

## /documents — สร้างเอกสารกฎหมาย
**File:** `app/documents/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "สร้างเอกสารกฎหมาย" / subtitle: "กรอกง่าย ใช้ภาษาถูกต้อง พร้อมดาวน์โหลดและส่งได้ทันที"
- Data: Static
- Status: Working

### Section: Disclaimer
- Element: "เอกสารที่สร้างเป็นแบบร่าง ควรตรวจสอบโดยผู้เชี่ยวชาญก่อนใช้งาน"
- Status: Working

### Section: Document Type Grid ("เอกสารที่เหมาะกับคุณ")
- 4 quick-start document types:
  1. "▤ หนังสือทวงถามค่าชดเชย" — Pill "แนะนำ" (blue) — "สำหรับแจ้งนายจ้างให้ชำระสิทธิที่ค้าง"
  2. "□ หนังสือร้องเรียนผู้บริโภค" — Pill "ยอดนิยม" (green) — "ร้องเรียนสินค้าและบริการที่ไม่เป็นธรรม"
  3. "⌂ หนังสือบอกเลิกสัญญาเช่า" — "แจ้งยุติสัญญาอย่างเป็นทางการ"
  4. "฿ หนังสือทวงหนี้" — "ระบุยอดหนี้และกำหนดวันชำระ"
- Algorithm: `useState(doc)` tracks selected document
- Data: Hardcoded `docTypes` array
- Status: Working

### Section: Document Builder (Paper Mockup)
- Element: Paper preview with "ย" logo, document title, placeholder lines, signature area "ลงชื่อ __________________"
- Element: `<Pill>` — "สร้างด้วย AI"
- Element: Feature list — "ใช้ภาษากฎหมายที่ถูกต้อง", "แก้ไขได้ทุกส่วน", "ดาวน์โหลดเป็น PDF หรือ Word"
- Element: `<PrototypeDataNotice />`
- Element: Button "เริ่มสร้างเอกสาร →"
- Element: "ใช้เวลาประมาณ 3–5 นาที"
- Algorithm: `startDraft()` — toast notification + `recordEvent({type:"document_draft_created"})`
- Data: Mock (no real generation yet)
- Status: Partial (toast-only, no real document generation)

### Section: Category Browser ("เรียกดูตามหมวดหมู่")
- Element: `<h3>` — "เรียกดูตามหมวดหมู่"
- Element: `<p>` — "{TOTAL_TEMPLATES} แบบฟอร์ม ใน {N} หมวดหมู่"
- Element: Search input (placeholder: "ค้นหาหมวดหมู่เอกสาร เช่น เช่า, สินเชื่อ, จ้าง...") with "ล้าง ✕" button
- Element: Category cards from `DOCUMENT_CATEGORIES` — icon, title_th, Pill with templateCount, subtitle_th
- Algorithm: `useMemo` filter by search term (matches title_th, subtitle_th, id). `handleCategoryClick()` routes to `cat.route`
- Empty state: "📭 ไม่พบหมวดหมู่ที่ตรงกับ ..." with "ล้างการค้นหา" button
- Bottom link: "ดูแบบฟอร์มทั้งหมด {TOTAL_TEMPLATES} รายการ →"
- Data: Mock (`DOCUMENT_CATEGORIES` from `@/lib/documents/categories`, `TOTAL_TEMPLATES`)
- Status: Working

---

## /documents/[category] — หมวดหมู่เอกสาร (Detail)
**File:** `app/documents/[category]/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` with backHref="/documents" — title: `{cat.title_th}`, subtitle: `{cat.subtitle_th}`, pill: `"{icon} {N} แบบฟอร์ม"`
- Data: Mock (`DOCUMENT_CATEGORIES`, `getTemplatesForCategory`)
- Status: Working

### Section: Category Info Card
- Element: Large icon (60x60), `<h2>` title_th, `<p>` subtitle_th, stats: "N แบบฟอร์ม", "N ฟรี" (green pill), "N เสียค่าบริการ" (amber pill)
- Data: Computed from templates
- Status: Working

### Section: Template List ("รายการแบบฟอร์ม (N รายการ)")
- Element: Per-template row — 📄 icon, template name, price badge (Pill "ฟรี" green or "฿N" amber), "เริ่มสร้าง →" button
- Algorithm: `handleCreateClick()` — records event + routes to `/documents/create?template=...&name=...&category=...&paid=...&price=...`
- Hover effects: blue border + box-shadow
- Empty state: "📭 ยังไม่มีแบบฟอร์มในหมวดนี้" + link "กลับไปเลือกหมวดหมู่อื่น →"
- Data: `getTemplatesForCategory(cat.id)` from `@/lib/documents/templates`
- Status: Working

### Section: Back Link
- Element: "← กลับไปเลือกหมวดหมู่อื่น"
- Status: Working

### 404 State
- Element: "📭 หมวดหมู่ ... ไม่พบในระบบ" + "กลับไปหน้าเอกสาร →"
- Status: Working

---

## /documents/create — สร้างเอกสาร
**File:** `app/documents/create/page.tsx` | **Type:** Client component (Suspense-wrapped)

### Section: Loading Fallback
- Element: ⏳ + "กำลังโหลด..."
- Status: Working

### Section: Page Header
- Element: `<PageHead>` — title: "สร้างเอกสาร", subtitle: template name, pill: "ฟรี" (green) or "฿N" (amber)
- Data: URL params (`template`, `name`, `category`, `paid`, `price`)
- Status: Working

### Section: Template Info Bar
- Element: 📄 icon + template name + "กรอกข้อมูลด้านล่างเพื่อสร้างเอกสาร — ดูตัวอย่างแบบเรียลไทม์ทางด้านขวา" + price badge
- Algorithm: `buildTemplateDoc(templateName, categoryId)` from `@/lib/documents/templates`
- Status: Working

### Section: Document Editor
- Element: `<DocumentEditor>` — templateId, templateContent (markdown), mergeFields, isPaid, priceThb, onGenerate callback
- Algorithm: `handleGenerate()` — records event + toast. Note: "In production, this would POST to /api/documents/generate"
- Data: Mock (merge fields generated from template)
- Status: Partial (toast-only, no real API)

### Section: Success State
- Element: Green banner ✅ + "เอกสาร ... พร้อมใช้งานแล้ว" / "คุณสามารถพิมพ์ PDF หรือดาวน์โหลด TXT ได้จากปุ่มด้านล่าง"
- Data: Generated flag
- Status: Working (UI only)

### Section: Back Link
- Element: "← กลับไปเลือกหมวดหมู่อื่น"
- Status: Working

### Missing Template State
- Element: "📭 ไม่พบข้อมูลแบบฟอร์ม — กรุณาเลือกจากหน้าเอกสาร" + "กลับไปหน้าเอกสาร →"
- Status: Working

---

## /tax — วางแผนภาษี
**File:** `app/tax/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "💰 วางแผนภาษี" / subtitle: "คำนวณภาษีเงินได้บุคคลธรรมดาและวางแผนลดหย่อน"
- Status: Working

### Section: Income Slider
- Element: `<label>` — "รายได้ต่อปี (บาท)" + range input (0–5,000,000, step 10,000)
- Element: Display — "฿{income.toLocaleString()}"
- State: `useState(600000)` default
- Status: Working

### Section: Action Buttons
- Element: Toggle button — "🔄 เปรียบเทียบแบบมี/ไม่มีลดหย่อน" / "🔽 ซ่อน"
- Element: Primary button — "🖨️ พิมพ์ / PDF"
- Algorithm: `compareMode` toggle. `handlePrint()` generates HTML with inline CSS + `printDocument()` from `@/lib/documents/export`
- Status: Working

### Section: Result Card
- Element: "รายได้สุทธิหลังหักลดหย่อน" — ฿{netIncome}
- Element: "ภาษีที่ต้องจ่าย" — ฿{tax} (red)
- Element: "อัตราภาษีจริง" — {effectiveRate}%
- Element: Savings banner — "✅ คุณประหยัดภาษีได้ ฿{savings} จากค่าลดหย่อน!" (conditional)
- Algorithm: `calcTax()` — progressive bracket calculation. `bracketBreakdown()` for per-bracket detail.
- Tax brackets (8): 0% (0-150k), 5% (150k-300k), 10% (300k-500k), 15% (500k-750k), 20% (750k-1M), 25% (1M-2M), 30% (2M-5M), 35% (5M+)
- Deduction classes (14): ส่วนตัว 60k, คู่สมรส 60k, บุตร 30k (max 3), พ่อแม่ 30k (max 2), ดอกเบี้ยบ้าน 100k, ประกันสุขภาพ 25k, ประกันชีวิต 100k, RMF 30% (max 500k), SSF 30% (max 200k), ThaiESG 30% (max 300k), ประกันสังคม 9k, บริจาค 10%, การศึกษา/กีฬา 30k, ฝากครรภ์ 60k
- Data: Hardcoded tax brackets (accurate per Thai Revenue Code)
- Status: Working

### Section: Comparison Mode
- Element: Two-column grid — "❌ ไม่มีลดหย่อน" (เฉพาะส่วนตัว 60,000) vs "✅ มีลดหย่อน"
- Each: tax amount, net income, effective rate
- Difference bar: "🎉 คุณประหยัดภาษีได้ ฿{savings} — ลดลง {percent}%" or "ไม่มีส่วนต่าง — ค่าลดหย่อนยังไม่ส่งผลกับอัตราภาษีของคุณ"
- Status: Working

### Section: Bracket Chart ("📊 ขั้นบันไดภาษี")
- Element: Horizontal bars per bracket — label, rate%, colored bar (low/mid/high tone), tax amount
- Active bracket indicator (▸)
- Info: "ⓘ คำนวณจากรายได้สุทธิ ฿{netIncome} — แถบสีแสดงอัตราภาษีแต่ละขั้น ▸ ขั้นที่คุณอยู่"
- Algorithm: `bracketBreakdown()`, `barTone(rate)` returns "low"/"mid"/"high"
- Status: Working

### Section: Deduction Selection ("📋 เลือกค่าลดหย่อน")
- Element: Chip buttons — icon + label + amount (or max) + ✓ when active
- Algorithm: `toggleDeduction(idx)` — calculates pct-based (RMF/SSF/ThaiESG/บริจาค) or fixed value. Respects `max` and `maxVal` limits.
- Status: Working

### Section: AI Tax Optimizer
- Element: "🤖 AI Tax Optimizer" card — gradient blue background
- Element: "AI จะวิเคราะห์รายได้ของคุณและแนะนำแผนลดหย่อนที่ประหยัดภาษีสูงสุด — รวมถึงลำดับการซื้อประกัน, RMF, SSF ที่เหมาะสมที่สุด"
- Element: 3 stat cards: "💰 ประหยัดสูงสุด ฿{income*0.15}", "📊 แผนแนะนำ RMF + SSF + ประกัน", "⏰ ภายใน 31 ธ.ค."
- Element: Button "🤖 ให้ AI วิเคราะห์แผนลดหย่อน"
- Status: Partial (UI only; optimizer button has no handler)

### Section: Filing Checklist ("📋 เช็คลิสต์ยื่นภาษี")
- Element: Progress bar + count "{checked}/{total}"
- 6 checklist items:
  1. "รวบรวมหนังสือรับรองการหักภาษี ณ ที่จ่าย (ทวิ 50)"
  2. "รวบรวมเอกสารลดหย่อน (ประกัน, RMF, SSF, ดอกเบี้ยบ้าน)"
  3. "ตรวจสอบยอดเงินได้ทั้งปีจากนายจ้าง"
  4. "คำนวณภาษีด้วยเครื่องคิดเลขด้านบน"
  5. "ยื่นแบบ ภ.ง.ด.90/91 ออนไลน์ที่ rd.go.th"
  6. "เก็บหลักฐานการยื่นแบบและใบเสร็จ"
- Celebration: "🎉 คุณทำครบทุกขั้นตอนแล้ว! พร้อมยื่นภาษีเรียบร้อย — ไปยื่นแบบออนไลน์กันเลย! 🚀"
- Element: "📤 เมื่อพร้อม — ยื่นแบบออนไลน์ ที่ efiling.rd.go.th" (external link)
- Algorithm: localStorage persistence (`legalai_tax_checklist`). `justCelebrated` state with 4s timeout.
- Status: Working

### Section: Sidebar
- "📅 กำหนดการภาษี" — ภ.ง.ด.90/91 (31 มี.ค.), RMF/SSF (31 ธ.ค.), ประกันชีวิต (31 ธ.ค.)
- "📊 อัตราภาษี" — bracket list
- "🤖 AI Tax Optimizer" card — "ให้ AI วิเคราะห์และแนะนำการวางแผนภาษีที่เหมาะกับคุณ" + "เปิดใช้งาน →" → `/tax/optimizer`
- Data: Static + internal link
- Status: Working

### Tax Note
- "ⓘ ข้อมูลนี้เป็นประมาณการเบื้องต้น — ควรตรวจสอบกับผู้เชี่ยวชาญด้านภาษีก่อนยื่นแบบ"
- Status: Working

---

## /pricing — แพ็กเกจและราคา
**File:** `app/pricing/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "💳 แพ็กเกจและราคา" / subtitle: "เลือกแพ็กเกจที่เหมาะกับคุณ — เริ่มต้นฟรี ไม่มีค่าใช้จ่ายแอบแฝง"
- Status: Working

### Section: Pricing Cards
- Element: Cards from `PACKAGE_ORDER` iterating `PACKAGES` (from `@/lib/packages/definitions`)
  - Featured card (sme_starter): "🌟 แนะนำ" badge
  - Header: `{pkg.name}` + `{pkg.nameEn}`
  - Price: "ฟรี" or "฿{monthly}/เดือน" + "หรือ ฿{priceTHB} แบบครั้งเดียว" or "฿{priceTHB} ต่อครั้ง"
  - Features list
  - CTA: "เริ่มใช้งานฟรี" (link to /auth/signin), "อัปเกรดเลย", "เลือกแพ็กเกจ"
- Data: Mock (`PACKAGES`, `PACKAGE_ORDER`)
- Status: Working

### Section: Feature Comparison Table ("📊 เปรียบเทียบฟีเจอร์")
- Columns per package, rows: AI วิเคราะห์คดี, Action Plan, เอกสารกฎหมาย, เอกสารธุรกิจ, อัปโหลดหลักฐาน, ปรึกษาทนาย, Tax Optimizer, LINE แจ้งเตือน, Priority Review, Team Access, Corporate Tax
- Data: Hardcoded HTML table
- Status: Working

### Section: FAQ ("❓ คำถามที่พบบ่อย")
- Q1: "เริ่มต้นฟรีจริงหรือ?" — "ใช่! แพ็กเกจฟรีให้คุณทดลองใช้ AI วิเคราะห์ 3 ครั้ง และดาวน์โหลดเอกสาร 1 ครั้ง โดยไม่ต้องกรอกบัตรเครดิต"
- Q2: "เปลี่ยนแพ็กเกจได้ไหม?" — "ได้ทุกเมื่อ — อัปเกรดหรือดาวน์เกรดผ่านหน้าโปรไฟล์"
- Q3: "ข้อมูลส่วนตัวปลอดภัยไหม?" — "เราเข้ารหัสข้อมูลตามมาตรฐานสากล — อ่านเพิ่มเติมในนโยบายความเป็นส่วนตัว" (link to /privacy)
- Status: Working

---

## /lawyers — ค้นหาทนาย
**File:** `app/lawyers/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "ปรึกษาทนายที่เหมาะกับคุณ" / subtitle: "ค้นหาทนายที่ผ่านการตรวจสอบ พร้อมดูราคาและขอบเขตที่ชัดเจน"
- Status: Working

### Section: Search and Filters
- Element: Search input (placeholder: "ค้นหาจากชื่อ, ความเชี่ยวชาญ...")
- Element: Specialty filter buttons — "ทั้งหมด" + categories from `SPECIALTY_LABELS`
- Element: Sort dropdown — "เกี่ยวข้องมากที่สุด" / "คะแนนสูง-ต่ำ" / "ประสบการณ์มาก-น้อย"
- Algorithm: `useMemo` filter by search term (name, specialties) + active specialty filter. Sort by selected sort key.
- Status: Working

### Section: Lawyer Cards
- Element: Per-lawyer card — initials avatar (blue gradient), name, specialties as pills, years experience, rating stars + review count
- Element: Price — "ค่าปรึกษา 30 นาที" / `{price}`
- Element: Button "ดูโปรไฟล์และนัดหมาย"
- Element: Save toggle "♡ บันทึก" / "✓ บันทึกแล้ว"
- Algorithm: `requestConsultation()` — routes to `/lawyers/{id}`. `toggleSave()` — local saved state.
- Data: Mock (`sampleLawyers` from `@/lib/mock/categories`)
- Status: Working

### Section: Sidebar
- AI Matching Card: "✦ ไม่แน่ใจว่าควรเลือกใคร?" / "ให้ AI ช่วยจับคู่ทนายจากประเภทเคส งบประมาณ และเวลาที่สะดวก" / Button "ให้ AI ช่วยเลือก" (toast-only)
- Verification Info: "เราตรวจสอบอะไรบ้าง" — "✓ ใบอนุญาตว่าความ", "✓ ทะเบียนภาษี", "✓ ประวัติและความเชี่ยวชาญ", "✓ รีวิวจากผู้ใช้จริง"
- `<PrototypeDataNotice />`
- Data: Static
- Status: Working

### Specialty Labels (Thai)
แรงงาน, ผู้บริโภค, หนี้และการเงิน, บ้านและที่อยู่อาศัย, ครอบครัวและมรดก, รถและอุบัติเหตุ, ภัยออนไลน์, อาชญากรรม, เรื่องราชการ, ประกันภัย, หมิ่นประมาท, ที่ดิน/ทรัพย์สิน

---

## /lawyers/[id] — โปรไฟล์ทนาย
**File:** `app/lawyers/[id]/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` backHref="/lawyers" — pill: `<Pill tone="green">` "✓ ตรวจสอบแล้ว", title: lawyer.displayName, subtitle: "{years} ปี • ภาษา {languages}"
- Element: Primary button "นัดหมายปรึกษา"
- Status: Working

### Section: Bio/Specialties Card ("เกี่ยวกับทนาย")
- Element: Initials avatar (64x64 blue gradient)
- Element: Specialties pills (blue) + online status "🟢 ออนไลน์" (green, if onlineSample)
- Element: Bio text — "ทนายความผู้เชี่ยวชาญด้าน{specialties} ด้วยประสบการณ์มากกว่า {years} ปี..."
- Element: Stats row — "คะแนน ★ {rating}", "รีวิว {count} รีวิว", "เริ่มต้น ฿{startingPrice}"
- Data: Mock (`sampleLawyers`)
- Status: Working

### Section: Scope of Service ("ขอบเขตการให้บริการ")
- Element: Per-scope row — 📋 icon, name, description, price (blue)
- Status: Working

### Section: Reviews ("รีวิวจากผู้ใช้บริการ")
- Element: Aggregate rating ★ + count
- Element: Per-review — author, star rating (★☆), text, date
- Element: `<PrototypeDataNotice label="รีวิวตัวอย่าง" />`
- Data: Mock (`sampleReviews` array — คุณสมชาย, คุณอรุณี, คุณวิชัย)
- Status: Working

### Section: Booking Widget ("🗓 นัดหมายปรึกษา")
- 3-step flow: select → confirm → done

#### Step: Select
- "เลือกบริการ" `<select>` — "เลือกบริการ", per-scope options "{name} • ฿{price}"
- "เลือกวันที่" `<select>` — next 7 days in Thai Buddhist calendar format
- "เลือกเวลา" — 2-column grid of 30-min slots (9:00–16:30, 16 slots)
- "หมายเหตุ (ไม่บังคับ)" `<textarea>` — placeholder "แจ้งรายละเอียดเคสโดยย่อ..."
- Button "ดำเนินการต่อ" (disabled until all selected)
- Button "ยกเลิก"
- Algorithm: `generateTimeSlots()` — 9:00-16:30 in 30-min intervals. Dates: next 7 days in Thai format (พุทธศักราช).
- Status: Working

#### Step: Confirm
- Summary: บริการ, วันที่ (Thai label), เวลา, ราคา (blue), optional note
- Buttons: "ย้อนกลับ" + "ยืนยันการจอง"
- Status: Working

#### Step: Done
- ✅ + "จองสำเร็จ!" + summary
- Buttons: "จองอีกครั้ง" + "ไปที่เคสของฉัน" → `/cases`
- Algorithm: `confirmBooking()` — toast "จองปรึกษาทนายเรียบร้อยแล้ว" + `recordEvent({type:"consultation_requested"})`
- Status: Working

### Section: Verification Info ("การตรวจสอบ")
- "✓ ใบอนุญาตทนายความ", "✓ ประวัติและความเชี่ยวชาญ", "✓ รีวิวจากผู้ใช้จริง", "✓ การรักษาความลับ"
- `<PrototypeDataNotice />`
- Status: Working

### 404 State
- "ไม่พบทนาย" / "ไม่พบข้อมูลทนายที่คุณค้นหา" / "ไม่พบข้อมูลทนายความ กรุณาลองใหม่อีกครั้ง" + "กลับไปค้นหาทนาย"
- Status: Working

---

## /profile — โปรไฟล์และการตั้งค่า
**File:** `app/profile/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "โปรไฟล์และการตั้งค่า" / subtitle: "จัดการข้อมูล บัญชี และความเป็นส่วนตัวของคุณ"
- Status: Working

### Section: Profile Card
- Element: Avatar "นภ" + edit button "✎"
- Element: `<h2>` — "นภัสสร วัฒนะ"
- Element: `<p>` — "napassorn@example.com • สมาชิกตั้งแต่ มิ.ย. 2569"
- Element: `<Pill>` — "แพ็กเกจพื้นฐาน"
- Element: Button "แก้ไขโปรไฟล์"
- Data: Hardcoded mock user
- Status: Working

### Section: Settings Navigation
- Tabs: "○ ข้อมูลส่วนตัว", "♧ การแจ้งเตือน", "⌾ ความเป็นส่วนตัว", "◫ การแสดงผล", "฿ แพ็กเกจและการชำระเงิน", "ⓘ ช่วยเหลือ"
- State: `activeTab` (SettingsTab)
- Status: Working

### Tab: ข้อมูลส่วนตัว (personal)
- Form fields: ชื่อ (default "นภัสสร"), นามสกุล (default "วัฒนะ"), อีเมล (default "napassorn@example.com"), เบอร์โทรศัพท์ (default "089 123 4567")
- Button "บันทึกการเปลี่ยนแปลง" (toast-only)
- Data: Hardcoded defaults
- Status: Partial (no persistence)

### Tab: การแจ้งเตือน (notifications)
- LINE connection card: LINE logo, status ("เชื่อมต่อแล้ว • รับการแจ้งเตือนผ่าน LINE" or "ยังไม่ได้เชื่อมต่อ"), Pill toggle, connect/disconnect button
- Email notification: select (เปิด/ปิด), default "on"
- Algorithm: `toggleLine()` — toggles state + toast "เชื่อมต่อ LINE แล้ว" / "ยกเลิกการเชื่อมต่อ LINE แล้ว" + records event
- Status: Partial (local state only, no LINE integration)

### Tab: ความเป็นส่วนตัว (privacy)
- AI Consent card: 🤖 icon, "AI Consent" text, toggle Pill (เปิด/ปิด), button เปิด/ปิด
  - Explanation: "เมื่อเปิด AI consent — ข้อมูลเคสของคุณจะถูกส่งให้ DeepSeek AI เพื่อวิเคราะห์ เมื่อปิด — ข้อมูลใหม่จะไม่ถูกส่งให้ AI แต่คุณจะยังใช้ฟีเจอร์อื่นได้ตามปกติ"
- PDPA Rights card: "📤 ส่งออกข้อมูลของฉัน" (toast: "กำลังส่งออกข้อมูล — เราจะส่งลิงก์ให้ทางอีเมลภายใน 24 ชม."), "🗑️ ลบข้อมูลของฉันทั้งหมด" (red, toast: "คำขอลบข้อมูลได้รับแล้ว — เราจะดำเนินการภายใน 30 วัน")
- Connected Accounts: LINE connection (same as notifications tab)
- Algorithm: `toggleAiConsent()` — toast "เปิดการประมวลผลด้วย AI แล้ว" / "ปิดการประมวลผลด้วย AI แล้ว — ข้อมูลใหม่จะไม่ถูกส่งให้ AI"
- Status: Partial (local state only, no actual API)

### Tab: การแสดงผล (display)
- ภาษา: select (ไทย/English), default "ไทย"
- ขนาดตัวอักษร: select (มาตรฐาน/ใหญ่), default "มาตรฐาน"
- Status: Working (local state only)

### Tab: แพ็กเกจและการชำระเงิน (package)
- Element: `<Pill tone="gray">` — "แพ็กเกจพื้นฐาน (ฟรี)"
- Element: Description — "อัปเกรดเพื่อปลดล็อกฟีเจอร์เพิ่ม: AI วิเคราะห์ไม่จำกัด, เอกสารกฎหมาย, ปรึกษาทนาย, LINE แจ้งเตือน"
- Element: Button "อัปเกรดแพ็กเกจ" (toast: "ระบบชำระเงินกำลังพัฒนา — เราจะแจ้งให้ทราบเมื่อพร้อม")
- Status: Partial (no payment integration)

### Tab: ช่วยเหลือ (help)
- Static help text:
  - "📖 วิธีเริ่มต้นใช้งาน: ค้นหาปัญหาของคุณหรือเริ่มวิเคราะห์เคสเพื่อรับคำแนะนำทีละขั้นตอน"
  - "🤖 AI Diagnosis: ตอบคำถาม 4 ข้อ — AI จะวิเคราะห์สิทธิและขั้นตอนที่ควรทำ"
  - "📄 เอกสาร: สร้างเอกสารกฎหมายอัตโนมัติ — ตรวจสอบกับผู้เชี่ยวชาญก่อนใช้งาน"
  - "👨‍⚖️ ทนาย: ค้นหาทนายที่ผ่านการตรวจสอบ — ดูราคาและขอบเขตก่อนตัดสินใจ"
  - "📧 ติดต่อ: help@legalai.co.th"
- Data: Static
- Status: Working

---

## /terms — ข้อกำหนดการใช้บริการ
**File:** `app/terms/page.tsx` | **Type:** Server component

### Content
- `<h1>` — "ข้อกำหนดการใช้บริการ (Terms of Service)"
- Effective date: "มีผลบังคับใช้: 9 สิงหาคม 2569"
- 9 sections:
  1. การยอมรับข้อกำหนด
  2. ขอบเขตการให้บริการ (AI วิเคราะห์, สร้างเอกสาร, ค้นหาทนาย, ข้อมูลกฎหมาย)
  3. ข้อจำกัดความรับผิด (⚠️ สำคัญ: LegalAI ให้ข้อมูลกฎหมายเท่านั้น ไม่ใช่คำแนะนำทางกฎหมาย)
  4. การใช้บริการอย่างเหมาะสม
  5. การระงับหรือยกเลิกบัญชี
  6. ทรัพย์สินทางปัญญา
  7. การเปลี่ยนแปลงข้อกำหนด
  8. กฎหมายที่ใช้บังคับ (กฎหมายไทย)
  9. ติดต่อ (legal@legalai.co.th)
- Data: Static HTML
- Status: Working

---

## /privacy — นโยบายความเป็นส่วนตัว
**File:** `app/privacy/page.tsx` | **Type:** Server component

### Content
- `<h1>` — "นโยบายความเป็นส่วนตัว (Privacy Policy)"
- Effective date: "มีผลบังคับใช้: 9 สิงหาคม 2569"
- PDPA reference: "ตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA)"
- 8 sections:
  1. ข้อมูลที่เราเก็บ (table: ข้อมูลบัญชี, ข้อมูลเคส, หลักฐาน, ข้อมูลการใช้งาน)
  2. การใช้ AI ประมวลผลข้อมูล (DeepSeek AI — not stored permanently)
  3. การเก็บรักษาและความปลอดภัย (TLS, Supabase SOC 2, 5-year max retention)
  4. การเปิดเผยข้อมูลแก่บุคคลที่สาม (ทนายความเมื่อยินยอม, กฎหมายบังคับ)
  5. สิทธิของคุณตาม PDPA (มาตรา 30-42): ขอเข้าถึง, ขอสำเนา, ขอลบ, คัดค้าน, ถอนความยินยอม
  6. คุกกี้ (necessary only, no tracking)
  7. ช่องทางติดต่อ (privacy@legalai.co.th)
  8. การเปลี่ยนแปลงนโยบาย
- Data: Static HTML
- Status: Working

---

## /notifications — การแจ้งเตือน
**File:** `app/notifications/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "การแจ้งเตือน" / subtitle: "ติดตามกำหนดการและความคืบหน้าสำคัญ"
- Element: Action button "✓ อ่านทั้งหมดแล้ว"
- Algorithm: `markAllRead()` — sets all notification IDs as read + toast
- Status: Working

### Section: Notification Tabs
- Tabs: "ทั้งหมด (3)", "เคสของฉัน", "เอกสาร", "ระบบ"
- Algorithm: `active` tab filter. Category mapping: n-1→case, n-2→document, n-3→case, n-4→system
- Status: Working

### Section: Notification List
- Element: Per-notification — icon (tone-colored), title, body, timestamp, CTA link/button
- Unread indicator (dot)
- Empty state: "ไม่มีการแจ้งเตือนในหมวดนี้"
- Algorithm: `isRead(id)` from local `readIds` Set
- Data: Mock (`sampleNotifications` from `@/lib/mock/categories`)
- Status: Working

### Section: Reminder Card
- Element: ◷ icon + "ตั้งค่าการแจ้งเตือนให้เหมาะกับคุณ" / "เลือกช่องทางและเวลาที่ต้องการรับการแจ้งเตือนผ่านแอป อีเมล หรือ LINE"
- Element: Link "ตั้งค่าการแจ้งเตือน" → `/profile`
- Status: Working

---

## /assistant — AI Legal Assistant (Chat)
**File:** `app/assistant/page.tsx` | **Type:** Client component

### Section: Chat Shell Header
- Element: AI orb with SparklesIcon + `<h1>` "AI Legal Assistant"
- Element: `<p>` — "พร้อมช่วยเหลือ • อ้างอิงกฎหมายไทย" (with green dot indicator)
- Element: "•••" menu button (toast: "กำลังเปิดตัวเลือกเพิ่มเติม")
- Status: Working

### Section: Context Banner
- Element: FolderIcon + "กำลังใช้ข้อมูลจากเคส" / `<strong>` "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า"
- Element: "เปลี่ยน" button (toast: "กำลังเปิดเมนูเปลี่ยนเคส")
- Data: Hardcoded `CASE_TITLE`
- Status: Working

### Section: Messages
- Element: "วันนี้" day label
- Element: `<PrototypeDataNotice label="ผู้ช่วย AI — ยังไม่ใช่ทนายความ" />`
- Welcome message: "สวัสดีค่ะ ฉันคือ AI Legal Assistant เล่าเหตุการณ์ให้ฟังได้เลย ฉันจะช่วยสรุปประเด็นและแนะนำขั้นตอนถัดไปค่ะ"
- Quick replies (on welcome): "มีหนังสือแจ้ง", "แจ้งด้วยวาจา", "ไม่ได้แจ้งเหตุผล" (click fills textarea)
- User messages: right-aligned, "ส่งแล้ว" label
- AI messages: left-aligned with SparklesIcon, "AI" label, optional `<SourceCitation>` components
- Loading: "AI กำลังพิมพ์..." / "กำลังคิด"
- Algorithm: `send()` — POSTs to `/api/ai/assistant` with `{message, history, category:"labour", caseTitle}`. Sends full chat history for context. Handles errors with fallback message.
- Data: Real API (`POST /api/ai/assistant`)
- Status: Working

### Section: Chat Compose
- Element: Suggestion chips — "สรุปสิทธิของฉัน", "ต้องเตรียมอะไรบ้าง?", "ช่วยร่างเอกสาร" (click sends immediately)
- Element: Paperclip button (disabled, no handler)
- Element: Textarea (placeholder: "พิมพ์คำถามของคุณ...", Enter to send)
- Element: Send button (ArrowUpIcon, disabled when empty or loading)
- Element: Disclaimer — "AI อาจให้ข้อมูลคลาดเคลื่อน โปรดตรวจสอบข้อมูลสำคัญกับผู้เชี่ยวชาญ"
- Status: Working

---

## /cases — เคสของฉัน
**File:** `app/cases/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` — title: "เคสของฉัน" / subtitle: "ทำต่อจากจุดที่ค้างไว้ หรือเริ่มเคสใหม่ได้ที่นี่"
- Element: Action link "+ สร้างเคสใหม่" → `/diagnosis`
- Status: Working

### Section: Stats Grid
- 4 stat cards: "3 เคสทั้งหมด" (FolderIcon), "1 กำลังดำเนินการ" (BellIcon, variant s2), "1 รอเอกสาร" (DocIcon), "1 เสร็จสิ้น" (CheckIcon, variant s3)
- Data: Hardcoded stats
- Status: Working

### Section: Filter Row
- Filters: "ทั้งหมด (3)", "กำลังดำเนินการ", "รอเอกสาร", "เสร็จสิ้น"
- Algorithm: `active` filter. `visible` computed by filtering `sampleCases` by status.
- Status: Working

### Section: Case List
- Element: `<CaseProgressCard>` per case with route mapping (case-1→timeline, case-2→evidence, case-3→timeline)
- Empty state: "ยังไม่มีเคสในสถานะนี้"
- Data: Mock (`sampleCases`)
- Status: Working

### Section: New Case CTA
- Element: "+" icon + "เริ่มเคสใหม่" / "วิเคราะห์เคสของคุณฟรี" → `/diagnosis`
- Element: `<PrototypeDataNotice />`
- Status: Working

---

## /cases/[caseId]/timeline — ไทม์ไลน์เคส
**File:** `app/cases/[caseId]/timeline/page.tsx` | **Type:** Client component

### Section: Breadcrumb
- Element: "เคสของฉัน › ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า"
- Status: Working

### Section: Case Header
- Element: `<Pill tone="blue">` — "กำลังดำเนินการ"
- Element: `<h1>` — "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า"
- Element: `<p>` — "{reference} • สร้างเมื่อ 8 ส.ค. 2569"
- Element: Case tabs — "ภาพรวม", "ไทม์ไลน์" (active), "หลักฐาน (N/N)", "เอกสาร"
- Status: Working

### Section: Timeline Card ("แผนดำเนินการ")
- Element: `<h3>` — "แผนดำเนินการ" / `<p>` — "ขั้นตอนและกำหนดเวลาของเคสนี้"
- Element: `<Pill tone="blue">` — "คืบหน้า {progress}%"
- Element: Timeline items — each: icon (✓ done / ! current / • pending), whenLabel, title, detail
  - Current item has action links: "สร้างหนังสือทวงถาม" (→ /documents), "ดูหลักฐาน" (→ evidence page)
- Element: `<GentleConsequenceNotice>` — "กำหนดเวลาในไทม์ไลน์เป็นการประมาณการตามแนวทางทั่วไป..."
- Algorithm: `recordEvent({type:"first_action_completed"})` on document link click
- Data: Mock (`sampleTimeline`, `sampleCases[0]`, `labourLawSources`)
- Status: Working

### Section: Sidebar
- Case info card: "ประเภทเรื่อง" → "กฎหมายแรงงาน", "สถานะหลักฐาน" → Pill "พร้อม {EVIDENCE_PERCENT}%", "ความเร่งด่วน" → Pill "ปานกลาง"
- AI Assistant card: "✦ มีคำถามเกี่ยวกับขั้นตอน?" / "ถาม AI Legal Assistant ได้ทุกเมื่อ..." / "ถาม AI →"
- Data: Mock
- Status: Working

---

## /cases/[caseId]/evidence — หลักฐานและเอกสาร
**File:** `app/cases/[caseId]/evidence/page.tsx` | **Type:** Client component

### Section: Page Header
- Element: `<PageHead>` backHref to timeline — title: "หลักฐานและเอกสาร" / subtitle: "รวบรวมหลักฐานเพื่อเสริมความแข็งแรงให้เคสของคุณ"
- Element: Action button "+ เพิ่มหลักฐาน" (triggers file input)
- Status: Working

### Section: Readiness Score
- Element: Score ring `{providedCount}/{required} รายการ`
- Element: `<Pill tone="amber">` — "ควรเพิ่มอีก {missing} รายการ"
- Element: `<h2>` — "ความพร้อมด้านหลักฐาน"
- Element: Dynamic message about missing/complete evidence
- Algorithm: `useMemo` counts provided items from evidence checklist
- Data: Mock (`sampleEvidenceRequirements`)
- Status: Working

### Section: Drag-and-Drop Upload Zone
- Element: Default state — ↑ icon + "ลากไฟล์มาวาง หรือคลิกเพื่อเลือก" / "PDF, JPG, PNG • สูงสุด 20 MB/ไฟล์ • อัปโหลดได้หลายไฟล์"
- Element: Drag-active state — blue border + shadow + "↓ วางไฟล์ที่นี่" / "ปล่อยเพื่ออัปโหลด"
- Element: Hidden file input (accept: .pdf,.jpg,.jpeg,.png,.webp, multiple)
- Algorithm: Drag handlers (dragEnter/Over/Leave/Drop). `addFiles()` — validates type (PDF/JPG/PNG/WebP), max 20MB, non-empty. `fileId()` generates unique IDs. Toast feedback on success/error.
- Data: Local state only (no real upload endpoint)
- Status: Working (client-side only)

### Section: Uploaded Files List ("ไฟล์ที่อัปโหลด (N)")
- Element: Per-file row — 🖼/📄 icon, name (truncated), size, link status
- Element: "เชื่อมโยง" button — opens linking selector to match file to evidence item
- Element: "×" remove button
- Element: "ล้างทั้งหมด" button
- Algorithm: `linkFileToEvidence(fileId, evidenceId)` — sets `evidenceId` on file + marks evidence as provided. `removeFile()` unlinks.
- Status: Working

### Section: Evidence Checklist ("รายการหลักฐานที่ต้องรวบรวม")
- Element: Per-item — ✓ toggle button (aria-pressed), □ icon, label, hint, file link indicator "✓ มีไฟล์" or "อัปโหลด" button
- Algorithm: `toggle(id)` toggles provided state + records event
- Data: Mock (evidence requirements)
- Status: Working

### Section: Sidebar
- Tip card: "💡 เคล็ดลับ" — drag-and-drop instructions
- Security box: "✓ ไฟล์ของคุณปลอดภัย" / "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยให้บุคคลภายนอก"
- `<PrototypeDataNotice />`
- Link "← กลับไปไทม์ไลน์"
- Status: Working

---

## /admin — LegalAI Admin
**File:** `app/admin/page.tsx` | **Type:** Client component (`dynamic = "force-dynamic"`)

### Section: Page Header
- Element: `<PageHead>` backHref="/" — pill: `<Pill tone="amber">` "ADMIN • ข้อมูลตัวอย่าง", title: "LegalAI Admin", subtitle: "สำหรับการจัดการเนื้อหาและการตรวจสอบ"
- Element: Legal note — "หน้านี้เป็นต้นแบบ การเข้าถึงจริงต้องมีบทบาท admin และ MFA"
- Status: Working

### Section: Stat Cards
- 4 stats: "เคสที่เปิดอยู่ 128 (+12%)", "ผู้ใช้ที่ลงทะเบียน 3,420 (+8%)", "รอตรวจสอบทนาย 7 (3 รายใหม่วันนี้)", "รายได้เดือนนี้ (ประมาณ) ฿86,400 (+15%)"
- Data: Mock (`stats` array)
- Status: Working

### Section: Quick Actions
- Buttons: "+ ตรวจสอบทนายใหม่", "📥 ส่งออกรายงาน", "⚙ ตั้งค่าระบบ" (all toast: "ฟีเจอร์จะพร้อมใช้งานเมื่อระบบ production พร้อม")
- Status: Stub (non-functional)

### Section: Revenue Dashboard ("💰 ภาพรวมรายได้")
- Element: `<PrototypeDataNotice />`
- 4 revenue streams: แพ็กเกจสมาชิก ฿52,800 (61%), ค่าที่ปรึกษาทนาย ฿18,600 (22%), Premium AI ฿9,600 (11%), Document Generation ฿5,400 (6%)
- Each: icon, label, amount, change%, share bar (gradient blue-green)
- SVG Line Chart (`RevenueLineChart`):
  - 8 months of data (ม.ค.-ส.ค. 2569)
  - Gradient area fill + polyline + hover tooltips
  - Y-axis grid lines (฿k labels)
  - "📈 รายได้รายเดือน (2569)" / "รวม ฿{total} • 8 เดือน"
  - "+91% YoY" growth badge
  - Legend: "— รายได้รายเดือน", "● ส.ค. (ล่าสุด)", "↗ +91% YoY"
  - Projection: "📊 คาดการณ์รายได้ทั้งปี 2569: ฿650,000 – ฿850,000 (จากอัตราการเติบโตปัจจุบัน)"
- Data: Fully mock
- Status: Working (display only)

### Section: Module Grid ("โมดูลผู้ดูแลระบบ")
- 6 modules: การตรวจสอบทนาย (badge: 3), ทะเบียนแหล่งกฎหมาย (12 แหล่ง), เทมเพลตเอกสาร (badge: 2), รายงานการใช้งานผิด (0), บันทึกการตรวจสอบ (read-only), เครื่องมือสนับสนุนผู้ใช้ (จำกัดสิทธิ์)
- All non-functional (display only)
- Data: Mock
- Status: Stub

### Section: Recent Activity ("กิจกรรมล่าสุด")
- Filter: "ทั้งหมด", "ทนาย", "เคส", "ระบบ"
- 5 activities: ลงทะเบียนทนายใหม่, เคสเสร็จสิ้น, เทมเพลตรอตรวจทาน, รายงานข้อผิดพลาด, ผู้ใช้ใหม่
- Each: color dot (blue/green/amber/red), action, detail, time
- Data: Mock
- Status: Working (filter non-functional — all show same data)

### Section: System Health
- Element: 🟢 + "ระบบทำงานปกติ" / "API uptime 99.8% • Last deploy: 10 ส.ค. 2569 12:00 น."
- Element: `<PrototypeDataNotice />`
- Data: Mock
- Status: Working

---

## /onboarding — การตั้งค่าบัญชีครั้งแรก
**File:** `app/onboarding/page.tsx` | **Type:** Client component

### Section: Auth Guard
- Algorithm: `useAuth()` — if not signed in, `router.replace("/auth/signin")`. Loading state shows "กำลังโหลด..." with AI orb.
- Status: Working

### Section: Focus Header
- Element: Back button `‹`, `<Brand />`, Close `×` → `/`
- Status: Working

### Section: Progress Bar
- Element: "การตั้งค่าบัญชีครั้งแรก" / "ขั้นตอน {step} จาก 5"
- Element: `<Progress value={progressPercent} />`
- Status: Working

### Step 1: ข้อกำหนดและเงื่อนไข
- `<Pill>` — "ขั้นตอนที่ 1 • ข้อกำหนด"
- `<h1>` — "ข้อกำหนดและเงื่อนไข"
- `<p>` — "กรุณาอ่านและยอมรับเพื่อเริ่มใช้งาน LegalAI"
- Checkboxes: "1 ฉันอ่านและยอมรับข้อกำหนดการใช้บริการแล้ว", "2 ฉันอ่านและยอมรับนโยบายความเป็นส่วนตัวแล้ว"
- Links to `/terms` and `/privacy`
- Status: Working

### Step 2: ความยินยอมประมวลผลด้วย AI
- `<Pill>` — "ขั้นตอนที่ 2 • ความยินยอม"
- `<h1>` — "ความยินยอมประมวลผลด้วย AI"
- Explanation about AI processing
- Checkbox: "ฉันยินยอมให้ประมวลผลข้อมูลของฉันด้วย AI เพื่อรับคำแนะนำกฎหมาย"
- Disclaimer: "คุณสามารถเพิกถอนความยินยอมและลบข้อมูลได้ตลอดเวลาในหน้าโปรไฟล์"
- Status: Working

### Step 3: ช่องทางแจ้งเตือน
- `<Pill>` — "ขั้นตอนที่ 3 • การแจ้งเตือน"
- `<h1>` — "ช่องทางแจ้งเตือน"
- Checkboxes: "แจ้งเตือนในแอป" (default on), "แจ้งเตือนทางอีเมล" (default on), "แจ้งเตือนทาง LINE" (default off)
- Disclaimer: "สามารถเปลี่ยนแปลงช่องทางแจ้งเตือนได้ภายหลังในหน้าโปรไฟล์"
- Status: Working

### Step 4: ยืนยันอีเมล
- `<Pill tone="amber">` — "ขั้นตอนที่ 4 • ยืนยันอีเมล"
- `<h1>` — "ยืนยันอีเมลของคุณ"
- Email input + "ส่งรหัส" button (disabled if no @ or already sent)
- After sending: shows "✓ ส่งรหัสยืนยันไปที่ {email} แล้ว (ตัวอย่าง — ในการใช้งานจริงจะส่งอีเมลจริง)"
- 6-digit code input (monospace, numeric, maxLength 6) + "ยืนยัน" button
- "ส่งรหัสอีกครั้ง" + "เปลี่ยนอีเมล" links
- Success state: ✓ green circle + "ยืนยันอีเมลสำเร็จ" + "{email} ได้รับการยืนยันแล้ว" + "เปลี่ยนอีเมล" button
- Disclaimer: "การยืนยันอีเมลช่วยปกป้องบัญชีของคุณและทำให้คุณสามารถกู้คืนบัญชีได้ในภายหลัง"
- Algorithm: `sendVerificationCode()` — mock 1.2s timeout. `verifyCode()` — accepts any 6-digit code. `changeEmail()` resets.
- Data: Fully mocked email verification
- Status: Partial (mock OTP, no real email service)

### Step 5: ข้อมูลพื้นฐาน
- `<Pill>` — "ขั้นตอนที่ 5 • โปรไฟล์"
- `<h1>` — "ข้อมูลพื้นฐาน"
- Form: ชื่อ-นามสกุล (required, autocomplete name), ภาษาที่ต้องการ (select: ไทย/English)
- Button: "เสร็จสิ้นการตั้งค่า" (submit)
- Algorithm: `next()` → toast "การตั้งค่าบัญชีเสร็จสมบูรณ์!" + route to `/`
- Status: Working

### Navigation
- Steps 1-4: "ย้อนกลับ" + "ถัดไป →" (disabled until valid)
- Step 5: "เสร็จสิ้นการตั้งค่า" (submit button inside form)
- Error message: "กรุณาตรวจสอบให้ครบทุกข้อก่อนดำเนินการต่อ"
- Privacy note: "⌾ ข้อมูลของคุณได้รับการเก็บรักษาอย่างปลอดภัย"
- Status: Working

---

## /auth/signin — เข้าสู่ระบบ LegalAI
**File:** `app/auth/signin/page.tsx` | **Type:** Client component

### Section: Auth Guard
- Algorithm: `useAuth()` — if already signed in, `router.replace("/onboarding")`
- Status: Working

### Section: Focus Header
- Element: Back link `‹` (aria-label "ย้อนกลับ"), `<Brand />`, Close `×` (aria-label "ปิดและกลับหน้าหลัก")
- Status: Working

### Section: Sign-In Card
- Element: AI orb `✦`
- Element: `<Pill>` — "ปลอดภัย • เข้ารหัสด้วย OTP"
- Element: `<h1>` — "เข้าสู่ระบบ LegalAI"
- Element: `<p>` — "ลงชื่อเข้าใช้เพื่อบันทึกเคสและเอกสารของคุณ"
- Data: Real (`useAuth` from `@/lib/auth/session`)
- Status: Working

### Stage: Email
- Element: Email input (placeholder: "อีเมลของคุณ", autocomplete email, inputMode email)
- Element: Submit button "ส่งรหัสยืนยัน" (shows "กำลังส่ง..." when submitting)
- Element: Divider "หรือ"
- Element: Google OAuth button "ดำเนินต่อด้วย Google"
- Algorithm: `handleEmail()` → `signInWithEmail(email)` from Supabase. On success → `setStage("otp")`. On error → set error state.
- Data: Real API (Supabase Auth)
- Status: Working

### Stage: OTP
- Element: Message "เราส่งรหัส 6 หลักไปยัง {email} แล้ว"
- Element: OTP input (6-digit, numeric, monospace, centered, large font)
- Element: Submit button "ยืนยันและเข้าสู่ระบบ" (shows "กำลังยืนยัน..." when submitting)
- Element: "แก้ไขอีเมล" button → back to email stage
- Algorithm: `handleOtp()` → `verifyOtp(email, otp)` from Supabase. On success → `onAuthStateChange` triggers redirect to `/onboarding`
- Data: Real API (Supabase Auth OTP)
- Status: Working

### Section: Terms Disclaimer
- Element: "การเข้าสู่ระบบแปลว่าคุณยอมรับ ข้อกำหนดการใช้บริการ และ นโยบายความเป็นส่วนตัว"
- Links to `/terms` and `/privacy`
- Status: Working

### Section: Footer
- Element: "‹ กลับหน้าหลัก" → `/`
- Status: Working

---

## GLOBAL SUMMARY

### Authentication
- Provider: Supabase Auth (email OTP + Google OAuth)
- Files: `@/lib/auth/session` (`useAuth` hook)
- Status: Working (real integration)

### AI/API Endpoints Referenced
1. `POST /api/ai/diagnosis` — Diagnosis analysis (DeepSeek, used in `/diagnosis`)
2. `POST /api/ai/assistant` — AI chat + search analysis (DeepSeek, used in `/assistant` + `/search`)
3. `/api/documents/generate` — Document generation (mentioned but NOT yet implemented in pages)

### Mock Data Sources
- `@/lib/mock/categories` — categories, sampleCases, sampleLawyers, sampleTimeline, sampleEvidenceRequirements, labourLawSources, sampleNotifications
- `@/lib/legal/diagnosis-config` — `getDiagnosisConfig()` per-category question configs
- `@/lib/legal/sources` — `sourcesForCategory()` legal source lookup
- `@/lib/legal/category-drives` — consumer psychology profiles per category
- `@/lib/documents/categories` — `DOCUMENT_CATEGORIES`, `TOTAL_TEMPLATES`, `suggestCategory()`
- `@/lib/documents/templates` — `getTemplatesForCategory()`, `buildTemplateDoc()`
- `@/lib/packages/definitions` — `PACKAGES`, `PACKAGE_ORDER`

### Working Status Summary
| Page | Status |
|------|--------|
| / (Home) | Working |
| /categories | Working |
| /categories/[category] | Working |
| /diagnosis | Working (live API) |
| /search | Working (live API) |
| /documents | Partial (mock generation) |
| /documents/[category] | Working |
| /documents/create | Partial (no real API) |
| /tax | Working (local calc) |
| /pricing | Working (mock) |
| /lawyers | Working (mock) |
| /lawyers/[id] | Working (mock booking) |
| /profile | Partial (local state) |
| /terms | Working |
| /privacy | Working |
| /notifications | Working (mock) |
| /assistant | Working (live API) |
| /cases | Working (mock) |
| /cases/[caseId]/timeline | Working (mock) |
| /cases/[caseId]/evidence | Working (local upload) |
| /admin | Stub (display only) |
| /onboarding | Partial (mock email) |
| /auth/signin | Working (live Supabase) |

### User Persona
- Hardcoded persona: "นภัสสร วัฒนะ" (คุณนภัสสร, napassorn@example.com)
- Member since: มิ.ย. 2569
- Package: แพ็กเกจพื้นฐาน (ฟรี)
- Demo case: "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า" (labour law)

### Component Dependencies
- `@/components/ui/primitives` — PageHead, Pill, Progress, PrototypeDataNotice
- `@/components/ui/icons` — SparklesIcon, DocIcon, ScaleIcon, SearchIcon, ShieldIcon, BellIcon, CheckIcon, FolderIcon, ArrowUpIcon, PaperclipIcon
- `@/components/layout/brand` — Brand
- `@/components/layout/app-providers` — useToast
- `@/components/cases/case-card` — CaseProgressCard
- `@/components/trust/social-proof` — SocialProofInline, SocialProofCard
- `@/components/trust/source-citation` — SourceCitation
- `@/components/trust/consequence-notice` — GentleConsequenceNotice
- `@/components/documents/document-editor` — DocumentEditor
- `@/lib/analytics/events` — recordEvent
- `@/lib/auth/session` — useAuth
- `@/lib/documents/export` — printDocument
