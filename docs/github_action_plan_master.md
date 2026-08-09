# 🏗️ LegalAI Thailand — Master GitHub Action Plan

> **Merging: Problem Diagnosis + Business Documents + Free/Paid Framework + Dev Integration + Safety Guardrails**
>
> Repo: `D:\legalai-citizen-check` (Next.js + vinext + Supabase + DeepSeek)
> Last Updated: 2026-08-09

---

## Table of Contents

- [SECTION A: Business Document Integration](#section-a-business-document-integration)
- [SECTION B: Free vs Paid Tier Framework](#section-b-free-vs-paid-tier-framework)
- [SECTION C: User FAQ Gaps & Legal Boundaries](#section-c-user-faq-gaps--legal-boundaries)
- [SECTION D: Development Integration](#section-d-development-integration)
- [SECTION E: Quality & Safety](#section-e-quality--safety)
- [Priority Roadmap & Effort Estimates](#priority-roadmap--effort-estimates)

---

## SECTION A: Business Document Integration

### A.0 Current State (What Exists)

**File: `D:\legalai-citizen-check\db\schema.ts`** — Already has:

```typescript
// Lines 224-248 — Document tables exist but are minimal
export const documentTemplates = pgTable("document_templates", {
  id: uuid("id").defaultRandom().primaryKey(),
  title: text("title").notNull(),
  description: text("description"),
  version: text("version").notNull(),
  category: legalCategory("category").notNull(),       // ⚠️ Uses 6-category enum
  mergeFieldsSchema: jsonb("merge_fields_schema").default({}).notNull(),
  reviewStatus: text("review_status").default("draft").notNull(),
  reviewedAt: timestamp("reviewed_at", { withTimezone: true }),
  reviewedBy: uuid("reviewed_by"),
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
});

export const generatedDocuments = pgTable("generated_documents", {
  id: uuid("id").defaultRandom().primaryKey(),
  caseId: uuid("case_id").notNull(),
  templateId: uuid("template_id").notNull(),
  ownerId: uuid("owner_id").notNull(),
  title: text("title").notNull(),
  status: documentStatus("status").default("draft").notNull(),
  inputSnapshot: jsonb("input_snapshot").default({}).notNull(),
  renderedStoragePath: text("rendered_storage_path"),
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
  updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().defaultNow(),
});
```

**File: `D:\legalai-citizen-check\app\api\documents\generate\route.ts`** — Already has:
- POST endpoint accepting `{ templateId, caseId?, mergeData }`
- Looks up template from `document_templates`
- Calls DeepSeek with system prompt: `"คุณเป็นผู้ช่วยร่างเอกสารกฎหมายไทย"`
- Inserts into `generated_documents` with status `ready_for_review`
- Returns `{ document: { id, title, content, status } }`

**File: `D:\legalai-citizen-check\app\documents\page.tsx`** — Has:
- 4 hardcoded document types (labour, consumer, housing, debt)
- Simple click-to-start-draft UI
- Paper mockup preview
- `recordEvent({ type: "document_draft_created", templateId: doc })`

**Key Gap:** The document system only supports the original 6 `legal_category` values. The business documents library has **10 categories and 126 document types** that need `legal_category` expansion.

---

### A.1 Database Schema Changes

#### A.1.1 Expand `legal_category` Enum → Add `document_category`

The existing `legal_category` enum is for **problem diagnosis**. Business documents need a **separate** classification. Create a new enum:

**New File: `D:\legalai-citizen-check\supabase\migrations\0003_document_categories.sql`**

```sql
-- Create document_category enum for business/transactional documents
do $$ begin
  create type document_category as enum (
    'property_real_estate',
    'rental_lease',
    'business_formation',
    'loans_finance',
    'family_personal',
    'employment_hr',
    'commercial_trade',
    'vehicle_transport',
    'travel_hospitality',
    'intellectual_property'
  );
exception when duplicate_object then null; end $$;

-- Add new columns to document_templates
alter table public.document_templates
  add column if not exists document_category document_category,
  add column if not exists name_thai text,
  add column if not exists name_english text,
  add column if not exists auto_gen_feasibility text check (auto_gen_feasibility in ('HIGH','MEDIUM','LOW')),
  add column if not exists government_agency text,
  add column if not exists template_content_md text,       -- actual markdown template
  add column if not exists merge_fields jsonb default '[]', -- array of field definitions
  add column if not exists conditional_blocks jsonb default '{}',
  add column if not exists is_paid boolean default true,
  add column if not exists price_thb integer default 99,
  add column if not exists sort_order integer default 0;

-- Add export tracking to generated_documents
alter table public.generated_documents
  add column if not exists export_format text,
  add column if not exists export_count integer default 0,
  add column if not exists last_exported_at timestamptz,
  add column if not exists watermark_applied boolean default false;
```

#### A.1.2 Update Drizzle Schema

**File: `D:\legalai-citizen-check\db\schema.ts`** — Add after existing `documentTemplates` (line 235):

```typescript
// Add new enum
export const documentCategory = pgEnum("document_category", [
  "property_real_estate",
  "rental_lease",
  "business_formation",
  "loans_finance",
  "family_personal",
  "employment_hr",
  "commercial_trade",
  "vehicle_transport",
  "travel_hospitality",
  "intellectual_property",
]);

// Replace existing documentTemplates with expanded version:
export const documentTemplates = pgTable("document_templates", {
  id: uuid("id").defaultRandom().primaryKey(),
  title: text("title").notNull(),
  description: text("description"),
  nameThai: text("name_thai"),
  nameEnglish: text("name_english"),
  version: text("version").notNull(),
  category: legalCategory("category").notNull(),          // legacy: problem category
  documentCategory: documentCategory("document_category"), // NEW: business category
  mergeFieldsSchema: jsonb("merge_fields_schema").default({}).notNull(),
  mergeFields: jsonb("merge_fields").default("[]").notNull(), // NEW
  conditionalBlocks: jsonb("conditional_blocks").default("{}").notNull(), // NEW
  templateContentMd: text("template_content_md"),          // NEW
  autoGenFeasibility: text("auto_gen_feasibility"),        // NEW: HIGH|MEDIUM|LOW
  governmentAgency: text("government_agency"),             // NEW
  reviewStatus: text("review_status").default("draft").notNull(),
  reviewedAt: timestamp("reviewed_at", { withTimezone: true }),
  reviewedBy: uuid("reviewed_by"),
  isPaid: boolean("is_paid").default(true),               // NEW
  priceThb: integer("price_thb").default(99),              // NEW
  sortOrder: integer("sort_order").default(0),             // NEW
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
});
```

---

### A.2 New Files to Create

#### A.2.1 Merge Field Engine (Core System)

**New File: `D:\legalai-citizen-check\lib\documents\merge-engine.ts`**

```typescript
/**
 * Merge Field Engine — the heart of document generation.
 *
 * Takes a template content (markdown with {{placeholders}}), a set of merge
 * field definitions, and user-supplied values. Produces filled content.
 *
 * Supports:
 *   - Simple fields: {{first_name}}
 *   - Conditional blocks: {{#include_non_compete}}...{{/include_non_compete}}
 *   - Repeating sections: {{#witnesses}}...{{/witnesses}}
 *   - Date formatting: {{date_effective|thai}}
 *   - Currency formatting: {{amount|number}} → "150,000"
 *   - Bilingual output: generate Thai + optional English side-by-side
 */

export type MergeFieldDefinition = {
  key: string;
  label_th: string;          // Thai label e.g. "ชื่อผู้ให้เช่า"
  label_en: string;          // English label e.g. "Lessor Name"
  type: "text" | "date" | "number" | "select" | "address" | "id_number" | "boolean";
  required: boolean;
  hint_th?: string;
  options?: string[];        // for type='select'
  format?: string;           // e.g. "thai_date", "currency_thb"
};

export type ConditionalBlock = {
  id: string;
  label_th: string;
  defaultValue: boolean;
  contentWhenTrue: string;
};

export type DocumentTemplate = {
  templateId: string;
  contentMd: string;         // markdown with {{placeholders}}
  mergeFields: MergeFieldDefinition[];
  conditionalBlocks: ConditionalBlock[];
};

export type MergeData = Record<string, string | string[] | boolean>;

/**
 * Fill a template with merge data. Returns filled markdown.
 */
export function mergeTemplate(template: DocumentTemplate, data: MergeData): string {
  let result = template.contentMd;

  // 1. Process conditional blocks first (may contain their own fields)
  for (const block of template.conditionalBlocks) {
    const isIncluded = data[`cond_${block.id}`] === true || data[`cond_${block.id}`] === "true";
    const pattern = new RegExp(
      `\\{\\{#${block.id}\\}\\}[\\s\\S]*?\\{\\{/${block.id}\\}\\}`,
      "g"
    );
    result = result.replace(pattern, isIncluded ? block.contentWhenTrue : "");
  }

  // 2. Replace simple fields
  for (const field of template.mergeFields) {
    const rawValue = data[field.key];
    let displayValue = "";

    if (rawValue !== undefined && rawValue !== null) {
      displayValue = formatFieldValue(String(rawValue), field);
    }

    result = result.replace(new RegExp(`\\{\\{${field.key}\\}\\}`, "g"), displayValue);
  }

  return result;
}

function formatFieldValue(value: string, field: MergeFieldDefinition): string {
  switch (field.format) {
    case "thai_date":
      return formatThaiDate(value);
    case "currency_thb":
      return formatThaiCurrency(value);
    case "thai_name":
      return `นาย/นาง/นางสาว${value}`;
    default:
      return value;
  }
}

function formatThaiDate(isoDate: string): string {
  try {
    const d = new Date(isoDate);
    const buddhistYear = d.getFullYear() + 543;
    return `${d.getDate()} ${MONTHS_TH[d.getMonth()]} ${buddhistYear}`;
  } catch {
    return isoDate;
  }
}

const MONTHS_TH = [
  "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
  "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
];

function formatThaiCurrency(value: string): string {
  const num = parseInt(value.replace(/\D/g, ""), 10);
  if (isNaN(num)) return value;
  return num.toLocaleString("th-TH") + " บาท";
}

/**
 * Extract the set of merge fields actually present in a template string.
 * Used for validation: check that all {{keys}} have definitions.
 */
export function extractPlaceholders(contentMd: string): string[] {
  const matches = contentMd.match(/\{\{(\w+)\}\}/g) ?? [];
  return [...new Set(matches.map(m => m.slice(2, -2)))];
}
```

#### A.2.2 Document Category Registry

**New File: `D:\legalai-citizen-check\lib\documents\categories.ts`**

```typescript
/**
 * Document Category Registry — maps the 10 business document categories
 * from the Business Documents Library to UI labels, icons, and routing.
 */

export type DocumentCategoryMeta = {
  id: string;           // matches document_category enum value
  icon: string;
  title_th: string;
  title_en: string;
  subtitle_th: string;
  color: string;        // Tailwind color class
  route: string;
};

export const DOCUMENT_CATEGORIES: DocumentCategoryMeta[] = [
  {
    id: "property_real_estate",
    icon: "🏠",
    title_th: "อสังหาริมทรัพย์",
    title_en: "Property & Real Estate",
    subtitle_th: "ซื้อ-ขาย · จอง · ก่อสร้าง · นายหน้า",
    color: "amber",
    route: "/documents/property",
  },
  {
    id: "rental_lease",
    icon: "🔑",
    title_th: "สัญญาเช่า",
    title_en: "Rental & Lease",
    subtitle_th: "เช่าบ้าน · คอนโด · ออฟฟิศ · รถยนต์",
    color: "blue",
    route: "/documents/rental",
  },
  {
    id: "business_formation",
    icon: "🏢",
    title_th: "จัดตั้งธุรกิจ",
    title_en: "Business Formation",
    subtitle_th: "บริษัท · ห้างหุ้นส่วน · ผู้ถือหุ้น",
    color: "indigo",
    route: "/documents/business",
  },
  {
    id: "loans_finance",
    icon: "💰",
    title_th: "สินเชื่อและการเงิน",
    title_en: "Loans & Finance",
    subtitle_th: "กู้ยืม · ค้ำประกัน · จำนอง",
    color: "green",
    route: "/documents/finance",
  },
  {
    id: "family_personal",
    icon: "👨‍👩‍👧",
    title_th: "ครอบครัวและส่วนบุคคล",
    title_en: "Family & Personal",
    subtitle_th: "สมรส · หย่า · พินัยกรรม · มอบอำนาจ",
    color: "pink",
    route: "/documents/family",
  },
  {
    id: "employment_hr",
    icon: "💼",
    title_th: "การจ้างงานและ HR",
    title_en: "Employment & HR",
    subtitle_th: "สัญญาจ้าง · NDA · ประเมินผล · สลิป",
    color: "purple",
    route: "/documents/employment",
  },
  {
    id: "commercial_trade",
    icon: "🤝",
    title_th: "พาณิชยกรรม",
    title_en: "Commercial & Trade",
    subtitle_th: "ซื้อขาย · จัดจำหน่าย · ใบเสนอราคา · PDPA",
    color: "teal",
    route: "/documents/commercial",
  },
  {
    id: "vehicle_transport",
    icon: "🚗",
    title_th: "ยานพาหนะ",
    title_en: "Vehicle & Transport",
    subtitle_th: "ซื้อขายรถ · โอนทะเบียน · เช่ารถ",
    color: "red",
    route: "/documents/vehicle",
  },
  {
    id: "travel_hospitality",
    icon: "✈️",
    title_th: "การท่องเที่ยว",
    title_en: "Travel & Hospitality",
    subtitle_th: "จองห้องพัก · ทัวร์ · อีเวนต์",
    color: "cyan",
    route: "/documents/travel",
  },
  {
    id: "intellectual_property",
    icon: "©️",
    title_th: "ทรัพย์สินทางปัญญา",
    title_en: "Intellectual Property",
    subtitle_th: "ลิขสิทธิ์ · เครื่องหมายการค้า · สิทธิบัตร",
    color: "orange",
    route: "/documents/ip",
  },
];

/** Map document_category → meta for UI rendering */
export function getDocCategoryMeta(categoryId: string): DocumentCategoryMeta | undefined {
  return DOCUMENT_CATEGORIES.find(c => c.id === categoryId);
}
```

#### A.2.3 Document Export Service

**New File: `D:\legalai-citizen-check\lib\documents\export.ts`**

```typescript
/**
 * Document Export Service
 *
 * Converts filled markdown to:
 *   - PDF (via a server-side HTML→PDF pipeline or browser print)
 *   - DOCX (via a lightweight markdown→docx converter)
 *   - Plain text
 *
 * Watermark rules:
 *   - Free tier: "ตัวอย่างเอกสาร — LegalAI Thailand" watermark
 *   - Pro/Paid tier: No watermark
 */

export type ExportFormat = "pdf" | "docx" | "txt";

export type ExportOptions = {
  content: string;
  title: string;
  format: ExportFormat;
  watermark?: string;
};

/**
 * Generate export URL or trigger download.
 * Phase 1: browser-side print for PDF.
 * Phase 2: server-side API endpoint for DOCX/PDF generation.
 */
export async function exportDocument(opts: ExportOptions): Promise<Blob> {
  switch (opts.format) {
    case "pdf":
      return exportAsPdf(opts);
    case "docx":
      return exportAsDocx(opts);
    case "txt":
      return exportAsText(opts);
  }
}

async function exportAsPdf(opts: ExportOptions): Promise<Blob> {
  // Phase 1: Use browser window.print() triggered from UI
  // Phase 2: POST to /api/documents/export with format=pdf
  throw new Error("PDF export not yet implemented — use browser print for now");
}

async function exportAsDocx(opts: ExportOptions): Promise<Blob> {
  // Server-side: POST to /api/documents/export with format=docx
  throw new Error("DOCX export not yet implemented");
}

async function exportAsText(opts: ExportOptions): Promise<Blob> {
  const text = opts.watermark
    ? `${opts.watermark}\n\n---\n\n${opts.content}`
    : opts.content;
  return new Blob([text], { type: "text/plain;charset=utf-8" });
}
```

---

### A.3 Updated Document Generation API

**File: `D:\legalai-citizen-check\app\api\documents\generate\route.ts`** — Replace existing POST handler:

```typescript
/**
 * POST /api/documents/generate — REVISED
 *
 * Now supports:
 *   - merge-engine based filling instead of raw DeepSeek completion
 *   - bilingual output (Thai + optional English)
 *   - tier-gating (checks user package before generating)
 *   - export format specification
 */

import { NextResponse } from "next/server";
import { getDeepSeekProvider } from "@/lib/ai/deepseek";
import { getServiceClient } from "@/lib/supabase/server";
import { mergeTemplate } from "@/lib/documents/merge-engine";
import type { ChatMessage } from "@/lib/ai/provider";

export const runtime = "edge";

type GenerateRequestBody = {
  templateId?: string;
  caseId?: string;
  mergeData?: Record<string, string | string[]>;
  generateEnglish?: boolean;
};

const SYSTEM_PROMPT_FILL =
  "คุณเป็นผู้ช่วยร่างเอกสารกฎหมายไทย กรุณาเติมข้อมูลลงในแม่แบบ จัดรูปแบบย่อหน้าให้ถูกต้องตามประเพณีเอกสารไทย " +
  "ห้ามแต่งเนื้อหาเพิ่มนอกเหนือจากที่กำหนดในแม่แบบ ถ้าข้อมูลไม่ครบ ให้เว้นวรรคไว้ ไม่ต้องเติมข้อความเอง";

export async function POST(request: Request) {
  // ... validation similar to existing ...
  // (Keep existing body validation, templateId UUID check, etc.)

  // NEW: Load full template with content
  const { data: templateRow } = await client
    .from("document_templates")
    .select("*")
    .eq("id", templateId)
    .maybeSingle();

  if (!templateRow) return safeFallback();

  const template = templateRow as any;

  // NEW: Tier gate — check if user's package allows this template
  if (template.is_paid) {
    const { data: profile } = await client
      .from("profiles")
      .select("package")
      .eq("id", ownerId)
      .maybeSingle();

    const pkg = (profile as any)?.package ?? "basic";
    const allowedDocs = PACKAGE_DOC_LIMITS[pkg as PackageTier] ?? 1;

    // Count user's generated documents this month
    const startOfMonth = new Date();
    startOfMonth.setDate(1);
    startOfMonth.setHours(0, 0, 0, 0);

    const { count } = await client
      .from("generated_documents")
      .select("*", { count: "exact", head: true })
      .eq("owner_id", ownerId)
      .gte("created_at", startOfMonth.toISOString());

    if ((count ?? 0) >= allowedDocs) {
      return NextResponse.json(
        { error: "limit_reached", message: "คุณใช้สิทธิ์ครบแล้วในเดือนนี้ อัปเกรดเพื่อสร้างเอกสารเพิ่ม" },
        { status: 402 }
      );
    }
  }

  // NEW: Use merge engine (template-driven) OR DeepSeek (AI-driven)
  let generatedContent: string;

  if (template.template_content_md) {
    // MERGE ENGINE path — deterministic, fast, no AI cost
    const mergeFields = template.merge_fields || [];
    const conditionalBlocks = template.conditional_blocks || {};

    generatedContent = mergeTemplate(
      {
        templateId: template.id,
        contentMd: template.template_content_md,
        mergeFields,
        conditionalBlocks,
      },
      mergeData as any,
    );

    // Optionally pass through DeepSeek for formatting polish
    const provider = getDeepSeekProvider();
    const polishResult = await provider.complete({
      messages: [
        { role: "system", content: SYSTEM_PROMPT_FILL },
        { role: "user", content: `แม่แบบ: ${generatedContent}\n\nกรุณาจัดรูปแบบย่อหน้าและตรวจสอบความถูกต้อง` },
      ],
      temperature: 0.2,
      maxTokens: 2000,
    });
    generatedContent = polishResult.content;

  } else {
    // FALLBACK: DeepSeek-only path (existing behavior)
    // ... existing code ...
  }

  // NEW: Bilingual generation
  if (body.generateEnglish) {
    const provider = getDeepSeekProvider();
    const enResult = await provider.complete({
      messages: [
        { role: "system", content: "Translate the following Thai legal document to English. Keep all names, amounts, dates unchanged." },
        { role: "user", content: generatedContent },
      ],
      temperature: 0.1,
      maxTokens: 2000,
    });
    generatedContent += "\n\n--- ENGLISH VERSION ---\n\n" + enResult.content;
  }

  // Persist + return (existing pattern)
  // ...
}
```

---

### A.4 Category Pages & UI Components

#### A.4.1 Document Browser Page (Redesigned)

**File: `D:\legalai-citizen-check\app\documents\page.tsx`** — Replace with:

```tsx
"use client";

import { useState } from "react";
import { PageHead, Pill } from "@/components/ui/primitives";
import { DOCUMENT_CATEGORIES, type DocumentCategoryMeta } from "@/lib/documents/categories";

export default function DocumentsPage() {
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);

  return (
    <>
      <PageHead
        title="สร้างเอกสารกฎหมาย"
        subtitle="เลือกประเภทเอกสารที่ต้องการ — เรามี 126 แบบฟอร์ม ครอบคลุม 10 หมวดหมู่"
      />

      {/* Category cards */}
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-8">
        {DOCUMENT_CATEGORIES.map((cat) => (
          <button
            key={cat.id}
            className={`category-card ${selectedCategory === cat.id ? "ring-2 ring-blue-500" : ""}`}
            onClick={() => setSelectedCategory(cat.id)}
          >
            <span className="text-3xl">{cat.icon}</span>
            <strong>{cat.title_th}</strong>
            <small>{cat.subtitle_th}</small>
          </button>
        ))}
      </div>

      {/* Template list for selected category */}
      {selectedCategory && (
        <TemplateList category={selectedCategory} />
      )}
    </>
  );
}

function TemplateList({ category }: { category: string }) {
  // Fetch templates from /api/documents/templates?category=X
  // Show grid of available documents with:
  //   - Thai name (bold)
  //   - English name (subtitle)
  //   - Price pill: "ฟรี" / "฿99" / "฿199"
  //   - Auto-gen feasibility badge
  //   - Government agency note
  return <div>{/* template grid */}</div>;
}
```

#### A.4.2 Template Detail Page

**New File: `D:\legalai-citizen-check\app\documents\[templateId]\page.tsx`**

```tsx
/**
 * Template detail page — shows merge fields form + preview
 *
 * Layout:
 *   Left: Merge field form (dynamic, built from merge_fields JSON)
 *   Right: Live preview (fills as user types)
 *   Bottom: Generate button + export options
 */
```

#### A.4.3 Document Editor Component

**New File: `D:\legalai-citizen-check\components\documents\document-editor.tsx`**

```tsx
"use client";

/**
 * DocumentEditor — the main document creation interface.
 *
 * Renders:
 *   1. Merge field form (auto-generated from template.merge_fields)
 *   2. Live preview panel (shows filled template in real-time)
 *   3. Conditional block toggles
 *   4. Export buttons (PDF, DOCX, TXT)
 *   5. AI polish button
 *   6. Price/credit display
 */

import { useState, useEffect } from "react";
import type { MergeFieldDefinition, MergeData } from "@/lib/documents/merge-engine";
import { mergeTemplate } from "@/lib/documents/merge-engine";

type Props = {
  templateId: string;
  templateContent: string;
  mergeFields: MergeFieldDefinition[];
  isPaid: boolean;
  priceThb: number;
};

export function DocumentEditor({ templateId, templateContent, mergeFields, isPaid, priceThb }: Props) {
  const [mergeData, setMergeData] = useState<MergeData>({});
  const [preview, setPreview] = useState("");

  // Update preview whenever mergeData changes
  useEffect(() => {
    const filled = mergeTemplate(
      { templateId, contentMd: templateContent, mergeFields, conditionalBlocks: [] },
      mergeData
    );
    setPreview(filled);
  }, [mergeData, templateContent, mergeFields, templateId]);

  return (
    <div className="editor-layout">
      {/* Left: Form */}
      <div className="merge-form">
        <h3>กรอกข้อมูล</h3>
        {mergeFields.map((field) => (
          <MergeFieldInput
            key={field.key}
            field={field}
            value={String(mergeData[field.key] ?? "")}
            onChange={(v) => setMergeData(prev => ({ ...prev, [field.key]: v }))}
          />
        ))}
      </div>

      {/* Right: Preview */}
      <div className="document-preview">
        <div className="paper">
          <pre>{preview}</pre>
        </div>
      </div>
    </div>
  );
}
```

#### A.4.4 Merge Field Input Component

**New File: `D:\legalai-citizen-check\components\documents\merge-field-input.tsx`**

```tsx
"use client";

import type { MergeFieldDefinition } from "@/lib/documents/merge-engine";

type Props = {
  field: MergeFieldDefinition;
  value: string;
  onChange: (value: string) => void;
};

export function MergeFieldInput({ field, value, onChange }: Props) {
  const requiredDot = field.required ? <span className="text-red-500">*</span> : null;

  switch (field.type) {
    case "select":
      return (
        <label>
          {field.label_th} {requiredDot}
          <select value={value} onChange={e => onChange(e.target.value)}>
            <option value="">— เลือก —</option>
            {field.options?.map(opt => (
              <option key={opt} value={opt}>{opt}</option>
            ))}
          </select>
          {field.hint_th && <small>{field.hint_th}</small>}
        </label>
      );

    case "date":
      return (
        <label>
          {field.label_th} {requiredDot}
          <input
            type="date"
            value={value}
            onChange={e => onChange(e.target.value)}
          />
          {field.hint_th && <small>{field.hint_th}</small>}
        </label>
      );

    case "boolean":
      return (
        <label className="toggle">
          {field.label_th} {requiredDot}
          <input
            type="checkbox"
            checked={value === "true"}
            onChange={e => onChange(e.target.checked ? "true" : "false")}
          />
        </label>
      );

    default:
      return (
        <label>
          {field.label_th} {requiredDot}
          <input
            type="text"
            placeholder={field.hint_th ?? field.label_th}
            value={value}
            onChange={e => onChange(e.target.value)}
          />
        </label>
      );
  }
}
```

---

### A.5 Document Templates API Endpoint (NEW)

**New File: `D:\legalai-citizen-check\app\api\documents\templates\route.ts`**

```typescript
/**
 * GET /api/documents/templates
 *
 * Lists document templates, filterable by:
 *   - ?category=business_formation    (document_category)
 *   - ?legal_category=labour          (legacy legal_category for problem docs)
 *   - ?tier=free                      (is_paid=false only)
 *   - ?search=สัญญาเช่า               (text search on title + name_thai)
 *   - ?feasibility=HIGH               (auto_gen_feasibility)
 */

import { NextResponse } from "next/server";
import { getServiceClient } from "@/lib/supabase/server";

export const runtime = "edge";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const category = url.searchParams.get("category");
  const legalCategory = url.searchParams.get("legal_category");
  const tier = url.searchParams.get("tier");
  const search = url.searchParams.get("search");
  const feasibility = url.searchParams.get("feasibility");

  const supabase = getServiceClient();
  let query = supabase
    .from("document_templates")
    .select("*")
    .eq("review_status", "approved")
    .order("sort_order", { ascending: true })
    .order("created_at", { ascending: false });

  if (category) query = query.eq("document_category", category);
  if (legalCategory) query = query.eq("category", legalCategory);
  if (tier === "free") query = query.eq("is_paid", false);
  if (feasibility) query = query.eq("auto_gen_feasibility", feasibility);
  if (search) query = query.or(`title.ilike.%${search}%,name_thai.ilike.%${search}%`);

  const { data, error } = await query.limit(50);
  if (error) {
    return NextResponse.json({ templates: [], error: error.message }, { status: 200 });
  }

  return NextResponse.json({ templates: data ?? [] });
}
```

---

### A.6 Seed Data: 126 Document Templates

**New File: `D:\legalai-citizen-check\supabase\migrations\0004_seed_document_templates.sql`**

```sql
-- Seed the 126 business document templates from the Business Documents Library
-- 10 categories, 126 entries, ~80% HIGH auto-gen feasibility

-- Category 2: Rental & Lease (17 docs — highest demand)
insert into public.document_templates
  (id, title, name_thai, name_english, description, version, category, document_category,
   auto_gen_feasibility, government_agency, is_paid, price_thb, sort_order, review_status, reviewed_at, reviewed_by)
values
  (gen_random_uuid(), 'สัญญาเช่าบ้าน', 'สัญญาเช่าบ้าน', 'House Rental Agreement',
   'สัญญาเช่าบ้านพักอาศัยมาตรฐาน ระยะเวลา 1-3 ปี', '1.0.0', 'housing', 'rental_lease',
   'HIGH', 'กรมที่ดิน (ถ้า ≥3 ปี)', false, 0, 1, 'approved', now(), null),
  (gen_random_uuid(), 'สัญญาเช่าคอนโด/ห้องชุด', 'สัญญาเช่าคอนโด/ห้องชุด', 'Condominium Unit Rental Agreement',
   'สัญญาเช่าห้องชุดพร้อมข้อกำหนดนิติบุคคล', '1.0.0', 'housing', 'rental_lease',
   'HIGH', null, true, 99, 2, 'approved', now(), null)
  -- ... (remaining 124 entries from the library)
;
```

---

## SECTION B: Free vs Paid Tier Framework

### B.1 Package Definitions

**New File: `D:\legalai-citizen-check\lib\packages\tiers.ts`**

```typescript
/**
 * Package Tier Definitions for LegalAI Thailand
 *
 * 4 tiers: Free (ฟรี), Action Pack, Case Plus, SME Starter
 * Each tier gates specific features via API middleware and UI components.
 */

export type PackageTier = "free" | "action_pack" | "case_plus" | "sme_starter";

export type PackageDefinition = {
  id: PackageTier;
  name_th: string;
  name_en: string;
  price_thb: number;           // one-time or monthly
  billing_period: "once" | "monthly";
  features: PackageFeatures;
};

export type PackageFeatures = {
  ai_diagnosis: boolean;           // AI diagnosis
  action_plan_preview: boolean;    // Preview action plan
  full_action_plan: boolean;       // Full action plan with steps
  free_document_count: number;     // Free document generations
  paid_document_access: boolean;   // Unlimited paid docs
  document_watermark: boolean;     // Watermark on PDFs
  export_formats: string[];        // Available export formats
  evidence_upload: boolean;        // Upload evidence files
  lawyer_search: boolean;          // Search lawyer marketplace
  case_workspace: boolean;         // Case workspace/timeline
  reminders: boolean;              // Deadline reminders
  priority_review: boolean;        // Priority lawyer review
  business_contracts: boolean;     // SME business contracts
  team_access: boolean;            // Multi-user team access
  api_access: boolean;             // API access
  max_cases: number;               // Max active cases
  max_storage_mb: number;          // Storage limit in MB
};

export const PACKAGES: Record<PackageTier, PackageDefinition> = {
  free: {
    id: "free",
    name_th: "ฟรี",
    name_en: "Free",
    price_thb: 0,
    billing_period: "once",
    features: {
      ai_diagnosis: true,            // ✅ Basic diagnosis (6 categories)
      action_plan_preview: true,     // ✅ Preview only (first 2 steps)
      full_action_plan: false,       // ❌
      free_document_count: 1,        // ✅ 1 free document download
      paid_document_access: false,   // ❌
      document_watermark: true,      // ✅ Watermark applied
      export_formats: ["pdf"],       // PDF only, watermarked
      evidence_upload: false,        // ❌
      lawyer_search: true,           // ✅ Basic search
      case_workspace: false,         // ❌
      reminders: false,              // ❌
      priority_review: false,        // ❌
      business_contracts: false,     // ❌
      team_access: false,            // ❌
      api_access: false,             // ❌
      max_cases: 1,                  // 1 case at a time
      max_storage_mb: 10,            // 10 MB
    },
  },

  action_pack: {
    id: "action_pack",
    name_th: "Action Pack",
    name_en: "Action Pack",
    price_thb: 299,
    billing_period: "once",
    features: {
      ai_diagnosis: true,
      action_plan_preview: true,
      full_action_plan: true,        // ✅ Full action plan
      free_document_count: -1,       // ✅ Unlimited (within pack)
      paid_document_access: true,
      document_watermark: false,     // ✅ Clean PDF
      export_formats: ["pdf", "docx", "txt"],
      evidence_upload: true,         // ✅ Upload evidence
      lawyer_search: true,
      case_workspace: false,
      reminders: false,
      priority_review: false,
      business_contracts: false,
      team_access: false,
      api_access: false,
      max_cases: 3,
      max_storage_mb: 100,
    },
  },

  case_plus: {
    id: "case_plus",
    name_th: "Case Plus",
    name_en: "Case Plus",
    price_thb: 999,
    billing_period: "once",
    features: {
      ai_diagnosis: true,
      action_plan_preview: true,
      full_action_plan: true,
      free_document_count: -1,
      paid_document_access: true,
      document_watermark: false,
      export_formats: ["pdf", "docx", "txt"],
      evidence_upload: true,
      lawyer_search: true,
      case_workspace: true,          // ✅ Full case workspace
      reminders: true,               // ✅ Deadline reminders
      priority_review: true,         // ✅ Priority lawyer review
      business_contracts: false,
      team_access: false,
      api_access: false,
      max_cases: 10,
      max_storage_mb: 500,
    },
  },

  sme_starter: {
    id: "sme_starter",
    name_th: "SME Starter",
    name_en: "SME Starter",
    price_thb: 2990,
    billing_period: "monthly",
    features: {
      ai_diagnosis: true,
      action_plan_preview: true,
      full_action_plan: true,
      free_document_count: -1,
      paid_document_access: true,
      document_watermark: false,
      export_formats: ["pdf", "docx", "txt"],
      evidence_upload: true,
      lawyer_search: true,
      case_workspace: true,
      reminders: true,
      priority_review: true,
      business_contracts: true,      // ✅ All SME contracts
      team_access: true,             // ✅ 5 team members
      api_access: true,              // ✅ REST API
      max_cases: 50,
      max_storage_mb: 5000,
    },
  },
};

/** Map the `profiles.package` column value to a tier. */
export function getPackageTier(packageValue: string): PackageTier {
  const valid: PackageTier[] = ["free", "action_pack", "case_plus", "sme_starter"];
  return valid.includes(packageValue as PackageTier)
    ? (packageValue as PackageTier)
    : "free";
}

/** Check if a tier has a specific feature. */
export function tierHasFeature(tier: PackageTier, feature: keyof PackageFeatures): boolean {
  return PACKAGES[tier].features[feature] === true;
}

/** Document generation limits per tier per month. -1 = unlimited. */
export const PACKAGE_DOC_LIMITS: Record<PackageTier, number> = {
  free: 1,
  action_pack: -1,
  case_plus: -1,
  sme_starter: -1,
};
```

---

### B.2 API Auth Gates (Middleware)

**New File: `D:\legalai-citizen-check\lib\packages\gate.ts`**

```typescript
/**
 * Package Tier Gate — middleware helper for API routes.
 *
 * Usage in any route handler:
 *   const gate = await requireFeature("evidence_upload", request);
 *   if (gate.blocked) return gate.response;  // 402 Payment Required
 */

import { NextResponse } from "next/server";
import { getServiceClient } from "@/lib/supabase/server";
import { getPackageTier, tierHasFeature, type PackageFeatures, type PackageTier } from "./tiers";

type GateResult = {
  allowed: true;
  tier: PackageTier;
  profile: any;
} | {
  allowed: false;
  response: NextResponse;
};

export async function requireFeature(
  feature: keyof PackageFeatures,
  ownerId: string,
): Promise<GateResult> {
  const client = getServiceClient();

  const { data: profile } = await client
    .from("profiles")
    .select("package")
    .eq("id", ownerId)
    .maybeSingle();

  if (!profile) {
    return {
      allowed: false,
      response: NextResponse.json({ error: "profile_not_found" }, { status: 401 }),
    };
  }

  const row = profile as { package: string };
  const tier = getPackageTier(row.package);

  if (!tierHasFeature(tier, feature)) {
    return {
      allowed: false,
      response: NextResponse.json(
        {
          error: "upgrade_required",
          feature,
          current_tier: tier,
          message: "แพ็กเกจปัจจุบันของคุณไม่รวมฟีเจอร์นี้ อัปเกรดเพื่อใช้งาน",
        },
        { status: 402 },
      ),
    };
  }

  return { allowed: true, tier, profile };
}

/**
 * Gate for document generation — checks count limits.
 */
export async function requireDocumentGeneration(
  ownerId: string,
): Promise<GateResult> {
  const client = getServiceClient();

  const { data: profile } = await client
    .from("profiles")
    .select("package")
    .eq("id", ownerId)
    .maybeSingle();

  if (!profile) {
    return {
      allowed: false,
      response: NextResponse.json({ error: "profile_not_found" }, { status: 401 }),
    };
  }

  const row = profile as { package: string };
  const tier = getPackageTier(row.package);

  const limit = PACKAGE_DOC_LIMITS[tier];
  if (limit === -1) return { allowed: true, tier, profile }; // Unlimited

  // Count documents generated this month
  const startOfMonth = new Date();
  startOfMonth.setDate(1);
  startOfMonth.setHours(0, 0, 0, 0);

  const { count } = await client
    .from("generated_documents")
    .select("*", { count: "exact", head: true })
    .eq("owner_id", ownerId)
    .gte("created_at", startOfMonth.toISOString());

  if ((count ?? 0) >= limit) {
    return {
      allowed: false,
      response: NextResponse.json(
        {
          error: "limit_reached",
          feature: "document_generation",
          current_count: count,
          limit,
          message: "คุณใช้สิทธิ์สร้างเอกสารครบแล้วในเดือนนี้",
        },
        { status: 402 },
      ),
    };
  }

  return { allowed: true, tier, profile };
}
```

#### B.2.1 Apply Gates to Existing Routes

**File: `D:\legalai-citizen-check\app\api\documents\generate\route.ts`** — Add at top of POST:

```typescript
// Before the main handler:
const gate = await requireDocumentGeneration(ownerId);
if (!gate.allowed) return gate.response;
```

**File: `D:\legalai-citizen-check\app\api\evidence\upload-url\route.ts`** — Add gate:

```typescript
const gate = await requireFeature("evidence_upload", ownerId);
if (!gate.allowed) return gate.response;
```

**File: `D:\legalai-citizen-check\app\api\ai\diagnosis\route.ts`** — Add tier discrimination:

```typescript
// Free tier: basic diagnosis (6 categories, 4 questions each)
// Action Pack+: full diagnosis (12 categories, fear calibration, urgency windows)

const gate = await requireFeature("full_action_plan", ownerId);
const isFree = !gate.allowed; // blocked means free tier

if (isFree && !BASIC_CATEGORIES.includes(body.category)) {
  return NextResponse.json(
    { error: "upgrade_required", message: "หมวดนี้ต้องใช้ Action Pack ขึ้นไป" },
    { status: 402 }
  );
}
```

---

### B.3 UI Components for Tiers

#### B.3.1 Upgrade Banner Component

**New File: `D:\legalai-citizen-check\components\packages\upgrade-banner.tsx`**

```tsx
"use client";

import type { PackageTier } from "@/lib/packages/tiers";
import { PACKAGES } from "@/lib/packages/tiers";

/**
 * UpgradeBanner — shown when a feature is locked.
 * Example: "สร้างเอกสารไม่จำกัด? → อัปเกรดเป็น Action Pack ฿299"
 */
export function UpgradeBanner({
  lockedFeature,
  currentTier,
  requiredTier,
}: {
  lockedFeature: string;
  currentTier: PackageTier;
  requiredTier: PackageTier;
}) {
  const pkg = PACKAGES[requiredTier];

  return (
    <div className="upgrade-banner">
      <div className="icon">🔒</div>
      <div>
        <strong>{lockedFeature}</strong>
        <p>แพ็กเกจ {PACKAGES[currentTier].name_th} ของคุณไม่รวมฟีเจอร์นี้</p>
      </div>
      <a href="/packages" className="cta">
        อัปเกรดเป็น {pkg.name_th} — ฿{pkg.price_thb.toLocaleString()}
      </a>
    </div>
  );
}
```

#### B.3.2 Tier Badge Component

**New File: `D:\legalai-citizen-check\components\packages\tier-badge.tsx`**

```tsx
"use client";

import type { PackageTier } from "@/lib/packages/tiers";

const TIER_COLORS: Record<PackageTier, string> = {
  free: "gray",
  action_pack: "blue",
  case_plus: "purple",
  sme_starter: "gold",
};

export function TierBadge({ tier }: { tier: PackageTier }) {
  return (
    <span className={`badge ${TIER_COLORS[tier]}`}>
      {tier === "free" ? "ฟรี" : tier === "action_pack" ? "Action Pack" :
       tier === "case_plus" ? "Case Plus" : "SME Starter"}
    </span>
  );
}
```

---

### B.4 Pricing Page

**New File: `D:\legalai-citizen-check\app\packages\page.tsx`**

```tsx
/**
 * Pricing page — shows all 4 tiers with feature comparison table.
 * Links to payment flow (LINE Pay / PromptPay / Credit Card).
 */
```

---

## SECTION C: User FAQ Gaps & Legal Boundaries

### C.1 Information vs Legal Advice — The Hard Line

**LegalAI Thailand MUST NOT:**

| ❌ Must NEVER | Why | What to do instead |
|---|---|---|
| Give legal advice ("คุณควรฟ้อง", "คุณจะชนะคดี") | Constitutes unauthorized legal practice under Lawyers Act B.E. 2528 | Say: "คุณมีสิทธิที่จะ...ตามกฎหมาย...", "ทางเลือกที่มีคือ..." |
| Predict case outcomes ("มีโอกาสชนะ 80%") | Misleading; creates liability | Use "Evidence Readiness" ratio: "คุณมีหลักฐาน 3 จาก 5 รายการ" |
| Recommend specific lawyers as "best" | Unfair competition; bias | Show verified lawyers sorted by rating; label "เรียงตามคะแนนรีวิว" |
| Guarantee results ("รับรองว่าชนะแน่นอน") | Deceptive advertising; illegal | Never guarantee. Always: "ผลลัพธ์ขึ้นอยู่กับข้อเท็จจริงและดุลพินิจของศาล" |
| Draft court filings (คำฟ้อง, คำให้การ) | Requires licensed lawyer in Thailand | Limit to: letters, contracts, notices — never pleadings |
| File documents with government on behalf of users | Unauthorized practice | Provide instructions + links to government portals |
| Collect or store sensitive PII (เลขบัตรประชาชน) without PDPA consent | Violates PDPA B.E. 2562 | Mask ID numbers: "1-2345-xxxxx-xx-x"; collect only with explicit consent |

### C.2 Guardrails Implementation

**New File: `D:\legalai-citizen-check\lib\legal\guardrails.ts`**

```typescript
/**
 * Legal Guardrails — system prompt injections and output filters
 * that prevent the AI from crossing the advice/information boundary.
 */

export const LEGAL_BOUNDARY_PROMPT = `
ข้อห้ามเด็ดขาด (คุณต้องปฏิบัติตามโดยไม่มีข้อยกเว้น):
1. ห้ามให้คำแนะนำทางกฎหมาย (legal advice) — ให้ข้อมูลสิทธิและทางเลือกเท่านั้น
2. ห้ามทำนายผลคดี — ใช้ "ความพร้อมของหลักฐาน" แทน
3. ห้ามรับรองผล — ทุกคำตอบต้องมีข้อความ "เป็นข้อมูลเบื้องต้นเท่านั้น"
4. ห้ามร่างคำฟ้องหรือคำให้การ — ทำได้เฉพาะจดหมาย หนังสือแจ้ง สัญญา
5. ห้ามแนะนำทนายคนใดว่า "ดีที่สุด" — ระบุเพียงข้อมูลที่ตรวจสอบได้
6. ทุกคำตอบทางกฎหมายต้องมีการอ้างอิงแหล่งที่มา
7. ท้ายทุกคำตอบต้องมี: "⚠️ ข้อมูลนี้เป็นข้อมูลเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย ควรปรึกษาทนายความก่อนดำเนินการ"
`;

/**
 * Filter AI output for banned phrases. Returns { clean, flagged }.
 */
export const BANNED_PHRASES = [
  "คุณควรฟ้อง",
  "คุณจะชนะ",
  "โอกาสชนะ",
  "รับรองว่า",
  "แนะนำทนายคนนี้",
  "ทนายที่ดีที่สุด",
  "ฟ้องแน่นอน",
  "ชนะแน่",
  "ได้เงินแน่",
];

export function filterAiOutput(text: string): { clean: string; flagged: string[] } {
  const flagged: string[] = [];
  let clean = text;

  for (const phrase of BANNED_PHRASES) {
    if (clean.includes(phrase)) {
      flagged.push(phrase);
      clean = clean.replace(new RegExp(phrase, "g"), "⚠️ [ข้อความนี้ถูกลบเพื่อความปลอดภัย]");
    }
  }

  // Ensure disclaimer exists
  if (!clean.includes("ไม่ใช่คำปรึกษาทางกฎหมาย")) {
    clean += "\n\n⚠️ ข้อมูลนี้เป็นข้อมูลเบื้องต้น ไม่ใช่คำปรึกษาทางกฎหมาย ควรปรึกษาทนายความก่อนดำเนินการ";
  }

  return { clean, flagged };
}

/**
 * Redact sensitive PII from user input before sending to AI.
 */
export function redactPii(text: string): string {
  // Thai national ID: 13 digits
  text = text.replace(/\b\d{13}\b/g, "[เลขบัตรประชาชนถูกลบ]");

  // Phone numbers
  text = text.replace(/\b0\d{8,9}\b/g, "[เบอร์โทรถูกลบ]");

  // Email addresses
  text = text.replace(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g, "[อีเมลถูกลบ]");

  return text;
}
```

### C.3 FAQ Content — What Users Ask

**New File: `D:\legalai-citizen-check\lib\legal\faq.ts`**

```typescript
/**
 * Common FAQ items — mapped to LegalAI responses.
 * Used by the assistant and the FAQ page.
 */

export type FaqItem = {
  id: string;
  question_th: string;
  answer_th: string;
  category?: string;
  relatedDocuments?: string[]; // template IDs
};

export const FAQ_DATABASE: FaqItem[] = [
  {
    id: "faq-001",
    question_th: "LegalAI เป็นทนายความไหม?",
    answer_th: "ไม่ใช่ค่ะ LegalAI เป็นระบบช่วยเหลือข้อมูลกฎหมายเบื้องต้น เราให้ข้อมูลสิทธิและขั้นตอน แต่ไม่ใช่การให้คำปรึกษาทางกฎหมายจากทนายความ หากต้องการคำปรึกษาเฉพาะกรณี คุณสามารถค้นหาทนายความผ่านแพลตฟอร์มของเราได้",
  },
  {
    id: "faq-002",
    question_th: "ฉันถูกเลิกจ้าง — จะได้เงินชดเชยเท่าไหร่?",
    answer_th: "จำนวนเงินชดเชยขึ้นอยู่กับอายุงานตาม พ.ร.บ. คุ้มครองแรงงาน พ.ศ. 2541:\n- อายุงาน 120 วัน – 1 ปี: ได้ค่าชดเชย 30 วัน\n- อายุงาน 1 – 3 ปี: ได้ค่าชดเชย 90 วัน\n- อายุงาน 3 – 6 ปี: ได้ค่าชดเชย 180 วัน\n- อายุงาน 6 – 10 ปี: ได้ค่าชดเชย 240 วัน\n- อายุงานเกิน 10 ปี: ได้ค่าชดเชย 300 วัน\n\n⚠️ เป็นข้อมูลเบื้องต้นเท่านั้น — ผลลัพธ์ขึ้นอยู่กับข้อเท็จจริงเฉพาะกรณี",
    category: "labour",
  },
  {
    id: "faq-003",
    question_th: "เอกสารที่ LegalAI สร้างใช้ได้จริงตามกฎหมายไหม?",
    answer_th: "เอกสารที่เราสร้างเป็นแบบร่างที่ใช้แม่แบบมาตรฐานและภาษากฎหมายที่ถูกต้อง อย่างไรก็ตาม:\n- สัญญาบางประเภทต้องจดทะเบียนกับหน่วยงานรัฐ (เช่น จำนองที่ดิน)\n- เอกสารสำคัญควรให้ทนายความตรวจสอบก่อนนำไปใช้จริง\n- LegalAI ไม่รับผิดชอบความเสียหายจากการใช้เอกสาร",
  },
  {
    id: "faq-004",
    question_th: "LegalAI เก็บข้อมูลส่วนตัวของฉันไหม?",
    answer_th: "เราเก็บข้อมูลเท่าที่จำเป็นเพื่อให้บริการ ตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA):\n- ชื่อ, อีเมล: สำหรับบัญชีผู้ใช้\n- ข้อมูลเคส: เฉพาะที่คุณกรอก\n- เราไม่ขายหรือส่งต่อข้อมูลให้บุคคลที่สาม\n- คุณสามารถขอลบข้อมูลได้ตลอดเวลา",
  },
  {
    id: "faq-005",
    question_th: "ทำไมบางเอกสารถึงต้องเสียเงิน?",
    answer_th: "LegalAI มีทั้งเอกสารฟรีและเสียเงิน:\n- ฟรี: เอกสารพื้นฐาน เช่น หนังสือทวงถาม หนังสือบอกเลิกสัญญา\n- เสียเงิน: เอกสารเฉพาะทาง เช่น สัญญาจัดตั้งบริษัท สัญญา Joint Venture\n- รายได้ส่วนหนึ่งนำไปพัฒนาแม่แบบและตรวจสอบโดยทีมกฎหมาย",
  },
];
```

---

## SECTION D: Development Integration

### D.1 Problem Diagnosis → Document Generation Bridge

**How it works:**

```
User completes diagnosis
        ↓
Diagnosis result includes recommendedDocuments[]
        ↓
User sees: "สิ่งที่คุณอาจต้องทำ: [สร้างหนังสือทวงถามค่าชดเชย →]"
        ↓
Click → navigates to /documents?category=labour&recommended=severance-letter
        ↓
Merge fields pre-filled from case data
        ↓
Document generated in 1 click
```

#### D.1.1 Add `recommendedDocuments` to Diagnosis Result

**File: `D:\legalai-citizen-check\lib\ai\diagnosis.ts`** — Add to `AnalysisResult`:

```typescript
export type AnalysisResult = {
  // ... existing fields ...
  /** Recommended document templates based on diagnosis */
  recommendedDocuments: Array<{
    templateId: string;
    reason: string;           // e.g. "ใช้แจ้งนายจ้างให้ชำระค่าชดเชย"
    priority: "must" | "recommended" | "optional";
  }>;
};
```

#### D.1.2 Cross-Referencing Map (Diagnosis → Documents)

**New File: `D:\legalai-citizen-check\lib\documents\diagnosis-bridge.ts`**

```typescript
/**
 * Diagnosis → Document Bridge
 *
 * Maps diagnosis answers to recommended document templates.
 * When a user completes a diagnosis, the system automatically suggests
 * relevant business/transactional documents.
 */

export type DiagnosisToDocument = {
  category: string;         // legal_category from diagnosis
  answerPattern: string;    // substring match on answer (e.g. "ถูกเลิกจ้าง")
  documentTemplateId: string;
  reason_th: string;
  priority: "must" | "recommended" | "optional";
};

export const DIAGNOSIS_DOCUMENT_MAP: DiagnosisToDocument[] = [
  // Labour → Employment docs
  {
    category: "labour",
    answerPattern: "ถูกเลิกจ้าง",
    documentTemplateId: "tpl-severance-letter",  // placeholder
    reason_th: "ใช้แจ้งนายจ้างให้ชำระค่าชดเชยตามกฎหมาย",
    priority: "must",
  },
  {
    category: "labour",
    answerPattern: "ถูกเลิกจ้าง",
    documentTemplateId: "tpl-employment-certificate",
    reason_th: "หนังสือรับรองการทำงานสำหรับสมัครงานใหม่",
    priority: "recommended",
  },
  {
    category: "labour",
    answerPattern: "นายจ้างค้างจ่ายเงิน",
    documentTemplateId: "tpl-payment-demand-letter",
    reason_th: "ใช้ทวงถามค่าจ้างค้างจ่ายอย่างเป็นทางการ",
    priority: "must",
  },

  // Consumer → Commercial docs
  {
    category: "consumer",
    answerPattern: "สินค้า",
    documentTemplateId: "tpl-consumer-complaint",
    reason_th: "หนังสือร้องเรียนผู้บริโภคถึง สคบ.",
    priority: "must",
  },

  // Debt → Finance docs
  {
    category: "debt",
    answerPattern: "ถูกทวงหนี้",
    documentTemplateId: "tpl-debt-settlement",
    reason_th: "หนังสือขอประนอมหนี้กับเจ้าหนี้",
    priority: "must",
  },
  {
    category: "debt",
    answerPattern: "ต้องการทวงหนี้",
    documentTemplateId: "tpl-debt-demand-letter",
    reason_th: "หนังสือทวงถามให้ชำระหนี้อย่างเป็นทางการ",
    priority: "must",
  },

  // Housing → Rental docs
  {
    category: "housing",
    answerPattern: "บอกเลิกสัญญาเช่า",
    documentTemplateId: "tpl-lease-termination",
    reason_th: "หนังสือบอกเลิกสัญญาเช่าอย่างเป็นทางการ",
    priority: "must",
  },
  {
    category: "housing",
    answerPattern: "เจ้าของที่ไม่คืนเงินมัดจำ",
    documentTemplateId: "tpl-deposit-demand",
    reason_th: "หนังสือทวงถามเงินมัดจำจากผู้ให้เช่า",
    priority: "must",
  },

  // Family → Personal docs
  {
    category: "family",
    answerPattern: "หย่าร้าง",
    documentTemplateId: "tpl-divorce-agreement",
    reason_th: "บันทึกข้อตกลงการหย่า (ใช้ยื่นที่อำเภอ)",
    priority: "recommended",
  },
  {
    category: "family",
    answerPattern: "มรดก",
    documentTemplateId: "tpl-will",
    reason_th: "พินัยกรรม — จัดการทรัพย์สินก่อนเสียชีวิต",
    priority: "optional",
  },

  // Accident → Vehicle + Insurance docs
  {
    category: "accident",
    answerPattern: "อุบัติเหตุ",
    documentTemplateId: "tpl-insurance-claim",
    reason_th: "แบบฟอร์มแจ้งเคลมประกันภัย",
    priority: "must",
  },
];

/**
 * Find recommended documents based on diagnosis answers.
 */
export function findRecommendedDocuments(category: string, answers: Record<string, string | string[]>): DiagnosisToDocument[] {
  const allAnswers = Object.values(answers).flatMap(v => Array.isArray(v) ? v : [v]).join(" ");

  return DIAGNOSIS_DOCUMENT_MAP.filter(entry => {
    if (entry.category !== category) return false;
    return allAnswers.includes(entry.answerPattern);
  });
}
```

#### D.1.3 Cross-Referencing: Preventive Document Suggestions

```typescript
/**
 * PREVENTIVE DOCUMENTS: when user solves a problem, suggest documents
 * that prevent recurrence. Example: solved lease dispute → "create a proper
 * lease agreement next time."
 */
export const PREVENTIVE_DOCUMENTS: Record<string, string[]> = {
  housing: ["tpl-house-lease-agreement", "tpl-rental-inspection-report"],
  labour: ["tpl-employment-contract", "tpl-remote-work-contract"],
  consumer: ["tpl-sales-contract", "tpl-return-policy"],
  debt: ["tpl-loan-agreement", "tpl-promissory-note"],
  family: ["tpl-prenup-agreement", "tpl-will"],
  accident: ["tpl-vehicle-insurance-auth"],
};
```

---

### D.2 LINE Bot Integration Points

**New File: `D:\legalai-citizen-check\lib\line\webhook.ts`**

```typescript
/**
 * LINE Bot Integration Points
 *
 * The LINE bot (future) will connect to these same API endpoints.
 * Design the API to be channel-agnostic:
 *   - Web app uses fetch() from browser
 *   - LINE bot uses fetch() from webhook handler
 *   - Same auth, same gates, same responses
 */

// LINE Messaging API webhook handler pattern:
// POST /api/line/webhook → validate signature → dispatch to handlers

export type LineMessageContext = {
  userId: string;          // LINE user ID → maps to profiles.id
  messageText: string;
  replyToken: string;
};

/**
 * LINE → LegalAI message routing:
 *
 * "ถูกเลิกจ้าง"      → POST /api/ai/diagnosis  (start diagnosis flow)
 * "สร้างสัญญาเช่า"   → GET /api/documents/templates?search=สัญญาเช่า
 * "หาทนาย"          → GET /api/lawyers
 * "สถานะเคส"        → GET /api/cases (list user cases)
 * "อัปเกรด"         → /packages page URL
 */

export const LINE_COMMAND_MAP: Record<string, { endpoint: string; method: string }> = {
  "วินิจฉัย": { endpoint: "/api/ai/diagnosis", method: "POST" },
  "เอกสาร":   { endpoint: "/api/documents/templates", method: "GET" },
  "ทนาย":     { endpoint: "/api/lawyers", method: "GET" },
  "เคส":      { endpoint: "/api/cases", method: "GET" },
  "แพ็กเกจ":  { endpoint: "/packages", method: "GET" },
};
```

---

### D.3 Analytics Events — Extended

**File: `D:\legalai-citizen-check\domain\types.ts`** — Add to `AnalyticsEvent` type (line 208-219):

```typescript
export type AnalyticsEvent =
  // ... existing events ...
  | { type: "document_generated"; templateId: string; category: string; tier: PackageTier }
  | { type: "document_exported"; templateId: string; format: string; tier: PackageTier }
  | { type: "upgrade_viewed"; fromTier: PackageTier; toTier: PackageTier }
  | { type: "upgrade_completed"; fromTier: PackageTier; toTier: PackageTier; amountThb: number }
  | { type: "diagnosis_to_document_bridge"; diagnosisCategory: string; templateId: string }
  | { type: "gate_blocked"; feature: string; currentTier: PackageTier }
  | { type: "preventive_document_suggested"; templateId: string; sourceCategory: string }
  | { type: "line_message_received"; command: string }
  | { type: "faq_viewed"; faqId: string }
  | { type: "template_viewed"; templateId: string; category: string };
```

---

## SECTION E: Quality & Safety

### E.1 Anti-Hallucination: Citation Validation

The existing system already has this in `lib/legal/sources.ts` with `resolveSource()` and `sourcesForCategory()`. Extend for business documents:

**File: `D:\legalai-citizen-check\lib\legal\sources.ts`** — Add government agency source registry:

```typescript
/**
 * Government Agency Source Registry
 *
 * Every document template that cites a government agency must reference
 * a source in this registry. The AI is constrained to only cite these.
 */
export const GOVERNMENT_AGENCY_SOURCES: Record<string, LegalSource> = {
  "land-department": {
    id: "land-department",
    title: "กรมที่ดิน กระทรวงมหาดไทย",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2484-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.dol.go.th",
    kind: "guide",
  },
  "dbd": {
    id: "dbd",
    title: "กรมพัฒนาธุรกิจการค้า กระทรวงพาณิชย์",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2485-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.dbd.go.th",
    kind: "guide",
  },
  "dlt": {
    id: "dlt",
    title: "กรมการขนส่งทางบก",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2482-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.dlt.go.th",
    kind: "guide",
  },
  "revenue-department": {
    id: "revenue-department",
    title: "กรมสรรพากร",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2475-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.rd.go.th",
    kind: "guide",
  },
  "dip": {
    id: "dip",
    title: "กรมทรัพย์สินทางปัญญา",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2535-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.ipthailand.go.th",
    kind: "guide",
  },
  "ocpb": {
    id: "ocpb",
    title: "สำนักงานคณะกรรมการคุ้มครองผู้บริโภค (สคบ.)",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2522-05-05",
    checkedDate: "2569-08-01",
    url: "https://www.ocpb.go.th",
    kind: "guide",
  },
  "pdpc": {
    id: "pdpc",
    title: "สำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล (สคส.)",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2562-05-28",
    checkedDate: "2569-08-01",
    url: "https://www.pdpc.or.th",
    kind: "guide",
  },
  "mol": {
    id: "mol",
    title: "กระทรวงแรงงาน",
    jurisdiction: "ประเทศไทย",
    effectiveDate: "2536-01-01",
    checkedDate: "2569-08-01",
    url: "https://www.mol.go.th",
    kind: "guide",
  },
};
```

### E.2 Human Review Workflow

**New File: `D:\legalai-citizen-check\lib\documents\review-workflow.ts`**

```typescript
/**
 * Human Review Workflow for Document Templates
 *
 * Every template goes through:
 *   draft → in_review → approved  (or rejected → draft)
 *
 * Reviewers check:
 *   1. Legal accuracy — content matches current law
 *   2. Thai language — grammar, formality level
 *   3. Merge fields — all {{placeholders}} have definitions
 *   4. Conditional logic — blocks don't produce contradictory text
 *   5. Government compliance — form matches official requirements
 */

export type ReviewStatus = "draft" | "in_review" | "approved" | "rejected";

export type ReviewChecklist = {
  legalAccuracy: boolean;
  thaiLanguage: boolean;
  mergeFieldsComplete: boolean;
  conditionalLogic: boolean;
  governmentCompliance: boolean;
  reviewerNotes: string;
};

export function validateTemplateForReview(template: {
  content_md: string;
  merge_fields: any[];
}): { valid: boolean; issues: string[] } {
  const issues: string[] = [];

  // Check 1: All placeholders have definitions
  const placeholders = extractPlaceholders(template.content_md);
  const definedKeys = new Set(template.merge_fields.map((f: any) => f.key));

  for (const ph of placeholders) {
    if (!definedKeys.has(ph)) {
      issues.push(`Missing merge field definition: {{${ph}}}`);
    }
  }

  // Check 2: All conditional blocks have matching open/close
  const openBlocks = (template.content_md.match(/\{\{#(\w+)\}\}/g) ?? [])
    .map(m => m.slice(3, -2));
  const closeBlocks = (template.content_md.match(/\{\{\/(\w+)\}\}/g) ?? [])
    .map(m => m.slice(3, -2));

  for (const block of openBlocks) {
    if (!closeBlocks.includes(block)) {
      issues.push(`Unclosed conditional block: {{#${block}}}`);
    }
  }

  // Check 3: No empty templates
  if (!template.content_md || template.content_md.trim().length < 50) {
    issues.push("Template content too short (< 50 chars)");
  }

  return { valid: issues.length === 0, issues };
}
```

### E.3 Version Tracking

**File: `D:\legalai-citizen-check\lib\documents\versioning.ts`**

```typescript
/**
 * Document Template Versioning
 *
 * Every template has a semver version. Changes are tracked in audit_events.
 *
 * Version policy:
 *   - MAJOR: content changed in legally significant way (e.g. law changed)
 *   - MINOR: new merge fields or conditional blocks added
 *   - PATCH: typo fixes, formatting, non-semantic changes
 *
 * Previous versions are KEPT (not overwritten) — generated_documents
 * records which template version was used for audit trail.
 */

export function bumpVersion(current: string, change: "major" | "minor" | "patch"): string {
  const [major, minor, patch] = current.split(".").map(Number);
  switch (change) {
    case "major": return `${major + 1}.0.0`;
    case "minor": return `${major}.${minor + 1}.0`;
    case "patch": return `${major}.${minor}.${patch + 1}`;
  }
}

/**
 * Audit record for template changes.
 * Inserted into audit_events table:
 *   { action: "template_updated", target_type: "document_template", target_id: "...",
 *     metadata: { old_version, new_version, change_type, changed_by } }
 */
```

### E.4 Thai Legal Accuracy Checks

**New File: `D:\legalai-citizen-check\lib\legal\thai-accuracy.ts`**

```typescript
/**
 * Thai Legal Accuracy Checks
 *
 * Automated checks that run on document content before publication.
 * These are NOT a substitute for human review — they catch obvious errors.
 */

export type AccuracyCheck = {
  id: string;
  description: string;
  check: (content: string) => { passed: boolean; message: string };
};

export const ACCURACY_CHECKS: AccuracyCheck[] = [
  {
    id: "thai-year-format",
    description: "Ensure Buddhist Era years are used (พ.ศ. not ค.ศ.)",
    check: (content) => {
      // Check for Western year format in a Thai document
      const westernYearPattern = /\b(19|20)\d{2}\b/g;
      const matches = content.match(westernYearPattern);
      if (matches) {
        return {
          passed: false,
          message: `พบปี ค.ศ. ${matches.join(", ")} — ควรใช้ พ.ศ.`,
        };
      }
      return { passed: true, message: "OK" };
    },
  },
  {
    id: "thai-formal-pronouns",
    description: "Check for informal pronouns in legal documents",
    check: (content) => {
      const informal = ["กู", "มึง", "แก", "เอ็ง"];
      const found = informal.filter(w => content.includes(w));
      if (found.length > 0) {
        return {
          passed: false,
          message: `พบคำไม่เป็นทางการ: ${found.join(", ")}`,
        };
      }
      return { passed: true, message: "OK" };
    },
  },
  {
    id: "required-thai-legal-terms",
    description: "Check for essential legal terminology",
    check: (content) => {
      const required = ["คู่สัญญา", "ลงชื่อ", "พยาน"];
      const missing = required.filter(w => !content.includes(w));
      if (missing.length > 0) {
        return {
          passed: false,
          message: `ขาดคำศัพท์กฎหมายที่จำเป็น: ${missing.join(", ")}`,
        };
      }
      return { passed: true, message: "OK" };
    },
  },
  {
    id: "unfilled-placeholders",
    description: "No unfilled {{placeholders}} in final output",
    check: (content) => {
      const unfilled = content.match(/\{\{\w+\}\}/g);
      if (unfilled) {
        return {
          passed: false,
          message: `พบ placeholder ที่ไม่ได้กรอก: ${unfilled.join(", ")}`,
        };
      }
      return { passed: true, message: "OK" };
    },
  },
  {
    id: "disclaimer-present",
    description: "Every document must have disclaimer text",
    check: (content) => {
      const hasDisclaimer =
        content.includes("ไม่ใช่คำปรึกษาทางกฎหมาย") ||
        content.includes("ข้อมูลเบื้องต้น");
      return {
        passed: hasDisclaimer,
        message: hasDisclaimer ? "OK" : "ไม่มีข้อความ disclaimer",
      };
    },
  },
];

/** Run all accuracy checks on a generated document. */
export function runAccuracyChecks(content: string): { allPassed: boolean; results: { id: string; passed: boolean; message: string }[] } {
  const results = ACCURACY_CHECKS.map(check => ({
    id: check.id,
    ...check.check(content),
  }));
  return {
    allPassed: results.every(r => r.passed),
    results,
  };
}
```

---

## Priority Roadmap & Effort Estimates

### Phase 1: Foundation (Week 1-2) — ~30 hours

| Priority | Task | Files | Est. Hours |
|:---:|------|-------|:---:|
| 🔴 P0 | Expand `legal_category` enum (6→12) | schema.ts, migration SQL, sources.ts, diagnosis-config.ts, categories.ts | 4 |
| 🔴 P0 | Add fear calibration + urgency windows | fear-calibration.ts (new), urgency-windows.ts (new) | 2 |
| 🔴 P0 | Create `document_category` enum + migration | schema.ts, 0003_document_categories.sql | 2 |
| 🔴 P0 | Merge field engine | merge-engine.ts (new) | 6 |
| 🔴 P0 | Document category registry + UI | categories.ts (new), documents/page.tsx (rewrite) | 4 |
| 🔴 P0 | Seed 126 document templates | 0004_seed_document_templates.sql, seed data | 4 |
| 🔴 P0 | Legal guardrails + PII redaction | guardrails.ts (new) | 3 |
| 🔴 P0 | Free tier gates + package model | tiers.ts (new), gate.ts (new) | 5 |

### Phase 2: Integration (Week 3) — ~20 hours

| Priority | Task | Files | Est. Hours |
|:---:|------|-------|:---:|
| 🟡 P1 | Diagnosis→Document bridge | diagnosis-bridge.ts (new), diagnosis.ts (edit) | 4 |
| 🟡 P1 | Document editor + merge field UI | document-editor.tsx, merge-field-input.tsx (new) | 6 |
| 🟡 P1 | Document export (PDF/DOCX/TXT) | export.ts (new), /api/documents/export (new) | 4 |
| 🟡 P1 | Upgrade banner + pricing page | upgrade-banner.tsx, tier-badge.tsx, /packages/page.tsx | 3 |
| 🟡 P1 | Thai accuracy checks | thai-accuracy.ts (new) | 3 |

### Phase 3: Polish (Week 4) — ~15 hours

| Priority | Task | Files | Est. Hours |
|:---:|------|-------|:---:|
| 🟢 P2 | LINE bot webhook integration | /api/line/webhook (new), webhook.ts (new) | 5 |
| 🟢 P2 | Human review workflow UI | review-workflow.ts (new), admin review page | 4 |
| 🟢 P2 | Analytics events (extended) | types.ts (edit), events.ts (edit) | 2 |
| 🟢 P2 | FAQ page | /faq/page.tsx, faq.ts (new) | 2 |
| 🟢 P2 | Preventive document suggestions | diagnosis-bridge.ts (extend) | 2 |

### Phase 4: Launch Readiness (Week 5) — ~10 hours

| Priority | Task | Files | Est. Hours |
|:---:|------|-------|:---:|
| 🟢 P2 | Payment integration (LINE Pay / PromptPay) | /api/payments (new) | 4 |
| 🟢 P2 | Admin dashboard for template review | /admin/documents (new) | 3 |
| 🟢 P2 | E2E tests for document generation | tests/ directory | 3 |

---

## Total Files Summary

### New Files to Create (~25 files)

| File | Purpose |
|------|---------|
| `lib/documents/merge-engine.ts` | Core template filling engine |
| `lib/documents/categories.ts` | 10 business document categories |
| `lib/documents/export.ts` | PDF/DOCX/TXT export service |
| `lib/documents/diagnosis-bridge.ts` | Problem→Document mapping |
| `lib/documents/review-workflow.ts` | Human review checklist |
| `lib/documents/versioning.ts` | Semver version tracking |
| `lib/packages/tiers.ts` | 4-tier package definitions |
| `lib/packages/gate.ts` | API middleware for tier gating |
| `lib/legal/guardrails.ts` | Legal boundaries + PII redaction |
| `lib/legal/thai-accuracy.ts` | Thai language accuracy checks |
| `lib/legal/faq.ts` | FAQ database |
| `lib/legal/fear-calibration.ts` | Fear level assessment (from existing plan) |
| `lib/legal/urgency-windows.ts` | Deadline mapping (from existing plan) |
| `lib/line/webhook.ts` | LINE bot integration |
| `components/documents/document-editor.tsx` | Document creation UI |
| `components/documents/merge-field-input.tsx` | Dynamic form field |
| `components/packages/upgrade-banner.tsx` | Upgrade prompt |
| `components/packages/tier-badge.tsx` | Package badge |
| `app/documents/[templateId]/page.tsx` | Template detail page |
| `app/packages/page.tsx` | Pricing page |
| `app/api/documents/templates/route.ts` | Template listing API |
| `supabase/migrations/0003_document_categories.sql` | Enum + schema migration |
| `supabase/migrations/0004_seed_document_templates.sql` | 126 template seed data |

### Files to Modify (~15 files)

| File | Change |
|------|--------|
| `db/schema.ts` | Add document_category enum, expand documentTemplates |
| `domain/types.ts` | Expand LegalCategory (6→12), add AnalyticsEvents |
| `domain/repositories.ts` | Add DocumentRepository methods |
| `lib/legal/diagnosis-config.ts` | Add 6 new categories + fear calibration |
| `lib/legal/sources.ts` | Add 30+ new sources + government agencies |
| `lib/ai/diagnosis.ts` | Add recommendedDocuments to AnalysisResult |
| `lib/analytics/events.ts` | Add new event types |
| `lib/mock/categories.ts` | Add 6 new category labels |
| `app/api/documents/generate/route.ts` | Add merge engine + tier gates |
| `app/api/ai/diagnosis/route.ts` | Add tier discrimination |
| `app/api/evidence/upload-url/route.ts` | Add tier gate |
| `app/documents/page.tsx` | Complete rewrite for 10 categories |
| `supabase/migrations/0001_*.sql` | Update enum values |
| `components/ui/primitives.tsx` | Add TierBadge, UpgradeBanner exports |
| `lib/supabase/repositories.ts` | Extend document repository |

---

> **Grand Total: ~75 hours across 5 weeks · ~40 files touched · 25 new, 15 modified**
>
> ⚡ **Next Action:** Start with Phase 1, P0 items — the foundation must be solid before adding the business document layer.
