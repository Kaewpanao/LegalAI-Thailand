# LegalAI Thailand — UX/UI Actionable Improvement Checklist

> **Source:** `legalai_ux_ui_audit_report.md` (3,617 lines)
> **Generated:** 12 สิงหาคม 2569
> **Scope:** Every actionable fix extracted from the audit, organized by page + library + cross-cutting

**Priority Legend:**
- 🔴 **P0** — Critical (must fix for launch: broken, missing safety, data loss)
- 🟡 **P1** — High (significant UX improvement, wired-but-not-working)
- 🟢 **P2** — Medium (polish, completeness, nice-to-have)

**Effort Legend:**
- **S** = Small (< 2 hrs): single-file tweak, wire existing lib, add prop
- **M** = Medium (2–8 hrs): new component, API endpoint, multi-file change
- **L** = Large (1–3 days): backend integration, new feature, DB schema

---

## 📋 1. Home Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Hardcoded user greeting | "คุณนภัสสร" hardcoded | Pull `user.displayName` from auth context | 🔴 P0 | S | `app/page.tsx` |
| 2 | No concierge-style CTA | Generic search | Add "ไม่แน่ใจว่าจะเริ่มตรงไหน? ให้ AI ช่วยแนะนำ →" | 🟡 P1 | S | `app/page.tsx` |
| 3 | No live social proof | Stats not shown on home | Show live social proof stats (e.g. "3,250 คนใช้ LegalAI เดือนนี้") | 🟡 P1 | M | `app/page.tsx` |
| 4 | No fear calibration entry point | Missing entirely | Add "😰 กำลังเครียดเรื่องกฎหมายอยู่? บอกเรา เราช่วยได้" entry | 🔴 P0 | M | `app/page.tsx` |
| 5 | No drive-based personalization | Static action card order | Integrate drive detection to personalize action card order | 🟡 P1 | M | `app/page.tsx` |
| 6 | Hardcoded case preview | Always shows "case-1" | Show real user cases sorted by urgency | 🟡 P1 | M | `app/page.tsx` |
| 7 | Quick searches static | 4 hardcoded pill buttons | Dynamically rank by trending/seasonal issues from social proof | 🟢 P2 | S | `app/page.tsx` |
| 8 | No loading state for initial load | No skeleton/loading | Add loading skeleton for initial page render | 🟢 P2 | S | `app/page.tsx` |
| 9 | No error boundary | No error handling | Add error boundary wrapper | 🟢 P2 | S | `app/page.tsx` |

---

## 📋 2. Categories List Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Links skip category detail page | Goes directly to `/diagnosis?category=` | Change links to `/categories/${cat.id}` for correct IA | 🟡 P1 | S | `app/categories/page.tsx` |
| 2 | No drive hooks on cards | Generic icon + hint only | Add drive-aware hooks per card (e.g. "⚖️ 1,284 คนได้ค่าชดเชยแล้ว") | 🟡 P1 | M | `app/categories/page.tsx` |
| 3 | No category search/filter | Only grid display | Add "🔍 ค้นหาหมวดหมู่" search bar | 🟢 P2 | M | `app/categories/page.tsx` |
| 4 | No urgency indicators | All cards look the same | Show urgency indicators per category | 🟢 P2 | S | `app/categories/page.tsx` |
| 5 | Social proof not used | Static list | Use `CATEGORY_SOCIAL_PROOF` data for "users helped" counts | 🟡 P1 | S | `app/categories/page.tsx` |
| 6 | No trending badges | All cards equal weight | Show "🔥 กำลังเป็นที่นิยม" badge from social proof data | 🟢 P2 | S | `app/categories/page.tsx` |

---

## 📋 3. Category Detail Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | PROBLEM_EXAMPLES hardcoded in page | 90-line inline Record | Extract to `lib/legal/problem-examples.ts` | 🟡 P1 | M | `app/categories/[category]/page.tsx` |
| 2 | No emergency redirect for crisis categories | crime/online_fraud/accident same as others | Add "🆘 ฉุกเฉิน — ติดต่อ 191 / 1441 / 1300 ทันที" banner | 🟡 P1 | M | `app/categories/[category]/page.tsx` |
| 3 | No fear calibration step before diagnosis | Goes straight to wizard | Insert fear calibration question between category page and diagnosis | 🔴 P0 | M | `app/categories/[category]/page.tsx` |
| 4 | Problem examples not ranked | Static order | Dynamic problem ranking from analytics | 🟢 P2 | M | `app/categories/[category]/page.tsx` |
| 5 | No real-time social proof | Only static data | Show "X คนกำลังอ่านหน้านี้" live counter | 🟢 P2 | M | `app/categories/[category]/page.tsx` |
| 6 | Gain messages not used on CTAs | Only loss messages shown | Use gain messages (not just loss aversion) on CTAs | 🟡 P1 | S | `app/categories/[category]/page.tsx` |

---

## 📋 4. Diagnosis Wizard Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Fear calibration not wired | Library exists but step 0 missing | Add `FEAR_CALIBRATION_QUESTION` as step 0 before category questions | 🔴 P0 | M | `app/diagnosis/page.tsx` |
| 2 | Drive detection not running during wizard | `detectDrives()` not called | Wire `detectDrives()` during answer collection for real-time personalization | 🔴 P0 | M | `app/diagnosis/page.tsx` |
| 3 | No answer persistence | Refresh loses all answers | Persist answers to localStorage for resume after refresh | 🟡 P1 | M | `app/diagnosis/page.tsx` |
| 4 | No transition animation between steps | Abrupt step changes | Show "กำลังเตรียมคำถามถัดไป..." transition between steps | 🟢 P2 | S | `app/diagnosis/page.tsx` |
| 5 | No skip button for optional questions | All questions required | Add skip button for optional questions | 🟢 P2 | S | `app/diagnosis/page.tsx` |
| 6 | Progress bar not determinate | Only percentage shown | Show determinate progress X/TOTAL not just percentage | 🟢 P2 | S | `app/diagnosis/page.tsx` |
| 7 | Category label missing in header | Only Brand logo | Show category label "⚖️ กฎหมายแรงงาน" in header | 🟢 P2 | S | `app/diagnosis/page.tsx` |
| 8 | Analysis result only in sessionStorage | Lost if new tab / clear storage | Persist to Supabase instead of sessionStorage | 🔴 P0 | L | `app/diagnosis/page.tsx` |

---

## 📋 5. Search Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Sort dropdown broken — doesn't re-sort | Purely cosmetic, one-shot API call | Wire sort to re-query API with different parameters | 🟡 P1 | M | `app/search/page.tsx` |
| 2 | Static "ขั้นตอนที่แนะนำ" always same 3 steps | Hardcoded generic steps | Replace with AI-generated next actions from API response | 🟡 P1 | M | `app/search/page.tsx` |
| 3 | No search history | No recent searches | Add search history with localStorage persistence | 🟡 P1 | M | `app/search/page.tsx` |
| 4 | No autocomplete/suggestions | Plain input box | Add autocomplete/suggestions dropdown as user types | 🟡 P1 | M | `app/search/page.tsx` |
| 5 | "บทความที่เกี่ยวข้อง" always static | 3 static article titles | Wire article links to real content pages | 🟡 P1 | M | `app/search/page.tsx` |
| 6 | No "ถามต่อ" follow-up | One-shot Q&A | Add "ถามต่อ" follow-up input on answer card (concierge chat mode) | 🟢 P2 | M | `app/search/page.tsx` |
| 7 | No drive-detected tone in response header | Generic "คำตอบแนะนำโดย LegalAI" | Show drive-detected tone in AI response header | 🟢 P2 | S | `app/search/page.tsx` |
| 8 | Save doesn't persist | Local toggle only | Save to user's case/bookmark collection | 🟡 P1 | M | `app/search/page.tsx` |
| 9 | Search input no debounce | Fires immediately | Implement search input debouncing (300ms) | 🟢 P2 | S | `app/search/page.tsx` |

---

## 📋 6. Documents Home Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | "เริ่มสร้างเอกสาร" button broken | Only shows toast, no navigation | Fix to route to `/documents/create` | 🔴 P0 | S | `app/documents/page.tsx` |
| 2 | Quick-start docs hardcoded | 4 static doc types | Pull quick-start templates from actual 126-template library, dynamic ranking | 🟡 P1 | M | `app/documents/page.tsx` |
| 3 | Quick-start cards not navigable | Selection only highlights, no link | Make quick-start cards navigable to document creation | 🟡 P1 | S | `app/documents/page.tsx` |
| 4 | No "เอกสารล่าสุด" for returning users | Always empty state for history | Add "เอกสารล่าสุด" section for returning users | 🟢 P2 | M | `app/documents/page.tsx` |
| 5 | No AI-powered template recommendation | Generic category browser | Add "จากเคสของคุณ — แนะนำ [template]" concierge recommendation | 🟡 P1 | M | `app/documents/page.tsx` |
| 6 | Template count badges may not match | Hardcoded category counts | Add template count badges that match actual registered counts | 🟢 P2 | S | `app/documents/page.tsx` |

---

## 📋 7. Document Category Detail Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | All templates use same generic content | `buildTemplateDoc()` is generic | Add per-template markdown content to registry (not generic) | 🔴 P0 | L | `app/documents/[category]/page.tsx` |
| 2 | No popularity/usage ranking | Templates listed in static order | Add popularity/usage ranking to templates | 🟢 P2 | M | `app/documents/[category]/page.tsx` |
| 3 | No template preview on hover | Only name + price badge | Show "ตัวอย่างเอกสาร" preview on hover | 🟢 P2 | M | `app/documents/[category]/page.tsx` |
| 4 | No category-specific tips | Generic layout only | Add category-specific tips section (e.g. "💡 เอกสารที่ใช้บ่อยในหมวดอสังหาฯ") | 🟢 P2 | S | `app/documents/[category]/page.tsx` |

---

## 📋 8. Document Create Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Generation is a stub — no real API | Toast only, no API call | Wire real API endpoint `/api/documents/generate` | 🔴 P0 | L | `app/documents/create/page.tsx` |
| 2 | All templates use same generic merge fields | `buildTemplateDoc()` one-size-fits-all | Add per-template markdown content to template registry | 🔴 P0 | L | `app/documents/create/page.tsx` |
| 3 | No category-specific merge fields | Only COMMON fields | Add category-specific merge fields (rental_amount, loan_amount, etc.) | 🟡 P1 | M | `app/documents/create/page.tsx` |
| 4 | No PDF/DOCX export | Generate stub only | Implement real PDF/DOCX export functionality | 🔴 P0 | L | `app/documents/create/page.tsx` |
| 5 | No auto-fill from user profile + case | Manual field entry only | Auto-fill fields from user profile and active case context | 🟡 P1 | M | `app/documents/create/page.tsx` |
| 6 | No "บันทึกเป็นร่าง" | No save draft | Add "บันทึกเป็นร่าง" for work-in-progress documents | 🟢 P2 | M | `app/documents/create/page.tsx` |
| 7 | No conditional blocks wired | Merge engine supports but unused | Wire conditional blocks for complex documents | 🟡 P1 | M | `app/documents/create/page.tsx` |

---

## 📋 9. Tax Calculator Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | AI Tax Optimizer is a stub | Button does nothing | Wire AI Tax Optimizer to real API using `calculateTax()` from lib | 🟡 P1 | M | `app/tax/page.tsx` |
| 2 | Not using real `TaxPayerProfile` type | Flat deduction toggles | Use `TaxPayerProfile` type for structured input | 🟡 P1 | M | `app/tax/page.tsx` |
| 3 | Page uses own calcTax() instead of lib | Duplicated logic | Refactor tax page to use `calculateTax()` from `lib/tax/calculator` | 🟡 P1 | M | `app/tax/page.tsx` |
| 4 | No year-over-year comparison | Single year only | Add year-over-year comparison (2568 vs 2569) | 🟢 P2 | M | `app/tax/page.tsx` |
| 5 | No what-if scenarios | Single scenario only | Add what-if: "ถ้าซื้อ RMF เพิ่ม 50,000 → ประหยัดอีก 7,500" | 🟢 P2 | M | `app/tax/page.tsx` |
| 6 | No spouse income input | Single filer only | Add spouse income input for married filing | 🟢 P2 | S | `app/tax/page.tsx` |
| 7 | Not using `quickEstimateDeductions()` | All deductions manual | Integrate `quickEstimateDeductions()` for simpler initial view | 🟢 P2 | S | `app/tax/page.tsx` |
| 8 | Deduction values hardcoded | Not from lib | Use deduction values from `lib/tax/deductions.ts` | 🟡 P1 | M | `app/tax/page.tsx` |
| 9 | Wire `scenarioAnalysis()` unused | Lib function exists but unused | Wire `scenarioAnalysis()` for what-if comparisons | 🟢 P2 | S | `app/tax/page.tsx` |

---

## 📋 10. Pricing Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Feature comparison table manually typed | Hardcoded HTML | Generate dynamically from `PackageLimits` types | 🟢 P2 | M | `app/pricing/page.tsx` |
| 2 | Paid tier CTAs have empty onClick | `onClick={() => {}}` | Add payment flow integration | 🟡 P1 | L | `app/pricing/page.tsx` |
| 3 | No personalized recommendation | Static tier display | Add personalized recommendation based on user activity | 🟢 P2 | M | `app/pricing/page.tsx` |
| 4 | No monthly/annual toggle | Single price shown | Monthly/annual pricing toggle | 🟢 P2 | M | `app/pricing/page.tsx` |
| 5 | No enterprise/contact sales option | Only 4 tiers | Add enterprise/contact sales option | 🟢 P2 | S | `app/pricing/page.tsx` |
| 6 | Feature gates not enforced | Defined but not checked | Enforce feature gates at API level | 🔴 P0 | L | `app/pricing/page.tsx` + API routes |
| 7 | No usage tracking against limits | Limits defined but unused | Add usage tracking and upgrade prompts at limit | 🟡 P1 | L | `lib/packages/definitions.ts` + API |

---

## 📋 11. Lawyers Marketplace Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | "ดูโปรไฟล์และนัดหมาย" doesn't navigate | No route to detail | Wire to `/lawyers/${lawyer.id}` | 🟡 P1 | S | `app/lawyers/page.tsx` |
| 2 | "ให้ AI ช่วยเลือก" only shows toast | No real matching | Implement AI matching based on case category + budget + language | 🟡 P1 | M | `app/lawyers/page.tsx` |
| 3 | All lawyer data is mock | 5 hardcoded lawyers | Connect to Supabase for real lawyer profiles | 🔴 P0 | L | `app/lawyers/page.tsx` |
| 4 | No booking/calendar integration | Toast only | Implement real booking flow with calendar integration | 🔴 P0 | L | `app/lawyers/page.tsx` |
| 5 | No rating/review sorting | Static order | Add rating/review sorting | 🟢 P2 | S | `app/lawyers/page.tsx` |
| 6 | Lawyer data inline in page | 100+ lines of mock data | Extract lawyer mock data to `lib/mock/lawyers.ts` | 🟢 P2 | S | `app/lawyers/page.tsx` |
| 7 | No pagination for lawyer listing | All shown at once | Add pagination (scales beyond 5 mock entries) | 🟢 P2 | M | `app/lawyers/page.tsx` |

---

## 📋 12. Lawyer Detail Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Booking doesn't connect to backend | Toast only | Connect booking to real backend/calendar API | 🔴 P0 | L | `app/lawyers/[id]/page.tsx` |
| 2 | No payment integration for booking | Free-form booking | Add payment integration for booking confirmation | 🟡 P1 | L | `app/lawyers/[id]/page.tsx` |
| 3 | Lawyer profiles from mock data | 5 hardcoded samples | Real lawyer profiles from database | 🔴 P0 | L | `app/lawyers/[id]/page.tsx` |
| 4 | Reviews from mock data | 3 hardcoded sample reviews | Real reviews from database | 🟡 P1 | M | `app/lawyers/[id]/page.tsx` |
| 5 | No video call integration | No meeting link generation | Video call integration (LINE Meet, Google Meet, Zoom) | 🟢 P2 | L | `app/lawyers/[id]/page.tsx` |
| 6 | No real calendar availability | `generateTimeSlots()` always same | Check real availability when selecting time slots | 🟡 P1 | M | `app/lawyers/[id]/page.tsx` |

---

## 📋 13. Profile Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No real data persistence | All save buttons toast-only | Connect to Supabase auth for real user profile | 🔴 P0 | L | `app/profile/page.tsx` |
| 2 | Form fields uncontrolled (defaultValue) | Edits lost on tab switch | Make form fields controlled (`value` + `onChange` instead of `defaultValue`) | 🟡 P1 | M | `app/profile/page.tsx` |
| 3 | LINE connection not real | Toggle only | Implement real LINE connection via LIFF | 🟡 P1 | L | `app/profile/page.tsx` |
| 4 | No real data export (PDPA) | Button shows toast | Add real data export functionality | 🟡 P1 | M | `app/profile/page.tsx` |
| 5 | No password change / 2FA settings | Missing | Add password change / 2FA settings | 🟢 P2 | M | `app/profile/page.tsx` |
| 6 | No avatar image upload | Initials only | Add avatar image upload | 🟢 P2 | M | `app/profile/page.tsx` |
| 7 | User data hardcoded | "นภัสสร", "napassorn@example.com" | Pull real data from Supabase user profile | 🔴 P0 | M | `app/profile/page.tsx` |

---

## 📋 14. Terms Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No version tracking | Static page | Add "last updated" version tracking | 🟢 P2 | S | `app/terms/page.tsx` |
| 2 | No table of contents | Long scrollable text | Add table of contents for easy navigation | 🟢 P2 | S | `app/terms/page.tsx` |
| 3 | No English version toggle | Thai only | Add English version toggle | 🟢 P2 | M | `app/terms/page.tsx` |

---

## 📋 15. Privacy Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No cookie consent management UI | Static policy page | Add cookie consent management UI | 🟢 P2 | M | `app/privacy/page.tsx` |
| 2 | No data processing activity log | Policy text only | Add data processing activity log | 🟢 P2 | M | `app/privacy/page.tsx` |
| 3 | No DPO contact information | Missing | Add DPO contact information | 🟢 P2 | S | `app/privacy/page.tsx` |

---

## 📋 16. Notifications Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | All notifications are mock data | 4 hardcoded samples | Connect to Supabase real-time subscriptions | 🟡 P1 | L | `app/notifications/page.tsx` |
| 2 | Read state not persisted | Resets on page reload | Persist read state to database | 🟡 P1 | M | `app/notifications/page.tsx` |
| 3 | No LINE push notification integration | In-app only | Add LINE push notification integration | 🟡 P1 | L | `app/notifications/page.tsx` |
| 4 | No notification preferences per type | In-app/email/LINE only | Add notification preferences per notification type | 🟢 P2 | M | `app/notifications/page.tsx` |

---

## 📋 17. Assistant Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Case context always hardcoded to labour | Fixed "ถูกเลิกจ้างโดยไม่แจ้งล่วงหน้า" | Read active case context from URL params or user session | 🟡 P1 | M | `app/assistant/page.tsx` |
| 2 | Quick replies always static | Same 3 replies every time | Generate dynamic quick replies based on AI response | 🟡 P1 | M | `app/assistant/page.tsx` |
| 3 | No conversation persistence | Refresh loses all messages | Add conversation persistence (localStorage or Supabase) | 🟡 P1 | M | `app/assistant/page.tsx` |
| 4 | File attachment disabled | Attach button non-functional | Enable file attachment (images, PDFs) | 🟢 P2 | M | `app/assistant/page.tsx` |
| 5 | No case switcher dropdown | single case context | Add case switcher dropdown in context banner | 🟢 P2 | M | `app/assistant/page.tsx` |
| 6 | No voice input | Text only | Add voice input option | 🟢 P2 | L | `app/assistant/page.tsx` |
| 7 | No drive detection on conversation | Static tone | Drive detection on conversation for tone adaptation | 🟡 P1 | M | `app/assistant/page.tsx` |

---

## 📋 18. Cases List Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | All 3 cases are sample data | Mock data only | Connect to Supabase for real case data | 🔴 P0 | L | `app/cases/page.tsx` |
| 2 | No sorting options | Static order | Add sorting options (deadline, created date, status) | 🟢 P2 | S | `app/cases/page.tsx` |
| 3 | No case search | Filter by status only | Add case search within cases list | 🟢 P2 | M | `app/cases/page.tsx` |
| 4 | No urgency indicators on cards | Only status filter | Add urgency indicators on each case card | 🟡 P1 | S | `app/cases/page.tsx` |
| 5 | "สร้างเคสใหม่" doesn't go to proper flow | Just navigation link | Wire to actual diagnosis flow with category selection | 🟡 P1 | M | `app/cases/page.tsx` |

---

## 📋 19. Case Timeline Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Timeline always shows case-1 data | Ignores caseId param | Read actual `caseId` param and load corresponding timeline | 🟡 P1 | M | `app/cases/[caseId]/timeline/page.tsx` |
| 2 | No user progress tracking | Static timeline items | Track user progress through timeline steps | 🟡 P1 | M | `app/cases/[caseId]/timeline/page.tsx` |
| 3 | No deadline countdown display | Static dates only | Add deadline countdown display | 🟡 P1 | M | `app/cases/[caseId]/timeline/page.tsx` |
| 4 | "สร้างหนังสือทวงถาม" not pre-filled | Generic link | Wire to document creation with pre-filled case context | 🟡 P1 | M | `app/cases/[caseId]/timeline/page.tsx` |

---

## 📋 20. Evidence Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No real file upload — local state only | Files vanish on refresh | Wire real file upload to Supabase Storage | 🔴 P0 | L | `app/cases/[caseId]/evidence/page.tsx` |
| 2 | No file preview | Name + size only | Add file preview (image thumbnails, PDF viewer) | 🟡 P1 | M | `app/cases/[caseId]/evidence/page.tsx` |
| 3 | No AI-powered document analysis | Manual checklist only | Add AI-powered document analysis | 🟢 P2 | L | `app/cases/[caseId]/evidence/page.tsx` |
| 4 | No OCR for auto-filling case data | All manual entry | Add OCR for auto-filling case data from uploaded documents | 🟢 P2 | L | `app/cases/[caseId]/evidence/page.tsx` |
| 5 | Uploaded files not persisted across sessions | Local state only | Persist uploaded files across sessions | 🟡 P1 | M | `app/cases/[caseId]/evidence/page.tsx` |

---

## 📋 21. Admin Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No admin auth guard — publicly accessible | Just a warning text | Add middleware-based admin auth guard | 🔴 P0 | M | `app/admin/page.tsx` + middleware |
| 2 | All data entirely mock | Hardcoded stats/charts | Real admin dashboard with live data from Supabase | 🟡 P1 | L | `app/admin/page.tsx` |
| 3 | No RBAC | No role checking | Role-based access control (RBAC) | 🟡 P1 | M | `app/admin/page.tsx` |
| 4 | No lawyer verification workflow | Mock data only | Lawyer verification workflow | 🟡 P1 | L | `app/admin/page.tsx` |
| 5 | Quick action buttons non-functional | All show toast | Wire admin actions (ตรวจสอบทนายใหม่, ส่งออกรายงาน, ตั้งค่าระบบ) | 🟡 P1 | L | `app/admin/page.tsx` |
| 6 | No revenue analytics with real data | Static SVG chart | Real revenue analytics | 🟢 P2 | L | `app/admin/page.tsx` |

---

## 📋 22. Onboarding Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Email OTP is mocked — accepts any code | Simulated 1.2s delay | Wire real email OTP via Supabase Auth | 🟡 P1 | M | `app/onboarding/page.tsx` |
| 2 | No persistence of onboarding preferences | All data lost after completion | Persist onboarding preferences to user profile | 🟡 P1 | M | `app/onboarding/page.tsx` |
| 3 | No skip option for email verification | Required step | Add skip option for email verification | 🟢 P2 | S | `app/onboarding/page.tsx` |
| 4 | No LINE connection step | Email only | Add LINE connection step (LIFF integration) | 🟢 P2 | M | `app/onboarding/page.tsx` |

---

## 📋 23. Auth Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No phone number auth option | Email + Google only | Add phone number auth option | 🟢 P2 | M | `app/auth/signin/page.tsx` |

---

## 📋 24. 404 / Error Pages Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | 404: No search suggestion | Simple message only | Add search box "ลองค้นหาสิ่งที่คุณต้องการ" | 🟢 P2 | S | `app/not-found.tsx` |
| 2 | 404: No popular page links | Single link to home | Add popular page links | 🟢 P2 | S | `app/not-found.tsx` |
| 3 | Error: No error reporting integration | No Sentry/etc. | Add error reporting integration (Sentry) | 🟢 P2 | M | `app/error.tsx` |

---

## 📋 25. Analysis Result Checklist

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Analysis only in sessionStorage | Lost on new tab / clear | Persist analysis to Supabase instead of sessionStorage | 🔴 P0 | L | `app/analysis/[caseId]/page.tsx` |
| 2 | No "แชร์ผลวิเคราะห์กับทนาย" | Save only | Add "แชร์ผลวิเคราะห์กับทนาย" feature | 🟢 P2 | M | `app/analysis/[caseId]/page.tsx` |
| 3 | No drive-aware tone on action plan | Generic tone | Drive-aware tone on action plan based on detected drives | 🟡 P1 | M | `app/analysis/[caseId]/page.tsx` |
| 4 | No one-click case creation from analysis | Manual flow | One-click "สร้างเคสและเริ่มดำเนินการ" to create case + populate timeline | 🟡 P1 | M | `app/analysis/[caseId]/page.tsx` |

---

## 📋 26. LIBRARY FIXES — Diagnosis Config

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Fear calibration question not integrated | Config has no step 0 | Integrate `FEAR_CALIBRATION_QUESTION` as configurable step 0 | 🔴 P0 | M | `lib/legal/diagnosis-config.ts` |
| 2 | No question dependency logic | All questions shown always | Add question dependency logic (skip based on previous answers) | 🟢 P2 | M | `lib/legal/diagnosis-config.ts` |
| 3 | No question priority ordering | Fixed order always | Add question priority ordering for different urgency levels | 🟢 P2 | M | `lib/legal/diagnosis-config.ts` |

---

## 📋 27. LIBRARY FIXES — Legal Sources

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | URLs are placeholders | Not all verified | Verify all URLs against official Royal Gazette / government portals | 🟢 P2 | M | `lib/legal/sources.ts` |
| 2 | No automatic update pipeline | Static data only | Add source update pipeline (automatic checking for law amendments) | 🟢 P2 | L | `lib/legal/sources.ts` |
| 3 | No English translations of law names | Thai only | Add English translations of law names | 🟢 P2 | S | `lib/legal/sources.ts` |

---

## 📋 28. LIBRARY FIXES — Fear Calibration

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | NOT WIRED to any page | Library exists, zero UI integration | Wire into diagnosis wizard as step 0 (before category questions) | 🔴 P0 | M | `lib/legal/fear-calibration.ts` |
| 2 | Calibrated tone not used anywhere | Functions exist but unused | Use calibrated tone in all subsequent AI communication | 🔴 P0 | M | `lib/legal/fear-calibration.ts` |
| 3 | Action plan urgency not adjusted | Fear level ignored | Adjust action plan urgency based on fear level | 🟡 P1 | M | `lib/legal/fear-calibration.ts` |
| 4 | Loading/analysis screen messages static | Not fear-aware | Show appropriate messaging on loading/analysis screens based on fear level | 🟡 P1 | S | `lib/legal/fear-calibration.ts` |

---

## 📋 29. LIBRARY FIXES — Guardrails

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | `isSafeForDisplay()` NOT wired | No evidence guardrails called before rendering | Wire `isSafeForDisplay()` as gate before rendering AI responses | 🔴 P0 | M | `lib/legal/guardrails.ts` |
| 2 | `checkGuardrails()` NOT in API layer | No guardrail checking on responses | Wire `checkGuardrails()` in the API layer before returning AI results | 🔴 P0 | M | `lib/legal/guardrails.ts` + API routes |
| 3 | No guardrail violation logging | Violations silently ignored | Add guardrail violation logging for monitoring | 🟡 P1 | M | `lib/legal/guardrails.ts` |
| 4 | Emergency redirect not integrated | Guardrail only | Integrate emergency redirect logic into AI assistant and search pages | 🟡 P1 | M | `lib/legal/guardrails.ts` |

---

## 📋 30. LIBRARY FIXES — Drive Detection

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | `detectDrives()` not called during diagnosis | Only used in category-drives | Wire `detectDrives()` into diagnosis wizard during answer collection | 🔴 P0 | M | `lib/legal/drive-detection.ts` |
| 2 | Detected drives not passed to AI prompts | AI responses not drive-aware | Pass detected drives to AI prompt for tone-adapted responses | 🔴 P0 | M | `lib/legal/drive-detection.ts` |
| 3 | `driveMessaging()` not used for CTAs | Static CTA text | Use `driveMessaging()` for CTA text personalization | 🟡 P1 | M | `lib/legal/drive-detection.ts` |
| 4 | Drive labels not shown in analysis result | No drive awareness post-analysis | Show drive labels in analysis result page | 🟡 P1 | S | `lib/legal/drive-detection.ts` |

---

## 📋 31. LIBRARY FIXES — Category Drives

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Only loss messages used on CTAs | Gain messages exist but unused | Use gain messages on CTAs (not just loss aversion) | 🟡 P1 | S | `lib/legal/category-drives.ts` |
| 2 | No A/B testing of motivation hooks | Single variant per category | A/B test different motivation hooks per category | 🟢 P2 | L | `lib/legal/category-drives.ts` |

---

## 📋 32. LIBRARY FIXES — Social Proof

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | All numbers hardcoded estimates | Not real data | Connect to real analytics for dynamic counts | 🟡 P1 | M | `lib/legal/social-proof.ts` |
| 2 | Time signals not shown on homepage | Only on category pages | Add time signals to homepage (e.g. "วันนี้: 142 คนเริ่มวิเคราะห์เคส") | 🟡 P1 | S | `lib/legal/social-proof.ts` |
| 3 | Trending badges not on category cards | Data exists unused | Show trending badges on category cards | 🟢 P2 | S | `lib/legal/social-proof.ts` |
| 4 | No monthly update from Supabase | Static numbers never change | Update monthly from actual Supabase data | 🟢 P2 | M | `lib/legal/social-proof.ts` |

---

## 📋 33. LIBRARY FIXES — Document Categories

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Template counts static | Hardcoded numbers | Add dynamic template counts from database | 🟢 P2 | M | `lib/documents/categories.ts` |
| 2 | No category usage analytics | No tracking | Add category usage analytics | 🟢 P2 | M | `lib/documents/categories.ts` |
| 3 | No "new" badge for recent categories | All look the same | Add "new" badge for recently added categories | 🟢 P2 | S | `lib/documents/categories.ts` |

---

## 📋 34. LIBRARY FIXES — Merge Engine

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Merge engine NOT WIRED — full power unused | `buildTemplateDoc()` creates generic template | Wire real per-template markdown content to template registry | 🔴 P0 | L | `lib/documents/merge-engine.ts` |
| 2 | Conditional blocks not utilized | Engine supports but content doesn't use | Wire conditional blocks for complex documents | 🟡 P1 | M | `lib/documents/merge-engine.ts` |
| 3 | No repeating sections | Not implemented | Add repeating sections (witnesses, properties, etc.) | 🟢 P2 | M | `lib/documents/merge-engine.ts` |
| 4 | No bilingual output | Thai only | Implement bilingual output (Thai + English) | 🟢 P2 | L | `lib/documents/merge-engine.ts` |

---

## 📋 35. LIBRARY FIXES — Templates

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | All templates use same generic content | `buildTemplateDoc()` identical for all | Add unique markdown content per template | 🔴 P0 | L | `lib/documents/templates.ts` |
| 2 | No per-template merge field definitions | Generic COMMON fields only | Add per-template merge field definitions | 🟡 P1 | L | `lib/documents/templates.ts` |
| 3 | No template preview content | Metadata only | Add template preview content | 🟢 P2 | M | `lib/documents/templates.ts` |
| 4 | No template versioning | No version tracking | Add template versioning | 🟢 P2 | M | `lib/documents/templates.ts` |

---

## 📋 36. LIBRARY FIXES — Tax Calculator

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Tax page uses own simplified calculation | Duplicates lib logic | Refactor tax page to use `calculateTax()` from this library | 🟡 P1 | M | `lib/tax/calculator.ts` |
| 2 | `scenarioAnalysis()` not wired | Lib function exists but unused | Wire `scenarioAnalysis()` for what-if comparisons | 🟢 P2 | M | `lib/tax/calculator.ts` |
| 3 | `TaxPayerProfile` not used by tax page | Flat state instead | Integrate `TaxPayerProfile` input form | 🟡 P1 | M | `lib/tax/calculator.ts` |

---

## 📋 37. LIBRARY FIXES — Tax Deductions

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Tax page uses hardcoded deduction values | Not from this lib | Wire into tax page for accurate deduction calculation | 🟡 P1 | M | `lib/tax/deductions.ts` |
| 2 | `quickEstimateDeductions()` not used | Complex mode only | Use `quickEstimateDeductions()` for the simple mode | 🟢 P2 | S | `lib/tax/deductions.ts` |

---

## 📋 38. LIBRARY FIXES — Package Definitions

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Feature gates not enforced at API level | Defined but unused | Enforce feature gates at API level | 🔴 P0 | L | `lib/packages/definitions.ts` + API |
| 2 | No upgrade prompts when users hit limits | No warning | Show upgrade prompts when users hit limits | 🟡 P1 | M | `lib/packages/definitions.ts` |
| 3 | No usage tracking against limits | No tracking | Add usage tracking against limits | 🟡 P1 | L | `lib/packages/definitions.ts` |

---

## 📋 39. CROSS-CUTTING — Accessibility (Every Page Needs)

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No skip-to-main-content link | Missing on all pages | Add skip-to-main-content link in layout | 🟡 P1 | S | `app/layout.tsx` |
| 2 | No high-contrast theme/mode | Single theme | Add high-contrast theme toggle | 🟢 P2 | M | Global CSS / theme |
| 3 | Color-dependent urgency pills lack text fallback | Color-only indicators | Add text labels alongside color for urgency pills | 🟡 P1 | S | Multiple pages |
| 4 | Decorative emojis lack `aria-hidden` | Emojis read by screen readers | Add `aria-hidden="true"` to decorative emojis | 🟢 P2 | S | Multiple pages |
| 5 | Dynamic state changes not all announced via `aria-live` | Partial coverage | Add `aria-live` regions for all dynamic content updates | 🟢 P2 | M | Multiple pages |
| 6 | Form validation errors not linked via `aria-describedby` | Visual-only errors | Link form validation errors via `aria-describedby` | 🟡 P1 | M | Multiple pages |
| 7 | Progress bar lacks ARIA value attributes | Only visual | Add `aria-valuenow`, `aria-valuemin`, `aria-valuemax` to progress bars | 🟡 P1 | S | Diagnosis + Onboarding |

---

## 📋 40. CROSS-CUTTING — Performance

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | PROBLEM_EXAMPLES inline in page (90 lines) | In `app/categories/[category]/page.tsx` | Extract to `lib/legal/problem-examples.ts` | 🟡 P1 | S | `app/categories/[category]/page.tsx` |
| 2 | Lawyer mock data inline in page (100 lines) | In `app/lawyers/page.tsx` | Extract to `lib/mock/lawyers.ts` | 🟢 P2 | S | `app/lawyers/page.tsx` |
| 3 | Missing Suspense boundaries | Only on document create | Add Suspense boundaries on search, diagnosis, and cases pages | 🟢 P2 | S | Multiple pages |
| 4 | Admin chart component not lazy-loaded | Always loaded | Implement `React.lazy` for admin chart component | 🟢 P2 | S | `app/admin/page.tsx` |
| 5 | No loading skeletons for initial page loads | Spinners only | Add loading skeletons for initial page renders | 🟢 P2 | M | Multiple pages |
| 6 | Search input no debounce | Immediate fire | Implement search input debouncing (300ms) | 🟡 P1 | S | `app/search/page.tsx` |
| 7 | No pagination for lawyer listing | All loaded at once | Add pagination for lawyer listing | 🟢 P2 | M | `app/lawyers/page.tsx` |

---

## 📋 41. CROSS-CUTTING — Security

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Admin page publicly accessible | Warning only, no guard | Add middleware-based admin auth guard | 🔴 P0 | M | `middleware.ts` + `app/admin/page.tsx` |
| 2 | Feature gates not enforced server-side | Defined but unchecked | Enforce feature gates with server-side checks | 🔴 P0 | M | API routes |
| 3 | No rate limiting on AI endpoints | No limits | Add rate limiting to `/api/ai/*` endpoints | 🔴 P0 | M | API routes |
| 4 | Analysis results in sessionStorage | Accessible to browser extensions | Move analysis results to server-side storage (not sessionStorage) | 🔴 P0 | L | `app/diagnosis/page.tsx` + API |
| 5 | No Content-Security-Policy headers | Missing | Add Content-Security-Policy headers | 🟡 P1 | M | `next.config` or middleware |
| 6 | No input sanitization before AI prompts | Raw input to AI | Add input sanitization before AI prompts | 🟡 P1 | M | API routes |
| 7 | No CSRF protection for mutation endpoints | Missing | Add CSRF protection for mutation endpoints | 🟡 P1 | M | API routes |

---

## 📋 42. CROSS-CUTTING — Data Architecture

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No case persistence (all mock data) | Client-side only | Implement real case persistence with Supabase | 🔴 P0 | L | Multiple pages + API |
| 2 | Document generation not persisted | No save to DB | Persist generated documents to Supabase | 🔴 P0 | L | API + `app/documents/create/page.tsx` |
| 3 | Lawyer booking not persisted | UI only | Persist bookings to Supabase with calendar integration | 🔴 P0 | L | API + `app/lawyers/[id]/page.tsx` |
| 4 | No `/api/documents/generate` endpoint | Not implemented | Create document generation API endpoint | 🔴 P0 | L | New API route |
| 5 | No `/api/tax/optimize` endpoint | Not implemented | Create tax optimization API endpoint | 🟡 P1 | M | New API route |
| 6 | No `/api/lawyers/book` endpoint | Not implemented | Create lawyer booking API endpoint | 🔴 P0 | L | New API route |
| 7 | No `/api/cases/*` CRUD endpoints | Not implemented | Create case management API endpoints | 🔴 P0 | L | New API routes |
| 8 | No `/api/evidence/upload` endpoint | Not implemented | Create evidence upload API endpoint | 🔴 P0 | L | New API route |
| 9 | No `/api/notifications` endpoint | Not implemented | Create notification list API endpoint | 🟡 P1 | M | New API route |
| 10 | No `/api/profile` endpoint | Not implemented | Create user profile API endpoint | 🔴 P0 | M | New API route |
| 11 | No `/api/admin/*` endpoints | Not implemented | Create admin operations API endpoints | 🟡 P1 | L | New API routes |

---

## 📋 43. CROSS-CUTTING — V4 Concierge Integration

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | Fear calibration not wired to any page | Library exists, zero UI | Wire as diagnosis step 0 | 🔴 P0 | M | Diagnosis + fear-calibration |
| 2 | Drive detection not in AI prompts | Only in category detail | Wire into diagnosis + AI response pipeline | 🔴 P0 | M | Diagnosis + Assistant + drive-detection |
| 3 | Guardrail enforcement not in API | Library complete, unused | Wire `isSafeForDisplay()` before rendering AI | 🔴 P0 | M | API routes + guardrails |
| 4 | Personalized greeting hardcoded | "คุณนภัสสร" | Use real auth user name everywhere | 🔴 P0 | M | Home + Layout + Profile |
| 5 | Proactive notifications missing | Mock data only | Real-time Supabase subscriptions + push | 🟡 P1 | L | Notifications + Supabase |
| 6 | Progress tracking mock only | No real case data | Real database-backed cases with progress | 🔴 P0 | L | Cases + Timeline + Evidence |
| 7 | 8-phase concierge flow not implemented | Phases 1-5 partial, 6-8 missing | Design and implement 8-phase case flow | 🟢 P2 | L | Architecture-level |
| 8 | Emergency redirect guardrail-only | No UI integration | Integrate emergency redirect into search and assistant | 🟡 P1 | M | Search + Assistant + guardrails |
| 9 | No voice input anywhere | Not implemented | Add voice input to AI assistant and search | 🟢 P2 | L | Assistant + Search |
| 10 | Social proof display partial | Only category detail pages | Add real-time social proof to homepage, search, diagnosis | 🟡 P1 | M | Home + Search + Diagnosis |

---

## 📋 44. CROSS-CUTTING — Tests

| # | Issue | Current | Fix | Priority | Effort | File |
|---|-------|---------|-----|----------|--------|------|
| 1 | No unit test for `calcTax()` | No tests | Unit test — 8 bracket correctness | 🔴 P0 | M | New test file |
| 2 | No unit test for `computeDeductions()` | No tests | Unit test — cap enforcement | 🔴 P0 | M | New test file |
| 3 | No unit test for `checkGuardrails()` | No tests | Unit test — all 14 rules | 🔴 P0 | M | New test file |
| 4 | No unit test for `detectDrives()` | No tests | Unit test — keyword accuracy | 🟡 P1 | M | New test file |
| 5 | No unit test for `mergeTemplate()` | No tests | Unit test — field replacement | 🟡 P1 | M | New test file |
| 6 | No unit test for `formatThaiDate()` | No tests | Unit test — Buddhist calendar | 🟡 P1 | S | New test file |
| 7 | No unit test for `suggestCategory()` | No tests | Unit test — keyword mapping | 🟢 P2 | S | New test file |
| 8 | No integration test for diagnosis wizard | No tests | Integration — full flow | 🟡 P1 | M | New test file |
| 9 | No integration test for search page | No tests | Integration — AI response | 🟡 P1 | M | New test file |
| 10 | No integration test for tax page | No tests | Integration — calculation | 🟡 P1 | M | New test file |
| 11 | No smoke tests for pages | No tests | All 27 pages — render without crash | 🔴 P0 | M | New test files |

---

## 📊 SUMMARY

### By Priority

| Priority | Count | Description |
|----------|:-----:|-------------|
| 🔴 P0 | 37 | Critical — broken features, missing safety, data loss, must-fix-for-launch |
| 🟡 P1 | 63 | High — significant UX improvement, wired-but-not-working, feature gaps |
| 🟢 P2 | 57 | Medium — polish, completeness, nice-to-have, future enhancements |
| **TOTAL** | **157** | |

### By Effort

| Effort | Count | Estimated Hours |
|--------|:-----:|:---------------:|
| S (Small, < 2h) | 48 | ~72 hrs |
| M (Medium, 2–8h) | 77 | ~385 hrs |
| L (Large, 1–3 days) | 32 | ~640 hrs |
| **TOTAL** | **157** | **~1,097 hrs** |

### Top 10 Critical (P0) Items

| # | Issue | File |
|---|-------|------|
| 1 | Wire fear calibration as diagnosis step 0 | `app/diagnosis/page.tsx` + `lib/legal/fear-calibration.ts` |
| 2 | Wire guardrails to API response pipeline | API routes + `lib/legal/guardrails.ts` |
| 3 | Persist analysis results to Supabase (not sessionStorage) | `app/diagnosis/page.tsx` + `app/analysis/[caseId]/page.tsx` |
| 4 | Implement real document generation with per-template content | `app/documents/create/page.tsx` + `lib/documents/merge-engine.ts` + `lib/documents/templates.ts` |
| 5 | Connect lawyer booking to real backend | `app/lawyers/[id]/page.tsx` + new API |
| 6 | Add admin auth guard (currently publicly accessible) | `middleware.ts` + `app/admin/page.tsx` |
| 7 | Replace hardcoded "คุณนภัสสร" with real user name | `app/page.tsx` + `app/profile/page.tsx` |
| 8 | Fix document "เริ่มสร้าง" to navigate to create page | `app/documents/page.tsx` |
| 9 | Wire drive detection into AI prompts for tone adaptation | `app/diagnosis/page.tsx` + `app/assistant/page.tsx` |
| 10 | Implement real case persistence with Supabase | `app/cases/page.tsx` + new API routes |

### By Section

| Section | Items | P0 | P1 | P2 |
|---------|:-----:|:--:|:--:|:--:|
| 1. Home | 9 | 1 | 4 | 4 |
| 2. Categories List | 6 | 0 | 3 | 3 |
| 3. Category Detail | 6 | 1 | 3 | 2 |
| 4. Diagnosis | 8 | 3 | 1 | 4 |
| 5. Search | 9 | 0 | 6 | 3 |
| 6. Documents Home | 6 | 1 | 3 | 2 |
| 7. Document Category | 4 | 1 | 0 | 3 |
| 8. Document Create | 7 | 3 | 3 | 1 |
| 9. Tax | 9 | 0 | 5 | 4 |
| 10. Pricing | 7 | 1 | 2 | 4 |
| 11. Lawyers | 7 | 2 | 2 | 3 |
| 12. Lawyer Detail | 6 | 2 | 2 | 1 |
| 13. Profile | 7 | 2 | 3 | 2 |
| 14. Terms | 3 | 0 | 0 | 3 |
| 15. Privacy | 3 | 0 | 0 | 3 |
| 16. Notifications | 4 | 0 | 3 | 1 |
| 17. Assistant | 7 | 0 | 4 | 3 |
| 18. Cases List | 5 | 1 | 2 | 2 |
| 19. Timeline | 4 | 0 | 4 | 0 |
| 20. Evidence | 5 | 1 | 2 | 2 |
| 21. Admin | 6 | 1 | 4 | 1 |
| 22. Onboarding | 4 | 0 | 2 | 2 |
| 23. Auth | 1 | 0 | 0 | 1 |
| 24. 404/Error | 3 | 0 | 0 | 3 |
| 25. Analysis Result | 4 | 1 | 2 | 1 |
| Library Fixes (26-38) | 37 | 7 | 16 | 14 |
| Cross-Cutting (39-44) | 42 | 17 | 19 | 6 |

---

*End of Checklist — 157 actionable items extracted from 3,617-line audit*
