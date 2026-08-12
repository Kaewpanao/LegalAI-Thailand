# 🏛️ Chujai Legal (ชูใจ ลีกัล) — Master Design Document

> **Version:** 1.0 | **Date:** 12 August 2026 | **Status:** Complete Design
> **Philosophy:** "ชูใจ" = comfort/uplift the heart. Every interaction must feel warm, empathetic, empowering.
> **Sources:** V4 WARM Concierge Cat 1-6 (24 sub-problems) + Cat 7-12 (23 sub-problems) = 47 flows total

---

## TABLE OF CONTENTS

- [SECTION A: Project Structure](#section-a-project-structure)
- [SECTION B: Dashboard (Admin SaaS)](#section-b-dashboard-admin-saas)
- [SECTION C: Consumer App — 52 Flows → Pages](#section-c-consumer-app--52-flows--pages)
- [SECTION D: Question Flow Per Page](#section-d-question-flow-per-page)
- [SECTION E: Master Checklist (Phases 1-6)](#section-e-master-checklist-phases-1-6)

---

# SECTION A: Project Structure

## A.1 Project Name & Identity

| Field | Value |
|-------|-------|
| **Name** | Chujai Legal (ชูใจ ลีกัล) |
| **Meaning** | "ชูใจ" = uplift/hearten the heart |
| **Tagline** | "กฎหมายใกล้ตัว อุ่นใจทุกปัญหา" (Law is close — warm heart for every problem) |
| **Domain** | chujai.legal / chujai.co.th |
| **Audience** | Thai citizens seeking legal help + Lawyers managing cases |

## A.2 Tech Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Framework** | Next.js 15 (App Router) | SSR/SSG, React Server Components, API routes |
| **Language** | TypeScript 5.x (strict) | Type safety, developer experience |
| **Styling** | Tailwind CSS 4 + shadcn/ui | Thai-friendly typography, warm color palette |
| **Database** | Supabase (PostgreSQL 16) | Auth, real-time, RLS, storage, edge functions |
| **AI Engine** | DeepSeek V3 (via OpenRouter) | Best Thai language model, cost-effective |
| **Messaging** | LINE Messaging API | LINE notifications, reminders, lawyer chat |
| **Payments** | Omise / PromptPay QR | Thai payment gateway, PromptPay integration |
| **Storage** | Supabase Storage | Document uploads, evidence files |
| **Analytics** | Plausible / PostHog | Privacy-first, self-hosted option |
| **Email** | Resend | Transactional emails (welcome, case updates) |
| **CMS** | Built-in (Supabase tables) | Legal content, FAQs, templates |
| **Monitoring** | Sentry / Logflare | Error tracking, log aggregation |
| **CI/CD** | GitHub Actions | Build, test, deploy to Vercel |

## A.3 Folder Structure

```
chujai-legal/
├── app/                          # Next.js App Router
│   ├── (marketing)/              # Public marketing site
│   │   ├── page.tsx              # Landing page
│   │   ├── about/
│   │   ├── how-it-works/
│   │   └── layout.tsx
│   ├── (consumer)/               # Consumer app (authenticated)
│   │   ├── layout.tsx            # Consumer shell (nav, sidebar)
│   │   ├── page.tsx              # Consumer home dashboard
│   │   ├── search/               # AI legal search
│   │   │   └── page.tsx
│   │   ├── diagnosis/            # 8-phase diagnosis wizard
│   │   │   ├── page.tsx
│   │   │   └── [caseId]/         # Individual case
│   │   │       ├── page.tsx
│   │   │       └── phase-[1-8]/
│   │   ├── concierge/            # Full concierge flow
│   │   │   ├── page.tsx
│   │   │   ├── [caseId]/
│   │   │   │   └── page.tsx
│   │   │   └── new/
│   │   │       └── page.tsx
│   │   ├── documents/            # Document library + generator
│   │   │   ├── page.tsx
│   │   │   ├── [docId]/
│   │   │   └── generate/
│   │   ├── tax/                  # Tax calculator + optimizer
│   │   │   ├── page.tsx
│   │   │   └── report/
│   │   ├── lawyers/              # Lawyer marketplace
│   │   │   ├── page.tsx
│   │   │   ├── [lawyerId]/
│   │   │   └── hire/
│   │   ├── profile/              # User profile + settings
│   │   │   ├── page.tsx
│   │   │   ├── settings/
│   │   │   └── cases/
│   │   ├── pricing/              # Pricing & plans
│   │   │   └── page.tsx
│   │   ├── notifications/        # Notifications inbox
│   │   │   └── page.tsx
│   │   └── help/                 # Help center
│   │       └── page.tsx
│   ├── (lawyer)/                 # Lawyer app (authenticated)
│   │   ├── layout.tsx            # Lawyer shell
│   │   ├── page.tsx              # Lawyer dashboard
│   │   ├── cases/                # Case management
│   │   │   ├── page.tsx
│   │   │   ├── [caseId]/
│   │   │   │   └── page.tsx
│   │   │   └── new/
│   │   ├── clients/              # Client portal
│   │   │   ├── page.tsx
│   │   │   └── [clientId]/
│   │   ├── billing/              # Billing & invoices
│   │   │   ├── page.tsx
│   │   │   └── [invoiceId]/
│   │   ├── documents/            # Legal document templates
│   │   │   └── page.tsx
│   │   ├── profile/              # Lawyer profile
│   │   │   ├── page.tsx
│   │   │   ├── edit/
│   │   │   └── verification/
│   │   ├── analytics/            # Practice analytics
│   │   │   └── page.tsx
│   │   └── settings/
│   │       └── page.tsx
│   ├── (admin)/                  # Admin dashboard
│   │   ├── layout.tsx            # Admin shell
│   │   ├── page.tsx              # Admin overview
│   │   ├── users/                # User management
│   │   │   └── page.tsx
│   │   ├── cases/                # All case management
│   │   │   ├── page.tsx
│   │   │   └── [caseId]/
│   │   ├── lawyers/              # Lawyer verification
│   │   │   ├── page.tsx
│   │   │   └── [lawyerId]/
│   │   ├── revenue/              # Financial dashboard
│   │   │   ├── page.tsx
│   │   │   └── transactions/
│   │   ├── content/              # Content management
│   │   │   ├── page.tsx
│   │   │   ├── categories/
│   │   │   ├── templates/
│   │   │   └── faq/
│   │   ├── settings/             # Platform config
│   │   │   └── page.tsx
│   │   └── analytics/            # Platform analytics
│   │       └── page.tsx
│   ├── api/                      # API routes
│   │   ├── ai/
│   │   │   ├── diagnose/route.ts
│   │   │   ├── search/route.ts
│   │   │   ├── generate/route.ts
│   │   │   └── assistant/route.ts
│   │   ├── auth/
│   │   │   ├── login/route.ts
│   │   │   ├── register/route.ts
│   │   │   ├── line/route.ts
│   │   │   └── callback/route.ts
│   │   ├── cases/
│   │   │   ├── route.ts
│   │   │   └── [caseId]/route.ts
│   │   ├── documents/
│   │   │   ├── generate/route.ts
│   │   │   └── [docId]/route.ts
│   │   ├── lawyers/
│   │   │   ├── route.ts
│   │   │   └── [lawyerId]/route.ts
│   │   ├── payments/
│   │   │   ├── create/route.ts
│   │   │   ├── webhook/route.ts
│   │   │   └── verify/route.ts
│   │   ├── notifications/
│   │   │   ├── route.ts
│   │   │   └── line/route.ts
│   │   ├── admin/
│   │   │   ├── users/route.ts
│   │   │   ├── cases/route.ts
│   │   │   ├── lawyers/route.ts
│   │   │   └── revenue/route.ts
│   │   ├── tax/
│   │   │   ├── calculate/route.ts
│   │   │   └── optimize/route.ts
│   │   └── upload/
│   │       └── route.ts
│   ├── layout.tsx                # Root layout
│   ├── globals.css               # Global styles + Tailwind
│   ├── providers.tsx             # React context providers
│   ├── error.tsx                 # Error boundary
│   ├── loading.tsx               # Loading state
│   └── not-found.tsx             # 404 page
├── components/                   # Shared React components
│   ├── ui/                       # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── input.tsx
│   │   ├── badge.tsx
│   │   ├── table.tsx
│   │   ├── tabs.tsx
│   │   ├── progress.tsx
│   │   ├── toast.tsx
│   │   ├── select.tsx
│   │   ├── checkbox.tsx
│   │   ├── radio-group.tsx
│   │   ├── textarea.tsx
│   │   ├── accordion.tsx
│   │   ├── sheet.tsx
│   │   ├── breadcrumb.tsx
│   │   ├── dropdown-menu.tsx
│   │   ├── command.tsx
│   │   ├── calendar.tsx
│   │   ├── chart.tsx
│   │   ├── skeleton.tsx
│   │   ├── separator.tsx
│   │   ├── tooltip.tsx
│   │   └── avatar.tsx
│   ├── auth/                     # Auth components
│   │   ├── login-form.tsx
│   │   ├── register-form.tsx
│   │   ├── line-login-button.tsx
│   │   └── forgot-password.tsx
│   ├── concierge/                # Concierge flow components
│   │   ├── phase-container.tsx   # Phase wrapper with progress
│   │   ├── phase-1-understand.tsx
│   │   ├── phase-2-rights.tsx
│   │   ├── phase-3-path.tsx
│   │   ├── phase-3-gate.tsx      # Monetization gate
│   │   ├── phase-4-jurisdiction.tsx
│   │   ├── phase-5-documents.tsx
│   │   ├── phase-6-prepare.tsx
│   │   ├── phase-7-file.tsx
│   │   ├── phase-8-followup.tsx
│   │   ├── compound-detector.tsx
│   │   └── category-card.tsx
│   ├── diagnosis/                # Diagnosis wizard
│   │   ├── diagnosis-flow.tsx
│   │   ├── question-step.tsx
│   │   ├── fear-calibrator.tsx
│   │   └── result-card.tsx
│   ├── search/                   # AI search
│   │   ├── search-bar.tsx
│   │   ├── search-results.tsx
│   │   └── category-chips.tsx
│   ├── documents/                # Document engine
│   │   ├── document-editor.tsx
│   │   ├── document-preview.tsx
│   │   ├── merge-form.tsx
│   │   └── export-button.tsx
│   ├── tax/                      # Tax module
│   │   ├── tax-calculator.tsx
│   │   ├── deduction-chips.tsx
│   │   ├── bracket-sidebar.tsx
│   │   ├── savings-tracker.tsx
│   │   ├── filing-checklist.tsx
│   │   └── optimize-suggestions.tsx
│   ├── lawyers/                  # Lawyer marketplace
│   │   ├── lawyer-card.tsx
│   │   ├── lawyer-filter.tsx
│   │   ├── lawyer-review.tsx
│   │   ├── hire-dialog.tsx
│   │   └── lawyer-map.tsx
│   ├── trust/                    # Trust & social proof
│   │   ├── social-proof.tsx
│   │   ├── legal-disclaimer.tsx
│   │   ├── verified-badge.tsx
│   │   └── testimonial-card.tsx
│   ├── payments/                 # Payment components
│   │   ├── pricing-card.tsx
│   │   ├── checkout-dialog.tsx
│   │   ├── payment-method.tsx
│   │   └── invoice-row.tsx
│   ├── notifications/            # Notification components
│   │   ├── notification-bell.tsx
│   │   ├── notification-list.tsx
│   │   └── notification-item.tsx
│   ├── admin/                    # Admin components
│   │   ├── stat-card.tsx
│   │   ├── data-table.tsx
│   │   ├── line-chart.tsx
│   │   ├── pie-chart.tsx
│   │   ├── admin-nav.tsx
│   │   └── audit-log.tsx
│   ├── lawyer-app/               # Lawyer app components
│   │   ├── case-timeline.tsx
│   │   ├── client-chat.tsx
│   │   ├── billing-form.tsx
│   │   └── document-list.tsx
│   ├── marketing/                # Marketing components
│   │   ├── hero-section.tsx
│   │   ├── feature-grid.tsx
│   │   ├── how-it-works.tsx
│   │   ├── pricing-table.tsx
│   │   ├── testimonial-carousel.tsx
│   │   └── cta-banner.tsx
│   └── shared/                   # Cross-cutting shared
│       ├── page-header.tsx
│       ├── empty-state.tsx
│       ├── loading-spinner.tsx
│       ├── warm-tone-badge.tsx
│       ├── thai-currency.tsx
│       ├── thai-date.tsx
│       ├── confirmation-dialog.tsx
│       └── file-upload.tsx
├── lib/                          # Business logic (no React)
│   ├── ai/                       # AI engine
│   │   ├── client.ts             # DeepSeek client wrapper
│   │   ├── diagnosis.ts          # Diagnosis logic + drive detection
│   │   ├── search.ts             # AI search implementation
│   │   ├── generate.ts           # Document generation
│   │   ├── assistant.ts          # AI assistant/chat
│   │   ├── prompts/              # AI prompt templates
│   │   │   ├── diagnosis.ts
│   │   │   ├── search.ts
│   │   │   ├── concierge.ts
│   │   │   ├── document.ts
│   │   │   ├── tax.ts
│   │   │   └── warm-tone.ts      # Empathetic tone instructions
│   │   └── warm-tone.ts          # Tone calibration engine
│   ├── legal/                    # Legal domain logic
│   │   ├── categories.ts         # 12 category definitions
│   │   ├── diagnosis-config.ts   # Diagnosis question flows
│   │   ├── sources.ts            # Legal source registry
│   │   ├── fear-calibration.ts   # 4 fear levels + urgency windows
│   │   ├── compound-detection.ts # Multi-category case detection
│   │   ├── guardrails.ts         # Safety rules (7 MUST-NEVER)
│   │   ├── drive-detection.ts    # 22 human drives keyword mapping
│   │   ├── social-proof.ts       # Platform metrics + success signals
│   │   ├── category-drives.ts    # Per-category emotional framing
│   │   └── definitions.ts        # Legal Thai terminology
│   ├── concierge/                # Concierge flow engine
│   │   ├── flow-engine.ts        # 8-phase state machine
│   │   ├── jurisdiction.ts       # Court/police station lookup
│   │   ├── documents.ts          # Document checklist per category
│   │   └── timeline.ts           # Case timeline estimation
│   ├── documents/                # Document engine
│   │   ├── merge-engine.ts       # {{field}} replacement engine
│   │   ├── categories.ts         # Document category registry
│   │   ├── export.ts             # PDF/DOCX/TXT export
│   │   └── templates/            # Document templates (MD)
│   │       ├── police-report.md
│   │       ├── complaint-letter.md
│   │       ├── demand-letter.md
│   │       ├── consumer-filing.md
│   │       ├── divorce-petition.md
│   │       └── ...
│   ├── tax/                      # Tax module
│   │   ├── calculator.ts         # Progressive tax calculator
│   │   ├── deductions.ts         # All 30+ Thai deductions
│   │   ├── constants.ts          # Tax brackets, deadlines, caps
│   │   └── types.ts              # TaxResult, DeductionItem
│   ├── payments/                 # Payment logic
│   │   ├── omise.ts              # Omise API wrapper
│   │   ├── packages.ts           # Package definitions + feature gates
│   │   └── invoices.ts           # Invoice generation
│   ├── notifications/            # Notification engine
│   │   ├── line.ts               # LINE Messaging API
│   │   ├── email.ts              # Resend email
│   │   ├── push.ts               # Web push notifications
│   │   └── reminders.ts          # Case reminder scheduler
│   ├── auth/                     # Auth helpers
│   │   ├── middleware.ts         # Auth middleware
│   │   ├── rbac.ts               # Role-based access control
│   │   └── line-auth.ts          # LINE Login integration
│   ├── db/                       # Database utilities
│   │   ├── supabase.ts           # Supabase client (server)
│   │   ├── supabase-client.ts    # Supabase client (browser)
│   │   ├── queries/              # Typed database queries
│   │   │   ├── users.ts
│   │   │   ├── cases.ts
│   │   │   ├── documents.ts
│   │   │   ├── lawyers.ts
│   │   │   ├── payments.ts
│   │   │   └── admin.ts
│   │   └── types.ts              # Database-generated types
│   └── utils/                    # General utilities
│       ├── formatting.ts         # Thai dates, currency, IDs
│       ├── validation.ts         # Form validation
│       ├── geo.ts                # Thai province/district data
│       └── analytics.ts          # Analytics helpers
├── supabase/                     # Supabase config
│   ├── migrations/               # Database migrations
│   ├── seed.sql                  # Seed data
│   ├── edge-functions/           # Edge functions
│   │   ├── line-webhook/
│   │   ├── payment-webhook/
│   │   └── case-reminder/
│   └── config.toml
├── public/                       # Static assets
│   ├── images/
│   │   ├── logo.svg
│   │   ├── og-image.png
│   │   └── illustrations/
│   ├── fonts/
│   │   └── ... (Noto Sans Thai, Sarabun)
│   └── favicon.ico
├── types/                        # Global TypeScript types
│   ├── user.ts
│   ├── case.ts
│   ├── document.ts
│   ├── lawyer.ts
│   ├── payment.ts
│   └── admin.ts
├── config/                       # App configuration
│   ├── site.ts                   # Site metadata
│   ├── navigation.ts             # Nav structure
│   ├── pricing.ts                # Pricing plans
│   └── features.ts               # Feature flags
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── docs/
│   ├── chujai_legal_master_design.md
│   ├── api-reference.md
│   ├── database-schema.md
│   └── deployment.md
├── next.config.ts
├── tailwind.config.ts
├── tsconfig.json
├── package.json
├── components.json              # shadcn/ui config
├── .env.local
└── README.md
```

## A.4 Complete Route Map

### PUBLIC ROUTES (no auth)
```
/                               → Landing page
/about                          → About Chujai
/how-it-works                   → How the platform works
/pricing                        → Pricing plans
/help                           → Help center / FAQ
/auth/login                     → Login page
/auth/register                  → Register page
/auth/forgot-password            → Forgot password
/auth/line-callback              → LINE Login callback
/terms                          → Terms of service
/privacy                        → Privacy policy
```

### CONSUMER ROUTES (authenticated as consumer)
```
/(consumer)/                    → Consumer home dashboard
/(consumer)/search              → AI legal search
/(consumer)/diagnosis           → Diagnosis wizard (8-phase)
/(consumer)/diagnosis/[caseId]  → Case detail
/(consumer)/concierge           → All concierge cases
/(consumer)/concierge/new       → Start new concierge flow
/(consumer)/concierge/[caseId]  → Concierge case (8 phases)
/(consumer)/documents           → Document library
/(consumer)/documents/[docId]   → View/edit document
/(consumer)/documents/generate  → Generate new document
/(consumer)/tax                 → Tax calculator
/(consumer)/tax/report          → Tax report
/(consumer)/lawyers             → Lawyer marketplace
/(consumer)/lawyers/[lawyerId]  → Lawyer profile
/(consumer)/lawyers/hire        → Hire a lawyer
/(consumer)/notifications       → Notifications inbox
/(consumer)/profile             → User profile
/(consumer)/profile/settings    → Account settings
/(consumer)/profile/cases       → My cases
/(consumer)/pricing             → Pricing (with upgrade)
/(consumer)/help                → Help center
```

### LAWYER ROUTES (authenticated as lawyer)
```
/(lawyer)/                      → Lawyer dashboard
/(lawyer)/cases                 → Case management
/(lawyer)/cases/[caseId]        → Case detail
/(lawyer)/cases/new             → Create new case
/(lawyer)/clients               → Client list
/(lawyer)/clients/[clientId]    → Client detail
/(lawyer)/billing               → Billing & invoices
/(lawyer)/billing/[invoiceId]   → Invoice detail
/(lawyer)/documents             → Document templates
/(lawyer)/profile               → Lawyer profile
/(lawyer)/profile/edit          → Edit profile
/(lawyer)/profile/verification  → Identity verification
/(lawyer)/analytics             → Practice analytics
/(lawyer)/settings              → Settings
```

### ADMIN ROUTES (authenticated as admin)
```
/(admin)/                       → Admin overview dashboard
/(admin)/users                  → User management
/(admin)/cases                  → All cases
/(admin)/cases/[caseId]         → Case detail
/(admin)/lawyers                → Lawyer verification
/(admin)/lawyers/[lawyerId]     → Lawyer detail
/(admin)/revenue                → Revenue dashboard
/(admin)/revenue/transactions   → Transaction list
/(admin)/content                → Content management
/(admin)/content/categories     → Category management
/(admin)/content/templates      → Template management
/(admin)/content/faq            → FAQ management
/(admin)/analytics              → Platform analytics
/(admin)/settings               → Platform settings
```

### API ROUTES
```
/api/ai/diagnose                → AI diagnosis
/api/ai/search                  → AI legal search
/api/ai/generate                → Document generation
/api/ai/assistant               → AI assistant chat
/api/auth/login                 → Email/password login
/api/auth/register              → User registration
/api/auth/line                  → LINE Login initiation
/api/auth/callback              → LINE Login callback
/api/cases                      → List/create cases
/api/cases/[caseId]             → Get/update case
/api/documents/generate         → Generate document
/api/documents/[docId]          → Get/update document
/api/lawyers                    → List lawyers
/api/lawyers/[lawyerId]         → Get lawyer
/api/payments/create            → Create payment
/api/payments/webhook           → Omise webhook
/api/payments/verify            → Verify payment
/api/notifications              → Get notifications
/api/notifications/line         → LINE webhook
/api/tax/calculate              → Tax calculation
/api/tax/optimize               → Tax optimization
/api/upload                     → File upload
/api/admin/users                → Admin: user CRUD
/api/admin/cases                → Admin: case CRUD
/api/admin/lawyers              → Admin: lawyer CRUD
/api/admin/revenue              → Admin: revenue data
```

---

# SECTION B: Dashboard (Admin SaaS)

## B.1 /admin — Overview Dashboard

### Purpose
Real-time platform KPI dashboard for admins.

### Key Metrics
- **Users**: Total, New Today, Active This Month, Churned
- **Revenue**: MRR, ARR, Today's Revenue, Projected
- **Cases**: Total Active, Completed, Average Resolution Time
- **Lawyers**: Verified, Pending Verification, Active
- **AI Usage**: Diagnoses Run, Documents Generated, Searches

### Charts
```
┌──────────────────────────────────────────────────────────┐
│  📊 Overview Dashboard                   [Last 30 Days ▼] │
├──────────────────────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │Users │ │Revenue│ │Cases │ │Active│ │Lawyer│ │AI    │  │
│  │8,421 │ │฿245K │ │1,203 │ │892   │ │47    │ │12.4K │  │
│  │↑12%  │ │↑8%   │ │↑15%  │ │↑5%   │ │↑3    │ │↑22%  │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐ ┌─────────────────────────────┐ │
│  │ Revenue Over Time    │ │ Cases by Category           │ │
│  │ 📈 Line Chart        │ │ 🥧 Pie Chart                 │ │
│  └─────────────────────┘ └─────────────────────────────┘ │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐ │
│  │ 🔔 Recent Activity                                   │ │
│  │ • New user: somchai@email.com (2 min ago)            │ │
│  │ • Case created: #LA-2026-0892 (5 min ago)            │ │
│  │ • Payment: ฿299 from user_0421 (12 min ago)          │ │
│  │ • Lawyer verified: ทนายสมหมาย (30 min ago)           │ │
│  │ • AI diagnosis completed: online_fraud (45 min ago)   │ │
│  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### AI Questions (for Admin)
| AI Asks | AI Returns |
|---------|-----------|
| "สรุป metrics วันนี้?" | Daily summary: users +X, revenue +฿X, alerts |
| "แนวโน้ม users?" | 7/30/90 day trend chart + forecast |
| "category ไหนมีปัญหาเยอะสุด?" | Top 5 categories by case volume + resolution rate |
| "มี anomaly อะไร?" | Automated anomaly detection (spike in fraud cases, drop in payments) |

### Checklist
- [ ] All stat cards render with real data
- [ ] Charts update when date range changes  
- [ ] Recent activity updates in real-time (Supabase real-time)
- [ ] Responsive layout (mobile sidebar → top tabs)
- [ ] Loading skeletons for all widgets
- [ ] Error states with retry buttons
- [ ] Export dashboard as PDF

---

## B.2 /admin/users — User Management

### Purpose
Manage all platform users (consumers + lawyers).

### Features
- **User table**: Name, email, role, plan, created, last active, status
- **Filters**: Role (consumer/lawyer/admin), Plan (free/action/case/sme), Status (active/inactive/banned)
- **Search**: Name, email, phone
- **Mass actions**: Export, Bulk delete, Bulk plan change
- **User detail modal**: Full profile, cases, payments, activity log
- **Actions**: Ban/unban, Change role, Change plan, Delete

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  👥 Users / Management                                     │
│  ┌──────────────────────┐ [Export] [Add User]              │
│  │🔍 Search users...     │                                  │
│  └──────────────────────┘                                  │
│  Filters: [Role ▼] [Plan ▼] [Status ▼]                    │
├──────────────────────────────────────────────────────────┤
│  Name       │ Email         │ Role  │ Plan   │ Joined  │   │
│  ─────────────────────────────────────────────────────────│
│  สมชาย ใจดี │ somchai@...   │Consumer│ Free │ 12/08/26│ 🔧│
│  ทนายสมหมาย │ lawyer1@...   │Lawyer │ Pro   │ 10/08/26│ 🔧│
│  ...                                                                        │
├──────────────────────────────────────────────────────────┤
│  Showing 1-25 of 8,421 users      [← 1 2 3 ... 337 →]    │
└──────────────────────────────────────────────────────────┘
```

### Checklist
- [ ] Paginated user table with sorting
- [ ] Role/plan/status filters work
- [ ] Search by name/email/phone
- [ ] User detail modal with tabs (Profile, Cases, Payments, Activity)
- [ ] Ban/unban with confirmation dialog
- [ ] Bulk CSV export
- [ ] Audit log for admin actions

---

## B.3 /admin/cases — All Cases

### Purpose
View and manage all cases across the platform.

### Features
- **Case table**: Case ID, User, Category, Status, Created, Last Updated, Assigned Lawyer
- **Filters**: Category (12 categories), Status (active/pending/closed/archived), Priority
- **Case detail**: Full case timeline, phases completed, documents, AI analysis, lawyer assignment
- **Actions**: Assign lawyer, Close case, Reopen, Delete

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  📂 Cases / All Cases                                      │
│  ┌──────────────────────┐ [Filters ▼]                      │
│  │🔍 Search cases...     │                                  │
│  └──────────────────────┘                                  │
│  Category: [All ▼]  Status: [All ▼]  Priority: [All ▼]    │
├──────────────────────────────────────────────────────────┤
│  Case ID    │ User    │ Category     │ Status  │ Created│   │
│  ─────────────────────────────────────────────────────────│
│  LA-2026-0892│สมชาย    │ online_fraud │ 🟡 Active│12/08│ 🔍│
│  LA-2026-0891│สมหญิง   │ labour       │ 🟢 Closed│11/08│ 🔍│
│  LA-2026-0890│อนุชา    │ defamation   │ 🔴 Urgent│11/08│ 🔍│
│  ...                                                                        │
└──────────────────────────────────────────────────────────┘
```

### AI Questions
| AI Asks | AI Returns |
|---------|-----------|
| "case อายุมากสุดที่ยังเปิดอยู่?" | Oldest open cases sorted by age |
| "lawyer คนไหนรับ case เยอะสุด?" | Lawyer workload distribution |
| "category ไหนปิด case ช้าสุด?" | Average resolution time by category |
| "มี case ที่ต้อง escalation มั้ย?" | Cases flagged for admin attention |

### Checklist
- [ ] Paginated case table
- [ ] Category/status/priority filters
- [ ] Case detail view with full timeline
- [ ] Lawyer assignment UI
- [ ] Case status transitions (with validation)
- [ ] Bulk actions (close, archive, assign)
- [ ] Export filtered cases to CSV

---

## B.4 /admin/lawyers — Lawyer Verification

### Purpose
Verify and manage lawyer accounts.

### Verification Flow
1. Lawyer submits application (license photo, ID, bar number)
2. Admin reviews documents
3. Admin approves/rejects with reason
4. Lawyer profile goes live (or stays pending)

### Features
- **Pending queue**: Lawyers awaiting verification
- **Verified list**: All verified lawyers
- **Rejected list**: Rejected applications (with reason)
- **Lawyer detail**: Profile, license image, bar number verification
- **Actions**: Approve, Reject (with reason), Request more info, Suspend, Ban
- **Stats**: Verification rate, average review time

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  👨‍⚖️ Lawyers / Verification          [Pending: 3] [Verified: 47]│
├──────────────────────────────────────────────────────────┤
│  Tabs: [🟡 Pending (3)] [🟢 Verified (47)] [🔴 Rejected (5)] │
├──────────────────────────────────────────────────────────┤
│  Lawyer     │ Bar #    │ Specialization │ Applied │ Actions│
│  ─────────────────────────────────────────────────────────│
│  สมหมาย รัก │ 12345/2567│ Criminal, Civil│ 10/08/26│ 👁 [✓][✗]│
│  ธรรม        │          │               │         │        │
│  วิภาดา ใจดี │ 67890/2567│ Family, Labour │ 11/08/26│ 👁 [✓][✗]│
│  ...                                                                        │
└──────────────────────────────────────────────────────────┘
```

### Verification Detail Modal
```
┌──────────────────────────────────────────────────────────┐
│  👁 Verify: ทนายสมหมาย รักธรรม                              │
├──────────────────────────────────────────────────────────┤
│  📋 Profile:                                               │
│  • Full Name: สมหมาย รักธรรม                               │
│  • Bar Number: 12345/2567                                  │
│  • License Expiry: 31/12/2569                              │
│  • Specialization: Criminal Law, Civil Law                 │
│  • Years of Practice: 12                                   │
│  • Province: กรุงเทพมหานคร                                  │
│                                                             │
│  📎 Documents:                                              │
│  ┌──────────────────────────────┐                         │
│  │ [📷 License Photo]            │ [📷 ID Card]            │ │
│  └──────────────────────────────┘                         │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ 📝 Rejection Reason (optional):                        │ │
│  │ "______________________________________"               │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                             │
│  [✓ Approve]  [✗ Reject]  [↩ Request More Info]            │
└──────────────────────────────────────────────────────────┘
```

### Checklist
- [ ] Pending/verified/rejected tabs
- [ ] Document viewer (license + ID card images)
- [ ] Approve with one click
- [ ] Reject requires reason (sent to lawyer)
- [ ] Request more info sends notification
- [ ] Audit log of all verification actions
- [ ] Bulk approve (select multiple)

---

## B.5 /admin/revenue — Financial Dashboard

### Purpose
Track platform revenue, payments, and financial health.

### Features
- **Revenue summary**: MRR, ARR, Today, This Month, Projected
- **Revenue charts**: Revenue over time, By plan, By payment method
- **Transaction table**: All payments with filters
- **Payout tracking**: Lawyer payouts (if marketplace takes commission)
- **Refund management**: Refund requests and processing
- **Export**: Financial reports (monthly, quarterly, yearly)

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  💰 Revenue Dashboard                [This Month ▼] [Export]│
├──────────────────────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │  MRR │ │  ARR │ │ Today│ │ Month│ │Avg/Usr│ │Refunds│ │
│  │฿89K  │ │฿1.07M│ │฿3.2K│ │฿245K│ │฿29   │ │฿1.2K │  │
│  │↑15%  │ │↑15%  │ │      │ │↑8%  │ │      │ │↓2%   │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐ ┌─────────────────────────────┐ │
│  │ Revenue Over Time    │ │ Revenue by Plan             │ │
│  │ 📈 Line (daily)      │ │ 🥧 Pie (Free/Action/Case/SME)│ │
│  └─────────────────────┘ └─────────────────────────────┘ │
├──────────────────────────────────────────────────────────┤
│  📋 Transactions                                            │
│  ID    │ User  │ Plan     │ Amount│ Method  │ Date  │Status│
│  ──────────────────────────────────────────────────────────│
│  TXN-001│สมชาย  │Action Pack│฿299  │ PromptPay│12/08 │✅    │
│  TXN-002│สมหญิง │Case Plus  │฿999  │ Credit  │12/08 │✅    │
│  ...                                                                        │
│  Total: ฿245,320.00                                        │
└──────────────────────────────────────────────────────────┘
```

### AI Questions
| AI Asks | AI Returns |
|---------|-----------|
| "revenue trend เทียบเดือนก่อน?" | MoM comparison with % change |
| "plan ไหนสร้างรายได้มากสุด?" | Revenue breakdown by plan tier |
| "คาดการณ์ revenue เดือนหน้า?" | Forecast based on 3-month trend |
| "มี payment ที่ failed มั้ย?" | List of failed/reversed payments |

### Checklist
- [ ] Real-time revenue stats
- [ ] Date range filter on all charts
- [ ] Transaction table with search + export
- [ ] Plan breakdown chart
- [ ] Refund flow (admin can issue refunds)
- [ ] Monthly financial report generation
- [ ] Lawyer commission tracking (if applicable)

---

## B.6 /admin/content — Content Management

### Purpose
Manage legal content, AI training data, and platform copy.

### Features
- **Categories**: Add/edit legal categories and sub-problems
- **Templates**: Document template management (add/edit/disable)
- **FAQ**: Frequently asked questions management
- **Sources**: Legal source registry (laws, sections, authorities)
- **Prompts**: AI prompt templates management
- **Copy**: Platform text strings (Thai + English)

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  📝 Content Management                                      │
│  Tabs: [Categories] [Templates] [FAQ] [Sources] [Prompts]  │
├──────────────────────────────────────────────────────────┤
│  📂 Categories (12/12)                         [Add Category]│
│  ┌────────────────────────────────────────────────────────┐│
│  │ ID │ Category     │ Sub-Problems│ Active Cases│ Status ││
│  │───│────────────│────────────│────────────│────────││
│  │ 1  │ online_fraud│ 5           │ 342         │ ✅     ││
│  │ 2  │ crime       │ 4           │ 156         │ ✅     ││
│  │ 3  │ defamation  │ 4           │ 98          │ ✅     ││
│  │ ... │             │             │             │        ││
│  └────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────┤
│  📄 Templates (24)                              [Add Template]│
│  ┌────────────────────────────────────────────────────────┐│
│  │ Name              │ Category     │ Updated   │ Usage  ││
│  │──────────────────│────────────│──────────│────────││
│  │ Police Report     │ general      │ 10/08/26  │ 1,204  ││
│  │ Demand Letter     │ general      │ 10/08/26  │ 892    ││
│  │ Consumer Filing   │ consumer     │ 09/08/26  │ 456    ││
│  │ ...               │              │           │        ││
│  └────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────┘
```

### Checklist
- [ ] Category CRUD with sub-problems
- [ ] Template editor (markdown with preview)
- [ ] FAQ CRUD with categories
- [ ] Source registry with law section validation
- [ ] Prompt version history
- [ ] Content publishing workflow (draft → review → publish)
- [ ] i18n support for Thai/English strings

---

## B.7 /admin/settings — Platform Configuration

### Purpose
Configure platform-wide settings.

### Settings Sections
- **General**: Platform name, logo, contact info, social links
- **AI**: Model selection, temperature, token limits, fallback behavior
- **Payments**: Omise keys, PromptPay settings, commission rates
- **LINE**: LINE channel settings, webhook URL, notification templates
- **Email**: SMTP settings, email templates
- **Security**: Rate limiting, session timeout, 2FA requirement
- **Notifications**: Default notification preferences
- **Maintenance**: Maintenance mode toggle, announcement banner

### UI Layout
```
┌──────────────────────────────────────────────────────────┐
│  ⚙️ Platform Settings                                       │
├──────────────────────────────────────────────────────────┤
│  Sidebar:                                                  │
│  • 📋 General                                              │
│  • 🤖 AI Configuration                                     │
│  • 💰 Payments                                             │
│  • 💬 LINE Integration                                     │
│  • 📧 Email                                                │
│  • 🔒 Security                                             │
│  • 🔔 Notifications                                        │
│  • 🛠️ Maintenance                                          │
├──────────────────────────────────────────────────────────┤
│  🤖 AI Configuration                                       │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Model: [DeepSeek V3 ▼]                               │  │
│  │ API Key: [••••••••••••••••]    [Test Connection]      │  │
│  │ Temperature: [━━━━━●━━] 0.7                          │  │
│  │ Max Tokens: [4000]                                    │  │
│  │ Fallback Model: [Claude 3.5 Sonnet ▼]                 │  │
│  │                                                       │  │
│  │ [Save Changes]                                         │  │
│  └─────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### Checklist
- [ ] All settings sections implemented
- [ ] AI connection test button
- [ ] Payment gateway configuration
- [ ] LINE webhook verification
- [ ] Email template preview
- [ ] Maintenance mode with custom message
- [ ] Settings audit log
- [ ] Import/export settings

---

# SECTION C: Consumer App — 52 Flows → Pages

## C.1 Flow-to-Page Mapping

Each of the 47 concierge sub-problems maps to the same 8-phase concierge flow, routed through the `/concierge` pages. The 52 flows include the 47 sub-problems plus 5 utility flows (search, tax, documents, lawyers, profile).

### Category Flow Map

```
CATEGORY 1: online_fraud (5 sub-problems)
├── 1.1 ซื้อของออนไลน์ไม่ได้ของ → /concierge/new → flow online_fraud
├── 1.2 Call Center → /concierge/new → flow online_fraud
├── 1.3 แอปกู้เงินเถื่อน → /concierge/new → flow online_fraud
├── 1.4 Romance Scam → /concierge/new → flow online_fraud
└── 1.5 แชร์ลูกโซ่ → /concierge/new → flow online_fraud

CATEGORY 2: crime (4 sub-problems)
├── 2.1 ทำร้ายร่างกาย → /concierge/new → flow crime
├── 2.2 ลักทรัพย์ → /concierge/new → flow crime
├── 2.3 ข่มขืน/อนาจาร → /concierge/new → flow crime
└── 2.4 ขู่กรรโชก → /concierge/new → flow crime

CATEGORY 3: defamation (4 sub-problems)
├── 3.1 ถูกด่าบนโซเชียล → /concierge/new → flow defamation
├── 3.2 ภาพหลุด/Revenge Porn → /concierge/new → flow defamation
├── 3.3 ถูกใส่ความ → /concierge/new → flow defamation
└── 3.4 PDPA ข้อมูลรั่วไหล → /concierge/new → flow defamation

CATEGORY 4: insurance (3 sub-problems)
├── 4.1 เคลมประกันรถ → /concierge/new → flow insurance
├── 4.2 เคลมประกันสุขภาพ → /concierge/new → flow insurance
└── 4.3 ยกเลิกกรมธรรม์ → /concierge/new → flow insurance

CATEGORY 5: government (3 sub-problems)
├── 5.1 ขอทะเบียน/บัตร ปชช. → /concierge/new → flow government
├── 5.2 รัฐละเมิด → /concierge/new → flow government
└── 5.3 ร้องเรียนไม่ตอบ → /concierge/new → flow government

CATEGORY 6: property (5 sub-problems)
├── 6.1 บุกรุก → /concierge/new → flow property
├── 6.2 พิพาทแนวเขต → /concierge/new → flow property
├── 6.3 ซื้อขายไม่ได้ → /concierge/new → flow property
├── 6.4 มรดก → /concierge/new → flow property
└── 6.5 โฉนดหาย → /concierge/new → flow property

CATEGORY 7: labour (4 sub-problems)
├── 7.1 ถูกเลิกจ้างไม่เป็นธรรม → /concierge/new → flow labour
├── 7.2 ไม่จ่ายค่าจ้าง/ค่าชดเชย → /concierge/new → flow labour
├── 7.3 บาดเจ็บจากการทำงาน → /concierge/new → flow labour
└── 7.4 ล่วงละเมิดในที่ทำงาน → /concierge/new → flow labour

CATEGORY 8: consumer (4 sub-problems)
├── 8.1 สินค้าชำรุด/ไม่ตรงปก → /concierge/new → flow consumer
├── 8.2 โฆษณาหลอกลวง → /concierge/new → flow consumer
├── 8.3 บริการไม่เป็นไปตามสัญญา → /concierge/new → flow consumer
└── 8.4 ถูกเอาเปรียบจากสัญญาสำเร็จรูป → /concierge/new → flow consumer

CATEGORY 9: debt (4 sub-problems)
├── 9.1 หนี้บัตรเครดิตท่วม → /concierge/new → flow debt
├── 9.2 ถูกฟ้องล้มละลาย → /concierge/new → flow debt
├── 9.3 หนี้นอกระบบ → /concierge/new → flow debt
└── 9.4 ค้ำประกันแล้วลูกหนี้หนี → /concierge/new → flow debt

CATEGORY 10: housing (3 sub-problems)
├── 10.1 ถูกไล่ออกจากหอ/คอนโด → /concierge/new → flow housing
├── 10.2 มัดจำไม่คืน → /concierge/new → flow housing
└── 10.3 ค่าเช่าขึ้นไม่เป็นธรรม → /concierge/new → flow housing

CATEGORY 11: family (5 sub-problems)
├── 11.1 หย่าร้าง → /concierge/new → flow family
├── 11.2 แบ่งสินสมรส → /concierge/new → flow family
├── 11.3 ค่าเลี้ยงดูบุตร → /concierge/new → flow family
├── 11.4 การรับบุตรบุญธรรม → /concierge/new → flow family
└── 11.5 ความรุนแรงในครอบครัว → /concierge/new → flow family

CATEGORY 12: accident (3 sub-problems)
├── 12.1 ถูกชนแล้วหนี → /concierge/new → flow accident
├── 12.2 ชนแล้วคู่กรณีไม่ยอม → /concierge/new → flow accident
└── 12.3 เรียกค่าเสียหายจากอุบัติเหตุ → /concierge/new → flow accident
```

### Utility Flows (5)
```
UTILITY 1: AI Search → /search
UTILITY 2: Tax Calculator → /tax
UTILITY 3: Document Library → /documents
UTILITY 4: Lawyer Marketplace → /lawyers
UTILITY 5: User Profile → /profile
```

### Total: 47 concierge sub-problems + 5 utility flows = 52 flows

## C.2 Page-by-Page Design

### C.2.1 / — Consumer Home (Authenticated)

```
┌──────────────────────────────────────────────────────────┐
│  🌸 ชูใจ (Chujai)                     [🔔] [👤 โปรไฟล์]    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🫶 สวัสดีค่ะ คุณสมชาย                                  │  │
│  │                                                       │  │
│  │ มีอะไรให้ชูใจช่วยวันนี้?                                 │  │
│  │                                                       │  │
│  │ ┌──────────────────────────────────────────────┐    │  │
│  │ │ 🔍 เล่าเรื่องให้เราฟังหน่อย...                   │    │  │
│  │ │ "เช่น ถูกโกงเงิน, โดนไล่ออก, มีปัญหาหนี้..."      │    │  │
│  │ │                                       [เริ่มเลย→]│    │  │
│  │ └──────────────────────────────────────────────┘    │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────────────┐ ┌──────────────────────┐      │
│  │ 🔍 AI ค้นหากฎหมาย     │ │ 🩺 ตรวจวินิจฉัยปัญหา   │      │
│  │ ค้นหาด้วยภาษาคน       │ │ รู้สิทธิ์ของคุณใน 5 นาที │      │
│  │                [ไป →]│ │                [ไป →]│      │
│  └──────────────────────┘ └──────────────────────┘      │
│                                                          │
│  ┌──────────────────────┐ ┌──────────────────────┐      │
│  │ 📄 สร้างเอกสาร         │ │ 💰 คำนวณภาษี           │      │
│  │ คำฟ้อง, หนังสือ, สัญญา │ │ วางแผนภาษีให้ประหยัดสุด │      │
│  │                [ไป →]│ │                [ไป →]│      │
│  └──────────────────────┘ └──────────────────────┘      │
│                                                          │
│  ┌──────────────────────┐ ┌──────────────────────┐      │
│  │ 👨‍⚖️ หาทนาย             │ │ 📚 คลังความรู้          │      │
│  │ ทนายเฉพาะทางใกล้บ้าน   │ │ กฎหมายที่ควรรู้          │      │
│  │                [ไป →]│ │                [ไป →]│      │
│  └──────────────────────┘ └──────────────────────┘      │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 📋 เคสที่คุณกำลังดำเนินการ                             │  │
│  │ ┌─────────────────────────────────────────────────┐ │  │
│  │ │ 🟡 LA-2026-0892 — ซื้อของออนไลน์ไม่ได้ของ         │ │  │
│  │ │ Phase 3/8 · อัปเดตล่าสุด: เมื่อวาน                 │ │  │
│  │ │                                        [ทำต่อ →]│ │  │
│  │ ├─────────────────────────────────────────────────┤ │  │
│  │ │ 🟢 LA-2026-0845 — ถูกเลิกจ้าง (ปิดแล้ว)            │ │  │
│  │ │ เสร็จสิ้น · 05/08/26                              │ │  │
│  │ │                                        [ดูสรุป →]│ │  │
│  │ └─────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 💬 "ชูใจช่วยคนไทยมาแล้ว 12,000+ เคส"                  │  │
│  │ ⭐ 4.8/5 จากผู้ใช้ 8,400+ คน                           │  │
│  │ "ไม่เคยคิดว่าจะจัดการเรื่องกฎหมายเองได้ ขอบคุณมากค่ะ"     │  │
│  │ — คุณวิภา, กรุงเทพฯ                                   │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### C.2.2 /concierge/new — Start New Concierge Flow

This is the ENTRY POINT for all 47 sub-problems. The user narrates their issue in natural language, and the AI detects the category and launches the 8-phase concierge flow.

```
┌──────────────────────────────────────────────────────────┐
│  ← กลับ          🧭 ที่ปรึกษากฎหมาย                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🎯 Phase 1: เล่าเรื่องให้เราฟัง                       │  │
│  │                                                       │  │
│  │ 😊 สวัสดีค่ะ เราคือ "ชูใจ"                               │  │
│  │                                                       │  │
│  │ ไม่ว่าจะเกิดอะไรขึ้น — เราอยู่ตรงนี้เพื่อช่วยคุณ             │  │
│  │                                                       │  │
│  │ 💬 เล่าให้เราฟังหน่อย ว่าเกิดอะไรขึ้นกับคุณ?               │  │
│  │ ┌──────────────────────────────────────────────┐    │  │
│  │ │                                              │    │  │
│  │ │ (พิมพ์เล่าเรื่องของคุณด้วยภาษาของคุณเอง)          │    │  │
│  │ │                                              │    │  │
│  │ │ เช่น: "สั่งของใน Shopee แล้วไม่ส่งของ"           │    │  │
│  │ │ "โดน call center หลอกให้โอนเงิน"               │    │  │
│  │ │ "ถูกไล่ออกจากงานกะทันหัน"                       │    │  │
│  │ │                                              │    │  │
│  │ └──────────────────────────────────────────────┘    │  │
│  │                                        [วิเคราะห์ →]│  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  หรือเลือกหมวดหมู่เอง:                                      │
│  ┌─────────────────────────────────────────────────────┐ │
│  │ [🌐 ถูกโกง] [👊 อาชญากรรม] [💬 หมิ่นประมาท]          │ │
│  │ [🏥 ประกัน] [🏛️ ราชการ] [🏠 ที่ดิน]                   │ │
│  │ [💼 แรงงาน] [🛒 ผู้บริโภค] [💸 หนี้]                   │ │
│  │ [🏢 ที่อยู่อาศัย] [👨‍👩‍👧 ครอบครัว] [🚗 อุบัติเหตุ]       │ │
│  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### C.2.3 /concierge/[caseId] — Concierge Case (8 Phases)

Each case follows the 8-phase flow within the same route, using a stepper/phase indicator.

```
┌──────────────────────────────────────────────────────────┐
│  ← กลับ    🧭 Case #LA-2026-0892                          │
├──────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🔵━━🔵━━🔵━━⚪━━⚪━━⚪━━⚪━━⚪  (Phase 3/8)            │  │
│  │ ①เข้าใจ ②สิทธิ์ ③เลือกทาง ④เขตอำนาจ ⑤เอกสาร ⑥สร้าง ⑦ยื่น ⑧ติดตาม│  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🆓 PHASE 1/8: เกิดอะไรขึ้น?                           │  │
│  │                                                       │  │
│  │ 😔 เราเข้าใจความรู้สึกของคุณนะ                           │  │
│  │                                                       │  │
│  │ จากที่คุณเล่า เราตรวจพบว่าเกี่ยวข้องกับ:                    │  │
│  │                                                       │  │
│  │ 1. 💰 ฉ้อโกง — สั่งของแล้วไม่ส่ง                          │  │
│  │ 2. 🌐 พ.ร.บ.คอมพิวเตอร์ ม.14(1) — หลอกลวงทางออนไลน์    │  │
│  │                                                       │  │
│  │ 📋 สรุปข้อมูลที่เราได้:                                   │  │
│  │ • สั่งซื้อสินค้าออนไลน์ — โอนเงินแล้ว                      │  │
│  │ • ผู้ขายไม่ส่งของ / หายไป / บล็อก                         │  │
│  │ • แพลตฟอร์ม: Shopee                                    │  │
│  │ • จำนวนเงิน: 3,500 บาท                                  │  │
│  │                                                       │  │
│  │ ข้อมูลยังขาด:                                           │  │
│  │ • 👤 ชื่อผู้ขาย: ______                                 │  │
│  │ • 📱 ช่องทางติดต่อ: ______                              │  │
│  │ • ⏰ วันที่โอน: ______                                  │  │
│  │                                                       │  │
│  │ 💪 ข่าวดี: เรื่องนี้แก้ได้ — และคุณมีสิทธิเต็มที่!         │  │
│  │                                                       │  │
│  │ [แก้ไขข้อมูล]              [ถัดไป: สิทธิของคุณ →]        │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

The 8 phases render as cards within the case page:
1. **PHASE 1**: Understand — AI parses narrative, detects category/ies (compound), identifies missing info
2. **PHASE 2**: Rights — Shows exact laws, penalties, self-help actions, critical warnings
3. **PHASE 3**: Path — Choose A (self-file), B (hire lawyer), or C (negotiate) + MONETIZATION GATE (฿299)
4. **PHASE 4**: Jurisdiction — Court lookup, police station finder, online filing options
5. **PHASE 5**: Documents — Checklist + evidence upload + readiness progress bar
6. **PHASE 6**: Prepare — AI generates documents (คำฟ้อง, คำร้อง, letters)
7. **PHASE 7**: File — Step-by-step filing instructions (online or physical)
8. **PHASE 8**: Follow-up — Timeline, reminders, contact schedule (฿999 Case Plus)

### C.2.4 /search — AI Legal Search

```
┌──────────────────────────────────────────────────────────┐
│  🔍 ค้นหากฎหมาย                                           │
├──────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🔍 ถามอะไรก็ได้เกี่ยวกับกฎหมาย...                      │  │
│  │ ┌──────────────────────────────────────────────┐    │  │
│  │ │ "ดอกเบี้ยบัตรเครดิตสูงสุดกี่ % ?"                │    │  │
│  │ └──────────────────────────────────────────────┘    │  │
│  │                                         [🔍 ค้นหา] │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  หมวดหมู่ยอดนิยม:                                            │
│  [💰 หนี้] [💼 แรงงาน] [🏠 ที่ดิน] [👨‍👩‍👧 ครอบครัว] [+6]      │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 📄 ผลลัพธ์                                            │  │
│  │ ┌─────────────────────────────────────────────────┐ │  │
│  │ │ ⚖️ กฎหมายดอกเบี้ย                                     │ │  │
│  │ │                                                    │ │  │
│  │ │ 📜 พ.ร.บ. ห้ามเรียกดอกเบี้ยเกินอัตรา พ.ศ. 2560       │ │  │
│  │ │ • ดอกเบี้ยสูงสุด = 15% ต่อปี                          │ │  │
│  │ │ • เกินกว่านี้ = เป็นโมฆะ จ่ายแค่เงินต้น                │ │  │
│  │ │ • โทษ: จำคุกไม่เกิน 2 ปี ปรับไม่เกิน 200,000 บาท     │ │  │
│  │ │                                                    │ │  │
│  │ │ 📚 แหล่งอ้างอิง: ราชกิจจานุเบกษา                     │ │  │
│  │ │ [อ่านเพิ่มเติม →]  [เริ่มเคสใหม่ →]                  │ │  │
│  │ └─────────────────────────────────────────────────┘ │  │
│  │ ┌─────────────────────────────────────────────────┐ │  │
│  │ │ ❓ คำถามที่เกี่ยวข้อง                                  │ │  │
│  │ │ • ดอกเบี้ยบัตรเครดิตสูงสุดเท่าไหร่?                    │ │  │
│  │ │ • ถูกเรียกดอกเบี้ยเกิน ฟ้องได้ไหม?                     │ │  │
│  │ │ • หนี้นอกระบบดอกเบี้ยโหด ทำไง?                       │ │  │
│  │ └─────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### C.2.5 /diagnosis — Diagnosis Wizard

```
┌──────────────────────────────────────────────────────────┐
│  🩺 ตรวจวินิจฉัยปัญหา                                      │
├──────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🔵━━⚪━━⚪━━⚪  (Step 1/4)                            │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ ❓ เกิดอะไรขึ้นกับคุณ?                                 │  │
│  │                                                       │  │
│  │ เลือกได้มากกว่า 1 ข้อ:                                  │  │
│  │                                                       │  │
│  │ ☐ มีคนเอาของฉันไป / ขโมย                                │  │
│  │ ☐ ถูกทำร้ายร่างกาย                                       │  │
│  │ ☐ ถูกโกง / หลอกลวง                                      │  │
│  │ ☐ ถูกคุกคาม / ข่มขู่                                     │  │
│  │ ☐ มีปัญหากับสัญญา / ข้อตกลง                              │  │
│  │ ☐ มีปัญหากับที่ดิน / บ้าน                                 │  │
│  │ ☐ มีปัญหากับครอบครัว                                     │  │
│  │ ☐ อื่นๆ: ______________                                 │  │
│  │                                                       │  │
│  │ [⬅ กลับ]                         [ถัดไป: รายละเอียด →] │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  (Subsequent steps narrow down to specific category,     │
│   sub-problem, ask key details, then route to concierge)  │
└──────────────────────────────────────────────────────────┘
```

### C.2.6 /documents — Document Library & Generator

```
┌──────────────────────────────────────────────────────────┐
│  📄 เอกสารของฉัน                                           │
├──────────────────────────────────────────────────────────┤
│  [📄 เอกสารทั้งหมด] [⭐ ที่ใช้บ่อย] [🤖 สร้างใหม่]           │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 📄 เอกสารของฉัน (12 รายการ)        [🔍 ค้นหา] [สร้างใหม่]│  │
│  │ ┌─────────────────────────────────────────────────┐ │  │
│  │ │ 📝 บันทึกแจ้งความ — LA-2026-0892                  │ │  │
│  │ │ ประเภท: บันทึก · สร้าง: 12/08/26 · 🟡 ร่าง        │ │  │
│  │ │                                        [แก้ไข →]│ │  │
│  │ ├─────────────────────────────────────────────────┤ │  │
│  │ │ ✉️ จดหมายทวงถาม — LA-2026-0892                  │ │  │
│  │ │ ประเภท: จดหมาย · สร้าง: 12/08/26 · 🟢 เสร็จ     │ │  │
│  │ │                                        [ดู →]  │ │  │
│  │ ├─────────────────────────────────────────────────┤ │  │
│  │ │ ...                                              │ │  │
│  │ └─────────────────────────────────────────────────┘ │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 🤖 สร้างเอกสารใหม่                                    │  │
│  │                                                       │  │
│  │ 📂 เลือกประเภทเอกสาร:                                   │  │
│  │ 🏛️ คำฟ้อง  ✉️ จดหมาย  📋 บันทึก  ⚖️ คำร้อง          │  │
│  │ 📊 รายงาน  📑 สัญญา  🏥 ประกัน  💼 แรงงาน             │  │
│  │                                                       │  │
│  │ หรือสร้างจากเคสที่มีอยู่:                                 │  │
│  │ ┌──────────────────────────────────────────────┐    │  │
│  │ │ LA-2026-0892 — ซื้อของออนไลน์ไม่ได้ของ [สร้างเอกสาร→] │  │
│  │ └──────────────────────────────────────────────┘    │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### C.2.7 /tax — Tax Calculator & Optimizer

```
┌──────────────────────────────────────────────────────────┐
│  💰 คำนวณภาษีเงินได้บุคคลธรรมดา                            │
├──────────────────────────────────────────────────────────┤
│  Tabs: [🧮 คำนวณ] [💡 วางแผน] [📋 เช็คลิสต์ยื่นภาษี]      │
├──────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐ ┌─────────────────────────────┐│
│  │ 📊 รายได้               │ │ 💰 สรุปภาษี                  ││
│  │                        │ │                             ││
│  │ เงินเดือน: [50,000]฿/ด.││ │ รายได้ทั้งปี: 600,000 บาท    ││
│  │ โบนัส:     [100,000]฿  │ │ หักค่าใช้จ่าย: -100,000      ││
│  │ อื่นๆ:     [0]฿        │ │ หักค่าลดหย่อน: -200,000      ││
│  │                        │ │ เงินได้สุทธิ: 300,000 บาท    ││
│  │ 📊 ค่าลดหย่อน:           │ │                             ││
│  │ ☑ ส่วนตัว 60,000        │ │ ภาษีที่ต้องจ่าย: ฿7,500      ││
│  │ ☑ ประกันสังคม 9,000     │ │ อัตราภาษีจริง: 1.25%         ││
│  │ ☑ RMF 50,000           │ │                             ││
│  │ ☐ SSF                  │ │ 📈 Bracket: 5%              ││
│  │ ☐ บุตร                 │ │                             ││
│  │ ☐ บิดามารดา             │ │ 💡 ประหยัดได้อีก: ฿5,500     ││
│  │ [+15 รายการ]           │ │ (ถ้าใช้ SSF + ประกันสุขภาพ)   ││
│  └──────────────────────┘ └─────────────────────────────┘│
└──────────────────────────────────────────────────────────┘
```

### C.2.8 /lawyers — Lawyer Marketplace

```
┌──────────────────────────────────────────────────────────┐
│  👨‍⚖️ หาทนาย                                               │
├──────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐ [📍 ใกล้ฉัน] [🔍 ค้นหา]         │
│  │🔍 ค้นหาทนาย...       │                                  │
│  └──────────────────────┘                                  │
│  หมวด: [ทั้งหมด ▼]  จังหวัด: [ทั้งหมด ▼]  ประสบการณ์: [ทั้งหมด ▼]│
├──────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────────────────────────┐  │
│  │ ┌────┐ ทนายสมหมาย รักธรรม            ⭐ 4.9 (87 รีวิว) │  │
│  │ │📷  │ กฎหมายอาญา · แพ่ง · ผู้บริโภค                  │  │
│  │ │    │ 12 ปี · กรุงเทพฯ                                │  │
│  │ │    │ ฿3,000-5,000 / ครั้ง                             │  │
│  │ └────┘                                    [ดูโปรไฟล์ →]│  │
│  ├────────────────────────────────────────────────────┤  │
│  │ ┌────┐ ทนายวิภาดา ใจดี               ⭐ 4.8 (54 รีวิว) │  │
│  │ │📷  │ กฎหมายครอบครัว · มรดก                            │  │
│  │ │    │ 8 ปี · นนทบุรี                                    │  │
│  │ │    │ ฿2,500-4,000 / ครั้ง                             │  │
│  │ └────┘                                    [ดูโปรไฟล์ →]│  │
│  ├────────────────────────────────────────────────────┤  │
│  │ ...                                                  │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### C.2.9 /pricing — Pricing

```
┌──────────────────────────────────────────────────────────┐
│  💰 แพ็กเกจ — เลือกที่เหมาะกับคุณ                            │
├──────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────┐│
│  │ 🆓 ฟรี     │ │ ⚡ Action Pack│ │ ⭐ Case Plus  │ │ 🏢 SME   ││
│  │          │ │              │ │              │ │         ││
│  │ ฿0      │ │ ฿299         │ │ ฿999         │ │฿2,990/ด.││
│  │          │ │ ครั้งเดียว     │ │ ครั้งเดียว     │ │         ││
│  │          │ │              │ │              │ │         ││
│  │✓ 1 เอกสาร │ │✓ ทุกอย่างฟรี  │ │✓ ทุกอย่างใน   │ │✓ ทุกอย่าง ││
│  │✓ 3 ตรวจ   │ │✓ ไม่จำกัดเอกสาร│ │  Case Plus   │ │✓ เอกสาร   ││
│  │  วินิจฉัย │ │✓ อัปโหลด     │ │✓ ติดตามคดี   │ │  ธุรกิจ   ││
│  │✓ ค้นหา    │ │  หลักฐาน     │ │✓ แจ้งเตือน    │ │✓ ทีม 5 คน ││
│  │✓ คำนวณภาษี│ │✓ สร้างเอกสาร │ │✓ ปรึกษาทนาย  │ │✓ ภาษีนิติ  ││
│  │✓ ดูทนาย   │ │✓ ขั้นตอนศาล  │ │  3 ครั้ง      │ │✓ API      ││
│  │          │ │✓ คำนวนภาษี   │ │✓ LINE แจ้ง   │ │         ││
│  │          │ │  ขั้นสูง     │ │              │ │         ││
│  │          │ │              │ │              │ │         ││
│  │[เริ่มใช้ฟรี]│ │[ซื้อเลย ฿299]│ │[ซื้อเลย ฿999]│ │[ติดต่อเรา]││
│  └──────────┘ └──────────────┘ └──────────────┘ └─────────┘│
├──────────────────────────────────────────────────────────┤
│  📊 เปรียบเทียบแพ็กเกจ                                     │
│  ┌────────────────────────────────────────────────────┐  │
│  │ Feature              │🆓│⚡ ฿299│⭐ ฿999│🏢 ฿2,990│  │
│  │──────────────────────│──│──────│──────│────────│  │
│  │ ตรวจวินิจฉัย AI       │3 │ไม่จำกัด│ไม่จำกัด│ไม่จำกัด  │  │
│  │ สร้างเอกสาร           │1 │ไม่จำกัด│ไม่จำกัด│ไม่จำกัด  │  │
│  │ อัปโหลดหลักฐาน        │✗ │✓     │✓     │✓       │  │
│  │ AI ขั้นตอนศาล         │✗ │✓     │✓     │✓       │  │
│  │ ติดตามคดีอัตโนมัติ     │✗ │✗     │✓     │✓       │  │
│  │ LINE แจ้งเตือน         │✗ │✗     │✓     │✓       │  │
│  │ ปรึกษาทนาย            │✗ │✗     │3 ครั้ง │10 ครั้ง  │  │
│  │ เอกสารธุรกิจ           │✗ │✗     │✗      │✓       │  │
│  │ ทีม (หลาย user)       │✗ │✗     │✗      │✓ (5)   │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### C.2.10 /profile — User Profile

```
┌──────────────────────────────────────────────────────────┐
│  👤 โปรไฟล์                                                │
├──────────────────────────────────────────────────────────┤
│  ┌────────────────────┐                                   │
│  │ 📷                 │ คุณสมชาย ใจดี                        │
│  │                    │ somchai@email.com                   │
│  │                    │ 📞 08x-xxx-xxxx                     │
│  │                    │                                     │
│  │                    │ 📦 แพ็กเกจ: 🆓 ฟรี                   │
│  │                    │ [อัปเกรด →]                         │
│  └────────────────────┘                                   │
│                                                          │
│  Tabs: [📊 ภาพรวม] [📋 เคสของฉัน] [📄 เอกสาร] [💰 การชำระเงิน] │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ 📊 ภาพรวม                                            │  │
│  │ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐            │  │
│  │ │เคส     │ │เอกสาร  │ │เคสที่  │ │เงินที่   │            │  │
│  │ │ทั้งหมด  │ │ที่สร้าง │ │ปิดแล้ว │ │ประหยัด  │            │  │
│  │ │  5     │ │  8     │ │  3     │ │฿45,000 │            │  │
│  │ └───────┘ └───────┘ └───────┘ └───────┘            │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ ⚙️ ตั้งค่า                                            │  │
│  │ • 🔔 การแจ้งเตือน (LINE / Email / In-App)             │  │
│  │ • 🔒 ความเป็นส่วนตัว + PDPA                           │  │
│  │ • 📤 ส่งออกข้อมูล / 🗑️ ลบบัญชี                        │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

# SECTION D: Question Flow Per Page

## D.1 Master Question Matrix

For every page, we define: what the USER provides, what the AI ASKS, what the AI RETURNS, and what the CHECKLIST verifies.

### HOME (/)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | Natural language problem description | "มีอะไรให้ชูใจช่วยวันนี้?" | Category detection + "เราพบว่าเรื่องนี้เกี่ยวกับ..." | [ ] Input accepts Thai NL<br>[ ] AI detects category correctly<br>[ ] Warm empathetic greeting shown<br>[ ] Active cases listed with correct status |
| 2 | (None) | - | Active cases + status | [ ] Each case shows phase progress<br>[ ] "Do next" links work<br>[ ] Social proof metrics display |
| 3 | (None) | - | Feature cards: Search, Diagnosis, Documents, Tax, Lawyers | [ ] All 6 cards render<br>[ ] Card links navigate correctly<br>[ ] Icons + descriptions load |

### DIAGNOSIS (/diagnosis) — 4-Step Wizard

| Step | User Provides | AI Asks | AI Returns | Checklist |
|------|--------------|---------|------------|-----------|
| 1 | Multiple-choice: what happened (9 options + custom) | "เกิดอะไรขึ้นกับคุณ? เลือกได้มากกว่า 1 ข้อ" | Narrowed category list | [ ] All 9 options render<br>[ ] Multi-select works<br>[ ] Custom text input saves<br>[ ] "Next" enables only when >=1 selected |
| 2 | Specific details (time, place, people, amounts) | Context-dependent questions per category | Refined sub-problem match | [ ] Questions dynamically generated per category<br>[ ] Thai date picker works<br>[ ] Currency input validates |
| 3 | Fear/urgency level (panic→planning) | "คุณรู้สึกเร่งด่วนแค่ไหน?" | Fear-calibrated tone + urgency window | [ ] 4 fear levels render<br>[ ] Tone changes per level<br>[ ] Urgency badge shown |
| 4 | Confirm + launch concierge | "ข้อมูลนี้ถูกต้องไหม?" | Route to /concierge/new with context | [ ] Summary card shows all inputs<br>[ ] "Start Concierge" button navigates<br>[ ] Back navigation preserves data |

### CONCIERGE (/concierge/[caseId]) — 8 Phases

| Phase | User Provides | AI Asks | AI Returns | Checklist |
|-------|--------------|---------|------------|-----------|
| 1: Understand | Full narrative text | "เล่าเรื่องให้เราฟังหน่อย" + "ข้อมูลยังขาดอะไรอีก?" | Category detection, compound case flag, summary, missing info prompts | [ ] Narrative parsed correctly<br>[ ] Category detected accurately<br>[ ] Compound cases flagged<br>[ ] Missing info highlighted with inline inputs<br>[ ] Empathetic opening message |
| 2: Rights | (Read only) | "พร้อมเรียนรู้สิทธิของคุณหรือยัง?" | Exact law sections, penalties, self-help actions, warnings, urgency level | [ ] All relevant laws listed with section numbers<br>[ ] Penalties shown (jail/fine)<br>[ ] Self-help actions enumerated<br>[ ] Critical DO NOT warnings shown<br>[ ] Urgency badge color-coded<br>[ ] Perjury warning included |
| 3: Path | Choice: A/B/C | "คุณอยากจัดการแบบไหน?" | 3 paths with cost/time/effort comparison + MONETIZATION GATE | [ ] Path A (self-file) shown with steps<br>[ ] Path B (hire lawyer) shown with cost range<br>[ ] Path C (negotiate/emergency) shown<br>[ ] Lawyer 10-point checklist included<br>[ ] Mediation benefits box shown<br>[ ] MONETIZATION GATE renders at correct position<br>[ ] ฿299 anchor price vs lawyer cost comparison<br>[ ] Free trial offer (1 document) shown |
| 4: Jurisdiction | Location (province/district) | "คุณอยู่ที่ไหน?" | Court name, address, phone; police station; online filing links | [ ] Province/district selector works<br>[ ] Correct court returned<br>[ ] Police station info displayed<br>[ ] Online filing links work<br>[ ] Blue-shirt receptionist info box<br>[ ] Court taxonomy explainer |
| 5: Documents | Evidence uploads | "คุณมีเอกสารเหล่านี้หรือยัง?" | Document checklist per category + readiness % + upload prompts | [ ] Checklist specific to category<br>[ ] Readiness % bar updates<br>[ ] File upload works (images, PDF)<br>[ ] Missing items visually distinct<br>[ ] What + how-to-get for each doc |
| 6: Prepare | (Wait) | (None — AI generating) | Generated documents list + missing evidence warnings | [ ] Loading animation during generation<br>[ ] All documents listed with checkmarks<br>[ ] AI-detected gaps highlighted<br>[ ] Download all button<br>[ ] Upload more button |
| 7: File | (Read + confirm) | "พร้อมดำเนินการหรือยัง?" | Step-by-step instructions: where, how, who, docs, cost, time | [ ] Steps numbered and clear<br>[ ] Each step has: where, how, who, docs, cost, time<br>[ ] Court behavior rules box<br>[ ] Courtroom etiquette box<br>[ ] Appeals guidance (if applicable)<br>[ ] "Done" confirmation button |
| 8: Follow-up | (Subscribe to Case Plus) | "อยากให้เราติดตามคดีให้ไหม?" | Timeline, contact schedule, Case Plus upsell (฿999) | [ ] Timeline rendered with checkmarks<br>[ ] Contact schedule listed<br>[ ] Case Plus card with benefits<br>[ ] Upgrade button<br>[ ] Appeals/ฎีกา guidance box |

### SEARCH (/search)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | Search query in Thai | (None) | AI-generated legal answer with law citations | [ ] Search fires on Enter + button click<br>[ ] Loading state during AI call<br>[ ] Results show law sections<br>[ ] Source citations included<br>[ ] Related questions shown<br>[ ] "Start case" button per result<br>[ ] Empty state for no results<br>[ ] Error state if AI fails |
| 2 | Category chip click | - | Pre-filtered results | [ ] Category chips render all 12<br>[ ] Click filters results<br>[ ] Active chip visually distinct |

### DOCUMENTS (/documents)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | (View list) | - | All user documents sorted by date | [ ] Document list renders with status<br>[ ] Filter by type works<br>[ ] Search by name works<br>[ ] Empty state shows CTA |
| 2 | Select template + choose case | "สร้างเอกสารจากเคสไหน?" | Generated document with merge fields filled | [ ] Template list renders by category<br>[ ] Case selector shows active cases<br>[ ] Generation triggers AI flow<br>[ ] Document preview renders<br>[ ] Merge fields replaced correctly<br>[ ] Thai dates formatted correctly<br>[ ] Export: PDF/DOCX/TXT |

### TAX (/tax)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | Income + deductions | (Guided form) | Tax calculation + bracket visualization | [ ] Income inputs (salary, bonus, other)<br>[ ] Deduction chips (15+ items) toggle<br>[ ] Bracket sidebar with progress<br>[ ] Real-time recalculation<br>[ ] Savings tracker vs optimized |
| 2 | Click "Optimize" | - | AI optimization suggestions | [ ] AI suggests additional deductions<br>[ ] Shows potential savings<br>[ ] Filing checklist with 6 steps<br>[ ] Export tax report |

### LAWYERS (/lawyers)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | Filter criteria | - | Filtered lawyer list | [ ] Category filter (12 categories)<br>[ ] Province filter (77 provinces)<br>[ ] Experience filter<br>[ ] Price range filter<br>[ ] Rating sort |
| 2 | Click lawyer card | - | Lawyer detail profile | [ ] Full profile with photo<br>[ ] Verification badge<br>[ ] Reviews + ratings<br>[ ] Specialization tags<br>[ ] Contact/hire button |
| 3 | Click "Hire" | "เลือกรูปแบบการว่าจ้าง?" | Hire confirmation + payment flow | [ ] Consultation vs full-case options<br>[ ] Price shown clearly<br>[ ] Omise checkout integration |

### PROFILE (/profile)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | (View) | - | Profile summary, stats, active plan | [ ] Avatar + name + email<br>[ ] Plan badge with upgrade CTA<br>[ ] Stats: cases, documents, savings<br>[ ] Active case list |
| 2 | Toggle settings | - | Settings saved | [ ] Notification prefs (LINE/Email/InApp)<br>[ ] PDPA data export<br>[ ] Data delete with confirmation<br>[ ] AI consent toggle |

### PRICING (/pricing)

| # | User Provides | AI Asks | AI Returns | Checklist |
|---|--------------|---------|------------|-----------|
| 1 | (View) | - | 4-tier comparison table | [ ] All 4 tiers render<br>[ ] Feature comparison matrix<br>[ ] Most popular highlighted<br>[ ] CTA per tier<br>[ ] FAQs below table |
| 2 | Click upgrade | "ยืนยันการอัปเกรด?" | Omise checkout | [ ] Payment modal opens<br>[ ] PromptPay + Credit Card options<br>[ ] Confirmation after payment<br>[ ] Plan updates immediately |

---

## D.2 Category-Specific Question Flows

Each of the 12 categories has unique questions in Phase 1 (Understand) and Phase 5 (Documents):

### online_fraud (5 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 1.1 ซื้อของไม่ได้ของ | แพลตฟอร์ม? จำนวนเงิน? วันที่โอน? ชื่อผู้ขาย? | สลิปโอน, แคปแชท, โปรไฟล์ผู้ขาย, Statement, เลขบัญชี, แคปโพสต์, บัตร ปชช. |
| 1.2 Call Center | เบอร์ที่โทร? อ้างเป็นใคร? จำนวนเงิน? วันที่? | Statement, เลขบัญชีปลายทาง, Call Log, บันทึกเนื้อหา, SMS/Line, บัตร ปชช. |
| 1.3 แอปกู้เถื่อน | ชื่อแอป? ดอกเบี้ยเท่าไหร่? จำนวนเงินกู้? วันที่? | แคปแอป, ข้อความทวงหนี้, Call Log, สลิปกู้, ใบอนุญาต (bot.or.th), บัตร ปชช. |
| 1.4 Romance Scam | แพลตฟอร์ม? ระยะเวลา? จำนวนเงินทั้งหมด? | สลิปทั้งหมด, แคปโปรไฟล์, แคปแชททั้งหมด, รูป, Statement, เลขบัญชีม้า, บันทึก Timeline, บัตร ปชช. |
| 1.5 แชร์ลูกโซ่ | ชื่อบริษัท? คนชักชวน? ลงทุนเท่าไหร่? จ่ายผลตอบแทนกี่ครั้ง? | Statement, สลิปโอนทั้งหมด, แคปโพสต์/แชท, เอกสารการลงทุน, รายชื่อผู้เสียหายอื่น, บัตร ปชช. |

### crime (4 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 2.1 ทำร้ายร่างกาย | ใคร? ที่ไหน? เมื่อไหร่? บาดเจ็บอย่างไร? ไป รพ. หรือยัง? | บัตร ปชช., ใบรับรองแพทย์, รูปบาดแผล, พยาน, แจ้งความ (ถ้ามี), แผนที่เกิดเหตุ |
| 2.2 ลักทรัพย์ | อะไรหาย? มูลค่า? ที่ไหน? เมื่อไหร่? มีกล้องวงจรปิด? | บัตร ปชช., รายการทรัพย์ที่หาย, รูปสถานที่, กล้องวงจรปิด (ถ้ามี), พยาน |
| 2.3 ข่มขืน/อนาจาร | ใคร? ที่ไหน? เมื่อไหร่? ไป รพ. หรือยัง? มีพยาน? | บัตร ปชช., ใบรับรองแพทย์ (นิติเวช), เสื้อผ้าที่ใส่, พยาน, หลักฐานการสื่อสาร |
| 2.4 ขู่กรรโชก | ใคร? ขู่ว่าอะไร? เรียกเท่าไหร่? ช่องทาง? | บัตร ปชช., หลักฐานการขู่ (แชท/บันทึกเสียง), Statement (ถ้าโอน), พยาน |

### defamation (4 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 3.1 ถูกด่าบนโซเชียล | ใครโพสต์? โพสต์อะไร? แพลตฟอร์มไหน? URL? | บัตร ปชช., แคปโพสต์ (เห็น URL, วันที่), โปรไฟล์ผู้โพสต์, แจ้งแพลตฟอร์ม |
| 3.2 ภาพหลุด/Revenge Porn | ใครเผยแพร่? แพลตฟอร์มไหน? รู้จักคนเผยแพร่ไหม? | บัตร ปชช., แคปภาพ+URL, โปรไฟล์คนเผยแพร่, Timeline, แจ้งแพลตฟอร์ม |
| 3.3 ถูกใส่ความ | ใคร? ใส่ความว่าอะไร? ต่อใคร? ช่องทาง? | บัตร ปชช., หลักฐานการใส่ความ, พยาน, Timeline, ผลกระทบ (ตกงาน/เสียชื่อ) |
| 3.4 PDPA ข้อมูลรั่ว | ข้อมูลอะไร? จากใคร? มีหลักฐาน? แจ้ง สคส. หรือยัง? | บัตร ปชช., หลักฐานการรั่วไหล, Logs, การติดต่อกับองค์กร, หนังสือถึง สคส. |

### insurance (3 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 4.1 เคลมประกันรถ | บริษัทประกัน? เลขทะเบียน? เลขเคลม? เกิดเหตุเมื่อไหร่? | บัตร ปชช., กรมธรรม์, ใบเคลม, รูปอุบัติเหตุ, บันทึกประจำวัน, ใบคู่กรณี |
| 4.2 เคลมประกันสุขภาพ | บริษัทประกัน? เลขกรมธรรม์? ค่ารักษา? วันที่? | บัตร ปชช., กรมธรรม์, ใบเสร็จ รพ., ใบรับรองแพทย์, หนังสือปฏิเสธการเคลม |
| 4.3 ยกเลิกกรมธรรม์ | บริษัท? เลขกรมธรรม์? เหตุผลที่ยกเลิก? ซื้อเมื่อไหร่? | บัตร ปชช., กรมธรรม์, หนังสือขอยกเลิก, หลักฐานการชำระเบี้ย |

### government (3 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 5.1 ขอทะเบียน/บัตร ปชช. | เอกสารอะไร? ทำไมต้องขอใหม่? ที่ว่าการอำเภอไหน? | ทะเบียนบ้าน, บัตร ปชช. (ถ้ามี), ใบแจ้งความ (ถ้าหาย), สูติบัตร |
| 5.2 รัฐละเมิด | หน่วยงานไหน? ทำอะไร? ความเสียหาย? เมื่อไหร่? | บัตร ปชช., หลักฐานความเสียหาย, Timeline, หนังสือถึงหน่วยงาน, คำสั่ง/ประกาศ |
| 5.3 ร้องเรียนไม่ตอบ | หน่วยงานไหน? ร้องเรียนเรื่องอะไร? เมื่อไหร่? | บัตร ปชช., สำเนาคำร้อง, หลักฐานการยื่น, Timeline การติดตาม |

### property (5 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 6.1 บุกรุก | ใครบุกรุก? ที่ดินอยู่ที่ไหน? บุกรุกแบบไหน? ตั้งแต่เมื่อไหร่? | บัตร ปชช., โฉนด, รูปที่ดิน, พยาน, แผนที่, หนังสือบอกกล่าว |
| 6.2 พิพาทแนวเขต | กับใคร? ที่ดินอยู่ที่ไหน? มีโฉนด? รังวัดหรือยัง? | โฉนด (ทั้ง 2 ฝั่ง), หลักเขต, หนังสือรับรอง, แผนที่, รูปถ่าย |
| 6.3 ซื้อขายไม่ได้ | ผู้ซื้อ/ผู้ขาย? ราคา? ติดปัญหาอะไร? มัดจำ? | สัญญาซื้อขาย, โฉนด, สลิปมัดจำ, บัตร ปชช., ทะเบียนบ้าน |
| 6.4 มรดก | ใครเสีย? มีพินัยกรรมไหม? ทายาทมีใครบ้าง? ทรัพย์มรดกอะไร? | มรณบัตร, ทะเบียนบ้าน, บัตร ปชช. ทายาท, พินัยกรรม, โฉนด, สมุดบัญชี |
| 6.5 โฉนดหาย | โฉนดที่ดินไหน? หายได้ยังไง? แจ้งความหรือยัง? | บัตร ปชช., ใบแจ้งความ, ทะเบียนบ้าน, เอกสารประกอบ (ภบท.5), หลักฐานการถือครอง |

### labour (4 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 7.1 เลิกจ้างไม่เป็นธรรม | ทำงานที่ไหน? ตำแหน่ง? เงินเดือน? ทำงานมากี่ปี? เลิกจ้างเพราะอะไร? | สัญญาจ้าง, สลิปเงินเดือน, หนังสือเลิกจ้าง, Statement, บัตร ปชช. |
| 7.2 ไม่จ่ายค่าจ้าง/ค่าชดเชย | ค้างจ่ายเท่าไหร่? กี่เดือน? นายจ้างคือใคร? | สัญญาจ้าง, สลิปเงินเดือน, Statement, บันทึกการทำงาน, หลักฐานการทวงถาม |
| 7.3 บาดเจ็บจากการทำงาน | ที่ไหน? เมื่อไหร่? บาดเจ็บอย่างไร? นายจ้างรู้หรือยัง? | บัตร ปชช., ใบรับรองแพทย์, รายงานอุบัติเหตุ, สัญญาจ้าง, รูปถ่าย |
| 7.4 ล่วงละเมิดในที่ทำงาน | ใคร? ทำอะไร? เมื่อไหร่? มีพยาน? เคยแจ้ง HR หรือยัง? | บัตร ปชช., หลักฐาน (แชท/อีเมล), บันทึกเหตุการณ์, พยาน, คำร้อง HR |

### consumer (4 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 8.1 สินค้าชำรุด/ไม่ตรงปก | สินค้าอะไร? ซื้อจากไหน? ราคา? เมื่อไหร่? แจ้งผู้ขายหรือยัง? | บัตร ปชช., ใบเสร็จ, รูปสินค้า, แคปแชท, หลักฐานการแจ้งผู้ขาย |
| 8.2 โฆษณาหลอกลวง | โฆษณาอะไร? แพลตฟอร์มไหน? ซื้อเพราะโฆษณานี้? ความเสียหาย? | แคปโฆษณา, ใบเสร็จ, รูปสินค้า, บัตร ปชช., หลักฐานการติดต่อ |
| 8.3 บริการไม่เป็นไปตามสัญญา | บริการอะไร? ตกลงอะไร? ไม่ได้อะไร? จ่ายเงินหรือยัง? | สัญญา, ใบเสร็จ, หลักฐานความเสียหาย, บัตร ปชช., หนังสือบอกกล่าว |
| 8.4 สัญญาสำเร็จรูป | สัญญาเรื่องอะไร? กับใคร? ข้อไหนไม่เป็นธรรม? | สัญญา, บัตร ปชช., หลักฐานการชำระเงิน, หนังสือโต้แย้ง |

### debt (4 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 9.1 หนี้บัตรเครดิต | ธนาคารไหน? ยอดหนี้? ค้างกี่เดือน? มีรายได้เท่าไหร่? | Statement, บัตร ปชช., สลิปเงินเดือน, ข้อความทวงหนี้, หนังสือประนอมหนี้ |
| 9.2 ถูกฟ้องล้มละลาย | ใครฟ้อง? ยอดหนี้? ศาลไหน? ได้รับหมายศาลหรือยัง? | หมายศาล, Statement, บัตร ปชช., รายการทรัพย์สิน, หนี้ทั้งหมด |
| 9.3 หนี้นอกระบบ | กู้จากใคร? ดอกเบี้ยเท่าไหร่? จำนวนเงิน? ถูกทวงยังไง? | บัตร ปชช., หลักฐานการกู้, ข้อความทวงหนี้, Call Log, Statement |
| 9.4 ค้ำประกันแล้วลูกหนี้หนี | ค้ำให้ใคร? จำนวนเงิน? เจ้าหนี้คือใคร? ลูกหนี้ไปไหน? | สัญญาค้ำประกัน, บัตร ปชช., Statement, หลักฐานการตามหาลูกหนี้ |

### housing (3 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 10.1 ถูกไล่ออกจากหอ | อยู่ที่ไหน? สัญญาเช่า? จ่ายค่าเช่าหรือยัง? ไล่เพราะอะไร? | สัญญาเช่า, บัตร ปชช., สลิปค่าเช่า, หนังสือบอกเลิกสัญญา, รูปห้อง |
| 10.2 มัดจำไม่คืน | มัดจำเท่าไหร่? วันที่เข้าอยู่? วันที่ออก? เจ้าของหอบอกเหตุผล? | สัญญาเช่า, สลิปมัดจำ, บัตร ปชช., รูปห้องตอนออก, แคปแชท |
| 10.3 ค่าเช่าขึ้นไม่เป็นธรรม | ขึ้นเท่าไหร่? สัญญาว่าอย่างไร? แจ้งล่วงหน้ากี่วัน? | สัญญาเช่า, บัตร ปชช., หนังสือแจ้งขึ้นค่าเช่า, สลิปค่าเช่าเดิม |

### family (5 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 11.1 หย่าร้าง | จดทะเบียนที่ไหน? มีบุตร? เหตุผลหย่า? ตกลงทรัพย์สินกันได้ไหม? | ทะเบียนสมรส, บัตร ปชช. ทั้งสองฝ่าย, สูติบัตรบุตร, ทรัพย์สิน, ข้อตกลง (ถ้ามี) |
| 11.2 แบ่งสินสมรส | ทรัพย์อะไรบ้าง? มูลค่า? ได้มาระหว่างสมรส? | ทะเบียนสมรส, โฉนด, สมุดบัญชี, หลักฐานทรัพย์สิน, บัตร ปชช. |
| 11.3 ค่าเลี้ยงดูบุตร | บุตรอายุกี่ขวบ? อีกฝ่ายมีรายได้เท่าไหร่? จ่ายหรือยัง? | สูติบัตร, บัตร ปชช., สลิปเงินเดือนอีกฝ่าย, หลักฐานค่าใช้จ่ายบุตร |
| 11.4 รับบุตรบุญธรรม | บุตรอายุ? ผู้ปกครองเดิม? เหตุผล? คุณสมบัติผู้รับ? | บัตร ปชช., ทะเบียนบ้าน, ใบรับรองแพทย์, หลักฐานรายได้, หนังสือยินยอม |
| 11.5 ความรุนแรงในครอบครัว | ใคร? ทำอะไร? เมื่อไหร่? ไป รพ. หรือบ้านพักฉุกเฉิน? | บัตร ปชช., ใบรับรองแพทย์, รูปบาดแผล, บันทึกเหตุการณ์, พยาน |

### accident (3 sub-problems)
| Sub-Problem | Phase 1 AI Questions | Phase 5 Required Documents |
|-------------|---------------------|---------------------------|
| 12.1 ถูกชนแล้วหนี | ที่ไหน? เมื่อไหร่? จำทะเบียนได้ไหม? มีกล้อง? | บัตร ปชช., ใบแจ้งความ, รูปที่เกิดเหตุ, กล้องวงจรปิด, พยาน |
| 12.2 ชนแล้วคู่กรณีไม่ยอม | ใครผิด? มี พ.ร.บ.? แจ้งประกัน? เรียกค่าเสียหายเท่าไหร่? | บัตร ปชช., พ.ร.บ., ใบเคลม, รูป, บันทึกประจำวัน, ใบเสร็จค่าซ่อม |
| 12.3 เรียกค่าเสียหายจากอุบัติเหตุ | อุบัติเหตุอะไร? ความเสียหาย? ประกันจ่ายเท่าไหร่? | บัตร ปชช., ใบแจ้งความ, ใบรับรองแพทย์, ใบเสร็จค่าซ่อม/รักษา, พ.ร.บ. |

---

## D.3 Dashboard Question Flows

### ADMIN OVERVIEW (/admin)

| # | Admin Asks AI | AI Returns | Checklist |
|---|--------------|------------|-----------|
| 1 | "สรุปวันนี้" | Daily KPIs + alerts | [ ] All 6 stat cards populated<br>[ ] Alerts for anomalies<br>[ ] Real-time refresh |
| 2 | "เทรนด์ users 30 วัน" | User growth chart | [ ] 7/30/90 day toggle<br>[ ] Line chart renders<br>[ ] Tooltip on hover |
| 3 | "category ไหน active สุด?" | Category breakdown pie + bar | [ ] Pie chart renders<br>[ ] Top 5 labeled<br>[ ] Click to filter cases |
| 4 | "มีเคสเร่งด่วนกี่เคส?" | Urgent cases count + list | [ ] Red badge for urgent<br>[ ] Quick-action button per case |

### ADMIN USERS (/admin/users)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Search user | Filtered table | [ ] Search by name/email/phone<br>[ ] Debounced search<br>[ ] Clear search button |
| 2 | Filter by role/plan/status | Filtered table | [ ] Multi-filter AND logic<br>[ ] Reset filters<br>[ ] Active filter count badge |
| 3 | Click user row | User detail modal | [ ] Profile tab (info + edit)<br>[ ] Cases tab (user's cases)<br>[ ] Payments tab (transaction history)<br>[ ] Activity tab (audit log) |
| 4 | Ban user | Confirmation → ban | [ ] Confirm dialog with reason<br>[ ] User status updates<br>[ ] Email notification sent |

### ADMIN CASES (/admin/cases)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Filter cases | Filtered table | [ ] Category dropdown (12 options)<br>[ ] Status dropdown<br>[ ] Date range picker |
| 2 | Click case | Case detail view | [ ] Full timeline<br>[ ] Phases completed<br>[ ] AI analysis<br>[ ] Assign lawyer dropdown |
| 3 | Assign lawyer | Case updated with lawyer | [ ] Lawyer search/select<br>[ ] Notification sent to lawyer<br>[ ] Case status updates |
| 4 | Close/reopen case | Status transition | [ ] Validation (can't close without reason)<br>[ ] Audit log entry<br>[ ] User notified |

### ADMIN LAWYERS (/admin/lawyers)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | View pending | Pending verification list | [ ] Document viewer (license + ID)<br>[ ] Bar number validation<br>[ ] Profile completeness check |
| 2 | Approve lawyer | Lawyer status → verified | [ ] One-click approve<br>[ ] Welcome notification sent<br>[ ] Profile goes live |
| 3 | Reject lawyer | Lawyer status → rejected | [ ] Rejection reason required<br>[ ] Notification with reason<br>[ ] Lawyer can reapply |
| 4 | Suspend lawyer | Lawyer status → suspended | [ ] Reason required<br>[ ] Active cases reassigned<br>[ ] Account frozen |

### ADMIN REVENUE (/admin/revenue)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | View dashboard | Revenue stats + charts | [ ] MRR/ARR/Today/Month stats<br>[ ] Revenue over time chart<br>[ ] By plan pie chart |
| 2 | Filter transactions | Filtered table | [ ] Date range<br>[ ] Plan filter<br>[ ] Status filter<br>[ ] Export CSV |
| 3 | Issue refund | Refund processed | [ ] Confirm dialog<br>[ ] Omise refund API<br>[ ] User notified |

### ADMIN CONTENT (/admin/content)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Add/edit category | Category CRUD | [ ] Name, slug, icon, description<br>[ ] Sub-problem sub-form<br>[ ] Ordering (drag-drop) |
| 2 | Add/edit template | Template editor | [ ] Markdown editor<br>[ ] Preview panel<br>[ ] {{field}} validation<br>[ ] Category assignment |
| 3 | Add/edit FAQ | FAQ CRUD | [ ] Question + answer<br>[ ] Category<br>[ ] Ordering |
| 4 | Edit sources | Source registry | [ ] Law name + section<br>[ ] URL reference<br>[ ] Category mapping |

### ADMIN SETTINGS (/admin/settings)

| # | Admin Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Save settings | Settings persisted | [ ] All sections save independently<br>[ ] Validation per field<br>[ ] Audit log of changes |
| 2 | Test AI connection | Connection status | [ ] Ping DeepSeek<br>[ ] Return latency<br>[ ] Error if invalid key |
| 3 | Toggle maintenance | Maintenance mode | [ ] Custom message<br>[ ] All routes show maintenance page<br>[ ] Admin bypass |

---

## D.4 Lawyer App Question Flows

### LAWYER DASHBOARD (/lawyer)

| # | Lawyer Sees | Action | Checklist |
|---|------------|--------|-----------|
| 1 | Active cases count + list | Click to view case | [ ] Case count (active/closed/pending)<br>[ ] Recent activity feed<br>[ ] Revenue this month |
| 2 | Client messages | Click to reply | [ ] Unread count badge<br>[ ] Message preview<br>[ ] Quick reply |
| 3 | Upcoming deadlines | View calendar | [ ] Court dates<br>[ ] Document deadlines<br>[ ] Client meetings |

### LAWYER CASES (/lawyer/cases)

| # | Lawyer Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | View case list | Filtered by status | [ ] Status tabs (All/Active/Closed/Archived)<br>[ ] Search by client name/case ID<br>[ ] Sort by date/urgency |
| 2 | Click case | Case detail + timeline | [ ] Full case data<br>[ ] Client info<br>[ ] Document list<br>[ ] AI-generated summary<br>[ ] Add note/update status |
| 3 | Create case | New case form | [ ] Client selector (existing or new)<br>[ ] Category + sub-problem<br>[ ] Description + notes |

### LAWYER CLIENTS (/lawyer/clients)

| # | Lawyer Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | View client list | Filtered + searchable | [ ] Name + contact<br>[ ] Case count<br>[ ] Last activity<br>[ ] Click for detail |
| 2 | Client detail | Full client profile | [ ] Contact info<br>[ ] All cases<br>[ ] Communication history<br>[ ] Billing history |

### LAWYER BILLING (/lawyer/billing)

| # | Lawyer Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Create invoice | Invoice form | [ ] Client selector<br>[ ] Line items<br>[ ] Due date<br>[ ] Thai invoice format |
| 2 | View invoices | Table with status | [ ] Status: draft/sent/paid/overdue<br>[ ] Filter by status<br>[ ] Download PDF |
| 3 | Record payment | Invoice status → paid | [ ] Payment method<br>[ ] Date<br>[ ] Receipt auto-generated |

### LAWYER PROFILE (/lawyer/profile)

| # | Lawyer Action | System Returns | Checklist |
|---|-------------|---------------|-----------|
| 1 | Edit profile | Profile form | [ ] Basic info (name, bar#, specialization)<br>[ ] Photo upload<br>[ ] Bio + experience<br>[ ] Pricing |
| 2 | Submit verification | Verification documents | [ ] License photo upload<br>[ ] ID card upload<br>[ ] Submit for review<br>[ ] Status tracker |

---

# SECTION E: Master Checklist (Phases 1-6)

## PHASE 1: Foundation (Weeks 1-3)

### E1.1 Project Setup
- [ ] Initialize Next.js 15 project with TypeScript
- [ ] Configure Tailwind CSS 4 + shadcn/ui
- [ ] Set up folder structure per Section A.3
- [ ] Configure ESLint + Prettier
- [ ] Set up GitHub repo + CI/CD pipeline
- [ ] Configure environment variables (.env.local template)
- [ ] Set up Supabase project (dev + prod)
- [ ] Create `README.md` with setup instructions
- [ ] Configure Vercel deployment

### E1.2 Authentication
- [ ] Set up Supabase Auth (email/password)
- [ ] Implement login page (`/auth/login`)
- [ ] Implement register page (`/auth/register`)
- [ ] Implement forgot password flow
- [ ] Set up LINE Login integration
- [ ] Create auth middleware + route protection
- [ ] Implement role-based access control (RBAC)
- [ ] Create session management
- [ ] Implement 2FA (optional, admin-only)
- [ ] Write auth tests (unit + integration)

### E1.3 Database
- [ ] Design database schema (all tables)
- [ ] Create Supabase migrations
- [ ] Set up Row Level Security (RLS) policies
- [ ] Create typed database queries
- [ ] Set up Supabase Storage buckets
- [ ] Create seed data script
- [ ] Set up database backups
- [ ] Write database tests

### E1.4 AI Engine
- [ ] Set up DeepSeek API client
- [ ] Create AI prompt templates (all 6 types)
- [ ] Implement warm-tone calibration engine
- [ ] Build diagnosis AI pipeline
- [ ] Build search AI pipeline
- [ ] Build concierge AI pipeline
- [ ] Build document generation AI pipeline
- [ ] Build tax optimization AI pipeline
- [ ] Set up fallback model (Claude/Haiku)
- [ ] Implement rate limiting + token counting
- [ ] Write AI pipeline tests + prompt eval

### E1.5 Core Types & Config
- [ ] Define all TypeScript types (user, case, document, lawyer, payment, admin)
- [ ] Create legal category definitions (12 categories)
- [ ] Create diagnosis config (all 47 sub-problems)
- [ ] Create legal source registry
- [ ] Create payment package definitions
- [ ] Create site configuration
- [ ] Create navigation configuration
- [ ] Create feature flags

---

## PHASE 2: Core Pages (Weeks 3-6)

### E2.1 Consumer Home
- [ ] Build consumer layout shell (nav + sidebar)
- [ ] Build home page with AI input box
- [ ] Build feature action cards (6 cards)
- [ ] Build active cases widget
- [ ] Build social proof section
- [ ] Implement warm empathetic design throughout
- [ ] Mobile responsive (all breakpoints)
- [ ] Loading skeletons
- [ ] Error + empty states

### E2.2 Diagnosis Wizard
- [ ] Build 4-step diagnosis flow
- [ ] Step 1: multi-select problem type
- [ ] Step 2: dynamic category-specific questions
- [ ] Step 3: fear level calibration
- [ ] Step 4: confirm + launch concierge
- [ ] Implement progress stepper
- [ ] Wire to AI diagnosis pipeline
- [ ] Back/forward navigation with data persistence
- [ ] Mobile responsive
- [ ] Loading + error states

### E2.3 Concierge Flow (8 Phases)
- [ ] Build phase container with stepper
- [ ] Phase 1: Understand (narrative parsing + compound detection)
- [ ] Phase 2: Rights (laws, penalties, warnings, urgency)
- [ ] Phase 3: Path (A/B/C + monetization gate)
- [ ] Phase 3 Gate: Payment flow (฿299 Action Pack)
- [ ] Phase 4: Jurisdiction (court lookup + map)
- [ ] Phase 5: Documents (checklist + upload + progress)
- [ ] Phase 6: Prepare (AI document generation)
- [ ] Phase 7: File (step-by-step instructions)
- [ ] Phase 8: Follow-up (timeline + Case Plus ฿999)
- [ ] Implement compound case handling
- [ ] All 47 sub-problems tested end-to-end
- [ ] Lawyer 10-point checklist integration
- [ ] Mediation benefits box
- [ ] Court behavior + etiquette info boxes
- [ ] Perjury warnings
- [ ] Blue-shirt receptionist info
- [ ] Appeals/ฎีกา guidance

### E2.4 AI Search
- [ ] Build search page with input + results
- [ ] Implement AI search pipeline
- [ ] Build category chips (12 categories)
- [ ] Build search results cards
- [ ] Build related questions section
- [ ] Implement "Start Case" from search result
- [ ] Loading skeleton
- [ ] Empty state
- [ ] Error state
- [ ] Mobile responsive

### E2.5 Pricing
- [ ] Build pricing page
- [ ] Implement 4-tier pricing cards
- [ ] Feature comparison matrix
- [ ] FAQ accordion
- [ ] "Most Popular" badge
- [ ] Upgrade CTAs with Omise checkout
- [ ] Mobile responsive
- [ ] Current plan indicator

### E2.6 User Profile
- [ ] Build profile page
- [ ] Profile summary card
- [ ] User stats (cases, documents, savings)
- [ ] Active plan badge + upgrade CTA
- [ ] Case list tab
- [ ] Document list tab
- [ ] Payment history tab
- [ ] Settings tab (notifications, PDPA, data export, delete)
- [ ] AI consent toggle
- [ ] Mobile responsive

### E2.7 Marketing Pages
- [ ] Landing page (hero, features, how-it-works, testimonials, CTA)
- [ ] About page
- [ ] How It Works page
- [ ] Help Center / FAQ
- [ ] Terms of Service
- [ ] Privacy Policy (PDPA-compliant)
- [ ] Mobile responsive (all pages)

---

## PHASE 3: Business Features (Weeks 6-9)

### E3.1 Document Engine
- [ ] Build document library page
- [ ] Build document list with search/filter
- [ ] Build document detail view
- [ ] Build document editor
- [ ] Implement merge engine (`{{field}}` replacement)
- [ ] Create all document templates (20+ templates)
- [ ] Build document generation from case
- [ ] Implement export: PDF, DOCX, TXT
- [ ] Watermark tiering per package
- [ ] Evidence upload integration
- [ ] Mobile responsive

### E3.2 Tax Module
- [ ] Build tax calculator page
- [ ] Implement progressive tax calculator
- [ ] Build deduction chips (all 30+ deductions)
- [ ] Build bracket sidebar with progress
- [ ] Build savings tracker
- [ ] Implement AI tax optimizer
- [ ] Build 6-step filing checklist
- [ ] Tax report export
- [ ] Mobile responsive

### E3.3 Lawyer Marketplace
- [ ] Build lawyer listing page
- [ ] Implement filters (category, province, experience, price)
- [ ] Build lawyer card component
- [ ] Build lawyer detail/profile page
- [ ] Implement reviews + ratings
- [ ] Build hire flow (consultation + full-case)
- [ ] Implement verification badge
- [ ] Lawyer search + map view
- [ ] Mobile responsive

### E3.4 Payments
- [ ] Integrate Omise payment gateway
- [ ] Implement PromptPay QR code
- [ ] Build checkout flow
- [ ] Implement payment webhook handler
- [ ] Create invoice generation
- [ ] Payment history in profile
- [ ] Admin refund flow
- [ ] Payment failure handling + retry

### E3.5 Notifications
- [ ] Build notifications inbox
- [ ] Implement in-app notifications (Supabase real-time)
- [ ] Implement LINE notification integration
- [ ] Implement email notifications (Resend)
- [ ] Build notification bell with unread count
- [ ] Build notification preferences
- [ ] Implement case reminder scheduler (Case Plus)

---

## PHASE 4: Admin Dashboard (Weeks 9-11)

### E4.1 Admin Shell
- [ ] Build admin layout (sidebar + top bar)
- [ ] Implement admin auth + RBAC
- [ ] Admin navigation
- [ ] Admin breadcrumbs
- [ ] Mobile responsive

### E4.2 Admin Overview
- [ ] Build overview dashboard
- [ ] Stat cards (users, revenue, cases, lawyers, AI usage)
- [ ] Revenue over time chart
- [ ] Cases by category chart
- [ ] Recent activity feed
- [ ] Date range filter
- [ ] Loading skeletons
- [ ] Export dashboard

### E4.3 User Management
- [ ] Build user table (paginated, sortable, filterable)
- [ ] Implement search (name, email, phone)
- [ ] Build user detail modal (profile, cases, payments, activity)
- [ ] Ban/unban functionality
- [ ] Role change
- [ ] Plan management
- [ ] Bulk export (CSV)
- [ ] Audit log

### E4.4 Case Management
- [ ] Build case table (all cases)
- [ ] Filter by category, status, priority, date
- [ ] Build case detail view (full timeline, phases, AI analysis)
- [ ] Lawyer assignment
- [ ] Case status transitions
- [ ] Bulk actions (close, archive, assign)
- [ ] Export cases

### E4.5 Lawyer Verification
- [ ] Build pending/verified/rejected tabs
- [ ] Build verification detail modal
- [ ] Document viewer (license + ID images)
- [ ] Approve/reject with reason
- [ ] Request more info
- [ ] Suspend/ban lawyer
- [ ] Audit log

### E4.6 Revenue Dashboard
- [ ] Revenue summary stats (MRR, ARR, Today, Month)
- [ ] Revenue charts (time series, by plan, by method)
- [ ] Transaction table (filterable, exportable)
- [ ] Refund management
- [ ] Financial report generation
- [ ] Lawyer commission tracking

### E4.7 Content Management
- [ ] Category CRUD (12 categories + sub-problems)
- [ ] Template editor (markdown + preview)
- [ ] FAQ CRUD
- [ ] Source registry management
- [ ] AI prompt management (version history)
- [ ] Platform copy management

### E4.8 Platform Settings
- [ ] General settings
- [ ] AI configuration (model, keys, params)
- [ ] Payment gateway settings
- [ ] LINE integration settings
- [ ] Email settings
- [ ] Security settings
- [ ] Notification defaults
- [ ] Maintenance mode

---

## PHASE 5: Integration & Lawyer App (Weeks 11-14)

### E5.1 LINE Integration
- [ ] Set up LINE Messaging API channel
- [ ] Implement LINE Login
- [ ] Build LINE webhook handler
- [ ] Implement LINE notification templates
- [ ] Build LINE rich menu
- [ ] Case updates via LINE
- [ ] Lawyer chat via LINE (one-way notifications → in-app chat)
- [ ] LINE OA auto-reply with AI

### E5.2 Lawyer App
- [ ] Build lawyer layout shell
- [ ] Lawyer dashboard (active cases, clients, revenue, deadlines)
- [ ] Case management (CRUD + timeline + AI summary)
- [ ] Client portal (list, detail, communication)
- [ ] Billing & invoices (create, send, track)
- [ ] Document templates (lawyer-specific)
- [ ] Lawyer profile + verification flow
- [ ] Practice analytics
- [ ] Settings

### E5.3 Lawyer-Client Communication
- [ ] In-app messaging between lawyer and client
- [ ] Document sharing
- [ ] Case status updates visible to both
- [ ] Billing visibility for client
- [ ] Notification routing (in-app + email + LINE)

### E5.4 Mobile Optimization
- [ ] Full mobile responsive audit
- [ ] Touch-friendly interactions
- [ ] PWA setup (service worker, manifest)
- [ ] Offline support for critical pages
- [ ] Mobile payment flow optimization

### E5.5 Security Hardening
- [ ] CSP headers
- [ ] Rate limiting (API routes)
- [ ] Input sanitization
- [ ] File upload validation
- [ ] SQL injection prevention (Supabase RLS)
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] Security audit
- [ ] Penetration testing

---

## PHASE 6: Polish & Launch (Weeks 14-16)

### E6.1 Tone & Empathy
- [ ] Audit all UI text for warm tone consistency
- [ ] Ensure every AI response has empathetic opening
- [ ] Test with real users for emotional resonance
- [ ] Verify all legal warnings are prominent
- [ ] Verify all disclaimers are present
- [ ] Ensure "ชูใจ" brand voice is consistent everywhere

### E6.2 Accessibility
- [ ] WCAG 2.1 AA compliance audit
- [ ] Keyboard navigation (all pages)
- [ ] Screen reader testing
- [ ] Color contrast verification
- [ ] Focus indicators
- [ ] Alt text on all images
- [ ] Form labels + error messages
- [ ] Skip navigation links

### E6.3 Performance
- [ ] Lighthouse audit (all critical pages)
- [ ] Bundle size optimization
- [ ] Image optimization (next/image)
- [ ] Font loading optimization
- [ ] Code splitting
- [ ] Caching strategy
- [ ] CDN configuration
- [ ] First paint < 1.5s
- [ ] Time to Interactive < 3s

### E6.4 Testing
- [ ] Unit tests (all lib/ functions)
- [ ] Integration tests (API routes)
- [ ] E2E tests (critical user journeys)
- [ ] All 47 sub-problems tested end-to-end
- [ ] 12 categories tested with real questions
- [ ] Payment flow tested (sandbox)
- [ ] LINE integration tested
- [ ] Mobile tested (iOS + Android)
- [ ] Browser tested (Chrome, Safari, Firefox, Edge)

### E6.5 SEO & Analytics
- [ ] Meta tags (all pages)
- [ ] Open Graph images
- [ ] Sitemap generation
- [ ] Robots.txt
- [ ] Structured data (FAQ, HowTo, Organization)
- [ ] Plausible/PostHog analytics setup
- [ ] Conversion tracking
- [ ] Funnel analysis

### E6.6 Launch Preparation
- [ ] Production environment setup
- [ ] SSL certificates
- [ ] DNS configuration
- [ ] Database production scaling
- [ ] Monitoring + alerting (Sentry, Logflare)
- [ ] Backup strategy verification
- [ ] Load testing
- [ ] Launch checklist document
- [ ] Rollback plan
- [ ] Customer support setup (LINE, email)
- [ ] Launch announcement content
- [ ] Press kit

### E6.7 Post-Launch (Week 17+)
- [ ] Monitor error rates
- [ ] Monitor AI quality
- [ ] User feedback collection
- [ ] A/B testing framework
- [ ] Feature request triage
- [ ] Performance monitoring
- [ ] Weekly review + iteration
- [ ] Content updates (laws, templates)
- [ ] Community building (LINE group, Facebook)

---

## Appendix A: Database Schema (High-Level)

```
users
├── id: uuid (PK)
├── email: text (unique)
├── phone: text
├── full_name: text
├── avatar_url: text
├── role: enum('consumer', 'lawyer', 'admin')
├── plan: enum('free', 'action_pack', 'case_plus', 'sme_starter')
├── plan_expires_at: timestamptz
├── line_user_id: text
├── created_at: timestamptz
├── updated_at: timestamptz

lawyer_profiles
├── id: uuid (PK)
├── user_id: uuid (FK → users)
├── bar_number: text
├── license_image_url: text
├── id_card_image_url: text
├── specialization: text[]
├── years_of_practice: int
├── province: text
├── bio: text
├── consultation_fee: int
├── case_fee_range: int[]
├── verification_status: enum('pending', 'verified', 'rejected')
├── rejection_reason: text
├── average_rating: float
├── review_count: int
├── is_active: boolean

cases
├── id: uuid (PK)
├── case_number: text (generated)
├── user_id: uuid (FK → users)
├── assigned_lawyer_id: uuid (FK → lawyer_profiles, nullable)
├── category: text (12 legal categories)
├── sub_problem: text
├── status: enum('active', 'pending', 'closed', 'archived')
├── priority: enum('low', 'medium', 'high', 'urgent')
├── current_phase: int (1-8)
├── narrative: text
├── ai_analysis: jsonb
├── compound_categories: text[]
├── jurisdiction: jsonb
├── timeline: jsonb
├── created_at: timestamptz
├── updated_at: timestamptz
├── closed_at: timestamptz

case_phases
├── id: uuid (PK)
├── case_id: uuid (FK → cases)
├── phase_number: int (1-8)
├── status: enum('not_started', 'in_progress', 'completed')
├── data: jsonb
├── completed_at: timestamptz
├── created_at: timestamptz

documents
├── id: uuid (PK)
├── user_id: uuid (FK → users)
├── case_id: uuid (FK → cases, nullable)
├── title: text
├── type: text
├── template_id: text
├── content: text (markdown)
├── status: enum('draft', 'completed', 'archived')
├── watermarked: boolean
├── created_at: timestamptz
├── updated_at: timestamptz

evidence
├── id: uuid (PK)
├── case_id: uuid (FK → cases)
├── document_checklist_id: text
├── file_url: text
├── file_type: text
├── uploaded_at: timestamptz

payments
├── id: uuid (PK)
├── user_id: uuid (FK → users)
├── case_id: uuid (FK → cases, nullable)
├── amount: int (satang)
├── currency: text ('THB')
├── plan_purchased: text
├── status: enum('pending', 'paid', 'failed', 'refunded')
├── method: text ('promptpay', 'credit_card')
├── omise_charge_id: text
├── created_at: timestamptz

notifications
├── id: uuid (PK)
├── user_id: uuid (FK → users)
├── type: text
├── title: text
├── body: text
├── data: jsonb
├── is_read: boolean
├── channel: enum('in_app', 'email', 'line')
├── created_at: timestamptz

lawyer_reviews
├── id: uuid (PK)
├── lawyer_id: uuid (FK → lawyer_profiles)
├── user_id: uuid (FK → users)
├── rating: int (1-5)
├── comment: text
├── case_id: uuid (FK → cases)
├── created_at: timestamptz

legal_sources
├── id: uuid (PK)
├── category: text
├── law_name: text
├── section: text
├── description: text
├── penalty: text
├── url: text
├── is_active: boolean

templates
├── id: uuid (PK)
├── name: text
├── type: text
├── category: text
├── content: text (markdown)
├── variables: jsonb
├── is_active: boolean
├── usage_count: int
├── created_at: timestamptz
├── updated_at: timestamptz

faqs
├── id: uuid (PK)
├── category: text
├── question: text
├── answer: text
├── order: int
├── is_active: boolean

platform_settings
├── id: uuid (PK)
├── key: text (unique)
├── value: jsonb
├── updated_by: uuid (FK → users)
├── updated_at: timestamptz

audit_logs
├── id: uuid (PK)
├── user_id: uuid (FK → users)
├── action: text
├── entity_type: text
├── entity_id: uuid
├── changes: jsonb
├── ip_address: text
├── created_at: timestamptz
```

---

## Appendix B: AI Prompt Architecture

### B.1 System Prompt (Base)
```
You are "ชูใจ" (Chujai), a warm, empathetic Thai legal AI assistant.
Your purpose: help Thai citizens understand their legal rights and take action.

TONE RULES:
- Always start with empathy: "เราเข้าใจความรู้สึกของคุณนะ"
- Use simple, everyday Thai — a high school student should understand
- Never use intimidating legal jargon without explanation
- Be encouraging but honest — never promise outcomes
- Use "เรา" (we) and "คุณ" (you) — friendly, not formal
- Add "ค่ะ" (female) or "ครับ" (male) based on user preference
- Never sound like a robot or a law textbook

SAFETY RULES:
- NEVER give legal advice — only legal information
- NEVER predict case outcomes (% chance to win)
- NEVER recommend specific lawyers (show data, don't rank)
- NEVER file documents on behalf of users
- NEVER fabricate legal citations — validate against source registry
- ALWAYS include disclaimer on generated documents
- ALWAYS warn about perjury (ป.อาญา ม.177) when relevant
```

### B.2 Fear Calibration (injected per user)
```
USER'S EMOTIONAL STATE: {fear_level}
- Panic → Ultra-gentle, reassurance first, emergency actions highlighted
- Urgent → Empathetic but action-focused, clear next steps
- Concerned → Informative, empowering, all options laid out
- Planning → Professional, efficient, comprehensive
```

### B.3 Compound Case Template
```
DETECTED ISSUES: {compound_categories}
- PRIMARY: {primary_category} (process first)
- SECONDARY: {secondary_categories} (process after primary)
- DEPENDENCY: {dependency_chain} (e.g., "police report needed before insurance claim")
```

### B.4 Monetization Gate Prompt
```
CURRENT STATE:
- User has completed Phases 1-3 (understand, rights, path)
- User knows: what laws apply, what to do, which path to take
- User DOES NOT know: which court, what documents, how to file

GATE MESSAGE:
- Remind user they have FREE information: laws, rights, path chosen
- Ask the curiosity question: "But... which court? What documents?"
- Price anchor: "Lawyers charge ฿10,000-30,000"
- Offer: "Action Pack — ฿299 (98% cheaper than a lawyer)"
- Free trial: "Try 1 document free first"
```

---

## Appendix C: Package Tier Definitions

| Feature | 🆓 Free | ⚡ Action Pack (฿299) | ⭐ Case Plus (฿999) | 🏢 SME Starter (฿2,990/mo) |
|---------|:---:|:---:|:---:|:---:|
| AI Diagnosis | 3/month | Unlimited | Unlimited | Unlimited |
| AI Legal Search | ✓ | ✓ | ✓ | ✓ |
| Documents Generated | 1 | Unlimited | Unlimited | Unlimited |
| Evidence Upload | ✗ | ✓ | ✓ | ✓ |
| Court Step-by-Step | ✗ | ✓ | ✓ | ✓ |
| Case Timeline | ✗ | ✗ | ✓ | ✓ |
| Auto Reminders | ✗ | ✗ | ✓ | ✓ |
| LINE Notifications | ✗ | ✗ | ✓ | ✓ |
| Lawyer Consultation | ✗ | ✗ | 3 sessions | 10 sessions/mo |
| Business Documents | ✗ | ✗ | ✗ | ✓ |
| Team Access | ✗ | ✗ | ✗ | 5 users |
| Tax Optimizer (Basic) | ✓ | ✓ | ✓ | ✓ |
| Tax Optimizer (Advanced) | ✗ | ✓ | ✓ | ✓ |
| Corporate Tax | ✗ | ✗ | ✗ | ✓ |
| API Access | ✗ | ✗ | ✗ | ✓ |
| Priority Support | ✗ | ✗ | ✓ | ✓ |
| Watermark on Exports | ✓ | ✗ (clean) | ✗ (clean) | ✗ (clean) |

---

## Appendix D: Key Metrics & KPIs

### Platform Health
| Metric | Target | Measurement |
|--------|--------|-------------|
| Monthly Active Users (MAU) | 5,000+ | Unique users with ≥1 action/month |
| Case Completion Rate | 60%+ | Cases reaching Phase 7 or 8 |
| AI Diagnosis Accuracy | 90%+ | Category correctly identified |
| User Satisfaction (NPS) | 50+ | In-app survey after case resolution |
| Page Load Time | <2s | Lighthouse performance score 90+ |
| Uptime | 99.9% | Vercel + Supabase monitoring |

### Revenue
| Metric | Target | Measurement |
|--------|--------|-------------|
| Free → Action Pack Conversion | 15-25% | Users who hit monetization gate |
| Action Pack → Case Plus Upgrade | 10-15% | Users upgrading within case |
| MRR | ฿500K+ by Month 6 | Sum of recurring + one-time ÷ avg |
| Customer Acquisition Cost (CAC) | <฿150 | Marketing spend ÷ new paying users |
| Lifetime Value (LTV) | ฿800+ | Average revenue per paying user |
| Churn Rate | <5%/month | Users canceling or going inactive |

---

*End of Chujai Legal Master Design Document — version 1.0*


---

# SECTION F: Design System & Brand (ชูใจ Identity)

## F.1 Brand Philosophy

"ชูใจ" (Chujai) translates to "uplift the heart" / "comfort the heart". The entire platform must embody this.

### Brand Pillars
| Pillar | Meaning | Design Expression |
|--------|---------|-------------------|
| 🫶 **Empathy** | We feel what the user feels | Warm copy, emotional validation, "เราเข้าใจคุณ" |
| 💪 **Empowerment** | We make users feel capable | Action-first language, "คุณทำได้", progress bars |
| 🛡️ **Trust** | We are legally reliable | Verified badges, source citations, disclaimers |
| 🌸 **Warmth** | Comfort in a scary space | Soft colors, rounded corners, gentle animations |
| 🎯 **Clarity** | No confusing legal jargon | Plain Thai, step-by-step, visual timelines |

## F.2 Color Palette

### Primary — Warm & Trusting
```
🌸 Blush Pink (Primary)      #FF7A9E  →  used for primary buttons, highlights
💗 Deep Rose (Hover)          #E85D82  →  button hover, active states
🌷 Soft Pink (Background)     #FFF0F5  →  card backgrounds, highlights
❤️ Heart Red (Accent)         #E85D82  →  urgent warnings, critical badges
```

### Secondary — Calm & Legal
```
🏛️ Deep Navy (Trust)          #1E3A5F  →  headings, navigation, legal text
🔵 Sky Blue (Info)            #4A90D9  →  information boxes, links
🌊 Soft Blue (Info BG)        #E8F1FB  →  info box backgrounds
```

### Status — Semantic
```
🟢 Success Green             #34C759  →  completed, verified, paid
🟡 Warning Amber             #FFB020  →  pending, in-progress, review
🔴 Danger Red                #E5484D  →  urgent, rejected, banned
⚪ Neutral Gray              #8A8F98  →  disabled, secondary text
```

### Neutral Scale
```
50:  #FAFAFA   (page background)
100: #F5F5F5   (card background)
200: #E8E8E8   (borders)
300: #D4D4D4   (disabled borders)
400: #A3A3A3   (placeholder text)
500: #737373   (secondary text)
600: #525252   (body text)
700: #404040   (emphasis text)
800: #262626   (headings)
900: #171717   (dark headings)
```

### Fear-Level Color Mapping (Fear Calibration)
| Fear Level | Tone | Accent Color | Urgency Badge |
|-----------|------|-------------|---------------|
| 😱 Panic | Ultra-gentle, reassurance-first | 🔴 Red | "ด่วนที่สุด — ทำทันที" |
| 😰 Urgent | Empathetic, action-focused | 🟠 Orange | "เร่งด่วน" |
| 😟 Concerned | Informative, empowering | 🟡 Amber | "ควรจัดการเร็วๆ" |
| 😌 Planning | Professional, efficient | 🔵 Blue | "วางแผนได้เลย" |

## F.3 Typography

### Font Stack
```
Thai:  'Noto Sans Thai', 'Sarabun', 'Prompt', sans-serif
Latin: 'Inter', -apple-system, sans-serif
Display: 'Prompt' (bold, headings)
Body: 'Noto Sans Thai' (regular 16px, line-height 1.7)
```

### Type Scale
```
Display XL: 36px / 48px  → Hero, landing
Display L:  28px / 36px  → Page titles
Heading 1:  24px / 32px  → Section titles
Heading 2:  20px / 28px  → Card titles
Heading 3:  18px / 24px  → Sub-section titles
Body L:     18px / 28px  → Lead paragraphs (emphasis)
Body:       16px / 24px  → Default body text
Body S:     14px / 20px  → Secondary, captions
Caption:    12px / 16px  → Labels, badges, meta
```

### Thai Typography Rules
- Minimum font size 14px for body (16px recommended — Thai needs larger glyphs)
- Line height minimum 1.6 for body text (Thai diacritics + tone marks need space)
- Do NOT use `letter-spacing` on Thai text (breaks tone marks)
- Use `word-break: break-word` for long legal terms
- Numbers in legal context: use Buddhist Era (พ.ศ.) with CE in parentheses

## F.4 Design Components

### Button Hierarchy
```
PRIMARY:   Solid blush pink (#FF7A9E), white text, rounded-lg (12px), shadow-sm
           hover: #E85D82, active: scale(0.98)
           Text: "เริ่มเลย", "วิเคราะห์", "ดำเนินการต่อ"

SECONDARY: Outline navy (#1E3A5F), transparent bg, rounded-lg
           Text: "ย้อนกลับ", "ดูรายละเอียด", "ภายหลัง"

GHOST:     Transparent, navy text, hover: soft pink bg
           Text: "ข้าม", "ไม่แน่ใจ"

DANGER:    Solid red (#E5484D), white text
           Text: "ลบบัญชี", "ยกเลิกเคส"

UPGRADE:   Gradient (pink → rose), white text, shadow-lg
           Text: "อัปเกรด — ฿299"
```

### Card Styles
```
BASE:      bg-white, rounded-2xl (16px), border (#E8E8E8), shadow-sm
HOVER:     shadow-md, translate-y(-2px), transition 200ms
URGENT:    border-red-200, bg-red-50, red accent left border
FREE:      soft pink bg (#FFF0F5), pink left border
LOCKED:    gray bg, lock icon, "🔒 อัปเกรดเพื่อปลดล็อก"
```

### Input Styles
```
BASE:      rounded-lg, border (#D4D4D4), focus: border-pink + ring-2 ring-pink-200
ERROR:     border-red-400, red helper text
SUCCESS:   border-green-400, check icon
DISABLED:  bg-gray-100, cursor-not-allowed
```

### Progress Indicators
```
STEPPER:   numbered circles, completed = filled pink with check,
           current = pink ring, upcoming = gray
PROGRESS:  rounded-full bar, gradient fill (pink → rose),
           percentage label with "●●●○○○○○○○ 30%"
```

### Emoji Usage (Warm Tone)
| Context | Emoji | Purpose |
|---------|-------|---------|
| Empathy opening | 😔 🫶 | Acknowledge pain |
| Encouragement | 💪 ✨ | Empower action |
| Good news | 🎉 ✅ | Celebrate progress |
| Warning | ⚠️ 🚨 | Safety-critical |
| Info | 📚 💡 | Knowledge sharing |
| Money | 💰 💸 | Financial context |
| Court/Legal | ⚖️ 🏛️ | Authority |
| Documents | 📄 📋 | Paperwork |
| Lawyer | 👨⚖️ | Professional help |

## F.5 Warm Language Guide (Tone Rules)

### Opening Phrases (Empathy)
```
"เราเข้าใจความรู้สึกของคุณนะ"
"เรื่องแบบนี้มันเครียดจริงๆ"
"ไม่เป็นไรนะ เราอยู่ตรงนี้เพื่อช่วยคุณ"
"ขอบคุณที่ไว้ใจเล่าเรื่องนี้ให้เราฟัง"
"คุณไม่ได้อยู่คนเดียวนะ"
```

### Reassurance (After fear)
```
"ข่าวดี — เรื่องนี้แก้ได้!"
"กฎหมายอยู่ข้างคุณ"
"คุณมีสิทธิเต็มที่ตามกฎหมาย"
"คนส่วนใหญ่จัดการเองได้ เราจะช่วยคุณทีละขั้น"
```

### Empowerment (Action)
```
"คุณทำได้!"
"เริ่มจากขั้นแรกง่ายๆ ก่อน"
"เราเคยช่วยคนที่เจอแบบนี้มาแล้วหลายเคส"
"ไม่ต้องทำทุกอย่างวันเดียว ค่อยๆ ทำทีละขั้น"
```

### Legal Information (Clarity)
```
"แปลเป็นภาษาง่ายๆ คือ..."
"กฎหมายข้อนี้แปลว่า..."
"พูดง่ายๆ คือคุณมีสิทธิที่จะ..."
"ถ้าเทียบกับชีวิตจริง มันเหมือนกับ..."
```

### NEVER Use
```
❌ Formal legal Thai: "ตามประมวลกฎหมายอาญา มาตรา 341 วรรคสอง"
✅ Plain: "กฎหมายอาญา ข้อ 341 บอกว่า การหลอกเอาทรัพย์คนอื่น ผิดกฎหมาย"
❌ Intimidating: "คุณต้องยื่นคำร้องต่อศาลภายในกำหนด"
✅ Warm: "คุณสามารถยื่นเอกสารได้เอง ใช้เวลาแค่ 30 นาที"
❌ Promising: "คุณจะชนะแน่นอน 100%"
✅ Honest: "จากข้อมูลที่คุณเล่า คุณมีหลักฐานครบ เรื่องนี้มีแนวโน้มดี"
```

## F.6 Accessibility Standards

### WCAG 2.1 AA Checklist
- [ ] Color contrast ≥ 4.5:1 for body, ≥ 3:1 for large text
- [ ] All interactive elements have visible focus indicators
- [ ] Keyboard navigation: Tab → logical order, Enter/Space for actions
- [ ] All images have descriptive alt text
- [ ] Forms have associated labels + error messages
- [ ] Skip-to-content link on all pages
- [ ] No color-only meaning (pair with icons/text)
- [ ] Screen reader: ARIA roles, live regions for dynamic content
- [ ] Reduced motion support (prefers-reduced-motion)
- [ ] Font size can scale to 200% without breaking layout

---

# SECTION G: API Reference

## G.1 Authentication Endpoints

### POST /api/auth/register
```
Request:
{
  "email": "user@email.com",
  "password": "********",
  "full_name": "สมชาย ใจดี",
  "phone": "0812345678"
}
Response 201:
{
  "user": { "id": "uuid", "email": "...", "full_name": "...", "role": "consumer" },
  "session": "..."
}
Errors: 409 (email exists), 400 (validation), 422 (weak password)
```

### POST /api/auth/login
```
Request: { "email": "...", "password": "..." }
Response 200: { "user": {...}, "session": "..." }
Errors: 401 (invalid credentials), 423 (banned account)
```

### GET /api/auth/line
```
Description: Initiate LINE Login
Response 302: Redirects to LINE authorization URL
```

### GET /api/auth/callback
```
Description: LINE Login callback
Query: code, state
Response 302: Redirect to / with session set
```

## G.2 AI Endpoints

### POST /api/ai/diagnose
```
Request:
{
  "narrative": "สั่งของใน Shopee แล้วไม่ส่ง",
  "answers": { "platform": "Shopee", "amount": 3500 },
  "fear_level": "urgent"
}
Response 200:
{
  "categories": ["online_fraud"],
  "sub_problem": "1.1 ซื้อของออนไลน์ไม่ได้ของ",
  "compound": false,
  "laws": ["ป.อาญา ม.341", "พ.ร.บ.คอมพิวเตอร์ ม.14(1)"],
  "urgency": "high",
  "drive_profile": { "safety": 0.9, "justice": 0.8 },
  "next_steps": [...]
}
```

### POST /api/ai/search
```
Request: { "query": "ดอกเบี้ยบัตรเครดิตสูงสุดกี่ %" }
Response 200:
{
  "answer": "...",
  "laws": [{ "name": "พ.ร.บ.ห้ามเรียกดอกเบี้ยเกินอัตรา", "section": "ม.1", "penalty": "..." }],
  "sources": [{ "url": "...", "title": "..." }],
  "related_questions": [...]
}
```

### POST /api/ai/generate
```
Request:
{
  "case_id": "uuid",
  "template_id": "police-report",
  "fields": { "victim_name": "...", "amount": 3500 }
}
Response 200:
{
  "document": { "id": "uuid", "content": "...", "status": "draft" },
  "missing_fields": ["account_number"]
}
```

### POST /api/ai/assistant
```
Request: { "case_id": "uuid", "message": "ต้องไปศาลไหน?" }
Response 200: { "reply": "...", "context": {...} }
```

## G.3 Case Endpoints

### GET /api/cases
```
Query: status, category, page, limit
Response 200: { "cases": [...], "total": 1203, "page": 1 }
```

### POST /api/cases
```
Request: { "category": "online_fraud", "sub_problem": "...", "narrative": "..." }
Response 201: { "case": { "id": "...", "case_number": "LA-2026-0892", ... } }
```

### GET /api/cases/[caseId]
```
Response 200: { "case": {...}, "phases": [...], "documents": [...], "timeline": [...] }
```

### PATCH /api/cases/[caseId]
```
Request: { "status": "closed", "priority": "high", "assigned_lawyer_id": "uuid" }
Response 200: { "case": {...} }
```

## G.4 Document Endpoints

### POST /api/documents/generate
```
Request: { "case_id": "uuid", "template_id": "...", "fields": {...} }
Response 201: { "document": {...} }
```

### GET /api/documents/[docId]
```
Response 200: { "document": {...} }
```

### POST /api/documents/[docId]/export
```
Request: { "format": "pdf" | "docx" | "txt" }
Response 200: { "url": "signed-download-url" }
```

## G.5 Lawyer Endpoints

### GET /api/lawyers
```
Query: category, province, min_experience, max_price, sort, page
Response 200: { "lawyers": [...], "total": 47 }
```

### GET /api/lawyers/[lawyerId]
```
Response 200: { "lawyer": {...}, "reviews": [...], "cases": [...] }
```

### POST /api/lawyers/[lawyerId]/reviews
```
Request: { "case_id": "uuid", "rating": 5, "comment": "..." }
Response 201: { "review": {...} }
```

## G.6 Payment Endpoints

### POST /api/payments/create
```
Request: { "plan": "action_pack", "case_id": "uuid" }
Response 201: { "payment": {...}, "checkout": { "url": "...", "qr_code": "..." } }
```

### POST /api/payments/webhook
```
Description: Omise webhook for payment status
Request: { "charge_id": "...", "status": "successful", ... }
Response 200: { "ok": true }
```

### POST /api/payments/verify
```
Request: { "payment_id": "uuid" }
Response 200: { "status": "paid" | "pending" | "failed" }
```

## G.7 Tax Endpoints

### POST /api/tax/calculate
```
Request: { "income": 600000, "deductions": { "personal": 60000, "rmf": 50000 } }
Response 200: { "tax": 7500, "bracket": "5%", "effective_rate": 1.25, "breakdown": [...] }
```

### POST /api/tax/optimize
```
Request: { "income": 600000, "deductions": {...} }
Response 200: { "suggestions": [...], "potential_savings": 5500, "optimized_tax": 2000 }
```

## G.8 Admin Endpoints (admin role required)

### GET /api/admin/users
```
Query: role, plan, status, search, page
Response 200: { "users": [...], "total": 8421 }
```

### PATCH /api/admin/users/[userId]
```
Request: { "role": "lawyer", "plan": "action_pack", "status": "banned" }
Response 200: { "user": {...} }
```

### GET /api/admin/revenue
```
Query: start_date, end_date
Response 200: { "mrr": 89000, "arr": 1070000, "transactions": [...] }
```

### POST /api/admin/lawyers/[lawyerId]/verify
```
Request: { "action": "approve" | "reject", "reason": "..." }
Response 200: { "lawyer": {...} }
```

## G.9 Error Response Format
```
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "อธิบายข้อผิดพลาดเป็นภาษาไทย",
    "details": { "field": "reason" }
  }
}
```

### Standard Error Codes
| Code | HTTP | Meaning |
|------|------|---------|
| INVALID_INPUT | 400 | Validation failed |
| UNAUTHORIZED | 401 | Not logged in |
| FORBIDDEN | 403 | Insufficient role |
| NOT_FOUND | 404 | Resource missing |
| RATE_LIMITED | 429 | Too many requests |
| AI_ERROR | 502 | AI upstream failure |
| PAYMENT_FAILED | 402 | Payment processing error |

---

# SECTION H: Detailed Per-Page Flow Specifications

## H.1 Consumer Home — Full Flow

### State 1: First Visit (No Cases)
```
RENDER: Empty active-cases widget → show "ยังไม่มีเคส — เริ่มเลย!" CTA
AI: No AI call on initial render (avoid latency)
CHECKLIST:
[ ] Warm greeting with user name
[ ] AI input box prominent (60% viewport width on desktop)
[ ] 6 feature cards in grid (2 cols mobile, 3 cols desktop)
[ ] Social proof section at bottom
[ ] Empty case state with strong CTA
```

### State 2: Has Active Cases
```
RENDER: Active cases list (sorted by last_updated desc)
EACH CASE CARD: case number, title, category icon, phase (e.g., "Phase 3/8"),
  last updated relative time, status badge, "ทำต่อ" button
CHECKLIST:
[ ] Cases sorted correctly
[ ] Phase progress shown
[ ] Status badge color correct (active=amber, closed=green, urgent=red)
[ ] "ทำต่อ" navigates to /concierge/[caseId]
```

### State 3: Multiple Cases
```
RENDER: Show up to 3 most recent, "+N more" link to /profile/cases
CHECKLIST:
[ ] Cap at 3 with "ดูทั้งหมด" link
[ ] Link navigates correctly
```

## H.2 Concierge Phase 1 — Full Flow (Understand)

### Input Processing Pipeline
```
1. User types narrative (free text, up to 2000 chars)
2. Debounce 500ms → live "กำลังอ่าน..." indicator
3. Submit → call /api/ai/diagnose
4. AI returns: categories, sub_problem, compound flag, laws, missing info
5. Render summary card + missing info inputs
```

### Missing Info Detection
```
AI scans for required fields per sub-problem:
- online_fraud: platform, amount, date, seller/buyer name
- crime: person, location, date, injury details
- labour: employer, position, salary, tenure, reason
- family: spouse, children, assets, reason
- property: land location, parties, deed status

RENDER: Inline input fields for each missing item
CHECKLIST:
[ ] Missing fields auto-detected
[ ] Inline inputs with Thai labels
[ ] Fields validate (currency, date, phone)
[ ] "Skip for now" option (fields not mandatory to proceed)
```

### Compound Case Detection
```
AI returns compound flag if multiple categories detected:
{ "compound": true, "categories": ["crime", "insurance"], "dependency": "police_report" }

RENDER: "พบ 2 ประเด็นที่ต้องจัดการ" banner + process order
CHECKLIST:
[ ] Compound banner renders
[ ] Process order shown (primary first)
[ ] Dependency explained ("ต้องแจ้งความก่อนจึงจะเคลมประกันได้")
```

## H.3 Concierge Phase 3 — Monetization Gate (Full Flow)

### Gate Rendering
```
After user selects path (A/B/C), render gate card:

┌─────────────────────────────────────────┐
│ 🆓 ถึงตรงนี้คุณรู้แล้วว่า:                │
│ ✅ รู้ว่าฟ้องอะไรได้ — ข้อหาและโทษ        │
│ ✅ รู้สิทธิของคุณ — ครบทุกด้าน           │
│ ✅ เลือกแนวทางแล้ว                       │
│ ══════════════════════════════          │
│ 🤔 แต่... ต้องไปศาลไหน?                  │
│      ต้องใช้เอกสารอะไร?                   │
│      ต้องเขียนคำฟ้องยังไง?                │
│      เดินเข้าไปในศาลแล้วต้องพูดอะไร?       │
│ 💡 แค่ ฿299 — เราบอกคุณทุกขั้นตอนจนจบ     │
│    (ถูกกว่าจ้างทนาย 98%)                 │
│ [📦 Action Pack — ฿299]  [เริ่มเลย]      │
│ 🎁 ยังไม่แน่ใจ? ทดลอง 1 เอกสารฟรีก่อน     │
└─────────────────────────────────────────┘

CHECKLIST:
[ ] Free summary shown (laws, rights, path)
[ ] Curiosity questions ("ต้องไปศาลไหน?")
[ ] Price anchor (lawyer ฿10,000-30,000 vs ฿299)
[ ] "98% cheaper" framing
[ ] CTA button opens payment
[ ] Free trial link (1 document) visible
[ ] Skip link for users who want to stay free
```

### Payment Flow
```
1. Click "เริ่มเลย — ฿299"
2. Open checkout modal (Omise)
3. Select: PromptPay QR or Credit Card
4. Confirm payment
5. Webhook confirms → unlock Phases 4-7
6. Show "ปลดล็อกแล้ว!" celebration
CHECKLIST:
[ ] Checkout modal opens
[ ] PromptPay QR generates
[ ] Credit card form validates
[ ] Payment success → phases unlock instantly
[ ] Payment failure → retry with error message
[ ] Receipt generated
```

## H.4 Concierge Phase 4 — Jurisdiction (Full Flow)

### Court Lookup
```
1. User selects province + district (dropdown, 77 provinces, 928 districts)
2. Call jurisdiction lookup (local data, not AI)
3. Return: court name, address, phone, map
CHECKLIST:
[ ] All 77 provinces in dropdown
[ ] Districts filtered by province
[ ] Correct court for district
[ ] Map embed (Google Maps)
[ ] Court phone + address
[ ] Online filing alternative shown
[ ] "แจ้งออนไลน์" vs "ไปสถานี" toggle
```

### Court Taxonomy Box
```
RENDER (info box):
🏛️ ศาลไทย — โครงสร้างที่ควรรู้
1️⃣ ศาลทั่วไป: ศาลจังหวัด (ฟ้องทุกประเภท), ศาลแขวง (คดีเล็ก)
2️⃣ ศาลชำนัญพิเศษ: ศาลแรงงาน, ศาลเยาวชน, ศาลผู้บริโภค,
   ศาลภาษีอากร, ศาลล้มละลาย, ศาลทรัพย์สินทางปัญญา
CHECKLIST: [ ] Rendered for all cases [ ] Expandable accordion
```

### Blue-Shirt Receptionist Box
```
RENDER (info box):
🔵 พนักงานต้อนรับประจำศาล (เสื้อฟ้า)
✓ บอกว่าต้องติดต่อเคาน์เตอร์ไหน ชั้นไหน
✓ แนะนำการเขียนคำร้อง คำขอ ประกันตัว
✓ บริการฟรี — "บริการด้วยรอยยิ้ม จากใจศาล"
CHECKLIST: [ ] Rendered [ ] Encouraging tone
```

## H.5 Concierge Phase 5 — Documents (Full Flow)

### Checklist Rendering
```
RENDER: Category-specific document checklist
EACH ITEM: checkbox, document name, "วิธีหา" (how to get) expandable
PROGRESS: "●●●○○○○○○○ 30% (2/7 มี)"
MISSING: Highlighted list "ยังขาด: สลิป, แคปโปรไฟล์, Statement"

CHECKLIST:
[ ] Checklist matches category (see Section D.2)
[ ] Each item has "how to get" instructions
[ ] Progress bar updates as user checks items
[ ] Upload button per item
[ ] Missing items visually distinct (red/amber)
[ ] Upload accepts: JPG, PNG, PDF (max 10MB each)
```

### Evidence Upload
```
FILE TYPES: JPG, PNG, PDF
MAX SIZE: 10MB per file, 20 files per case
STORAGE: Supabase Storage (private bucket)
CHECKLIST:
[ ] Drag-and-drop upload
[ ] Image preview
[ ] PDF preview
[ ] Progress indicator per file
[ ] Error handling (wrong type, too large)
[ ] Delete uploaded file
```

## H.6 Concierge Phase 6 — Prepare (Full Flow)

### Document Generation
```
PROCESS:
1. User clicks "สร้างเอกสาร"
2. Show loading animation ("AI กำลังสร้างเอกสารให้คุณ...")
3. AI generates documents (call /api/ai/generate)
4. Render generated documents list
5. AI returns "missing evidence" warnings
CHECKLIST:
[ ] Loading animation (document names streaming in)
[ ] Each document with checkmark
[ ] Missing evidence warnings
[ ] Download all button
[ ] Individual download buttons
[ ] "Upload more evidence" button
[ ] Re-generate button
```

### Generated Documents (by category)
```
online_fraud: บันทึกแจ้งความ, คำร้องขออายัดบัญชี, คำร้องขอเปิดเผยข้อมูล, จดหมายทวงถาม
crime: บันทึกแจ้งความ, คำร้องขอหมายจับ (ถ้าเหมาะสม), คำร้องขอความคุ้มครอง
defamation: บันทึกแจ้งความ, คำร้องขอให้ลบข้อมูล, หนังสือถึงแพลตฟอร์ม
insurance: หนังสือร้องเรียน คปภ., หนังสือบอกเลิกสัญญา, คำฟ้องเรียกค่าเสียหาย
government: คำร้องขอเอกสาร, หนังสือร้องเรียน, ฟ้องคดีปกครอง
property: หนังสือบอกกล่าว, คำร้องขอรังวัด, ฟ้องขับไล่, คำร้องขอออกโฉนดแทน
labour: หนังสือถึงนายจ้าง, คำร้องต่อพนักงานตรวจแรงงาน, ฟ้องคดีแรงงาน
consumer: หนังสือถึงผู้ขาย, ร้องเรียน สคบ., ฟ้องคดีผู้บริโภค
debt: หนังสือประนอมหนี้, คำร้องขอเจรจา, หนังสือถึงเจ้าหนี้
housing: หนังสือบอกเลิกสัญญาเช่า, หนังสือทวงมัดจำ, ร้องเรียน
family: ฟ้องหย่า, คำร้องแบ่งสินสมรส, คำร้องค่าเลี้ยงดู, คำร้องรับบุตรบุญธรรม
accident: หนังสือเรียกค่าเสียหาย, คำฟ้องคดีแพ่ง, หนังสือถึงประกัน
CHECKLIST: [ ] Correct documents per category [ ] All merge fields filled
```

## H.7 Concierge Phase 7 — File (Full Flow)

### Step-by-Step Rendering
```
EACH STEP: numbered, title, details card with:
- WHERE: exact location/URL
- HOW: instructions
- WHO: who to contact
- DOCUMENTS: what to bring
- COST: cost estimate
- TIME: time estimate
- NEXT: what happens after
CHECKLIST:
[ ] Each step has all 7 fields
[ ] Steps in correct order
[ ] Online vs physical options
[ ] "Done" checkbox per step
[ ] Overall progress indicator
```

### Court Behavior Box (rendered before filing steps)
```
RENDER (warning box):
🏛️ ข้อควรรู้: การปฏิบัติตนเมื่อไปศาล
🚫 ห้ามนำเข้าศาล: อาวุธ / ยาเสพติด / สิ่งผิดกฎหมาย
🚫 ห้ามในศาล: ส่งเสียงดัง / ถ่ายรูป / อัดเสียง / สูบบุหรี่
✅ ควรทำ: แต่งกายสุภาพ / ปิดเสียงมือถือ / มาก่อน 30 นาที
CHECKLIST: [ ] Rendered for physical-filing paths
```

### Courtroom Etiquette Box
```
RENDER:
🏛️ มารยาทในห้องพิจารณาคดี
👔 แต่งกายสุภาพ เรียบร้อย
🙏 ศาลขึ้น/ลงบัลลังก์ → ลุกขึ้นทำความเคารพ
🗣️ พูดต่อศาล: ต้องลุกขึ้นยืนพูด
    เรียกผู้พิพากษาว่า "ท่านครับ/ท่านค่ะ"
CHECKLIST: [ ] Rendered [ ] Formal but friendly tone
```

## H.8 Concierge Phase 8 — Follow-up (Full Flow)

### Timeline Rendering
```
RENDER: Vertical timeline with:
✅ = completed (past events)
⏳ = pending (future events)
EACH NODE: date, event, who contacts user

CHECKLIST:
[ ] Timeline matches category (each category has own timeline)
[ ] Completed vs pending visually distinct
[ ] Contact schedule listed
[ ] Case number displayed
[ ] Status badge
```

### Case Plus Upsell (฿999)
```
RENDER:
⭐ Case Plus — ฿999
✓ AI ติดตามคดีอัตโนมัติ
✓ แจ้งเตือนทุกกำหนด
✓ ปรึกษาทนาย 3 ครั้ง
[อัปเกรด]

CHECKLIST:
[ ] Upsell card rendered
[ ] Benefits clear
[ ] Upgrade button
[ ] Non-intrusive (not blocking)
```

### Appeals Guidance (all cases)
```
RENDER:
⚖️ อุทธรณ์/ฎีกา — ถ้าไม่พอใจคำพิพากษา
📍 ศาลชั้นต้น → อุทธรณ์ → ศาลอุทธรณ์ → ฎีกา → ศาลฎีกา
⏰ ต้องยื่นภายใน 1 เดือน
⚠️ ปรึกษาทนายก่อนตัดสินใจอุทธรณ์
CHECKLIST: [ ] Rendered at case completion [ ] Timely (1-month deadline shown)


---

# SECTION I: All 47 Sub-Problems — 8-Phase Master Matrix

This matrix summarizes the 8-phase flow for all 47 sub-problems. Each row = one sub-problem. Columns = key per-phase differentiators.

## I.1 Category 1: online_fraud (5 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 1.1 ซื้อของออนไลน์ไม่ได้ของ | สั่งของ-โอนเงิน-ไม่ส่ง | ป.อาญา ม.341, พ.ร.บ.คอมพ์ ม.14(1), ป.พ.พ. | ทวงถามก่อน | แจ้งได้ทั่วประเทศ / ออนไลน์ | 7 รายการ | บันทึกแจ้งความ, คำร้องเปิดเผยข้อมูล, จดหมายทวงถาม, ฟ้องผู้บริโภค, อายัดบัญชี | แจ้งออนไลน์→ระบุข้อหา→รับเอกสาร | 3 เดือนอายุความ (ฉ้อโกง) |
| 1.2 Call Center | โทรอ้างเป็นเจ้าหน้าที่-หลอกโอน | ป.อาญา ม.342, พ.ร.บ.คอมพ์ ม.14, ม.209 | ฉุกเฉิน 1441 | แจ้ง 1441 ก่อน / ออนไลน์ | 6 รายการ | บันทึกแจ้งความ (3 ข้อหา), อายัดบัญชี, เปิดเผยข้อมูล, ถึง กสทช., ฟอร์ม ปปง. | โทร 1441→ติดต่อธนาคาร→แจ้งความ | ทันที (อายัดภายใน 15-30 นาที) |
| 1.3 แอปกู้เงินเถื่อน | ดอกเบี้ยโหด-ทวงผิดกฎหมาย | พ.ร.บ.ดอกเบี้ย 2560, พ.ร.บ.ทวงหนี้ 2558, พ.ร.บ.คอมพ์ ม.5 | เจรจาประนอมหนี้ | ธปท. 1213 / สคบ. 1166 | 6 รายการ | บันทึกแจ้งความ, ถึง ธปท., ร้อง สคบ., ตารางคำนวณดอกเบี้ย, หนังสือประนอมหนี้ | เช็ค ธปท.→ร้อง สคบ.→แจ้งความ | 10 ปี (อาญา) / 2 ปี (แพ่ง) |
| 1.4 Romance Scam | หลอกรัก-หลอกโอนหลายครั้ง | ป.อาญา ม.342-343, พ.ร.บ.คอมพ์ ม.14, ม.5 | แจ้งไซเบอร์ก่อน | แจ้งได้ทั่วประเทศ / 1441 | 8 รายการ | บันทึกแจ้งความ, อายัดบัญชีทุกบัญชี, เปิดเผยข้อมูล, Timeline, เปิดเผย IP | Reverse search→แจ้งความ→แจ้งเพิ่มเติม | 3 เดือน (ฉ้อโกง) |
| 1.5 แชร์ลูกโซ่ | ผลตอบแทนสูงเกินจริง-หยุดจ่าย | ป.อาญา ม.343, พ.ร.ก.กู้ยืม 2527, พ.ร.บ.คอมพ์ ม.14 | รวมกลุ่มก่อน | ปอท. / กลต. | 6 รายการ | บันทึกแจ้งความ, ถึง ปปง., ฟ้องคดีแพ่ง, ฟ้องแบบกลุ่ม | แจ้ง ปอท.→แจ้ง ปปง.→รวมกลุ่ม | 10 ปี (อาญา) / 5 ปี (พ.ร.ก.) |

## I.2 Category 2: crime (4 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 2.1 ทำร้ายร่างกาย | ใคร-ที่ไหน-บาดเจ็บอย่างไร | ป.อาญา ม.295-297, ม.391 | ไกล่เกลี่ย | สน.ท้องที่เกิดเหตุ | 6 รายการ | บันทึกแจ้งความ, คำร้องขอคุ้มครอง, ฟ้องแพ่งเรียกค่าเสียหาย | ไป รพ.→แจ้งความ→เก็บหลักฐาน | 3 เดือน (ความผิดอันยอมความ) |
| 2.2 ลักทรัพย์ | อะไรหาย-มูลค่า-มีกล้องไหม | ป.อาญา ม.334-335 | - | สน.ท้องที่ | 5 รายการ | บันทึกแจ้งความ, คำร้องขอคืนทรัพย์ | แจ้งความ→ให้หลักฐาน→ติดตาม | 10 ปี (อาญาแผ่นดิน) |
| 2.3 ข่มขืน/อนาจาร | ใคร-ไป รพ.-มีพยานไหม | ป.อาญา ม.276-278, ม.284 | คุ้มครองด่วน | สน. / รพ. (นิติเวช) | 5 รายการ | บันทึกแจ้งความ, คำร้องขอคุ้มครอง, ฟ้องแพ่ง | ไป รพ.ทันที→แจ้งความ→เก็บหลักฐาน | 20 ปี (ไม่มียอมความ) |
| 2.4 ขู่กรรโชก | ใคร-ขู่อะไร-เรียกเท่าไหร่ | ป.อาญา ม.337-338 | - | สน.ท้องที่ | 5 รายการ | บันทึกแจ้งความ, คำร้องขอคุ้มครอง | เก็บหลักฐานขู่→แจ้งความ→อายัดบัญชี | 10 ปี |

## I.3 Category 3: defamation (4 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 3.1 ถูกด่าบนโซเชียล | ใครโพสต์-โพสต์อะไร-URL | ป.อาญา ม.326-328, พ.ร.บ.คอมพ์ ม.14 | แจ้งแพลตฟอร์ม | สน. / แจ้งแพลตฟอร์ม | 5 รายการ | บันทึกแจ้งความ, หนังสือขอให้ลบ, ถึงแพลตฟอร์ม | แคปหลักฐาน→แจ้งแพลตฟอร์ม→แจ้งความ | 3 เดือน (หมิ่นประมาท) |
| 3.2 ภาพหลุด/Revenge Porn | ใครเผยแพร่-แพลตฟอร์มไหน | ป.อาญา ม.287, พ.ร.บ.คอมพ์ ม.14(4) | แจ้งไซเบอร์ | ปอท. / สน. | 5 รายการ | บันทึกแจ้งความ, หนังสือขอให้ลบเร่งด่วน, ถึงแพลตฟอร์ม | แคปหลักฐาน→แจ้งแพลตฟอร์ม→แจ้ง ปอท. | 3 เดือน / ต่อเนื่อง |
| 3.3 ถูกใส่ความ | ใคร-ใส่ความอะไร-ต่อใคร | ป.อาญา ม.326-328 | ไกล่เกลี่ย | สน. / ศาล | 5 รายการ | บันทึกแจ้งความ, ฟ้องหมิ่นประมาท, ฟ้องแพ่งเรียกค่าเสียหาย | รวบรวมหลักฐาน→แจ้งความ→ฟ้อง | 3 เดือน |
| 3.4 PDPA ข้อมูลรั่ว | ข้อมูลอะไร-จากใคร-หลักฐาน | พ.ร.บ.คุ้มครองข้อมูล 2562, ป.อาญา ม.326 | แจ้ง สคส. | สคส. / สน. | 5 รายการ | หนังสือถึงองค์กร, ร้องเรียน สคส., ฟ้องเรียกค่าเสียหาย | แจ้งองค์กร→ร้อง สคส.→ฟ้อง | 1 ปี (ทางปกครอง) |

## I.4 Category 4: insurance (3 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 4.1 เคลมประกันรถ | บริษัท-ทะเบียน-เลขเคลม | ป.พ.พ., พ.ร.บ.คุ้มครองผู้ประสบภัยจากรถ 2535 | เจรจากับประกัน | คปภ. / ศาลผู้บริโภค | 6 รายการ | หนังสือถึงประกัน, ร้อง คปภ., ฟ้องเรียกค่าเสียหาย | แจ้งประกัน→รวบรวมหลักฐาน→ร้อง คปภ. | 2 ปี (สัญญาประกัน) |
| 4.2 เคลมประกันสุขภาพ | บริษัท-กรมธรรม์-ค่ารักษา | ป.พ.พ., พ.ร.บ.ประกันชีวิต 2535 | เจรจากับประกัน | คปภ. / ศาล | 5 รายการ | หนังสือถึงประกัน, ร้อง คปภ., ฟ้องเรียกค่าเคลม | ยื่นเคลม→ถ้าปฏิเสธ→ร้อง คปภ. | 2 ปี |
| 4.3 ยกเลิกกรมธรรม์ | บริษัท-กรมธรรม์-เหตุผล | ป.พ.พ., พ.ร.บ.ประกันชีวิต 2535 | ขอคืนเบี้ย | คปภ. / สนง.ประกัน | 5 รายการ | หนังสือขอยกเลิก, ถึง คปภ., ฟ้องขอคืนเบี้ย | แจ้งยกเลิก→ขอคืนเบี้ย→ร้อง คปภ. | ภายใน 30 วัน (ช่วงฟรีลุค) |

## I.5 Category 5: government (3 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 5.1 ขอทะเบียน/บัตร ปชช. | เอกสารอะไร-อำเภอไหน | พ.ร.บ.บัตรประจำตัวประชาชน 2526, พ.ร.บ.ทะเบียนราษฎร 2534 | - | ที่ว่าการอำเภอ | 5 รายการ | คำร้องขอออกใหม่, หนังสือถึงนายทะเบียน | เตรียมเอกสาร→ยื่นอำเภอ→รับเอกสาร | 30 วัน (บัตร) / 7 วัน (ทะเบียน) |
| 5.2 รัฐละเมิด | หน่วยงาน-ความเสียหาย | พ.ร.บ.ความรับผิดทางละเมิดของเจ้าหน้าที่ 2539 | ร้องเรียน | ศาลปกครอง | 6 รายการ | หนังสือถึงหน่วยงาน, ฟ้องคดีปกครอง, เรียกค่าเสียหาย | หนังสือถึงหน่วยงาน→ฟ้องปกครอง | 1 ปี (ละเมิด) |
| 5.3 ร้องเรียนไม่ตอบ | หน่วยงาน-เรื่อง-เมื่อไหร่ | พ.ร.บ.ข้อมูลข่าวสาร 2540, พ.ร.บ.วิธีปฏิบัติราชการ 2539 | ฟ้องปกครอง | ศาลปกครอง | 5 รายการ | หนังสือทวงถาม, ฟ้องคดีปกครอง | ติดตาม→ทวงถาม→ฟ้องปกครอง | 90 วัน (ปกครอง) |

## I.6 Category 6: property (5 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 6.1 บุกรุก | ใคร-ที่ดินไหน-บุกรุกแบบไหน | ป.อาญา ม.362-365 | เจรจา/บอกกล่าว | สน.ท้องที่ / ศาล | 6 รายการ | หนังสือบอกกล่าว, บันทึกแจ้งความ, ฟ้องขับไล่ | บอกกล่าว→แจ้งความ→ฟ้องขับไล่ | 1 ปี (ละเมิด) / 10 ปี (อาญา) |
| 6.2 พิพาทแนวเขต | กับใคร-มีโฉนด-รังวัดไหม | ป.พ.พ. ม.1335-1336, ป.ที่ดิน 2497 | รังวัด | กรมที่ดิน / ศาล | 6 รายการ | คำร้องขอรังวัด, ฟ้องเรื่องเขตที่ดิน | ขอรังวัด→เจรจา→ฟ้อง | ไม่มีอายุความ (ครอบครอง) |
| 6.3 ซื้อขายไม่ได้ | ผู้ซื้อ/ขาย-ราคา-ติดอะไร | ป.พ.พ. ม.456, ป.ที่ดิน | เจรจา/บอกเลิก | กรมที่ดิน / ศาล | 6 รายการ | หนังสือบอกกล่าว, ฟ้องผิดสัญญา, ฟ้องบังคับโอน | บอกกล่าว→เจรจา→ฟ้องบังคับโอน | 10 ปี (สัญญา) |
| 6.4 มรดก | ใครเสีย-พินัยกรรม-ทายาท | ป.พ.พ. ม.1599-1755 | ไกล่เกลี่ย | ศาล / ที่ว่าการอำเภอ | 6 รายการ | คำร้องขอเป็นผู้จัดการมรดก, ฟ้องแบ่งมรดก | ขอมรณบัตร→ยื่นจัดการมรดก→แบ่งทรัพย์ | 1 ปี (เจ้ามรดก) / 5 ปี (ทายาท) |
| 6.5 โฉนดหาย | ที่ดินไหน-หายยังไง | ป.ที่ดิน 2497 ม.61 | แจ้งความ | กรมที่ดิน / สน. | 6 รายการ | ใบแจ้งความ, คำร้องขอออกโฉนดแทน | แจ้งความ→ยื่นกรมที่ดิน→ออกโฉนดแทน | 30 วัน (ประกาศ) |

## I.7 Category 7: labour (4 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 7.1 เลิกจ้างไม่เป็นธรรม | บริษัท-ตำแหน่ง-เงินเดือน-อายุงาน | พ.ร.บ.แรงงานสัมพันธ์ 2518, พ.ร.บ.คุ้มครองแรงงาน 2541 | เจรจากับนายจ้าง | พนักงานตรวจแรงงาน / ศาลแรงงาน | 6 รายการ | หนังสือถึงนายจ้าง, ร้องพนักงานตรวจแรงงาน, ฟ้องคดีแรงงาน | ร้องตรวจแรงงาน→เจรจา→ฟ้องแรงงาน | 2 ปี (ค่าชดเชย) |
| 7.2 ไม่จ่ายค่าจ้าง/ค่าชดเชย | ค้างเท่าไหร่-กี่เดือน-นายจ้าง | พ.ร.บ.คุ้มครองแรงงาน 2541 ม.70 | เจรจา/ประนอม | พนักงานตรวจแรงงาน / ศาลแรงงาน | 6 รายการ | หนังสือทวงค่าจ้าง, ร้องตรวจแรงงาน, ฟ้องคดีแรงงาน | ทวงถาม→ร้องตรวจแรงงาน→ฟ้อง | 2 ปี |
| 7.3 บาดเจ็บจากการทำงาน | ที่ไหน-เมื่อไหร่-บาดเจ็บ | พ.ร.บ.เงินทดแทน 2537, พ.ร.บ.ประกันสังคม 2533 | แจ้งนายจ้าง | ประกันสังคม / ศาลแรงงาน | 6 รายการ | หนังสือแจ้งนายจ้าง, ร้องประกันสังคม, ฟ้องเรียกค่าเสียหาย | แจ้งนายจ้าง→ไป รพ.→ร้องประกันสังคม | 180 วัน (เงินทดแทน) |
| 7.4 ล่วงละเมิดในที่ทำงาน | ใคร-ทำอะไร-มีพยานไหม | พ.ร.บ.คุ้มครองแรงงาน 2541, ป.อาญา ม.397 | แจ้ง HR | พนักงานตรวจแรงงาน / สน. | 6 รายการ | หนังสือถึง HR, ร้องตรวจแรงงาน, บันทึกแจ้งความ | แจ้ง HR→ร้องตรวจแรงงาน→แจ้งความ | 2 ปี / 3 เดือน (อาญา) |

## I.8 Category 8: consumer (4 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 8.1 สินค้าชำรุด/ไม่ตรงปก | สินค้า-ซื้อที่ไหน-ราคา | พ.ร.บ.คุ้มครองผู้บริโภค 2522, ป.พ.พ. ม.472 | เจรจากับผู้ขาย | สคบ. / ศาลผู้บริโภค | 6 รายการ | หนังสือถึงผู้ขาย, ร้อง สคบ., ฟ้องผู้บริโภค | แจ้งผู้ขาย→ร้อง สคบ.→ฟ้องผู้บริโภค | 2 ปี (ชำรุดบกพร่อง) |
| 8.2 โฆษณาหลอกลวง | โฆษณาอะไร-แพลตฟอร์มไหน | พ.ร.บ.คุ้มครองผู้บริโภค 2522 ม.22 | แจ้ง สคบ. | สคบ. / ศาลผู้บริโภค | 6 รายการ | ร้อง สคบ., ฟ้องเรียกค่าเสียหาย, หนังสือถึงผู้ขาย | แคปโฆษณา→ร้อง สคบ.→ฟ้อง | 1 ปี (โฆษณาเท็จ) |
| 8.3 บริการไม่เป็นไปตามสัญญา | บริการอะไร-ตกลงอะไร | ป.พ.พ. ม.386-388, พ.ร.บ.คุ้มครองผู้บริโภค | เจรจา/บอกเลิก | สคบ. / ศาลผู้บริโภค | 6 รายการ | หนังสือบอกกล่าว, ร้อง สคบ., ฟ้องผิดสัญญา | บอกกล่าว→ร้อง สคบ.→ฟ้อง | 2 ปี |
| 8.4 สัญญาสำเร็จรูป | สัญญาเรื่อง-ข้อไหนไม่เป็นธรรม | พ.ร.บ.ข้อสัญญาที่ไม่เป็นธรรม 2540, ป.พ.พ. | เจรจา | ศาลผู้บริโภค / ศาลแพ่ง | 6 รายการ | หนังสือโต้แย้ง, ฟ้องให้ข้อสัญญาเป็นโมฆะ | วิเคราะห์สัญญา→โต้แย้ง→ฟ้อง | 10 ปี (สัญญา) |

## I.9 Category 9: debt (4 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 9.1 หนี้บัตรเครดิต | ธนาคาร-ยอดหนี้-ค้างกี่เดือน | ป.พ.พ., พ.ร.บ.คุ้มครองผู้บริโภค | ประนอมหนี้ | ธนาคาร / ศาล | 6 รายการ | หนังสือประนอมหนี้, หนังสือถึงธนาคาร, ฟ้อง | เจรจากับธนาคาร→ประนอมหนี้→ฟ้อง | 10 ปี (หนี้) |
| 9.2 ถูกฟ้องล้มละลาย | ใครฟ้อง-ยอดหนี้-ศาลไหน | พ.ร.บ.ล้มละลาย 2483 | ประนอม/เจรจา | ศาลล้มละลาย | 6 รายการ | คำให้การต่อสู้คดี, หนังสือเจรจา, ฟ้องขอเพิกถอน | ยื่นคำให้การ→เจรจา→ต่อสู้คดี | 30 วัน (ยื่นคำให้การ) |
| 9.3 หนี้นอกระบบ | กู้จากใคร-ดอกเบี้ย-ถูกทวงยังไง | พ.ร.บ.ห้ามเรียกดอกเบี้ยเกินอัตรา, พ.ร.บ.ทวงหนี้ | แจ้งความ | สน. / ธปท. | 6 รายการ | บันทึกแจ้งความ, หนังสือประนอมหนี้, ร้อง ธปท. | แจ้งความ→เจรจาจ่ายแค่ต้น→ร้อง ธปท. | 10 ปี |
| 9.4 ค้ำประกันแล้วลูกหนี้หนี | ค้ำให้ใคร-จำนวนเงิน-เจ้าหนี้ | ป.พ.พ. ม.680-701 | เจรจากับเจ้าหนี้ | ศาล / เจ้าหนี้ | 6 รายการ | หนังสือถึงเจ้าหนี้, ฟ้องไล่เบี้ย, หนังสือทวงลูกหนี้ | เจรจากับเจ้าหนี้→ฟ้องไล่เบี้ย→ติดตามลูกหนี้ | 10 ปี |

## I.10 Category 10: housing (3 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 10.1 ถูกไล่ออกจากหอ | อยู่ที่ไหน-สัญญา-จ่ายค่าเช่าไหม | ป.พ.พ. ม.537-571, พ.ร.บ.อาคารชุด 2522 | เจรจา | ศาล / สำนักงานเขต | 6 รายการ | หนังสือโต้แย้งการบอกเลิก, ฟ้องขับไล่, ฟ้องเรียกค่าเสียหาย | เจรจา→โต้แย้ง→ฟ้อง | 1 ปี |
| 10.2 มัดจำไม่คืน | มัดจำเท่าไหร่-วันที่เข้าออก | ป.พ.พ. ม.378-379 | เจรจา/ทวงถาม | ศาล / สคบ. | 6 รายการ | หนังสือทวงมัดจำ, ร้อง สคบ., ฟ้องเรียกมัดจำคืน | ทวงถาม→ร้อง สคบ.→ฟ้อง | 10 ปี |
| 10.3 ค่าเช่าขึ้นไม่เป็นธรรม | ขึ้นเท่าไหร่-สัญญาว่าอะไร | ป.พ.พ. ม.566, พ.ร.บ.การเช่าทรัพย์สิน 2561 | เจรจา | สำนักงานเขต / ศาล | 6 รายการ | หนังสือโต้แย้ง, ฟ้อง, ร้องหน่วยงาน | โต้แย้ง→เจรจา→ฟ้อง | 1 ปี |

## I.11 Category 11: family (5 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 11.1 หย่าร้าง | จดทะเบียนที่ไหน-มีบุตร-เหตุผล | ป.พ.พ. ม.1514-1535 | ไกล่เกลี่ย/ยินยอม | ที่ว่าการอำเภอ / ศาล | 7 รายการ | ฟ้องหย่า, บันทึกข้อตกลง, คำร้องค่าเลี้ยงดู | ยื่นฟ้อง→ไกล่เกลี่ย→ศาลพิพากษา | 1 ปี (ฟ้องหย่าเหตุ) |
| 11.2 แบ่งสินสมรส | ทรัพย์อะไร-มูลค่า-ได้มาตอนไหน | ป.พ.พ. ม.1471-1482 | เจรจา/ไกล่เกลี่ย | ศาล | 6 รายการ | ฟ้องแบ่งสินสมรส, คำร้องขอบัญชีทรัพย์สิน | เจรจา→ฟ้อง→ศาลแบ่ง | 1 ปี |
| 11.3 ค่าเลี้ยงดูบุตร | บุตรอายุ-รายได้อีกฝ่าย-จ่ายไหม | ป.พ.พ. ม.1598-1600 | เจรจา | ศาล / อัยการ | 6 รายการ | ฟ้องเรียกค่าเลี้ยงดู, คำร้องบังคับคดี | เจรจา→ฟ้อง→บังคับคดี | ตลอดระยะ (ต่อเนื่อง) |
| 11.4 รับบุตรบุญธรรม | บุตรอายุ-ผู้ปกครองเดิม | ป.พ.พ. ม.1598/27-37 | - | ศาล / สนง.คุ้มครอง | 6 รายการ | คำร้องขอรับบุตรบุญธรรม, เอกสารยินยอม | เตรียมเอกสาร→ยื่นคำร้อง→ศาลอนุมัติ | 60 วัน |
| 11.5 ความรุนแรงในครอบครัว | ใคร-ทำอะไร-ไป รพ.ไหม | พ.ร.บ.คุ้มครองผู้ถูกกระทำความรุนแรงในครอบครัว 2550 | คุ้มครองด่วน | สน. / บ้านพักฉุกเฉิน | 6 รายการ | บันทึกแจ้งความ, คำร้องขอคุ้มครอง, ฟ้อง | ขอความช่วยเหลือ→แจ้งความ→ขอคุ้มครอง | ทันที (ฉุกเฉิน) |

## I.12 Category 12: accident (3 sub-problems)

| Sub-Problem | P1 Key Facts | P2 Key Laws | P3 Path C | P4 Venue | P5 Docs | P6 Documents Generated | P7 Steps | P8 Timeline |
|------------|-------------|-------------|-----------|----------|---------|----------------------|----------|-------------|
| 12.1 ถูกชนแล้วหนี | ที่ไหน-เมื่อไหร่-จำทะเบียนไหม | ป.อาญา ม.293-300, พ.ร.บ.จราจร 2522 | แจ้งความด่วน | สน.ท้องที่ | 6 รายการ | บันทึกแจ้งความ, หนังสือถึงประกัน, ฟ้องเรียกค่าเสียหาย | แจ้งความ→เก็บหลักฐาน→ติดตาม | 1 ปี (ละเมิด) |
| 12.2 ชนแล้วคู่กรณีไม่ยอม | ใครผิด-มี พ.ร.บ.-แจ้งประกันไหม | ป.พ.พ. ม.420, พ.ร.บ.จราจร | เจรจา/ไกล่เกลี่ย | สน. / ศาล | 6 รายการ | หนังสือถึงคู่กรณี, ฟ้องเรียกค่าเสียหาย, ร้องประกัน | แจ้งประกัน→เจรจา→ฟ้อง | 1 ปี |
| 12.3 เรียกค่าเสียหายจากอุบัติเหตุ | อุบัติเหตุอะไร-ความเสียหาย | ป.พ.พ. ม.420, พ.ร.บ.คุ้มครองผู้ประสบภัยจากรถ | เจรจากับประกัน | ศาล / คปภ. | 6 รายการ | ฟ้องเรียกค่าเสียหาย, หนังสือถึงประกัน, ร้อง คปภ. | รวบรวมหลักฐาน→เจรจา→ฟ้อง | 1 ปี |

---

# SECTION J: Edge Cases & Pitfalls

## J.1 Compound Case Handling

### Scenario: Multiple Categories
```
Case: "บ้านโดนงัด + ประกันไม่จ่ายค่าชดเชย"
Detection: crime (ลักทรัพย์) + insurance (เคลมถูกปฏิเสธ)
Dependency: police report (crime) must happen BEFORE insurance claim

FLOW:
1. Banner: "พบ 2 ประเด็นที่ต้องจัดการ"
2. Process order: PRIMARY (crime) first
3. Explain: "ต้องแจ้งความก่อน จึงจะเคลมประกันได้ (ประกันต้องใช้ใบแจ้งความ)"
4. After Phase 8 of primary → prompt to start secondary

CHECKLIST:
[ ] Compound detection at Phase 1
[ ] Clear process order
[ ] Dependency explained in plain Thai
[ ] Smooth transition to secondary issue
[ ] Both categories tracked separately but linked
```

### Scenario: Category Borderline
```
Case: "ถูกด่าบน Facebook" → could be defamation OR online_fraud
RESOLUTION: AI asks clarifying question:
"เขาแค่ด่าคุณ (หมิ่นประมาท) หรือหลอกเอาเงินด้วย (ฉ้อโกง)?"
```

## J.2 Urgency Escalation

### Emergency Cases (immediate escalation)
```
URGENT CASES: Call Center (อายัดบัญชีภายใน 15 นาที), ข่มขืน, ความรุนแรงในครอบครัว,
  อุบัติเหตุร้ายแรง, ถูกขู่กรรโชก

FLOW: Detect → override normal flow → show emergency banner:
"🚨 เรื่องนี้เร่งด่วน — ทำตามนี้ทันที: โทร 1441 / 191 / ไป รพ."

CHECKLIST:
[ ] Emergency banner at top (sticky)
[ ] Emergency phone numbers clickable (tel: links)
[ ] Tone shifts to urgent but calm
[ ] Bypass monetization gate for emergency action info
```

## J.3 Fear Level Edge Cases
```
Case: User in panic but issue is low-urgency (e.g., lost ID card)
RESOLUTION: Reassurance first: "ไม่ต้องกังวล — เรื่องนี้แก้ได้ง่ายมาก"
Then: gentle path to simple steps

Case: User calm but issue is high-urgency (e.g., fraud but not worried)
RESOLUTION: Raise awareness: "เรื่องนี้มีกำหนดเวลา 3 เดือน เราควรเริ่มวันนี้"
```

## J.4 Legal Jargon Translation
```
HARD TERMS → PLAIN THAI:
- "อายุความ" → "กำหนดเวลาที่คุณยังฟ้องได้"
- "เขตอำนาจศาล" → "ศาลที่คุณต้องไปยื่น"
- "คำร้อง" → "เอกสารขอศาลช่วย"
- "คำฟ้อง" → "เอกสารเริ่มคดี"
- "โมฆะ" → "ใช้ไม่ได้ตามกฎหมาย"
- "โมฆียะ" → "อาจใช้ไม่ได้ ถ้าไม่ยอมรับ"
- "ทายาท" → "คนที่รับมรดก"
- "สินสมรส" → "ทรัพย์ที่ได้มาหลังแต่งงาน"
```

## J.5 Error Handling Patterns
```
AI FAILURE: "ขอโทษด้วยค่ะ ระบบของเราขัดข้องชั่วคราว
            ลองอีกครั้ง หรือติดต่อเราได้ที่ LINE @chujai"

PAYMENT TIMEOUT: "ยังไม่ได้รับการยืนยันการชำระเงิน
            ถ้าคุณจ่ายแล้ว กรุณารอ 1-2 นาที หรือติดต่อเรา"

UPLOAD FAILURE: "อัปโหลดไม่สำเร็จ — ตรวจสอบขนาดไฟล์ (ไม่เกิน 10MB)
            หรือลองเปลี่ยนเป็น JPG/PNG/PDF"

NOT FOUND: "ไม่พบเคสนี้ — อาจถูกลบหรือหมดอายุ
            [กลับหน้าแรก] [สร้างเคสใหม่]"
```

## J.6 PDPA Consent Edge Cases
```
Case: User wants to delete data mid-case
RESOLUTION: Show warning: "การลบข้อมูลจะลบเคสทั้งหมด
            และไม่สามารถกู้คืนได้ — คุณแน่ใจหรือไม่?"
            + 30-day grace period before permanent deletion

Case: User asks "AI ใช้ข้อมูลฉันเทรนไหม?"
RESOLUTION: Always answer: "ไม่ — ข้อมูลของคุณไม่ถูกนำไปเทรน AI"
            (aligned with guardrail #7)
```

## J.7 Multi-Device / Resume Flow
```
Case: User starts case on phone, continues on desktop
RESOLUTION: All case data saved to Supabase real-time
  Phase progress persists
  Evidence uploads persist
  "ทำต่อ" button always resumes at correct phase
CHECKLIST: [ ] State persists cross-device [ ] No data loss on refresh
```

## J.8 Time-Sensitive Legal Deadlines
```
Track per sub-problem:
- ฉ้อโกง: 3 เดือน (แจ้งความ)
- หมิ่นประมาท: 3 เดือน
- แรงงานค่าชดเชย: 2 ปี
- ละเมิด: 1 ปี
- ฟ้องแพ่งทั่วไป: 10 ปี

RENDER: Countdown badge on case card when deadline approaching:
"⏰ เหลือ 45 วัน ก่อนหมดอายุความ"
CHECKLIST: [ ] Deadline tracked [ ] Countdown shown when < 90 days
  [ ] Urgent reminder at < 30 days [ ] LINE/email alert at < 14 days
```

---

# SECTION K: Testing Strategy

## K.1 Test Pyramid

```
        ┌─────────────┐
        │  E2E (5%)    │   Playwright — critical journeys
        ├─────────────┤
        │ Integration  │   Supabase + API route tests (20%)
        │  (20%)       │
        ├─────────────┤
        │   Unit (75%) │   Vitest — lib/ functions, pure logic
        └─────────────┘
```

## K.2 Unit Test Coverage (lib/)

### Legal Domain Tests
- [ ] All 12 categories defined with correct sub-problems
- [ ] All 47 sub-problems have: laws, documents, steps, timeline
- [ ] Compound detection: 10+ test cases (multi-category)
- [ ] Fear calibration: 4 levels → correct tone/urgency
- [ ] Guardrails: 7 MUST-NEVER rules enforced
- [ ] Drive detection: 22 drives keyword mapping
- [ ] Legal source validation: no fabricated citations

### AI Pipeline Tests (mocked AI)
- [ ] Diagnosis: narrative → correct category (20 test narratives)
- [ ] Search: query → answer with citations
- [ ] Concierge: phase transitions correct
- [ ] Document generation: merge fields filled correctly
- [ ] Tax optimization: correct suggestions

### Document Engine Tests
- [ ] Merge engine: `{{field}}` replacement
- [ ] Conditional blocks: `{{#if}}` logic
- [ ] Thai date formatting (พ.ศ.)
- [ ] Currency formatting (฿ with commas)
- [ ] Export: PDF/DOCX/TXT generation

### Tax Calculator Tests
- [ ] Progressive brackets correct (0-35%)
- [ ] All 30+ deductions with correct limits
- [ ] Edge cases: 0 income, negative, huge income
- [ ] Rounding correct

## K.3 Integration Tests

- [ ] Auth flow (register → login → session)
- [ ] Case CRUD (create → update → close)
- [ ] Payment flow (create → webhook → verify)
- [ ] Document generation (case → document → export)
- [ ] Lawyer verification (submit → approve → live)
- [ ] Notification delivery (in-app, email, LINE)
- [ ] Admin actions (ban, verify, refund)

## K.4 E2E Test Scenarios (Playwright)

### Critical User Journeys
```
1. Guest → Register → Start Concierge → Phase 1-3 → Pay ฿299 → Phase 4-8 → Download docs
2. User → Diagnosis → Get result → Route to concierge
3. User → Search → Get answer → Start case
4. User → Tax → Calculate → Optimize → Export
5. Lawyer → Login → Create case → Invoice client
6. Admin → Login → Verify lawyer → View revenue
7. User → LINE Login → Complete case → Get LINE notification
```

### Cross-Browser Matrix
```
| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | Latest  | ✅ Tested |
| Safari  | Latest  | ✅ Tested |
| Firefox | Latest  | ✅ Tested |
| Edge    | Latest  | ✅ Tested |
| Mobile Chrome | Latest | ✅ Tested |
| Mobile Safari | Latest | ✅ Tested |
```

### Mobile Device Matrix
```
| Device | Screen | Status |
|--------|--------|--------|
| iPhone 15 Pro | 393×852 | ✅ |
| iPhone SE | 375×667 | ✅ |
| Pixel 8 | 412×915 | ✅ |
| Galaxy S24 | 384×832 | ✅ |
| iPad | 768×1024 | ✅ |
```

## K.5 Performance Budgets

```
| Metric | Budget | Target |
|--------|--------|--------|
| LCP (Largest Contentful Paint) | < 2.5s | 1.5s |
| FID (First Input Delay) | < 100ms | 50ms |
| CLS (Cumulative Layout Shift) | < 0.1 | 0.05 |
| TTI (Time to Interactive) | < 3.5s | 2s |
| Bundle Size (gzip) | < 300KB | 200KB |
| AI Response Time (p95) | < 5s | 3s |
```

## K.6 AI Quality Evaluation

```
METRICS:
- Category accuracy: ≥ 90% (47 sub-problems correctly identified)
- Thai language quality: native-level, no awkward translations
- Tone consistency: 100% warm/empathetic
- Source accuracy: 0 fabricated citations
- Compound detection: ≥ 85% recall

EVALUATION SET: 135 real-user questions (from 2-team Q&A methodology)
  = 12 categories × 45 sub-problems × 3 questions each

PROCESS: Run eval monthly + after every prompt change
```

## K.7 Load Testing

```
SCENARIOS:
- 1,000 concurrent users browsing
- 100 concurrent AI diagnosis calls
- 50 concurrent payments
- 20 concurrent document generations

TARGETS:
- No request errors
- p95 < 3s for AI calls
- p95 < 500ms for static pages
- 0 dropped database connections
```

---

# SECTION L: Security & PDPA Compliance

## L.1 Security Architecture

### Authentication
- [ ] Supabase Auth (email/password + LINE OAuth)
- [ ] JWT with short expiry (1 hour) + refresh tokens
- [ ] 2FA for admin accounts (TOTP)
- [ ] Session revocation on password change
- [ ] Rate limiting on login (5 attempts / 15 min)
- [ ] Account lockout after repeated failures

### Authorization (RBAC)
```
ROLES: consumer, lawyer, admin
MATRIX:
| Resource | consumer | lawyer | admin |
|----------|----------|--------|-------|
| Own cases | ✅ CRUD | — | ✅ |
| Assigned cases | — | ✅ CRUD | ✅ |
| All cases | — | — | ✅ |
| Lawyer verification | — | — | ✅ |
| Revenue data | — | — | ✅ |
| Platform settings | — | — | ✅ |
| Own documents | ✅ | ✅ | ✅ |
| Client portal | — | ✅ (own) | — |
```

### Data Protection
- [ ] TLS 1.3 everywhere (Vercel + Supabase)
- [ ] Passwords hashed with bcrypt/argon2 (Supabase default)
- [ ] Row Level Security on ALL tables
- [ ] Evidence files in private buckets (signed URLs only)
- [ ] Encrypted at rest (Supabase default)
- [ ] Encrypted backups
- [ ] Data export (user-initiated, 30-day window)
- [ ] Data deletion (user-initiated, 30-day grace period)

### Input Validation
- [ ] All form inputs validated (zod schemas)
- [ ] File uploads: type + size validation (JPG/PNG/PDF, 10MB)
- [ ] XSS prevention (React escapes by default + sanitize)
- [ ] SQL injection (Supabase parameterized queries)
- [ ] CSRF tokens on state-changing requests

### API Security
- [ ] Rate limiting (per-user, per-IP)
- [ ] Input size limits
- [ ] AI prompt injection defense (system prompt hardens against it)
- [ ] API keys stored in environment variables (never client-side)
- [ ] CORS restricted to known origins

## L.2 PDPA (พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562) Compliance

### Consent Management
- [ ] Explicit consent at registration (checkbox, not pre-checked)
- [ ] AI data processing consent (separate from general)
- [ ] Consent withdrawal option (profile settings)
- [ ] Consent records (what, when, version)

### Data Subject Rights
- [ ] Right to access (data export button)
- [ ] Right to rectification (edit profile)
- [ ] Right to erasure (delete account button)
- [ ] Right to restrict processing
- [ ] Right to data portability (JSON/CSV export)
- [ ] Right to object (opt-out of AI processing)
- [ ] Right to withdraw consent (at any time)

### Required Documentation
- [ ] Privacy Policy page (/privacy) with:
  - Data types collected
  - Purpose of collection
  - AI usage disclosure
  - Third-party sharing (DeepSeek, Omise, LINE, Supabase)
  - Data retention period
  - User rights
  - Contact for complaints
- [ ] Terms of Service page (/terms)
- [ ] Data Processing Agreement (with vendors)
- [ ] Data breach notification procedure (72-hour window)

### Data Minimization
- [ ] Only collect necessary data
- [ ] Evidence files auto-delete after case closes (configurable)
- [ ] AI conversation logs retained max 30 days
- [ ] Analytics anonymized

### Cross-Border Data
- [ ] DeepSeek (China) — disclose in privacy policy
- [ ] Supabase (region selectable)
- [ ] Vercel (region selectable)
- [ ] Document cross-border transfers in DPA

---

# SECTION M: Deployment & DevOps

## M.1 Environments
```
┌──────────┬────────────────────────────────────────────┐
│ ENV      │ Purpose            │ URL                   │
├──────────┼────────────────────┼───────────────────────┤
│ Local    │ Development        │ localhost:3000         │
│ Staging  │ QA/Testing         │ staging.chujai.legal  │
│ Prod     | Live              │ chujai.legal           │
└──────────┴────────────────────┴───────────────────────┘
```

## M.2 CI/CD Pipeline (GitHub Actions)
```
1. Push to main → trigger pipeline
2. Install deps → cache
3. Lint (ESLint)
4. Type check (tsc)
5. Unit tests (Vitest)
6. Build (Next.js)
7. Integration tests (Supabase test DB)
8. E2E tests (Playwright, staging)
9. Deploy to Vercel (staging)
10. Smoke tests on staging
11. Manual approve → Deploy to prod
12. Post-deploy health checks
```

## M.3 Monitoring & Alerting
```
| Layer | Tool | Alerts |
|-------|------|--------|
| Errors | Sentry | 500s, exceptions, AI failures |
| Logs | Logflare | Query logs, audit logs |
| APM | Vercel Analytics | Core Web Vitals, latency |
| DB | Supabase | Connection pool, query perf |
| Uptime | UptimeRobot | Downtime > 1 min |
| AI | Custom | Token usage, cost, latency |

ALERT RULES:
- Error rate > 1% → notify on-call
- AI latency p95 > 5s → scale/optimize
- Payment failure rate > 5% → immediate alert
- DB connections > 80% → scale pool
```

## M.4 Backup & Recovery
```
DATABASE: Daily full backup + WAL (point-in-time recovery)
STORAGE: Versioned (evidence files, documents)
CONFIG: Git-versioned (Infrastructure as Code)
RECOVERY:
- RPO (Recovery Point Objective): < 5 minutes
- RTO (Recovery Time Objective): < 1 hour
- Restore drill: monthly
```

## M.5 Scaling Strategy
```
PHASE 1 (Launch): Vercel free/Pro + Supabase free/Pro
  → 10K users, 1K MAU

PHASE 2 (Growth): Vercel Pro + Supabase Pro + Edge Functions
  → 100K users, 10K MAU

PHASE 3 (Scale): Vercel Enterprise + Supabase Team + Redis cache
  → 1M users, 100K MAU
  → Add: CDN, read replicas, queue for AI jobs

AI COST CONTROL:
- Cache common search results (30-day TTL)
- Rate limit AI calls per user tier
- Fallback to cheaper model for simple queries
- Token budget per request
```

---

# SECTION N: Knowledge Base & Content Design

## N.1 Content Architecture

### Legal Knowledge Base
```
Structure:
└── categories (12)
    ├── online_fraud (5 sub-problems)
    ├── crime (4)
    ├── defamation (4)
    ├── insurance (3)
    ├── government (3)
    ├── property (5)
    ├── labour (4)
    ├── consumer (4)
    ├── debt (4)
    ├── housing (3)
    ├── family (5)
    └── accident (3)

Each sub-problem contains:
- Title + category
- Summary (plain Thai)
- Laws (with sections + penalties)
- Rights
- Self-help actions
- Document checklist
- Filing steps
- Timeline
- FAQs (3-7)
- Related sub-problems
```

### Content Types
```
| Type | Format | Where |
|------|--------|-------|
| Legal guides | Long-form (MD) | /help + category pages |
| FAQs | Q&A | /help + search results |
| Document templates | MD with merge fields | /documents |
| Court guides | Step-by-step | Concierge Phase 7 |
| Glossary | Term → plain Thai | Hover tooltips |
| News/updates | Law changes | Notification center |
```

## N.2 Content Workflow
```
1. Legal researcher drafts content
2. Lawyer reviews (accuracy)
3. Editor adapts to warm tone
4. Admin publishes via /admin/content
5. Version tracked
6. AI uses published content as grounding

CHECKLIST:
[ ] Every content piece has a lawyer review stamp
[ ] Warm tone applied consistently
[ ] Sources cited
[ ] Version history
[ ] Scheduled publishing (for law updates)
```

## N.3 SEO Content Strategy
```
TARGET QUERIES (Thai, high-volume):
- "แจ้งความออนไลน์" → /help/filing-police-report
- "ดอกเบี้ยเกินอัตรา" → /help/interest-rate
- "ถูกไล่ออก" → /help/unfair-dismissal
- "ฟ้องหย่า" → /help/divorce
- "โฉนดหาย" → /help/lost-title-deed

STRUCTURED DATA:
- FAQPage (for /help)
- HowTo (for /how-it-works)
- Organization (for / and /about)

CHECKLIST:
[ ] Each category has a SEO landing page
[ ] Each sub-problem has a guide page
[ ] Schema markup added
[ ] Internal linking between guides
[ ] Sitemap auto-generated
```

---

# SECTION O: Analytics & Growth

## O.1 Key Events to Track
```
| Event | When | Properties |
|-------|------|------------|
| user_registered | Signup | source, channel |
| diagnosis_started | Begin diagnosis | entry_point |
| diagnosis_completed | Finish diagnosis | category, duration |
| concierge_started | Start concierge | category, sub_problem |
| phase_completed | Each phase (1-8) | phase_number |
| monetization_gate_shown | Gate render | category |
| payment_started | Click pay | plan, price |
| payment_completed | Payment success | plan, amount |
| document_generated | Doc created | template, category |
| document_downloaded | Doc export | format |
| lawyer_viewed | View lawyer | lawyer_id |
| lawyer_hired | Hire lawyer | lawyer_id, type |
| case_closed | Close case | duration, outcome |
| upgrade_clicked | Click upgrade | from_plan, to_plan |
```

## O.2 Funnel Analysis
```
FUNNEL (concierge):
1. Concierge started          → 100%
2. Phase 1 completed          → 85% (drop: narrative too hard)
3. Phase 2 completed          → 75% (drop: overwhelmed by info)
4. Phase 3 completed          → 60% (drop: not ready to choose)
5. Monetization gate shown    → 55%
6. Payment completed          → 15-25% (KEY conversion)
7. Phase 7 completed          → 20%
8. Case Plus upgraded         → 2-4%

OPTIMIZATION:
- Drop at Phase 1 → simplify narrative input (voice input, examples)
- Drop at Phase 2 → chunk info, use accordions
- Drop at Phase 3 → clearer path comparison
- Gate conversion < 15% → test price, copy, free trial
```

## O.3 A/B Testing Framework
```
TESTABLE ELEMENTS:
- Gate copy (price anchor variants)
- CTA button text/color
- Free trial vs no free trial
- Path A default vs path B default
- Warm tone intensity (high vs moderate)
- Price point (฿199 vs ฿299 vs ฿399)

TOOL: PostHog experiments (or Vercel flags)
CHECKLIST: [ ] Experiment framework wired [ ] Sample size calculator
  [ ] Statistical significance tracking [ ] Kill switch for bad experiments
```

---

*End of Part 3 — Continue to Part 4 (Checklist expansion + Appendices)*


---

# SECTION P: User Personas & Journeys

## P.1 Consumer Personas

### Persona 1: "คุณแม่บ้าน" (Homemaker, 45)
```
NAME: คุณวิภา ใจดี
AGE: 45 | LOCATION: นนทบุรี | INCOME: 20,000/เดือน
TECH LEVEL: ต่ำ-กลาง (ใช้ Facebook, Line, Shopee)
LEGAL KNOWLEDGE: แทบไม่มี — กลัวกฎหมาย
PAIN: ถูกหลอกซื้อของออนไลน์ 3,500 บาท ไม่รู้จะทำยังไง
FEAR: กลัวเสียหน้า กลัวยุ่งยาก กลัวค่าใช้จ่าย
MOTIVATION: อยากได้เงินคืน อยากให้คนโกงถูกลงโทษ
DEVICE: มือถือ Android (สมาร์ทโฟน)

JOURNEY:
1. เล่าเรื่องผ่านกล่องแชท (พิมพ์ช้า พิมพ์ผิด)
2. AI ตอบแบบอบอุ่น "เราเข้าใจคุณนะ"
3. เลือก "จัดการเอง" (ไม่อยากเสียเงิน)
4. AI ให้เอกสาร + บอกทีละขั้น
5. ทำตามได้สำเร็จ ได้เงินคืน
6. รีวิว 5 ดาว "ไม่คิดว่าจะทำเองได้"

DESIGN IMPLICATIONS:
- ปุ่มใหญ่ ตัวหนังสือใหญ่
- Voice input (พิมพ์ช้า)
- หลีกเลี่ยงศัพท์กฎหมาย
- ค่าใช้จ่ายชัดเจน ฿299 = "ค่ากาแฟ 2 แก้ว"
- กำลังใจตลอดทาง
```

### Persona 2: "พนักงานออฟฟิศ" (Office Worker, 28)
```
NAME: คุณสมชาย ใจดี
AGE: 28 | LOCATION: กรุงเทพฯ | INCOME: 35,000/เดือน
TECH LEVEL: สูง (ใช้แอปทุกอย่าง)
LEGAL KNOWLEDGE: พื้นฐาน — รู้ว่ามีกฎหมายแรงงาน
PAIN: ถูกเลิกจ้างกะทันหัน ไม่ได้ค่าชดเชย
FEAR: กลัวเสียเวลา กลัวสู้กับบริษัทใหญ่
MOTIVATION: อยากได้ค่าชดเชยที่ควรได้ อยากรู้สิทธิ
DEVICE: iPhone + MacBook

JOURNEY:
1. ค้นหา "ถูกไล่ออก" ผ่าน Google → เจอ chujai.legal
2. ใช้ AI search หาคำตอบ
3. เริ่ม diagnosis → ได้ผลว่ามีสิทธิค่าชดเชย
4. ใช้ tax calculator วางแผน
5. ซื้อ Action Pack ฿299 (เงินไม่ใช่ปัญหา)
6. AI สร้างหนังสือถึงนายจ้าง
7. ยื่นเรื่องสำเร็จ

DESIGN IMPLICATIONS:
- ค้นหาผ่าน Google สำคัญ (SEO)
- ข้อมูลเชิงลึก (สถิติ, กฎหมายอ้างอิง)
- เร็ว ทันสมัย ไม่เสียเวลา
- แสดง ROI ชัดเจน (จ่าย 299 ได้คืน 100,000+)
```

### Persona 3: "นักศึกษา" (Student, 21)
```
NAME: น้องมิ้นท์
AGE: 21 | LOCATION: เชียงใหม่ | INCOME: เงินจากพ่อแม่
TECH LEVEL: สูงมาก (TikTok, Instagram)
LEGAL KNOWLEDGE: ไม่มี
PAIN: ถูกแฟนเก่าเอาภาพหลุดไปโพสต์ในกลุ่มลับ
FEAR: อับอาย กลัว ไม่อยากให้ใครรู้ ไม่รู้จะไปปรึกษาใคร
MOTIVATION: อยากให้ลบภาพ อยากให้หยุดเผยแพร่
DEVICE: iPhone (ใช้งาน Line, Telegram)

JOURNEY:
1. ค้นหาแบบลับๆ "ภาพหลุดทำไง" 
2. เจอ chujai.legal — รู้สึกปลอดภัย (อบอุ่น ไม่ตัดสิน)
3. เล่าเรื่อง (AI ไม่ตัดสิน)
4. AI ให้ขั้นตอนด่วน: แจ้งแพลตฟอร์ม, แจ้ง ปอท.
5. สร้างหนังสือขอให้ลบ
6. ได้รับกำลังใจ + ช่องทางช่วยเหลือ

DESIGN IMPLICATIONS:
- ความเป็นส่วนตัวสูงสุด (ไม่โพสต์อะไรบนหน้าสาธารณะ)
- น้ำเสียงไม่ตัดสิน (สำคัญมากสำหรับกรณีอ่อนไหว)
- ช่องทางช่วยเหลือฉุกเฉิน (สายด่วน, หน่วยงานช่วยเหลือ)
- แชร์ได้ผ่าน Line (เพื่อนแนะนำกัน)
```

## P.2 Lawyer Persona

### Persona 4: "ทนายรุ่นใหม่" (Young Lawyer, 35)
```
NAME: ทนายสมหมาย รักธรรม
AGE: 35 | LOCATION: กรุงเทพฯ | EXPERIENCE: 12 ปี
PRACTICE: กฎหมายอาญา, แพ่ง, ผู้บริโภค
TECH LEVEL: กลาง-สูง (ใช้ iPad, Line)
PAIN: หาลูกความยาก งานเอกสารเยอะ ตามคดีหลายคดี
MOTIVATION: ได้ลูกความจากแพลตฟอร์ม ลดงานเอกสาร
DEVICE: iPhone + iPad + MacBook

JOURNEY:
1. สมัครเป็นทนายบนแพลตฟอร์ม
2. ยื่นใบอนุญาต + บัตรประชาชน
3. รอ admin ตรวจสอบ (1-2 วัน)
4. ได้รับการยืนยัน → โปรไฟล์ live
5. รับคำปรึกษาจากผู้ใช้ (ผ่านแพลตฟอร์ม)
6. ใช้ case management จัดการคดี
7. สร้างใบแจ้งหนี้ → ลูกความจ่ายผ่านแพลตฟอร์ม
8. ใช้ AI ช่วยร่างเอกสาร → ลดเวลางาน 50%

DESIGN IMPLICATIONS:
- Dashboard เร็ว เห็นทุกคดีในหน้าเดียว
- Case timeline ละเอียด
- Billing ง่าย (สร้าง invoice 1 คลิก)
- AI ช่วยร่างเอกสาร (จุดขายหลัก)
- Mobile-friendly (ทำงานระหว่างเดินทาง)
```

## P.3 Admin Persona

### Persona 5: "ผู้ดูแลแพลตฟอร์ม" (Platform Admin, 30)
```
NAME: คุณอนุชา
AGE: 30 | LOCATION: กรุงเทพฯ | ROLE: Ops Manager
TECH LEVEL: สูง
PAIN: ต้องตรวจทนาย ดูแลผู้ใช้ ดูรายได้ หลายอย่าง
MOTIVATION: แพลตฟอร์มปลอดภัย มีรายได้ โตต่อเนื่อง
DEVICE: MacBook + iPhone

JOURNEY:
1. เช้า: เปิด dashboard ดู metrics + แจ้งเตือน
2. ตรวจทนายที่รอ verification
3. ดูเคสที่ต้องการ escalation
4. ตรวจรายได้ + ธุรกรรม
5. อัปเดตเนื้อหากฎหมาย (มีกฎหมายใหม่)
6. ตอบ ticket ผู้ใช้

DESIGN IMPLICATIONS:
- Overview dashboard ครบในหน้าเดียว
- ตรวจทนายเร็ว (ดูเอกสาร + อนุมัติ 1 คลิก)
- รายได้ real-time
- Content management ง่าย
- Audit log ครบถ้วน
```

---

# SECTION Q: Granular Master Checklist (Acceptance Criteria)

## Q.1 Phase 1: Foundation — Acceptance Criteria

### AUTH
- [ ] **AC-A1**: User can register with email+password in < 60 seconds
- [ ] **AC-A2**: User can login with LINE (1-click, no password)
- [ ] **AC-A3**: Wrong password shows warm error "รหัสผ่านไม่ถูกต้อง ลองอีกครั้งนะ"
- [ ] **AC-A4**: Banned user sees clear reason, not generic error
- [ ] **AC-A5**: Session persists 30 days (refresh token rotation)
- [ ] **AC-A6**: Logout invalidates all sessions on all devices
- [ ] **AC-A7**: Password reset email arrives < 5 minutes
- [ ] **AC-A8**: Admin can force-logout any user
- [ ] **AC-A9**: RBAC blocks lawyer from accessing /admin (403)
- [ ] **AC-A10**: RBAC blocks consumer from accessing /lawyer (403)

### DATABASE
- [ ] **AC-D1**: All tables created with correct constraints
- [ ] **AC-D2**: RLS policies block cross-user data access
- [ ] **AC-D3**: Evidence files only accessible via signed URL
- [ ] **AC-D4**: Case numbers auto-generate (LA-YYYY-NNNN)
- [ ] **AC-D5**: Seed data loads (12 categories, 47 sub-problems, 24 templates)
- [ ] **AC-D6**: Backup restore tested (RTO < 1 hour)
- [ ] **AC-D7**: Migration rollback tested
- [ ] **AC-D8**: Database connections pooled correctly

### AI ENGINE
- [ ] **AC-AI1**: Diagnosis identifies correct category ≥ 90% on eval set
- [ ] **AC-AI2**: Search returns citations (no fabricated sources)
- [ ] **AC-AI3**: Warm tone applied to 100% of AI responses
- [ ] **AC-AI4**: Compound detection catches multi-category cases
- [ ] **AC-AI5**: Fallback model activates on DeepSeek failure
- [ ] **AC-AI6**: Rate limiting prevents abuse
- [ ] **AC-AI7**: Token budget enforced per request
- [ ] **AC-AI8**: AI latency p95 < 5s
- [ ] **AC-AI9**: AI cost tracked per user
- [ ] **AC-AI10**: Prompt injection attempts blocked

## Q.2 Phase 2: Core Pages — Acceptance Criteria

### HOME
- [ ] **AC-H1**: Home loads < 1.5s (LCP)
- [ ] **AC-H2**: Warm greeting with user's name
- [ ] **AC-H3**: AI input box prominent, mobile-friendly
- [ ] **AC-H4**: 6 feature cards all navigate correctly
- [ ] **AC-H5**: Active cases sorted by recency
- [ ] **AC-H6**: Empty state shows strong CTA
- [ ] **AC-H7**: Social proof with real metrics
- [ ] **AC-H8**: Fully responsive (320px - 1440px)

### DIAGNOSIS
- [ ] **AC-DG1**: 4-step wizard completes in < 3 minutes
- [ ] **AC-DG2**: Category-specific questions fire correctly
- [ ] **AC-DG3**: Fear level changes tone + urgency
- [ ] **AC-DG4**: Back navigation preserves data
- [ ] **AC-DG5**: Route to concierge with context
- [ ] **AC-DG6**: All 12 categories reachable
- [ ] **AC-DG7**: Custom text input saved

### CONCIERGE (8 phases)
- [ ] **AC-C1**: Phase 1 detects category + missing info
- [ ] **AC-C2**: Phase 2 shows laws + penalties + warnings
- [ ] **AC-C3**: Phase 3 shows 3 paths + monetization gate
- [ ] **AC-C4**: Gate converts 15-25% (tracked)
- [ ] **AC-C5**: Payment unlocks Phases 4-7 instantly
- [ ] **AC-C6**: Phase 4 court lookup correct for all 928 districts
- [ ] **AC-C7**: Phase 5 checklist matches category
- [ ] **AC-C8**: Phase 6 generates correct documents
- [ ] **AC-C9**: Phase 7 steps have all 7 fields (where/how/who/docs/cost/time/next)
- [ ] **AC-C10**: Phase 8 timeline + Case Plus upsell
- [ ] **AC-C11**: All 47 sub-problems work end-to-end
- [ ] **AC-C12**: Compound cases handled
- [ ] **AC-C13**: Lawyer 10-point checklist included
- [ ] **AC-C14**: Perjury warning included
- [ ] **AC-C15**: Blue-shirt receptionist info included
- [ ] **AC-C16**: Appeals guidance included

### SEARCH
- [ ] **AC-S1**: Search fires on Enter + button
- [ ] **AC-S2**: Results with citations in < 5s
- [ ] **AC-S3**: Related questions shown
- [ ] **AC-S4**: "Start case" from result works
- [ ] **AC-S5**: Empty + error states
- [ ] **AC-S6**: 12 category chips work

### PRICING
- [ ] **AC-P1**: 4 tiers render correctly
- [ ] **AC-P2**: Feature comparison accurate
- [ ] **AC-P3**: Upgrade → Omise checkout
- [ ] **AC-P4**: Current plan highlighted
- [ ] **AC-P5**: FAQ accordion works

### PROFILE
- [ ] **AC-PR1**: Stats correct (cases, documents, savings)
- [ ] **AC-PR2**: Plan badge + upgrade CTA
- [ ] **AC-PR3**: Notification preferences save
- [ ] **AC-PR4**: Data export works (JSON/CSV)
- [ ] **AC-PR5**: Delete account with confirmation + grace period
- [ ] **AC-PR6**: AI consent toggle works

### MARKETING
- [ ] **AC-M1**: Landing page converts (track signup rate)
- [ ] **AC-M2**: /terms exists + linked from signup
- [ ] **AC-M3**: /privacy exists + PDPA-compliant
- [ ] **AC-M4**: All pages responsive
- [ ] **AC-M5**: SEO meta tags complete

## Q.3 Phase 3: Business — Acceptance Criteria

### DOCUMENTS
- [ ] **AC-DC1**: Merge fields replaced correctly ({{field}})
- [ ] **AC-DC2**: Thai dates formatted (พ.ศ.)
- [ ] **AC-DC3**: Export PDF/DOCX/TXT works
- [ ] **AC-DC4**: Watermark on free tier exports
- [ ] **AC-DC5**: 24 templates available
- [ ] **AC-DC6**: Generate from case works
- [ ] **AC-DC7**: Conditional blocks work ({{#if}})

### TAX
- [ ] **AC-T1**: Brackets correct (0-35%)
- [ ] **AC-T2**: All 30+ deductions with limits
- [ ] **AC-T3**: Real-time recalculation
- [ ] **AC-T4**: Savings tracker shows optimized vs current
- [ ] **AC-T5**: AI optimizer suggests valid deductions
- [ ] **AC-T6**: 6-step filing checklist
- [ ] **AC-T7**: Export tax report

### LAWYERS
- [ ] **AC-L1**: Filter by 12 categories, 77 provinces
- [ ] **AC-L2**: Verified badge only on verified lawyers
- [ ] **AC-L3**: Reviews + ratings work
- [ ] **AC-L4**: Hire flow → payment
- [ ] **AC-L5**: Map view (optional)

### PAYMENTS
- [ ] **AC-PY1**: PromptPay QR generates
- [ ] **AC-PY2**: Credit card works (sandbox → prod)
- [ ] **AC-PY3**: Webhook updates status
- [ ] **AC-PY4**: Payment failure → retry
- [ ] **AC-PY5**: Invoice generated
- [ ] **AC-PY6**: Refund works (admin)

### NOTIFICATIONS
- [ ] **AC-N1**: In-app notifications (real-time)
- [ ] **AC-N2**: LINE notifications
- [ ] **AC-N3**: Email notifications
- [ ] **AC-N4**: Unread count badge
- [ ] **AC-N5**: Preferences respected
- [ ] **AC-N6**: Case reminders (Case Plus)

## Q.4 Phase 4: Admin — Acceptance Criteria

- [ ] **AC-AD1**: Overview loads < 2s with real data
- [ ] **AC-AD2**: Charts update on date range change
- [ ] **AC-AD3**: User table paginated + filterable + searchable
- [ ] **AC-AD4**: User detail modal with 4 tabs
- [ ] **AC-AD5**: Ban/unban with confirmation
- [ ] **AC-AD6**: Case table with all filters
- [ ] **AC-AD7**: Case detail with timeline + lawyer assignment
- [ ] **AC-AD8**: Lawyer verification flow (approve/reject/reason)
- [ ] **AC-AD9**: Revenue stats + charts + transactions
- [ ] **AC-AD10**: Refund flow
- [ ] **AC-AD11**: Content CRUD (categories, templates, FAQ)
- [ ] **AC-AD12**: Settings with validation + audit log
- [ ] **AC-AD13**: All admin actions logged (audit trail)

## Q.5 Phase 5: Integration — Acceptance Criteria

- [ ] **AC-I1**: LINE Login works end-to-end
- [ ] **AC-I2**: LINE webhook receives messages
- [ ] **AC-I3**: LINE notifications delivered
- [ ] **AC-I4**: LINE rich menu configured
- [ ] **AC-I5**: Lawyer app dashboard with cases/clients/billing
- [ ] **AC-I6**: Lawyer case CRUD + timeline + AI summary
- [ ] **AC-I7**: Client portal (list, detail, messaging)
- [ ] **AC-I8**: Lawyer billing (invoice create/send/track)
- [ ] **AC-I9**: Lawyer verification flow
- [ ] **AC-I10**: In-app messaging lawyer↔client
- [ ] **AC-I11**: PWA setup (manifest + service worker)
- [ ] **AC-I12**: Mobile fully responsive
- [ ] **AC-I13**: Security headers (CSP, etc.)
- [ ] **AC-I14**: Rate limiting on all API routes
- [ ] **AC-I15**: Penetration test passed

## Q.6 Phase 6: Polish — Acceptance Criteria

- [ ] **AC-PL1**: 100% UI text warm tone
- [ ] **AC-PL2**: WCAG 2.1 AA passed
- [ ] **AC-PL3**: Keyboard navigation works
- [ ] **AC-PL4**: Screen reader tested
- [ ] **AC-PL5**: Color contrast ≥ 4.5:1
- [ ] **AC-PL6**: Lighthouse ≥ 90 performance
- [ ] **AC-PL7**: LCP < 1.5s, TTI < 3s
- [ ] **AC-PL8**: Unit test coverage ≥ 80%
- [ ] **AC-PL9**: All 47 sub-problems tested E2E
- [ ] **AC-PL10**: Payment flow tested (sandbox)
- [ ] **AC-PL11**: Cross-browser tested
- [ ] **AC-PL12**: Mobile tested (iOS + Android)
- [ ] **AC-PL13**: SEO meta + sitemap + robots.txt
- [ ] **AC-PL14**: Analytics tracking live
- [ ] **AC-PL15**: Monitoring + alerting live
- [ ] **AC-PL16**: Backup strategy verified
- [ ] **AC-PL17**: Launch checklist complete
- [ ] **AC-PL18**: Rollback plan documented

---

# SECTION R: Component Inventory

## R.1 UI Components (shadcn/ui based)

### Core (20)
```
button, card, input, textarea, select, checkbox, radio-group,
dialog, sheet, dropdown-menu, tabs, accordion, tooltip, badge,
avatar, table, progress, skeleton, separator, toast
```

### Specialized (30)
```
| Component | Purpose |
|-----------|---------|
| phase-stepper | 8-phase concierge progress |
| phase-container | Phase wrapper with content |
| monetization-gate | ฿299 gate card |
| fear-indicator | Fear level badge |
| urgency-badge | Urgency level indicator |
| compound-banner | Multi-category detection |
| law-card | Law + section + penalty display |
| warning-box | Safety-critical warnings |
| info-box | Court/mediation info |
| checklist-item | Document checklist with upload |
| readiness-bar | Document readiness progress |
| evidence-uploader | Drag-drop file upload |
| document-preview | Generated document viewer |
| merge-form | {{field}} input form |
| export-button | PDF/DOCX/TXT export |
| tax-bracket-sidebar | Tax bracket visualization |
| deduction-chip | Toggleable deduction |
| savings-tracker | Tax savings comparison |
| filing-checklist | 6-step tax filing |
| lawyer-card | Lawyer marketplace card |
| lawyer-filter | Multi-filter panel |
| review-list | Lawyer reviews |
| hire-dialog | Hire confirmation |
| verified-badge | Lawyer verification badge |
| pricing-card | 4-tier pricing |
| checkout-dialog | Omise payment modal |
| notification-bell | Unread count + dropdown |
| notification-item | Individual notification |
| stat-card | Admin stat with trend |
| data-table | Paginated/filterable table |
```

## R.2 Legal Domain Modules

```
| Module | Purpose | Key Functions |
|--------|---------|---------------|
| categories.ts | 12 category definitions | getCategory, listCategories |
| diagnosis-config.ts | 47 sub-problem configs | getSubProblem, getQuestions |
| sources.ts | Legal source registry | validateSource, getLaws |
| fear-calibration.ts | 4 fear levels | calibrateFear, getTone |
| compound-detection.ts | Multi-category | detectCompound, getDependency |
| guardrails.ts | 7 MUST-NEVER rules | enforceGuardrails |
| drive-detection.ts | 22 human drives | detectDrives, driveAwareContext |
| social-proof.ts | Platform metrics | getMetrics, getCategoryStats |
| warm-tone.ts | Tone calibration | applyWarmTone, getOpeningPhrase |
```

## R.3 Feature Flags
```
| Flag | Default | Purpose |
|------|---------|---------|
| ENABLE_LINE_LOGIN | true | LINE Login toggle |
| ENABLE_AI_SEARCH | true | AI search feature |
| ENABLE_COMPOUND | true | Compound case detection |
| ENABLE_LAWYER_MARKETPLACE | true | Lawyer marketplace |
| ENABLE_TAX_OPTIMIZER | false | Tax optimizer (launch later) |
| ENABLE_SME_PLAN | false | SME tier (phase 2) |
| ENABLE_CASE_PLUS | true | Case Plus tier |
| ENABLE_PUSH | false | Web push notifications |
| ENABLE_BETA_BADGE | false | Show beta badges |
| FORCE_MAINTENANCE | false | Maintenance mode |
```

---

# SECTION S: Product Roadmap

## S.1 Release Timeline

### v0.1 — MVP (Month 1-3)
```
SCOPE: Foundation + Core Pages
- Auth (email + LINE)
- Diagnosis (12 categories)
- Concierge (8 phases, online_fraud + labour first)
- Search (AI)
- Documents (10 templates)
- Pricing + Payment (฿299)
- Admin (basic: users, cases, revenue)

GOAL: 100 beta users, validate ฿299 conversion
```

### v0.2 — Full Concierge (Month 3-5)
```
SCOPE: All 47 sub-problems
- All 12 categories in concierge
- Compound case handling
- Tax calculator
- Lawyer marketplace (listing only)
- Case Plus (฿999)

GOAL: 1,000 users, 20% gate conversion
```

### v0.3 — Lawyer App (Month 5-7)
```
SCOPE: Two-sided platform
- Lawyer dashboard + case management
- Client portal
- Billing + invoices
- Lawyer verification
- LINE notifications

GOAL: 50 verified lawyers, first hires
```

### v1.0 — Launch (Month 7-9)
```
SCOPE: Production ready
- Full admin dashboard
- Analytics + monitoring
- SME tier
- Polish (tone, accessibility, testing)

GOAL: Public launch, 5,000 users
```

### v1.1+ — Growth (Month 9+)
```
- Tax optimizer (advanced)
- SME documents + corporate tax
- API access
- Lawyer analytics
- Mobile app (React Native)
- AI-powered case prediction (careful — no outcome promises)
```

## S.2 Team & Resourcing (Recommended)

```
| Role | FTE | Focus |
|------|-----|-------|
| Full-stack Engineer | 2 | Next.js + Supabase + AI integration |
| Frontend Engineer | 1 | UI/UX, warm tone, accessibility |
| Backend/DevOps | 1 | APIs, security, CI/CD, infra |
| Product Designer | 1 | UX flows, design system, empathy |
| Legal Content Lead | 1 | Legal accuracy, content, lawyer network |
| QA Engineer | 1 | Testing, 47 sub-problem validation |
| Data/AI Engineer | 0.5 | AI quality, evals, cost optimization |
| **Total** | **7.5** | |
```

---

# SECTION T: Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| 1 | AI gives wrong legal info | High | High | Guardrails, source registry, lawyer review, disclaimers, no-outcome-promise rule |
| 2 | Data breach (sensitive case data) | Low | Critical | RLS, encryption, PDPA compliance, security audit, pen test |
| 3 | DeepSeek API outage | Medium | High | Fallback model (Claude), retry logic, cached responses |
| 4 | Payment fraud/chargebacks | Medium | Medium | Omise fraud detection, transaction monitoring |
| 5 | Low gate conversion (< 10%) | Medium | High | A/B test price/copy, free trial, anchor pricing |
| 6 | Lawyer verification fraud | Medium | High | Manual review, bar number validation, document checks |
| 7 | Legal liability (user misuses advice) | Medium | High | Disclaimers, "not legal advice" labeling, ToS, insurance |
| 8 | Competitor launches similar | Medium | Medium | Speed, warm tone differentiation, lawyer network moat |
| 9 | Regulatory change (Thai law) | Low | Medium | Content update pipeline, lawyer network for review |
| 10 | Scope creep (feature bloat) | High | Medium | MVP discipline, feature flags, roadmap review |
| 11 | AI cost overruns | Medium | Medium | Token budgets, caching, rate limits, tiered access |
| 12 | Low Thai content quality | Medium | High | Native Thai lawyers review, warm tone guidelines, QA |

---

# SECTION U: Launch Runbook

## U.1 Pre-Launch (T-2 weeks)
- [ ] Freeze feature scope (no new features)
- [ ] Complete all 47 sub-problems testing
- [ ] Legal review of all content (lawyer sign-off)
- [ ] PDPA compliance audit
- [ ] Security audit + pen test
- [ ] Load test (1,000 concurrent users)
- [ ] Payment flow sandbox test
- [ ] LINE integration test
- [ ] Analytics + monitoring verified
- [ ] Backup + rollback plan tested
- [ ] Customer support channel ready (LINE + email)

## U.2 Launch Day (T-0)
- [ ] Deploy to production
- [ ] Verify SSL + DNS
- [ ] Smoke test all critical flows
- [ ] Monitor error rates (Sentry)
- [ ] Monitor AI latency + cost
- [ ] Monitor payment webhooks
- [ ] Social media announcement
- [ ] Press release distribution
- [ ] LINE broadcast to waitlist

## U.3 Post-Launch (T+1 week)
- [ ] Daily monitoring review
- [ ] Fix P0 bugs immediately
- [ ] Collect user feedback (survey + reviews)
- [ ] Track funnel metrics (gate conversion)
- [ ] A/B test pricing/copy
- [ ] Weekly iteration cycle

## U.4 Launch Metrics (Success Criteria)
```
| Metric | Week 1 | Month 1 | Month 3 |
|--------|--------|---------|---------|
| Users | 500 | 2,000 | 5,000 |
| Paying users | 50 | 300 | 750 |
| Gate conversion | 15% | 18% | 20% |
| Case completion | 40% | 50% | 60% |
| NPS | 40 | 45 | 50 |
| AI accuracy | 85% | 88% | 90% |
| Uptime | 99.5% | 99.7% | 99.9% |
```

---

# SECTION V: Warm Tone Copy Samples (Actual Thai)

## V.1 Empathy Openings
```
😔 เราเข้าใจความรู้สึกของคุณนะ เรื่องแบบนี้มันเครียดจริงๆ
    แต่ไม่ต้องห่วง — เราจะช่วยคุณทีละขั้น

😔 ถูกหลอกแบบนี้มันเสียความรู้สึกมาก เราเข้าใจ
    และข่าวดีคือ เรื่องนี้มีทางแก้ — คุณไม่ได้สู้คนเดียว

😔 การถูกเลิกจ้างเป็นเรื่องที่เจ็บปวด อยู่ดีๆ ก็ไม่มีรายได้
    เราเข้าใจนะ และคุณมีสิทธิที่ควรได้ — มาดูกันว่าคุณได้อะไรบ้าง
```

## V.2 Reassurance
```
💪 ข่าวดี — เรื่องนี้แก้ได้ และคุณมีสิทธิเต็มที่!
    กฎหมายอยู่ข้างคุณ

💪 คุณไม่ได้อยู่คนเดียว เราเคยช่วยคนที่เจอแบบนี้มาแล้วหลายเคส
    และส่วนใหญ่จัดการเองได้สำเร็จ

💪 ไม่ต้องทำทุกอย่างวันเดียว ค่อยๆ ทำทีละขั้น
    เราเดินไปด้วยกัน
```

## V.3 Empowerment
```
✅ คุณทำได้! เริ่มจากขั้นแรกง่ายๆ ก่อน
    ใช้เวลาแค่ 20-30 นาที

✅ คนส่วนใหญ่เลือกจัดการเอง — 80% ทำสำเร็จ
    และเราจะอยู่ตรงนี้ตลอดทาง

✅ ทีละขั้น ทีละนิด เดี๋ยวก็เสร็จ
    มาลองขั้นแรกกัน
```

## V.4 Legal Information (Plain Thai)
```
📜 แปลเป็นภาษาง่ายๆ: กฎหมายบอกว่า การหลอกเอาทรัพย์คนอื่น
    ผ่านการโพสต์ขายของปลอม มีโทษจำคุกไม่เกิน 5 ปี

📜 พูดง่ายๆ คือ: คุณมีสิทธิได้เงินคืน + ดอกเบี้ย 7.5% ต่อปี
    และสามารถฟ้องได้เอง ไม่ต้องจ้างทนาย

📜 ถ้าเทียบกับชีวิตจริง: มันเหมือนคุณซื้อของแล้วเขาไม่ส่ง
    กฎหมายถือว่าเขาผิดสัญญา — คุณฟ้องได้
```

## V.5 Monetization Gate
```
🤔 ถึงตรงนี้คุณรู้แล้วว่า: ฟ้องอะไรได้ + สิทธิอะไร + เลือกทางไหน

แต่... ต้องไปศาลไหน? ต้องใช้เอกสารอะไร?
ต้องเขียนคำฟ้องยังไง? เดินเข้าไปในศาลต้องพูดอะไร?

💡 แค่ ฿299 — เราบอกคุณทุกขั้นตอนจนจบ
    (ถูกกว่าจ้างทนาย 98% — ทนายคิด 10,000-30,000)

    ≈ ค่ากาแฟ 2 แก้ว แลกกับการรู้ทุกขั้นตอนที่ถูกต้อง
```

## V.6 Error Messages (Warm)
```
🙏 ขอโทษด้วยนะ ระบบของเรามีปัญหาชั่วคราว
    ลองอีกครั้งในสักครู่ หรือทักหาเราที่ LINE @chujai ได้เลย

🙏 ยังไม่ได้รับการยืนยันการชำระเงิน
    ถ้าคุณจ่ายแล้ว กรุณารอ 1-2 นาที แล้วรีเฟรชหน้านี้

🙏 อัปโหลดไม่สำเร็จ — ไฟล์ใหญ่เกินไป (สูงสุด 10MB)
    ลองบีบอัดไฟล์หรือถ่ายใหม่ให้ชัดๆ นะ
```

## V.7 Court Filing (Warm but Professional)
```
🏛️ เมื่อถึงศาล: มองหาพนักงานต้อนรับเสื้อฟ้า!
    เขาจะเดินเข้ามาถามคุณเอง — บอกเลยว่ามาทำอะไร
    เขาจะพาไปถูกเคาน์เตอร์ ไม่ต้องหลง

🙏 เวลาพูดกับผู้พิพากษา: เรียก "ท่านครับ" หรือ "ท่านค่ะ"
    ต้องยืนพูด ห้ามนั่งพูด — และแต่งตัวสุภาพนะ
```

## V.8 Lawyer Hiring (Trust + Warm)
```
👨⚖️ ก่อนจ้างทนาย — ตรวจ 10 อย่างนี้ให้ชัวร์:
    1. ขอดูใบอนุญาตทนายความ
    2. ถามค่าทนายทั้งหมด — อย่าอายที่จะถาม!
    3. ขอทำ "หนังสือสัญญาว่าความ"
    ... (ครบ 10 ข้อใน Phase 3)

💡 ทิป: อย่าวางใจ 100% — ติดตามคดีด้วยตัวเองสม่ำเสมอ
    เพราะผลคดีตกที่คุณ
```

---

# SECTION W: Summary & Key Decisions

## W.1 Critical Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Framework | Next.js 15 + Supabase | Type-safe, real-time, fast MVP |
| AI | DeepSeek V3 | Best Thai + cost-effective |
| Messaging | LINE | Thai standard, lawyer+user already on it |
| Payment | Omise + PromptPay | Thai gateway, PromptPay universal |
| Monetization | Freemium + gate at Phase 3 | Curiosity peak, anchor pricing |
| Tone | Warm empathetic | Core brand differentiator |
| Compound handling | Built-in at Phase 1 | Real cases span categories |
| Pricing | 4 tiers (Free/299/999/2990) | Proven Thai SaaS structure |

## W.2 North Star Metric
```
NORTH STAR: Successful case resolutions
  = Users who reach Phase 7 (filed) or Phase 8 (follow-up)
  → Measures actual value delivered, not just engagement
```

## W.3 Anti-Goals (What we DON'T build in MVP)
```
❌ No outcome prediction ("คุณชนะ 80%") — legal/ethical risk
❌ No lawyer ranking (show data, don't recommend)
❌ No court filing on user's behalf
❌ No auto-legal-advice without human review
❌ No crypto/NFT integrations
❌ No English UI (Thai-first, English later)
❌ No mobile native app (web PWA first)
```

---

*End of Chujai Legal Master Design Document — Complete*


---

# SECTION X: Detailed Admin & Lawyer App Page Flows (Granular)

## X.1 Admin Overview — Component-by-Component

### Stat Card Component
```
┌────────────────────┐
│ Total Users        │
│ 8,421              │
│ ↑12.4% vs last mo  │
│ [sparkline]        │
└────────────────────┘

DATA SOURCES:
- Total Users: SELECT COUNT(*) FROM users
- Trend: compare current month vs previous
- Sparkline: 30-day daily active

STATES:
- Loading: skeleton shimmer
- Error: "โหลดไม่สำเร็จ" + retry
- Empty: "ยังไม่มีข้อมูล"
```

### Revenue Chart Component
```
TYPE: Line chart (Recharts)
DATA: daily revenue, 30 days
INTERACTIONS:
- Hover → tooltip with exact value
- Click date range → 7/30/90/365 days
- Toggle: revenue vs users (dual axis)
```

### Category Pie Chart
```
TYPE: Pie chart (Recharts)
DATA: case count by category (12 slices)
INTERACTIONS:
- Hover → count + percentage
- Click slice → navigate to /admin/cases?category=X
- Legend toggle (show/hide category)
```

### Recent Activity Feed
```
TYPE: Realtime list (Supabase subscription)
DATA: latest 20 events
FORMAT: [icon] [description] [relative time]
ICONS: 👤 user, 📂 case, 💰 payment, ⚖️ lawyer, 🤖 AI
AUTO-REFRESH: real-time via Supabase channels
```

## X.2 Admin Users — Data Table Spec

### Columns
```
| Column | Type | Sortable | Filterable |
|--------|------|----------|------------|
| Avatar + Name | component | ✅ name | ✅ search |
| Email | text | ✅ | ✅ search |
| Phone | text | ✅ | ✅ search |
| Role | badge | ✅ | ✅ dropdown |
| Plan | badge | ✅ | ✅ dropdown |
| Status | badge | ✅ | ✅ dropdown |
| Joined | date | ✅ | ❌ |
| Last Active | date | ✅ | ❌ |
| Actions | dropdown | ❌ | ❌ |
```

### Pagination
```
PAGE SIZE: 25 (configurable: 10/25/50/100)
CONTROLS: [← prev] [1 2 3 ... 337] [next →]
INFO: "Showing 1-25 of 8,421 users"
```

### User Detail Modal Tabs
```
TAB 1: Profile
  - Avatar, name, email, phone
  - Role selector (consumer/lawyer/admin)
  - Plan selector (free/action_pack/case_plus/sme_starter)
  - Status (active/inactive/banned)
  - Joined date, last active
  - LINE user ID (if linked)

TAB 2: Cases
  - Table: case number, category, status, created
  - Click case → navigate to /admin/cases/[caseId]

TAB 3: Payments
  - Table: transaction, plan, amount, method, date, status
  - Total spent

TAB 4: Activity
  - Audit log: action, entity, timestamp, IP
```

## X.3 Admin Lawyer Verification — Detail Spec

### Verification Checklist (what admin checks)
```
- [ ] Bar number format valid (NNNNN/BBBB)
- [ ] License image clear + not expired
- [ ] ID card matches name
- [ ] Specialization categories valid
- [ ] Contact info complete
- [ ] Profile photo appropriate
```

### Approval Actions
```
APPROVE:
1. Click "✓ Approve"
2. Confirm dialog: "อนุมัติทนายสมหมาย รักธรรม?"
3. Status → verified
4. Welcome email + LINE notification
5. Profile goes live on /lawyers

REJECT:
1. Click "✗ Reject"
2. Rejection reason (required, min 10 chars)
3. Status → rejected
4. Notification with reason
5. Lawyer can reapply after fixing

REQUEST MORE INFO:
1. Click "↩ Request Info"
2. Specify what's missing
3. Status → pending (with note)
4. Notification sent
```

## X.4 Admin Revenue — Detail Spec

### Revenue Calculations
```
MRR = Σ (monthly recurring plan fees)
    + (one-time purchases ÷ 12, amortized)
ARR = MRR × 12
Today = Σ (payments today)
This Month = Σ (payments this month)

NOTE: For Chujai's mostly one-time model (฿299/฿999):
  MRR = (Σ one-time revenue ÷ 3-month trailing window)
  This smooths lumpy one-time revenue
```

### Transaction Table Columns
```
| Column | Type |
|--------|------|
| Transaction ID | text (TXN-YYYY-NNNN) |
| User | avatar + name |
| Plan | badge |
| Amount | currency (฿, satang → baht) |
| Method | badge (PromptPay/Credit) |
| Date | datetime |
| Status | badge (paid/failed/refunded) |
```

### Refund Flow
```
1. Click refund on transaction
2. Confirm dialog: "คืนเงิน ฿299 ให้ผู้ใช้?"
3. Call Omise refund API
4. Status → refunded
5. User notified
6. Audit log entry
```

## X.5 Lawyer Dashboard — Detail Spec

### Layout
```
┌──────────────────────────────────────────────────────────┐
│  👨⚖️ ทนายสมหมาย                     [🔔] [👤]           │
├──────────────────────────────────────────────────────────┤
│  Sidebar:                                                │
│  • 📊 Dashboard                                          │
│  • 📂 เคสของฉัน                                          │
│  • 👥 ลูกความ                                            │
│  • 💰 การเรียกเก็บเงิน                                    │
│  • 📄 เอกสาร                                             │
│  • 📈 วิเคราะห์                                          │
│  • ⚙️ ตั้งค่า                                            │
├──────────────────────────────────────────────────────────┤
│  📊 Dashboard                                            │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐          │
│  │เคสที่    │ │ลูกความ  │ │รายได้   │ │เคสใหม่  │          │
│  │ดำเนินอยู่ │ │ทั้งหมด   │ │เดือนนี้ │ │สัปดาห์นี้│          │
│  │  12     │ │  47     │ │฿45,000 │ │   3     │          │
│  └────────┘ └────────┘ └────────┘ └────────┘          │
│                                                          │
│  📅 กำหนดการที่ใกล้ถึง:                                     │
│  • ศาลนัด 14/08/26 — คดี LA-2026-0892                    │
│  • เอกสารครบกำหนด 16/08/26 — คดี LA-2026-0877            │
│                                                          │
│  📋 เคสล่าสุด:                                             │
│  [case rows...]                                          │
└──────────────────────────────────────────────────────────┘
```

### Case Detail (Lawyer View)
```
┌──────────────────────────────────────────────────────────┐
│  📂 LA-2026-0892 — ซื้อของออนไลน์ไม่ได้ของ                  │
│  ลูกความ: สมชาย ใจดี | 🟡 Active | Priority: High          │
├──────────────────────────────────────────────────────────┤
│  Tabs: [📋 ภาพรวม] [📅 ไทม์ไลน์] [📄 เอกสาร] [💬 แชท] [💰 บิล]│
│                                                          │
│  📋 ภาพรวม:                                               │
│  • ประเภท: online_fraud / ฉ้อโกง                            │
│  • สรุปโดย AI: "ผู้ใช้สั่งของ Shopee 3,500 บาท ไม่ส่งของ..." │
│  • หลักฐาน: 5/7 รายการอัปโหลดแล้ว                          │
│  • เฟสที่ดำเนินถึง: 4/8                                    │
│                                                          │
│  [อัปเดตสถานะ] [เพิ่มหมายเหตุ] [สร้างเอกสาร]                 │
└──────────────────────────────────────────────────────────┘
```

### Client Portal (Lawyer → Client)
```
MESSAGING: lawyer ↔ client (real-time)
DOCUMENT SHARING: lawyer shares drafts with client for review
CASE STATUS: both see same timeline
BILLING: lawyer creates invoice → client sees + pays via platform
```

### Billing Form (Lawyer)
```
FIELDS:
- Client selector
- Invoice number (auto)
- Line items (description, amount) — dynamic
- Due date
- Notes

THAI INVOICE FORMAT:
- ชื่อทนาย + เลขที่ใบอนุญาต
- ที่อยู่สำนักงาน
- เลขประจำตัวผู้เสียภาษี
- รายการ + จำนวนเงิน
- ภาษีมูลค่าเพิ่ม (ถ้ามี VAT)
- ยอดรวม
```

---

# SECTION Y: Database Detail (Indexes, Constraints, Relations)

## Y.1 Indexes
```
users:
  - UNIQUE INDEX on email
  - INDEX on role
  - INDEX on plan
  - INDEX on created_at (desc)

cases:
  - UNIQUE INDEX on case_number
  - INDEX on user_id
  - INDEX on category
  - INDEX on status
  - INDEX on created_at (desc)
  - INDEX on assigned_lawyer_id
  - COMPOSITE INDEX (user_id, status)

case_phases:
  - UNIQUE INDEX (case_id, phase_number)
  - INDEX on case_id

documents:
  - INDEX on user_id
  - INDEX on case_id
  - INDEX on type

evidence:
  - INDEX on case_id
  - COMPOSITE INDEX (case_id, document_checklist_id)

payments:
  - UNIQUE INDEX on omise_charge_id
  - INDEX on user_id
  - INDEX on status
  - INDEX on created_at (desc)

notifications:
  - INDEX on user_id
  - INDEX on is_read
  - COMPOSITE INDEX (user_id, is_read)

lawyer_profiles:
  - UNIQUE INDEX on bar_number
  - UNIQUE INDEX on user_id
  - INDEX on verification_status
  - INDEX on province
  - INDEX on specialization (GIN, array)

lawyer_reviews:
  - UNIQUE INDEX (lawyer_id, user_id, case_id)
  - INDEX on lawyer_id

audit_logs:
  - INDEX on user_id
  - INDEX on entity_type
  - INDEX on created_at (desc)
```

## Y.2 Constraints
```
cases:
  - CHECK (current_phase BETWEEN 1 AND 8)
  - CHECK (status IN ('active','pending','closed','archived'))
  - FK user_id → users ON DELETE CASCADE

payments:
  - CHECK (amount > 0)
  - FK user_id → users

lawyer_reviews:
  - CHECK (rating BETWEEN 1 AND 5)
  - FK lawyer_id, user_id, case_id

documents:
  - FK case_id → cases ON DELETE SET NULL
```

## Y.3 Triggers
```
TRIGGER 1: update_cases_updated_at
  → auto-update updated_at on any case change

TRIGGER 2: generate_case_number
  → auto-generate LA-YYYY-NNNN on insert

TRIGGER 3: update_lawyer_rating
  → recalculate average_rating + review_count on review insert/update/delete

TRIGGER 4: audit_admin_actions
  → log all admin mutations to audit_logs
```

## Y.4 Views
```
VIEW v_revenue_daily:
  → daily revenue aggregation for charts

VIEW v_cases_by_category:
  → case count + avg resolution time by category

VIEW v_lawyer_workload:
  → active cases per lawyer
```

---

# SECTION Z: Complete Reference Flow (Fully Rendered Example)

## Z.1 Full Concierge — "ซื้อของออนไลน์ไม่ได้ของ" (online_fraud 1.1)

This is the COMPLETE reference implementation showing every phase, every question, every AI response, and every checklist — the gold standard for all 47 flows.

### PHASE 1: UNDERSTAND (🆓 Free)

```
USER INPUT: "สั่งรองเท้าใน Shopee 3,500 บาท ร้านไม่ส่งของแล้วบล็อกเรา"

AI PROCESSING:
1. Parse narrative → detect category online_fraud
2. Detect sub-problem → 1.1 ซื้อของออนไลน์ไม่ได้ของ
3. Check compound → false (single category)
4. Detect missing info → seller name, transfer date, bank account

AI RESPONSE:
😔 เราเข้าใจความรู้สึกของคุณนะ ถูกหลอกแบบนี้มันเสียความรู้สึกมาก

จากที่คุณเล่า เราพบว่าเรื่องนี้เกี่ยวข้องกับ:
1. 💰 ฉ้อโกง — สั่งของแล้วไม่ส่ง
2. 🌐 พ.ร.บ.คอมพิวเตอร์ ม.14(1) — หลอกลวงทางออนไลน์

📋 สิ่งที่เรารู้:
• สั่งรองเท้าออนไลน์ — โอนเงินแล้ว 3,500 บาท
• ผู้ขายไม่ส่งของ / บล็อก
• แพลตฟอร์ม: Shopee

ข้อมูลยังขาด (ช่วยเติมให้ครบหน่อย):
• 👤 ชื่อผู้ขาย: [_______]
• ⏰ วันที่โอน: [_______]
• 🏦 เลขบัญชีผู้ขาย: [_______]

💪 ข่าวดี: เรื่องนี้แก้ได้ — และคุณมีสิทธิเต็มที่!

[เริ่มวิเคราะห์ →]
```

### PHASE 2: ANALYZE RIGHTS (🆓 Free)

```
AI RESPONSE:
🛡️ ข่าวดี — คุณมีสิทธิ์เต็มที่และกฎหมายอยู่ข้างคุณ!

⚖️ สิทธิของคุณ:
• ได้เงินคืนเต็มจำนวน + ดอกเบี้ย 7.5% ต่อปี
• แจ้งความดำเนินคดีอาญาได้
• ฟ้องคดีผู้บริโภคได้ (ไม่ต้องมีทนาย)

📜 กฎหมายที่เกี่ยวข้อง:
✓ ป.อาญา ม.341 — ฉ้อโกง
  • หลอกให้ส่งมอบทรัพย์สิน → จำคุกไม่เกิน 3 ปี ปรับ 60,000
✓ พ.ร.บ.คอมพิวเตอร์ ม.14(1) — นำเข้าข้อมูลเท็จ
  • โพสต์หลอกขาย → จำคุกไม่เกิน 5 ปี ปรับ 100,000
✓ ป.พ.พ. — ผิดสัญญาซื้อขาย
  • โอนเงินแล้วไม่ส่ง = ผิดสัญญา → เรียกเงินคืน + ดอกเบี้ย 7.5%

✅ คุณจัดการเองได้:
• แจ้งความออนไลน์ — thaipoliceonline.go.th
• แจ้งแพลตฟอร์ม — ขอข้อมูลผู้ขาย + ระงับบัญชี
• ตรวจสอบเลขบัญชี — blacklistseller.com
• แจ้ง ปปง. — ถ้าเป็นขบวนการ

🚨 คำเตือนสำคัญ: ห้ามเบิกความเท็จ (ป.อาญา ม.177)
   โทษจำคุก ≤ 5 ปี / ปรับ ≤ 10,000 บาท

⚠️ อย่าเพิ่ง:
• ลบแชท — หลักฐานสำคัญที่สุด!
• รอนาน — อายุความฉ้อโกง 3 เดือน!

⚡ ความเร่งด่วน: สูง
⏰ อายุความ: 3 เดือน (ต้องแจ้งความให้ทัน!)
```

### PHASE 3: CHOOSE PATH (🆓 Free)

```
AI RESPONSE:
🛤️ คุณอยากจัดการแบบไหน? เลือกที่คุณสบายใจ

🅰️ จัดการเอง (ฟรี — ฿0-200)
   ✓ แจ้งความออนไลน์
   ✓ แจ้งแพลตฟอร์ม
   ✓ ตรวจเลขบัญชี
   👉 80% ทำสำเร็จด้วยตัวเอง

🅱️ ให้ทนายจัดการ (฿10,000-20,000)
   ✓ ทนายจัดการทั้งหมด
   ✓ เหมาะกับมูลค่าสูง 50,000+

🅲️ ทวงถามก่อน (ฟรี)
   ✓ ส่งจดหมายทวงถาม (AI สร้างให้)
   ✓ ให้เวลา 7 วัน
   ⚠️ ถ้าไม่ตอบ → กลับไปใช้ A หรือ B

⚠️ ก่อนจ้างทนาย — 10 สิ่งที่ต้องตรวจสอบ: [10-item checklist]

📚 การไกล่เกลี่ยฟรี: [4 benefits + ศูนย์ไกล่เกลี่ย]

[เลือก 🅰️] [เลือก 🅱️] [เลือก 🅲️]
```

### MONETIZATION GATE (after path selection)

```
🆓 ถึงตรงนี้คุณรู้แล้วว่า:
✅ ฟ้องอะไรได้ — ข้อหา + โทษ
✅ สิทธิของคุณ — ครบทุกด้าน
✅ เลือกแนวทางแล้ว — จัดการเอง

🤔 แต่... ต้องไปศาลไหน? ใช้เอกสารอะไร?
   เขียนคำฟ้องยังไง? เดินเข้าไปในศาลต้องพูดอะไร?

💡 แค่ ฿299 — บอกคุณทุกขั้นตอนจนจบ
   (ถูกกว่าจ้างทนาย 98%)

[📦 Action Pack — ฿299 → เริ่มเลย]
[🎁 ทดลอง 1 เอกสารฟรีก่อน]
```

### PHASE 4: JURISDICTION (🔒 ฿299)

```
📍 คุณอยู่ที่ไหน?
[ที่อยู่ปัจจุบัน] [ตามบัตรประชาชน] [ที่เกิดเหตุ]
🏠 สมมติ: อ.เมือง จ.ขอนแก่น

🏛️ สถานีตำรวจ: สภ.เมืองขอนแก่น
   123 ถ.กลางเมือง | 📞 043-123456

🏛️ ศาล: ศาลจังหวัดขอนแก่น
   456 ถ.ศาล | 📞 043-789012

🌐 หรือแจ้งออนไลน์: thaipoliceonline.go.th
💡 เหมาะมาก — หลักฐานเป็นดิจิทัล

🔵 พนักงานต้อนรับเสื้อฟ้า: [info box]
📚 ศาลไทยโครงสร้าง: [taxonomy box]
```

### PHASE 5: DOCUMENTS (🔒 ฿299)

```
📄 เอกสารที่ต้องเตรียม (7 รายการ):
☐ 1. บัตรประชาชน
☐ 2. สลิปโอนเงิน (screenshot)
☐ 3. แคปแชทซื้อขายทั้งหมด
☐ 4. แคปโปรไฟล์ผู้ขาย
☐ 5. แคปโพสต์ขายของ
☐ 6. เลขบัญชีผู้ขาย
☐ 7. Statement ธนาคาร

📊 ความพร้อม: ●●○○○○○○○○ 20% (2/7 มี)
• ยังขาด: สลิป, แคปโปรไฟล์, Statement, เลขบัญชี, แคปโพสต์

[📤 อัปโหลดหลักฐาน]
```

### PHASE 6: PREPARE (🔒 ฿299)

```
🔧 AI กำลังสร้างเอกสารให้คุณ...

📄 กำลังสร้าง:
✓ บันทึกแจ้งความ (2 ข้อหา)
✓ คำร้องขอเปิดเผยข้อมูลเจ้าของบัญชี
✓ จดหมายทวงถาม
✓ ฟ้องคดีผู้บริโภค (พร้อมดอกเบี้ย 7.5%)
✓ คำร้องขออายัดบัญชี

🤖 AI ตรวจพบสิ่งที่ขาด:
⚠️ ไม่มีเลขบัญชีผู้ขาย — จำเป็นมาก
⚠️ ยังไม่แจ้งแพลตฟอร์ม
⚠️ ตรวจ blacklistseller.com

[📥 ดาวน์โหลดทั้งหมด] [📤 อัปโหลดเพิ่ม]
```

### PHASE 7: FILE (🔒 ฿299)

```
🏛️ ขั้นตอนการแจ้งความ (ออนไลน์):

STEP 1: เข้า thaipoliceonline.go.th
  WHERE: เว็บไซต์ตำรวจ
  HOW: เลือก "แจ้งความคดีอาญา" → กรอกข้อมูล
  WHO: คุณเอง
  DOCS: สลิป, แคปแชท, โปรไฟล์ผู้ขาย
  COST: ฟรี
  TIME: 20-30 นาที
  NEXT: ได้เลขคดี

STEP 2: ระบุข้อหา
  ข้อหา 1: ป.อาญา ม.341 (ฉ้อโกง)
  ข้อหา 2: พ.ร.บ.คอมพ์ ม.14(1)

STEP 3: รับเอกสาร
  • หมายเลขคดี
  • ใบแจ้งความ
  • ตำรวจติดต่อกลับ 7-14 วัน

🏛️ ข้อควรรู้เมื่อไปศาล: [behavior box]
🏛️ มารยาทในห้องพิจารณา: [etiquette box]
```

### PHASE 8: FOLLOW-UP (🔒 ฿999 Case Plus)

```
📊 Timeline — คดีของคุณ:
✅ วันนี้ — แจ้งความออนไลน์ + แจ้งแพลตฟอร์ม
✅ +1 วัน — แพลตฟอร์มระงับบัญชี
⏳ +7-14 วัน — ตำรวจติดต่อกลับ
⏳ +30 วัน — ธนาคารให้ข้อมูลเจ้าของบัญชี
⏳ +1-3 เดือน — ตำรวจเรียกผู้ขายสอบปากคำ
⏳ +3-6 เดือน — อัยการฟ้องศาล
⏳ +6-12 เดือน — ศาลพิพากษา

📞 ใครจะติดต่อคุณ:
• พนักงานสอบสวน — ความคืบหน้า
• แพลตฟอร์ม — ผลตรวจสอบ
• อัยการ — นัดศาล

📊 คดี: LA-2569-0XXX | 🟡 กำลังดำเนินการ

⭐ Case Plus — ฿999
✓ ติดตามคดีอัตโนมัติ
✓ แจ้งเตือนทุกกำหนด
✓ ปรึกษาทนาย 3 ครั้ง
[อัปเกรด]

⚖️ อุทธรณ์/ฎีกา: [guidance box]
```

---

# SECTION AA: Implementation Order (Sprint Plan)

## AA.1 Sprint Breakdown (2-week sprints)

```
SPRINT 1 (Foundation): Project setup, auth, DB schema, AI client
SPRINT 2 (Foundation): AI pipelines (diagnosis, search), guardrails
SPRINT 3 (Core): Home, Diagnosis wizard, Concierge Phase 1-3
SPRINT 4 (Core): Monetization gate, Payment, Concierge Phase 4-7
SPRINT 5 (Core): Concierge Phase 8, Search page, Pricing
SPRINT 6 (Core): Profile, Documents (basic), Marketing pages
SPRINT 7 (Business): Documents (full), Tax calculator
SPRINT 8 (Business): Lawyer marketplace, Notifications
SPRINT 9 (Admin): Overview, Users, Cases
SPRINT 10 (Admin): Lawyers verification, Revenue, Content, Settings
SPRINT 11 (Integration): LINE, Lawyer app (dashboard, cases, clients)
SPRINT 12 (Integration): Lawyer billing, verification, messaging
SPRINT 13 (Polish): Tone audit, accessibility, performance
SPRINT 14 (Polish): Testing (all 47 flows), security, launch prep
```

## AA.2 Dependency Map
```
Foundation (S1-2)
  ├── Core Pages (S3-6)
  │     ├── Business (S7-8)
  │     │     └── Integration (S11-12)
  │     └── Admin (S9-10)
  └── All → Polish (S13-14) → Launch
```

## AA.3 Definition of Done
```
EVERY FEATURE IS DONE WHEN:
- [ ] Code merged (with review)
- [ ] Unit tests pass (≥80% coverage)
- [ ] Integration tests pass
- [ ] E2E test passes (if critical path)
- [ ] Mobile responsive verified
- [ ] Warm tone applied to all user-facing text
- [ ] Accessibility verified (WCAG AA)
- [ ] Documentation updated
- [ ] Feature flag wired (if applicable)
- [ ] Analytics event tracked (if applicable)
```

---

# SECTION AB: Final Verification Checklist

## AB.1 Document Completeness Verification

- [ ] Section A: Project Structure (folders, stack, routes) ✅
- [ ] Section B: Dashboard — all 7 admin pages ✅
- [ ] Section C: Consumer App — 52 flows mapped to pages ✅
- [ ] Section D: Question flow per page ✅
- [ ] Section E: Master checklist (Phases 1-6) ✅
- [ ] Section F: Design system & brand ✅
- [ ] Section G: API reference ✅
- [ ] Section H: Detailed per-page flow specs ✅
- [ ] Section I: All 47 sub-problems 8-phase matrix ✅
- [ ] Section J: Edge cases & pitfalls ✅
- [ ] Section K: Testing strategy ✅
- [ ] Section L: Security & PDPA ✅
- [ ] Section M: Deployment & DevOps ✅
- [ ] Section N: Knowledge base & content ✅
- [ ] Section O: Analytics & growth ✅
- [ ] Section P: Personas & journeys ✅
- [ ] Section Q: Granular acceptance criteria ✅
- [ ] Section R: Component inventory ✅
- [ ] Section S: Product roadmap ✅
- [ ] Section T: Risk register ✅
- [ ] Section U: Launch runbook ✅
- [ ] Section V: Warm tone copy samples ✅
- [ ] Section W: Summary & key decisions ✅
- [ ] Section X: Admin/lawyer detailed flows ✅
- [ ] Section Y: Database detail ✅
- [ ] Section Z: Complete reference flow ✅
- [ ] Section AA: Sprint plan ✅
- [ ] Section AB: Final verification ✅

## AB.2 Design Philosophy Verification

- [ ] "ชูใจ" (uplift the heart) is the core brand ✅
- [ ] Every interaction warm, empathetic, empowering ✅
- [ ] Plain Thai (high school student understands) ✅
- [ ] 8-phase concierge flow (gold standard) ✅
- [ ] Monetization gate at curiosity peak (Phase 3) ✅
- [ ] 4-tier pricing (Free/299/999/2990) ✅
- [ ] Compound case handling ✅
- [ ] Fear calibration ✅
- [ ] 22 human drives integration ✅
- [ ] 7 guardrails (MUST-NEVER rules) ✅
- [ ] PDPA compliance ✅
- [ ] Lawyer 10-point checklist ✅
- [ ] Court guide integration (blue-shirt, etiquette, perjury) ✅
- [ ] LINE integration ✅

---

## 🎯 Final Summary

This document provides a COMPLETE design for **Chujai Legal (ชูใจ ลีกัล)** — a full SaaS legal platform built from scratch.

### What's Covered
1. **Project Structure**: Folder structure, tech stack (Next.js 15 + Supabase + DeepSeek + LINE), complete route map (60+ routes)
2. **Dashboard (Admin)**: 7 admin pages with full specs, charts, filters, AI questions, checklists
3. **Consumer App**: All 52 flows (47 sub-problems + 5 utility) mapped to pages, 12 categories × 8-phase concierge flows
4. **Question Flow Per Page**: Master question matrix + per-category question flows + admin/lawyer flows
5. **Master Checklist**: 6 phases (Foundation → Core → Business → Admin → Integration → Polish) with acceptance criteria
6. **Plus**: Design system, API reference, 47 sub-problem matrix, edge cases, testing, security, DevOps, personas, roadmap, risks, launch runbook, copy samples

### Total Scale
- **29 sections** (A through AB)
- **47 sub-problems** fully mapped
- **60+ routes** specified
- **150+ acceptance criteria** defined
- **12 categories** with complete legal detail

*ชูใจ ลีกัล — กฎหมายใกล้ตัว อุ่นใจทุกปัญหา* 🌸
