# LegalAI Thailand — Complete UX/UI Audit Report

**Date:** 12 สิงหาคม 2569 (August 12, 2026)  
**Version:** 1.0 — Comprehensive Audit  
**Scope:** ALL 27 pages + 15 library files  
**Auditor:** Hermes Subagent  
**Platform:** legalai-citizen-check (Next.js App Router)

---

## EXECUTIVE SUMMARY

LegalAI Thailand is a citizen legal-assistance platform built with Next.js App Router, serving the Thai market with AI-powered legal information, document generation, lawyer marketplace, and tax planning features. This exhaustive audit covers every page file (27 total, including analysis, design-system, and auth/callback) and all 15 key library files in `D:\legalai-citizen-check`.

### Key Architecture Findings

1. **Rich Thai-language UI** — All copy is Thai with consistent emoji usage, tonal design (8 design tokens), 4 interaction states (loading/empty/error/success), responsive breakpoints (320/768/1200px).
2. **12 legal categories** — labour, consumer, debt, housing, family, accident, online_fraud, crime, government, insurance, defamation, property — each with dedicated diagnosis questions, drive-aware emotional framing, social proof, and 36+ cited legal sources.
3. **V4 Concierge Gaps** — The backend has deep infrastructure (drive detection, fear calibration, guardrails, social proof, merge engine) but pages don't expose full V4 flow: no fear calibration pre-diagnosis, no drive-personalized category pages, no 8-phase concierge dashboard, and no proactive notifications.
4. **Document library (126 templates)** — 10 categories defined with full template lists but only 4 quick-start documents on the main page; DocumentEditor exists but real generation is stubbed.
5. **Tax calculator is production-ready** — Progressive tax engine, bracket visualization, comparison mode, deduction toggles, checklist with localStorage, printable HTML report, AI optimizer stub.
6. **Prototype quality throughout** — `PrototypeDataNotice` on 15+ pages, mock data everywhere, only 2 real API endpoints (/api/ai/assistant, /api/ai/diagnosis).

---

## PART 1: PAGE-BY-PAGE AUDIT (27 Pages)

---

### 1. HOME PAGE — `app/page.tsx` (217 lines)

**Route:** `/`

#### Sections
- **Welcome banner** — Date card showing Thai weekday/day/month/year (2569), greeting "สวัสดีค่ะ คุณนภัสสร 👋"
- **Hero card** — "เรื่องกฎหมายไม่ต้องเป็นเรื่องยากอีกต่อไป" + search box
- **Quick searches** — 4 pill buttons: "ถูกโกงออนไลน์", "นายจ้างไม่จ่ายเงิน", "ขอคืนเงิน", "สัญญาเช่า"
- **Category grid** — Map of 12 legal categories from `categories` mock data
- **Action grid** — 5 action cards: diagnosis, documents, lawyers, tax, pricing
- **Case preview** — Sample case progress card ("case-1")
- **Trust strip** — Shield icon + "ข้อมูลของคุณได้รับการปกป้อง" + PrototypeDataNotice

#### Exact Thai Copy
- Welcome: "สวัสดีค่ะ คุณนภัสสร 👋", "วันนี้มีเรื่องกฎหมายอะไรให้เราช่วยดูแลคะ?"
- Hero: "เรื่องกฎหมายไม่ต้องเป็นเรื่องยากอีกต่อไป", "พิมพ์คำถามด้วยภาษาของคุณ เราจะช่วยสรุปให้เข้าใจง่าย พร้อมบอกขั้นตอนที่ควรทำต่อ"
- Search placeholder: "เช่น ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า ทำอย่างไร?"
- Search button: "ค้นหา"
- Quick search label: "ค้นหายอดนิยม:"
- Section head: "เริ่มต้นจากเรื่องที่คุณสนใจ", "เลือกหมวดหมู่เพื่อดูคำแนะนำเบื้องต้น"
- Action cards:
  1. "วิเคราะห์เคสของฉัน" / "ตอบคำถามสั้น ๆ แล้ว AI จะช่วยวิเคราะห์สิทธิ หลักฐาน และขั้นตอนถัดไป" / "เริ่มวิเคราะห์ฟรี →" (Pill: "แนะนำ")
  2. "สร้างเอกสารกฎหมาย" / "หนังสือทวงถาม ร้องเรียน หรือบอกเลิกสัญญา พร้อมใช้งาน" / "เลือกเอกสาร →"
  3. "ปรึกษาทนายที่เหมาะกับคุณ" / "ค้นหาทนายที่ผ่านการตรวจสอบ พร้อมดูราคาและขอบเขตชัดเจน" / "ค้นหาทนาย →"
  4. "วางแผนภาษี" / "คำนวณภาษีเงินได้บุคคลธรรมดา วางแผนลดหย่อน และประหยัดภาษีสูงสุด" / "ลองคำนวณ →"
  5. "อัปเกรดแพ็กเกจ" / "ปลดล็อกฟีเจอร์เพิ่ม — เอกสารไม่จำกัด ปรึกษาทนาย และ LINE แจ้งเตือน" / "ดูแพ็กเกจ →"
- Cases: "เคสที่กำลังดำเนินการ", "ทำต่อจากจุดที่ค้างไว้"
- Trust: "ข้อมูลของคุณได้รับการปกป้อง", "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยข้อมูลให้บุคคลภายนอก"

#### Current Algorithm
- `search()`: Trims query (or defaults to "นายจ้างเลิกจ้างโดยไม่แจ้งล่วงหน้า"), fires `search_submitted` event, navigates to `/search?q=...`
- Quick search: Sets query + immediately routes to search page
- Date: `formatThaiToday()` runs client-side only to avoid hydration mismatch, uses `useEffect` with `setState`
- Categories: Hardcoded from `@/lib/mock/categories`, links to `/categories/${c.id}`
- All links use `onClick` handlers firing analytics events

#### Current State
- ✅ Working: Search routing, category links, action cards, date display
- ⚠️ Placeholder: Hardcoded greeting "คุณนภัสสร" — no dynamic user name
- ⚠️ Missing: No loading state for initial page load, no error boundary
- ⚠️ Hardcoded: Case preview always shows "case-1"

#### Desired State (V4 Concierge)
- Welcome should pull real user name from auth session
- Hero should integrate concierge: "สวัสดีค่ะ [ชื่อ] — วันนี้อยากให้เราช่วยเรื่องอะไรคะ?" with voice-input option
- Quick searches should be dynamically ranked by trending/seasonal legal issues
- Category grid should show drive-aware hooks ("⚖️ ความเป็นธรรมที่คุณสมควรได้" instead of generic hints)
- Case preview should show real user cases sorted by urgency

#### Improvements Needed
1. Replace hardcoded "คุณนภัสสร" with `user.displayName` from auth context
2. Add concierge-style CTA: "ไม่แน่ใจว่าจะเริ่มตรงไหน? ให้ AI ช่วยแนะนำ →"
3. Show live social proof stats (e.g., "3,250 คนใช้ LegalAI เดือนนี้")
4. Add fear calibration entry point: "😰 กำลังเครียดเรื่องกฎหมายอยู่? บอกเรา เราช่วยได้"
5. Integrate drive detection to personalize action card order

---

### 2. CATEGORIES LIST — `app/categories/page.tsx` (61 lines)

**Route:** `/categories`

#### Sections
- PageHead: "🔍 เลือกหมวดหมู่ปัญหากฎหมาย" / "เลือกหมวดที่ตรงกับปัญหาของคุณ — AI จะถามคำถามทีละข้อ"
- Category grid — 12 cards, each with icon, title, hint, question count, CTA "เริ่มวิเคราะห์ →"
- Privacy note: "⌾ คำตอบของคุณใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น — เราไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
- SocialProofInline component

#### Exact Thai Copy
- Title: "🔍 เลือกหมวดหมู่ปัญหากฎหมาย"
- Subtitle: "เลือกหมวดที่ตรงกับปัญหาของคุณ — AI จะถามคำถามทีละข้อ"
- Question display: "{N} คำถาม — {list of question titles}"
- CTA: "เริ่มวิเคราะห์ →"
- Note: "⌾ คำตอบของคุณใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น — เราไม่เปิดเผยข้อมูลให้บุคคลภายนอก"

#### Current Algorithm
- Maps `categories` array (from mock), loads `getDiagnosisConfig(cat.id)` to show question count and titles
- All category links point to `/diagnosis?category=${cat.id}` (direct to wizard, skip detail page)
- SocialProofInline shown at bottom

#### Current State
- ✅ Working: Category listing, question previews
- ⚠️ Skip: Links go directly to diagnosis wizard, bypassing category detail page (`/categories/[category]`)
- ⚠️ Missing: No search/filter for categories, no sorting by popularity

#### Desired State (V4 Concierge)
- Should link to `/categories/[category]` detail pages first (not directly to diagnosis)
- Show category cards with drive-aware emotional framing (not just icon+hint)
- Add "🔍 ค้นหาหมวดหมู่" search bar
- Show trending categories with "🔥 กำลังเป็นที่นิยม" badge from social proof data

#### Improvements Needed
1. Change links from `/diagnosis?category=` to `/categories/${cat.id}` for better information architecture
2. Add drive hooks to each card (e.g., "⚖️ 1,284 คนได้ค่าชดเชยแล้ว" for labour)
3. Add category search/filter input
4. Show urgency indicators per category
5. Use CATEGORY_SOCIAL_PROOF data for "users helped" counts

---

### 3. CATEGORY DETAIL — `app/categories/[category]/page.tsx` (258 lines)

**Route:** `/categories/[category]` (12 variants)

#### Sections
- PageHead: icon + title + hint
- Drive-aware emotional framing bar — motivation hook + SocialProofInline
- Drive labels — emoji + Thai drive names (e.g., "⚖️ ยุติธรรม/ถูกต้อง", "💰 ผลประโยชน์/คุ้มค่า")
- Problem examples — per-category list with title, description, urgency pill
- AI questions preview — numbered list with title + rationale
- Start CTA: "🤖 เริ่มวิเคราะห์เคสของฉัน" + "ใช้เวลาประมาณ 3 นาที • ข้อมูลของคุณปลอดภัย"
- Sidebar:
  - Loss aversion card: "⚠️ อย่ารอจนสาย" + drive-specific loss message
  - SocialProofCard
  - Quick actions: search, documents, lawyers
  - Legal sources — from `sourcesForCategory()`
  - Related categories — 6 other categories

#### Exact Thai Copy (sampled from labour category)
- "⚖️ ความเป็นธรรมในที่ทำงาน"
- "ถูกเลิกจ้าง? ไม่ได้รับค่าจ้าง? AI ช่วยสรุปสิทธิและวางแผนเรียกร้องค่าชดเชย"
- Motivation hook: "คุณทำงานหนักมา — ถึงเวลาเรียกร้องสิทธิที่ควรได้"
- Loss message: "ถ้าไม่ยื่นคำร้องภายใน 2 ปี คุณจะเสียสิทธิเรียกร้องถาวร"
- "📋 ปัญหาที่พบบ่อยในหมวดนี้"
- "🤖 AI จะถามคุณ"
- "🤖 เริ่มวิเคราะห์เคสของฉัน"
- "⚠️ อย่ารอจนสาย"
- "⚖️ กฎหมายที่เกี่ยวข้อง"
- "📂 หมวดอื่นๆ"

#### Current Algorithm
- Reads `params.category`, finds matching category in mock data
- Loads diagnosis config, sources, problem examples, drive profile
- PROBLEM_EXAMPLES is a 90-line hardcoded Record with ~50 problem scenarios across 12 categories
- Each problem has urgency label (⚡ ทันที, ⚡ ภายใน 24 ชม., ⏰ 1-3 วัน, 📅 30-60 วัน, etc.)
- Drive-aware: uses `getCategoryDriveProfile`, `getCategoryDriveLabels`, `getEmotionalFrame`, `getLossAversionMessage`
- 404 fallback if category not found

#### Current State
- ✅ Working: Category detail rendering, drive-aware hooks, problem examples, source citations
- ✅ Best page for emotional intelligence — drive hooks + loss aversion + social proof all present
- ⚠️ PROBLEM_EXAMPLES hardcoded in page file (should be in library)
- ⚠️ Missing: No real analytics on which problems are most common
- ⚠️ Missing: No "I'm in crisis" emergency CTA for urgent categories (crime, online_fraud)

#### Desired State (V4 Concierge)
- Emergency overlay for crisis categories (crime, online_fraud) with phone numbers (191, 1441, 1300)
- Dynamic problem examples ranked by actual platform data
- Fear calibration question BEFORE "เริ่มวิเคราะห์" — "คุณรู้สึกยังไงกับเรื่องนี้?"
- Concierge greeting that adapts to time of day and urgency
- "เห็นว่าคุณกำลังดูเรื่อง [category] — มีคน 890 คนใช้ AI ช่วยแล้ววันนี้"

#### Improvements Needed
1. Extract PROBLEM_EXAMPLES to `lib/legal/problem-examples.ts`
2. Add emergency redirect for crisis categories (crime, online_fraud, accident)
3. Insert fear calibration step between category page and diagnosis wizard
4. Add "🆘 ฉุกเฉิน — ติดต่อ 191 / 1441 / 1300 ทันที" banner for urgent categories
5. Dynamic problem ranking from analytics
6. Show real-time social proof: "X คนกำลังอ่านหน้านี้"

---

### 4. DIAGNOSIS WIZARD — `app/diagnosis/page.tsx` (334 lines)

**Route:** `/diagnosis?category=...`

#### Sections
- Header: back button (‹) + Brand logo + close (×)
- Progress bar: "หาเส้นทางที่เหมาะกับเรื่องของคุณ" + "ขั้นตอน {step} จาก {TOTAL}"
- Question card:
  - AI orb (✦)
  - Pill: "ตอบเท่าที่ทราบ • กลับมาแก้ได้"
  - Question title + rationale
  - Option list — radio (single-select) or checkbox (multi-select for evidence question)
  - Each option: letter badge (A, B, C, D) + text + check indicator
- Navigation: "ย้อนกลับ" + "ถัดไป →" / "ดูผลวิเคราะห์"
- Privacy note: "⌾ คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น คุณลบหรือแก้ไขได้เสมอ"
- Loading state: AI orb + "AI กำลังวิเคราะห์เคสของคุณ..." + indeterminate progress + "DeepSeek ใช้เวลา 30–90 วินาที"
- Error state: "ไม่สามารถวิเคราะห์ได้" + retry button

#### Exact Thai Copy
- Progress: "หาเส้นทางที่เหมาะกับเรื่องของคุณ", "ขั้นตอน {N} จาก {TOTAL}"
- Pill: "ตอบเท่าที่ทราบ • กลับมาแก้ได้"
- Loading: "AI กำลังวิเคราะห์เคสของคุณ...", "DeepSeek ใช้เวลาพิจารณาเหตุการณ์และสิทธิของคุณ ปกติใช้เวลาประมาณ 30–90 วินาที กรุณาอย่าปิดหน้าต่างนี้"
- Error: "ไม่สามารถวิเคราะห์ได้ในขณะนี้ กรุณาลองอีกครั้ง"
- Navigation: "ย้อนกลับ", "ถัดไป →", "ดูผลวิเคราะห์"
- Privacy: "⌾ คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น คุณลบหรือแก้ไขได้เสมอ"

#### Current Algorithm
1. Reads `?category=` param, validates against 12 VALID_CATEGORIES, defaults to "labour"
2. Loads `getDiagnosisConfig(category)` — gets 4-5 questions with options
3. `step` state tracks current question (1-indexed)
4. `answers` stores `Record<string, string | string[]>` — single-select stores string, multi-select stores array
5. `selectAnswer(option)`: For multi, toggles in array; for single, replaces
6. `canProceed()`: Checks if current question has at least one selection
7. `next()`: Increments step; on last step calls `runAnalysis()`
8. `runAnalysis()`: POSTs `{category, answers}` to `/api/ai/diagnosis`, stores result in `sessionStorage`, routes to `/analysis/case-1?session=new`
9. Fires `diagnosis_started` / `diagnosis_completed` analytics events

#### Current State
- ✅ Working: Multi-step wizard flow, question rendering, option selection
- ✅ Good: Loading state with estimated time, error state with retry
- ⚠️ Missing: Fear calibration question (exists in fear-calibration.ts but not wired)
- ⚠️ Missing: No back-navigation mid-wizard preserves answers (only step decrements)
- ⚠️ Missing: No "skip" option for optional questions
- ⚠️ Missing: No progress persistence (refresh loses all answers)

#### Desired State (V4 Concierge)
- Insert fear calibration as step 0: "😰 คุณรู้สึกยังไงกับเรื่องนี้?" with 4 emotional options
- Drive detection runs in real-time as user answers, updating the tone of subsequent questions
- Concierge-like transitions: "เข้าใจแล้ว — ต่อไปขอถามเรื่อง..." with emotional acknowledgment
- Answer persistence in localStorage (resume after refresh)
- Estimated time remaining updates based on actual typing speed

#### Improvements Needed
1. Add fear calibration question from `FEAR_CALIBRATION_QUESTION` as step 0
2. Wire `detectDrives()` during answer collection for real-time personalization
3. Add answer persistence to localStorage
4. Show "กำลังเตรียมคำถามถัดไป..." transition animation between steps
5. Add skip button for optional questions
6. Progress bar should be determinate (X/TOTAL) not just percentage
7. Category label in header: "⚖️ กฎหมายแรงงาน" instead of just Brand

---

### 5. SEARCH — `app/search/page.tsx` (288 lines)

**Route:** `/search?q=...`

#### Sections
- Page head: back link + "ผลการค้นหา" / "คำแนะนำที่เข้าใจง่ายและนำไปใช้ได้จริง"
- Search box (standalone variant) — input + submit button
- Empty state: "🔍 พิมพ์ปัญหากฎหมายของคุณด้านบน — เช่น 'ถูกเลิกจ้าง', 'ถูกโกงออนไลน์', 'สัญญาเช่า'"
- Results layout (when query present):
  - Result meta: status text + sort dropdown (เกี่ยวข้องมากที่สุด/ใหม่ที่สุด/เก่าที่สุด)
  - Disclaimer: "ผลค้นหาเป็นข้อมูลกฎหมายเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย"
  - Answer card: AI response with save/share buttons
  - Loading card: "AI กำลังวิเคราะห์..." / "⏳ AI กำลังประมวลผล"
  - Error card: "เกิดข้อผิดพลาด" + link to diagnosis
  - Steps row: 3 static steps (รวบรวมหลักฐาน, ประเมินสิทธิ, ดำเนินการตามขั้นตอน)
  - Related articles: 3 buttons (สิทธิทางกฎหมาย, วิธีดำเนินการ, หน่วยงาน)
  - Sidebar:
    - "อยากได้คำตอบที่ตรงกับเคสของคุณ?" + "เริ่มวิเคราะห์ฟรี" link
    - Document categories — suggested from keyword matching or top 5
    - "📋 ดูเอกสารทั้งหมด 126+ รายการ →"

#### Exact Thai Copy
- Title: "ผลการค้นหา"
- Subtitle: "คำแนะนำที่เข้าใจง่ายและนำไปใช้ได้จริง"
- Placeholder: "พิมพ์ปัญหากฎหมายของคุณ..."
- Empty: "🔍 พิมพ์ปัญหากฎหมายของคุณด้านบน — เช่น 'ถูกเลิกจ้าง', 'ถูกโกงออนไลน์', 'สัญญาเช่า'"
- Status: "กำลังค้นหา...", "ไม่พบผลลัพธ์", "พบผลลัพธ์"
- Disclaimer: "ผลค้นหาเป็นข้อมูลกฎหมายเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย"
- AI label: "คำตอบแนะนำโดย LegalAI"
- Error: "เกิดข้อผิดพลาด", "คุณสามารถลองค้นหาด้วยคำอื่น หรือเริ่มวิเคราะห์เคสแบบทีละขั้นตอน"
- Steps: "ขั้นตอนที่แนะนำ" — "รวบรวมหลักฐาน"/"ประเมินสิทธิ"/"ดำเนินการตามขั้นตอน"
- Articles: "บทความที่เกี่ยวข้อง"
- Sidebar: "อยากได้คำตอบที่ตรงกับเคสของคุณ?", "📄 เอกสารธุรกิจที่เกี่ยวข้อง"

#### Current Algorithm
1. Reads `?q=` param, sets initial query
2. On mount (when query present): POSTs to `/api/ai/assistant` with prompt: "ช่วยวิเคราะห์ปัญหากฎหมายนี้เป็นภาษาไทย สั้นๆ: "{query}" — ให้บอกว่า (1) ปัญหานี้เกี่ยวข้องกับกฎหมายอะไร (2) สิทธิที่ผู้ถามมีคืออะไร (3) ขั้นตอนที่ควรทำ"
3. `suggestCategory(query)`: Matches keywords to document categories
4. `matchingDocCats`: Filters DOCUMENT_CATEGORIES by query match on title_th/subtitle_th/title_en
5. Sort dropdown: purely cosmetic — no backend re-sorting
6. Share: Uses `navigator.share` or falls back to clipboard copy
7. Save: Toggles local state, no persistence
8. Article clicks: Just show toast notification

#### Current State
- ✅ Working: AI search via `/api/ai/assistant`, document category matching
- ⚠️ Broken: Sort dropdown doesn't actually re-sort results (one-shot API call)
- ⚠️ Hardcoded: "ขั้นตอนที่แนะนำ" always shows same 3 generic steps regardless of query
- ⚠️ Hardcoded: "บทความที่เกี่ยวข้อง" always shows 3 static article titles
- ⚠️ Missing: No search history, no "recent searches", no autocomplete
- ⚠️ Missing: Save functionality doesn't persist to user account

#### Desired State (V4 Concierge)
- Concierge-style search: "🔍 กำลังหาเรื่อง..." → "พบข้อมูลที่เกี่ยวข้องกับ '[query]' — นี่คือสิ่งที่คุณควรรู้"
- AI response should include drive-aware tone based on query sentiment
- Dynamic steps based on actual AI analysis (not static)
- Real related articles from a content database
- "บันทึก" should save to user's case/bookmark collection
- Search suggestions should come from trending queries (social proof data)

#### Improvements Needed
1. Wire sort to re-query with different parameters
2. Replace STATIC_STEPS with AI-generated next actions from the API response
3. Add search history with localStorage persistence
4. Add autocomplete/suggestions dropdown as user types
5. Wire article links to real content pages
6. Add "ถามต่อ" follow-up input on the answer card (concierge chat mode)
7. Show drive-detected tone in AI response header

---

### 6. DOCUMENTS HOME — `app/documents/page.tsx` (257 lines)

**Route:** `/documents`

#### Sections
- PageHead: "สร้างเอกสารกฎหมาย" / "กรอกง่าย ใช้ภาษาถูกต้อง พร้อมดาวน์โหลดและส่งได้ทันที"
- Disclaimer: "เอกสารที่สร้างเป็นแบบร่าง ควรตรวจสอบโดยผู้เชี่ยวชาญก่อนใช้งาน"
- Document grid (left): 4 quick-start doc types with selection
- Document builder (right): Paper mockup + features list + "เริ่มสร้างเอกสาร →"
- Category browser: Search bar + category cards with template counts
- Bottom link: "ดูแบบฟอร์มทั้งหมด 126 รายการ →"

#### Exact Thai Copy
- Title: "สร้างเอกสารกฎหมาย"
- Subtitle: "กรอกง่าย ใช้ภาษาถูกต้อง พร้อมดาวน์โหลดและส่งได้ทันที"
- Disclaimer: "เอกสารที่สร้างเป็นแบบร่าง ควรตรวจสอบโดยผู้เชี่ยวชาญก่อนใช้งาน"
- Doc types:
  1. "หนังสือทวงถามค่าชดเชย" / "สำหรับแจ้งนายจ้างให้ชำระสิทธิที่ค้าง" (Pill: "แนะนำ")
  2. "หนังสือร้องเรียนผู้บริโภค" / "ร้องเรียนสินค้าและบริการที่ไม่เป็นธรรม" (Pill: "ยอดนิยม")
  3. "หนังสือบอกเลิกสัญญาเช่า" / "แจ้งยุติสัญญาอย่างเป็นทางการ"
  4. "หนังสือทวงหนี้" / "ระบุยอดหนี้และกำหนดวันชำระ"
- Features: "ใช้ภาษากฎหมายที่ถูกต้อง", "แก้ไขได้ทุกส่วน", "ดาวน์โหลดเป็น PDF หรือ Word"
- Builder: "สร้างด้วย AI", "ระบบจะนำข้อมูลจากเคสมาเติมให้อัตโนมัติ คุณตรวจสอบและแก้ไขได้ก่อนดาวน์โหลด"
- CTA: "เริ่มสร้างเอกสาร →", "ใช้เวลาประมาณ 3–5 นาที"
- Category browser: "เรียกดูตามหมวดหมู่", "{N} แบบฟอร์ม ใน 10 หมวดหมู่"
- Search: "ค้นหาหมวดหมู่เอกสาร เช่น เช่า, สินเชื่อ, จ้าง..."
- Bottom: "ดูแบบฟอร์มทั้งหมด 126 รายการ →"

#### Current Algorithm
- `startDraft()`: Shows toast, fires analytics event — NO actual document generation
- `filteredCategories`: Filters DOCUMENT_CATEGORIES by search text on title_th/subtitle_th/id
- `handleCategoryClick`: Routes to `cat.route` (e.g., `/documents/property`)
- `selected` doc state tracks which quick-start card is highlighted
- Paper mockup shows selected doc title with decorative lines

#### Current State
- ✅ Working: Category browser, search filtering, doc type selection
- ⚠️ Broken: "เริ่มสร้างเอกสาร" button only shows toast, doesn't navigate anywhere
- ⚠️ Hardcoded: 4 quick-start docs are hardcoded, not pulled from the 126-template library
- ⚠️ Missing: No link from quick-start docs to the actual document creation flow

#### Desired State (V4 Concierge)
- Quick-start docs should come from most-popular templates (dynamic ranking)
- "เริ่มสร้างเอกสาร" should navigate to `/documents/create?template=...`
- Concierge: "ไม่แน่ใจว่าต้องใช้เอกสารอะไร? AI ช่วยแนะนำ →" based on user's active cases
- Recent documents section showing user's draft history
- Template preview thumbnail instead of generic paper mockup

#### Improvements Needed
1. Make quick-start cards navigable to document creation
2. Pull quick-start templates from the actual 126-template library
3. Add "เอกสารล่าสุด" section for returning users
4. Add AI-powered template recommendation: "จากเคสของคุณ — แนะนำหนังสือทวงถามค่าชดเชย"
5. Fix "เริ่มสร้างเอกสาร" to route to `/documents/create`
6. Add template count badges per category that match actual counts

---

### 7. DOCUMENT CATEGORY DETAIL — `app/documents/[category]/page.tsx` (317 lines)

**Route:** `/documents/[category]` (10 variants)

#### Sections
- PageHead with back link, category title, subtitle, template count pill
- Info card: category icon + title + subtitle + free/paid counts
- Template list header: "รายการแบบฟอร์ม ({N} รายการ)" + free/paid count
- Template rows: icon, name, price badge (ฟรี / ฿{price}), "เริ่มสร้าง →" button
- Empty state: "ยังไม่มีแบบฟอร์มในหมวดนี้"
- Back link: "← กลับไปเลือกหมวดหมู่อื่น"

#### Exact Thai Copy
- Not found: "ไม่พบหมวดหมู่", "หมวดหมู่นี้ไม่มีในระบบ กรุณาเลือกใหม่"
- Template list: "รายการแบบฟอร์ม ({N} รายการ)"
- Price badges: "ฟรี", "ฟรี — ไม่มีค่าใช้จ่าย", "เสียค่าบริการ ฿{price}"
- Button: "เริ่มสร้าง →"
- Empty: "ยังไม่มีแบบฟอร์มในหมวดนี้", "กลับไปเลือกหมวดหมู่อื่น →"

#### Current Algorithm
- `findCategoryBySegment()`: Matches URL segment to category route (e.g., "property" → `/documents/property`)
- `getTemplatesForCategory(cat.id)`: Returns TemplateMeta[] from templates.ts registry
- `handleCreateClick(template)`: Routes to `/documents/create?template={id}&name={name}&category={catId}&paid={bool}&price={amount}`
- Free/paid counts computed from template list
- Hover effects on template rows (border color + box shadow transitions)

#### Current State
- ✅ Working: Category routing, template listing, navigation to create page
- ✅ Good: Price badges, free/paid counts, hover effects
- ⚠️ Hardcoded: Template names come from registry but actual markdown content is generated by `buildTemplateDoc()` (generic template, not category-specific)

#### Desired State (V4 Concierge)
- Template previews showing first few lines of filled content
- "ใช้บ่อย" / "แนะนำ" badges on popular templates
- Category-specific tips: "💡 เอกสารที่ใช้บ่อยในหมวดอสังหาฯ"
- Concierge: "จากเคสของคุณ — แนะนำให้สร้าง [template name]"

#### Improvements Needed
1. Add per-template markdown content to registry (not generic `buildTemplateDoc`)
2. Add popularity/usage ranking to templates
3. Show "ตัวอย่างเอกสาร" preview on hover
4. Add category-specific tips section

---

### 8. DOCUMENT CREATE — `app/documents/create/page.tsx` (232 lines)

**Route:** `/documents/create?template=...&name=...&category=...&paid=...&price=...`

#### Sections
- PageHead with back link, "สร้างเอกสาร", template name, price pill
- Template info bar: icon + name + "กรอกข้อมูลด้านล่างเพื่อสร้างเอกสาร — ดูตัวอย่างแบบเรียลไทม์ทางด้านขวา" + price badge
- DocumentEditor component (imported from `@/components/documents/document-editor`)
- Success state: "✅ เอกสาร '{name}' พร้อมใช้งานแล้ว" + "คุณสามารถพิมพ์ PDF หรือดาวน์โหลด TXT ได้จากปุ่มด้านล่าง"
- Back link: "← กลับไปเลือกหมวดหมู่อื่น"
- Suspense fallback: "⏳ กำลังโหลด..."

#### Exact Thai Copy
- No template: "ไม่พบแม่แบบ", "กรุณาเลือกแบบฟอร์มจากหมวดหมู่ก่อน", "ไม่พบข้อมูลแบบฟอร์ม — กรุณาเลือกจากหน้าเอกสาร"
- Info bar: "กรอกข้อมูลด้านล่างเพื่อสร้างเอกสาร — ดูตัวอย่างแบบเรียลไทม์ทางด้านขวา"
- Success: "เอกสาร '{name}' พร้อมใช้งานแล้ว", "คุณสามารถพิมพ์ PDF หรือดาวน์โหลด TXT ได้จากปุ่มด้านล่าง"

#### Current Algorithm
- Reads query params: template, name, category, paid, price
- `buildTemplateDoc(templateName, categoryId)`: Creates a generic MergeTemplate with COMMON_PERSON_FIELDS + COMMON_DATE_FIELDS + COMMON_AMOUNT_FIELDS + 2 clause fields
- `handleGenerate(mergeData)`: Sets `generated=true`, fires analytics — NO real API call
- `DocumentEditor` component handles field input and live preview

#### Current State
- ✅ Working: Form rendering, field input, live preview (via DocumentEditor)
- ⚠️ Broken: Generation is a stub — no real template content, no PDF/TXT export
- ⚠️ Hardcoded: All templates use same generic content regardless of type
- ⚠️ Missing: No conditional blocks, no category-specific merge fields

#### Desired State (V4 Concierge)
- Real merge engine integration with 126 unique template contents
- Category-specific merge fields (rental_amount for lease, loan_amount for loans, etc.)
- Real PDF/DOCX export via `/api/documents/generate`
- Concierge: "เรากรอกข้อมูลจากเคสของคุณให้แล้ว — ตรวจสอบและแก้ไขก่อนดาวน์โหลด"
- Auto-fill from user profile and active case data

#### Improvements Needed
1. Wire real API endpoint for document generation
2. Add per-template markdown content to the template registry
3. Add category-specific merge fields to templates
4. Implement PDF/DOCX export functionality
5. Auto-fill fields from user profile and active case context
6. Add "บันทึกเป็นร่าง" for work-in-progress documents

---

### 9. TAX CALCULATOR — `app/tax/page.tsx` (516 lines)

**Route:** `/tax`

#### Sections
- PageHead: "💰 วางแผนภาษี" / "คำนวณภาษีเงินได้บุคคลธรรมดาและวางแผนลดหย่อน"
- Income slider: range 0-5,000,000, step 10,000, displays formatted THB
- Action buttons: "🔄 เปรียบเทียบแบบมี/ไม่มีลดหย่อน" + "🖨️ พิมพ์ / PDF"
- Result card: net income, tax liability, effective rate, savings message
- Comparison mode: side-by-side cards (no deductions vs with deductions) + savings difference
- Bracket chart: 8 horizontal bars showing progressive tax brackets with active highlight
- Deduction grid: 14 deduction chips (ส่วนตัว, คู่สมรส, บุตร, พ่อแม่, ดอกเบี้ยบ้าน, ประกันสุขภาพ, ประกันชีวิต, RMF, SSF, ThaiESG, ประกันสังคม, บริจาค, การศึกษา/กีฬา, ฝากครรภ์)
- Tax optimizer card: AI analysis CTA + savings estimate + recommended plan + deadline
- Filing checklist: 6 items with localStorage persistence + progress bar + celebration animation
- E-filing link: "📤 เมื่อพร้อม — ยื่นแบบออนไลน์ที่ efiling.rd.go.th"
- Sidebar: deadlines card, tax rate table, AI optimizer link

#### Exact Thai Copy
- Title: "💰 วางแผนภาษี"
- Subtitle: "คำนวณภาษีเงินได้บุคคลธรรมดาและวางแผนลดหย่อน"
- Income label: "รายได้ต่อปี (บาท)"
- Compare button: "🔄 เปรียบเทียบแบบมี/ไม่มีลดหย่อน"
- Print button: "🖨️ พิมพ์ / PDF"
- Result: "รายได้สุทธิหลังหักลดหย่อน", "ภาษีที่ต้องจ่าย", "อัตราภาษีจริง"
- Savings: "✅ คุณประหยัดภาษีได้ ฿{amount} จากค่าลดหย่อน!"
- Comparison: "❌ ไม่มีลดหย่อน (เฉพาะส่วนตัว 60,000)", "✅ มีลดหย่อน"
- Savings diff: "🎉 คุณประหยัดภาษีได้ ฿{amount} — ลดลง {percent}%"
- No diff: "ไม่มีส่วนต่าง — ค่าลดหย่อนยังไม่ส่งผลกับอัตราภาษีของคุณ"
- Deduction label: "📋 เลือกค่าลดหย่อน"
- Note: "ⓘ ข้อมูลนี้เป็นประมาณการเบื้องต้น — ควรตรวจสอบกับผู้เชี่ยวชาญด้านภาษีก่อนยื่นแบบ"
- Optimizer: "🤖 AI Tax Optimizer", "AI จะวิเคราะห์รายได้ของคุณและแนะนำแผนลดหย่อนที่ประหยัดภาษีสูงสุด"
- CTA: "🤖 ให้ AI วิเคราะห์แผนลดหย่อน"
- Checklist: "📋 เช็คลิสต์ยื่นภาษี"
- Checklist items: "รวบรวมหนังสือรับรองการหักภาษี ณ ที่จ่าย (ทวิ 50)", "รวบรวมเอกสารลดหย่อน", "ตรวจสอบยอดเงินได้ทั้งปีจากนายจ้าง", "คำนวณภาษีด้วยเครื่องคิดเลขด้านบน", "ยื่นแบบ ภ.ง.ด.90/91 ออนไลน์ที่ rd.go.th", "เก็บหลักฐานการยื่นแบบและใบเสร็จ"
- Done: "🎉 คุณทำครบทุกขั้นตอนแล้ว!", "พร้อมยื่นภาษีเรียบร้อย — ไปยื่นแบบออนไลน์กันเลย! 🚀"
- E-filing: "📤 เมื่อพร้อม — ยื่นแบบออนไลน์ ที่ efiling.rd.go.th"
- Sidebar: "📅 กำหนดการภาษี", "📊 อัตราภาษี"

#### Current Algorithm
1. `calcTax(income, deductions)`: Pure function — iterates 8 progressive brackets, sums tax
2. `bracketBreakdown(income, deductions)`: Returns per-bracket taxable amount and tax
3. `toggleDeduction(idx)`: Toggles deduction chip on/off; for percentage-based (RMF, SSF, etc.), calculates `income * rate` capped at maxVal
4. `taxSummaryHtml()`: Generates full printable HTML report with Thai Buddhist calendar date
5. `handlePrint()`: Calls `printDocument(html, title)` from export library
6. Checklist persists to `localStorage` with key `legalai_tax_checklist`
7. Celebration: When all 6 items checked, shows 🎉 banner for 4 seconds
8. Comparison mode: Shows side-by-side tax with/without deductions
9. Default income: 600,000 THB

#### Current State
- ✅ Excellent: Working tax calculation, progressive brackets visualized, deduction toggles
- ✅ Excellent: Checklist with localStorage persistence + celebration animation
- ✅ Excellent: Printable HTML report with full styling
- ✅ Good: Comparison mode, savings calculation, effective rate display
- ⚠️ Stub: AI Tax Optimizer button doesn't connect to real optimizer
- ⚠️ Static: Deduction values hardcoded (not pulled from tax/calculator.ts or tax/deductions.ts libraries)
- ⚠️ Missing: No connection to real `TaxPayerProfile` from tax/types.ts

#### Desired State (V4 Concierge)
- AI Tax Optimizer that analyzes real user profile and suggests optimal deduction allocation
- Year-over-year comparison
- Tax projection: "ถ้าคุณลงทุน RMF 50,000 บาท — ประหยัดภาษีได้เพิ่มอีก 7,500 บาท"
- Concierge: "วางแผนภาษีปี 2569 — เราช่วยคุณประหยัดไปแล้ว ฿XX,XXX โดยเฉลี่ย"
- Integration with real tax calculator from `lib/tax/calculator.ts`

#### Improvements Needed
1. Wire AI Tax Optimizer to real analysis (using `calculateTax()` from lib)
2. Use `TaxPayerProfile` type for structured input instead of flat deduction toggles
3. Add year-over-year comparison (2568 vs 2569)
4. Add what-if scenarios: "ถ้าซื้อ RMF เพิ่ม 50,000 → ประหยัดอีก 7,500"
5. Add spouse income input for married filing
6. Integrate `quickEstimateDeductions()` for simpler initial view

---

### 10. PRICING — `app/pricing/page.tsx` (97 lines)

**Route:** `/pricing`

#### Sections
- PageHead: "💳 แพ็กเกจและราคา" / "เลือกแพ็กเกจที่เหมาะกับคุณ — เริ่มต้นฟรี ไม่มีค่าใช้จ่ายแอบแฝง"
- Pricing cards: 4 tiers (ฟรี, Action Pack, Case Plus, SME Starter) with name, price, features list, CTA
- Feature comparison table: 11 feature rows × 4 columns
- FAQ: 3 expandable questions

#### Exact Thai Copy
- Title: "💳 แพ็กเกจและราคา"
- Subtitle: "เลือกแพ็กเกจที่เหมาะกับคุณ — เริ่มต้นฟรี ไม่มีค่าใช้จ่ายแอบแฝง"
- Free CTA: "เริ่มใช้งานฟรี"
- Pro CTA: "อัปเกรดเลย"
- Other CTA: "เลือกแพ็กเกจ"
- Compare: "📊 เปรียบเทียบฟีเจอร์"
- FAQ title: "❓ คำถามที่พบบ่อย"
- FAQ 1: "เริ่มต้นฟรีจริงหรือ?" / "ใช่! แพ็กเกจฟรีให้คุณทดลองใช้ AI วิเคราะห์ 3 ครั้ง..."
- FAQ 2: "เปลี่ยนแพ็กเกจได้ไหม?" / "ได้ทุกเมื่อ — อัปเกรดหรือดาวน์เกรดผ่านหน้าโปรไฟล์"
- FAQ 3: "ข้อมูลส่วนตัวปลอดภัยไหม?" / "เราเข้ารหัสข้อมูลตามมาตรฐานสากล..."

#### Current Algorithm
- Static rendering of PACKAGES and PACKAGE_ORDER from definitions.ts
- Feature comparison table is hardcoded HTML (not generated from PackageLimits)
- Free tier links to `/auth/signin`; paid tier buttons have empty onClick

#### Current State
- ✅ Working: Package display, comparison table, FAQ
- ⚠️ Hardcoded: Feature comparison table manually typed (should be generated from PackageLimits)
- ⚠️ Broken: Paid tier CTA buttons have empty `onClick={() => {}}`
- ⚠️ Missing: No payment gateway integration

#### Desired State (V4 Concierge)
- Dynamic feature comparison generated from PackageLimits
- "แนะนำสำหรับคุณ" badge based on usage patterns
- Monthly vs annual toggle
- Concierge: "จาก 3 เคสของคุณ — แนะนำ Action Pack (฿299) เพื่อ AI ไม่จำกัด"

#### Improvements Needed
1. Generate comparison table dynamically from PackageLimits types
2. Add payment flow integration
3. Add personalized recommendation based on user activity
4. Monthly/annual pricing toggle
5. Add enterprise/contact sales option

---

### 11. LAWYERS MARKETPLACE — `app/lawyers/page.tsx` (315 lines)

**Route:** `/lawyers`

#### Sections
- PageHead: "ค้นหาทนายที่เหมาะกับคุณ" / "ทนายทุกคนผ่านการตรวจสอบใบอนุญาตและประวัติแล้ว"
- Search bar: "⌕ ค้นหาชื่อทนาย ความเชี่ยวชาญ หรือภาษา (English, 中文...)"
- Filter chips: ทั้งหมด, กฎหมายแรงงาน, ครอบครัว, อสังหาริมทรัพย์, ผู้บริโภค, 🟢 ออนไลน์
- Disclaimer: "ข้อมูลทนายเป็นข้อมูลตัวอย่าง ควรตรวจสอบใบอนุญาตอิสระ"
- Lawyer cards: avatar (initials + online dot), verified badge, name, specialty, rating, reviews, response time, availability, languages, tags, price, CTA buttons
- Sidebar: AI matching card ("ไม่แน่ใจว่าควรเลือกใคร?") + verification list + PrototypeDataNotice

#### Exact Thai Copy (sampled)
- Title: "ค้นหาทนายที่เหมาะกับคุณ"
- Subtitle: "ทนายทุกคนผ่านการตรวจสอบใบอนุญาตและประวัติแล้ว"
- Search: "ค้นหาชื่อทนาย ความเชี่ยวชาญ หรือภาษา (English, 中文...)"
- Disclaimer: "ข้อมูลทนายเป็นข้อมูลตัวอย่าง ควรตรวจสอบใบอนุญาตอิสระ"
- Lawyer: "ทนายชลธิชา วงศ์ดี" / "กฎหมายแรงงาน • 12 ปี" / "★ 4.9" / "(327 รีวิว)" / "ตอบกลับใน 10 นาที" / "เริ่มต้น ฿800"
- Availability: "ว่างล่าสุด: พรุ่งนี้ 10:00" / "● ออนไลน์"
- Tags: "ปรึกษาวิดีโอ", "ตรวจเอกสาร", "รับว่าความ"
- Price: "ค่าปรึกษา 30 นาที"
- CTA: "ดูโปรไฟล์และนัดหมาย" / "♡ บันทึก"
- Sidebar AI: "ไม่แน่ใจว่าควรเลือกใคร?", "ให้ AI ช่วยจับคู่ทนายจากประเภทเคส งบประมาณ และเวลาที่สะดวก", "ให้ AI ช่วยเลือก"
- Verification: "เราตรวจสอบอะไรบ้าง" — "ใบอนุญาตทนายความ", "ประวัติและความเชี่ยวชาญ", "รีวิวจากผู้ใช้จริง", "การรักษาความลับ"

#### Current Algorithm
- `filtered`: Multi-filter pipeline — chip keyword, onlineOnly toggle, search query (name/specialty/languages)
- `requestConsultation(lawyer)`: Shows toast + fires analytics — NO actual booking
- `toggleSave(name)`: Toggles in local Set, shows toast
- 5 hardcoded lawyers with Thai names, specialties, ratings, languages (ไทย, English, 日本語, 中文)

#### Current State
- ✅ Working: Search + filter, lawyer cards, save toggles
- ⚠️ Broken: "ดูโปรไฟล์และนัดหมาย" doesn't navigate to lawyer detail page
- ⚠️ Broken: "ให้ AI ช่วยเลือก" only shows toast
- ⚠️ Hardcoded: All lawyer data is mock (5 sample lawyers)
- ⚠️ Missing: No booking/calendar integration

#### Desired State (V4 Concierge)
- Real lawyer profiles from database with verification badges
- AI matching that recommends lawyers based on user's active case category
- "จองเลย" with real calendar/time slot integration
- Concierge: "จากเคสแรงงานของคุณ — ทนายชลธิชาเชี่ยวชาญด้านนี้โดยตรง"

#### Improvements Needed
1. Wire "ดูโปรไฟล์และนัดหมาย" to `/lawyers/${lawyer.id}`
2. Implement real booking flow with calendar integration
3. Connect to Supabase for real lawyer profiles
4. AI matching based on case category + budget + language preference
5. Add rating/review sorting

---

### 12. LAWYER DETAIL — `app/lawyers/[id]/page.tsx` (565 lines)

**Route:** `/lawyers/[id]`

#### Sections
- PageHead: verified badge + name + years + languages + "นัดหมายปรึกษา" button
- Profile card: avatar + specialties pills + bio + stats (rating, reviews, starting price)
- Service scope list: icon + name + description + price
- Reviews section: rating summary + 3 sample reviews with star ratings
- Booking widget (right sidebar): multi-step booking flow
  - Initial: "🗓 นัดหมายปรึกษา" + "เริ่มนัดหมาย" button
  - Step 1 (select): Service scope dropdown + date selector + time slot grid + note textarea
  - Step 2 (confirm): Booking summary (service, date, time, price, note)
  - Step 3 (done): "✅ จองสำเร็จ!" + booking details + "จองอีกครั้ง" / "ไปที่เคสของฉัน"
- Verification info: 4 check marks
- PrototypeDataNotice

#### Exact Thai Copy
- Verified: "✓ ตรวจสอบแล้ว"
- CTA: "นัดหมายปรึกษา"
- About: "เกี่ยวกับทนาย"
- Bio: "ทนายความผู้เชี่ยวชาญด้าน... ด้วยประสบการณ์มากกว่า {N} ปี พร้อมให้คำปรึกษาอย่างมืออาชีพ ตรงไปตรงมา และรักษาความลับของลูกความสูงสุด"
- Stats: "คะแนน", "รีวิว", "เริ่มต้น"
- Services: "ขอบเขตการให้บริการ"
- Reviews: "รีวิวจากผู้ใช้บริการ"
- Booking: "🗓 นัดหมายปรึกษา", "เลือกวัน เวลา และขอบเขตบริการที่คุณต้องการ"
- Select: "เลือกบริการ", "เลือกวันที่", "เลือกเวลา", "หมายเหตุ (ไม่บังคับ)"
- Confirm: "บริการ:", "วันที่:", "เวลา:", "ราคา:", "ย้อนกลับ", "ยืนยันการจอง"
- Done: "จองสำเร็จ!", "จองอีกครั้ง", "ไปที่เคสของฉัน"
- Verification: "การตรวจสอบ", "ใบอนุญาตทนายความ", "ประวัติและความเชี่ยวชาญ", "รีวิวจากผู้ใช้จริง", "การรักษาความลับ"

#### Current Algorithm
- `useMemo` to find lawyer by ID from `sampleLawyers`
- `generateTimeSlots()`: Creates 16 half-hour slots from 9:00-17:00
- `dates`: Generates 7 days from today with Thai Buddhist calendar labels
- Booking flow: 3-step state machine (select → confirm → done)
- `confirmBooking()`: Shows toast + fires analytics
- `resetBooking()`: Resets all booking state to initial
- 404 fallback if lawyer not found

#### Current State
- ✅ Working: Profile display, booking flow UI, review display
- ✅ Good: Multi-step booking with service/date/time selection
- ⚠️ Broken: Booking doesn't connect to any real backend
- ⚠️ Hardcoded: 3 sample reviews, sample lawyer data
- ⚠️ Missing: No real calendar availability checking

#### Desired State (V4 Concierge)
- Real booking with calendar integration and confirmation
- Concierge: "ทนายคนนี้ว่างพรุ่งนี้ 10:00 — จองเลย?"
- Integrated with payment: "ชำระเงิน ฿800 เพื่อยืนยันการจอง"
- Video call link generation after booking confirmation

#### Improvements Needed
1. Connect booking to real backend/calendar API
2. Add payment integration for booking confirmation
3. Real lawyer profiles from database
4. Real reviews from database
5. Video call integration (LINE Meet, Google Meet, Zoom)

---

### 13. PROFILE SETTINGS — `app/profile/page.tsx` (196 lines)

**Route:** `/profile`

#### Sections
- PageHead: "โปรไฟล์และการตั้งค่า" / "จัดการข้อมูล บัญชี และความเป็นส่วนตัวของคุณ"
- Profile card: avatar (initials "นภ") with edit button, name, email, member since, package pill, edit button
- Settings layout:
  - Sidebar nav: 6 tabs — ข้อมูลส่วนตัว, การแจ้งเตือน, ความเป็นส่วนตัว, การแสดงผล, แพ็กเกจและการชำระเงิน, ช่วยเหลือ
  - Content panels:
    - Personal: 4 fields (ชื่อ, นามสกุล, อีเมล, เบอร์โทรศัพท์) + save button
    - Notifications: LINE connection toggle + email notification select
    - Privacy: AI consent toggle + PDPA rights (ส่งออกข้อมูล, ลบข้อมูล) + connected accounts
    - Display: language select (ไทย/English) + font size select (มาตรฐาน/ใหญ่)
    - Package: current package + upgrade CTA
    - Help: 5 help items + contact email

#### Exact Thai Copy
- Title: "โปรไฟล์และการตั้งค่า"
- Subtitle: "จัดการข้อมูล บัญชี และความเป็นส่วนตัวของคุณ"
- Profile: "นภัสสร วัฒนะ", "napassorn@example.com • สมาชิกตั้งแต่ มิ.ย. 2569", "แพ็กเกจพื้นฐาน"
- Tabs: "○ ข้อมูลส่วนตัว", "♧ การแจ้งเตือน", "⌾ ความเป็นส่วนตัว", "◫ การแสดงผล", "฿ แพ็กเกจและการชำระเงิน", "ⓘ ช่วยเหลือ"
- AI consent: "เมื่อเปิด AI consent — ข้อมูลเคสของคุณจะถูกส่งให้ DeepSeek AI เพื่อวิเคราะห์ เมื่อปิด — ข้อมูลใหม่จะไม่ถูกส่งให้ AI แต่คุณจะยังใช้ฟีเจอร์อื่นได้ตามปกติ"
- PDPA: "สิทธิข้อมูลส่วนบุคคล (PDPA)", "📤 ส่งออกข้อมูลของฉัน", "🗑️ ลบข้อมูลของฉันทั้งหมด"
- Package: "แพ็กเกจปัจจุบัน", "แพ็กเกจพื้นฐาน (ฟรี)", "อัปเกรดเพื่อปลดล็อกฟีเจอร์เพิ่ม: AI วิเคราะห์ไม่จำกัด, เอกสารกฎหมาย, ปรึกษาทนาย, LINE แจ้งเตือน"
- Help: "📖 วิธีเริ่มต้นใช้งาน:", "🤖 AI Diagnosis:", "📄 เอกสาร:", "👨‍⚖️ ทนาย:", "📧 ติดต่อ: help@legalai.co.th"

#### Current Algorithm
- `toggleLine()`: Toggles boolean + fires `line_opt_in_changed` event
- `toggleAiConsent()`: Toggles AI consent + shows toast
- All "save" buttons show toast notifications — no real persistence
- Form fields have `defaultValue` (not controlled `value`) — uncontrolled inputs

#### Current State
- ✅ Working: Tab navigation, form rendering, toggle states
- ⚠️ Broken: No real data persistence (all save buttons are toast-only)
- ⚠️ Hardcoded: User data (name, email, phone) is hardcoded
- ⚠️ Uncontrolled: Form fields use defaultValue instead of controlled value — edits lost on tab switch
- ⚠️ Missing: No avatar upload, no password change, no 2FA settings

#### Desired State (V4 Concierge)
- Real profile sync with Supabase auth
- Actual LINE connection via LINE Login/LIFF
- Real data export (GDPR/PDPA compliance)
- Concierge: "โปรไฟล์ของคุณ — ข้อมูลนี้ช่วยให้ AI วิเคราะห์ได้แม่นยำขึ้น"

#### Improvements Needed
1. Connect to Supabase auth for real user profile
2. Make form fields controlled (use `value` + `onChange` instead of `defaultValue`)
3. Implement real LINE connection via LIFF
4. Add real data export functionality
5. Add password change / 2FA settings
6. Add avatar image upload

---

### 14. TERMS OF SERVICE — `app/terms/page.tsx` (97 lines)

**Route:** `/terms` — Server component

#### Sections
- Title: "ข้อกำหนดการใช้บริการ (Terms of Service)"
- Effective date: "มีผลบังคับใช้: 9 สิงหาคม 2569"
- 9 sections: การยอมรับ, ขอบเขตการให้บริการ, ข้อจำกัดความรับผิด, การใช้บริการอย่างเหมาะสม, การระงับหรือยกเลิกบัญชี, ทรัพย์สินทางปัญญา, การเปลี่ยนแปลงข้อกำหนด, กฎหมายที่ใช้บังคับ, ติดต่อ
- Warning box with "⚠️ สำคัญ:" listing 5 disclaimers

#### Current State
- ✅ Complete: Full legal terms in Thai
- ✅ Good: Warning box prominently placed
- ⚠️ Static: No interactive elements, no version history

#### Improvements
1. Add "last updated" version tracking
2. Add table of contents for easy navigation
3. Add English version toggle

---

### 15. PRIVACY POLICY — `app/privacy/page.tsx` (94 lines)

**Route:** `/privacy` — Server component

#### Sections
- Title: "นโยบายความเป็นส่วนตัว (Privacy Policy)"
- Effective date: "มีผลบังคับใช้: 9 สิงหาคม 2569"
- 8 sections with 2 data tables
- PDPA rights table: 5 rights with how-to-use instructions

#### Current State
- ✅ Complete: Full privacy policy with PDPA compliance
- ✅ Good: Data tables for clarity
- ⚠️ Static: No cookie consent banner integration

#### Improvements
1. Add cookie consent management UI
2. Add data processing activity log
3. Add DPO contact information

---

### 16. NOTIFICATIONS — `app/notifications/page.tsx` (129 lines)

**Route:** `/notifications`

#### Sections
- PageHead: "การแจ้งเตือน" / "ติดตามกำหนดการและความคืบหน้าสำคัญ" + "✓ อ่านทั้งหมดแล้ว" button
- Tabs: ทั้งหมด (3), เคสของฉัน, เอกสาร, ระบบ
- Notification list: article cards with tone icon, title, body, timestamp, CTA link
- Unread indicator dot
- Reminder card: "◷ ตั้งค่าการแจ้งเตือนให้เหมาะกับคุณ" / link to profile

#### Exact Thai Copy
- Title: "การแจ้งเตือน"
- Subtitle: "ติดตามกำหนดการและความคืบหน้าสำคัญ"
- Tabs: "ทั้งหมด", "เคสของฉัน", "เอกสาร", "ระบบ"
- Empty: "ไม่มีการแจ้งเตือนในหมวดนี้"
- Reminder: "ตั้งค่าการแจ้งเตือนให้เหมาะกับคุณ", "เลือกช่องทางและเวลาที่ต้องการรับการแจ้งเตือนผ่านแอป อีเมล หรือ LINE"
- Link: "ตั้งค่าการแจ้งเตือน"

#### Current Algorithm
- `sampleNotifications` from mock data (4 notifications)
- `NOTIFICATION_CATEGORY` maps notification IDs to tabs
- `markAllRead()`: Sets all IDs in readIds Set
- `isRead()`: Checks readIds Set
- Notification count only shown on "ทั้งหมด" tab

#### Current State
- ✅ Working: Tab filtering, mark-all-read, notification display
- ⚠️ Hardcoded: All 4 notifications are sample data
- ⚠️ Missing: No real-time notifications, no push notifications
- ⚠️ Missing: Read state not persisted (resets on page reload)

#### Desired State (V4 Concierge)
- Real notifications from Supabase with real-time subscription
- Push notifications via LINE
- Concierge: "คุณมี 2 กำหนดการที่ใกล้ถึง — อย่าลืม!"
- Smart grouping: "เอกสาร 3 รายการรอตรวจสอบ"

#### Improvements Needed
1. Connect to Supabase real-time subscriptions
2. Persist read state to database
3. Add LINE push notification integration
4. Add notification preferences per type

---

### 17. AI ASSISTANT — `app/assistant/page.tsx` (268 lines)

**Route:** `/assistant`

#### Sections
- Header: AI orb (SparklesIcon) + "AI Legal Assistant" + "พร้อมช่วยเหลือ • อ้างอิงกฎหมายไทย" + menu button
- Context banner: folder icon + "กำลังใช้ข้อมูลจากเคส" + case title + "เปลี่ยน" button
- Messages area:
  - "วันนี้" day label
  - PrototypeDataNotice: "ผู้ช่วย AI — ยังไม่ใช่ทนายความ"
  - Chat messages: user (right-aligned) + assistant (with SparklesIcon + SourceCitation)
  - Quick replies on first message: "มีหนังสือแจ้ง", "แจ้งด้วยวาจา", "ไม่ได้แจ้งเหตุผล"
  - Loading: "AI กำลังพิมพ์..." + "กำลังคิด"
- Chat compose:
  - Suggestion buttons: "สรุปสิทธิของฉัน", "ต้องเตรียมอะไรบ้าง?", "ช่วยร่างเอกสาร"
  - Input area: attach button + textarea + send button
  - Disclaimer: "AI อาจให้ข้อมูลคลาดเคลื่อน โปรดตรวจสอบข้อมูลสำคัญกับผู้เชี่ยวชาญ"

#### Exact Thai Copy
- Header: "AI Legal Assistant", "พร้อมช่วยเหลือ • อ้างอิงกฎหมายไทย"
- Welcome: "สวัสดีค่ะ ฉันคือ AI Legal Assistant เล่าเหตุการณ์ให้ฟังได้เลย ฉันจะช่วยสรุปประเด็นและแนะนำขั้นตอนถัดไปค่ะ"
- Context: "กำลังใช้ข้อมูลจากเคส", "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า"
- Quick replies: "มีหนังสือแจ้ง", "แจ้งด้วยวาจา", "ไม่ได้แจ้งเหตุผล"
- Suggestions: "สรุปสิทธิของฉัน", "ต้องเตรียมอะไรบ้าง?", "ช่วยร่างเอกสาร"
- Loading: "AI กำลังพิมพ์..."
- Error: "เกิดข้อผิดพลาดในการเชื่อจ่อ โปรดลองส่งคำถามอีกครั้ง"
- Fallback: "ขออภัย ฉันยังไม่สามารถตอบได้ในตอนนี้ โปรดลองอีกครั้ง"
- Disclaimer: "AI อาจให้ข้อมูลคลาดเคลื่อน โปรดตรวจสอบข้อมูลสำคัญกับผู้เชี่ยวชาญ"

#### Current Algorithm
1. Initializes with WELCOME message
2. `send(textToSend?)`: Creates user message, builds history array, POSTs to `/api/ai/assistant`
3. API payload: `{message, history, category: "labour", caseTitle: CASE_TITLE}`
4. Response: `{reply: {text, citations}}` — renders with SourceCitation component
5. Auto-scroll to latest message via useEffect
6. Enter key sends (shift+Enter for newline)
7. Quick replies fill the textarea; suggestion buttons send directly
8. Attach button disabled (no file upload)
9. Returns focus to textarea after send

#### Current State
- ✅ Working: Chat with real AI backend, message history, citations display
- ⚠️ Hardcoded: Case context always "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า" (labour)
- ⚠️ Hardcoded: Category always "labour"
- ⚠️ Missing: File attachment not implemented
- ⚠️ Missing: No conversation persistence (refresh loses all messages)
- ⚠️ Missing: Quick replies and suggestions are static

#### Desired State (V4 Concierge)
- Dynamic case context from user's active cases
- Dynamic quick replies based on conversation stage
- Concierge-style proactive suggestions: "จากที่คุณเล่า — ฉันแนะนำให้..."
- Conversation persistence to Supabase
- Multi-case support: switch between active cases
- Drive-aware tone adaptation based on conversation sentiment

#### Improvements Needed
1. Read active case context from URL params or user session
2. Generate dynamic quick replies based on AI response
3. Add conversation persistence (localStorage or Supabase)
4. Enable file attachment (images, PDFs)
5. Add case switcher dropdown in context banner
6. Add voice input option
7. Drive detection on conversation for tone adaptation

---

### 18. CASES LIST — `app/cases/page.tsx` (154 lines)

**Route:** `/cases`

#### Sections
- PageHead: "เคสของฉัน" / "ทำต่อจากจุดที่ค้างไว้ หรือเริ่มเคสใหม่ได้ที่นี่" + "สร้างเคสใหม่" button
- Stat grid: 4 stat cards — เคสทั้งหมด (3), กำลังดำเนินการ (1), รอเอกสาร (1), เสร็จสิ้น (1)
- Filter row: ทั้งหมด, กำลังดำเนินการ, รอเอกสาร, เสร็จสิ้น — with counts
- Case list: CaseProgressCard components for each visible case
- Empty state: "ยังไม่มีเคสในสถานะนี้"
- Bottom link: "+ เริ่มเคสใหม่" / "วิเคราะห์เคสของคุณฟรี"
- PrototypeDataNotice

#### Exact Thai Copy
- Title: "เคสของฉัน"
- Subtitle: "ทำต่อจากจุดที่ค้างไว้ หรือเริ่มเคสใหม่ได้ที่นี่"
- CTA: "+ สร้างเคสใหม่"
- Stats: "เคสทั้งหมด", "กำลังดำเนินการ", "รอเอกสาร", "เสร็จสิ้น"
- Bottom: "เริ่มเคสใหม่", "วิเคราะห์เคสของคุณฟรี"

#### Current Algorithm
- `sampleCases` from mock data (3 sample cases)
- `caseRoutes`: Maps case IDs to timeline/evidence pages
- `visible`: Filters by active filter key
- Filter button shows count of cases in that status

#### Current State
- ✅ Working: Case listing, filtering, stat display
- ⚠️ Hardcoded: All 3 cases are sample data
- ⚠️ Missing: No real case creation from user's diagnosis history
- ⚠️ Missing: No search within cases

#### Desired State (V4 Concierge)
- Real cases from database tied to user account
- Case sorting by urgency/deadline
- Concierge: "เคสแรงงานของคุณ — deadline ในอีก 5 วัน"
- Case progress visualization (not just percentage number)

#### Improvements Needed
1. Connect to Supabase for real case data
2. Add sorting options (deadline, created date, status)
3. Add case search
4. Add urgency indicators on each case card
5. Wire "สร้างเคสใหม่" to actual diagnosis flow with category selection

---

### 19. CASE TIMELINE — `app/cases/[caseId]/timeline/page.tsx` (168 lines)

**Route:** `/cases/[caseId]/timeline`

#### Sections
- Breadcrumb: "เคสของฉัน › [case title]"
- Case header: status pill + title + reference + created date
- Case tabs: ภาพรวม, ไทม์ไลน์ (active), หลักฐาน (X/Y), เอกสาร
- Timeline card: "แผนดำเนินการ" + progress pill + timeline items (done/current/future)
- Current step actions: "สร้างหนังสือทวงถาม" link + "ดูหลักฐาน" link
- GentleConsequenceNotice
- Sidebar: case summary (ประเภทเรื่อง, สถานะหลักฐาน, ความเร่งด่วน) + AI assistant prompt

#### Exact Thai Copy
- Tabs: "ภาพรวม", "ไทม์ไลน์", "หลักฐาน", "เอกสาร"
- Timeline: "แผนดำเนินการ", "ขั้นตอนและกำหนดเวลาของเคสนี้"
- Progress: "คืบหน้า {N}%"
- Sidebar: "สร้างเคส", "ประเภทเรื่อง", "สถานะหลักฐาน", "ความเร่งด่วน"
- AI prompt: "มีคำถามเกี่ยวกับขั้นตอน?", "ถาม AI Legal Assistant ได้ทุกเมื่อ"
- CTA: "ถาม AI →"

#### Current Algorithm
- Static rendering of case-1 data
- Timeline items from `sampleTimeline` with done/current/future statuses
- Evidence progress computed from `sampleEvidenceRequirements`
- ConsequenceNotice warns about estimated deadlines

#### Current State
- ✅ Working: Timeline display, tab navigation
- ⚠️ Hardcoded: Timeline always shows case-1 data regardless of caseId
- ⚠️ Missing: No dynamic timeline updates (no progress tracking)

#### Desired State (V4 Concierge)
- Dynamic timeline driven by user's actual progress
- Concierge: "ขั้นตอนต่อไป — สร้างหนังสือทวงถามภายใน 3 วัน"
- Auto-updating timeline as user completes steps
- Integration with notification system for deadline reminders

#### Improvements Needed
1. Read actual caseId param and load corresponding timeline
2. Track user progress through timeline steps
3. Add deadline countdown display
4. Wire "สร้างหนังสือทวงถาม" to document creation with pre-filled context

---

### 20. EVIDENCE — `app/cases/[caseId]/evidence/page.tsx` (542 lines)

**Route:** `/cases/[caseId]/evidence`

#### Sections
- PageHead: "หลักฐานและเอกสาร" / "รวบรวมหลักฐานเพื่อเสริมความแข็งแรงให้เคสของคุณ" + "เพิ่มหลักฐาน" button
- Readiness score: ring display (X/Y รายการ) + "ควรเพิ่มอีก N รายการ" pill + description
- Drag-and-drop zone: "ลากไฟล์มาวาง หรือคลิกเพื่อเลือก" / "PDF, JPG, PNG • สูงสุด 20 MB/ไฟล์ • อัปโหลดได้หลายไฟล์"
- Drag active state: "วางไฟล์ที่นี่" with blue highlight
- Uploaded files list: file cards with icon, name, size, link status, connect/remove buttons
- Linking selector: choose evidence item to connect file to
- Evidence checklist: toggleable items with labels + hints + file indicators + upload buttons
- Sidebar: tips card + security box + PrototypeDataNotice + back link

#### Exact Thai Copy
- Title: "หลักฐานและเอกสาร"
- Subtitle: "รวบรวมหลักฐานเพื่อเสริมความแข็งแรงให้เคสของคุณ"
- CTA: "+ เพิ่มหลักฐาน"
- Score pill: "ควรเพิ่มอีก {N} รายการ"
- Score title: "ความพร้อมด้านหลักฐาน"
- Drop zone: "ลากไฟล์มาวาง หรือคลิกเพื่อเลือก", "PDF, JPG, PNG • สูงสุด 20 MB/ไฟล์ • อัปโหลดได้หลายไฟล์"
- Drag active: "วางไฟล์ที่นี่", "ปล่อยเพื่ออัปโหลด"
- Files: "ไฟล์ที่อัปโหลด ({N})", "ล้างทั้งหมด"
- Link selector: "เลือกหลักฐานที่ต้องการเชื่อมโยง:"
- Checklist: "รายการหลักฐานที่ต้องรวบรวม"
- Tips: "💡 เคล็ดลับ", "ลากไฟล์จากโฟลเดอร์มาวางที่โซนอัปโหลดได้ทันที"
- Security: "ไฟล์ของคุณปลอดภัย", "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยให้บุคคลภายนอก"

#### Current Algorithm
- `items`: Evidence checklist from `sampleEvidenceRequirements`
- `toggle(id)`: Toggles provided state
- `validateFile(file)`: Checks type (PDF/JPG/PNG) and size (20MB max)
- `addFiles(newFiles)`: Validates and adds to local files state
- `removeFile(id)`: Removes from files, unlinks from evidence
- `linkFileToEvidence(fileId, evidenceId)`: Links file to evidence item, marks as provided
- Drag events: `dragEnter`, `dragOver`, `dragLeave`, `drop` — sets visual state
- Hidden file input for click-to-upload fallback
- No real upload endpoint (files stay in local state)

#### Current State
- ✅ Excellent: Full drag-and-drop UX with visual feedback
- ✅ Good: File validation, file-evidence linking system
- ⚠️ Broken: No real file upload (files only in local state)
- ⚠️ Broken: File list lost on page refresh
- ⚠️ Missing: No Supabase storage integration

#### Desired State (V4 Concierge)
- Real file upload to Supabase Storage
- AI-powered evidence analysis: "ตรวจพบว่าสัญญาจ้างของคุณมีลายเซ็น — ✓"
- Concierge: "คุณมีหลักฐาน 3 จาก 5 รายการ — อีก 2 รายการคือ..."
- OCR for uploaded documents to auto-extract key information
- Evidence chain visualization

#### Improvements Needed
1. Wire real file upload to Supabase Storage
2. Add file preview (image thumbnails, PDF viewer)
3. Add AI-powered document analysis
4. Add OCR for auto-filling case data
5. Persist uploaded files across sessions

---

### 21. ADMIN — `app/admin/page.tsx` (713 lines)

**Route:** `/admin`

#### Sections
- PageHead: "LegalAI Admin" / "สำหรับการจัดการเนื้อหาและการตรวจสอบ" + ADMIN pill
- Legal note: "หน้านี้เป็นต้นแบบ การเข้าถึงจริงต้องมีบทบาท admin และ MFA"
- Stat cards: 4 dashboard stats (เคสที่เปิดอยู่: 128, ผู้ใช้: 3,420, รอตรวจสอบทนาย: 7, รายได้: ฿86,400)
- Quick actions: ตรวจสอบทนายใหม่, ส่งออกรายงาน, ตั้งค่าระบบ
- Revenue dashboard:
  - 4 revenue stream cards with share bars
  - Monthly line chart (SVG with gradient, hover tooltips, data dots)
  - Legend: "— รายได้รายเดือน", "● ส.ค. (ล่าสุด)", "↗ +91% YoY"
  - Projection: "📊 คาดการณ์รายได้ทั้งปี 2569: ฿650,000 – ฿850,000"
- Module grid: 6 admin modules with badges (ทนาย, แหล่งกฎหมาย, เทมเพลต, รายงาน, บันทึก, สนับสนุน)
- Activity feed: filter row + 5 recent activities with color dots
- System health: "🟢 ระบบทำงานปกติ" / "API uptime 99.8% • Last deploy: 10 ส.ค. 2569"

#### Current State
- ✅ Excellent: Full admin dashboard mockup with SVG chart, revenue breakdown, activity feed
- ⚠️ Entirely mock: All data is hardcoded, no real admin functionality
- ⚠️ No auth: Page is publicly accessible (no admin guard)
- ⚠️ Buttons: All quick action buttons show "ฟีเจอร์จะพร้อมใช้งานเมื่อระบบ production พร้อม"

#### Desired State (V4 Concierge)
- Real admin dashboard with live data from Supabase
- Role-based access control (RBAC)
- Lawyer verification workflow
- Content moderation tools
- Revenue analytics with real data

---

### 22. ONBOARDING — `app/onboarding/page.tsx` (563 lines)

**Route:** `/onboarding`

#### Sections
- Same focus-layout as diagnosis (header + progress + question card)
- 5 steps:
  1. Terms consent: 2 checkboxes (ข้อกำหนด + นโยบาย) + links to /terms and /privacy
  2. AI consent: 1 checkbox + disclaimer "คุณสามารถเพิกถอนความยินยอมและลบข้อมูลได้ตลอดเวลา"
  3. Notifications: 3 checkboxes (ในแอป, อีเมล, LINE)
  4. Email verification: email input + send code button + 6-digit OTP input + verify button
  5. Profile: name input + language select (ไทย/English) + "เสร็จสิ้นการตั้งค่า" submit
- Progress: "การตั้งค่าบัญชีครั้งแรก" + "ขั้นตอน {N} จาก 5"
- Guard: Redirects to /auth/signin if no authenticated user

#### Current Algorithm
- `useAuth()` for session check, redirect to sign-in if not authenticated
- Step validation per step (terms both checked, AI consent checked, email verified, name filled)
- Email verification mocked: any 6-digit code accepted, simulated 1.2s delay
- On finish: toast + route to "/"
- No real data persistence

#### Current State
- ✅ Working: Multi-step flow, validation, auth guard
- ⚠️ Mock: Email verification accepts any code
- ⚠️ Missing: No real data persistence to user profile
- ⚠️ Missing: No email service integration

#### Improvements Needed
1. Wire real email OTP via Supabase Auth
2. Persist onboarding preferences to user profile
3. Add skip option for email verification
4. Add LINE connection step (LIFF integration)

---

### 23. SIGN IN — `app/auth/signin/page.tsx` (212 lines)

**Route:** `/auth/signin`

#### Sections
- Focus layout with header (back + Brand + close)
- Question card:
  - AI orb (✦) + "ปลอดภัย • เข้ารหัสด้วย OTP" pill
  - "เข้าสู่ระบบ LegalAI" + "ลงชื่อเข้าใช้เพื่อบันทึกเคสและเอกสารของคุณ"
  - Stage 1 (email): email input + "ส่งรหัสยืนยัน" button + "หรือ" divider + "ดำเนินต่อด้วย Google" button
  - Stage 2 (OTP): "เราส่งรหัส 6 หลักไปยัง {email} แล้ว" + OTP input + "ยืนยันและเข้าสู่ระบบ" + "แก้ไขอีเมล"
- Disclaimer: "การเข้าสู่ระบบแปลว่าคุณยอมรับข้อกำหนดการใช้บริการและนโยบายความเป็นส่วนตัว"
- Back link: "‹ กลับหน้าหลัก"

#### Current Algorithm
- `useAuth()`: Uses `signInWithEmail`, `verifyOtp`, `signInWithGoogle`
- Already signed in? → redirects to `/onboarding`
- Email stage: Validates email, calls Supabase magic link / OTP
- OTP stage: 6-digit numeric input, calls `verifyOtp`
- Error display from Supabase auth errors
- Google OAuth redirects to `/auth/callback`

#### Current State
- ✅ Working: Real Supabase auth (magic link/OTP + Google OAuth)
- ✅ Good: Two-stage flow with clear UX
- ⚠️ Missing: No phone number auth option
- ⚠️ Missing: No "forgot password" flow (passwordless, so N/A but could add recovery)

---

### 24. 404 — `app/not-found.tsx` (20 lines)

**Route:** any unmatched route

#### Sections
- Focus layout centered
- AI orb: "⌕"
- Pill: "404"
- "ไม่พบหน้าที่คุณค้นหา"
- "หน้าที่คุณเข้าถึงอาจถูกย้าย หรือไม่มีอยู่อีกต่อไป"
- "กลับหน้าหลัก" link

#### Current State
- ✅ Clean: Simple, clear, Thai-localized 404
- ⚠️ Missing: No search suggestion, no sitemap links

#### Improvements
1. Add search box: "ลองค้นหาสิ่งที่คุณต้องการ"
2. Add popular page links

---

### 25. ERROR — `app/error.tsx` (51 lines)

**Route:** triggered by Next.js error boundary

#### Sections
- Focus layout centered
- AI orb: "!"
- "เกิดข้อผิดพลาด"
- "ขออภัย เกิดปัญหาขณะแสดงหน้านี้ ข้อมูลของคุณยังปลอดภัย"
- "ลองอีกครั้ง" button + "กลับหน้าหลัก" link

#### Current Algorithm
- `reset()`: Next.js error boundary reset function
- Only logs error digest in non-production (never raw error to avoid leaking sensitive context)

#### Current State
- ✅ Good: User-friendly error state, preserves trust ("ข้อมูลของคุณยังปลอดภัย")
- ✅ Good: Never exposes stack traces
- ⚠️ Missing: No error reporting integration (Sentry, etc.)

---

### 26. ANALYSIS RESULT — `app/analysis/[caseId]/page.tsx` (277 lines)

**Route:** `/analysis/[caseId]?session=new` (arrives from diagnosis wizard)

#### Sections
- PageHead: headline + "สรุปจาก AI พร้อมแหล่งอ้างอิงกฎหมายไทย" + AI pill + save button
- Evidence readiness hero: readiness label pill + "ความพร้อมข้อมูล/หลักฐาน X จาก Y" + summary + progress bar
- Rights section: numbered cards with icons, labels, details
- Sources section: SourceCitation components + GentleConsequenceNotice
- Next actions: step-by-step plan (from AI or sampleActionPlan fallback)
- CTA buttons: "สร้างเคสและเริ่มดำเนินการ" + "♙ ปรึกษาทนายเกี่ยวกับเคสนี้"
- Model info: "แนะนำโดย AI" / "ข้อมูลตัวอย่าง" badge + model name + source version
- LegalDisclaimer

#### Exact Thai Copy
- AI pill: "✦ วิเคราะห์โดย AI"
- Fallback pill: "✓ จัดแผนเบื้องต้นให้แล้ว"
- Save: "♡ บันทึกไว้ทำต่อ" / "✓ บันทึกแล้ว"
- Rights: "สิทธิที่ควรตรวจสอบเพิ่มเติม"
- Sources: "ทำไมเราจึงแนะนำแบบนี้"
- Actions: "แผนทีละขั้น", "จากวันนี้ไปจนถึงการยื่นเรื่อง"
- CTAs: "สร้างเคสและเริ่มดำเนินการ", "♙ ปรึกษาทนายเกี่ยวกับเคสนี้"

#### Current Algorithm
1. Reads `legalai:latest-analysis` from sessionStorage
2. If AI result present: renders AI headline, summary, rights, citations, next actions, limitations
3. If absent: falls back to hardcoded sample data
4. Evidence readiness: explainable ratio (X of Y items provided), never a win probability
5. Rights: Maps from AI result or falls back to 3 hardcoded rights
6. Next actions: From AI result or falls back to `sampleActionPlan`
7. `saved` state: Local toggle only

#### Current State
- ✅ Working: AI result display, fallback to sample data
- ✅ Good: Explainable evidence readiness (not outcome probability)
- ⚠️ SessionStorage: Lost if user opens in new tab or clears storage
- ⚠️ Missing: No persistence of analysis results to database

#### Desired State (V4 Concierge)
- Analysis results persisted to user's case history
- Concierge: "จากการวิเคราะห์ — คุณมีสิทธิได้รับค่าชดเชย X บาท พร้อมเริ่มดำเนินการ?"
- Drive-aware action plan tone based on detected drives
- One-click "เริ่มดำเนินการ" to create case and populate timeline

#### Improvements Needed
1. Persist analysis to Supabase instead of sessionStorage
2. Add "แชร์ผลวิเคราะห์กับทนาย" feature
3. Drive-aware tone on action plan
4. One-click case creation from analysis

---

### 27. DESIGN SYSTEM — `app/design-system/page.tsx` (139 lines)

**Route:** `/design-system` — Server component

#### Sections
- Design tokens: 8 colors (Primary, Primary dark, Surface, Canvas, Success, Warning, Danger, Ink)
- Type scale & spacing: Display 40/48, Heading 28/36, Title 20/28, Body 16/26, Caption 13/20
- Spacing: 4, 8, 12, 16, 24, 32, 48px
- Components: Primary, Secondary, Disabled buttons; default + invalid inputs; 3 Pill variants
- Interaction states: Loading (skeleton), Empty, Error, Success
- Developer handoff: Responsive breakpoints, accessibility specs, state model, core tokens

#### Current State
- ✅ Complete: Design system documentation page
- ✅ Good: Handoff notes cover responsive, a11y, state model, tokens

---

## PART 2: LIBRARY FILE AUDIT (15 Files)

---

### 28. DIAGNOSIS CONFIG — `lib/legal/diagnosis-config.ts` (462 lines)

**Purpose:** Versioned diagnosis question configuration — drives the wizard.

**Key Types:** `DiagnosisConfig`, `DiagnosisQuestion`

**All 12 Categories, Questions, and Options:**

| Category | Q1 | Q2 | Q3 | Q4 | Q5 |
|----------|----|----|----|----|-----|
| labour | เกิดอะไรขึ้น? (4) | ทำงานมานาน? (4) | แจ้งล่วงหน้า? (4) | หลักฐาน? (4 multi) | — |
| consumer | ปัญหาคือ? (4) | ช่องทาง? (4) | มูลค่า? (4) | หลักฐาน? (4 multi) | — |
| debt | สถานการณ์? (4) | ยอดหนี้? (4) | นานแค่ไหน? (4) | หลักฐาน? (4 multi) | — |
| housing | ปัญหา? (4) | สัญญา? (4) | เช่านาน? (4) | หลักฐาน? (4 multi) | — |
| family | เรื่อง? (4) | สถานะสมรส? (4) | มีบุตร? (4) | หลักฐาน? (4 multi) | — |
| accident | เกิดอะไร? (4) | ใครผิด? (4) | บาดเจ็บ? (4) | หลักฐาน? (4 multi) | — |
| online_fraud | หลอกแบบไหน? (5) | โอนเงินเท่าไหร่? (4) | เมื่อไหร่? (4) | หลักฐาน? (5 multi) | — |
| crime | เกิดอะไร? (4) | เมื่อไหร่? (4) | หลักฐาน? (5 multi) | แจ้งความ? (3) | — |
| government | ปัญหาอะไร? (4) | นานแค่ไหน? (4) | หน่วยงาน? (5) | เอกสาร? (4 multi) | — |
| insurance | ปัญหาประกัน? (4) | เมื่อไหร่? (4) | หลักฐาน? (5 multi) | บ.ประกันตอบ? (4) | — |
| defamation | เกิดอะไร? (4) | ช่องทาง? (6) | ใครโพสต์? (4) | เมื่อไหร่? (4) | หลักฐาน? (4 multi) |
| property | ปัญหาอะไร? (5) | เอกสารสิทธิ์? (4) | นานแค่ไหน? (4) | หลักฐาน? (4 multi) | — |

**All questions have:**
- `id`: Unique identifier
- `title`: Thai question text
- `rationale`: Why we ask (transparency for user trust)
- `multi`: Boolean for single vs multi-select
- `options`: Array of Thai option strings

**Current State:**
- ✅ Complete: All 12 categories with 4-5 questions each (50 total questions)
- ✅ Versioned: `diagnosis-v1` for audit trail
- ⚠️ Missing: Fear calibration question not integrated into config flow

**Improvements Needed:**
1. Integrate `FEAR_CALIBRATION_QUESTION` as configurable step 0
2. Add question dependency logic (skip questions based on previous answers)
3. Add question priority ordering for different urgency levels

---

### 29. LEGAL SOURCES — `lib/legal/sources.ts` (284 lines)

**Purpose:** Authoritative legal source registry — prevents fabricated citations.

**Key Types:** `LegalSource`

**Source Count by Category:**
- labour: 3 (พ.ร.บ. คุ้มครองแรงงาน, พ.ร.บ. ศาลแรงงาน, พ.ร.บ. ประกันสังคม)
- consumer: 2 (พ.ร.บ. คุ้มครองผู้บริโภค, พ.ร.บ. วิธีพิจารณาคดีผู้บริโภค)
- debt: 3 (ป.พ.พ. ลูกหนี้-เจ้าหนี้, พ.ร.บ. ทวงถามหนี้, พ.ร.บ. ล้มละลาย)
- housing: 1 (ป.พ.พ. เช่าทรัพย์)
- family: 3 (ป.พ.พ. บรรพ 5, ป.พ.พ. บรรพ 6, พ.ร.บ. คุ้มครองผู้ถูกกระทำ)
- accident: 2 (พ.ร.บ. จราจร, ป.พ.พ. ละเมิด)
- online_fraud: 4 (มาตรา 341, พ.ร.บ. คอมพิวเตอร์, พ.ร.บ. ฟอกเงิน, พ.ร.บ. สินเชื่อ)
- crime: 5 (มาตรา 295/276/334/337, พ.ร.บ. ค่าตอบแทนผู้เสียหาย)
- government: 3 (พ.ร.บ. ศาลปกครอง, พ.ร.บ. ละเมิด จนท., พ.ร.บ. ทะเบียนราษฎร)
- insurance: 3 (พ.ร.บ. ประกันวินาศภัย, พ.ร.บ. ประกันชีวิต, พ.ร.บ. คปภ.)
- defamation: 4 (มาตรา 326/328, PDPA, พ.ร.บ. คอมฯ ม.16)
- property: 3 (ประมวลกฎหมายที่ดิน, ป.พ.พ. บรรพ 4, พ.ร.บ. อาคารชุด)

**Total: 36 legal sources** across 12 categories.

**Key Functions:**
- `sourcesForCategory(category)`: Returns relevant sources by category
- `resolveSource(id)`: Anti-hallucination — returns null for unknown IDs

**Current State:**
- ✅ Excellent: Comprehensive source registry with jurisdiction, effective date, checked date
- ✅ Auditable: `checkedDate` shows last human review
- ⚠️ URLs are placeholders (not all verified against official portals)

**Improvements Needed:**
1. Verify all URLs against official Royal Gazette / government portals
2. Add source update pipeline (automatic checking for law amendments)
3. Add English translations of law names

---

### 30. FEAR CALIBRATION — `lib/legal/fear-calibration.ts` (100 lines)

**Purpose:** Asks emotional state before diagnosis to calibrate urgency and tone.

**Key Types:** `FearLevel` (panic/urgent/concerned/planning), `Urgency`

**Fear Level → Calibration:**
| Fear Level | Tone | Message | Deadline |
|-----------|------|---------|----------|
| panic | soothe | "ใจเย็นนะ — เราพร้อมช่วย! ทำตามขั้นตอนนี้เลย" | ⚡ ทำทันที — อย่ารอ |
| urgent | reassure | "เราเข้าใจว่าคุณกังวล — เริ่มทำภายใน 3 วัน" | ⏰ ควรทำภายใน 1-3 วัน |
| concerned | guide | "เป็นห่วงเป็นเรื่องดี — เราจะพาเตรียมตัว" | 📅 ควรทำภายใน 1-2 สัปดาห์ |
| planning | inform | "วางแผนล่วงหน้าดีกว่ามาตามแก้ทีหลัง!" | 📋 เตรียมพร้อม — ไม่ต้องรีบ |

**Current State:**
- ✅ Complete: Fear calibration logic, question, and calibration function
- ⚠️ NOT WIRED: Not used in any page — exists in library but no UI integration
- This is a KEY V4 concierge gap

**Improvements Needed:**
1. Wire into diagnosis wizard as step 0 (before category-specific questions)
2. Use calibrated tone in all subsequent communication
3. Adjust action plan urgency based on fear level
4. Show appropriate messaging on loading/analysis screens

---

### 31. GUARDRAILS — `lib/legal/guardrails.ts` (444 lines)

**Purpose:** Safety rules AI must never violate — protects users, platform, and legal integrity.

**14 Guardrail Rules:**
- P0 (Must Never):
  1. `no-legal-advice` — ห้ามให้คำแนะนำทางกฎหมาย
  2. `no-outcome-prediction` — ห้ามทำนายผลคดี
  3. `no-lawyer-ranking` — ห้ามจัดอันดับทนาย
  4. `no-court-filing` — ห้ามยื่นเอกสารแทนผู้ใช้
  5. `no-fabricated-sources` — ห้ามอ้างอิงกฎหมายที่ไม่มีจริง
  6. `no-data-without-consent` — PDPA compliance
  7. `no-self-representation` — ห้ามแนะนำให้ดำเนินคดีเอง
  8. `no-statute-of-limitations` — ห้ามระบุอายุความโดยไม่อ้างอิง
  9. `no-legal-fee-quotes` — ห้ามประมาณค่าทนาย
  10. `emergency-redirect` — ตรวจพบเหตุฉุกเฉิน → redirect
- P1 (Should Fix):
  11. `disclaimer-required` — ทุกผลลัพธ์ต้องมี disclaimer
  12. `pii-redaction` — ห้ามแสดง PII
  13. `jurisdiction-scope` — ระบุว่าเป็นกฎหมายไทย
  14. `no-foreign-law-comparison` — ห้ามเปรียบเทียบกฎหมายต่างประเทศ
- P2 (Nice to Have):
  15. `language-quality` — ใช้ภาษาทางการ
  16. `outdated-law-warning` — แจ้งเมื่อกฎหมายเกิน 5 ปี

**Key Functions:**
- `checkGuardrails(text)`: First-match violation check
- `checkAllGuardrails(text)`: Returns all violations
- `getGuardrailSummary(text)`: Violations by severity
- `isSafeForDisplay(text)`: Gate for P0 violations
- `ACCURACY_CHECKS`: Thai-specific checks (BE year, formal language, required terms, placeholders, emergency keywords, legal register)

**Current State:**
- ✅ Excellent: Comprehensive guardrail system with banned patterns
- ✅ Good: Thai-specific accuracy checks (BE year validation, formal language)
- ⚠️ NOT WIRED: No evidence guardrails are called before AI responses are shown

**Improvements Needed:**
1. Wire `isSafeForDisplay()` as gate before rendering AI responses
2. Wire `checkGuardrails()` in the API layer before returning AI results
3. Add guardrail violation logging for monitoring
4. Integrate emergency redirect logic into AI assistant and search pages

---

### 32. DRIVE DETECTION — `lib/legal/drive-detection.ts` (377 lines)

**Purpose:** Maps user answers to 22 Human Drives for personalization.

**Key Types:** `DriveId` (22 drives), `DriveProfile`

**22 Human Drives:**
1-4 (มี): survival, value, recognition, status
5-7 (ได้รับ): belonging, love, fairness
8-11 (เป็น): competence, achievement, identity, novelty
12-15 (ควบคุม): power, dominance, freedom, order
16-18 (ส่งต่อ): caregiving, purpose, legacy
19-22 (หลีกหนี): avoid_shame, avoid_loss, revenge, prove_self

**Keyword-Drive Mapping:** 22 keyword entries mapping Thai phrases to drives:
- "กลัว, ไม่ปลอดภัย, อันตราย" → survival (0.9)
- "ค่าเสียหาย, ค่าชดเชย, เงินคืน" → value (0.8)
- "ไม่เป็นธรรม, ไม่ยุติธรรม, เอาเปรียบ" → fairness (0.85)
- "ถูกด่า, ถูกประจาน, หมิ่นประมาท" → status + avoid_shame (0.85)
- "ดูแล, บุตร, ลูก, พ่อแม่" → caregiving (0.75)
- "มรดก, พินัยกรรม, ทายาท" → legacy (0.7)

**Category Defaults:**
- labour: fairness, value, avoid_loss, freedom
- online_fraud: survival, avoid_shame, fairness, revenge, value
- family: love, caregiving, belonging, legacy, avoid_loss
- defamation: status, avoid_shame, revenge, fairness, identity

**Key Functions:**
- `detectDrives(answers, category)`: Main detection — keyword matching with category fallback
- `driveMessaging(drive)`: Do/don't say guidance + urgency phrases
- `driveAwareContext(profile)`: Tone instruction + loss aversion + empowerment lines

**Current State:**
- ✅ Excellent: Full 22-drive framework with Thai keyword mapping
- ⚠️ PARTIALLY WIRED: Used in category-drives.ts but not integrated into diagnosis flow or AI responses

**Improvements Needed:**
1. Wire `detectDrives()` into diagnosis wizard during answer collection
2. Pass detected drives to AI prompt for tone-adapted responses
3. Use `driveMessaging()` for CTA text personalization
4. Show drive labels in analysis result page

---

### 33. CATEGORY DRIVES — `lib/legal/category-drives.ts` (226 lines)

**Purpose:** Per-category drive profiles with emotional framing and messaging.

**Key Types:** `CategoryDriveProfile`

**All 12 Category Profiles:**
| Category | Primary Drive | Emotional Frame | Gain Message | Loss Message |
|----------|--------------|-----------------|--------------|--------------|
| labour | fairness | ถูกเอาเปรียบ | ได้รับค่าชดเชยตามกฎหมาย | เสียสิทธิภายใน 2 ปี |
| consumer | fairness | ถูกหลอก | ได้เงินคืนเต็มจำนวน | สิทธิหมดอายุ 1 ปี |
| debt | survival | กลัว — ถูกคุกคาม | หยุดทวงหนี้ผิดกฎหมาย | หนี้บานปลาย |
| housing | survival | กังวล — กลัวถูกไล่ | อยู่ต่อหรือได้มัดจำคืน | เสียค่าเสียหายเพิ่ม |
| family | caregiving | เป็นห่วงครอบครัว | จัดการมรดกถูกกฎหมาย | ทรัพย์สินตกถึงคนไม่ตั้งใจ |
| accident | survival | ตกใจ/กลัว | ได้ค่าสินไหม+ค่าเสียหาย | หลักฐานสูญหาย |
| online_fraud | survival | กลัว+โกรธ | อายัดบัญชีทันเวลา | เงินถูกย้ายทุกนาที |
| crime | survival | กลัว/ตกใจ | ได้ค่าตอบแทนผู้เสียหาย | หลักฐานสูญหาย |
| government | fairness | หงุดหงิด | ลดเวลาดำเนินการ 50% | หมดสิทธิ 1 ปี |
| insurance | survival | กังวล — จ่ายแล้วเคลมไม่ได้ | ได้เคลมตามสิทธิ | เคลมช้าเกินกำหนด |
| defamation | status | โกรธ+อับอาย | ลบเนื้อหา+เรียกค่าเสียหาย | อายุความ 3 เดือน |
| property | legacy | กังวล — กลัวเสียทรัพย์สิน | จดทะเบียนถูกต้อง | เสียสิทธิ์ครอบครอง 10 ปี |

**Key Functions:**
- `getCategoryDriveProfile(category)`: Get full profile
- `getLossAversionMessage(category)`: Urgency messaging
- `getCategoryDriveLabels(category)`: Emoji + Thai drive labels
- `getEmotionalFrame(category)`: How users feel

**Current State:**
- ✅ Fully wired: Used in `app/categories/[category]/page.tsx` for drive-aware hooks, loss messages, emotional framing
- ✅ Best integrated library in the codebase

**Improvements Needed:**
1. Use gain messages on CTAs (currently only loss messages are shown)
2. A/B test different motivation hooks per category

---

### 34. SOCIAL PROOF — `lib/legal/social-proof.ts` (285 lines)

**Purpose:** Anonymized platform trust signals for social proof.

**Key Types:** `PlatformMetrics`, `CategorySocialProof`

**Platform Metrics (mock data):**
- Users helped: 8,420
- Diagnoses: 12,350
- Action plans: 9,842
- Documents: 6,420
- Consultations: 1,280
- Verified lawyers: 48

**Per-Category Social Proof:**
- labour: 2,840 users, 82% success, trending ✅
- consumer: 1,980 users, 76% success
- debt: 1,560 users, 71% success, trending ✅
- online_fraud: 2,100 users, 65% success, trending ✅
- defamation: 760 users, 70% success, trending ✅
- etc...

**Time Signals:**
- วันนี้: 142 คนเริ่มวิเคราะห์เคส
- สัปดาห์นี้: 980 คนได้รับแผนปฏิบัติการ
- เดือนนี้: 3,250 คนใช้ LegalAI

**Current State:**
- ✅ Good: Per-category social proof with testimonials
- ⚠️ Static: All numbers are hardcoded estimates
- ⚠️ Partially wired: Used in category detail page via SocialProofInline/ SocialProofCard

**Improvements Needed:**
1. Connect to real analytics for dynamic counts
2. Add time signals to homepage
3. Show trending badges on category cards
4. Update monthly from actual Supabase data

---

### 35. DOCUMENT CATEGORIES — `lib/documents/categories.ts` (221 lines)

**Purpose:** Registry of 10 business document categories.

**10 Categories:**
1. อสังหาริมทรัพย์ (15 templates, amber)
2. สัญญาเช่า (17 templates, blue)
3. จัดตั้งธุรกิจ (14 templates, indigo)
4. สินเชื่อและการเงิน (12 templates, green)
5. ครอบครัวและส่วนบุคคล (13 templates, pink)
6. การจ้างงานและ HR (16 templates, purple)
7. พาณิชยกรรม (14 templates, teal)
8. ยานพาหนะและการขนส่ง (8 templates, red)
9. การท่องเที่ยวและบริการ (9 templates, cyan)
10. ทรัพย์สินทางปัญญา (8 templates, orange)

**Total: 126 templates** (calculated dynamically from templateCount)

**Key Functions:**
- `getDocCategoryMeta(categoryId)`: Lookup
- `suggestCategory(search)`: Keyword-based category matching (20 Thai keywords mapped)
- `categoryFilterToQuery(filter)`: Free/paid filtering

**Current State:**
- ✅ Complete: All 10 categories with metadata
- ✅ Used: In documents page, search page, document detail page
- ⚠️ Static: Category data is entirely static

**Improvements Needed:**
1. Add dynamic template counts from database
2. Add category usage analytics
3. Add "new" badge for recently added categories

---

### 36. MERGE ENGINE — `lib/documents/merge-engine.ts` (521 lines)

**Purpose:** Core document generation engine — fills templates with user data.

**Key Features:**
- Simple field replacement: `{{first_name}}` → value
- Conditional blocks: `{{#include_non_compete}}...{{/include_non_compete}}`
- Date formatting: `{{date_effective|thai_date}}` → "15 สิงหาคม 2569"
- Currency formatting: `{{amount|currency_thb}}` → "150,000 บาท"
- Thai name prefix: `{{lessor_name|thai_name}}` → "นายสมชาย ใจดี"
- ID card formatting: 1-2345-67890-12-3
- Phone formatting: 081-234-5678
- Built-in resolvers: date_thai, amount_text, lease_duration_months, next_clause
- Batch merge: Fill template for multiple records
- Template validation: Check all placeholders have definitions

**Key Types:** `MergeFieldDefinition`, `MergeData`, `MergeResult`, `DocumentTemplate`

**Current State:**
- ✅ Excellent: Feature-rich merge engine with Thai-specific formatting
- ⚠️ NOT WIRED: The `buildTemplateDoc()` function in templates.ts creates a generic template — the merge engine's full power (conditional blocks, true per-template content) is unused
- ⚠️ Missing: Real per-template markdown content (all templates use same generic structure)

**Improvements Needed:**
1. Add per-template markdown content to the template registry
2. Wire conditional blocks for complex documents
3. Add repeating sections (witnesses, properties, etc.)
4. Implement bilingual output (Thai + English)

---

### 37. TEMPLATES — `lib/documents/templates.ts` (383 lines)

**Purpose:** Template registry — 126 templates across 10 categories.

**Key Functions:**
- `getTemplatesForCategory(categoryId)`: Returns templates for a category
- `getTemplateById(templateId)`: Single template lookup
- `getCategoryIdForTemplate(templateId)`: Reverse lookup
- `buildTemplateDoc(templateName, categoryId)`: Creates generic merge template

**Template Distribution:**
- Property: 15 (6 free, 9 paid)
- Rental: 17 (12 free, 5 paid)
- Business: 14 (8 free, 6 paid)
- Loans: 12 (6 free, 6 paid)
- Family: 13 (8 free, 5 paid)
- Employment: 16 (10 free, 6 paid)
- Commercial: 14 (7 free, 7 paid)
- Vehicle: 8 (5 free, 3 paid)
- Travel: 9 (5 free, 4 paid)
- IP: 8 (3 free, 5 paid)

**Total: 126 templates** (70 free, 56 paid)

**Current State:**
- ✅ Complete: All template names and metadata registered
- ⚠️ Generic: `buildTemplateDoc()` creates identical structure for all templates — no category-specific content
- ⚠️ Missing: No real markdown template content per template ID

**Improvements Needed:**
1. Add unique markdown content per template
2. Add per-template merge field definitions
3. Add template preview content
4. Add template versioning

---

### 38. TAX CALCULATOR — `lib/tax/calculator.ts` (310 lines)

**Purpose:** Progressive Thai personal income tax calculation engine.

**Key Functions:**
- `calculateTax(profile)`: Full calculation with bracket breakdown
- `calculateTaxSummary(profile)`: Summary with derived fields (monthly tax, net income, savings by category)
- `computeProgressiveTax(income, brackets)`: Progressive bracket application
- `scenarioAnalysis(baseProfile, scenarios)`: What-if comparisons
- `findMarginalBracket(income, taxYear)`: Find highest bracket
- `estimateMonthlyWithholding(params)`: Monthly withholding estimator

**Current State:**
- ✅ Production-quality: Full progressive tax engine
- ⚠️ NOT WIRED: The tax page uses its own simplified calculation instead of this library
- ⚠️ Missing: The tax page doesn't use `TaxPayerProfile` type

**Improvements Needed:**
1. Refactor tax page to use `calculateTax()` from this library
2. Wire `scenarioAnalysis()` for what-if comparisons
3. Integrate `TaxPayerProfile` input form

---

### 39. TAX DEDUCTIONS — `lib/tax/deductions.ts` (512 lines)

**Purpose:** Pure-function deduction calculator with all Thai tax rules.

**Processing Phases:**
1. Fixed personal/family deductions (personal, spouse, children, parents, disabled)
2. Insurance with combined cap (life + health ≤ 100K)
3. Investment/retirement with combined cap (RMF+Provident+SSF+NSF ≤ 500K)
4. Real estate (mortgage, first home)
5. Special deductions (pregnancy, child education, disability)
6. Travel/temporary measures (tourism, e-receipt)
7. Donations (percentage-capped: 10% of income after fixed deductions)

**Key Functions:**
- `computeDeductions(profile)`: Full deduction calculation
- `computeSavingsByCategory(deductions, marginalRate)`: Tax saved per category
- `quickEstimateDeductions(input)`: Simplified estimation

**Current State:**
- ✅ Excellent: Comprehensive Thai tax deduction rules
- ⚠️ NOT WIRED: Tax page uses hardcoded deduction values instead

**Improvements Needed:**
1. Wire into tax page for accurate deduction calculation
2. Use `quickEstimateDeductions()` for the simple mode

---

### 40. PACKAGE DEFINITIONS — `lib/packages/definitions.ts` (172 lines)

**Purpose:** Package/tier definitions with feature gates.

**4 Tiers:**
| Tier | Price | Key Features |
|------|-------|-------------|
| ฟรี | ฿0 | 3 AI analyses, 1 document, 3 evidence, 1 consultation |
| Action Pack | ฿299 | Unlimited AI/docs, 20 evidence, 1 consultation, Tax Optimizer |
| Case Plus | ฿999 | +Priority review, 50 evidence, 3 consultations, LINE |
| SME Starter | ฿2,990/mo | +Business docs, team (5), corporate tax, unlimited consultations |

**Feature Gates:** 10 feature keys mapping to minimum tier requirements

**Current State:**
- ✅ Complete: Full package definitions with limits
- ⚠️ NOT ENFORCED: Feature gates defined but not enforced in API/pages

**Improvements Needed:**
1. Enforce feature gates at API level
2. Show upgrade prompts when users hit limits
3. Add usage tracking against limits

---

### 41. DOMAIN TYPES — `domain/types.ts` (225 lines)

**Purpose:** Framework-agnostic domain types for the entire platform.

**Key Types:**
- `LegalCategory` (12 union)
- `LegalSource`, `ActionPlanStep`, `EvidenceRequirement`
- `CaseStatus`, `CaseSummary`, `CaseTimelineEvent`
- `LawyerProfile`, `LawyerServiceScope`
- `ConsentPreference`, `DocumentStatus`, `DocumentTemplate`
- `AssistantMessage`, `Notification`
- `AnalyticsEvent` (11 union variants)

**Current State:**
- ✅ Well-structured: Clean domain model
- ✅ Analytics events: No PII, no case text, no filenames
- ⚠️ Some types unused: `DocumentStatus`, full `ConsentPreference` not fully utilized

---

## PART 3: V4 CONCIERGE INTEGRATION ANALYSIS

### What V4 Concierge Is (from context)
V4 concierge is a proactive, personalized legal assistant flow that:
1. Greets the user by name
2. Understands their emotional state (fear calibration)
3. Detects core human drives
4. Personalizes everything (tone, urgency, recommendations)
5. Proactively guides through 8 phases
6. Tracks progress and sends reminders

### Current V4 Concierge Readiness

| Component | Status | Gap |
|-----------|--------|-----|
| Fear calibration | Library exists, NOT wired to any page | Wire as diagnosis step 0 |
| Drive detection | Library exists, used only in category detail | Wire into diagnosis + AI responses |
| Category drives | Fully wired in category detail pages | Use gain messages, not just loss messages |
| Social proof | Partially wired (category pages) | Add to homepage, search, diagnosis |
| Guardrails | Library complete, NOT wired to API | Wire `isSafeForDisplay()` before rendering AI |
| Personalization | Hardcoded "คุณนภัสสร" | Use real auth user name |
| Proactive notifications | Mock data only | Real-time Supabase subscriptions |
| Progress tracking | Mock case data | Real database-backed cases |
| 8-phase flow | Not implemented | Design and implement phased case flow |

### 8-Phase Concierge Flow (Desired vs Actual)

| Phase | Description | Current State |
|-------|-------------|---------------|
| 1. Welcome | Personalized greeting + triage | Homepage has hardcoded greeting |
| 2. Listen | Fear calibration + drive detection | Fear calibration not wired |
| 3. Diagnose | Category-specific questions | ✓ Working (diagnosis wizard) |
| 4. Analyze | AI analysis with citations | ✓ Working (via /api/ai/diagnosis) |
| 5. Plan | Action plan with deadlines | ✓ Working (analysis result page) |
| 6. Act | Document generation + lawyer booking | Stubs (no real generation/booking) |
| 7. Track | Case timeline + evidence management | Mock data only |
| 8. Resolve | Case completion + feedback | Not implemented |

### Critical Missing Concierge Features

1. **Fear Calibration Entry Point** — `FEAR_CALIBRATION_QUESTION` exists but is never shown to users
2. **Drive-Personalized AI Responses** — Drive detection runs but results don't influence AI prompt tone
3. **Proactive Notifications** — No push/LINE notifications for deadlines or next steps
4. **Real Document Generation** — Merge engine is production-ready but no real templates or API endpoint
5. **Real Lawyer Booking** — Booking UI exists but no backend or calendar integration
6. **Case Persistence** — All cases are mock data; analysis results lost on browser close
7. **Progress Dashboard** — No single view showing all active cases with urgency indicators

---

## PART 4: PRIORITIZED IMPROVEMENT ROADMAP

### P0 — Critical (Must Fix for Launch)

1. **Wire fear calibration** into diagnosis wizard as step 0
2. **Persist analysis results** to Supabase (not sessionStorage)
3. **Implement real document generation** with per-template content
4. **Connect lawyer booking** to real backend
5. **Add admin/auth guard** to `/admin` page
6. **Wire guardrails** to API response pipeline
7. **Replace hardcoded "คุณนภัสสร"** with real user name
8. **Fix document "เริ่มสร้าง"** to navigate to create page

### P1 — High (Significant UX Improvement)

9. **Personalize AI tone** based on detected drives
10. **Add real-time social proof** to homepage and diagnosis
11. **Implement real notifications** via Supabase real-time
12. **Add search autocomplete** and history
13. **Connect tax page** to real calculator library
14. **Add drive-aware CTAs** (gain messages, not just loss)
15. **Implement case persistence** with real database
16. **Add emergency redirect** for crisis keywords in search/assistant

### P2 — Medium (Polish & Completeness)

17. **Add per-template markdown content** to template registry
18. **Add bilingual output** for documents
19. **Add voice input** to AI assistant
20. **Add annual/monthly pricing toggle**
21. **Add cookie consent banner**
22. **Add year-over-year tax comparison**
23. **Generate feature comparison table** from PackageLimits
24. **Add conversation persistence** to AI assistant

### P3 — Low (Future Enhancements)

25. **OCR for uploaded evidence documents**
26. **Video call integration** for lawyer consultations
27. **AI-powered evidence analysis**
28. **Multi-language support** (English UI)
29. **Enterprise/team admin dashboard**
30. **API for third-party integrations**

---

## PART 5: METRICS & SUMMARY

### Page Completeness Summary

| Page | Thai Copy | UI Complete | Working Logic | Real Data | V4 Ready |
|------|-----------|-------------|---------------|-----------|----------|
| Home | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Categories List | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Category Detail | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Diagnosis | ✅ | ✅ | ✅ | ✅(AI) | ⚠️ |
| Search | ✅ | ✅ | ⚠️ | ✅(AI) | ⚠️ |
| Documents Home | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| Doc Category | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Doc Create | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| Tax | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Pricing | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Lawyers | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Lawyer Detail | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Profile | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| Terms | ✅ | ✅ | N/A | ✅ | N/A |
| Privacy | ✅ | ✅ | N/A | ✅ | N/A |
| Notifications | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Assistant | ✅ | ✅ | ✅ | ✅(AI) | ⚠️ |
| Cases | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Timeline | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Evidence | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Admin | ✅ | ✅ | ❌ | ❌ | ❌ |
| Onboarding | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Sign In | ✅ | ✅ | ✅ | ✅ | ✅ |
| 404 | ✅ | ✅ | N/A | N/A | N/A |
| Error | ✅ | ✅ | ✅ | N/A | N/A |
| Analysis | ✅ | ✅ | ⚠️ | ✅(AI) | ⚠️ |
| Design System | ✅ | ✅ | N/A | N/A | N/A |

### Library Integration Status

| Library | Complete | Wired | Used By |
|---------|----------|-------|---------|
| diagnosis-config | ✅ | ✅ | Diagnosis wizard, Categories |
| sources | ✅ | ✅ | Category detail, Analysis |
| fear-calibration | ✅ | ❌ | NOTHING (gap) |
| guardrails | ✅ | ❌ | NOTHING (gap) |
| drive-detection | ✅ | ⚠️ | category-drives only |
| category-drives | ✅ | ✅ | Category detail |
| social-proof | ✅ | ⚠️ | Category detail (partial) |
| documents/categories | ✅ | ✅ | Documents, Search |
| merge-engine | ✅ | ❌ | NOTHING (gap) |
| templates | ⚠️ | ⚠️ | Doc category detail |
| tax/calculator | ✅ | ❌ | NOTHING (tax page uses own) |
| tax/deductions | ✅ | ❌ | NOTHING (gap) |
| packages/definitions | ✅ | ✅ | Pricing page |
| domain/types | ✅ | ✅ | Throughout |

---

## CONCLUSION

LegalAI Thailand has an impressive foundation: rich Thai-language UI across 27 pages, a comprehensive legal domain model (12 categories, 36 sources, 22 human drives, 14 guardrails, 126 templates), working AI integration (DeepSeek), and a polished design system. The platform is approximately **60% complete for a citizen MVP** — strong on information architecture and AI analysis, but weak on transactional features (document generation, lawyer booking, case persistence, real notifications).

The **critical path to V4 concierge readiness** is:
1. Wire fear calibration + drive detection into the diagnosis flow
2. Connect document generation + lawyer booking to real backends
3. Implement case persistence and real-time notifications
4. Add proactive concierge behaviors (personalized greeting, deadline tracking, progress nudges)

The libraries are well-engineered but underutilized — the merge engine, tax calculator, and guardrails are essentially complete but disconnected from the UI. Bridging this gap would unlock significant value quickly.

---

*End of Report — 3,544 lines*
*Generated: 12 August 2026*
*Next Review: After V4 concierge integration sprint*

---

## PART 6: DETAILED ALGORITHM ANALYSIS PER PAGE

### Home Page Algorithm Trace
```
1. Component mounts → formatThaiToday() runs in useEffect
2. User types in search box → setQuery(e.target.value) updates state
3. User submits form → search() called:
   a. Prevents default form submission
   b. Trims query, defaults to "นายจ้างเลิกจ้างโดยไม่แจ้งล่วงหน้า"
   c. Fires recordEvent({ type: "search_submitted" })
   d. Navigates to /search?q={encodedQuery}
4. User clicks quick search → setQuery + immediate router.push
5. Category cards → Link to /categories/{id} with onClick analytics
6. Action cards → Link to respective routes
7. CasePreviewCard → Links to /cases/case-1/timeline (hardcoded)
```

### Diagnosis Wizard Algorithm Trace (Full)
```
1. Page loads → reads ?category= from URL
2. isValidCategory check against 12 VALID_CATEGORIES
3. Falls back to "labour" if invalid/missing
4. getDiagnosisConfig(category) loads questions array
5. useEffect fires diagnosis_started analytics event
6. State machine:
   STATUS: "intake" | "loading" | "error"
   STEP: 1 to TOTAL (4-5 questions)
   ANSWERS: Record<string, string | string[]>
7. User selects option → selectAnswer(option):
   - If multi: toggle in array
   - If single: replace string
8. canProceed(): Check current question has answer
9. "ถัดไป" button → next():
   - If not last step: increment step
   - If last step: call runAnalysis()
10. runAnalysis():
    a. Set status="loading"
    b. POST /api/ai/diagnosis with {category, answers}
    c. On success: store in sessionStorage
    d. Fire diagnosis_completed event
    e. Route to /analysis/case-1?session=new
    f. On error: Set status="error" with message
11. Error state: Show retry button → setStatus("intake")
12. Loading state: Show indeterminate progress → user can click back to return to intake
```

### Search Page Algorithm Trace (Full)
```
1. Page loads → reads ?q= from URL params
2. setQuery(initial) initializes search box
3. hasQuery check: if initial.trim().length > 0
4. If hasQuery:
   a. suggestCategory(initial) → keyword matching
   b. Filter DOCUMENT_CATEGORIES by query match
   c. useEffect fires:
      - setResult({loading: true})
      - POST /api/ai/assistant with prompt
      - On response: setResult({text, loading: false})
      - On error: setResult({error: "...", loading: false})
5. Sort dropdown: Purely visual, no actual resorting
   - SORT_OPTIONS: relevant/newest/oldest — all show same result
6. Save button: Toggles local saved state, no persistence
7. Share button:
   - Try navigator.share() API
   - Fallback: navigator.clipboard.writeText()
8. Article click: Shows toast notification, no actual navigation
9. Document category sidebar:
   - Shows suggested category (if keyword match)
   - Shows matching categories (filtered by query)
   - Fallback: Shows top 5 categories
10. "ดูเอกสารทั้งหมด 126+ รายการ" → links to /documents
```

### Tax Page Algorithm Trace (Full)
```
1. Initial state: income=600000, deductions={}, compareMode=false
2. Derived values per render:
   - totalDeductions = sum(deductions) + 60000 personal
   - tax = calcTax(income, totalDeductions)
   - taxNoDeductions = calcTax(income, 60000)
   - savings = taxNoDeductions - tax
   - netIncome = max(0, income - totalDeductions)
   - effectiveRate = (tax/income * 100).toFixed(1)
   - breakdown = bracketBreakdown(income, totalDeductions)
3. calcTax algorithm:
   a. net = max(0, income - deductions)
   b. FOR each bracket in TAX_BRACKETS:
      - taxable = min(net, bracket.to) - bracket.from (if net > from)
      - tax += (taxable * bracket.rate) / 100
   c. Return Math.round(tax)
4. bracketBreakdown algorithm:
   a. net = max(0, income - deductions)
   b. FOR each bracket:
      - taxable = net > from ? min(net, to) - from : 0
      - tax = round((taxable * rate) / 100)
      - Return { ...bracket, taxable, tax }
5. User moves income slider → setIncome(Number(e.target.value))
6. User toggles deduction chip → toggleDeduction(idx):
   a. Get deduction definition from DEDUCTION_CLASSES
   b. If pct (RMF, SSF, ThaiESG, donation):
      - val = round(income * d.value)
      - If maxVal: val = min(val, d.maxVal)
   c. Else: val = d.value (fixed amount)
   d. If already active: set to 0 (toggle off)
   e. If not active: set to val (toggle on)
7. User toggles compare mode → setCompareMode(!compareMode)
8. handlePrint():
   a. Generate HTML string via taxSummaryHtml()
   b. Call printDocument(html, title) from export library
9. Checklist:
   a. Load from localStorage key "legalai_tax_checklist"
   b. toggleCheckItem(id): Toggle in checkedItems state
   c. useEffect persists to localStorage on change
   d. checkedCount / totalItems → progressPercent
   e. allDone check: If all 6 checked + not yet celebrated
      → setJustCelebrated(true) + 4s timeout
```

### Evidence Page Algorithm Trace (Full)
```
1. Initialize items from sampleEvidenceRequirements
2. Initialize empty files array
3. File validation (validateFile): Check type + size + non-empty
4. addFiles(newFiles): Validate each, push valid, notify errors
5. removeFile(id): Filter + unlink from evidence
6. linkFileToEvidence(fileId, evidenceId): Update file + mark provided
7. Drag handlers: dragEnter/Over/Leave/Drop manage visual state
8. Click/Keyboard: Open hidden file input
9. toggle evidence: Toggle provided state + fire analytics
```

### Evidence Page Algorithm — Full Detail
```
DRAG STATE MACHINE:
  idle ──dragEnter──► active
    ▲                   │
    │                   ├──dragLeave──► idle (if leaving container)
    │                   │
    └──────drop─────────┘

FILE STATE:
  files: UploadedFile[]
    │
    ├── addFiles() ──► validateFile() ──► valid → push
    │                                    └─► invalid → notify error
    │
    ├── removeFile() ──► filter out + unlink evidence
    │
    └── linkFileToEvidence() ──► set evidenceId + mark provided
```

### Admin Page Algorithm Trace (Full)
```
1. RevenueLineChart SVG rendering:
   a. Calculate chart dimensions (W=600, H=220, padding)
   b. Compute polyline points from monthlyRevenue data
   c. Y-axis: 4 grid lines with labels (฿Xk format)
   d. X-axis: Month labels (ม.ค. - ส.ค.)
   e. Area fill: Gradient polygon under the line
   f. Data dots: Circles with hover tooltip on each data point
   g. Latest month highlight: Larger dot + blue fill
   h. Hover state: Shows tooltip rect with month + value
2. Stat cards: Static display of hardcoded dashboard stats
3. Quick action buttons: All show toast "ฟีเจอร์จะพร้อมใช้งาน..."
4. Revenue stream cards: Static display with share bar visualization
5. Activity filter: activeFilter state — no actual filtering
6. Module grid: Static display of 6 admin module cards
7. System health: Static display of 99.8% uptime + deploy date
```

### Onboarding Algorithm Trace (Full)
```
1. useAuth() check:
   - loading=true → show loading spinner
   - user=null → router.replace("/auth/signin")
   - user present → proceed to onboarding flow
2. 5-step state machine:
   - Step 1 (Terms): agreeTerms + agreePrivacy checkboxes
   - Step 2 (AI): agreeAi checkbox
   - Step 3 (Notifications): notifyInApp/notifyEmail/notifyLine
   - Step 4 (Email): email verification flow
   - Step 5 (Profile): fullName + language inputs
3. Step validation (stepValid):
   - Step 1: both checkboxes checked
   - Step 2: agreeAi checked
   - Step 3: always valid
   - Step 4: emailVerified=true
   - Step 5: fullName.trim().length > 0
4. Email verification (MOCK):
   a. sendVerificationCode(): Validate email, 1200ms delay, setCodeSent
   b. verifyCode(): Accept any 6-digit code, setEmailVerified
   c. changeEmail(): Reset all email state
5. next(): Check stepValid, increment step or finish → router.replace("/")
```

### Sign In Algorithm Trace (Full)
```
1. useAuth() check: user → router.replace("/onboarding")
2. Stage "email":
   a. handleEmail(form): signInWithEmail → setStage("otp") or setError
   b. handleGoogle(): signInWithGoogle → redirect to /auth/callback
3. Stage "otp":
   a. handleOtp(form): verifyOtp → AuthProvider updates → redirect /onboarding
   b. "แก้ไขอีเมล" button: setStage("email"), clear OTP
4. Error display: From Supabase auth errors
```

### AI Assistant Algorithm Trace (Full)
```
1. Initialize with WELCOME message in messages state
2. User types in textarea → setChatText(e.target.value)
3. Send flow:
   a. send(textToSend?):
      - Get userText from param or chatText state
      - Guard: no empty text, no loading
      - Create userMessage with unique ID
      - Snapshot history from messagesHistoryRef
      - Add userMessage to messages state
      - Clear chatText, set loading=true
      - POST /api/ai/assistant with {message, history, category, caseTitle}
      - On response: parse reply.text + reply.citations
      - Add assistant message to state
      - On error: Add error message
      - Finally: setLoading(false), focus textarea
4. Quick replies (first message only):
   - Click fills chatText with reply text
5. Suggestion buttons:
   - Click calls send(s.value) directly
6. Enter key: Sends (shift+Enter for newline)
7. Auto-scroll: useEffect scrolls messagesRef to bottom
8. Citations: SourceCitation component renders LegalSource data
```

---

## PART 7: CROSS-PAGE CONSISTENCY AUDIT

### Terminology Consistency Matrix
| Term | Used Consistently? | Locations | Notes |
|------|-------------------|-----------|-------|
| "เคส" vs "คดี" | ✅ "เคส" | Throughout | Informal but consistent |
| "วิเคราะห์" | ✅ | Diagnosis, search, analysis | Consistent verb |
| "AI" vs "ปัญญาประดิษฐ์" | ✅ "AI" | All pages | User-friendly choice |
| "ทนาย" vs "ทนายความ" | ⚠️ Mixed | Cards vs formal contexts | Minor inconsistency |
| "เอกสาร" vs "แบบฟอร์ม" | ⚠️ Mixed | Main docs vs category browser | Different contexts |
| "หลักฐาน" | ✅ | Evidence, analysis pages | Consistent |
| "ค่าชดเชย" vs "ค่าสินไหม" | ⚠️ Context | Labour vs insurance | Domain-appropriate |
| "สิทธิ" | ✅ | Analysis, category detail | Consistent legal term |
| "ขั้นตอน" | ✅ | Timeline, search, analysis | Consistent |
| "กำหนดการ" | ✅ | Tax, notifications | Consistent |

### Tone Consistency Per Context
| Context | Tone | Examples |
|---------|------|----------|
| Homepage greeting | Warm, inviting | "สวัสดีค่ะ...", "วันนี้มีเรื่องอะไรให้ช่วย?" |
| Category detail | Empowering, urgent | "คุณทำงานหนักมา — ถึงเวลาเรียกร้องสิทธิ" |
| Diagnosis wizard | Neutral, supportive | "ตอบเท่าที่ทราบ • กลับมาแก้ได้" |
| Loading states | Reassuring | "AI กำลังวิเคราะห์เคสของคุณ... ปกติ 30-90 วินาที" |
| Error states | Apologetic, helpful | "ขออภัย เกิดปัญหาขณะแสดงหน้านี้" |
| Legal pages | Formal, precise | "ข้อกำหนดการใช้บริการ (Terms of Service)" |
| AI assistant | Friendly, helpful | "สวัสดีค่ะ ฉันคือ AI Legal Assistant" |
| Tax page | Professional, optimistic | "✅ คุณประหยัดภาษีได้ ฿XX,XXX" |

### Icon & Emoji Usage Inventory
| Icon/Emoji | Meaning | Pages Used | Consistent? |
|-----------|---------|-----------|-------------|
| ✦ | AI / Sparkle | Home, diagnosis, assistant, onboarding, signin | ✅ |
| ⌕ | Search | Home, search, 404 | ✅ |
| 🛡️ | Security | Home, evidence, trust-strip | ✅ |
| 📄 | Document | Documents, search sidebar | ✅ |
| 👨‍⚖️ | Lawyer | Lawyers, category detail | ✅ |
| ⚖️ | Justice/Law | Category pages, lawyer detail | ✅ |
| 💰 | Money/Tax | Tax page, pricing | ✅ |
| ⚡ | Urgent action | Category problem examples | ✅ |
| ⏰ | Time-sensitive | Category problem examples | ✅ |
| 📅 | Scheduled/Long term | Category problem examples, tax | ✅ |
| ✓ | Verified/Done | Lawyer cards, evidence checklist | ✅ |
| ✎ | Edit | Profile avatar | ✅ |
| ♡ | Save/Favorite | Search, lawyer cards | ✅ |
| ↗ | Share | Search | ✅ |

### Button/CTA Style Consistency
| Pattern | Format | Used Where | Consistent? |
|---------|--------|-----------|-------------|
| Primary CTA | `className="primary"` + "→" suffix | Main CTAs | ✅ |
| Ghost/Back | `className="ghost"` + "←" prefix | Back navigation | ✅ |
| Outline | `className="outline"` | Secondary actions | ✅ |
| Full width | `className="primary full"` | Sidebar CTAs | ✅ |
| "เริ่ม..." prefix | Entry points | "เริ่มวิเคราะห์", "เริ่มสร้าง", "เริ่มนัดหมาย" | ✅ |
| "กลับ..." prefix | Back nav | "กลับหน้าหลัก", "กลับไปเลือกหมวดหมู่" | ✅ |
| "ดู..." prefix | Browse | "ดูทั้งหมด", "ดูแพ็กเกจ", "ดูโปรไฟล์" | ✅ |

### Privacy/Disclaimer Pattern Inventory
| Pattern | Prefix | Location | Count |
|---------|--------|----------|-------|
| Privacy note | "⌾ " | Diagnosis, categories, onboarding | 4 |
| Info disclaimer | "ⓘ " | Search, analysis, tax | 3 |
| Warning | "⚠️ " | Terms, guardrails, category detail | 3 |
| Emergency | "🚨 " | Guardrails (emergency-redirect) | 1 |
| Example data | PrototypeDataNotice | 15+ pages | 15+ |
| Legal disclaimer | LegalDisclaimer | Analysis page | 1 |
| Consequence notice | GentleConsequenceNotice | Timeline, analysis | 2 |

---

## PART 8: ACCESSIBILITY AUDIT

### Current Accessibility Features
- ✅ Semantic HTML: header, nav, section, article, aside, main
- ✅ ARIA labels: aria-label on interactive elements (buttons, inputs, links)
- ✅ ARIA live regions: aria-live="polite" on loading/error states
- ✅ Keyboard navigation: Tab order follows visual order
- ✅ Focus indicators: CSS :focus-visible styles
- ✅ Role attributes: role="search", role="radiogroup", role="group"
- ✅ Form labels: htmlFor connections, aria-labelledby
- ✅ ARIA states: aria-pressed, aria-current="page", aria-invalid
- ✅ Reduced motion: Mentioned in design system handoff docs
- ✅ Touch targets: Design system specifies ≥44px

### Accessibility Gaps
- ❌ No skip-to-main-content link
- ❌ No high-contrast theme/mode
- ⚠️ Color-dependent info: Urgency pills use color without text fallback
- ⚠️ Emoji-only icons: Some decorative emojis lack aria-hidden
- ⚠️ Dynamic content: Not all state changes announced via aria-live
- ❌ No focus trap in modals (no modals implemented yet)
- ⚠️ Form validation errors: Shown visually but not linked via aria-describedby
- ⚠️ Progress indicators: Progress bar lacks aria-valuenow/aria-valuemin/aria-valuemax

---

## PART 9: PERFORMANCE ANALYSIS

### Current State
- ✅ Server components: terms, privacy, design-system (zero client JS)
- ✅ useMemo for expensive computations (tax bracket breakdown, lawyer finding)
- ✅ useCallback for stable callbacks (evidence validation)
- ⚠️ No lazy loading beyond Next.js defaults
- ⚠️ No image optimization needed (few images used)
- ⚠️ Large inline data: PROBLEM_EXAMPLES (90 lines), lawyer data (100 lines)
- ⚠️ Only one Suspense boundary (document create page)

### Performance Recommendations
1. Extract PROBLEM_EXAMPLES to lib/legal/problem-examples.ts
2. Extract lawyer mock data to lib/mock/lawyers.ts
3. Add Suspense boundaries on search, diagnosis, and cases pages
4. Implement React.lazy for admin chart component
5. Add loading skeletons for initial page loads (not just spinners)
6. Implement search input debouncing (300ms)
7. Add pagination for lawyer listing (scales beyond 5 mock entries)

---

## PART 10: SECURITY POSTURE

### Current Security Features
- ✅ Supabase Auth: Email OTP + Google OAuth
- ✅ Admin warning: "การเข้าถึงจริงต้องมีบทบาท admin และ MFA"
- ✅ Error boundaries: Never expose stack traces to users
- ✅ PII redaction rules: Defined in guardrails (banned patterns)
- ✅ Privacy-safe analytics: No PII, case text, or filenames in events

### Security Gaps
- ❌ Admin page: No real auth guard (publicly accessible with just a warning)
- ❌ Feature gates: Defined but not enforced at API level
- ❌ Rate limiting: Not visible on any API route
- ⚠️ sessionStorage: Analysis results accessible to browser extensions
- ❌ CSP headers: No Content-Security-Policy visible
- ❌ CSRF: No CSRF tokens on API routes
- ❌ Input sanitization: No visible sanitization before AI prompts

### Security Recommendations
1. Add middleware-based admin auth guard
2. Enforce feature gates with server-side checks
3. Add rate limiting to /api/ai/* endpoints
4. Move analysis results to server-side storage (not sessionStorage)
5. Add Content-Security-Policy headers
6. Add input sanitization before AI prompts
7. Add CSRF protection for mutation endpoints

---

## PART 11: DATA ARCHITECTURE

### Current Data Flow
```
                    ┌─────────────┐
                    │  DeepSeek AI │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
    /api/ai/assistant  /api/ai/diagnosis
              │            │
              ▼            ▼
         Search Page   Diagnosis Wizard
              │            │
              │            ▼
              │     sessionStorage
              │            │
              │            ▼
              │     Analysis Page
              │
              ▼
         No persistence

    ┌─────────────┐
    │ Supabase Auth│──► Sign In ──► Onboarding (mock)
    └─────────────┘

    ┌──────────────────────┐
    │ Client-side only:     │
    │  - Tax calculator     │
    │  - Document editor    │
    │  - Evidence upload    │
    │  - Lawyer booking     │
    │  - Case management    │
    └──────────────────────┘
```

### Desired Data Architecture (V4)
```
                    ┌──────────────┐
                    │  DeepSeek AI  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              │            │                │
    /api/ai/assistant  /api/ai/diagnosis  /api/tax/optimize
              │            │                │
              └────────────┼────────────────┘
                           │
                    ┌──────▼──────┐
                    │  Guardrails  │──► Filter + Validate
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Supabase    │──► Persist results
                    └──────┬──────┘
                           │
              ┌────────────┼──────────────┐
              │            │              │
         Cases Table   Documents Table   User Profile
              │            │              │
              ▼            ▼              ▼
         Case Pages   Document Pages   Settings

    ┌──────────────────────┐
    │ Real-time:            │
    │  Supabase Realtime ──► Notifications
    │  Supabase Storage  ──► Evidence files
    │  Calendar API      ──► Lawyer booking
    │  Payment Gateway   ──► Package upgrades
    └──────────────────────┘
```

---

## PART 12: EXECUTABLE IMPROVEMENT SPECS

### Home Page Specific Changes
```
FILE: app/page.tsx
1. Replace hardcoded "คุณนภัสสร" with user.displayName from auth
2. Add <LiveSocialProof /> component below hero card
3. Add <FearCheckinButton /> entry point
4. Add concierge CTA: "ไม่แน่ใจ? ให้ AI ช่วยแนะนำ →"
5. Quick searches: Pull from trending data (social-proof time signals)
```

### Diagnosis Wizard Specific Changes
```
FILE: app/diagnosis/page.tsx
1. Add fear calibration as step 0 (before category questions)
2. Wire detectDrives() during answer collection
3. Pass driveProfile.tone to question framing
4. Add answer persistence to localStorage
5. Show "กำลังเตรียมคำถามถัดไป..." transition
6. Add skip button for optional questions
7. Category label in header instead of just Brand logo
```

### Search Page Specific Changes
```
FILE: app/search/page.tsx
1. Replace STATIC_STEPS with AI-generated steps from API response
2. Add search history with localStorage persistence
3. Add autocomplete/suggestions dropdown
4. Wire sort functionality to re-query API
5. Wire article links to real content pages
6. Add "ถามต่อ" follow-up input on answer card
7. Show drive-detected tone in AI response header
```

### Tax Page Specific Changes
```
FILE: app/tax/page.tsx
1. Refactor to use calculateTax() from lib/tax/calculator
2. Use TaxPayerProfile type for structured input
3. Wire AI Tax Optimizer to real API
4. Add year-over-year comparison (2568 vs 2569)
5. Add what-if scenarios
6. Integrate quickEstimateDeductions() for simple mode
```

### Evidence Page Specific Changes
```
FILE: app/cases/[caseId]/evidence/page.tsx
1. Wire real file upload to Supabase Storage
2. Add file preview (image thumbnails, PDF viewer)
3. Add AI-powered document analysis
4. Add OCR for auto-filling case data
5. Persist uploaded files across sessions
```

---

## PART 13: TEST COVERAGE RECOMMENDATIONS

### Priority Test Cases
| # | Function | Test Type | Priority |
|---|----------|-----------|----------|
| 1 | calcTax() | Unit — 8 bracket correctness | P0 |
| 2 | computeDeductions() | Unit — cap enforcement | P0 |
| 3 | checkGuardrails() | Unit — all 14 rules | P0 |
| 4 | detectDrives() | Unit — keyword accuracy | P1 |
| 5 | mergeTemplate() | Unit — field replacement | P1 |
| 6 | formatThaiDate() | Unit — Buddhist calendar | P1 |
| 7 | suggestCategory() | Unit — keyword mapping | P2 |
| 8 | Diagnosis wizard | Integration — full flow | P1 |
| 9 | Search page | Integration — AI response | P1 |
| 10 | Tax page | Integration — calculation | P1 |
| 11 | All 27 pages | Smoke — render without crash | P0 |

---

## APPENDIX A: Complete Thai CTA Inventory

### Entry Point CTAs
1. "เริ่มวิเคราะห์ฟรี →"
2. "เลือกเอกสาร →"
3. "ค้นหาทนาย →"
4. "ลองคำนวณ →"
5. "ดูแพ็กเกจ →"
6. "ดูทั้งหมด →"
7. "ดูเคสทั้งหมด →"
8. "เริ่มวิเคราะห์ →"
9. "🤖 เริ่มวิเคราะห์เคสของฉัน"
10. "เริ่มสร้างเอกสาร →"
11. "ดูแบบฟอร์มทั้งหมด 126 รายการ →"
12. "เริ่มสร้าง →"
13. "+ สร้างเคสใหม่"
14. "+ เริ่มเคสใหม่"
15. "เริ่มนัดหมาย"

### Purchase CTAs
16. "อัปเกรดเลย"
17. "เลือกแพ็กเกจ"
18. "เริ่มใช้งานฟรี"
19. "อัปเกรดแพ็กเกจ"

### Navigation CTAs
20. "ดูโปรไฟล์และนัดหมาย"
21. "นัดหมายปรึกษา"
22. "ถาม AI →"
23. "♙ ปรึกษาทนายเกี่ยวกับเคสนี้"
24. "สร้างเคสและเริ่มดำเนินการ"
25. "กลับหน้าหลัก"
26. "← กลับไปเลือกหมวดหมู่อื่น"
27. "‹ กลับหน้าหลัก"

### Action CTAs
28. "ส่งรหัสยืนยัน"
29. "ดำเนินต่อด้วย Google"
30. "ยืนยันและเข้าสู่ระบบ"
31. "🤖 ให้ AI วิเคราะห์แผนลดหย่อน"
32. "🖨️ พิมพ์ / PDF"
33. "🔄 เปรียบเทียบแบบมี/ไม่มีลดหย่อน"
34. "ให้ AI ช่วยเลือก"

---

## APPENDIX B: All Privacy & Security Messages

1. "ข้อมูลของคุณได้รับการปกป้อง" (homepage trust strip)
2. "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
3. "⌾ คำตอบของคุณใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น — เราไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
4. "⌾ คำตอบของคุณถูกส่งเพื่อวิเคราะห์เท่านั้น และไม่ถูกเก็บไว้ที่อื่น"
5. "⌾ คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น คุณลบหรือแก้ไขได้เสมอ"
6. "ไฟล์ของคุณปลอดภัย — เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยให้บุคคลภายนอก"
7. "⌾ ข้อมูลของคุณได้รับการเก็บรักษาอย่างปลอดภัย"
8. "ⓘ ข้อมูลนี้เป็นคำแนะนำเบื้องต้น ผลลัพธ์จริงขึ้นอยู่กับรายละเอียดของแต่ละกรณี"
9. "AI อาจให้ข้อมูลคลาดเคลื่อน โปรดตรวจสอบข้อมูลสำคัญกับผู้เชี่ยวชาญ"
10. "ผลค้นหาเป็นข้อมูลกฎหมายเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย"
11. "⚠️ ข้อมูลนี้เป็นข้อมูลกฎหมายทั่วไป (legal information) ไม่ใช่คำแนะนำทางกฎหมาย (legal advice)"
12. "AI อาจมีข้อผิดพลาด — ควรตรวจสอบกับทนายหรือผู้เชี่ยวชาญก่อนดำเนินการ"
13. "เราไม่รับประกันผลลัพธ์ — แต่ละคดีมีปัจจัยเฉพาะ"
14. "ข้อมูลนี้เป็นประมาณการเบื้องต้น — ควรตรวจสอบกับผู้เชี่ยวชาญด้านภาษีก่อนยื่นแบบ"
15. "เอกสารที่สร้างเป็นแบบร่าง ควรตรวจสอบโดยผู้เชี่ยวชาญก่อนใช้งาน"
16. "ข้อมูลทนายเป็นข้อมูลตัวอย่าง ควรตรวจสอบใบอนุญาตอิสระ"
17. "⌾ เราไม่สามารถทำนายผลคดีได้ — แต่ละคดีมีปัจจัยเฉพาะ"
18. "🚨 หากคุณกำลังอยู่ในสถานการณ์ฉุกเฉิน — กรุณาติดต่อ 191 (ตำรวจ) หรือ 1300 ทันที"

---

## APPENDIX C: File Size Summary

| File | Lines | Size |
|------|-------|------|
| admin/page.tsx | 713 | 23.7 KB |
| onboarding/page.tsx | 563 | 23.2 KB |
| lawyers/[id]/page.tsx | 565 | 23.5 KB |
| cases/[caseId]/evidence/page.tsx | 542 | 20.0 KB |
| tax/page.tsx | 516 | 25.4 KB |
| lib/tax/deductions.ts | 512 | 18.7 KB |
| lib/documents/merge-engine.ts | 521 | 18.7 KB |
| lib/legal/diagnosis-config.ts | 462 | 24.6 KB |
| lib/legal/guardrails.ts | 444 | 23.7 KB |
| lib/documents/templates.ts | 383 | 22.4 KB |
| lib/legal/drive-detection.ts | 377 | 27.8 KB |
| app/diagnosis/page.tsx | 334 | 11.0 KB |
| app/documents/[category]/page.tsx | 317 | 10.4 KB |
| app/lawyers/page.tsx | 315 | 11.8 KB |
| lib/tax/calculator.ts | 310 | 9.1 KB |
| app/search/page.tsx | 288 | 13.9 KB |
| lib/legal/social-proof.ts | 285 | 11.6 KB |
| lib/legal/sources.ts | 284 | 15.6 KB |
| app/analysis/[caseId]/page.tsx | 277 | 11.8 KB |
| app/assistant/page.tsx | 268 | 9.6 KB |
| app/categories/[category]/page.tsx | 258 | 21.5 KB |
| app/documents/page.tsx | 257 | 9.7 KB |
| app/documents/create/page.tsx | 232 | 7.6 KB |
| lib/legal/category-drives.ts | 226 | 16.1 KB |
| domain/types.ts | 225 | 6.8 KB |
| lib/documents/categories.ts | 221 | 8.2 KB |
| app/page.tsx | 217 | 9.3 KB |
| app/auth/signin/page.tsx | 212 | 7.7 KB |
| app/profile/page.tsx | 196 | 12.1 KB |
| lib/packages/definitions.ts | 172 | 5.2 KB |
| app/cases/[caseId]/timeline/page.tsx | 168 | 6.8 KB |
| app/cases/page.tsx | 154 | 5.1 KB |
| app/design-system/page.tsx | 139 | 5.3 KB |
| app/notifications/page.tsx | 129 | 4.4 KB |
| lib/legal/fear-calibration.ts | 100 | 4.4 KB |
| app/pricing/page.tsx | 97 | 5.5 KB |
| app/terms/page.tsx | 97 | 6.2 KB |
| app/privacy/page.tsx | 94 | 6.8 KB |
| app/categories/page.tsx | 61 | 2.9 KB |
| app/error.tsx | 51 | 1.8 KB |
| app/not-found.tsx | 20 | 0.9 KB |
| **TOTAL** | **~12,700** | **~520 KB** |

---

## APPENDIX D: Component Hierarchy Map

```
AppShell (layout.tsx)
├── Header / Brand
├── Navigation
│   ├── Home (/)
│   ├── Categories (/categories)
│   │   └── Category Detail (/categories/[category])
│   ├── Diagnosis (/diagnosis)
│   ├── Search (/search)
│   ├── Documents (/documents)
│   │   ├── Category Detail (/documents/[category])
│   │   └── Create (/documents/create)
│   ├── Tax (/tax)
│   ├── Pricing (/pricing)
│   ├── Lawyers (/lawyers)
│   │   └── Lawyer Detail (/lawyers/[id])
│   ├── Cases (/cases)
│   │   ├── Timeline (/cases/[caseId]/timeline)
│   │   └── Evidence (/cases/[caseId]/evidence)
│   ├── Assistant (/assistant)
│   ├── Notifications (/notifications)
│   ├── Profile (/profile)
│   ├── Admin (/admin)
│   └── Analysis (/analysis/[caseId])
├── Auth
│   ├── Sign In (/auth/signin)
│   ├── Callback (/auth/callback)
│   └── Onboarding (/onboarding)
├── Legal
│   ├── Terms (/terms)
│   └── Privacy (/privacy)
├── Error (/error)
├── 404 (/not-found)
└── Dev
    └── Design System (/design-system)
```

---

## APPENDIX E: API Endpoint Inventory

| Endpoint | Method | Purpose | Status |
|----------|--------|---------|--------|
| /api/ai/assistant | POST | AI chat assistant | ✅ Working |
| /api/ai/diagnosis | POST | AI case diagnosis | ✅ Working |
| /api/documents/generate | POST | Document generation | ❌ Not implemented |
| /api/tax/optimize | POST | Tax optimization | ❌ Not implemented |
| /api/lawyers/book | POST | Lawyer booking | ❌ Not implemented |
| /api/cases/* | CRUD | Case management | ❌ Not implemented |
| /api/evidence/upload | POST | Evidence upload | ❌ Not implemented |
| /api/notifications | GET | Notification list | ❌ Not implemented |
| /api/profile | GET/PUT | User profile | ❌ Not implemented |
| /api/admin/* | Various | Admin operations | ❌ Not implemented |

---

## APPENDIX F: Complete V4 Concierge Gap Analysis

| Concierge Feature | Current State | Library Ready | UI Ready | Priority |
|-------------------|---------------|---------------|----------|----------|
| Personalized greeting | Hardcoded name | ❌ (no user context) | ⚠️ (UI exists) | P0 |
| Fear calibration | Not wired | ✅ | ❌ | P0 |
| Drive detection in AI | Not in prompts | ✅ | ❌ | P0 |
| Drive-aware category hooks | ✅ (cat detail) | ✅ | ✅ | Done |
| Social proof display | ⚠️ (partial) | ✅ | ⚠️ | P1 |
| Guardrail enforcement | Not wired | ✅ | ❌ | P0 |
| Proactive notifications | Mock only | ❌ | ⚠️ | P1 |
| Deadline tracking | Mock only | ❌ | ⚠️ | P1 |
| Progress dashboard | Mock cases | ❌ | ⚠️ | P1 |
| Case persistence | Not implemented | ❌ | ⚠️ | P0 |
| Document generation | Stub only | ✅ | ⚠️ | P0 |
| Lawyer booking | UI only | ❌ | ✅ | P0 |
| 8-phase flow | Not designed | ❌ | ❌ | P2 |
| Emergency redirect | Guardrail only | ✅ | ❌ | P1 |
| Voice input | Not implemented | ❌ | ❌ | P3 |

---

*End of Report — Expanded Appendices*
*Total: 3,150+ lines*
*Generated: 12 August 2026*

---

## PART 6: DETAILED ALGORITHM ANALYSIS PER PAGE

### Home Page Algorithm Trace
```
1. Component mounts → formatThaiToday() runs in useEffect
2. User types in search box → setQuery(e.target.value) updates state
3. User submits form → search() called:
   a. Prevents default form submission
   b. Trims query, defaults to "นายจ้างเลิกจ้างโดยไม่แจ้งล่วงหน้า"
   c. Fires recordEvent({ type: "search_submitted" })
   d. Navigates to /search?q={encodedQuery}
4. User clicks quick search → setQuery + immediate router.push
5. Category cards → Link to /categories/{id} with onClick analytics
6. Action cards → Link to respective routes
7. CasePreviewCard → Links to /cases/case-1/timeline (hardcoded)
```

### Diagnosis Wizard Algorithm Trace (Full)
```
1. Page loads → reads ?category= from URL
2. isValidCategory check against 12 VALID_CATEGORIES
3. Falls back to "labour" if invalid/missing
4. getDiagnosisConfig(category) loads questions array
5. useEffect fires diagnosis_started analytics event
6. State machine:
   STATUS: "intake" | "loading" | "error"
   STEP: 1 to TOTAL (4-5 questions)
   ANSWERS: Record<string, string | string[]>
7. User selects option → selectAnswer(option):
   - If multi: toggle in array
   - If single: replace string
8. canProceed(): Check current question has answer
9. "ถัดไป" button → next():
   - If not last step: increment step
   - If last step: call runAnalysis()
10. runAnalysis():
    a. Set status="loading"
    b. POST /api/ai/diagnosis with {category, answers}
    c. On success: store in sessionStorage
    d. Fire diagnosis_completed event
    e. Route to /analysis/case-1?session=new
    f. On error: Set status="error" with message
11. Error state: Show retry button → setStatus("intake")
12. Loading state: Show indeterminate progress → user can click back to return to intake
```

### Search Page Algorithm Trace (Full)
```
1. Page loads → reads ?q= from URL params
2. setQuery(initial) initializes search box
3. hasQuery check: if initial.trim().length > 0
4. If hasQuery:
   a. suggestCategory(initial) → keyword matching
   b. Filter DOCUMENT_CATEGORIES by query match
   c. useEffect fires:
      - setResult({loading: true})
      - POST /api/ai/assistant with prompt
      - On response: setResult({text, loading: false})
      - On error: setResult({error: "...", loading: false})
5. Sort dropdown: Purely visual, no actual resorting
   - SORT_OPTIONS: relevant/newest/oldest — all show same result
6. Save button: Toggles local saved state, no persistence
7. Share button:
   - Try navigator.share() API
   - Fallback: navigator.clipboard.writeText()
8. Article click: Shows toast notification, no actual navigation
9. Document category sidebar:
   - Shows suggested category (if keyword match)
   - Shows matching categories (filtered by query)
   - Fallback: Shows top 5 categories
10. "ดูเอกสารทั้งหมด 126+ รายการ" → links to /documents
```

### Tax Page Algorithm Trace (Full)
```
1. Initial state: income=600000, deductions={}, compareMode=false
2. Derived values per render:
   - totalDeductions = sum(deductions) + 60000 personal
   - tax = calcTax(income, totalDeductions)
   - taxNoDeductions = calcTax(income, 60000)
   - savings = taxNoDeductions - tax
   - netIncome = max(0, income - totalDeductions)
   - effectiveRate = (tax/income * 100).toFixed(1)
   - breakdown = bracketBreakdown(income, totalDeductions)
3. calcTax algorithm:
   a. net = max(0, income - deductions)
   b. FOR each bracket in TAX_BRACKETS:
      - taxable = min(net, bracket.to) - bracket.from (if net > from)
      - tax += (taxable * bracket.rate) / 100
   c. Return Math.round(tax)
4. bracketBreakdown algorithm:
   a. net = max(0, income - deductions)
   b. FOR each bracket:
      - taxable = net > from ? min(net, to) - from : 0
      - tax = round((taxable * rate) / 100)
      - Return { ...bracket, taxable, tax }
5. User moves income slider → setIncome(Number(e.target.value))
6. User toggles deduction chip → toggleDeduction(idx):
   a. Get deduction definition from DEDUCTION_CLASSES
   b. If pct (RMF, SSF, ThaiESG, donation):
      - val = round(income * d.value)
      - If maxVal: val = min(val, d.maxVal)
   c. Else: val = d.value (fixed amount)
   d. If already active: set to 0 (toggle off)
   e. If not active: set to val (toggle on)
7. User toggles compare mode → setCompareMode(!compareMode)
8. handlePrint():
   a. Generate HTML string via taxSummaryHtml()
   b. Call printDocument(html, title) from export library
9. Checklist:
   a. Load from localStorage key "legalai_tax_checklist"
   b. toggleCheckItem(id): Toggle in checkedItems state
   c. useEffect persists to localStorage on change
   d. checkedCount / totalItems → progressPercent
   e. allDone check: If all 6 checked + not yet celebrated
      → setJustCelebrated(true) + 4s timeout
```

### Evidence Page Algorithm Trace (Full)
```
1. Initialize items from sampleEvidenceRequirements
2. Initialize empty files array
3. File validation (validateFile): Check type + size + non-empty
4. addFiles(newFiles): Validate each, push valid, notify errors
5. removeFile(id): Filter + unlink from evidence
6. linkFileToEvidence(fileId, evidenceId): Update file + mark provided
7. Drag handlers: dragEnter/Over/Leave/Drop manage visual state
8. Click/Keyboard: Open hidden file input
9. toggle evidence: Toggle provided state + fire analytics
```

### Evidence Page Algorithm — Full Detail
```
DRAG STATE MACHINE:
  idle ──dragEnter──► active
    ▲                   │
    │                   ├──dragLeave──► idle (if leaving container)
    │                   │
    └──────drop─────────┘

FILE STATE:
  files: UploadedFile[]
    │
    ├── addFiles() ──► validateFile() ──► valid → push
    │                                    └─► invalid → notify error
    │
    ├── removeFile() ──► filter out + unlink evidence
    │
    └── linkFileToEvidence() ──► set evidenceId + mark provided
```

### Admin Page Algorithm Trace (Full)
```
1. RevenueLineChart SVG rendering:
   a. Calculate chart dimensions (W=600, H=220, padding)
   b. Compute polyline points from monthlyRevenue data
   c. Y-axis: 4 grid lines with labels (฿Xk format)
   d. X-axis: Month labels (ม.ค. - ส.ค.)
   e. Area fill: Gradient polygon under the line
   f. Data dots: Circles with hover tooltip on each data point
   g. Latest month highlight: Larger dot + blue fill
   h. Hover state: Shows tooltip rect with month + value
2. Stat cards: Static display of hardcoded dashboard stats
3. Quick action buttons: All show toast "ฟีเจอร์จะพร้อมใช้งาน..."
4. Revenue stream cards: Static display with share bar visualization
5. Activity filter: activeFilter state — no actual filtering
6. Module grid: Static display of 6 admin module cards
7. System health: Static display of 99.8% uptime + deploy date
```

### Onboarding Algorithm Trace (Full)
```
1. useAuth() check:
   - loading=true → show loading spinner
   - user=null → router.replace("/auth/signin")
   - user present → proceed to onboarding flow
2. 5-step state machine:
   - Step 1 (Terms): agreeTerms + agreePrivacy checkboxes
   - Step 2 (AI): agreeAi checkbox
   - Step 3 (Notifications): notifyInApp/notifyEmail/notifyLine
   - Step 4 (Email): email verification flow
   - Step 5 (Profile): fullName + language inputs
3. Step validation (stepValid):
   - Step 1: both checkboxes checked
   - Step 2: agreeAi checked
   - Step 3: always valid
   - Step 4: emailVerified=true
   - Step 5: fullName.trim().length > 0
4. Email verification (MOCK):
   a. sendVerificationCode(): Validate email, 1200ms delay, setCodeSent
   b. verifyCode(): Accept any 6-digit code, setEmailVerified
   c. changeEmail(): Reset all email state
5. next(): Check stepValid, increment step or finish → router.replace("/")
```

### Sign In Algorithm Trace (Full)
```
1. useAuth() check: user → router.replace("/onboarding")
2. Stage "email":
   a. handleEmail(form): signInWithEmail → setStage("otp") or setError
   b. handleGoogle(): signInWithGoogle → redirect to /auth/callback
3. Stage "otp":
   a. handleOtp(form): verifyOtp → AuthProvider updates → redirect /onboarding
   b. "แก้ไขอีเมล" button: setStage("email"), clear OTP
4. Error display: From Supabase auth errors
```

### AI Assistant Algorithm Trace (Full)
```
1. Initialize with WELCOME message in messages state
2. User types in textarea → setChatText(e.target.value)
3. Send flow:
   a. send(textToSend?):
      - Get userText from param or chatText state
      - Guard: no empty text, no loading
      - Create userMessage with unique ID
      - Snapshot history from messagesHistoryRef
      - Add userMessage to messages state
      - Clear chatText, set loading=true
      - POST /api/ai/assistant with {message, history, category, caseTitle}
      - On response: parse reply.text + reply.citations
      - Add assistant message to state
      - On error: Add error message
      - Finally: setLoading(false), focus textarea
4. Quick replies (first message only):
   - Click fills chatText with reply text
5. Suggestion buttons:
   - Click calls send(s.value) directly
6. Enter key: Sends (shift+Enter for newline)
7. Auto-scroll: useEffect scrolls messagesRef to bottom
8. Citations: SourceCitation component renders LegalSource data
```

---

## PART 7: CROSS-PAGE CONSISTENCY AUDIT

### Terminology Consistency Matrix
| Term | Used Consistently? | Locations | Notes |
|------|-------------------|-----------|-------|
| "เคส" vs "คดี" | ✅ "เคส" | Throughout | Informal but consistent |
| "วิเคราะห์" | ✅ | Diagnosis, search, analysis | Consistent verb |
| "AI" vs "ปัญญาประดิษฐ์" | ✅ "AI" | All pages | User-friendly choice |
| "ทนาย" vs "ทนายความ" | ⚠️ Mixed | Cards vs formal contexts | Minor inconsistency |
| "เอกสาร" vs "แบบฟอร์ม" | ⚠️ Mixed | Main docs vs category browser | Different contexts |
| "หลักฐาน" | ✅ | Evidence, analysis pages | Consistent |
| "ค่าชดเชย" vs "ค่าสินไหม" | ⚠️ Context | Labour vs insurance | Domain-appropriate |
| "สิทธิ" | ✅ | Analysis, category detail | Consistent legal term |
| "ขั้นตอน" | ✅ | Timeline, search, analysis | Consistent |
| "กำหนดการ" | ✅ | Tax, notifications | Consistent |

### Tone Consistency Per Context
| Context | Tone | Examples |
|---------|------|----------|
| Homepage greeting | Warm, inviting | "สวัสดีค่ะ...", "วันนี้มีเรื่องอะไรให้ช่วย?" |
| Category detail | Empowering, urgent | "คุณทำงานหนักมา — ถึงเวลาเรียกร้องสิทธิ" |
| Diagnosis wizard | Neutral, supportive | "ตอบเท่าที่ทราบ • กลับมาแก้ได้" |
| Loading states | Reassuring | "AI กำลังวิเคราะห์เคสของคุณ... ปกติ 30-90 วินาที" |
| Error states | Apologetic, helpful | "ขออภัย เกิดปัญหาขณะแสดงหน้านี้" |
| Legal pages | Formal, precise | "ข้อกำหนดการใช้บริการ (Terms of Service)" |
| AI assistant | Friendly, helpful | "สวัสดีค่ะ ฉันคือ AI Legal Assistant" |
| Tax page | Professional, optimistic | "✅ คุณประหยัดภาษีได้ ฿XX,XXX" |

### Icon & Emoji Usage Inventory
| Icon/Emoji | Meaning | Pages Used | Consistent? |
|-----------|---------|-----------|-------------|
| ✦ | AI / Sparkle | Home, diagnosis, assistant, onboarding, signin | ✅ |
| ⌕ | Search | Home, search, 404 | ✅ |
| 🛡️ | Security | Home, evidence, trust-strip | ✅ |
| 📄 | Document | Documents, search sidebar | ✅ |
| 👨‍⚖️ | Lawyer | Lawyers, category detail | ✅ |
| ⚖️ | Justice/Law | Category pages, lawyer detail | ✅ |
| 💰 | Money/Tax | Tax page, pricing | ✅ |
| ⚡ | Urgent action | Category problem examples | ✅ |
| ⏰ | Time-sensitive | Category problem examples | ✅ |
| 📅 | Scheduled/Long term | Category problem examples, tax | ✅ |
| ✓ | Verified/Done | Lawyer cards, evidence checklist | ✅ |
| ✎ | Edit | Profile avatar | ✅ |
| ♡ | Save/Favorite | Search, lawyer cards | ✅ |
| ↗ | Share | Search | ✅ |

### Button/CTA Style Consistency
| Pattern | Format | Used Where | Consistent? |
|---------|--------|-----------|-------------|
| Primary CTA | `className="primary"` + "→" suffix | Main CTAs | ✅ |
| Ghost/Back | `className="ghost"` + "←" prefix | Back navigation | ✅ |
| Outline | `className="outline"` | Secondary actions | ✅ |
| Full width | `className="primary full"` | Sidebar CTAs | ✅ |
| "เริ่ม..." prefix | Entry points | "เริ่มวิเคราะห์", "เริ่มสร้าง", "เริ่มนัดหมาย" | ✅ |
| "กลับ..." prefix | Back nav | "กลับหน้าหลัก", "กลับไปเลือกหมวดหมู่" | ✅ |
| "ดู..." prefix | Browse | "ดูทั้งหมด", "ดูแพ็กเกจ", "ดูโปรไฟล์" | ✅ |

### Privacy/Disclaimer Pattern Inventory
| Pattern | Prefix | Location | Count |
|---------|--------|----------|-------|
| Privacy note | "⌾ " | Diagnosis, categories, onboarding | 4 |
| Info disclaimer | "ⓘ " | Search, analysis, tax | 3 |
| Warning | "⚠️ " | Terms, guardrails, category detail | 3 |
| Emergency | "🚨 " | Guardrails (emergency-redirect) | 1 |
| Example data | PrototypeDataNotice | 15+ pages | 15+ |
| Legal disclaimer | LegalDisclaimer | Analysis page | 1 |
| Consequence notice | GentleConsequenceNotice | Timeline, analysis | 2 |

---

## PART 8: ACCESSIBILITY AUDIT

### Current Accessibility Features
- ✅ Semantic HTML: header, nav, section, article, aside, main
- ✅ ARIA labels: aria-label on interactive elements (buttons, inputs, links)
- ✅ ARIA live regions: aria-live="polite" on loading/error states
- ✅ Keyboard navigation: Tab order follows visual order
- ✅ Focus indicators: CSS :focus-visible styles
- ✅ Role attributes: role="search", role="radiogroup", role="group"
- ✅ Form labels: htmlFor connections, aria-labelledby
- ✅ ARIA states: aria-pressed, aria-current="page", aria-invalid
- ✅ Reduced motion: Mentioned in design system handoff docs
- ✅ Touch targets: Design system specifies ≥44px

### Accessibility Gaps
- ❌ No skip-to-main-content link
- ❌ No high-contrast theme/mode
- ⚠️ Color-dependent info: Urgency pills use color without text fallback
- ⚠️ Emoji-only icons: Some decorative emojis lack aria-hidden
- ⚠️ Dynamic content: Not all state changes announced via aria-live
- ❌ No focus trap in modals (no modals implemented yet)
- ⚠️ Form validation errors: Shown visually but not linked via aria-describedby
- ⚠️ Progress indicators: Progress bar lacks aria-valuenow/aria-valuemin/aria-valuemax

---

## PART 9: PERFORMANCE ANALYSIS

### Current State
- ✅ Server components: terms, privacy, design-system (zero client JS)
- ✅ useMemo for expensive computations (tax bracket breakdown, lawyer finding)
- ✅ useCallback for stable callbacks (evidence validation)
- ⚠️ No lazy loading beyond Next.js defaults
- ⚠️ No image optimization needed (few images used)
- ⚠️ Large inline data: PROBLEM_EXAMPLES (90 lines), lawyer data (100 lines)
- ⚠️ Only one Suspense boundary (document create page)

### Performance Recommendations
1. Extract PROBLEM_EXAMPLES to lib/legal/problem-examples.ts
2. Extract lawyer mock data to lib/mock/lawyers.ts
3. Add Suspense boundaries on search, diagnosis, and cases pages
4. Implement React.lazy for admin chart component
5. Add loading skeletons for initial page loads (not just spinners)
6. Implement search input debouncing (300ms)
7. Add pagination for lawyer listing (scales beyond 5 mock entries)

---

## PART 10: SECURITY POSTURE

### Current Security Features
- ✅ Supabase Auth: Email OTP + Google OAuth
- ✅ Admin warning: "การเข้าถึงจริงต้องมีบทบาท admin และ MFA"
- ✅ Error boundaries: Never expose stack traces to users
- ✅ PII redaction rules: Defined in guardrails (banned patterns)
- ✅ Privacy-safe analytics: No PII, case text, or filenames in events

### Security Gaps
- ❌ Admin page: No real auth guard (publicly accessible with just a warning)
- ❌ Feature gates: Defined but not enforced at API level
- ❌ Rate limiting: Not visible on any API route
- ⚠️ sessionStorage: Analysis results accessible to browser extensions
- ❌ CSP headers: No Content-Security-Policy visible
- ❌ CSRF: No CSRF tokens on API routes
- ❌ Input sanitization: No visible sanitization before AI prompts

### Security Recommendations
1. Add middleware-based admin auth guard
2. Enforce feature gates with server-side checks
3. Add rate limiting to /api/ai/* endpoints
4. Move analysis results to server-side storage (not sessionStorage)
5. Add Content-Security-Policy headers
6. Add input sanitization before AI prompts
7. Add CSRF protection for mutation endpoints

---

## PART 11: DATA ARCHITECTURE

### Current Data Flow
```
                    ┌─────────────┐
                    │  DeepSeek AI │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
    /api/ai/assistant  /api/ai/diagnosis
              │            │
              ▼            ▼
         Search Page   Diagnosis Wizard
              │            │
              │            ▼
              │     sessionStorage
              │            │
              │            ▼
              │     Analysis Page
              │
              ▼
         No persistence

    ┌─────────────┐
    │ Supabase Auth│──► Sign In ──► Onboarding (mock)
    └─────────────┘

    ┌──────────────────────┐
    │ Client-side only:     │
    │  - Tax calculator     │
    │  - Document editor    │
    │  - Evidence upload    │
    │  - Lawyer booking     │
    │  - Case management    │
    └──────────────────────┘
```

### Desired Data Architecture (V4)
```
                    ┌──────────────┐
                    │  DeepSeek AI  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              │            │                │
    /api/ai/assistant  /api/ai/diagnosis  /api/tax/optimize
              │            │                │
              └────────────┼────────────────┘
                           │
                    ┌──────▼──────┐
                    │  Guardrails  │──► Filter + Validate
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Supabase    │──► Persist results
                    └──────┬──────┘
                           │
              ┌────────────┼──────────────┐
              │            │              │
         Cases Table   Documents Table   User Profile
              │            │              │
              ▼            ▼              ▼
         Case Pages   Document Pages   Settings

    ┌──────────────────────┐
    │ Real-time:            │
    │  Supabase Realtime ──► Notifications
    │  Supabase Storage  ──► Evidence files
    │  Calendar API      ──► Lawyer booking
    │  Payment Gateway   ──► Package upgrades
    └──────────────────────┘
```

---

## PART 12: EXECUTABLE IMPROVEMENT SPECS

### Home Page Specific Changes
```
FILE: app/page.tsx
1. Replace hardcoded "คุณนภัสสร" with user.displayName from auth
2. Add <LiveSocialProof /> component below hero card
3. Add <FearCheckinButton /> entry point
4. Add concierge CTA: "ไม่แน่ใจ? ให้ AI ช่วยแนะนำ →"
5. Quick searches: Pull from trending data (social-proof time signals)
```

### Diagnosis Wizard Specific Changes
```
FILE: app/diagnosis/page.tsx
1. Add fear calibration as step 0 (before category questions)
2. Wire detectDrives() during answer collection
3. Pass driveProfile.tone to question framing
4. Add answer persistence to localStorage
5. Show "กำลังเตรียมคำถามถัดไป..." transition
6. Add skip button for optional questions
7. Category label in header instead of just Brand logo
```

### Search Page Specific Changes
```
FILE: app/search/page.tsx
1. Replace STATIC_STEPS with AI-generated steps from API response
2. Add search history with localStorage persistence
3. Add autocomplete/suggestions dropdown
4. Wire sort functionality to re-query API
5. Wire article links to real content pages
6. Add "ถามต่อ" follow-up input on answer card
7. Show drive-detected tone in AI response header
```

### Tax Page Specific Changes
```
FILE: app/tax/page.tsx
1. Refactor to use calculateTax() from lib/tax/calculator
2. Use TaxPayerProfile type for structured input
3. Wire AI Tax Optimizer to real API
4. Add year-over-year comparison (2568 vs 2569)
5. Add what-if scenarios
6. Integrate quickEstimateDeductions() for simple mode
```

### Evidence Page Specific Changes
```
FILE: app/cases/[caseId]/evidence/page.tsx
1. Wire real file upload to Supabase Storage
2. Add file preview (image thumbnails, PDF viewer)
3. Add AI-powered document analysis
4. Add OCR for auto-filling case data
5. Persist uploaded files across sessions
```

---

## PART 13: TEST COVERAGE RECOMMENDATIONS

### Priority Test Cases
| # | Function | Test Type | Priority |
|---|----------|-----------|----------|
| 1 | calcTax() | Unit — 8 bracket correctness | P0 |
| 2 | computeDeductions() | Unit — cap enforcement | P0 |
| 3 | checkGuardrails() | Unit — all 14 rules | P0 |
| 4 | detectDrives() | Unit — keyword accuracy | P1 |
| 5 | mergeTemplate() | Unit — field replacement | P1 |
| 6 | formatThaiDate() | Unit — Buddhist calendar | P1 |
| 7 | suggestCategory() | Unit — keyword mapping | P2 |
| 8 | Diagnosis wizard | Integration — full flow | P1 |
| 9 | Search page | Integration — AI response | P1 |
| 10 | Tax page | Integration — calculation | P1 |
| 11 | All 27 pages | Smoke — render without crash | P0 |

---

## APPENDIX A: Complete Thai CTA Inventory

### Entry Point CTAs
1. "เริ่มวิเคราะห์ฟรี →"
2. "เลือกเอกสาร →"
3. "ค้นหาทนาย →"
4. "ลองคำนวณ →"
5. "ดูแพ็กเกจ →"
6. "ดูทั้งหมด →"
7. "ดูเคสทั้งหมด →"
8. "เริ่มวิเคราะห์ →"
9. "🤖 เริ่มวิเคราะห์เคสของฉัน"
10. "เริ่มสร้างเอกสาร →"
11. "ดูแบบฟอร์มทั้งหมด 126 รายการ →"
12. "เริ่มสร้าง →"
13. "+ สร้างเคสใหม่"
14. "+ เริ่มเคสใหม่"
15. "เริ่มนัดหมาย"

### Purchase CTAs
16. "อัปเกรดเลย"
17. "เลือกแพ็กเกจ"
18. "เริ่มใช้งานฟรี"
19. "อัปเกรดแพ็กเกจ"

### Navigation CTAs
20. "ดูโปรไฟล์และนัดหมาย"
21. "นัดหมายปรึกษา"
22. "ถาม AI →"
23. "♙ ปรึกษาทนายเกี่ยวกับเคสนี้"
24. "สร้างเคสและเริ่มดำเนินการ"
25. "กลับหน้าหลัก"
26. "← กลับไปเลือกหมวดหมู่อื่น"
27. "‹ กลับหน้าหลัก"

### Action CTAs
28. "ส่งรหัสยืนยัน"
29. "ดำเนินต่อด้วย Google"
30. "ยืนยันและเข้าสู่ระบบ"
31. "🤖 ให้ AI วิเคราะห์แผนลดหย่อน"
32. "🖨️ พิมพ์ / PDF"
33. "🔄 เปรียบเทียบแบบมี/ไม่มีลดหย่อน"
34. "ให้ AI ช่วยเลือก"

---

## APPENDIX B: All Privacy & Security Messages

1. "ข้อมูลของคุณได้รับการปกป้อง" (homepage trust strip)
2. "เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
3. "⌾ คำตอบของคุณใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น — เราไม่เปิดเผยข้อมูลให้บุคคลภายนอก"
4. "⌾ คำตอบของคุณถูกส่งเพื่อวิเคราะห์เท่านั้น และไม่ถูกเก็บไว้ที่อื่น"
5. "⌾ คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น คุณลบหรือแก้ไขได้เสมอ"
6. "ไฟล์ของคุณปลอดภัย — เข้ารหัสตามมาตรฐานสากล • ไม่เปิดเผยให้บุคคลภายนอก"
7. "⌾ ข้อมูลของคุณได้รับการเก็บรักษาอย่างปลอดภัย"
8. "ⓘ ข้อมูลนี้เป็นคำแนะนำเบื้องต้น ผลลัพธ์จริงขึ้นอยู่กับรายละเอียดของแต่ละกรณี"
9. "AI อาจให้ข้อมูลคลาดเคลื่อน โปรดตรวจสอบข้อมูลสำคัญกับผู้เชี่ยวชาญ"
10. "ผลค้นหาเป็นข้อมูลกฎหมายเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย"
11. "⚠️ ข้อมูลนี้เป็นข้อมูลกฎหมายทั่วไป (legal information) ไม่ใช่คำแนะนำทางกฎหมาย (legal advice)"
12. "AI อาจมีข้อผิดพลาด — ควรตรวจสอบกับทนายหรือผู้เชี่ยวชาญก่อนดำเนินการ"
13. "เราไม่รับประกันผลลัพธ์ — แต่ละคดีมีปัจจัยเฉพาะ"
14. "ข้อมูลนี้เป็นประมาณการเบื้องต้น — ควรตรวจสอบกับผู้เชี่ยวชาญด้านภาษีก่อนยื่นแบบ"
15. "เอกสารที่สร้างเป็นแบบร่าง ควรตรวจสอบโดยผู้เชี่ยวชาญก่อนใช้งาน"
16. "ข้อมูลทนายเป็นข้อมูลตัวอย่าง ควรตรวจสอบใบอนุญาตอิสระ"
17. "⌾ เราไม่สามารถทำนายผลคดีได้ — แต่ละคดีมีปัจจัยเฉพาะ"
18. "🚨 หากคุณกำลังอยู่ในสถานการณ์ฉุกเฉิน — กรุณาติดต่อ 191 (ตำรวจ) หรือ 1300 ทันที"

---

## APPENDIX C: File Size Summary

| File | Lines | Size |
|------|-------|------|
| admin/page.tsx | 713 | 23.7 KB |
| onboarding/page.tsx | 563 | 23.2 KB |
| lawyers/[id]/page.tsx | 565 | 23.5 KB |
| cases/[caseId]/evidence/page.tsx | 542 | 20.0 KB |
| tax/page.tsx | 516 | 25.4 KB |
| lib/tax/deductions.ts | 512 | 18.7 KB |
| lib/documents/merge-engine.ts | 521 | 18.7 KB |
| lib/legal/diagnosis-config.ts | 462 | 24.6 KB |
| lib/legal/guardrails.ts | 444 | 23.7 KB |
| lib/documents/templates.ts | 383 | 22.4 KB |
| lib/legal/drive-detection.ts | 377 | 27.8 KB |
| app/diagnosis/page.tsx | 334 | 11.0 KB |
| app/documents/[category]/page.tsx | 317 | 10.4 KB |
| app/lawyers/page.tsx | 315 | 11.8 KB |
| lib/tax/calculator.ts | 310 | 9.1 KB |
| app/search/page.tsx | 288 | 13.9 KB |
| lib/legal/social-proof.ts | 285 | 11.6 KB |
| lib/legal/sources.ts | 284 | 15.6 KB |
| app/analysis/[caseId]/page.tsx | 277 | 11.8 KB |
| app/assistant/page.tsx | 268 | 9.6 KB |
| app/categories/[category]/page.tsx | 258 | 21.5 KB |
| app/documents/page.tsx | 257 | 9.7 KB |
| app/documents/create/page.tsx | 232 | 7.6 KB |
| lib/legal/category-drives.ts | 226 | 16.1 KB |
| domain/types.ts | 225 | 6.8 KB |
| lib/documents/categories.ts | 221 | 8.2 KB |
| app/page.tsx | 217 | 9.3 KB |
| app/auth/signin/page.tsx | 212 | 7.7 KB |
| app/profile/page.tsx | 196 | 12.1 KB |
| lib/packages/definitions.ts | 172 | 5.2 KB |
| app/cases/[caseId]/timeline/page.tsx | 168 | 6.8 KB |
| app/cases/page.tsx | 154 | 5.1 KB |
| app/design-system/page.tsx | 139 | 5.3 KB |
| app/notifications/page.tsx | 129 | 4.4 KB |
| lib/legal/fear-calibration.ts | 100 | 4.4 KB |
| app/pricing/page.tsx | 97 | 5.5 KB |
| app/terms/page.tsx | 97 | 6.2 KB |
| app/privacy/page.tsx | 94 | 6.8 KB |
| app/categories/page.tsx | 61 | 2.9 KB |
| app/error.tsx | 51 | 1.8 KB |
| app/not-found.tsx | 20 | 0.9 KB |
| **TOTAL** | **~12,700** | **~520 KB** |

---

## APPENDIX D: Component Hierarchy Map

```
AppShell (layout.tsx)
├── Header / Brand
├── Navigation
│   ├── Home (/)
│   ├── Categories (/categories)
│   │   └── Category Detail (/categories/[category])
│   ├── Diagnosis (/diagnosis)
│   ├── Search (/search)
│   ├── Documents (/documents)
│   │   ├── Category Detail (/documents/[category])
│   │   └── Create (/documents/create)
│   ├── Tax (/tax)
│   ├── Pricing (/pricing)
│   ├── Lawyers (/lawyers)
│   │   └── Lawyer Detail (/lawyers/[id])
│   ├── Cases (/cases)
│   │   ├── Timeline (/cases/[caseId]/timeline)
│   │   └── Evidence (/cases/[caseId]/evidence)
│   ├── Assistant (/assistant)
│   ├── Notifications (/notifications)
│   ├── Profile (/profile)
│   ├── Admin (/admin)
│   └── Analysis (/analysis/[caseId])
├── Auth
│   ├── Sign In (/auth/signin)
│   ├── Callback (/auth/callback)
│   └── Onboarding (/onboarding)
├── Legal
│   ├── Terms (/terms)
│   └── Privacy (/privacy)
├── Error (/error)
├── 404 (/not-found)
└── Dev
    └── Design System (/design-system)
```

---

## APPENDIX E: API Endpoint Inventory

| Endpoint | Method | Purpose | Status |
|----------|--------|---------|--------|
| /api/ai/assistant | POST | AI chat assistant | ✅ Working |
| /api/ai/diagnosis | POST | AI case diagnosis | ✅ Working |
| /api/documents/generate | POST | Document generation | ❌ Not implemented |
| /api/tax/optimize | POST | Tax optimization | ❌ Not implemented |
| /api/lawyers/book | POST | Lawyer booking | ❌ Not implemented |
| /api/cases/* | CRUD | Case management | ❌ Not implemented |
| /api/evidence/upload | POST | Evidence upload | ❌ Not implemented |
| /api/notifications | GET | Notification list | ❌ Not implemented |
| /api/profile | GET/PUT | User profile | ❌ Not implemented |
| /api/admin/* | Various | Admin operations | ❌ Not implemented |

---

## APPENDIX F: Complete V4 Concierge Gap Analysis

| Concierge Feature | Current State | Library Ready | UI Ready | Priority |
|-------------------|---------------|---------------|----------|----------|
| Personalized greeting | Hardcoded name | ❌ (no user context) | ⚠️ (UI exists) | P0 |
| Fear calibration | Not wired | ✅ | ❌ | P0 |
| Drive detection in AI | Not in prompts | ✅ | ❌ | P0 |
| Drive-aware category hooks | ✅ (cat detail) | ✅ | ✅ | Done |
| Social proof display | ⚠️ (partial) | ✅ | ⚠️ | P1 |
| Guardrail enforcement | Not wired | ✅ | ❌ | P0 |
| Proactive notifications | Mock only | ❌ | ⚠️ | P1 |
| Deadline tracking | Mock only | ❌ | ⚠️ | P1 |
| Progress dashboard | Mock cases | ❌ | ⚠️ | P1 |
| Case persistence | Not implemented | ❌ | ⚠️ | P0 |
| Document generation | Stub only | ✅ | ⚠️ | P0 |
| Lawyer booking | UI only | ❌ | ✅ | P0 |
| 8-phase flow | Not designed | ❌ | ❌ | P2 |
| Emergency redirect | Guardrail only | ✅ | ❌ | P1 |
| Voice input | Not implemented | ❌ | ❌ | P3 |

---

*End of Report — Expanded Appendices*
*Total: 3,150+ lines*
*Generated: 12 August 2026*


---

## APPENDIX G: Per-Category Diagnosis Question Inventory (Complete)

### 1. labour (กฎหมายแรงงาน) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | เกิดอะไรขึ้นกับคุณ? | ถูกเลิกจ้าง, ถูกบังคับให้ลาออก, นายจ้างค้างจ่ายเงิน, เงื่อนไขการทำงานไม่เป็นธรรม |
| 2 | คุณทำงานมานานเท่าไร? | น้อยกว่า 120 วัน, 120 วัน – 1 ปี, 1 – 3 ปี, มากกว่า 3 ปี |
| 3 | นายจ้างแจ้งล่วงหน้าหรือไม่? | ไม่แจ้ง เลิกจ้างทันที, แจ้งล่วงหน้าแล้ว, แจ้งด้วยวาจาเท่านั้น, ไม่แน่ใจ |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | สัญญาจ้างงาน, สลิปเงินเดือน, หนังสือเลิกจ้าง, แชทหรืออีเมล |

### 2. consumer (ผู้บริโภค) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | ปัญหาที่พบคืออะไร? | สินค้าไม่ตรงปก, สินค้าชำรุด, ไม่ได้รับสินค้า, บริการไม่เป็นธรรม |
| 2 | ซื้อผ่านช่องทางใด? | แพลตฟอร์มออนไลน์, ร้านค้าปลีก, เพจ/โซเชียล, เว็บไซต์ของผู้ขาย |
| 3 | มูลค่าความเสียหายประมาณเท่าไร? | น้อยกว่า 1,000, 1,000–10,000, 10,001–50,000, มากกว่า 50,000 |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | ใบเสร็จ/หลักฐานการชำระ, ภาพสินค้า, แชทกับผู้ขาย, นโยบายคืนสินค้า |

### 3. debt (หนี้และการเงิน) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | สถานการณ์ของคุณคืออะไร? | ถูกทวงหนี้, ต้องการทวงหนี้, ปัญหาดอกเบี้ยนอกระบบ, ถูกคุกคามจากเจ้าหนี้ |
| 2 | ยอดหนี้ประมาณเท่าไร? | น้อยกว่า 10,000, 10,000–100,000, 100,001–500,000, มากกว่า 500,000 |
| 3 | หนี้เกิดขึ้นนานแค่ไหนแล้ว? | น้อยกว่า 2 ปี, 2–5 ปี, มากกว่า 5 ปี, ไม่แน่ใจ |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | สัญญากู้ยืม, หลักฐานการโอนเงิน, บันทึกการทวงถาม, แชท/อีเมล |

### 4. housing (บ้านและที่อยู่อาศัย) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | ปัญหาของคุณคืออะไร? | ต้องการบอกเลิกสัญญาเช่า, เจ้าของที่ไม่คืนเงินมัดจำ, ผู้เช่าไม่จ่ายค่าเช่า, ข้อพิพาทสภาพทรัพย์ |
| 2 | มีสัญญาเป็นลายลักษณ์อักษรหรือไม่? | มี สัญญาเป็นลายลักษณ์อักษร, สัญญาปากเปล่า, มีแชท/อีเมล, ไม่แน่ใจ |
| 3 | เช่ามานานแค่ไหนแล้ว? | น้อยกว่า 6 เดือน, 6 เดือน – 1 ปี, 1–3 ปี, มากกว่า 3 ปี |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | สัญญาเช่า, หลักฐานการชำระค่าเช่า, ภาพสภาพทรัพย์, แชทกับอีกฝ่าย |

### 5. family (ครอบครัวและมรดก) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | เรื่องที่ต้องการคำปรึกษาคืออะไร? | หย่าร้าง, การปกครองบุตร, มรดก, คู่สมรสไม่ซื่อสัตย์ |
| 2 | สถานะการสมรสในปัจจุบัน? | จดทะเบียนสมรส, ไม่จดทะเบียน, หย่าแล้ว, แยกกันอยู่ |
| 3 | มีบุตรด้วยกันหรือไม่? | มี อายุต่ำกว่า 7 ปี, มี อายุ 7 ปีขึ้นไป, ไม่มีบุตร, มีบุตรจากการสมรสก่อนหน้า |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | ทะเบียนสมรส, ทะเบียนบุตร, หนังสือมอบอำนาจ, สัญญายกทรัพย์/พินัยกรรม |

### 6. accident (รถและอุบัติเหตุ) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | เกิดอะไรขึ้น? | อุบัติเหตุรถยนต์, อุบัติเหตุมอเตอร์ไซค์, บาดเจ็บในที่สาธารณะ, รถชนทรัพย์สิน |
| 2 | ใครเป็นฝ่ายผิด? | อีกฝ่ายผิดชัดเจน, ตนเองผิด, ผิดร่วมกัน, ยังไม่ชัดเจน |
| 3 | มีการบาดเจ็บหรือไม่? | ไม่บาดเจ็บ, บาดเจ็บเล็กน้อย, บาดเจ็บสาหัส, เสียชีวิต |
| 4 | คุณมีหลักฐานอะไรบ้าง? (multi) | ใบแจ้งความ, ภาพถ่าย, ใบรับรองแพทย์, ประกันภัย |

### 7. online_fraud (ภัยออนไลน์) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | คุณถูกหลอกแบบไหน? | ซื้อของออนไลน์ไม่ได้ของ, Call Center หลอกโอนเงิน, แอปกู้เงินเถื่อน, Romance Scam/หลอกรัก, แชร์ลูกโซ่/ลงทุนปลอม |
| 2 | โอนเงินไปเท่าไหร่? | น้อยกว่า 5,000, 5,000–50,000, 50,001–200,000, มากกว่า 200,000 |
| 3 | โอนเงินไปเมื่อไหร่? | ภายใน 24 ชม. (รีบที่สุด!), 1-3 วัน, 3-7 วัน, เกิน 7 วัน |
| 4 | คุณมีหลักฐานอะไร? (multi) | สลิปโอนเงิน, แชทกับมิจฉาชีพ, URL/ลิงก์, เบอร์โทร, เลขบัญชีปลายทาง |

### 8. crime (อาชญากรรม) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | เกิดอะไรขึ้น? | ถูกทำร้ายร่างกาย, ถูกลักทรัพย์/ชิงทรัพย์, ถูกข่มขืน/คุกคามทางเพศ, ถูกขู่กรรโชก |
| 2 | เกิดขึ้นเมื่อไหร่? | กำลังเกิด/เพิ่งเกิด, ภายใน 24 ชม., 1-7 วัน, เกิน 7 วัน |
| 3 | มีหลักฐานอะไร? (multi) | ใบรับรองแพทย์, ภาพถ่าย, พยานบุคคล, คลิป/กล้องวงจรปิด, รายการทรัพย์ที่หาย |
| 4 | แจ้งความแล้วหรือยัง? | ยัง, แจ้งแล้ว, ไม่แน่ใจ |

### 9. government (เรื่องราชการ) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | ปัญหาเกี่ยวกับอะไร? | ขอทะเบียน/บัตร ปชช.ไม่ได้, ถูกรัฐละเมิดจนเสียหาย, ร้องเรียนแล้วไม่ตอบ, ถูกเวนคืนที่ดิน |
| 2 | เกิดปัญหามานานแค่ไหน? | น้อยกว่า 30 วัน, 1-3 เดือน, 3-6 เดือน, เกิน 6 เดือน |
| 3 | เกี่ยวข้องกับหน่วยงานไหน? | อำเภอ/เขต, กรมที่ดิน, สรรพากร, กระทรวง/กรม, ไม่แน่ใจ |
| 4 | มีเอกสารอะไรบ้าง? (multi) | คำขอ/แบบฟอร์มที่ยื่น, ใบเสร็จ/หลักฐานการติดต่อ, หนังสือตอบกลับ, ภาพถ่าย |

### 10. insurance (ประกันภัย) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | ปัญหาเกี่ยวกับประกันอะไร? | เคลมประกันรถไม่ได้, เคลมประกันสุขภาพ/ชีวิต, ยกเลิกกรมธรรม์ไม่เป็นธรรม, ประกันไม่จ่ายตามสัญญา |
| 2 | เกิดเรื่องเมื่อไหร่? | ภายใน 7 วัน, 7-30 วัน, 1-6 เดือน, เกิน 6 เดือน |
| 3 | มีหลักฐานอะไร? (multi) | กรมธรรม์, ใบแจ้งเหตุ, ใบรับรองแพทย์, รูปถ่าย, บันทึกการติดต่อ |
| 4 | บริษัทประกันตอบว่าอะไร? | ยังไม่ตอบ, ปฏิเสธการเคลม, ขอเอกสารเพิ่ม, รับเคลมแต่จ่ายน้อย |

### 11. defamation (หมิ่นประมาท) — 5 questions
| # | Question | Options |
|---|----------|---------|
| 1 | เกิดอะไรขึ้น? | ถูกด่าบนโซเชียล, ภาพหลุด/แอบถ่าย, ถูกใส่ความ/ให้ร้าย, ข้อมูลส่วนตัวรั่วไหล |
| 2 | ผ่านช่องทางไหน? | Facebook, LINE, TikTok, X (Twitter), Telegram, เว็บบอร์ด/เว็บไซต์ |
| 3 | ใครเป็นคนโพสต์? | แฟนเก่า/คนเคยรู้จัก, เพื่อน/คนรู้จัก, คนแปลกหน้า, ไม่รู้ว่าใคร |
| 4 | เกิดขึ้นเมื่อไหร่? | ภายใน 7 วัน, 7-30 วัน, 1-2 เดือน, เกิน 2 เดือน (เหลือเวลาน้อย!) |
| 5 | มีหลักฐานอะไร? (multi) | แคปหน้าจอ, URL/ลิงก์, พยานบุคคล, บันทึกแชท |

### 12. property (ที่ดิน/ทรัพย์สิน) — 4 questions
| # | Question | Options |
|---|----------|---------|
| 1 | ปัญหาเกี่ยวกับที่ดิน/ทรัพย์สินอะไร? | ที่ดินถูกบุกรุก, แนวเขตไม่ชัด, ซื้อขาย/โอนไม่ได้, มรดกที่ดิน, โฉนดหาย/ชำรุด |
| 2 | มีเอกสารสิทธิ์อะไร? | โฉนด (น.ส.4), น.ส.3 ก., สัญญาซื้อขาย, ไม่มีเอกสาร |
| 3 | เกิดปัญหามานานแค่ไหน? | น้อยกว่า 1 ปี, 1-5 ปี, 5-10 ปี, เกิน 10 ปี |
| 4 | มีหลักฐานอะไร? (multi) | เอกสารสิทธิ์, ภาพถ่าย, พยานบุคคล, หนังสือแจ้งเตือน |

---

## APPENDIX H: Complete Guardrail Pattern Reference

### P0 Patterns (Must Never Violate)
| Guardrail | Banned Patterns (regex) | User Message |
|-----------|------------------------|--------------|
| no-legal-advice | /คุณควร(ทำ|ฟ้อง|ยื่น|เรียก)/gi, /แนะนำให้/gi | ข้อมูลนี้เป็นข้อมูลกฎหมายทั่วไป ไม่ใช่คำแนะนำทางกฎหมาย |
| no-outcome-prediction | /โอกาสชนะ\d+%/gi, /ชนะ(คดี|แน่)/gi | เราไม่สามารถทำนายผลคดีได้ |
| no-lawyer-ranking | /ทนาย(ที่|คนนี้)(ดี|เก่ง)(ที่สุด|มาก)/gi | เราให้คุณเลือกทนายที่เหมาะกับคุณ |
| no-court-filing | /เรา(จะ|ได้)ยื่น(เอกสาร|คำร้อง)/gi | การยื่นต่อศาลเป็นหน้าที่ของคุณหรือทนาย |
| no-self-representation | /(ไม่ต้อง|ไม่จำเป็นต้อง)จ้างทนาย/gi | การดำเนินคดีด้วยตนเองมีความเสี่ยง |
| emergency-redirect | /ถูกทำร้าย|ถูกข่มขืน|ถูกคุกคาม|กลัวตาย|จะฆ่า/gi | กรุณาติดต่อ 191 หรือ 1300 ทันที |
| no-statute-of-limitations | /อายุความ.*\d+\s*(ปี|วัน|เดือน)/gi | อายุความเป็นเรื่องที่ควรตรวจสอบกับทนาย |
| no-legal-fee-quotes | /ค่าทนาย(ประมาณ|ราวๆ?)\s*[\d,]+/gi | เราไม่สามารถประมาณค่าทนายได้ |

---

## APPENDIX I: Complete Drive Detection Keyword Map

### Positive Drives (1-18)
| # | Drive | Thai Label | Top Keywords | Weight |
|---|-------|-----------|-------------|--------|
| 1 | survival | อยู่รอดและปลอดภัย | กลัว, ไม่ปลอดภัย, อันตราย, ถูกข่มขู่, ถูกคุกคาม, ถูกทำร้าย, ฉุกเฉิน | 0.9 |
| 2 | value | ผลประโยชน์/คุ้มค่า | ค่าเสียหาย, ค่าชดเชย, เงินคืน, ค่าเช่า, ค่าจ้าง, ค้างจ่าย, เงินมัดจำ | 0.8 |
| 3 | recognition | การยอมรับ/คำชม | เครดิต, ชื่อเสียง, ถูกมองข้าม, ไม่มีใครเห็น, ผลงาน | 0.6 |
| 4 | status | สถานะ/หน้ามีตา | หน้า, เสียหน้า, ภาพลักษณ์, ตำแหน่ง, สังคม | 0.7 |
| 5 | belonging | ความสัมพันธ์/พวกพ้อง | ครอบครัว, พวกเรา, กลุ่ม, เพื่อน, สังคม, ชุมชน | 0.6 |
| 6 | love | ความรัก/ใกล้ชิด | รัก, คนรัก, คู่สมรส, แฟน, สามี, ภรรยา, หย่า, นอกใจ | 0.8 |
| 7 | power | อำนาจ/ควบคุม | จัดการเอง, ควบคุม, ตัดสินใจ, สั่ง, บังคับ, อำนาจ, สิทธิ | 0.5 |
| 8 | dominance | ข่ม/อยู่เหนือ | ชนะ, เอาชนะ, เหนือกว่า, สู้, ต้องชนะ | 0.5 |
| 9 | freedom | อิสระ/เป็นตัวเอง | อิสระ, ไม่ต้องมาสั่ง, เลือกเอง, ถูกบังคับให้ลาออก, บังคับ, ไล่ที่, ขับไล่ | 0.7 |
| 10 | competence | ความสามารถ/เก่ง | เก่ง, ความสามารถ, ทักษะ, เชี่ยวชาญ, ผู้เชี่ยวชาญ | 0.4 |
| 11 | achievement | ความสำเร็จ/ชัยชนะ | สำเร็จ, ชนะ, ที่ 1, เป้าหมาย, ความก้าวหน้า | 0.4 |
| 12 | order | ความแน่นอน/ระเบียบ | checklist, ระเบียบ, แน่นอน, ชัดเจน, สัญญา, หลักฐาน, เอกสาร, ใบเสร็จ | 0.7 |
| 13 | novelty | ตื่นเต้น/ประสบการณ์ใหม่ | ใหม่, ลอง, เปลี่ยน, ประสบการณ์ใหม่, ไม่เคย | 0.3 |
| 14 | fairness | ยุติธรรม/ถูกต้อง | ไม่เป็นธรรม, ไม่ยุติธรรม, ไม่แฟร์, เลือกปฏิบัติ, ละเมิด, เอาเปรียบ, ไม่ตรงปก | 0.85 |
| 15 | caregiving | ดูแล/เป็นผู้ให้ | ดูแล, ช่วยเหลือ, ปกครอง, บุตร, ลูก, พ่อแม่, ผู้สูงอายุ, มีบุตร | 0.75 |
| 16 | identity | อัตลักษณ์/ตัวตน | ผมเป็นคน, ฉันเป็นคน, ตัวตน, ความเป็นตัวของตัวเอง, สไตล์ | 0.5 |
| 17 | purpose | ความหมาย/จุดมุ่งหมาย | ความหมาย, จุดมุ่งหมาย, เปลี่ยนแปลง, สร้างผลกระทบ, ประโยชน์ส่วนรวม | 0.4 |
| 18 | legacy | มรดก/ชื่อเสียง | มรดก, ตกทอด, รุ่นต่อไป, สืบทอด, พินัยกรรม, ทายาท | 0.7 |

### Avoidance Drives (19-22)
| # | Drive | Thai Label | Top Keywords | Weight |
|---|-------|-----------|-------------|--------|
| 19 | avoid_shame | หลีกเลี่ยงความอับอาย | อาย, อับอาย, เสียหน้า, อย่าบอกใคร, ความลับ, แอบ, ปกปิด | 0.9 |
| 20 | avoid_loss | หลีกเลี่ยงการสูญเสีย | เสียโอกาส, สูญเสีย, เสีย, พลาด, รักษา, เก็บไว้, ไม่อยากเสีย, ถูกเลิกจ้าง, ตกงาน | 0.85 |
| 21 | revenge | แก้แค้น/ทวงคืน | แก้แค้น, ชดใช้, ต้องชดใช้, ไม่ลืม, เจ็บใจ, แค้น, เอาคืน | 0.7 |
| 22 | prove_self | พิสูจน์ตนเอง | พิสูจน์, ดูถูก, ให้เห็น, จะทำให้ดู, เดี๋ยวก็รู้, ไม่เชื่อ | 0.6 |

---

## APPENDIX J: Social Proof Complete Reference

| Category | Users | Success Signal | Resolution Time | Engagement | Trending |
|----------|-------|---------------|-----------------|------------|----------|
| labour | 2,840 | 82% ได้รับค่าชดเชย | 2-4 สัปดาห์ | 78% | ✅ |
| consumer | 1,980 | 76% ได้เงินคืน | 1-2 สัปดาห์ | 72% | ❌ |
| debt | 1,560 | 71% หยุดทวงหนี้ | 2-8 สัปดาห์ | 65% | ✅ |
| housing | 920 | 74% แก้ปัญหาเช่า | 3-6 สัปดาห์ | 68% | ❌ |
| family | 1,340 | 69% ตกลงโดยไม่ฟ้อง | 1-6 เดือน | 71% | ❌ |
| accident | 1,120 | 80% ได้ค่าสินไหม | 1-4 สัปดาห์ | 75% | ❌ |
| online_fraud | 2,100 | 65% อายัดทันเวลา | 24ชม-2สป | 82% | ✅ |
| crime | 680 | 73% ดำเนินการถูกต้อง | 1-12 สัปดาห์ | 70% | ❌ |
| government | 540 | 68% ยื่นถูกช่องทาง | 1-6 เดือน | 60% | ❌ |
| insurance | 890 | 77% ได้เคลมตามสิทธิ | 1-4 สัปดาห์ | 73% | ❌ |
| defamation | 760 | 70% ลบเนื้อหาได้ | 1-8 สัปดาห์ | 76% | ✅ |
| property | 620 | 65% แก้ไขเอกสาร | 1-12 เดือน | 58% | ❌ |

---

## FINAL VERDICT

LegalAI Thailand is a well-architected citizen legal platform at approximately 60% MVP completion. The strongest areas are:

1. Thai-language UX with emotional intelligence (drive-aware messaging, fear calibration logic)
2. Comprehensive legal domain modeling (12 categories, 36 sources, 126 templates, 14 guardrails)
3. Working AI integration with DeepSeek
4. Production-quality tax calculator

The critical path to launch is:
1. Wire fear calibration + drive detection into the diagnosis and AI response pipeline
2. Implement real data persistence (cases, documents, bookings to Supabase)
3. Add guardrail enforcement at API level
4. Complete document generation with per-template content
5. Add admin auth guard and real admin functionality

With these five items addressed, LegalAI would be ready for citizen beta launch with V4 concierge capabilities.

---

*End of Report — 3,500+ lines*
*Generated: 12 August 2026 by Hermes Subagent*
*Source: D:\legalai-citizen-check — 27 page files + 15 library files*
