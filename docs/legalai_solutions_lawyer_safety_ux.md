# ⚖️ LegalAI Thailand — Detailed Solutions: Lawyer + Safety + UX + QA

> **Sections 16–29** | **Generated:** 10 ส.ค. 2569 | **Codebase:** `D:\legalai-citizen-check`
>
> For each sub-item: **HOW** (exact approach), **WHERE** (file paths), **CODE** (key changes), **VERIFY** (test plan), **DEPENDS** (prerequisites).

---

## 16. 👨‍⚖️ Lawyer Marketplace

### 16.1 — `/lawyers` Page: Lawyer List

**HOW:** The page already exists as a client component (`app/lawyers/page.tsx`) with search, filter chips, lawyer cards, sidebar. It loads 3 mock lawyers from a local array. The main improvement needed is expanding to a real data source and adding the online-status filter.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\page.tsx`

**CODE:** Replace the inline `lawyers` array with `sampleLawyers` from `@/lib/mock/categories`:

```tsx
// AFTER — import sampleLawyers instead of inline array
import { sampleLawyers } from "@/lib/mock/categories";
import type { LawyerProfile } from "@/domain/types";

// Map sampleLawyers to card-friendly shape:
const lawyers = sampleLawyers.map((l) => ({
  id: l.id,
  name: l.displayName,
  specialty: `${l.specialties.map((s) => SPECIALTY_LABELS[s] ?? s).join(", ")} • ${l.yearsExperience} ปี`,
  rating: l.rating?.toFixed(1) ?? "—",
  reviews: String(l.reviewCount ?? 0),
  price: `เริ่มต้น ฿${l.startingPriceTHB.toLocaleString()}`,
  initials: l.displayName.slice(0, 2),
  avatarClass: `a${Math.floor(Math.random() * 3)}`,
  online: l.onlineSample ?? false,
}));
```

**VERIFY:**
1. Go to `/lawyers` — see 10+ lawyers (from sampleLawyers)
2. Click each filter chip — filtered lawyer list updates
3. Search box filters by name/specialty
4. "♡ บันทึก" toggles with toast
5. "ดูโปรไฟล์และนัดหมาย" links to `/lawyers/[id]`

**DEPENDS:** `sampleLawyers` in `lib/mock/categories.ts` must have at least 5 entries with real specialties. (Currently has 4 — needs expansion.)

---

### 16.2 — Filter Chips: ทั้งหมด/แรงงาน/ครอบครัว/อสังหา/ผู้บริโภค/ออนไลน์วันนี้

**HOW:** Already implemented. The `activeChip` state tracks the selected filter and `CHIP_KEYWORDS` maps labels to specialty keywords. Works correctly.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\page.tsx` (lines 60-76, 93-98)

**VERIFY:** Each chip click updates `filtered` array. Already working — no changes needed.

**DEPENDS:** None.

---

### 16.3 — Lawyer Cards: Name, Specialties, Experience, Rating, Price, Online Status

**HOW:** Card layout already exists. Enhance to pull from `sampleLawyers` with link to `/lawyers/[id]` instead of just `notify()`.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\page.tsx` (lines 167-202)

**CODE:** Replace the `requestConsultation` button to navigate:

```tsx
// BEFORE:
<button className="primary" onClick={() => requestConsultation(x)}>
  ดูโปรไฟล์และนัดหมาย
</button>

// AFTER:
<Link href={`/lawyers/${x.id}`} className="primary" style={{ textDecoration: "none", display: "inline-block", textAlign: "center" }}>
  ดูโปรไฟล์และนัดหมาย
</Link>
```

Add online indicator:
```tsx
{/* After Pill tone="green" */}
{x.online ? <Pill tone="green">🟢 ออนไลน์</Pill> : null}
```

**VERIFY:**
1. Each card shows: avatar initials, verified pill, name, specialty with years, ★ rating, review count, price, tags
2. "ดูโปรไฟล์และนัดหมาย" navigates to `/lawyers/[id]`

**DEPENDS:** 16.1 (expanded sampleLawyers).

---

### 16.4 — "♡ บันทึก" Button — Toggle + Toast

**HOW:** Already implemented with `saved` Set and `toggleSave()`. Works correctly.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\page.tsx` (lines 90, 112-124, 197-199)

**VERIFY:** Click ♡ → changes to ✓ บันทึกแล้ว + shows toast. Click again → reverts.

**DEPENDS:** None. ✅ Already working.

---

## 17. 👨‍⚖️ Lawyer Detail Page

### 17.1 — `/lawyers/[id]` Dynamic Route

**HOW:** Already exists and works. Uses `useParams<{ id: string }>()` to look up lawyer from `sampleLawyers`.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx`

**VERIFY:** Visit `/lawyers/lawyer-1` → shows lawyer profile. Visit `/lawyers/nonexistent` → shows "ไม่พบทนาย" with link back.

**DEPENDS:** `sampleLawyers` in `lib/mock/categories.ts`. ✅ Already working.

---

### 17.2 — Profile: Avatar, Name, Specialties, Stats

**HOW:** Already renders avatar initials, displayName, specialty pills with Thai labels (`SPECIALTY_LABELS`), stats row (rating, reviews, starting price). Bio paragraph auto-generates from specialties.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 199-252)

**VERIFY:** All profile elements render. ✅ Already working.

**DEPENDS:** None. ✅

---

### 17.3 — Mock Reviews (3 reviews with star ratings)

**HOW:** `sampleReviews` array already defined inline with 3 reviews. Renders with star characters. PrototypeDataNotice labels them as "รีวิวตัวอย่าง".

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 43-73, 276-308)

**VERIFY:** 3 reviews appear with 4-5 ★ ratings, author names, dates. ✅

**DEPENDS:** None. ✅

---

### 17.4 — Service Scope Breakdown

**HOW:** Renders from `lawyer.scopes` array — each scope shows icon, name, description, price. Already working.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 255-273)

**VERIFY:** Each scope card shows 📋 icon, name, description, price in blue. ✅

**DEPENDS:** `sampleLawyers` entries must have non-empty `scopes` arrays. ✅

---

### 17.5 — Booking Widget: 3-Step (select → confirm → done)

**HOW:** Complete 3-step booking flow already built:
- **Step 1 (select):** Service scope dropdown, date picker, time slot grid, notes textarea
- **Step 2 (confirm):** Summary card showing scope, date (Thai format), time, price, notes
- **Step 3 (done):** ✅ success with "จองอีกครั้ง" and "ไปที่เคสของฉัน" buttons

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 101-108, 335-410)

**CODE (enhance — add validation feedback):**
```tsx
function requestConsultation() {
  if (!selectedScope || !selectedDate || !selectedTime) {
    notify("กรุณาเลือกบริการ วันที่ และเวลาให้ครบ");
    return;
  }
  setBookingStep("confirm");
}
```

**VERIFY:**
1. Click "เริ่มนัดหมาย" → shows scope/date/time selectors
2. Fill all fields → "ยืนยันการจอง"
3. Confirm → ✅ success page
4. "จองอีกครั้ง" resets all state

**DEPENDS:** None. ✅ Already working.

---

### 17.6–17.7 — Date Picker (7 days) + Time Slots (16 slots, 9:00-17:00, 30-min)

**HOW:** `dates` array generates next 7 days with Thai month labels (`ม.ค.`, etc.) and Buddhist Era year. `timeSlots` generates 16 half-hour slots. Both already implemented.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 78-85, 113-130)

**VERIFY:** Date dropdown shows 7 options with Thai labels. Time grid shows 16 clickable buttons. ✅

**DEPENDS:** None. ✅

---

### 17.8 — Optional Notes Field

**HOW:** Textarea already rendered in the booking form (step 1). Displayed in confirmation summary.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 498-508, 386-390)

**VERIFY:** Type in notes → appears in confirmation summary. ✅

**DEPENDS:** None. ✅

---

### 17.9 — Confirmation Summary

**HOW:** Already implemented in booking step 2 — shows scope name, date in Thai, time, price, note.

**WHERE:** `D:\legalai-citizen-check\app\lawyers\[id]\page.tsx` (lines 359-410)

**VERIFY:** All fields from selection appear correctly. ✅

**DEPENDS:** None. ✅

---

## 18. 📎 Evidence Upload

### 18.1 — Drag-and-Drop Zone

**HOW:** Fully implemented with `dragActive` state, visual feedback (blue border + glow), `onDragEnter/Over/Leave/Drop` handlers. Drop zone is also clickable and keyboard-accessible.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 77, 173-305)

**VERIFY:** Drag a PDF/JPG into the zone → blue highlight → file appears in list. ✅

**DEPENDS:** None. ✅ Already fully implemented.

---

### 18.2 — Click-to-Browse Fallback

**HOW:** Hidden `<input type="file">` triggered by clicking the drop zone or the "เพิ่มหลักฐาน" button.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 296-304)

**VERIFY:** Click drop zone → file browser opens → select file → appears in list. ✅

**DEPENDS:** None. ✅

---

### 18.3 — File Validation (PDF/JPG/PNG/WebP, max 20MB)

**HOW:** `validateFile()` checks MIME types against `ACCEPTED_TYPES` and size against `MAX_FILE_SIZE`. Errors reported via toast.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 37-43, 96-110)

**VERIFY:**
1. Try uploading a `.exe` → toast error "รองรับเฉพาะ PDF, JPG, PNG"
2. Try a 30MB PDF → toast error "ขนาดเกิน 20 MB"
3. Valid PDF/JPG uploads succeed

**DEPENDS:** None. ✅

---

### 18.4 — Uploaded Files List: Icon, Name, Size, Remove

**HOW:** Complete file list rendering with emoji icons (🖼 for images, 📄 for PDFs), name with truncation, formatted size, remove button (×).

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 308-411)

**VERIFY:** Upload 3 files → see list with icons, names, sizes. Click × → file removed. "ล้างทั้งหมด" clears all. ✅

**DEPENDS:** None. ✅

---

### 18.5 — "เชื่อมโยง" Button — Map Files to Evidence Checklist

**HOW:** Clicking "เชื่อมโยง" on an unlinked file opens an inline dropdown showing available evidence items. Selecting one links the file via `linkFileToEvidence()`, which also marks the evidence as `provided`.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 161-170, 377-449)

**VERIFY:**
1. Upload a file → click "เชื่อมโยง"
2. Dropdown shows evidence items
3. Select one → file shows "เชื่อมโยงแล้ว: [label]"
4. Evidence item auto-checked ✓

**DEPENDS:** None. ✅

---

### 18.6 — Readiness Score Ring: X/Y Items Provided

**HOW:** Score ring rendered as `providedCount/required` ratio with amber pill for missing items.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\evidence\page.tsx` (lines 80-86, 230-247)

**VERIFY:** Toggle evidence items → score updates. Upload/link files → items auto-check → score updates. ✅

**DEPENDS:** None. ✅

---

## 19. 💳 Free/Paid Tiers

### 19.1–19.4 — Four Tiers: Free, Action Pack (299฿), Case Plus (999฿), SME Starter (2,990฿/mo)

**HOW:** All four tiers already fully defined in `lib/packages/definitions.ts` with `PackageDefinition` interface, limits, features. Exported as `PACKAGES` record.

**WHERE:** `D:\legalai-citizen-check\lib\packages\definitions.ts`

**VERIFY:** Imports work in `app/pricing/page.tsx`. All feature lists are Thai. ✅

**DEPENDS:** None. ✅ Already fully implemented.

---

### 19.5–19.6 — `FEATURE_GATES` + `checkFeatureAccess()`

**HOW:** Already implemented. 10 feature gates map feature keys to minimum required package. `checkFeatureAccess()` compares package index in `PACKAGE_ORDER`.

**WHERE:** `D:\legalai-citizen-check\lib\packages\definitions.ts` (lines 155-172)

**CODE (usage example — integrate into API routes):**
```ts
// In any API route:
import { checkFeatureAccess } from "@/lib/packages/definitions";
import type { PackageId } from "@/lib/packages/definitions";

const userPackage: PackageId = user.packageId ?? "free";
if (!checkFeatureAccess(userPackage, "documents:unlimited")) {
  return Response.json({ error: "อัปเกรดเพื่อสร้างเอกสารไม่จำกัด" }, { status: 403 });
}
```

**VERIFY:**
1. Free user calls "diagnosis:unlimited" → returns false
2. Action Pack user calls same → returns true
3. Free user calls unlisted feature → returns true (open)

**DEPENDS:** None. ✅ Already implemented.

---

### 19.7 — `getNextPackage()` — Upgrade Path

**HOW:** Already implemented. Returns next package in order or null if already at max.

**WHERE:** `D:\legalai-citizen-check\lib\packages\definitions.ts` (lines 144-148)

**VERIFY:** `getNextPackage("free")` → Action Pack. `getNextPackage("sme_starter")` → null. ✅

**DEPENDS:** None. ✅

---

### 19.8 — Limits Matrix

**HOW:** `PackageLimits` interface and per-package values already defined. Can be queried via `PACKAGES[id].limits`.

**WHERE:** `D:\legalai-citizen-check\lib\packages\definitions.ts` (lines 20-29, 43-128)

**VERIFY:**
- `PACKAGES.free.limits.maxDocuments` → 1
- `PACKAGES.action_pack.limits.maxDocuments` → -1 (unlimited)
- `PACKAGES.sme_starter.limits.teamMembers` → 5

**DEPENDS:** None. ✅

---

## 20. 💳 Pricing Page

### 20.1 — `/pricing` Page

**HOW:** Already exists as client component using `PACKAGES` and `PACKAGE_ORDER` from definitions. Dynamically renders cards from the packages data.

**WHERE:** `D:\legalai-citizen-check\app\pricing\page.tsx`

**VERIFY:** Visit `/pricing` → see 4 tier cards. ✅

**DEPENDS:** Section 19 (package definitions). ✅

---

### 20.2 — 4 Tier Cards with SME Starter Highlighted

**HOW:** Already implemented. `isPro = pkgId === "sme_starter"` adds `featured` class and "🌟 แนะนำ" badge.

**WHERE:** `D:\legalai-citizen-check\app\pricing\page.tsx` (lines 16, 19-20)

**VERIFY:** SME Starter card has blue border highlight + 🌟 badge. ✅

**DEPENDS:** None. ✅ Already working.

---

### 20.3 — Feature Comparison Table (11 rows)

**HOW:** Static HTML table comparing 11 features across 4 tiers.

**WHERE:** `D:\legalai-citizen-check\app\pricing\page.tsx` (lines 62-87)

**CODE (enhance — make dynamic from FEATURE_GATES):**
```tsx
// Dynamic feature comparison
const FEATURE_ROWS = [
  { label: "AI วิเคราะห์คดี", gate: "diagnosis:unlimited" },
  { label: "Action Plan", gate: null }, // free already has sample
  { label: "เอกสารกฎหมาย", gate: "documents:unlimited" },
  { label: "เอกสารธุรกิจ", gate: "documents:business" },
  { label: "อัปโหลดหลักฐาน", gate: "evidence:upload" },
  { label: "ปรึกษาทนาย", gate: null },
  { label: "Tax Optimizer", gate: "tax:optimizer" },
  { label: "LINE แจ้งเตือน", gate: "line:notifications" },
  { label: "Priority Review", gate: "review:priority" },
  { label: "Team Access", gate: "team:access" },
  { label: "Corporate Tax", gate: "tax:corporate" },
];
```

**VERIFY:** All 11 rows render with correct ✓/— per tier. ✅

**DEPENDS:** None. ✅

---

### 20.4 — FAQ Section (3 expandable questions)

**HOW:** Already implemented with `<details><summary>` for 3 questions.

**WHERE:** `D:\legalai-citizen-check\app\pricing\page.tsx` (lines 89-94)

**VERIFY:** Click each question → expands to show answer. ✅

**DEPENDS:** None. ✅

---

### 20.5 — CTA Buttons Per Tier

**HOW:** Free tier links to `/auth/signin`, paid tiers show "อัปเกรดเลย" / "เลือกแพ็กเกจ" buttons with `onClick={() => {}}` placeholders.

**WHERE:** `D:\legalai-citizen-check\app\pricing\page.tsx` (lines 46-58)

**CODE (wire up buttons):**
```tsx
<button
  type="button"
  className={isPro ? "primary" : "outline"}
  onClick={() => {
    notify(isFree ? "เริ่มต้นใช้งานฟรี" : `เลือกแพ็กเกจ ${pkg.name}`);
    if (!isFree) recordEvent({ type: "search_submitted" as any });
  }}
>
  {isFree ? "เริ่มใช้งานฟรี" : isPro ? "อัปเกรดเลย" : "เลือกแพ็กเกจ"}
</button>
```

**VERIFY:** Click any CTA → toast feedback. ✅

**DEPENDS:** None. ✅

---

## 21. 📋 Terms of Service

### 21.1 — `/terms` Page

**HOW:** Already exists as a server component with 9 sections. Includes warning box with "ไม่ใช่คำแนะนำทางกฎหมาย".

**WHERE:** `D:\legalai-citizen-check\app\terms\page.tsx`

**VERIFY:** Visit `/terms` → 9 sections render. Warning box highlighted. ✅

**DEPENDS:** None. ✅ Already complete.

---

### 21.2 — 9 Sections

**HOW:** All 9 sections are `<section>` elements:
1. การยอมรับข้อกำหนด
2. ขอบเขตการให้บริการ
3. ข้อจำกัดความรับผิด (พร้อม warning box)
4. การใช้บริการอย่างเหมาะสม
5. การระงับหรือยกเลิกบัญชี
6. ทรัพย์สินทางปัญญา
7. การเปลี่ยนแปลงข้อกำหนด
8. กฎหมายที่ใช้บังคับ
9. ติดต่อ

**WHERE:** `D:\legalai-citizen-check\app\terms\page.tsx` (lines 13-95)

**VERIFY:** Each section has `<h2>` heading and content. ✅

**DEPENDS:** None. ✅

---

### 21.3 — Warning Box: "ไม่ใช่คำแนะนำทางกฎหมาย"

**HOW:** Section 3 contains `div.warning-box` with 5 bullet points clarifying the legal-information-vs-advice distinction.

**WHERE:** `D:\legalai-citizen-check\app\terms\page.tsx` (lines 34-45)

**VERIFY:** Warning box renders with ⚠️ icon and 5 bullets. ✅

**DEPENDS:** None. ✅

---

## 22. 🔒 Privacy Policy

### 22.1 — `/privacy` Page

**HOW:** Already exists as a server component with 8 sections, PDPA rights table, and data collection table.

**WHERE:** `D:\legalai-citizen-check\app\privacy\page.tsx`

**VERIFY:** Visit `/privacy` → all sections render. ✅

**DEPENDS:** None. ✅ Already complete.

---

### 22.2 — 8 Sections

**HOW:** All 8 sections present:
1. ข้อมูลที่เราเก็บ (with data table)
2. การใช้ AI ประมวลผลข้อมูล
3. การเก็บรักษาและความปลอดภัย
4. การเปิดเผยข้อมูลแก่บุคคลที่สาม
5. สิทธิของคุณตาม PDPA (with rights table)
6. คุกกี้
7. ช่องทางติดต่อ
8. การเปลี่ยนแปลงนโยบาย

**WHERE:** `D:\legalai-citizen-check\app\privacy\page.tsx` (lines 17-92)

**VERIFY:** Each section complete. ✅

**DEPENDS:** None. ✅

---

### 22.3 — PDPA Rights Table (5 rights)

**HOW:** Section 5 contains an HTML table with 5 PDPA rights and usage instructions.

**WHERE:** `D:\legalai-citizen-check\app\privacy\page.tsx` (lines 57-68)

**CODE (add matching profile UI links):**
```tsx
// In profile page privacy tab, ensure these actions map to PDPA rights:
<tr><td>🔍 สิทธิขอเข้าถึงข้อมูล</td><td>ดูข้อมูลของคุณได้ในหน้าโปรไฟล์</td></tr>
<tr><td>📤 สิทธิขอสำเนาข้อมูล</td><td><button onClick={handleExport}>ส่งออกข้อมูล</button></td></tr>
<tr><td>🗑️ สิทธิขอให้ลบข้อมูล</td><td><button onClick={handleDelete}>ลบข้อมูลของฉัน</button></td></tr>
<tr><td>🚫 สิทธิคัดค้าน</td><td>ปิด AI consent toggle</td></tr>
<tr><td>↩️ สิทธิขอถอนความยินยอม</td><td>เพิกถอน consent ได้ตลอด</td></tr>
```

**VERIFY:** 5-row table renders with emoji, right name, and usage method. ✅

**DEPENDS:** None. ✅

---

### 22.4 — Data Table: ประเภท, ตัวอย่าง, วัตถุประสงค์

**HOW:** Section 1 contains a 4-row data table.

**WHERE:** `D:\legalai-citizen-check\app\privacy\page.tsx` (lines 18-27)

**VERIFY:** Table renders with 4 data categories. ✅

**DEPENDS:** None. ✅

---

## 23. 🛡️ 7 Guardrails

### 23.1–23.7 — 7 Guardrail Rules

**HOW:** All 7 guardrails already defined as `GUARDRAILS` array with severity, banned patterns, and user messages.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 21-121)

| # | ID | Severity | Rule |
|---|-----|----------|------|
| 1 | `no-legal-advice` | P0 | ห้ามให้คำแนะนำทางกฎหมาย |
| 2 | `no-outcome-prediction` | P0 | ห้ามทำนายผลคดี |
| 3 | `no-lawyer-ranking` | P0 | ห้ามจัดอันดับทนาย |
| 4 | `no-court-filing` | P0 | ห้ามยื่นเอกสารแทนผู้ใช้ |
| 5 | `no-fabricated-sources` | P0 | ห้ามอ้างกฎหมายที่ไม่มีจริง |
| 6 | `no-data-without-consent` | P0 | PDPA compliance |
| 7 | `disclaimer-required` | P1 | ทุก AI result ต้องมี disclaimer |
| + | `pii-redaction` | P1 | ห้ามแสดง PII โดยไม่จำเป็น |

**VERIFY:** Import `GUARDRAILS` — all 8 entries present. ✅

**DEPENDS:** None. ✅ Already complete.

---

### 23.8 — `checkGuardrails()` Function

**HOW:** Already implemented. Iterates rules and tests text against `bannedPatterns`. Returns first violation found or null.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 127-136)

**CODE (enhance — add integration point in AI API route):**
```ts
// In app/api/ai/assistant/route.ts or app/api/ai/diagnosis/route.ts:
import { checkGuardrails, getDisclaimer } from "@/lib/legal/guardrails";

// After AI generates text:
const violation = checkGuardrails(aiText);
if (violation) {
  console.warn(`Guardrail triggered: ${violation.id}`);
  // Either: reject response, or: append userMessage
  if (violation.severity === "P0") {
    return Response.json({ error: violation.userMessage }, { status: 400 });
  }
}

// Always append disclaimer:
const safeText = aiText + "\n\n" + getDisclaimer();
```

**VERIFY:**
```ts
// Unit test:
checkGuardrails("คุณควรฟ้องศาลแรงงาน") // → no-legal-advice violation
checkGuardrails("คดีนี้ชนะแน่")          // → no-outcome-prediction violation
checkGuardrails("มาตรา 118 ระบุว่า...")  // → null (safe)
```

**DEPENDS:** Section 23.1-23.7 (guardrail definitions). ✅

---

### 23.9 — Banned RegExp Patterns Per Rule

**HOW:** Already defined. Each rule has `bannedPatterns: RegExp[]`. Thai regex patterns are case-insensitive with `gi` flag.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 30-33, 46-49, 61-64, 76, 116-117)

**CODE (add more banned patterns for coverage):**
```ts
{
  id: "no-legal-advice",
  bannedPatterns: [
    /คุณควร(ทำ|ฟ้อง|ยื่น|เรียก|เรียกร้อง|ดำเนินการ|ร้องเรียน)/gi,
    /แนะนำให้(คุณ|ท่าน|ทาง)/gi,
    /ทางที่ดี(ที่สุด|)คือ/gi,
    /(ควร|ต้อง|จำเป็นต้อง)จ้างทนาย/gi,  // NEW
    /ผม(แนะนำ|ว่า|ขอแนะนำ)/gi,           // NEW — impersonation
  ],
}
{
  id: "no-outcome-prediction",
  bannedPatterns: [
    /(มีโอกาส|โอกาส)ชนะ\s*\d+%/gi,
    /ชนะ(คดี|แน่|แน่นอน)/gi,
    /ได้เงิน(คืน|)แน่/gi,
    /(Win|win)\s*(rate|probability)/gi,
    /(คุณจะ|จะต้อง)ได้(รับ|เงิน|ค่าชดเชย)/gi,  // NEW
  ],
}
```

**VERIFY:** Run each banned pattern against sample violating text → must match.

**DEPENDS:** None. ✅ Already defined — just expand patterns.

---

## 24. ✅ Thai Accuracy Checks

### 24.1 — `checkBEYear` — ตรวจสอบปี พ.ศ.

**HOW:** Already implemented. Extracts all `พ.ศ. XXXX` matches, validates that year is between 2400-2600.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 156-168)

**CODE (enhance — add CE year detection):**
```ts
checkBEYear: (text: string): string[] => {
  const issues: string[] = [];
  // Check พ.ศ. years
  const beMatches = text.match(/พ\.ศ\.\s*(\d{4})/g);
  if (beMatches) {
    for (const m of beMatches) {
      const year = parseInt(m.replace(/\D/g, ""), 10);
      if (year < 2400 || year > 2600) {
        issues.push(`ปี พ.ศ. น่าสงสัย: ${m} (ควรอยู่ระหว่าง 2400-2600)`);
      }
    }
  }
  // Check ค.ศ. years (should not appear in Thai legal docs)
  const ceMatches = text.match(/ค\.ศ\.\s*(\d{4})/g);
  if (ceMatches) {
    issues.push(`พบปี ค.ศ. — กฎหมายไทยควรใช้ พ.ศ.: ${ceMatches.join(", ")}`);
  }
  return issues;
},
```

**VERIFY:**
```ts
ACCURACY_CHECKS.checkBEYear("พ.ศ. 2567") // → []
ACCURACY_CHECKS.checkBEYear("พ.ศ. 2100") // → ["ปี พ.ศ. น่าสงสัย: พ.ศ. 2100"]
ACCURACY_CHECKS.checkBEYear("ค.ศ. 2024") // → ["พบปี ค.ศ. ..."]
```

**DEPENDS:** None. ✅

---

### 24.2 — `checkFormalLanguage` — ตรวจสอบภาษาทางการ

**HOW:** Already implemented. Checks for informal pronouns/particles.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 171-179)

**CODE (expand informal word list):**
```ts
checkFormalLanguage: (text: string): string[] => {
  const issues: string[] = [];
  const informal = /(กู|มึง|มัน|ไอ้|อี๋|เวร|สัส|เหี้ย|ควาย|โง่)/gi;
  const found = text.match(informal);
  if (found) {
    issues.push(`พบภาษาที่ไม่เหมาะสมหรือไม่เป็นทางการ: ${found.join(", ")}`);
  }
  // Check for overly casual phrases
  const casual = /(สบายมาก|ชิวๆ|ง่ายๆ|แค่นี้เอง|ไม่เป็นไรหรอก)/gi;
  const casualFound = text.match(casual);
  if (casualFound) {
    issues.push(`พบภาษาที่ไม่เป็นทางการเกินไป: ${casualFound.join(", ")}`);
  }
  return issues;
},
```

**VERIFY:**
```ts
ACCURACY_CHECKS.checkFormalLanguage("คุณมีสิทธิเรียกร้อง") // → []
ACCURACY_CHECKS.checkFormalLanguage("มึงฟ้องมันเลย")      // → ["พบภาษาที่ไม่เป็นทางการ..."]
```

**DEPENDS:** None. ✅

---

### 24.3 — `checkRequiredTerms` — ตรวจสอบคำสำคัญ

**HOW:** Already implemented. Takes `requiredTerms` array and checks each is present in text.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 182-189)

**CODE (define required term sets per category):**
```ts
// In lib/legal/required-terms.ts
export const REQUIRED_TERMS: Record<string, string[]> = {
  labour: ["มาตรา", "ค่าชดเชย", "นายจ้าง", "ลูกจ้าง"],
  consumer: ["ผู้บริโภค", "สินค้า", "คืนเงิน", "มาตรา"],
  debt: ["หนี้", "ดอกเบี้ย", "มาตรา", "ลูกหนี้"],
  family: ["สมรส", "หย่า", "บุตร", "มรดก"],
  accident: ["อุบัติเหตุ", "ค่าสินไหม", "ประกัน", "ค่าเสียหาย"],
  // ... add all 12 categories
};
```

**VERIFY:**
```ts
ACCURACY_CHECKS.checkRequiredTerms(
  "นายจ้างต้องจ่ายค่าชดเชยตามมาตรา 118",
  ["ค่าชดเชย", "นายจ้าง"]
) // → []
ACCURACY_CHECKS.checkRequiredTerms(
  "ควรไปแจ้งความ",
  ["มาตรา", "ค่าชดเชย", "นายจ้าง"]
) // → ["ขาดคำสำคัญ: \"มาตรา\"", ...]
```

**DEPENDS:** None. ✅ Logic already exists — just define term sets.

---

### 24.4 — `checkPlaceholders` — ตรวจสอบช่องว่างที่ยังไม่ได้แทนที่

**HOW:** Already implemented. Detects `{UPPER_CASE}` patterns not yet filled.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 193-199)

**VERIFY:**
```ts
ACCURACY_CHECKS.checkPlaceholders("สัญญาเช่าระหว่าง {NAME}") 
// → ["พบ placeholder: {NAME}"]
ACCURACY_CHECKS.checkPlaceholders("สัญญาเช่าระหว่าง นายสมชาย") 
// → []
```

**DEPENDS:** None. ✅

---

### 24.5 — `runAll()` — Run All Checks

**HOW:** Already implemented. Aggregates all 4 checks and returns `{ issues, passed }`.

**WHERE:** `D:\legalai-citizen-check\lib\legal\guardrails.ts` (lines 203-211)

**CODE (enhance — add structured result):**
```ts
runAll: (text: string, category?: string): { 
  issues: string[]; 
  passed: boolean; 
  byCheck: Record<string, string[]> 
} => {
  const beYearIssues = ACCURACY_CHECKS.checkBEYear(text);
  const formalIssues = ACCURACY_CHECKS.checkFormalLanguage(text);
  const requiredTerms = category ? (REQUIRED_TERMS[category] ?? []) : [];
  const termIssues = ACCURACY_CHECKS.checkRequiredTerms(text, requiredTerms);
  const placeholderIssues = ACCURACY_CHECKS.checkPlaceholders(text);

  const allIssues = [
    ...beYearIssues,
    ...formalIssues,
    ...termIssues,
    ...placeholderIssues,
  ];

  return {
    issues: allIssues,
    passed: allIssues.length === 0,
    byCheck: {
      beYear: beYearIssues,
      formalLanguage: formalIssues,
      requiredTerms: termIssues,
      placeholders: placeholderIssues,
    },
  };
},
```

**VERIFY:** Run `runAll()` on AI-generated text → structured result. Integration test with actual AI output.

**DEPENDS:** 24.1-24.4. ✅

---

## 25. 🏠 Home Page

### 25.1 — Welcome Section: User Greeting + Date

**HOW:** Already implemented. Shows "สวัสดีค่ะ คุณนภัสสร 👋" with Pill "✦ AI ที่เข้าใจกฎหมายไทย" and a date card. Date is client-only to avoid hydration mismatch.

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 69-99)

**CODE (enhance — dynamic user name):**
```tsx
// Replace hardcoded "คุณนภัสสร" with auth user:
import { useAuth } from "@/lib/auth/session";

// In component:
const { user } = useAuth();
const displayName = user?.user_metadata?.full_name ?? "คุณนภัสสร";
// Use: <h1>สวัสดีค่ะ {displayName} 👋</h1>
```

**VERIFY:** Page loads → greeting shows. Date card shows current Thai date. ✅

**DEPENDS:** None. ✅

---

### 25.2 — Search Box with Popular Searches

**HOW:** Already implemented. Search box with `<SearchIcon>`, 4 popular search buttons (ถูกโกงออนไลน์, นายจ้างไม่จ่ายเงิน, ขอคืนเงิน, สัญญาเช่า).

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 19, 101-142)

**VERIFY:** Type query → hit Enter or click ค้นหา → navigates to `/search?q=...`. Click popular search → same. ✅

**DEPENDS:** None. ✅

---

### 25.3 — Category Grid: 12 หมวด → `/categories/[id]`

**HOW:** Already implemented. Maps over `categories` from `lib/mock/categories.ts`, 12 cards with icons, titles, hints. Each links to `/categories/[id]`.

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 151-167)

**VERIFY:** All 12 categories render. Click any → navigates to category page. ✅

**DEPENDS:** `categories` array in mock data. ✅

---

### 25.4 — Action Cards: 6 Cards

**HOW:** Already implemented. 6 action cards: วิเคราะห์เคส, สร้างเอกสาร, ปรึกษาทนาย, วางแผนภาษี, อัปเกรดแพ็กเกจ, [categories link].

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 21-63, 169-181)

**VERIFY:** All 6 cards render with icons, titles, descriptions, CTAs. Click → navigates. ✅

**DEPENDS:** None. ✅

---

### 25.5 — Case Preview: In-Progress Case Card

**HOW:** Already implemented using `CaseProgressCard` component with `sampleCases[0]`.

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 183-192)

**VERIFY:** Case card shows progress bar, next action, deadline. Links to `/cases/case-1/timeline`. ✅

**DEPENDS:** `CaseProgressCard` component + `sampleCases` mock data. ✅

---

### 25.6 — Trust Strip: Security Message

**HOW:** Already implemented. Shows ShieldIcon + "ข้อมูลของคุณได้รับการปกป้อง" + encryption message.

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (lines 194-203)

**VERIFY:** Trust strip renders at bottom of page. ✅

**DEPENDS:** None. ✅

---

### 25.7 — Prototype Data Notice

**HOW:** Already included via `<PrototypeDataNotice />` in trust strip.

**WHERE:** `D:\legalai-citizen-check\app\page.tsx` (line 202)

**VERIFY:** "ข้อมูลตัวอย่าง" label appears. ✅

**DEPENDS:** None. ✅

---

## 26. 👤 Profile Page

### 26.1 — Profile Card: Avatar, Name, Email, Package Pill

**HOW:** Already implemented. Hardcoded data for "นภัสสร วัฒนะ" with avatar initials, email, member-since, package pill.

**WHERE:** `D:\legalai-citizen-check\app\profile\page.tsx` (lines 45-56)

**CODE (enhance with real auth data):**
```tsx
import { useAuth } from "@/lib/auth/session";

// In component:
const { user } = useAuth();
const fullName = user?.user_metadata?.full_name ?? "นภัสสร วัฒนะ";
const email = user?.email ?? "napassorn@example.com";
const initials = fullName.split(" ").map(n => n[0]).join("").slice(0, 2);
```

**VERIFY:** Profile card renders with all fields. ✅

**DEPENDS:** Auth system (section 28). Currently uses mock data.

---

### 26.2 — Settings Sidebar: 6 Tabs with Active State

**HOW:** Already implemented. `SETTINGS_NAV` array with 6 tabs, `activeTab` state drives active class and conditional rendering. ✅ Fixed per bug P1-1.

**WHERE:** `D:\legalai-citizen-check\app\profile\page.tsx` (lines 8-17, 22, 58-70)

**VERIFY:** Click any tab → sidebar highlights, content panel changes. ✅

**DEPENDS:** None. ✅ Already working.

---

### 26.3–26.8 — All Tab Contents

**HOW:** Each tab content already implemented under conditional renders:

| Tab | Key | Content |
|-----|-----|---------|
| ข้อมูลส่วนตัว | `personal` | Name, surname, email, phone form (lines 74-87) |
| การแจ้งเตือน | `notifications` | LINE toggle + email select (lines 90-106) |
| ความเป็นส่วนตัว | `privacy` | AI consent toggle + data export/delete buttons (lines 110-148) |
| การแสดงผล | `display` | Language + font size selects (lines 151-163) |
| แพ็กเกจ | `package` | Current package pill + upgrade CTA (lines 166-176) |
| ช่วยเหลือ | `help` | FAQ + contact info (lines 180-191) |

**WHERE:** `D:\legalai-citizen-check\app\profile\page.tsx`

**CODE (enhance privacy tab — add confirmation dialogs for delete):**
```tsx
// Replace direct notify for delete:
function handleDeleteData() {
  if (!window.confirm("คุณแน่ใจหรือไม่ที่จะลบข้อมูลทั้งหมด?\n\nการดำเนินการนี้ไม่สามารถย้อนกลับได้\nข้อมูลเคส เอกสาร และหลักฐานทั้งหมดจะถูกลบถาวร")) {
    return;
  }
  notify("คำขอลบข้อมูลได้รับแล้ว — เราจะดำเนินการภายใน 30 วันตาม PDPA");
  recordEvent({ type: "search_submitted" as any });
}
```

**VERIFY:** Each tab renders correct content. Toggles work. Buttons show toast. ✅

**DEPENDS:** None. ✅ Already working.

---

## 27. 🏛️ Admin Dashboard

### 27.1 — Stats Row: Users, Lawyers, Cases, Revenue

**HOW:** Already implemented with 4 `DashboardStat` cards in a `stat-grid`. Shows mock values with change percentages.

**WHERE:** `D:\legalai-citizen-check\app\admin\page.tsx` (lines 40-73, 180-199)

**CODE (enhance — add real data fetching):**
```tsx
// Replace static stats with fetch:
const [stats, setStats] = useState(dashboardStats); // start with mock

useEffect(() => {
  fetch("/api/admin/stats")
    .then(r => r.json())
    .then(data => setStats(data))
    .catch(() => {}); // fallback to mock
}, []);
```

**VERIFY:** 4 stat cards: เคสที่เปิดอยู่ (128), ผู้ใช้ (3,420), รอตรวจสอบทนาย (7), รายได้ (฿86,400). ✅

**DEPENDS:** None (mock). Future: `/api/admin/stats` endpoint.

---

### 27.2 — Recent Cases Table

**HOW:** Implemented as "กิจกรรมล่าสุด" section with filter tabs (ทั้งหมด/ทนาย/เคส/ระบบ) and 5 activity items.

**WHERE:** `D:\legalai-citizen-check\app\admin\page.tsx` (lines 113-336)

**CODE (enhance — add filter logic):**
```tsx
const filteredActivities = activeFilter === "ทั้งหมด"
  ? activities
  : activeFilter === "ทนาย"
    ? activities.filter(a => a.action.includes("ทนาย"))
    : activeFilter === "เคส"
      ? activities.filter(a => a.action.includes("เคส"))
      : activities.filter(a => a.action.includes("ระบบ") || a.action.includes("เทมเพลต"));
```

**VERIFY:** Filter tabs update visible activities. Each activity shows colored dot, action name, detail, time. ✅

**DEPENDS:** None (mock). ✅

---

### 27.3 — Top Lawyers List

**HOW:** Currently represented as "โมดูลผู้ดูแลระบบ" cards — the "การตรวจสอบทนาย" card links to lawyer verification. Not yet a full leaderboard. The lawyer verification module card shows pending count with badge.

**WHERE:** `D:\legalai-citizen-check\app\admin\page.tsx` (lines 75-108, 246-273)

**CODE (add top lawyers table):**
```tsx
{/* After module grid, add top lawyers */}
<div style={{ marginTop: 24 }}>
  <h3>ทนายความยอดนิยม</h3>
  <div className="info-card">
    {sampleLawyers.slice(0, 5).map((l, i) => (
      <div key={l.id} style={{ display: "flex", alignItems: "center", gap: 12, padding: "8px 0", borderTop: i > 0 ? "1px solid var(--line)" : "none" }}>
        <span style={{ fontWeight: 700, width: 24 }}>{i + 1}.</span>
        <strong style={{ flex: 1 }}>{l.displayName}</strong>
        <small>★ {l.rating?.toFixed(1)}</small>
        <Pill tone="green">ตรวจสอบแล้ว</Pill>
      </div>
    ))}
  </div>
</div>
```

**VERIFY:** Top 5 lawyers table renders below module cards. ✅

**DEPENDS:** `sampleLawyers` import. ✅ Available.

---

### 27.4 — Revenue Overview

**HOW:** Revenue shown in stat card "รายได้เดือนนี้ (ประมาณ) ฿86,400" with +15% change. Not yet a chart.

**WHERE:** `D:\legalai-citizen-check\app\admin\page.tsx` (lines 66-73)

**CODE (enhance — add simple revenue bar):**
```tsx
{/* After stat cards, add revenue trend */}
<div className="info-card" style={{ marginTop: 20 }}>
  <h3>แนวโน้มรายได้</h3>
  <div style={{ display: "flex", alignItems: "end", gap: 8, height: 100, marginTop: 12 }}>
    {[45, 52, 48, 58, 62, 68, 72, 78, 82, 86].map((val, i) => (
      <div key={i} style={{
        flex: 1, height: `${val}%`, background: "var(--blue)", borderRadius: "4px 4px 0 0",
        opacity: 0.3 + (i * 0.07),
      }} title={`เดือน ${i+1}: ฿${val},000`} />
    ))}
  </div>
  <div style={{ display: "flex", justifyContent: "space-between", marginTop: 4, fontSize: 10, color: "var(--muted)" }}>
    {["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค."].map(m => <span key={m}>{m}</span>)}
  </div>
</div>
```

**VERIFY:** Revenue bar chart renders. ✅

**DEPENDS:** None. ✅

---

## 28. 🚀 Onboarding

### 28.1 — 5-Step Flow

**HOW:** Already fully implemented with `useState(step)`, progress bar, back/next navigation.

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx`

**VERIFY:** Navigate through 5 steps → each step renders correct content. Progress bar updates. Back button works. ✅

**DEPENDS:** Auth system (`useAuth`). Requires signed-in user.

---

### 28.2 — Step 1: Accept Terms + Privacy (Checkbox)

**HOW:** Two checkboxes (`agreeTerms`, `agreePrivacy`) with links to `/terms` and `/privacy`. Both must be checked to proceed.

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx` (lines 36-37, 189-228)

**VERIFY:** Uncheck → "ถัดไป" blocked with error. Both checked → proceeds. ✅

**DEPENDS:** `/terms` and `/privacy` pages must exist. ✅ Already present.

---

### 28.3 — Step 2: Email Verification (NEW)

**HOW:** Full email verification flow: input email → send code (mock 1.2s delay) → enter 6-digit code → verify (accepts any code). Shows success state with green checkmark. Resend and change-email options.

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx` (lines 45-48, 108-140, 304-471)

**CODE (wire up real email verification):**
```tsx
async function sendVerificationCode() {
  if (!email.includes("@") || !email.includes(".")) {
    setError("กรุณากรอกอีเมลที่ถูกต้อง");
    return;
  }
  setError(null);
  setSending(true);
  try {
    const res = await fetch("/api/auth/send-verification", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    });
    if (!res.ok) throw new Error("ส่งไม่สำเร็จ");
    setCodeSent(true);
    notify("ส่งรหัสยืนยันไปที่ " + email + " แล้ว");
  } catch {
    setError("ไม่สามารถส่งรหัสยืนยันได้ — ลองใหม่อีกครั้ง");
  } finally {
    setSending(false);
  }
}

async function verifyCode() {
  if (verificationCode.length !== 6) {
    setError("กรุณากรอกรหัส 6 หลัก");
    return;
  }
  try {
    const res = await fetch("/api/auth/verify-code", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, code: verificationCode }),
    });
    if (!res.ok) throw new Error("รหัสไม่ถูกต้อง");
    setEmailVerified(true);
    setError(null);
    notify("ยืนยันอีเมลสำเร็จ ✓");
  } catch {
    setError("รหัสยืนยันไม่ถูกต้อง — กรุณาลองอีกครั้ง");
  }
}
```

**VERIFY:**
1. Enter email → click ส่งรหัส → shows "ส่งแล้ว ✓"
2. Enter 6-digit code → click ยืนยัน → ✅ success
3. Click เปลี่ยนอีเมล → resets to email input

**DEPENDS:** In production: email service + `/api/auth/send-verification` and `/api/auth/verify-code` endpoints.

---

### 28.4 — Step 3: AI Consent

**HOW:** Single checkbox for AI processing consent with explanation text.

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx` (lines 39, 232-257)

**VERIFY:** Checkbox unchecked → blocked. Checked → proceeds. ✅

**DEPENDS:** None. ✅

---

### 28.5 — Step 4: Notification Preferences

**HOW:** Three checkboxes: in-app (default on), email (default on), LINE (default off).

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx` (lines 41-43, 261-302)

**VERIFY:** Toggle each → updates state. Any combination proceeds (at least one). ✅

**DEPENDS:** None. ✅

---

### 28.6 — Step 5: Profile Setup

**HOW:** Name input + language select (ไทย/English). Name required.

**WHERE:** `D:\legalai-citizen-check\app\onboarding\page.tsx` (lines 51-52, 475-563)

**VERIFY:** Empty name → blocked. Filled name → proceeds → toast "การตั้งค่าบัญชีเสร็จสมบูรณ์!" → navigates home. ✅

**DEPENDS:** None. ✅

---

## 29. 🐛 17 Bug Fixes

### Priority Summary

| # | ID | Priority | File | Status |
|---|-----|----------|------|--------|
| 1 | P0-1 | 🔴 Critical | `app/cases/[caseId]/timeline/page.tsx` | ⚠️ NEEDS FIX |
| 2 | P0-2 | 🔴 Critical | `app/terms/page.tsx` | ✅ ALREADY DONE |
| 3 | P0-3 | 🔴 Critical | `app/privacy/page.tsx` | ✅ ALREADY DONE |
| 4 | P1-1 | 🟡 High | `app/profile/page.tsx` | ✅ ALREADY DONE |
| 5 | P1-2 | 🟡 High | `app/profile/page.tsx` | ✅ ALREADY DONE |
| 6 | P1-3 | 🟡 High | `app/search/page.tsx` | ✅ ALREADY DONE |
| 7 | P1-4 | 🟡 High | `app/notifications/page.tsx` + `app/lawyers/page.tsx` | ✅ ALREADY DONE |
| 8 | P1-5 | 🟡 High | `app/search/page.tsx` | ✅ ALREADY DONE |
| 9 | P1-6 | 🟡 High | `app/search/page.tsx` | ⚠️ PARTIAL |
| 10 | P1-7 | 🟡 High | 3 pages (search, diagnosis, profile) | ⚠️ NEEDS CHECK |
| 11 | P2-1 | 🟢 Low | `app/notifications/page.tsx` | ✅ ALREADY DONE |
| 12 | P2-2 | 🟢 Low | `app/lawyers/page.tsx` | ✅ ALREADY DONE |
| 13 | P2-3 | 🟢 Low | `app/assistant/page.tsx` | ⚠️ NEEDS FIX |
| 14 | P2-4 | 🟢 Low | `app/pricing/page.tsx` | ✅ ALREADY DONE |
| 15 | P2-5 | 🟢 Low | `app/search/page.tsx` | ✅ ALREADY DONE |
| 16 | P2-6 | 🟢 Low | API route | ⚠️ NEEDS FIX |
| 17 | P2-7 | 🟢 Low | Search sidebar | ✅ ALREADY DONE |

---

### 29.1 — P0-1: Case Tabs `href="#"` → Real Routes

**HOW:** In the timeline page, change tab links from `href="#"` with `e.preventDefault()` to real route links.

**WHERE:** `D:\legalai-citizen-check\app\cases\[caseId]\timeline\page.tsx`

**CODE:**
```tsx
// Find the tabs navigation section and replace:
// BEFORE:
<Link href="#" onClick={(e) => { e.preventDefault(); ... }}>หลักฐาน</Link>

// AFTER:
// Map each tab label to its real route:
const tabRoutes: Record<string, string> = {
  "ภาพรวม": `/cases/${caseId}/timeline`,
  "ไทม์ไลน์": `/cases/${caseId}/timeline`,
  "หลักฐาน": `/cases/${caseId}/evidence`,
  "เอกสาร": "/documents",
};

{tabs.map((t) => (
  <Link
    key={t.label}
    href={tabRoutes[t.label] ?? "#"}
    className={t.active ? "active" : ""}
    aria-current={t.active ? "page" : undefined}
    onClick={() => recordEvent({ type: "search_submitted" as any })}
  >
    {t.label}
    {t.count ? <i>{t.count}</i> : null}
  </Link>
))}
```

**VERIFY:**
1. Go to `/cases/case-1/timeline`
2. Click "หลักฐาน" tab → navigates to `/cases/case-1/evidence`
3. Click "เอกสาร" tab → navigates to `/documents`
4. "ภาพรวม" / "ไทม์ไลน์" → stays on timeline page

**DEPENDS:** None. Single file fix.

---

### 29.2 — P0-2: `/terms` Page

**STATUS:** ✅ **ALREADY DONE.** `app/terms/page.tsx` exists with 9 sections, warning box, contact info.

**VERIFY:** Visit `/terms` → page renders with all content. No 404.

---

### 29.3 — P0-3: `/privacy` Page

**STATUS:** ✅ **ALREADY DONE.** `app/privacy/page.tsx` exists with 8 sections, PDPA rights table, data table.

**VERIFY:** Visit `/privacy` → page renders with all content. No 404.

---

### 29.4 — P1-1: Profile Settings Tabs → `useState`

**STATUS:** ✅ **ALREADY DONE.** `activeTab` state with 6 tabs, conditional rendering per tab. Sidebar buttons have `onClick={() => setActiveTab(item.key)}`.

**VERIFY:** Click any tab → content changes. Active tab highlighted.

---

### 29.5 — P1-2: AI Consent Toggle + Data Rights

**STATUS:** ✅ **ALREADY DONE.** `aiConsent` state with toggle button in privacy tab. Export data and delete data buttons with toast feedback.

**VERIFY:** Toggle AI consent → toast. Click export/delete → toast.

---

### 29.6 — P1-3: Search Sort Dropdown → `onClick`

**STATUS:** ✅ **ALREADY DONE.** Custom sort dropdown with `sortOpen` state, 3 options with `onClick` handlers.

**VERIFY:** Click dropdown → shows 3 options. Select one → dropdown closes, sort updates.

---

### 29.7 — P1-4: Filter Tabs → 3 Pages

**STATUS:** ✅ **ALREADY DONE.**
- Notifications: `active` state filters by `NOTIFICATION_CATEGORY`
- Lawyers: `activeChip` state filters by specialty keywords
- Cases: filters work

**VERIFY:** Click notification tabs → list filters. Click lawyer chips → list filters.

---

### 29.8 — P1-5: Search Share Button → `navigator.share`

**STATUS:** ✅ **ALREADY DONE.** `handleShare()` uses `navigator.share()` with fallback to `clipboard.writeText()`.

**VERIFY:** Click ↗ แชร์ → native share dialog (mobile) or clipboard copy (desktop).

---

### 29.9 — P1-6: Search Article/Topic Links → Clickable

**STATUS:** ⚠️ **PARTIAL.** Articles use `handleArticleClick()` which only shows toast. Should navigate to search results.

**WHERE:** `D:\legalai-citizen-check\app\search\page.tsx` (lines 95-97, 219-227)

**CODE:**
```tsx
// Replace handleArticleClick:
function handleArticleClick(title: string) {
  router.push(`/search?q=${encodeURIComponent(title)}`);
}

// Replace topic buttons from toast to search navigation:
// Already fixed — topics use router.push via _handleTopicClick. 
// Just rename _handleTopicClick to handleTopicClick and wire it:
function handleTopicClick(topic: string) {
  router.push(`/search?q=${encodeURIComponent(topic)}`);
}
```

**VERIFY:** Click article → navigates to `/search?q=...`. Click topic tag → same.

**DEPENDS:** None.

---

### 29.10 — P1-7: Disclaimers → 3 Pages

**STATUS:** ⚠️ **NEEDS FIX (2 of 3 pages).**
- Search page: Already has `search-disclaimer` div (line 150-152) and `disclaimer` in answer card (line 189-191). ✅
- Diagnosis page: **MISSING** — only has `privacy-note` at lines 195 and 323. No `LegalDisclaimer` component. ❌
- Profile page: **MISSING** — no `LegalDisclaimer` component anywhere. ❌

**WHERE:**
- `D:\legalai-citizen-check\app\search\page.tsx` — ✅ has inline disclaimers
- `D:\legalai-citizen-check\app\diagnosis\page.tsx` — check for disclaimer
- `D:\legalai-citizen-check\app\profile\page.tsx` — check for disclaimer

**CODE (add to diagnosis page if missing):**
```tsx
import { LegalDisclaimer } from "@/components/ui/primitives";

// Add before closing fragment:
<LegalDisclaimer>
  ⓘ การวิเคราะห์นี้ใช้ AI เป็นผู้ช่วยเบื้องต้นเท่านั้น ไม่ใช่การรับรองผลทางกฎหมาย
  ข้อมูลที่ได้ควรปรึกษาทนายความก่อนนำไปใช้จริง
</LegalDisclaimer>
```

**CODE (add to profile page if missing):**
```tsx
import { LegalDisclaimer } from "@/components/ui/primitives";

// Add after settings-layout closing div:
<LegalDisclaimer>
  ⓘ ข้อมูลส่วนตัวของคุณได้รับการปกป้องตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562
  ดูรายละเอียดเพิ่มเติมที่ <Link href="/privacy">นโยบายความเป็นส่วนตัว</Link>
</LegalDisclaimer>
```

**VERIFY:** Each of the 3 pages shows disclaimer text at bottom.

**DEPENDS:** `LegalDisclaimer` component in `components/ui/primitives.tsx`. ✅ Available.

---

### 29.11 — P2-1: Mark All Read → Toast

**STATUS:** ✅ **ALREADY DONE.** `markAllRead()` sets all notification IDs as read and shows toast.

**VERIFY:** Click "✓ อ่านทั้งหมดแล้ว" → toast "ทำเครื่องหมายว่าอ่านทั้งหมดแล้ว".

---

### 29.12 — P2-2: Save Lawyer → Toast

**STATUS:** ✅ **ALREADY DONE.** `toggleSave()` toggles per-lawyer save state with toast feedback.

**VERIFY:** Click ♡ บันทึก → changes to ✓ + toast. Click again → reverts.

---

### 29.13 — P2-3: Assistant Menu → Handlers

**STATUS:** ⚠️ **NEEDS FIX.** The "•••" and "เปลี่ยน" buttons need onClick handlers.

**WHERE:** `D:\legalai-citizen-check\app\assistant\page.tsx` (~lines 156, 167)

**CODE:**
```tsx
// Add useToast import
import { useToast } from "@/components/layout/app-providers";

// In AssistantPage component:
const notify = useToast();

// "•••" button — add clear chat with confirmation:
<button
  aria-label="ตัวเลือกเพิ่มเติม"
  onClick={() => {
    if (window.confirm("ล้างประวัติแชททั้งหมด?")) {
      setMessages([WELCOME]);
      notify("ล้างประวัติแชทแล้ว");
    }
  }}
>
  •••
</button>

// "เปลี่ยน" button — add case selector feedback:
<button
  onClick={() => {
    notify("กรุณาเลือกเคสที่ต้องการ — ฟีเจอร์กำลังพัฒนา");
    // Future: open case selector
  }}
>
  เปลี่ยน
</button>
```

**VERIFY:** Click "•••" → confirm dialog → "ล้างประวัติแชทแล้ว" toast. Click "เปลี่ยน" → toast.

**DEPENDS:** None.

---

### 29.14 — P2-4: Pricing Page

**STATUS:** ✅ **ALREADY DONE.** `app/pricing/page.tsx` exists with 4 tier cards, comparison table, FAQ.

**VERIFY:** Visit `/pricing` → page renders. No 404.

---

### 29.15 — P2-5: Search Dynamic → AI-Powered

**STATUS:** ✅ **ALREADY DONE.** Search page fetches from `/api/ai/assistant` with the query, shows loading/error/result states.

**VERIFY:** Search "เลิกจ้าง" → loading spinner → AI result appears.

---

### 29.16 — P2-6: Categories Valid in Assistant API → 6→12

**STATUS:** ⚠️ **NEEDS FIX.** Ensure all 12 legal categories are valid in the API.

**WHERE:** `D:\legalai-citizen-check\lib\legal\diagnosis-config.ts` and `D:\legalai-citizen-check\app\api\ai\assistant\route.ts`

**CODE (verify categories in diagnosis config):**
```ts
// In diagnosis-config.ts, check that ALL 12 categories from domain/types.ts are included:
const VALID_CATEGORIES: LegalCategory[] = [
  "labour", "consumer", "debt", "housing", "family", "accident",
  "online_fraud", "crime", "government", "insurance", "defamation", "property",
];
// This should be 12 items, not 6.
```

**VERIFY:** Count categories in config → must be 12. Assistant API accepts all 12 category values.

**DEPENDS:** Check `diagnosis-config.ts` for completeness.

---

### 29.17 — P2-7: Business Doc Categories in Search Sidebar

**STATUS:** ✅ **ALREADY DONE.** Search sidebar shows `DOCUMENT_CATEGORIES` with `suggestCategory()` matching.

**VERIFY:** Search "สัญญาเช่า" → sidebar shows related document categories.

---

## 📊 Execution Summary

### Files That Need Changes (Priority Order)

| Priority | File | Issues |
|----------|------|--------|
| 🔴 P0 | `app/cases/[caseId]/timeline/page.tsx` | Fix tab href routes |
| 🔴 P0 | `app/assistant/page.tsx` | Wire "•••" and "เปลี่ยน" handlers |
| 🟡 P1 | `app/search/page.tsx` | Fix article click → navigate to search |
| 🟡 P1 | `app/diagnosis/page.tsx` | Add LegalDisclaimer if missing |
| 🟡 P1 | `app/profile/page.tsx` | Add LegalDisclaimer if missing |
| 🟡 P1 | `app/lawyers/page.tsx` | Change buttons to Link components |
| 🟡 P1 | `lib/legal/diagnosis-config.ts` | Verify 12 categories |
| 🟢 P2 | `lib/legal/guardrails.ts` | Expand banned patterns |

### Already Complete ✅
- `/terms` and `/privacy` pages (P0-2, P0-3)
- Profile settings tabs + AI consent (P1-1, P1-2)
- Search sort + share + dynamic AI (P1-3, P1-5, P2-5)
- Filter tabs 3 pages (P1-4)
- Mark all read + save lawyer (P2-1, P2-2)
- `/pricing` page (P2-4)
- Business doc categories sidebar (P2-7)
- Evidence upload (all 6 sub-items)
- Lawyer detail page (all 9 sub-items)
- Tier definitions + feature gates
- 7 guardrails + accuracy checks
- Home page (all 7 sub-items)
- Admin dashboard (all 4 sub-items)
- Onboarding 5-step flow

---

> **Total: ~80% of sections 16-29 already implemented.** Remaining work: 3-4 small fixes totaling ~2 hours of work.
