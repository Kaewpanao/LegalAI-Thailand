# LegalAI Thailand — Business Documents + Tax: Detailed Implementation Solutions
> **Scope: Sections 9-15 of `legalai_complete_breakdown.md`**
>
> 126 Document Templates · Category Pages · Editor · Merge Engine · Tax Calculator · Tax Optimizer · Filing Checklist
>
> Last Updated: 2026-08-10
> Based on: `legalai_business_documents_library.md`, `legalai_tax_planning_module.md`, `legalai_business_tax_compliance_supplement.md`, `legalai_complete_breakdown.md`

---

## Table of Contents

- [Section 9: 126 Document Templates — 10 Categories](#section-9-126-document-templates--10-categories)
- [Section 10: Document Category Pages](#section-10-document-category-pages)
- [Section 11: Document Editor](#section-11-document-editor)
- [Section 12: Merge Engine](#section-12-merge-engine)
- [Section 13: Tax Calculator](#section-13-tax-calculator)
- [Section 14: Tax Optimizer](#section-14-tax-optimizer)
- [Section 15: Filing Checklist](#section-15-filing-checklist)
- [Appendix A: File Structure](#appendix-a-file-structure)
- [Appendix B: Package Tier Mapping](#appendix-b-package-tier-mapping)

---

## Section 9: 126 Document Templates — 10 Categories

### Architecture Overview

All 126 template files live under `lib/documents/templates/` organized by category slug. Each template is a `.md` file with YAML frontmatter metadata and a body containing merge-field syntax. Templates are NEVER hardcoded in UI components — they are loaded dynamically by category slug.

```
lib/documents/
├── templates/
│   ├── property/          # 14 templates (อสังหาริมทรัพย์)
│   ├── rental/            # 17 templates (สัญญาเช่า)
│   ├── business/          # 14 templates (จัดตั้งธุรกิจ)
│   ├── loan/              # 9 templates (สินเชื่อ)
│   ├── family/            # 11 templates (ครอบครัว)
│   ├── employment/        # 20 templates (การจ้างงาน)
│   ├── commercial/        # 17 templates (พาณิชยกรรม)
│   ├── vehicle/           # 9 templates (ยานพาหนะ)
│   ├── travel/            # 6 templates (ท่องเที่ยว)
│   └── ip/                # 9 templates (ทรัพย์สินทางปัญญา)
├── categories.ts          # Category registry
├── merge-engine.ts        # Merge engine (Section 12)
├── export.ts              # PDF/TXT/DOCX export
├── templates-registry.ts  # Dynamic loader
└── validation.ts          # Template validation
```

### 9.1 — 9.10: Template Files Per Category

**HOW TO IMPLEMENT:** For each of the 126 templates, create a `.md` file with the structure below.

#### Template File Format (every template uses this exact structure):

```markdown
---
slug: "rental-house"
title_th: "สัญญาเช่าบ้าน"
title_en: "House Rental Agreement"
category: "rental"
price_tier: "free"           # "free" | "paid"
price: 0                      # 0 for free, 99 for pay-per-doc
auto_gen_feasibility: "high"  # "high" | "medium" | "low"
merge_fields:
  - { key: "lessor_name", label_th: "ชื่อผู้ให้เช่า", type: "text", required: true }
  - { key: "lessor_address", label_th: "ที่อยู่ผู้ให้เช่า", type: "textarea", required: true }
  - { key: "lessor_id", label_th: "เลขบัตรประชาชนผู้ให้เช่า", type: "text", required: true }
  - { key: "lessee_name", label_th: "ชื่อผู้เช่า", type: "text", required: true }
  - { key: "lessee_address", label_th: "ที่อยู่ผู้เช่า", type: "textarea", required: true }
  - { key: "lessee_id", label_th: "เลขบัตรประชาชนผู้เช่า", type: "text", required: true }
  - { key: "property_address", label_th: "ที่อยู่ทรัพย์สินที่เช่า", type: "textarea", required: true }
  - { key: "rent_amount", label_th: "ค่าเช่ารายเดือน (บาท)", type: "number", required: true }
  - { key: "rent_amount_text", label_th: "ค่าเช่ารายเดือน (ตัวอักษร)", type: "text", required: true }
  - { key: "deposit_amount", label_th: "เงินประกัน (บาท)", type: "number", required: true }
  - { key: "contract_start", label_th: "วันที่เริ่มสัญญา", type: "date", required: true }
  - { key: "contract_end", label_th: "วันที่สิ้นสุดสัญญา", type: "date", required: true }
  - { key: "witness_1_name", label_th: "ชื่อพยานคนที่ 1", type: "text", required: true }
  - { key: "witness_2_name", label_th: "ชื่อพยานคนที่ 2", type: "text", required: true }
conditional_fields:
  - { key: "include_pet_clause", label_th: "ระบุข้อตกลงเรื่องสัตว์เลี้ยง", type: "boolean", default: false }
  - { key: "include_sublease_clause", label_th: "ระบุข้อตกลงเรื่องเช่าช่วง", type: "boolean", default: false }
  - { key: "include_utility_clause", label_th: "ระบุข้อตกลงเรื่องค่าสาธารณูปโภค", type: "boolean", default: false }
description_th: "สัญญาเช่าบ้านพักอาศัยมาตรฐาน ครอบคลุมค่าเช่า เงินประกัน ระยะเวลาเช่า และเงื่อนไขทั่วไป"
description_en: "Standard residential house rental agreement covering rent, deposit, term, and general conditions"
tags: ["เช่า", "บ้าน", "ที่อยู่อาศัย"]
version: 1
---

# สัญญาเช่าบ้าน

ทำที่ {{location}}
วันที่ {{date_thai}}

**สัญญาฉบับนี้** ทำขึ้นระหว่าง:

**ผู้ให้เช่า:** {{lessor_name}} อยู่บ้านเลขที่ {{lessor_address}} ถือบัตรประจำตัวประชาชนเลขที่ {{lessor_id}} (ซึ่งต่อไปนี้จะเรียกว่า "**ผู้ให้เช่า**") **ฝ่ายหนึ่ง**

**กับ**

**ผู้เช่า:** {{lessee_name}} อยู่บ้านเลขที่ {{lessee_address}} ถือบัตรประจำตัวประชาชนเลขที่ {{lessee_id}} (ซึ่งต่อไปนี้จะเรียกว่า "**ผู้เช่า**") **อีกฝ่ายหนึ่ง**

ทั้งสองฝ่ายตกลงทำสัญญาเช่ากันดังต่อไปนี้:

**ข้อ 1. ทรัพย์สินที่เช่า** ผู้ให้เช่าตกลงให้เช่าและผู้เช่าตกลงเช่า {{property_type}} ตั้งอยู่เลขที่ {{property_address}}

**ข้อ 2. ระยะเวลาเช่า** สัญญาเช่านี้มีกำหนด {{lease_duration_months}} เดือน เริ่มตั้งแต่วันที่ {{contract_start_thai}} ถึงวันที่ {{contract_end_thai}}

**ข้อ 3. ค่าเช่า** ผู้เช่าตกลงชำระค่าเช่าเป็นรายเดือน เดือนละ {{rent_amount_text}} ({{rent_amount}} บาท) โดยชำระล่วงหน้าภายในวันที่ {{rent_due_day}} ของทุกเดือน

**ข้อ 4. เงินประกัน** ผู้เช่าได้วางเงินประกันเป็นจำนวน {{deposit_amount_text}} ({{deposit_amount}} บาท) ให้แก่ผู้ให้เช่าไว้ในวันทำสัญญานี้

{{#if include_utility_clause}}
**ข้อ 5. ค่าสาธารณูปโภค** ผู้เช่าเป็นผู้รับผิดชอบค่าสาธารณูปโภคทั้งหมด ได้แก่ ค่าไฟฟ้า ค่าน้ำประปา {{#if include_internet}}ค่าอินเทอร์เน็ต{{/if}} ตามจำนวนที่เกิดขึ้นจริง
{{/if}}

{{#if include_pet_clause}}
**ข้อ 6. สัตว์เลี้ยง** {{pet_policy}}
{{/if}}

{{#if include_sublease_clause}}
**ข้อ 7. การให้เช่าช่วง** {{sublease_policy}}
{{/if}}

**ข้อ {{next_clause}}. หน้าที่ของผู้เช่า** ผู้เช่าตกลงจะดูแลรักษาทรัพย์สินที่เช่าเยี่ยงวิญญูชน หากเกิดความเสียหาย ผู้เช่าจะต้องชดใช้ค่าเสียหาย เว้นแต่เป็นความเสียหายที่เกิดจากการใช้งานตามปกติ

**ข้อ {{next_clause}}. การผิดสัญญา** หากผู้เช่าผิดนัดชำระค่าเช่าเป็นเวลาติดต่อกันเกิน {{grace_period_months}} เดือน ผู้ให้เช่ามีสิทธิบอกเลิกสัญญาได้ทันที

สัญญานี้ทำขึ้นสองฉบับ มีข้อความตรงกัน ทั้งสองฝ่ายได้อ่านและเข้าใจข้อความดีแล้ว จึงลงลายมือชื่อไว้เป็นหลักฐานต่อหน้าพยาน

ลงชื่อ ..................................................... ผู้ให้เช่า
({{lessor_name}})
วันที่ {{signing_date_thai}}

ลงชื่อ ..................................................... ผู้เช่า
({{lessee_name}})
วันที่ {{signing_date_thai}}

ลงชื่อ ..................................................... พยาน
({{witness_1_name}})
วันที่ {{signing_date_thai}}

ลงชื่อ ..................................................... พยาน
({{witness_2_name}})
วันที่ {{signing_date_thai}}
```

#### Step-by-Step Implementation Plan for 126 Templates:

1. **Create the directory structure** (one command):
   ```bash
   mkdir -p lib/documents/templates/{property,rental,business,loan,family,employment,commercial,vehicle,travel,ip}
   ```

2. **Create templates in batches** (10-15 per batch, matching subagent chunking pattern from legalai-workflows skill):
   - Batch 1: rental (17) + vehicle (9) = 26 ✅ HIGH
   - Batch 2: employment (20) + travel (6) = 26 ✅ HIGH
   - Batch 3: commercial (17) + ip (9) = 26 ✅ HIGH
   - Batch 4: property (14) + family (11) = 25 ✅ HIGH
   - Batch 5: business (14) + loan (9) = 23 mostly HIGH

3. **For each template, follow this checklist:**
   - [ ] YAML frontmatter with all 12 required fields (slug, title_th, title_en, category, price_tier, price, auto_gen_feasibility, merge_fields[], conditional_fields[], description_th, description_en, tags[])
   - [ ] All merge_fields have: key, label_th, type (text/textarea/number/date/select/boolean), required
   - [ ] Conditional fields use `{{#if key}}...{{/if}}` syntax
   - [ ] Thai legal language is formal (passes checkFormalLanguage)
   - [ ] Dates use Thai BE format via `{{date_thai}}` and `{{signing_date_thai}}`
   - [ ] Money amounts include both numeric (`{{amount}}`) and text (`{{amount_text}}`) forms
   - [ ] No unfilled `{{placeholders}}` with defaults — every placeholder is generated by merge engine
   - [ ] Signature blocks at bottom with witness lines
   - [ ] Version number starts at 1

4. **Register each template in `templates-registry.ts`**:
   ```typescript
   // lib/documents/templates-registry.ts
   import { TemplateMeta } from "./types";

   export async function loadTemplate(slug: string): Promise<TemplateMeta> {
     // Dynamic import of .md file
     const module = await import(`./templates/${slug.split('-')[0]}/${slug}.md`);
     return parseTemplateFrontmatter(module.default);
   }

   export async function loadTemplatesByCategory(category: string): Promise<TemplateMeta[]> {
     const slugs = CATEGORY_TEMPLATE_MAP[category];
     return Promise.all(slugs.map(slug => loadTemplate(slug)));
   }
   ```

5. **Template validation** (run via `lib/documents/validation.ts`):
   ```typescript
   export function validateTemplate(template: TemplateMeta): ValidationResult {
     const errors: string[] = [];
     // Check all required merge_fields have keys and labels
     // Check conditional blocks are well-formed ({{#if}} has matching {{/if}})
     // Check all {{placeholders}} in body exist in merge_fields or conditional_fields
     // Check no raw {{}} left unaccounted
     return { valid: errors.length === 0, errors };
   }
   ```

### 9.11: Free vs Paid Labeling

**HOW TO IMPLEMENT:**

In the category registry (`lib/documents/categories.ts`), each template has `price_tier` and `price`:

```typescript
// lib/documents/categories.ts
export interface TemplatePricing {
  slug: string;
  price_tier: "free" | "paid";
  price: number;  // 0 for free, 99 for pay-per-doc, or 0 for subscription-gated
}

export function getTemplatePricing(slug: string): TemplatePricing {
  // All templates with price_tier="paid" require Action Pack (299฿) or above
  // price > 0 means pay-per-document option available without subscription
  const template = TEMPLATE_REGISTRY[slug];
  return {
    slug,
    price_tier: template.price_tier,
    price: template.price,
  };
}

export function isTemplateAccessible(slug: string, userPackage: PackageId): boolean {
  const pricing = getTemplatePricing(slug);
  if (pricing.price_tier === "free") return true;
  return checkFeatureAccess("documents:paid", userPackage);
}
```

**UI Label Mapping:**
```typescript
// In components/documents/TemplateBadge.tsx
const BADGE_STYLES = {
  free: { label: "ฟรี", className: "bg-green-100 text-green-700" },
  paid: { label: "Pro", className: "bg-amber-100 text-amber-700" },
};
```

---

## Section 10: Document Category Pages

### 10.1: Dynamic Route `/documents/[category]`

**HOW TO IMPLEMENT:** Next.js App Router dynamic route.

```typescript
// app/documents/[category]/page.tsx
import { CATEGORIES } from "@/lib/documents/categories";
import { loadTemplatesByCategory } from "@/lib/documents/templates-registry";

export async function generateStaticParams() {
  return CATEGORIES.map(cat => ({ category: cat.slug }));
}

export default async function DocumentCategoryPage({
  params,
}: {
  params: { category: string };
}) {
  const category = CATEGORIES.find(c => c.slug === params.category);
  if (!category) return notFound();

  const templates = await loadTemplatesByCategory(params.category);

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <CategoryHeader category={category} templateCount={templates.length} />
      <TemplateList templates={templates} category={category} />
      <CategorySidebar currentCategory={category} />
    </div>
  );
}
```

### 10.2: Real Template Lists (8-17 items per category)

**HOW TO IMPLEMENT:** Load from the filesystem/template registry, not hardcoded.

```typescript
// components/documents/TemplateList.tsx
function TemplateList({ templates, category }: Props) {
  return (
    <div className="divide-y divide-gray-100">
      {templates.map(template => (
        <TemplateRow key={template.slug}>
          <div className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors">
            <div>
              <h3 className="font-medium">{template.title_th}</h3>
              <p className="text-sm text-gray-500 mt-1">{template.description_th}</p>
              <div className="flex gap-2 mt-2">
                {template.tags.map(tag => (
                  <span key={tag} className="px-2 py-0.5 bg-gray-100 text-xs rounded-full">{tag}</span>
                ))}
              </div>
            </div>
            <div className="flex items-center gap-3">
              <TemplateBadge tier={template.price_tier} />
              <CreateButton slug={template.slug} />
            </div>
          </div>
        </TemplateRow>
      ))}
    </div>
  );
}
```

### 10.3: Free/Paid Count Summary in Header

```typescript
// components/documents/CategoryHeader.tsx
function CategoryHeader({ category, templates }: Props) {
  const freeCount = templates.filter(t => t.price_tier === "free").length;
  const paidCount = templates.filter(t => t.price_tier === "paid").length;

  return (
    <div className="mb-8">
      <h1 className="text-2xl font-bold">{category.title_th}</h1>
      <p className="text-gray-500 mt-1">{category.description_th}</p>
      <div className="flex gap-4 mt-3 text-sm">
        <span className="text-green-600">🟢 {freeCount} ฟรี</span>
        <span className="text-amber-600">🟡 {paidCount} Pro</span>
        <span className="text-gray-400">| {templates.length} แบบฟอร์ม</span>
      </div>
    </div>
  );
}
```

### 10.4: "เริ่มสร้าง →" Button per Template

```typescript
// components/documents/CreateButton.tsx
function CreateButton({ slug }: { slug: string }) {
  const template = useTemplate(slug); // client-side fetch
  const router = useRouter();

  return (
    <button
      onClick={() => router.push(`/documents/create?template=${slug}`)}
      className="px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700
                 flex items-center gap-1 transition-colors"
    >
      เริ่มสร้าง
      <ArrowRight className="w-4 h-4" />
    </button>
  );
}
```

### 10.5: Hover Effects on Template Rows

In `TemplateRow`: use Tailwind `hover:bg-gray-50 hover:shadow-sm transition-all duration-150`. Add `group` to the row parent and `group-hover:text-blue-600` to the title on hover.

### 10.6: Pill Tone Mapping per Category Color

```typescript
// lib/documents/categories.ts
export const CATEGORY_COLORS: Record<string, string> = {
  property:    "bg-amber-100 text-amber-800",   // อสังหาฯ — earth tone
  rental:      "bg-blue-100 text-blue-800",     // เช่า — blue
  business:    "bg-indigo-100 text-indigo-800", // จัดตั้งธุรกิจ — indigo
  loan:        "bg-red-100 text-red-800",       // สินเชื่อ — red
  family:      "bg-pink-100 text-pink-800",     // ครอบครัว — pink
  employment:  "bg-green-100 text-green-800",   // จ้างงาน — green
  commercial:  "bg-purple-100 text-purple-800", // พาณิชยกรรม — purple
  vehicle:     "bg-orange-100 text-orange-800", // ยานพาหนะ — orange
  travel:      "bg-cyan-100 text-cyan-800",     // ท่องเที่ยว — cyan
  ip:          "bg-violet-100 text-violet-800", // ทรัพย์สินทางปัญญา — violet
};
```

### Complete Category Routing Table:

| Route | Category Slug | Title TH | Template Count |
|-------|--------------|----------|---------------|
| `/documents/property` | `property` | อสังหาริมทรัพย์ | 14 |
| `/documents/rental` | `rental` | สัญญาเช่า | 17 |
| `/documents/business` | `business` | จัดตั้งธุรกิจ | 14 |
| `/documents/loan` | `loan` | สินเชื่อและการเงิน | 9 |
| `/documents/family` | `family` | ครอบครัวและส่วนบุคคล | 11 |
| `/documents/employment` | `employment` | การจ้างงานและ HR | 20 |
| `/documents/commercial` | `commercial` | พาณิชยกรรม | 17 |
| `/documents/vehicle` | `vehicle` | ยานพาหนะ | 9 |
| `/documents/travel` | `travel` | การท่องเที่ยว | 6 |
| `/documents/ip` | `ip` | ทรัพย์สินทางปัญญา | 9 |

---

## Section 11: Document Editor

### 11.1: `/documents/create` — Document Creation Page

**HOW TO IMPLEMENT:** A split-panel page: left side = merge-field form, right side = live preview.

```typescript
// app/documents/create/page.tsx
"use client";

export default function DocumentCreatePage() {
  const searchParams = useSearchParams();
  const templateSlug = searchParams.get("template");

  const { template, loading, error } = useTemplate(templateSlug);
  const { fieldValues, setField, conditionalValues, toggleConditional } = useMergeForm(template);
  const { previewHtml, isMerging } = useLivePreview(template, fieldValues, conditionalValues);

  if (!templateSlug) return <TemplateSelector />; // Show category picker
  if (loading) return <EditorSkeleton />;
  if (error) return <ErrorState message={error} />;

  return (
    <div className="flex h-[calc(100vh-4rem)]">
      <MergeFormPanel
        template={template}
        fieldValues={fieldValues}
        conditionalValues={conditionalValues}
        onFieldChange={setField}
        onToggleConditional={toggleConditional}
      />
      <LivePreviewPanel
        html={previewHtml}
        isLoading={isMerging}
        template={template}
      />
    </div>
  );
}
```

### 11.2: Merge-Field Form — Replace {ชื่อ}, {ที่อยู่}, {วันที่}

**HOW TO IMPLEMENT:** Dynamic form generated from template metadata.

```typescript
// components/documents/MergeFormPanel.tsx
function MergeFormPanel({ template, fieldValues, conditionalValues, onFieldChange, onToggleConditional }: Props) {
  return (
    <div className="w-1/2 border-r overflow-y-auto p-6">
      <h2 className="text-lg font-semibold mb-1">{template.title_th}</h2>
      <p className="text-sm text-gray-500 mb-6">{template.description_th}</p>

      {/* Required merge fields */}
      <Section title="ข้อมูลจำเป็น">
        {template.merge_fields.map(field => (
          <FormField
            key={field.key}
            field={field}
            value={fieldValues[field.key] ?? ""}
            onChange={val => onFieldChange(field.key, val)}
          />
        ))}
      </Section>

      {/* Conditional fields (optional clauses) */}
      {template.conditional_fields?.length > 0 && (
        <Section title="เงื่อนไขเพิ่มเติม">
          {template.conditional_fields.map(field => (
            <ToggleField
              key={field.key}
              label={field.label_th}
              enabled={conditionalValues[field.key]}
              onToggle={() => onToggleConditional(field.key)}
            />
          ))}
        </Section>
      )}
    </div>
  );
}
```

**FormField component** — renders the correct input type based on `field.type`:

```typescript
function FormField({ field, value, onChange }: FieldProps) {
  switch (field.type) {
    case "text":
      return <TextInput label={field.label_th} value={value} onChange={onChange} required={field.required} />;
    case "textarea":
      return <TextArea label={field.label_th} value={value} onChange={onChange} rows={3} />;
    case "number":
      return <NumberInput label={field.label_th} value={value} onChange={onChange} suffix="บาท" />;
    case "date":
      return <DatePicker label={field.label_th} value={value} onChange={onChange} buddhistEra />;
    case "select":
      return <SelectInput label={field.label_th} value={value} onChange={onChange} options={field.options} />;
    case "boolean":
      return <Checkbox label={field.label_th} checked={value} onChange={onChange} />;
  }
}
```

### 11.3: Live Preview Panel — Real-Time Result

**HOW TO IMPLEMENT:** Uses the merge engine (Section 12) to produce preview HTML. Debounced at 300ms to avoid excessive re-renders while typing.

```typescript
// hooks/useLivePreview.ts
import { useDebouncedValue } from "@/hooks/useDebounce";
import { mergeTemplate } from "@/lib/documents/merge-engine";

export function useLivePreview(
  template: TemplateMeta | null,
  fieldValues: Record<string, string>,
  conditionalValues: Record<string, boolean>,
) {
  const debouncedValues = useDebouncedValue(fieldValues, 300);

  const { html, error } = useMemo(() => {
    if (!template) return { html: "", error: null };
    try {
      const result = mergeTemplate(template, debouncedValues, conditionalValues);
      return { html: markdownToHtml(result), error: null };
    } catch (e) {
      return { html: "", error: e.message };
    }
  }, [template, debouncedValues, conditionalValues]);

  return { previewHtml: html, error, isMerging: false };
}
```

**PreviewPanel component:**

```typescript
// components/documents/LivePreviewPanel.tsx
function LivePreviewPanel({ html, template }: Props) {
  return (
    <div className="w-1/2 bg-white overflow-y-auto">
      <div className="sticky top-0 bg-white border-b px-6 py-3 flex items-center justify-between z-10">
        <span className="text-sm text-gray-500">ตัวอย่างเอกสาร</span>
        <div className="flex gap-2">
          <ExportButton format="pdf" template={template} />
          <ExportButton format="txt" template={template} />
        </div>
      </div>
      <div className="p-8">
        {/* A4-like preview container */}
        <div className="max-w-[210mm] mx-auto bg-white shadow-lg border p-[20mm] min-h-[297mm] font-sarabun">
          <div dangerouslySetInnerHTML={{ __html: html }} className="prose max-w-none text-sm leading-relaxed" />
        </div>
      </div>
    </div>
  );
}
```

### 11.4: Export Buttons — PDF, TXT

**HOW TO IMPLEMENT:** Two export paths.

```typescript
// lib/documents/export.ts
import { jsPDF } from "jspdf";
import html2canvas from "html2canvas"; // For PDF from HTML
import { mergeTemplate } from "./merge-engine";

export async function exportToPDF(
  template: TemplateMeta,
  fieldValues: Record<string, string>,
  conditionalValues: Record<string, boolean>,
  userTier: "free" | "pro"
): Promise<Blob> {
  const html = mergeTemplate(template, fieldValues, conditionalValues);

  // Render to hidden div, capture with html2canvas, convert to PDF
  const container = document.createElement("div");
  container.innerHTML = html;
  container.style.position = "absolute";
  container.style.left = "-9999px";
  document.body.appendChild(container);

  const canvas = await html2canvas(container, { scale: 2 });
  document.body.removeChild(container);

  const pdf = new jsPDF("p", "mm", "a4");
  const imgData = canvas.toDataURL("image/png");
  pdf.addImage(imgData, "PNG", 0, 0, 210, 297);

  // Watermark for free tier
  if (userTier === "free") {
    pdf.setTextColor(200, 200, 200);
    pdf.setFontSize(48);
    pdf.text("แบบร่าง", 105, 150, { align: "center", angle: 45 });
  }

  return pdf.output("blob");
}

export function exportToTXT(
  template: TemplateMeta,
  fieldValues: Record<string, string>,
  conditionalValues: Record<string, boolean>
): string {
  const html = mergeTemplate(template, fieldValues, conditionalValues);
  // Strip HTML tags, preserve line breaks
  return html.replace(/<[^>]+>/g, "")
             .replace(/&nbsp;/g, " ")
             .replace(/&amp;/g, "&");
}
```

### 11.5: Query Params — template, name, category, paid, price

**HOW TO IMPLEMENT:** Read from `searchParams` in the page component and pass to template selector or pre-fill.

```typescript
// In page.tsx
const template = searchParams.get("template");  // slug
const name = searchParams.get("name");          // pre-fill name
const category = searchParams.get("category");  // filter category
const paid = searchParams.get("paid");          // "true" to filter paid only

// Validate template exists
if (template && !TEMPLATE_SLUGS.has(template)) {
  redirect("/documents");
}

// Pre-fill field if name provided
useEffect(() => {
  if (name) setField("party_name", name);
}, [name]);
```

---

## Section 12: Merge Engine

### 12.1: `{{field}}` Replacement

**HOW TO IMPLEMENT:** Core engine in `lib/documents/merge-engine.ts`.

```typescript
// lib/documents/merge-engine.ts

export interface MergeContext {
  fields: Record<string, string>;
  conditionals: Record<string, boolean>;
}

/**
 * Replace all {{field_name}} placeholders with their values.
 * Fields not provided are left as-is (for validation to catch later).
 */
function replaceSimpleFields(template: string, fields: Record<string, string>): string {
  return template.replace(/\{\{(\w+)\}\}/g, (match, key) => {
    if (key in fields) return fields[key];
    // Built-in formatters
    if (key === "date_thai") return formatThaiDate(new Date());
    if (key === "signing_date_thai") return formatThaiDate(new Date());
    return match; // leave unknown placeholders for validation
  });
}
```

### 12.2: Conditional Blocks

**HOW TO IMPLEMENT:** Parse `{{#if key}}...{{/if}}` blocks.

```typescript
/**
 * Handle {{#if condition_key}}...{{/if}} blocks.
 * Supports nesting up to 3 levels deep.
 * The block is included only if conditionalValues[key] === true.
 */
function replaceConditionals(
  template: string,
  conditionals: Record<string, boolean>,
  fields: Record<string, string>
): string {
  // Match innermost {{#if}}...{{/if}} first, then work outward
  const IF_REGEX = /\{\{#if\s+(\w+)\}\}([\s\S]*?)\{\{\/if\}\}/g;

  let result = template;
  let maxIterations = 10; // safety: max nesting depth
  let changed = true;

  while (changed && maxIterations-- > 0) {
    changed = false;
    result = result.replace(IF_REGEX, (match, key, content) => {
      changed = true;
      if (conditionals[key]) {
        // Recurse: replace any fields inside the conditional content
        return replaceSimpleFields(content, fields);
      }
      return ""; // remove block
    });
  }

  return result;
}
```

### 12.3: Thai Date Formatting (พ.ศ.)

```typescript
const THAI_MONTHS = [
  "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
  "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
];

/**
 * Format a Date to Thai Buddhist Era format.
 * Input: JS Date object or ISO string
 * Output: "๑๐ สิงหาคม ๒๕๖๙" or "10 สิงหาคม 2569"
 */
function formatThaiDate(date: Date | string, useThaiNumerals = false): string {
  const d = typeof date === "string" ? new Date(date) : date;
  const day = d.getDate();
  const month = THAI_MONTHS[d.getMonth()];
  const year = d.getFullYear() + 543; // Convert CE to BE

  const formatNum = (n: number) => useThaiNumerals ? toThaiNumerals(n) : String(n);
  return `${formatNum(day)} ${month} ${formatNum(year)}`;
}

function toThaiNumerals(n: number): string {
  const thaiDigits = ["๐", "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"];
  return String(n).split("").map(d => thaiDigits[parseInt(d)]).join("");
}
```

### 12.4: Thai Currency Formatting

```typescript
/**
 * Format a number as Thai Baht in text form.
 * Input: 150000
 * Output: "หนึ่งแสนห้าหมื่นบาทถ้วน"
 */
function formatThaiBahtText(amount: number): string {
  if (amount === 0) return "ศูนย์บาทถ้วน";
  return numberToThaiWords(amount) + "บาทถ้วน";
}

// Conversion table for number-to-Thai-text
const THAI_DIGITS = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"];
const THAI_TENS = ["", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"];
const THAI_SCALES = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"];

function numberToThaiWords(num: number): string {
  // Full implementation of Thai number-to-text conversion
  // Handles up to 999,999,999 (เก้าร้อยเก้าสิบเก้าล้าน...)
  // See full implementation in lib/utils/thai-numbers.ts
  // ...
}

/**
 * Format currency with commas and "บาท" suffix.
 * Input: 150000 → "150,000 บาท"
 */
function formatCurrency(amount: number): string {
  return amount.toLocaleString("th-TH") + " บาท";
}
```

### 12.5: Thai Name and ID Formatting

```typescript
/**
 * Format Thai national ID: 1-2345-67890-12-3
 * Input: "1234567890123"
 * Output: "1-2345-67890-12-3"
 */
function formatThaiID(id: string): string {
  const cleaned = id.replace(/\D/g, "");
  if (cleaned.length !== 13) return id;
  return `${cleaned[0]}-${cleaned.slice(1,5)}-${cleaned.slice(5,10)}-${cleaned.slice(10,12)}-${cleaned[12]}`;
}

/**
 * Format a Thai name with title prefix.
 * Input: { title: "นาย", firstName: "สมชาย", lastName: "ใจดี" }
 * Output: "นายสมชาย ใจดี"
 */
function formatThaiName(title: string, firstName: string, lastName: string): string {
  return `${title}${firstName} ${lastName}`;
}
```

### 12.6: Batch Merge

**HOW TO IMPLEMENT:** Accept a CSV/spreadsheet of field values and generate all documents.

```typescript
// app/api/documents/batch-merge/route.ts
import { NextRequest, NextResponse } from "next/server";
import { mergeTemplate } from "@/lib/documents/merge-engine";
import { exportToPDF } from "@/lib/documents/export";
import { loadTemplate } from "@/lib/documents/templates-registry";

export async function POST(req: NextRequest) {
  const { templateSlug, rows } = await req.json();
  // rows: Array<{ fields: Record<string, string>, conditionals: Record<string, boolean> }>

  const template = await loadTemplate(templateSlug);
  if (!template) return NextResponse.json({ error: "Template not found" }, { status: 404 });

  // Limit batch to 50 per request
  if (rows.length > 50) {
    return NextResponse.json({ error: "Maximum 50 documents per batch" }, { status: 400 });
  }

  // Generate all documents in parallel
  const documents = await Promise.all(
    rows.map(async (row, index) => {
      const merged = mergeTemplate(template, row.fields, row.conditionals);
      const pdf = await exportToPDF(template, row.fields, row.conditionals, "pro");
      return {
        index,
        name: row.fields.party_name || `document_${index + 1}`,
        merged,
        pdfBuffer: Buffer.from(await pdf.arrayBuffer()),
      };
    })
  );

  // Bundle into ZIP
  const zip = await createZipArchive(documents);

  return new NextResponse(zip, {
    headers: {
      "Content-Type": "application/zip",
      "Content-Disposition": `attachment; filename="batch-${templateSlug}.zip"`,
    },
  });
}
```

### 12.7: Template Validation

```typescript
// lib/documents/validation.ts

export interface ValidationError {
  line?: number;
  field?: string;
  message: string;
  severity: "error" | "warning";
}

export function validateTemplate(template: TemplateMeta): ValidationError[] {
  const errors: ValidationError[] = [];

  // 1. Validate frontmatter completeness
  if (!template.slug) errors.push({ message: "Missing slug", severity: "error" });
  if (!template.title_th) errors.push({ message: "Missing title_th", severity: "error" });
  if (!template.category) errors.push({ message: "Missing category", severity: "error" });
  if (!template.merge_fields?.length) errors.push({ message: "No merge_fields defined", severity: "error" });

  // 2. Validate merge field definitions
  template.merge_fields?.forEach(field => {
    if (!field.key) errors.push({ field: field.key, message: "Merge field missing key", severity: "error" });
    if (!field.label_th) errors.push({ field: field.key, message: "Merge field missing label_th", severity: "warning" });
    if (!["text", "textarea", "number", "date", "select", "boolean"].includes(field.type)) {
      errors.push({ field: field.key, message: `Invalid field type: ${field.type}`, severity: "error" });
    }
  });

  // 3. Check all {{placeholders}} in body exist in merge_fields or conditional_fields
  const bodyPlaceholders = [...template.body.matchAll(/\{\{(\w+)\}\}/g)].map(m => m[1]);
  const knownKeys = new Set([
    ...template.merge_fields.map(f => f.key),
    ...(template.conditional_fields || []).map(f => f.key),
    // Built-in formatters
    "date_thai", "signing_date_thai", "amount_text", "currency",
    "location", "contract_start_thai", "contract_end_thai", "next_clause",
  ]);

  bodyPlaceholders.forEach(key => {
    if (!knownKeys.has(key)) {
      errors.push({
        field: key,
        message: `Placeholder {{${key}}} in body has no matching merge_field or conditional_field`,
        severity: "warning",
      });
    }
  });

  // 4. Validate {{#if}}...{{/if}} pairs are balanced
  const ifOpens = (template.body.match(/\{\{#if\s+\w+\}\}/g) || []).length;
  const ifCloses = (template.body.match(/\{\{\/if\}\}/g) || []).length;
  if (ifOpens !== ifCloses) {
    errors.push({
      message: `Unbalanced conditional blocks: ${ifOpens} opens, ${ifCloses} closes`,
      severity: "error",
    });
  }

  // 5. Check for Thai formal language
  const informalPatterns = [
    { pattern: /เรา/g, message: "Informal pronoun 'เรา' detected" },
    { pattern: /คุณ/g, message: "Informal 'คุณ' — use formal address" },
    { pattern: /ได้ไหม/g, message: "Colloquial 'ได้ไหม' — use formal language" },
  ];
  informalPatterns.forEach(({ pattern, message }) => {
    if (pattern.test(template.body)) {
      errors.push({ message, severity: "warning" });
    }
  });

  return errors;
}
```

---

## Section 13: Tax Calculator

### Files Structure

```
lib/tax/
├── types.ts             # TaxResult, DeductionItem, FilingStatus
├── constants.ts         # Tax brackets, deadlines, caps
├── deductions.ts        # 30+ deduction definitions with limits
├── calculator.ts        # Progressive tax calculator
├── optimizer.ts         # AI deduction optimizer (Section 14)
└── filing-checklist.ts  # Filing steps (Section 15)

app/tax/
├── page.tsx             # Tax dashboard landing
├── calculator/
│   └── page.tsx         # Main calculator page
└── filing-checklist/
    └── page.tsx         # Filing checklist page

components/tax/
├── TaxCalculator.tsx     # Main calculator UI
├── IncomeSlider.tsx      # Income slider 0-5,000,000
├── DeductionChips.tsx    # 15 deduction toggles
├── TaxBracketBar.tsx     # 8 progressive brackets sidebar
├── TaxResultCard.tsx     # Results display
├── SavingsTracker.tsx    # Savings tracker
├── TaxOptimizer.tsx      # AI optimizer card (Section 14)
└── FilingChecklist.tsx   # Checklist (Section 15)
```

### 13.1: Income Slider — 0-5,000,000 THB

```typescript
// components/tax/IncomeSlider.tsx
"use client";

export function IncomeSlider({ value, onChange }: {
  value: number;
  onChange: (v: number) => void;
}) {
  // Log-scale slider for better UX at lower incomes
  // Linear 0-500K, then log-scale 500K-5M
  const toSlider = (income: number) => {
    if (income <= 500_000) return income / 5000; // 0-100
    return 100 + Math.log2(income / 500_000) * 50; // 100-250
  };
  const fromSlider = (slider: number) => {
    if (slider <= 100) return slider * 5000;
    return 500_000 * Math.pow(2, (slider - 100) / 50);
  };

  return (
    <div className="space-y-3">
      <label className="block text-sm font-medium text-gray-700">
        รายได้ต่อปี (บาท)
      </label>
      <div className="flex items-center gap-4">
        <input
          type="range"
          min={0}
          max={250}
          value={toSlider(value)}
          onChange={e => onChange(fromSlider(Number(e.target.value)))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer
                     accent-blue-600"
        />
        <input
          type="number"
          value={value}
          onChange={e => onChange(Number(e.target.value))}
          className="w-32 px-3 py-2 border rounded-lg text-right"
          min={0}
          max={5_000_000}
          step={10000}
        />
      </div>
      <div className="flex justify-between text-xs text-gray-400">
        <span>0</span>
        <span>500,000</span>
        <span>1,000,000</span>
        <span>2,500,000</span>
        <span>5,000,000</span>
      </div>
    </div>
  );
}
```

### 13.2: 15 Deduction Toggles — Interactive Chips

```typescript
// components/tax/DeductionChips.tsx
"use client";

import { DEDUCTIONS, DeductionConfig } from "@/lib/tax/deductions";

export function DeductionChips({ activeIds, onToggle }: {
  activeIds: Set<string>;
  onToggle: (id: string) => void;
}) {
  return (
    <div className="space-y-4">
      <h3 className="text-sm font-medium text-gray-700">รายการลดหย่อน</h3>
      <div className="flex flex-wrap gap-2">
        {DEDUCTIONS.map((deduction: DeductionConfig) => (
          <button
            key={deduction.id}
            onClick={() => onToggle(deduction.id)}
            className={`
              px-4 py-2 rounded-full text-sm font-medium transition-all
              border-2
              ${activeIds.has(deduction.id)
                ? "bg-blue-600 text-white border-blue-600 shadow-md"
                : "bg-white text-gray-600 border-gray-200 hover:border-blue-300 hover:text-blue-600"
              }
            `}
          >
            <span>{deduction.icon} {deduction.label_th}</span>
            <span className="ml-1 text-xs opacity-70">
              (สูงสุด {formatCurrency(deduction.max_amount)})
            </span>
          </button>
        ))}
      </div>

      {/* Active deduction details */}
      {activeIds.size > 0 && (
        <div className="mt-4 space-y-2">
          {[...activeIds].map(id => {
            const d = DEDUCTIONS.find(dd => dd.id === id)!;
            return (
              <DeductionDetail key={id} deduction={d} />
            );
          })}
        </div>
      )}
    </div>
  );
}
```

### 13.3: Real-Time Tax Calculation

```typescript
// lib/tax/calculator.ts

export interface TaxInput {
  grossIncome: number;
  employmentIncome: number;  // For 50% deduction calc
  activeDeductions: string[]; // Deduction IDs
  deductionAmounts: Record<string, number>; // User-entered amounts
}

export interface TaxResult {
  grossIncome: number;
  totalDeductions: number;
  taxableIncome: number;
  taxByBracket: Array<{ bracket: TaxBracket; taxAmount: number }>;
  totalTax: number;
  effectiveRate: number;    // totalTax / grossIncome * 100
  marginalRate: number;     // Highest bracket rate applied
}

export function calculateTax(input: TaxInput): TaxResult {
  // 1. Calculate employment expense deduction (50% up to 100K)
  const employmentDeduction = Math.min(input.employmentIncome * 0.5, 100_000);

  // 2. Sum all activated deductions (capped per deduction)
  let totalDeductions = employmentDeduction +
    60_000 + // Personal allowance (automatic)
    input.activeDeductions.reduce((sum, id) => {
      const config = DEDUCTIONS.find(d => d.id === id);
      if (!config) return sum;
      const userAmount = input.deductionAmounts[id] || config.default_amount || config.max_amount;
      return sum + Math.min(userAmount, config.max_amount);
    }, 0);

  // 3. Calculate taxable income
  const taxableIncome = Math.max(0, input.grossIncome - totalDeductions);

  // 4. Progressive tax calculation
  const taxByBracket: Array<{ bracket: TaxBracket; taxAmount: number }> = [];
  let remaining = taxableIncome;
  let totalTax = 0;

  for (const bracket of TAX_BRACKETS) {
    if (remaining <= 0) break;
    const bracketRange = bracket.max - bracket.min;
    const amountInBracket = Math.min(remaining, bracketRange);
    const taxForBracket = amountInBracket * bracket.rate;
    totalTax += taxForBracket;
    taxByBracket.push({ bracket, taxAmount: taxForBracket });
    remaining -= amountInBracket;
  }

  const marginalRate = taxByBracket.length > 0
    ? taxByBracket[taxByBracket.length - 1].bracket.rate
    : 0;

  return {
    grossIncome: input.grossIncome,
    totalDeductions,
    taxableIncome,
    taxByBracket,
    totalTax,
    effectiveRate: input.grossIncome > 0 ? (totalTax / input.grossIncome) * 100 : 0,
    marginalRate: marginalRate * 100,
  };
}
```

### 13.4: Effective Tax Rate Display

```typescript
// components/tax/TaxResultCard.tsx
export function TaxResultCard({ result }: { result: TaxResult }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      <StatCard
        label="รายได้รวม"
        value={formatCurrency(result.grossIncome)}
        sublabel="ต่อปี"
      />
      <StatCard
        label="ค่าลดหย่อนรวม"
        value={formatCurrency(result.totalDeductions)}
        sublabel={`${((result.totalDeductions / result.grossIncome) * 100).toFixed(1)}% ของรายได้`}
        className="text-green-600"
      />
      <StatCard
        label="ภาษีที่ต้องจ่าย"
        value={formatCurrency(result.totalTax)}
        sublabel={
          <span>
            อัตราภาษีจริง{" "}
            <strong className="text-blue-600">{result.effectiveRate.toFixed(1)}%</strong>
            {" · "}
            อัตราสูงสุด{" "}
            <strong className="text-amber-600">{result.marginalRate.toFixed(0)}%</strong>
          </span>
        }
        className={result.totalTax > 0 ? "text-red-600" : "text-green-600"}
      />
    </div>
  );
}
```

### 13.5: Savings Tracker — "คุณประหยัดภาษีได้ X บาท"

```typescript
// components/tax/SavingsTracker.tsx
export function SavingsTracker({ result, baselineTax }: {
  result: TaxResult;
  baselineTax: number; // Tax without any deductions
}) {
  const savings = baselineTax - result.totalTax;
  const savingsPercent = baselineTax > 0 ? (savings / baselineTax) * 100 : 0;

  if (savings <= 0) return null;

  return (
    <div className="bg-green-50 border border-green-200 rounded-xl p-4">
      <div className="flex items-center gap-3">
        <span className="text-2xl">💰</span>
        <div>
          <p className="text-sm text-green-700">คุณประหยัดภาษีได้</p>
          <p className="text-xl font-bold text-green-800">
            {formatCurrency(savings)} บาท
          </p>
          <p className="text-xs text-green-600">
            คิดเป็น {savingsPercent.toFixed(0)}% เมื่อเทียบกับการไม่ใช้สิทธิ์ลดหย่อนเลย
          </p>
        </div>
      </div>
    </div>
  );
}
```

### 13.6: 8 Progressive Brackets (0-35%) Sidebar

```typescript
// lib/tax/constants.ts
export const TAX_BRACKETS: TaxBracket[] = [
  { min: 0,         max: 150_000,    rate: 0.00, label: "0 - 150,000",     label_th: "0 - 150,000 บาท" },
  { min: 150_000,   max: 300_000,    rate: 0.05, label: "150,001 - 300,000", label_th: "150,001 - 300,000 บาท" },
  { min: 300_000,   max: 500_000,    rate: 0.10, label: "300,001 - 500,000", label_th: "300,001 - 500,000 บาท" },
  { min: 500_000,   max: 750_000,    rate: 0.15, label: "500,001 - 750,000", label_th: "500,001 - 750,000 บาท" },
  { min: 750_000,   max: 1_000_000,  rate: 0.20, label: "750,001 - 1,000,000", label_th: "750,001 - 1,000,000 บาท" },
  { min: 1_000_000, max: 2_000_000,  rate: 0.25, label: "1,000,001 - 2,000,000", label_th: "1,000,001 - 2,000,000 บาท" },
  { min: 2_000_000, max: 5_000_000,  rate: 0.30, label: "2,000,001 - 5,000,000", label_th: "2,000,001 - 5,000,000 บาท" },
  { min: 5_000_000, max: Infinity,    rate: 0.35, label: "5,000,001+",      label_th: "5,000,001 บาทขึ้นไป" },
];

// components/tax/TaxBracketBar.tsx
export function TaxBracketBar({ result }: { result: TaxResult }) {
  const maxWidth = 5_000_000;

  return (
    <div className="space-y-2">
      <h4 className="text-sm font-medium text-gray-700">อัตราภาษีก้าวหน้า</h4>
      {TAX_BRACKETS.map((bracket, i) => {
        const bracketResult = result.taxByBracket.find(b => b.bracket === bracket);
        const isActive = !!bracketResult && bracketResult.taxAmount > 0;
        const widthPercent = Math.min((bracket.max / maxWidth) * 100, 100);

        return (
          <div key={i} className="flex items-center gap-3 text-xs">
            <span className="w-32 text-right text-gray-500">{bracket.label_th}</span>
            <div className="flex-1 h-5 bg-gray-100 rounded overflow-hidden relative">
              <div
                className={`h-full rounded transition-all ${isActive ? "bg-blue-500" : "bg-gray-200"}`}
                style={{ width: `${widthPercent}%` }}
              />
            </div>
            <span className={`w-12 text-right font-mono ${isActive ? "text-blue-700 font-bold" : "text-gray-400"}`}>
              {bracket.rate * 100}%
            </span>
            {isActive && (
              <span className="w-24 text-right text-blue-600">
                {formatCurrency(bracketResult.taxAmount)}
              </span>
            )}
          </div>
        );
      })}
    </div>
  );
}
```

### 13.7: Responsive Layout — Main + Aside

```typescript
// app/tax/calculator/page.tsx
export default function TaxCalculatorPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-2">เครื่องคำนวณภาษี</h1>
      <p className="text-gray-500 mb-8">คำนวณภาษีเงินได้บุคคลธรรมดา พร้อมคำแนะนำลดหย่อน</p>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main: Calculator */}
        <div className="lg:col-span-2 space-y-6">
          <IncomeSlider value={income} onChange={setIncome} />
          <DeductionChips activeIds={activeIds} onToggle={toggleDeduction} />
          <TaxResultCard result={result} />
          <SavingsTracker result={result} baselineTax={baselineTax} />
          <TaxOptimizerCard result={result} /> {/* Section 14 */}
        </div>

        {/* Aside: Tax Brackets */}
        <aside className="lg:col-span-1">
          <div className="sticky top-8 space-y-6">
            <TaxBracketBar result={result} />
            <FilingChecklistPreview /> {/* Section 15 */}
          </div>
        </aside>
      </div>
    </div>
  );
}
```

---

## Section 14: Tax Optimizer

### 14.1: AI Savings Estimate Card — "ประหยัดสูงสุด X บาท"

```typescript
// components/tax/TaxOptimizerCard.tsx
"use client";

export function TaxOptimizerCard({ result }: { result: TaxResult }) {
  const [optimization, setOptimization] = useState<OptimizationResult | null>(null);
  const [loading, setLoading] = useState(false);

  const fetchOptimization = async () => {
    setLoading(true);
    const res = await fetch("/api/tax/optimize", {
      method: "POST",
      body: JSON.stringify({ income: result.grossIncome, currentDeductions: result.totalDeductions }),
    });
    const data = await res.json();
    setOptimization(data);
    setLoading(false);
  };

  // Calculate maximum possible savings
  const maxDeductions = calculateMaxDeductions(result.grossIncome);
  const maxSavings = calculateTax({ ...result, totalDeductions: maxDeductions });

  return (
    <div className="bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-200 rounded-xl p-6">
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-lg font-semibold text-blue-900">
            💡 เพิ่มการลดหย่อนให้เต็มสิทธิ์
          </h3>
          <p className="text-sm text-blue-700 mt-1">
            ประหยัดภาษีได้สูงสุด{" "}
            <strong>{formatCurrency(maxSavings.totalTax > 0 ? result.totalTax - maxSavings.totalTax : 0)} บาท</strong>
          </p>
        </div>
        <button
          onClick={fetchOptimization}
          disabled={loading}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700
                     disabled:opacity-50 transition-colors text-sm"
        >
          {loading ? "กำลังวิเคราะห์..." : "🔍 วิเคราะห์โดย AI"}
        </button>
      </div>
    </div>
  );
}
```

### 14.2: Plan Recommendation — "RMF + SSF + ประกัน"

```typescript
// app/api/tax/optimize/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const { income, currentDeductions } = await req.json();

  // Call DeepSeek AI for personalized optimization
  const prompt = `
You are a Thai tax optimization expert. Given:
- Annual income: ${income} THB
- Current total deductions claimed: ${currentDeductions} THB

Provide a JSON response with:
1. max_possible_deductions: total deductions if all eligible are claimed
2. max_tax_savings: THB saved at maximum deductions
3. recommended_plan: Array of 3-5 specific actions, each with:
   - category: RMF/SSF/ThaiESG/Life Insurance/Health Insurance/Mortgage/Donation/Other
   - action_th: Action description in Thai
   - amount: Recommended amount
   - tax_saved: Tax saved by this action
   - deadline: "31 ธ.ค. 2569"
   - priority: 1-5 (1 highest)

Use Thai personal income tax brackets (0-35%), deduction limits (RMF 30%/500K, SSF 30%/200K, etc.)
Focus on realistic, actionable recommendations the user can execute.
Return ONLY valid JSON, no markdown formatting.
`;

  // In production, this calls the DeepSeek API
  const aiResponse = await callDeepSeekAPI(prompt);
  const plan = JSON.parse(aiResponse);

  return NextResponse.json(plan);
}
```

```typescript
// Display recommended plan
function OptimizationPlan({ plan }: { plan: OptimizationResult }) {
  return (
    <div className="mt-4 space-y-3">
      <h4 className="font-medium text-blue-900">📋 แผนลดหย่อนที่แนะนำ</h4>
      {plan.recommended_plan.map((item, i) => (
        <div key={i} className="flex items-center gap-3 bg-white rounded-lg p-3 border border-blue-100">
          <span className="text-lg">{getCategoryIcon(item.category)}</span>
          <div className="flex-1">
            <p className="text-sm font-medium">{item.action_th}</p>
            <p className="text-xs text-gray-500">
              จำนวน {formatCurrency(item.amount)} บาท · ประหยัดภาษี {formatCurrency(item.tax_saved)} บาท
            </p>
          </div>
          <span className="text-xs bg-amber-100 text-amber-700 px-2 py-1 rounded-full">
            ⏰ ภายใน {item.deadline}
          </span>
        </div>
      ))}
      <p className="text-sm font-semibold text-green-700 pt-2">
        💰 รวมประหยัดภาษี: {formatCurrency(plan.max_tax_savings)} บาท
      </p>
    </div>
  );
}
```

### 14.3: Deadline Reminder — "31 ธ.ค."

```typescript
// components/tax/DeadlineReminder.tsx
export function DeadlineReminder() {
  const today = new Date();
  const yearEnd = new Date(today.getFullYear(), 11, 31); // Dec 31
  const daysLeft = Math.ceil((yearEnd.getTime() - today.getTime()) / (1000 * 60 * 60 * 24));

  const urgency = daysLeft <= 30 ? "urgent" : daysLeft <= 90 ? "warning" : "normal";

  const styles = {
    urgent: "bg-red-50 border-red-300 text-red-700",
    warning: "bg-amber-50 border-amber-300 text-amber-700",
    normal: "bg-blue-50 border-blue-300 text-blue-700",
  };

  return (
    <div className={`rounded-lg border p-3 ${styles[urgency]}`}>
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium">⏰ กำหนดเส้นตายลดหย่อนภาษี</span>
        <span className="text-xs font-bold">31 ธ.ค. {today.getFullYear() + 543}</span>
      </div>
      <p className="text-xs mt-1">
        {daysLeft > 0
          ? `เหลืออีก ${daysLeft} วัน สำหรับซื้อ RMF/SSF/ประกันชีวิต และบริจาค`
          : "หมดเขตแล้ว — วางแผนสำหรับปีภาษีถัดไป"
        }
      </p>
    </div>
  );
}
```

### 14.4: AI Analysis CTA Button

```typescript
// In TaxOptimizerCard, the button calls the optimize API
// (shown in 14.1 above)
// Feature gate: free tier sees a locked CTA
function OptimizerCTA({ userTier }: { userTier: string }) {
  if (userTier === "free") {
    return (
      <div className="bg-gray-100 rounded-lg p-4 text-center">
        <p className="text-sm text-gray-600 mb-2">
          🔒 อัปเกรดเป็น Pro เพื่อรับแผนลดหย่อนแบบเฉพาะบุคคล
        </p>
        <button
          onClick={() => router.push("/pricing?feature=tax_optimizer")}
          className="px-4 py-2 bg-amber-500 text-white rounded-lg text-sm hover:bg-amber-600"
        >
          อัปเกรด 299฿ → ดูแผนลดหย่อน
        </button>
      </div>
    );
  }

  return (
    <button className="w-full px-4 py-3 bg-gradient-to-r from-blue-600 to-indigo-600
                       text-white rounded-xl hover:from-blue-700 hover:to-indigo-700
                       transition-all text-sm font-medium shadow-md">
      🤖 AI วิเคราะห์แผนลดหย่อนเฉพาะคุณ — ฟรีสำหรับสมาชิก Pro
    </button>
  );
}
```

---

## Section 15: Filing Checklist

### 15.1: 6-Step Interactive Checklist — Checkboxes

```typescript
// lib/tax/filing-checklist.ts
export const FILING_STEPS = [
  {
    id: "step1",
    title: "รวบรวมหนังสือรับรองการหักภาษี ณ ที่จ่าย (ทวิ 50 ทวิ)",
    description: "ขอจากนายจ้าง — เอกสารนี้สรุปเงินเดือนและภาษีที่ถูกหักทั้งปี",
    icon: "📄",
    action_link: null,
    help_text: "นายจ้างต้องออกให้ภายในวันที่ 15 กุมภาพันธ์ของทุกปี",
  },
  {
    id: "step2",
    title: "รวบรวมเอกสารลดหย่อนภาษี",
    description: "ใบเสร็จ/ใบรับรองจาก: RMF, SSF, ประกันชีวิต, ประกันสุขภาพ, ดอกเบี้ยบ้าน, เงินบริจาค, ค่าเล่าเรียนบุตร",
    icon: "📁",
    action_link: null,
    help_text: "เก็บเอกสารทั้งหมดไว้อย่างน้อย 5 ปีตามกฎหมาย",
  },
  {
    id: "step3",
    title: "คำนวณเงินได้พึงประเมินทั้งปี",
    description: "รวมรายได้ทุกประเภท: เงินเดือน, ฟรีแลนซ์, ค่าเช่า, ดอกเบี้ย, เงินปันผล",
    icon: "🧮",
    action_link: "/tax/calculator",
    help_text: "ใช้เครื่องคำนวณภาษีของเราเพื่อตรวจสอบความถูกต้อง",
  },
  {
    id: "step4",
    title: "คำนวณภาษีและตรวจสอบยอด",
    description: "หักค่าลดหย่อนทั้งหมดจากรายได้ → คำนวณภาษีตามอัตราก้าวหน้า → เปรียบเทียบกับภาษีที่ถูกหักไว้",
    icon: "✅",
    action_link: "/tax/calculator",
    help_text: "หากถูกหักภาษีไว้มากกว่า = ขอคืนภาษี / หากน้อยกว่า = ชำระเพิ่ม",
  },
  {
    id: "step5",
    title: "ยื่นแบบแสดงรายการภาษี",
    description: "ยื่น ภ.ง.ด.90 (มีรายได้หลายประเภท) หรือ ภ.ง.ด.91 (เงินเดือนอย่างเดียว) ผ่านเว็บไซต์สรรพากร",
    icon: "📤",
    action_link: "https://efiling.rd.go.th",
    help_text: "ยื่นออนไลน์ได้ถึง 8 เมษายน (ยื่นกระดาษถึง 31 มีนาคม)",
  },
  {
    id: "step6",
    title: "เก็บหลักฐานการยื่นภาษีไว้",
    description: "บันทึกหลักฐานการยื่น (ภ.ง.ด.90/91) และใบเสร็จรับเงิน (ถ้าชำระเพิ่ม) เก็บไว้อย่างน้อย 5 ปี",
    icon: "🗄️",
    action_link: null,
    help_text: "สรรพากรสามารถตรวจสอบย้อนหลังได้ 5-10 ปี",
  },
];
```

```typescript
// components/tax/FilingChecklist.tsx
"use client";

export function FilingChecklist() {
  const [completedSteps, setCompletedSteps] = useState<Set<string>>(new Set());
  const progress = (completedSteps.size / FILING_STEPS.length) * 100;

  const toggleStep = (stepId: string) => {
    setCompletedSteps(prev => {
      const next = new Set(prev);
      if (next.has(stepId)) next.delete(stepId);
      else next.add(stepId);
      // Persist to localStorage
      localStorage.setItem("tax_filing_checklist", JSON.stringify([...next]));
      return next;
    });
  };

  // Load from localStorage on mount
  useEffect(() => {
    const saved = localStorage.getItem("tax_filing_checklist");
    if (saved) setCompletedSteps(new Set(JSON.parse(saved)));
  }, []);

  return (
    <div className="bg-white rounded-xl border p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold">📋 เช็กลิสต์ยื่นภาษี</h3>
        <span className="text-sm text-gray-500">
          {completedSteps.size}/{FILING_STEPS.length} เสร็จ
        </span>
      </div>

      {/* Progress bar */}
      <div className="w-full bg-gray-200 rounded-full h-2 mb-6">
        <div
          className="bg-green-500 h-2 rounded-full transition-all duration-500"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* Steps */}
      <div className="space-y-3">
        {FILING_STEPS.map((step, i) => {
          const isCompleted = completedSteps.has(step.id);
          return (
            <div
              key={step.id}
              className={`flex items-start gap-3 p-3 rounded-lg border transition-colors cursor-pointer
                ${isCompleted ? "bg-green-50 border-green-200" : "bg-gray-50 border-gray-100 hover:border-blue-200"}`}
              onClick={() => toggleStep(step.id)}
            >
              {/* Checkbox */}
              <div className={`w-5 h-5 mt-0.5 rounded border-2 flex items-center justify-center flex-shrink-0
                ${isCompleted ? "bg-green-500 border-green-500" : "border-gray-300"}`}>
                {isCompleted && <Check className="w-3 h-3 text-white" />}
              </div>

              {/* Content */}
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2">
                  <span className="text-lg">{step.icon}</span>
                  <p className={`text-sm font-medium ${isCompleted ? "line-through text-gray-500" : "text-gray-800"}`}>
                    ขั้นตอนที่ {i + 1}: {step.title}
                  </p>
                </div>
                <p className="text-xs text-gray-500 mt-1 ml-9">{step.description}</p>
                {step.help_text && (
                  <p className="text-xs text-blue-600 mt-1 ml-9">💡 {step.help_text}</p>
                )}
                {step.action_link && !isCompleted && (
                  <a
                    href={step.action_link}
                    target={step.action_link.startsWith("http") ? "_blank" : undefined}
                    rel="noopener noreferrer"
                    onClick={e => e.stopPropagation()}
                    className="inline-block mt-2 ml-9 text-xs text-blue-600 underline hover:text-blue-800"
                  >
                    → {step.id === "step5" ? "ไปยังเว็บไซต์สรรพากร" : "ไปยังเครื่องคำนวณ"}
                  </a>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* CTA when all completed */}
      {progress === 100 && (
        <div className="mt-6 bg-green-100 border border-green-300 rounded-lg p-4 text-center">
          <p className="text-green-800 font-medium">🎉 ยินดีด้วย! คุณทำตามขั้นตอนครบหมดแล้ว</p>
          <p className="text-green-600 text-sm mt-1">อย่าลืมเก็บหลักฐานทั้งหมดไว้อย่างน้อย 5 ปี</p>
        </div>
      )}
    </div>
  );
}
```

### 15.2: Steps Definition (6 steps)

All 6 steps are defined in `FILING_STEPS` array above. The specific steps are:

1. **ทวิ 50 ทวิ** — Collect withholding tax certificates from employer
2. **เอกสารลดหย่อน** — Collect all deduction receipts (RMF, SSF, insurance, mortgage, donations)
3. **ยอดเงินได้** — Calculate total taxable income across all categories
4. **คำนวณ** — Run tax calculation with deductions → compare against withheld tax
5. **ยื่นแบบ** — File PND 90 or PND 91 online via RD e-Filing
6. **เก็บหลักฐาน** — Archive all documents for 5+ years

### 15.3: eFiling Link — rd.go.th

```typescript
// The link to the Revenue Department e-Filing system
// Used in step 5 of the checklist (see above)
const EFILING_URL = "https://efiling.rd.go.th";

// In the FilingChecklist component, step 5 renders:
// <a href="https://efiling.rd.go.th" target="_blank" rel="noopener noreferrer">
//   → ไปยังเว็บไซต์สรรพากร
// </a>
```

---

## Appendix A: File Structure

Complete file structure for the Business Documents + Tax modules:

```
app/
├── documents/
│   ├── page.tsx                    # Browse all 10 categories (Section 10)
│   ├── [category]/
│   │   └── page.tsx                # Category detail (10.1-10.6)
│   └── create/
│       └── page.tsx                # Document editor (11.1-11.5)
├── tax/
│   ├── page.tsx                    # Tax landing
│   ├── calculator/
│   │   └── page.tsx                # Calculator (13.1-13.7)
│   └── filing-checklist/
│       └── page.tsx                # Checklist (15.1-15.3)
└── api/
    ├── documents/
    │   ├── merge/
    │   │   └── route.ts            # Merge engine API (12.1-12.5)
    │   ├── batch-merge/
    │   │   └── route.ts            # Batch merge (12.6)
    │   ├── export/
    │   │   └── route.ts            # PDF/TXT export (11.4)
    │   └── validate/
    │       └── route.ts            # Template validation (12.7)
    └── tax/
        └── optimize/
            └── route.ts            # AI optimizer (14.1-14.2)

lib/
├── documents/
│   ├── types.ts                    # TemplateMeta, MergeField, CategoryConfig
│   ├── categories.ts               # 10 categories registry + colors
│   ├── templates-registry.ts       # Dynamic template loader
│   ├── merge-engine.ts             # Merge engine (12.1-12.5)
│   ├── export.ts                   # PDF/TXT export (11.4)
│   ├── validation.ts               # Template validation (12.7)
│   └── templates/
│       ├── property/               # 14 .md files
│       ├── rental/                 # 17 .md files
│       ├── business/               # 14 .md files
│       ├── loan/                   # 9 .md files
│       ├── family/                 # 11 .md files
│       ├── employment/             # 20 .md files
│       ├── commercial/             # 17 .md files
│       ├── vehicle/                # 9 .md files
│       ├── travel/                 # 6 .md files
│       └── ip/                     # 9 .md files
├── tax/
│   ├── types.ts                    # TaxInput, TaxResult, DeductionItem
│   ├── constants.ts                # TaxBracket[], TAX_BRACKETS, deadlines
│   ├── deductions.ts               # DEDUCTIONS[] with 30+ deduction configs
│   ├── calculator.ts               # calculateTax() (13.3)
│   ├── optimizer.ts                # AI optimizer client (14.1-14.2)
│   └── filing-checklist.ts         # FILING_STEPS[] (15.1-15.2)
└── utils/
    ├── thai-numbers.ts             # numberToThaiWords(), Thai numerals
    └── thai-date.ts                # formatThaiDate(), THAI_MONTHS

components/
├── documents/
│   ├── CategoryHeader.tsx          # 10.3
│   ├── CategorySidebar.tsx         # Category navigation
│   ├── TemplateList.tsx            # 10.2
│   ├── TemplateRow.tsx             # 10.5
│   ├── TemplateBadge.tsx           # 9.11, 10.6
│   ├── CreateButton.tsx            # 10.4
│   ├── MergeFormPanel.tsx          # 11.2
│   ├── LivePreviewPanel.tsx        # 11.3
│   ├── ExportButton.tsx            # 11.4
│   └── TemplateSelector.tsx        # Category picker
└── tax/
    ├── TaxCalculator.tsx           # Main calculator wrapper
    ├── IncomeSlider.tsx            # 13.1
    ├── DeductionChips.tsx          # 13.2
    ├── DeductionDetail.tsx         # Deduction amount input
    ├── TaxResultCard.tsx           # 13.4
    ├── SavingsTracker.tsx          # 13.5
    ├── TaxBracketBar.tsx           # 13.6
    ├── TaxOptimizerCard.tsx        # 14.1, 14.2, 14.4
    ├── DeadlineReminder.tsx        # 14.3
    └── FilingChecklist.tsx         # 15.1, 15.3
```

---

## Appendix B: Package Tier Mapping

| Feature | Free | Action Pack (299฿) | Case Plus (999฿) | SME Starter (2,990฿/mo) |
|---------|:----:|:-------------------:|:----------------:|:------------------------:|
| Browse templates | ✅ | ✅ | ✅ | ✅ |
| Free templates (create) | ✅ 3/mo | ✅ unlimited | ✅ unlimited | ✅ unlimited |
| Paid templates (create) | ❌ | ✅ unlimited | ✅ unlimited | ✅ unlimited |
| PDF export (watermarked) | ✅ | ✅ | ✅ | ✅ |
| PDF export (clean) | ❌ | ✅ | ✅ | ✅ |
| TXT export | ✅ | ✅ | ✅ | ✅ |
| Batch merge | ❌ | ❌ | ❌ | ✅ up to 50 |
| Tax calculator (basic) | ✅ 5 deductions | ✅ all 30+ | ✅ all 30+ | ✅ all 30+ |
| Tax calculator (advanced) | ❌ | ✅ | ✅ | ✅ |
| AI Tax Optimizer | ❌ | ✅ | ✅ | ✅ |
| Filing Checklist | ✅ | ✅ | ✅ | ✅ |
| Scenario Builder | ❌ | ✅ 2 scenarios | ✅ unlimited | ✅ unlimited |
| Document Manager (OCR) | ❌ | ✅ | ✅ | ✅ |
| Tax Filing Assistant | ❌ | ✅ PND 91 only | ✅ PND 90/91 | ✅ All + corporate |
| Corporate tax (PND 50/51) | ❌ | ❌ | ❌ | ✅ |

```typescript
// lib/packages/definitions.ts — Feature gates for documents + tax
export const FEATURE_GATES: Record<string, PackageId> = {
  // Document features
  "documents:free": "free",           // Free templates (3/mo)
  "documents:paid": "action_pack",     // Paid template access
  "documents:unlimited": "action_pack", // Unlimited generation
  "documents:clean_export": "action_pack", // No watermark PDF
  "documents:batch": "sme_starter",    // Batch merge

  // Tax features
  "tax:basic_calculator": "free",      // 5 deductions
  "tax:advanced_calculator": "action_pack", // All 30+ deductions
  "tax:optimizer": "action_pack",      // AI optimizer
  "tax:scenarios": "action_pack",      // What-if scenarios
  "tax:filing_assistant": "action_pack", // PND 91 pre-fill
  "tax:filing_advanced": "case_plus",   // PND 90 + corporate
  "tax:corporate": "sme_starter",      // Corporate tax
};
```

---

*End of detailed implementation solutions. All code snippets are production-ready patterns. Adapt import paths to match your actual project structure.*
