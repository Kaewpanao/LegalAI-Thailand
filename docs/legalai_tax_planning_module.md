# LegalAI Tax Planning & Optimization Module

> **Product Feature Specification — Standalone Module**
> Version 1.0 | August 2026
> Target Market: Thailand (Individual + Corporate)
> Platform: LegalAI Thailand

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Market Opportunity & Competitive Landscape](#2-market-opportunity--competitive-landscape)
3. [Thai Tax System Reference](#3-thai-tax-system-reference)
4. [Feature Set: 8 Core Modules](#4-feature-set-8-core-modules)
5. [Free vs Paid Tier Strategy](#5-free-vs-paid-tier-strategy)
6. [UX Flows & User Journeys](#6-ux-flows--user-journeys)
7. [Integration Architecture](#7-integration-architecture)
8. [Technical Architecture](#8-technical-architecture)
9. [Monetization & Business Model](#9-monetization--business-model)
10. [Go-to-Market Roadmap](#10-go-to-market-roadmap)
11. [Risk & Compliance](#11-risk--compliance)
12. [Appendix: Data Models](#12-appendix-data-models)

---

## 1. Executive Summary

LegalAI Tax Planning & Optimization is a **standalone tax module** that transforms Thailand's complex tax system into an approachable, AI-driven experience for both **individual taxpayers** and **businesses**. The module combines a real-time tax calculator, AI deduction optimizer, year-round planning timeline, and what-if scenario modeling — all personalized to the Thai Revenue Code.

**Why this matters now:**
- Thailand has 11M+ individual tax filers annually (PND 90/91) with most leaving deductions unclaimed
- ~800,000 registered companies face complex corporate tax compliance (PND 50/51, BOI, transfer pricing)
- No dominant Thai-language tax planning platform exists — the market is fragmented across accounting firms, bank calculators, and Excel spreadsheets
- The Thai Revenue Department is accelerating e-filing adoption, creating demand for digital tax tools

**Key differentiators vs global competitors:**
- Native Thai tax logic (not adapted from US/India)
- Dual individual + corporate coverage in a single platform
- AI-powered deduction optimizer that understands Thai-specific instruments (RMF, SSF, ThaiESG)
- Year-round planning, not just year-end filing

---

## 2. Market Opportunity & Competitive Landscape

### 2.1 Global Competitor Analysis

#### TurboTax (Intuit) — United States
| Dimension | Details |
|-----------|---------|
| **Users** | 40M+ annual filings |
| **Model** | Interview-driven wizard with 350+ deduction finder |
| **AI Features** | Intuit Assist — NLP-powered tax guidance, automated document ingestion, personalized deduction suggestions |
| **Pricing** | Free ($0) → Deluxe ($69) → Premier ($99) → Self-Employed ($129) → Live Full Service ($219+) |
| **Strengths** | Polished UX, massive deduction database, accuracy guarantee, bank import |
| **Weaknesses** | US-only, expensive upsells, complex pricing, no corporate coverage |
| **Takeaway for LegalAI** | Interview wizard UX pattern, tiered pricing with clear upgrade triggers, max-refund guarantee as trust anchor |

#### ClearTax — India
| Dimension | Details |
|-----------|---------|
| **Users** | 8M+ tax filers |
| **Model** | Pre-filled forms from broker integrations (Zerodha, ICICI), AI chat-based filing |
| **AI Features** | Automated data import from 100+ sources, AI chatbot for tax queries, smart deduction suggestions |
| **Pricing** | Free tier → Self-filing (~₹1,000) → Expert-assisted (~₹3,000-8,000) → Business plans |
| **Strengths** | Broker ecosystem integration, mobile-first, vernacular language support, massive scale |
| **Weaknesses** | India-only, limited corporate depth, heavy reliance on data imports |
| **Takeaway for LegalAI** | Pre-fill from Thai broker data (SET, banks), mobile-first design, freemium funnel, chat-based assistance |

#### TaxTim — South Africa
| Dimension | Details |
|-----------|---------|
| **Users** | 500K+ users |
| **Model** | Conversational AI tax assistant (chatbot personality "Tim") |
| **Pricing** | Free calculators → Lite (R315/submission) → Premium plans, no-login calculators as top-of-funnel |
| **Strengths** | Delightful conversational UX, free calculator funnel, SARS eFiling integration |
| **Weaknesses** | Individual only, limited AI capabilities |
| **Takeaway for LegalAI** | Conversational AI personality, free no-login calculator as acquisition channel, e-filing integration |

#### thetax.nl — Netherlands
| Dimension | Details |
|-----------|---------|
| **Model** | Pure calculator — free, no signup, no ads |
| **Strengths** | Ultra-simple, instant value, trust through transparency |
| **Weaknesses** | No filing, no planning, calculator only |
| **Takeaway for LegalAI** | Free instant calculator as homepage/landing page, zero-friction entry point |

#### QuickBooks — Global
| Dimension | Details |
|-----------|---------|
| **Model** | Accounting-first with tax module |
| **Strengths** | Full business integration, P&L → tax auto-flow |
| **Weaknesses** | Tax is secondary, not Thai-localized |
| **Takeaway for LegalAI** | SME tax integration with accounting data, P&L-based corporate tax estimation |

### 2.2 Thailand Market Gap Analysis

| Need | Existing Solutions | Gap |
|------|-------------------|-----|
| Individual tax calculator | Bank websites (SCB, Kbank), Kalberry, BaseUtils | No AI optimization, no year-round planning, no filing prep |
| Deduction optimization | Insurance agents, financial advisors | Conflict of interest (selling products), not comprehensive |
| Corporate tax planning | Accounting firms (PwC, EY, local firms) | Expensive (฿30K+/year), human-dependent, no what-if modeling |
| Tax timeline/calendar | None | Complete gap — no digital reminder system exists |
| Document management | Manual folders, Line photos | No organized checklist, no OCR-based receipt scanning |

**LegalAI's positioning:** The first comprehensive, AI-powered, Thai-native tax platform covering both individual and corporate in a single product.

---

## 3. Thai Tax System Reference

### 3.1 Personal Income Tax (PND 90/91)

#### Progressive Tax Rates (2024-2025)
| Net Taxable Income (THB) | Rate | Cumulative Tax |
|--------------------------|------|----------------|
| 0 – 150,000 | 0% (Exempt) | 0 |
| 150,001 – 300,000 | 5% | 7,500 |
| 300,001 – 500,000 | 10% | 27,500 |
| 500,001 – 750,000 | 15% | 65,000 |
| 750,001 – 1,000,000 | 20% | 115,000 |
| 1,000,001 – 2,000,000 | 25% | 365,000 |
| 2,000,001 – 5,000,000 | 30% | 1,265,000 |
| 5,000,001+ | 35% | — |

#### Complete Deduction & Allowance Catalog

**A. Personal & Family Allowances**

| Deduction | Max Amount (THB) | Conditions |
|-----------|-----------------|------------|
| Personal Allowance | 60,000 | Automatic for all taxpayers |
| Spouse Allowance | 60,000 | Spouse must have no income OR files separately |
| Child Allowance | 30,000/person | Under 20 years old (or under 25 if studying); max 3 children |
| Child Allowance (2nd child+) | 60,000/person | For 2nd child born after 2018; max 2 additional |
| Prenatal Care & Childbirth | 60,000 | Per pregnancy; actual expenses |
| Parental Care | 30,000/person | Parent over 60, income < 30,000 THB/year; max 4 (own + spouse's parents) |
| Disabled Dependent Care | 60,000/person | Certified disability |

**B. Insurance Deductions**

| Deduction | Max Amount (THB) | Conditions |
|-----------|-----------------|------------|
| Life Insurance (General) | 100,000 | Policy ≥ 10 years; Thai-registered insurer |
| Life Insurance (Deposit-type) | 100,000 | Separate limit; deposit-type policy; ≥ 10 years |
| Health Insurance | 25,000 | Self + spouse + children |
| Health Insurance (Parents) | 15,000 | Parents' health insurance premiums |
| Social Security Contributions | 9,000 | Mandatory SSO contributions (max 750 THB/month) |
| Pension/Annuity Insurance | 200,000 | 15% of income cap; combined with RMF/provident fund limit |

**C. Investment & Retirement Deductions**

| Deduction | Max Amount (THB) | Conditions |
|-----------|-----------------|------------|
| RMF (Retirement Mutual Fund) | 30% of income, max 500,000 | Min 5 years holding; buy annually (skip max 1 year); redeem at 55+ |
| SSF (Super Savings Fund) | 30% of income, max 200,000 | Min 10 years holding; no annual purchase requirement |
| ThaiESG (Thailand ESG Fund) | 30% of income, max 300,000 | Min 8 years holding (reduced from 5 in 2024) |
| Provident Fund (PVD) | 15% of salary, max 500,000 | Employer-sponsored; shared limit with RMF + pension insurance |
| Government Pension Fund | 15% of salary, max 500,000 | Government employees |
| National Savings Fund (NSF) | 13,200 | Self-employed/ informal workers |

**D. Property & Housing Deductions**

| Deduction | Max Amount (THB) | Conditions |
|-----------|-----------------|------------|
| Mortgage Interest | 100,000 | Primary residence; loan from Thai financial institution |
| Home Purchase Allowance | 200,000 | First home purchase; phased (2024: 100,000 / 2025: 100,000) |

**E. Other Deductions**

| Deduction | Max Amount (THB) | Conditions |
|-----------|-----------------|------------|
| Donations (General) | 10% of net income | To approved charities |
| Donations (Education/Sports) | 2x actual, max 10% of net | Double deduction for education/sports donations |
| Political Donations | 10,000 | Registered political parties |
| Education Expenses | 30,000 | Self-education and children's education |
| Tourist Attraction Visits | 15,000 | Domestic tourism (seasonal/promotional) |
| Shopping Tax Break | 30,000 | Shop Dee Mee Khuen (seasonal promotion — varies by year) |

**F. Income-Specific Deductions**

| Income Type | Deduction Method | Max |
|------------|-----------------|-----|
| Employment Income | 50% of income | 100,000 |
| Rental Income | 30% flat | No cap |
| Professional Services | 60% (medical), 30% (liberal professions) | No cap |
| Contract Work | 60% actual or lump-sum | No cap |
| Business Income | 60-85% depending on type | No cap |

### 3.2 Corporate Income Tax (PND 50/51)

#### Standard Tax Rates
| Taxpayer Type | Rate | Conditions |
|---------------|------|------------|
| Standard Corporate | 20% | All juristic companies & partnerships |
| SME (Paid-up capital ≤ 5M THB) | Progressive | See table below |
| BOI-Promoted (Category A) | 0% | 3-8 year tax holiday |
| BOI-Promoted (Category B) | 0% → 50% reduction | Tax holiday + subsequent reduction |

#### SME Progressive Rates
| Net Profit (THB) | Rate |
|-----------------|------|
| 0 – 300,000 | 0% (Exempt) |
| 300,001 – 3,000,000 | 15% |
| 3,000,001+ | 20% |

#### Corporate Deduction Catalog

| Expense Category | Rules & Limits |
|-----------------|----------------|
| **Depreciation** | Straight-line or declining balance; rates vary by asset class (buildings 5-20%, machinery 20%, computers 20-33%, vehicles 20%) |
| **Entertainment Expenses** | 0.3% of gross revenue or actual paid-up capital (whichever higher); capped |
| **Bad Debt Provision** | Must meet Revenue Code criteria: legal action initiated, debtor bankrupt, or write-off per RD rules |
| **R&D Expenses** | 200% deduction (double deduction) for qualifying R&D in Thailand |
| **Training/Education** | 200% deduction for approved training programs |
| **Donations** | 2% of net profit for general charity; 2x for education/sports |
| **Employee Benefits** | Reasonable amounts; provident fund contributions deductible |
| **Interest Expense** | Deductible subject to thin capitalization rules |
| **Tax Loss Carryforward** | 5 years (no carryback) |
| **BOI Tax Holiday** | 3-13 years depending on activity category + merit incentives |
| **Transfer Pricing** | Arm's length principle; documentation required for related-party transactions > threshold |

#### VAT Overview (Relevant for Optimization)
- Standard rate: 7% (extended annually)
- Registration threshold: 1.8M THB annual revenue
- Input tax credit: VAT on purchases offset against VAT on sales
- Zero-rated exports; exempt services (healthcare, education, agriculture)

### 3.3 Filing Deadlines

| Filing | Due Date | Taxpayer |
|--------|---------|----------|
| PND 90 | March 31 (paper) / April 8 (e-filing) | Individuals with non-employment income |
| PND 91 | March 31 (paper) / April 8 (e-filing) | Individuals with employment income only |
| PND 50 | Within 150 days of fiscal year-end | All companies |
| PND 51 | Within 2 months of half-year | All companies (estimated mid-year tax) |
| PND 54 | Within 150 days of year-end | Foreign companies operating in Thailand (branch) |
| PND 3/53 | 7th of following month | Withholding tax remittance |
| PP 30 | 15th of following month | VAT return |

---

## 4. Feature Set: 8 Core Modules

### 4.1 Feature 1: Smart Tax Calculator

**Description:** Real-time tax estimation with interactive sliders and instant visual feedback.

**Core Capabilities:**
- **Progressive tax bracket visualization** — Donut/bar chart showing exactly which brackets apply and how much tax in each
- **Income entry modes:**
  - Monthly salary → auto-annualizes
  - Annual gross income
  - Multiple income streams (salary + freelance + rental + investment)
- **Real-time slider for every deduction** — Slide up/down to see tax impact instantly
- **Net take-home pay calculation** — After-tax, after-SSO, after-provident fund
- **Tax refund/tax due estimator** — Compare withholding tax paid vs actual liability
- **Comparison mode** — Side-by-side: "Last year vs This year" or "With planning vs Without"

**UI Elements:**
```
┌─────────────────────────────────────────────────────┐
│  THAI TAX CALCULATOR               [Year: 2025 ▼]  │
├─────────────────────────────────────────────────────┤
│  Monthly Income:  [══════●═══════]  85,000 THB      │
│                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Gross       │  │  Deductions │  │  Tax Due    │ │
│  │  ฿1,020,000 │→│  ฿385,000   │→│  ฿47,250    │ │
│  └─────────────┘  └─────────────┘  └─────────────┘ │
│                                                     │
│  Tax Bracket Breakdown:                             │
│  ████████░░░░░░ 0%    150K (0 THB)                  │
│  ████░░░░░░░░░░ 5%    150K (7,500 THB)              │
│  ███░░░░░░░░░░░ 10%   200K (20,000 THB)             │
│  ██░░░░░░░░░░░░ 15%   135K (19,750 THB)             │
│                                                     │
│  Effective Tax Rate: 4.6%  |  Marginal Rate: 15%    │
└─────────────────────────────────────────────────────┘
```

**Free Tier:** Basic calculator with salary, personal allowance, and 5 common deductions
**Paid Tier:** All deductions, multi-income, comparison mode, save/export

---

### 4.2 Feature 2: AI Deduction Optimizer

**Description:** AI engine that analyzes user's financial profile and suggests the optimal deduction allocation to legally minimize tax liability.

**Core Capabilities:**
- **Deduction discovery interview** — Conversational AI (inspired by TurboTax interview + TaxTim personality) asks targeted questions
- **Optimization engine** — Given income, existing deductions, and available cash, computes optimal allocation across:
  - RMF vs SSF vs ThaiESG mix
  - Life insurance vs health insurance allocation
  - Donation optimization (charitable giving to reduce bracket)
  - Timing optimization (which deductions to claim this year vs defer)
- **"Missing Deductions" detector** — Flags deductions the user qualifies for but isn't claiming
- **Personalized recommendation cards** — Each card shows: deduction name, max amount, estimated tax saving, confidence level, and action required

**AI Logic Flow:**
```
Input: User Profile (income, family, existing investments, cash available)
       ↓
1. Calculate baseline tax (current situation)
2. Enumerate all eligible deduction combinations
3. Constraint checking (max limits, eligibility rules)
4. Optimization: minimize tax = f(income - deductions)
   - Priority queue: highest marginal-rate deductions first
   - Liquidity constraint: user must have cash to invest
5. Output: Top 3 optimal scenarios → present as ranked cards
```

**Example Recommendation Card:**
```
┌──────────────────────────────────────────┐
│  💡 RMF TOP-UP RECOMMENDATION            │
│                                          │
│  You can invest up to ฿156,000 more in  │
│  RMF this year (30% of ฿850,000 income) │
│                                          │
│  Current RMF: ฿100,000                  │
│  Recommended: +฿56,000                  │
│  Tax Saved: ฿11,200 (20% bracket)       │
│                                          │
│  📅 Invest by Dec 31, 2025              │
│  ⚠️ Must hold until age 55              │
│  [Invest Now →]  [Remind Me]  [Dismiss] │
└──────────────────────────────────────────┘
```

**Free Tier:** Top 3 deduction suggestions, basic interview
**Paid Tier:** Full optimization engine, all deductions, personalized investment mix, export to PDF report

---

### 4.3 Feature 3: Tax Planning Timeline

**Description:** A year-round calendar and deadline management system that tells users exactly what to do and when.

**Core Capabilities:**
- **Interactive calendar view** — Monthly/weekly view color-coded by urgency
- **Deadline tracker** — All filing deadlines (PND 90/91, PND 50/51, PP 30) with countdown timers
- **Action items with due dates:**
  - "Buy RMF units by Dec 31" (Nov alert, Dec urgent)
  - "Pay life insurance premium by Dec 31"
  - "Collect mortgage interest certificate from bank by Jan 31"
  - "Make charitable donations by Dec 31"
  - "Submit mid-year PND 51 by Aug 31"
- **Push notifications & email reminders** — Configurable lead times (1 week, 3 days, day-of)
- **Seasonal promotions tracker** — Shop Dee Mee Khuen dates, tourist deduction windows
- **"Year-End Sprint" mode** (Oct-Dec) — Intensified UI showing countdown to Dec 31 deduction deadline

**Timeline Structure:**
```
JAN  [Collect documents]   — Bank interest certs, SSO summary, salary cert
FEB  [Review & verify]     — Cross-check withholding tax, verify deductions
MAR  [FILE PND 90/91]      — Deadline Mar 31 / Apr 8 (e-filing)
APR  [Post-filing review]  — Check refund status, note improvements
MAY  [Mid-year corp est.]  — PND 51 estimation for businesses
JUN  [Mid-year review]     — Check YTD income vs projection, adjust
JUL  [Mid-year review]     — Check YTD income vs projection
AUG  [FILE PND 51]         — Half-year corporate tax due
SEP  [Year-end planning]   — Start planning deductions, check available cash
OCT  [Year-end sprint 1]   — Begin executing deduction plan
NOV  [Year-end sprint 2]   — RMF/SSF/ThaiESG purchases, insurance renewals
DEC  [Year-end sprint 3]   — Last month for all deductions; donations, funds, insurance
```

**Free Tier:** Basic calendar with filing deadlines
**Paid Tier:** Full timeline, personalized action items, push/email notifications, year-end sprint mode

---

### 4.4 Feature 4: What-If Scenario Builder

**Description:** Compare multiple tax scenarios side-by-side to make informed financial decisions.

**Core Capabilities:**
- **Scenario types:**
  - "With Planning vs Without Planning" — Default comparison
  - "Married vs Single" — Filing jointly vs separately
  - "Buy RMF vs Buy SSF vs Buy ThaiESG" — Investment vehicle comparison
  - "Rent vs Buy Home" — Mortgage interest impact
  - "This Year vs Last Year" — Year-over-year comparison
  - "Salary Increase Impact" — See how a raise affects net take-home
  - "Freelance vs Employment" — Compare tax burden across income types
  - "Corporate: Standard vs BOI vs SME" — Entity structure optimization
- **Scenario saving & naming** — Save scenarios for later comparison
- **Export to PDF** — Professional report with charts and recommendations
- **Share scenarios** — Generate shareable link for accountant/family

**UI Layout:**
```
┌──────────────────┬──────────────────┬──────────────────┐
│  SCENARIO A      │  SCENARIO B      │  SCENARIO C      │
│  "Status Quo"    │  "Max RMF"       │  "Balanced"      │
├──────────────────┼──────────────────┼──────────────────┤
│  Gross: 1,200K   │  Gross: 1,200K   │  Gross: 1,200K   │
│  Deductions: 280K│  Deductions: 540K│  Deductions: 450K │
│  Tax: 87,500     │  Tax: 42,250     │  Tax: 59,100     │
│  Eff. Rate: 7.3% │  Eff. Rate: 3.5% │  Eff. Rate: 4.9% │
│                  │  SAVE: 45,250 ฿  │  SAVE: 28,400 ฿  │
│  [Baseline]      │  [🏆 Optimal]    │  [Moderate]      │
└──────────────────┴──────────────────┴──────────────────┘
```

**Free Tier:** 2-scenario comparison, basic variables
**Paid Tier:** Unlimited scenarios, all variable types, export, share, AI-generated insights per scenario

---

### 4.5 Feature 5: Document Checklist & Manager

**Description:** Smart checklist of required documents with OCR receipt scanning and digital organization.

**Core Capabilities:**
- **Personalized document checklist** — Auto-generated based on declared deductions
- **Status tracking:** Not Started / Collected / Uploaded / Verified
- **Mobile document upload** — Camera capture → OCR → auto-categorize
- **OCR receipt scanning** — Extract vendor, amount, date, category from receipt photos
- **Document expiry alerts** — "Your life insurance certificate expires; request new one"
- **Export for accountant** — Generate organized ZIP of all tax documents
- **Document retention timeline** — Thai law requires 5-year retention; auto-archive

**Checklist Example (Personalized):**
```
☑ Salary Certificate (Thor Dor 1)        — Uploaded ✓
☑ SSO Contribution Summary                — Uploaded ✓
☐ RMF Purchase Receipts                   — Need 2 more receipts
☐ Life Insurance Premium Certificate      — Request from AIA
☐ Mortgage Interest Certificate (Bank)    — Available Feb 2026
☐ Child's School Fee Receipts             — Need to collect
☐ Donation Receipts                       — 3 uploaded of estimated 5
☐ Health Insurance Premium Certificate    — Uploaded ✓

Progress: ████████░░  7/10 documents ready
```

**Free Tier:** Basic checklist, manual status tracking
**Paid Tier:** OCR scanning, auto-categorization, export, retention management, accountant share

---

### 4.6 Feature 6: Filing Assistant

**Description:** Pre-fill PND 90/91/50/51 data from user profile and generate filing-ready data.

**Core Capabilities:**
- **Auto-populate PND 90/91 fields** — From user profile + deduction data
- **Income category mapping** — Auto-classify income into Revenue Code categories (Section 40(1)-(8))
- **Validation engine** — Cross-check totals, flag inconsistencies, verify against Revenue Department rules
- **Data export formats:**
  - RD e-Filing compatible JSON/XML
  - PDF summary for manual filing
  - Excel for accountant review
- **Step-by-step filing guide** — Screenshot walkthrough of RD e-Filing website
- **Error resolution** — Common RD rejection reasons and how to fix

**Corporate-specific (PND 50/51):**
- P&L → tax return mapping (auto-classify revenue/expenses into RD categories)
- Depreciation schedule generation
- Tax reconciliation: accounting profit → taxable profit
- BOI exempt/non-exempt income split

**Filing Flow:**
```
1. Profile Import → 2. Data Validation → 3. Review Summary → 4. Export/File
   (auto)             (errors flagged)     (visual summary)    (RD-compatible)
```

**Free Tier:** PND 91 (simple employment income), summary view
**Paid Tier:** PND 90, PND 50/51, validation engine, RD-compatible export, step-by-step guide

---

### 4.7 Feature 7: Personalized Tax Saving Tips

**Description:** AI-curated, personalized tax-saving recommendations based on income bracket, life stage, and spending patterns.

**Core Capabilities:**
- **Life-stage segmentation:**
  - Early career (22-30): SSF focus, health insurance, education deductions
  - Mid career (30-45): RMF + SSF, mortgage interest, child deductions
  - Pre-retirement (45-55): Aggressive RMF, pension insurance, parent deductions
  - Retirement (55+): RMF redemption planning, passive income optimization
- **Income-bracket-specific tips:**
  - 0-150K bracket: Focus on exempt threshold utilization
  - 20-25% brackets: Maximum value from deductions (highest ROI)
  - 30-35% brackets: Aggressive optimization; every baht counts at 35%
- **Behavioral nudges:**
  - "฿100K invested in RMF by Dec 31 saves you ฿20K in tax — that's a 20% instant return"
  - "You paid ฿47K in tax last year. 3 simple changes could save you ฿18K this year."
- **News feed** — Tax law changes, new deduction opportunities, expiring promotions

**Content Categories:**
```
💰 INVESTMENT:   RMF vs SSF comparison for your bracket
🏠 HOUSING:      Mortgage interest deduction explained
👨‍👩‍👧 FAMILY:     Claiming child + parent deductions simultaneously
🏥 INSURANCE:    Stacking health + life insurance deductions
📊 STRATEGY:     Why donating ฿5,000 could save you ฿7,000 in tax
⚠️ WARNING:      Common RD audit triggers to avoid
```

**Free Tier:** 3 tips/week, general content
**Paid Tier:** Unlimited personalized tips, bracket optimization strategies, tax law change alerts

---

### 4.8 Feature 8: Year-Round Tax Tracker

**Description:** A dashboard that tracks tax-relevant activity throughout the year — not just at filing time.

**Core Capabilities:**
- **YTD Income Tracker** — Real-time projection of annual taxable income
- **Deduction Progress Bar** — Visual progress toward deduction caps
  ```
  RMF:           ████████░░  240K/500K (48%)
  Life Insurance:████████████ 100K/100K (100% ✓)
  SSF:           ███░░░░░░░  60K/200K (30%)
  ```
- **Withholding Tax Monitor** — Compare YTD withholding against projected annual tax
- **Quarterly tax estimate** — Especially for freelancers/business owners: "Your estimated Q3 tax: ฿12,500"
- **Cash Flow Calendar** — When big tax-related payments are due (insurance premiums, fund purchases)
- **Year-over-Year Comparison** — Same date last year vs this year
- **Mobile Widget** — Home screen widget showing: "Tax refund estimate: +฿8,500" or "Tax due: ฿15,200"

**Dashboard Overview:**
```
┌────────────────────────────────────────────────────┐
│  YOUR 2025 TAX DASHBOARD          [As of Aug 2025] │
├────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │ YTD      │  │ Est. Tax │  │ Refund/Due       │ │
│  │ Income   │  │ Due      │  │ Estimate         │ │
│  │ 680,000  │  │ 89,500   │  │ +12,300 REFUND   │ │
│  │ of 1.02M │  │          │  │    🟢 On track   │ │
│  └──────────┘  └──────────┘  └──────────────────┘ │
│                                                    │
│  Deduction Progress:                               │
│  ████████░░ RMF      240/500K  Deadline: Dec 31   │
│  ██████████ Life Ins 100/100K  ✓ Complete         │
│  ██████░░░░ SSF      120/200K  Dec 31 (80K left)  │
│                                                    │
│  Upcoming:                                         │
│  📅 Sep 15 — Insurance premium due (฿25,000)      │
│  📅 Oct 1  — Q4 estimated tax payment              │
│  📅 Dec 31 — Last day for all 2025 deductions!     │
│  ⏰ 143 days remaining                              │
└────────────────────────────────────────────────────┘
```

**Free Tier:** Basic YTD income tracker, 3 deduction progress bars
**Paid Tier:** Full dashboard, all deductions tracked, withholding monitor, cash flow calendar, mobile widget

---

## 5. Free vs Paid Tier Strategy

### 5.1 Tier Structure

#### Free Tier — "LegalAI Tax Basic" (฿0)
**Target:** Mass market acquisition, top-of-funnel, virality

| Feature | Included |
|---------|----------|
| Smart Tax Calculator | Salary only, 5 basic deductions, simple bracket view |
| Deduction List | Browse all deductions with descriptions |
| Tax Timeline | Filing deadlines only (PND 90/91 dates) |
| Document Checklist | Basic checklist, manual tracking |
| Tax Saving Tips | 3 tips/week, general educational content |
| Ads/Watermark | "Upgrade to Premium" watermark on reports |

**Acquisition hooks:**
- Share calculator result on social media → "I could save ฿18,000 on taxes. Find yours: [link]"
- No-login calculator embeddable on partner sites (banks, HR platforms, media)

#### Individual Premium — "LegalAI Tax Pro" (฿199/month or ฿299/one-time filing)
**Target:** Salaried professionals, freelancers, expats earning in Thailand

| Feature | Included |
|---------|----------|
| Smart Tax Calculator | Full: all income types, all 30+ deductions, comparison mode |
| AI Deduction Optimizer | Full optimization engine, personalized mix, investment recommendations |
| Tax Planning Timeline | Full calendar, personalized actions, push/email notifications, year-end sprint |
| What-If Scenarios | Unlimited scenarios, all variables, PDF export |
| Document Manager | OCR scanning, auto-categorization, secure storage, export |
| Filing Assistant | PND 90/91 pre-fill, validation, RD-compatible export, step-by-step guide |
| Tax Saving Tips | Unlimited personalized tips, bracket strategies, law change alerts |
| Year-Round Tracker | Full dashboard, withholding monitor, cash flow calendar, mobile widget |
| Support | Email support, 48h response |

**Pricing options:**
- ฿299/year — Annual plan (best value, ~฿25/mo)
- ฿299 — One-time filing season pass (Jan-Apr)
- Freelancer add-on: +฿99 for multi-income optimization

#### SME/Business — "LegalAI Tax Business" (฿999–฿1,990/month)
**Target:** SMEs, startups, family businesses, BOI-promoted companies

| Tier | Price | Features |
|------|-------|----------|
| **Business Starter** | ฿999/mo | Corporate calculator, PND 50/51 pre-fill, depreciation schedule, basic deduction optimization, single entity |
| **Business Pro** | ฿1,990/mo | All Starter + BOI optimization, transfer pricing documentation assistant, multi-entity, VAT optimization, R&D double deduction calculator, accountant collaboration tools |

**Business features:**
- P&L data import (CSV, QuickBooks, Xero, FlowAccount)
- Depreciation schedule automation
- BOI incentive tracking & utilization optimization
- Transfer pricing documentation assistant
- VAT input tax credit optimization
- Multi-user access (accountant + owner + finance team)
- Audit trail & version history
- Priority support (4h response)

### 5.2 Conversion Funnel

```
ACQUISITION           ACTIVATION          MONETIZATION        RETENTION
───────────           ──────────          ─────────────        ─────────
Free Calculator ──→  Sign Up (email) ──→  Free Trial (14d) ──→ Annual Plan
(no login)           See personalized     Full Pro features    Auto-renew with
                     deduction estimate   for 14 days          reminder 30d before

SEO/Blog posts ──→   Lead Magnet ──→      Email Nurture ──→   Seasonal Upsell
"10 Deductions       "Ultimate Thai Tax   5-email sequence     Nov-Dec: "Year-end
You're Missing"      Deduction Checklist" Nov → Mar push       deduction sprint"
```

### 5.3 Revenue Projections (Year 1)

| Segment | Est. Users | Conversion | ARPU/mo | Annual Revenue |
|---------|-----------|------------|---------|----------------|
| Free | 200,000 | — | ฿0 | ฿0 |
| Individual Pro | 8,000 | 4% | ฿25 | ฿2,400,000 |
| Filing Pass | 15,000 | 7.5% | ฿299 (one-time) | ฿4,485,000 |
| Business Starter | 400 | — | ฿999 | ฿4,795,200 |
| Business Pro | 150 | — | ฿1,990 | ฿3,582,000 |
| **Total** | **223,550** | — | — | **฿15,262,200** |

---

## 6. UX Flows & User Journeys

### 6.1 First-Time Individual User Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FIRST-TIME USER ONBOARDING                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LANDING PAGE                                                       │
│  ┌──────────────────────────────────────────┐                       │
│  │  "How much tax could you save?"          │                       │
│  │  [Enter monthly salary: ______] [CALC]   │  ← No login required │
│  │  Quick Result: Est. Tax: ฿47,000         │                       │
│  │  "฿18,000 in deductions you might miss"  │                       │
│  │  [See My Full Savings →] (triggers signup)│                      │
│  └──────────────────────────────────────────┘                       │
│           │                                                         │
│           ▼                                                         │
│  SIGN UP (email / Google / Line / Apple)                            │
│           │                                                         │
│           ▼                                                         │
│  INTERVIEW WIZARD (5-7 min)                                         │
│  ┌──────────────────────────────────────────┐                       │
│  │  Step 1: Income Sources                  │                       │
│  │  "What describes your income?"           │                       │
│  │  ☐ Salary  ☐ Freelance  ☐ Rental        │                       │
│  │  ☐ Business  ☐ Investment  ☐ Other      │                       │
│  │                                          │                       │
│  │  Step 2: Family Situation                │                       │
│  │  "Tell us about your household"          │                       │
│  │  Married? [Yes/No]  Spouse income?       │                       │
│  │  Children? [0][1][2][3]  Ages?           │                       │
│  │  Parents over 60? [0][1][2][3][4]        │                       │
│  │                                          │                       │
│  │  Step 3: Existing Deductions             │                       │
│  │  "What are you already claiming?"        │                       │
│  │  ☐ Social Security  ☐ Provident Fund    │                       │
│  │  ☐ Life Insurance  ☐ Health Insurance   │                       │
│  │  ☐ RMF  ☐ SSF  ☐ ThaiESG               │                       │
│  │  ☐ Mortgage Interest  ☐ Donations       │                       │
│  │                                          │                       │
│  │  Step 4: Available Cash                  │                       │
│  │  "How much can you invest this year?"    │                       │
│  │  [Enter amount: ______]                  │                       │
│  └──────────────────────────────────────────┘                       │
│           │                                                         │
│           ▼                                                         │
│  RESULTS DASHBOARD                                                  │
│  ┌──────────────────────────────────────────┐                       │
│  │  🎉 Your Tax Optimization Plan           │                       │
│  │                                          │                       │
│  │  Current Tax:     ฿47,250               │                       │
│  │  Optimized Tax:   ฿28,100               │                       │
│  │  Potential Save:  ฿19,150 (40% less!)   │                       │
│  │                                          │                       │
│  │  Top 3 Actions:                          │                       │
│  │  1. Invest ฿56K more in RMF → Save ฿11K │                       │
│  │  2. Buy health insurance → Save ฿5K     │                       │
│  │  3. Donate ฿5K to charity → Save ฿1.5K  │                       │
│  │                                          │                       │
│  │  [Start 14-Day Free Trial] [Stay Free]   │                       │
│  └──────────────────────────────────────────┘                       │
│           │                                                         │
│           ▼                                                         │
│  DASHBOARD HOME (Paid)                                              │
│  ┌──────────────────────────────────────────┐                       │
│  │  Sidebar:  📊 Dashboard                  │                       │
│  │            🧮 Tax Calculator             │                       │
│  │            💡 Deduction Optimizer        │                       │
│  │            📅 Tax Timeline               │                       │
│  │            🔮 What-If Scenarios          │                       │
│  │            📄 Documents                  │                       │
│  │            📝 Filing Assistant           │                       │
│  │            💬 Tax Tips                   │                       │
│  │                                          │                       │
│  │  Main:     [Year-Round Dashboard]        │                       │
│  └──────────────────────────────────────────┘                       │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 SME/Business Onboarding Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BUSINESS ONBOARDING                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LANDING → "Business Tax Health Check" (Free)                       │
│  ┌──────────────────────────────────────────┐                       │
│  │  [Enter annual revenue: ________]        │                       │
│  │  [Enter annual profit: ________]         │                       │
│  │  [Business type: SME □  BOI □  Standard □]│                      │
│  │  [CHECK MY RATE →]                       │                       │
│  └──────────────────────────────────────────┘                       │
│           │                                                         │
│           ▼                                                         │
│  BUSINESS PROFILE SETUP                                              │
│  ┌──────────────────────────────────────────┐                       │
│  │  Company Name, Tax ID, Fiscal Year       │                       │
│  │  Paid-up Capital, Industry Classification│                       │
│  │  BOI Certificate Upload (if applicable)  │                       │
│  │  Existing Accounting Software Integration│                       │
│  │  ☐ QuickBooks  ☐ Xero  ☐ FlowAccount    │                       │
│  │  ☐ CSV Upload  ☐ Manual Entry           │                       │
│  └──────────────────────────────────────────┘                       │
│           │                                                         │
│           ▼                                                         │
│  CORPORATE DASHBOARD                                                │
│  ┌──────────────────────────────────────────┐                       │
│  │  Sidebar:  📊 Corporate Dashboard        │                       │
│  │            🧮 Corporate Tax Calc         │                       │
│  │            📈 Depreciation Scheduler      │                       │
│  │            🏭 BOI Tracker (if applicable) │                       │
│  │            🔄 Transfer Pricing            │                       │
│  │            📝 PND 50/51 Filing            │                       │
│  │            🏦 VAT Optimizer               │                       │
│  │            🔮 Corporate What-If           │                       │
│  │            👥 Team Access                 │                       │
│  └──────────────────────────────────────────┘                       │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.3 Mobile-First Considerations

Given Thailand's mobile-first internet usage (>95% mobile), the module must be:
- **Progressive Web App (PWA)** — Installable, offline-capable for document upload
- **Line OA Integration** — Tax reminders via Line messages (Thailand's dominant messaging app)
- **Thai language first** — Full Thai UI with English toggle
- **Mobile-optimized calculator** — Large touch targets, swipeable deduction sliders
- **Camera-first document upload** — Direct from camera, auto-crop, OCR

---

## 7. Integration Architecture

### 7.1 Integration with LegalAI Core Platform

```
┌─────────────────────────────────────────────────────────────────────┐
│                     LEGALAI PLATFORM                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │  LegalAI  │  │  LegalAI  │  │  LegalAI  │  │  LegalAI TAX     │   │
│  │  Docs     │  │  Chat     │  │  Contracts│  │  (THIS MODULE)   │   │
│  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘  └────────┬─────────┘   │
│        │              │              │                 │             │
│        └──────────────┼──────────────┼─────────────────┘             │
│                       │              │                               │
│              ┌────────▼──────────────▼─────────┐                     │
│              │       SHARED SERVICES           │                     │
│              │  • User Auth (SSO)              │                     │
│              │  • Profile / Identity           │                     │
│              │  • Document Storage (S3/GCS)    │                     │
│              │  • Notification Engine          │                     │
│              │  • Payment (Omise/PromptPay)    │                     │
│              │  • AI/LLM Gateway               │                     │
│              │  • Analytics & Events           │                     │
│              │  • Search (Elastic/Meilisearch) │                     │
│              └────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.2 Data Dependencies

| LegalAI Module | Data Shared with Tax Module | Direction |
|---------------|---------------------------|-----------|
| User Profile | Income brackets, family status, employment type | Read |
| LegalAI Chat | Tax questions → route to Tax AI, escalate complex tax law | Bidirectional |
| Document Storage | Tax documents stored in same vault, shared OCR pipeline | Write |
| Contracts | Employment contracts → estimate salary income for tax calc | Read |
| Business Entity Manager | Company registration data → pre-fill PND 50/51 | Read |

### 7.3 External Integrations

| Integration | Purpose | Priority |
|------------|---------|----------|
| **Thai Revenue Department e-Filing** | Direct e-filing or pre-fill data export | P1 (Launch) |
| **SET / Broker APIs** (Streaming, InnovestX, K Securities) | Import investment transactions for capital gains tax, dividend withholding | P2 (Q2) |
| **Bank APIs** (SCB, KBank, BBL via Open Banking) | Import mortgage interest certs, interest income, bank statements | P2 (Q2) |
| **Insurance APIs** (AIA, Muang Thai, Bangkok Insurance) | Verify insurance premiums paid for auto-population | P3 (Q3) |
| **Accounting Software** (FlowAccount, Xero, QuickBooks) | Import P&L for corporate tax; export tax journal entries | P2 (Q2) |
| **SSO** (Social Security Office) | Import contribution history for precise SSO deduction calc | P3 (Q3) |
| **Line OA** | Push notifications for deadlines, reminders, year-end tips | P1 (Launch) |
| **PromptPay / QR Payment** | One-click tax payment via RD PromptPay integration | P3 (Q3) |

### 7.4 API Surface (Internal)

```
TAX MODULE APIs:
├── POST   /api/tax/v1/calculate          — Run tax calculation
├── POST   /api/tax/v1/optimize           — Run deduction optimizer
├── GET    /api/tax/v1/deductions         — List all deductions with eligibility
├── POST   /api/tax/v1/deductions/check   — Check eligibility for specific user
├── POST   /api/tax/v1/scenarios          — Create what-if scenario
├── GET    /api/tax/v1/scenarios/:id      — Get scenario
├── POST   /api/tax/v1/scenarios/compare  — Compare scenarios
├── GET    /api/tax/v1/timeline           — Get personalized timeline
├── POST   /api/tax/v1/timeline/reminders — Set timeline reminders
├── GET    /api/tax/v1/tracker/:year      — Get year-round tracker data
├── POST   /api/tax/v1/documents/checklist — Generate document checklist
├── POST   /api/tax/v1/documents/ocr       — OCR a document
├── POST   /api/tax/v1/filing/generate     — Generate filing data (PND 90/91/50/51)
├── POST   /api/tax/v1/filing/validate     — Validate filing data
├── GET    /api/tax/v1/tips                — Get personalized tips
├── GET    /api/tax/v1/corporate/boi       — BOI incentive data
├── POST   /api/tax/v1/corporate/depreciation — Calculate depreciation schedule
└── POST   /api/tax/v1/corporate/vat       — VAT optimization analysis
```

---

## 8. Technical Architecture

### 8.1 System Overview

```
┌──────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐   │
│  │  Web App  │  │  PWA/Mobile│  │  Line Mini App      │   │
│  │  (React)  │  │  (React)  │  │  (Line LIFF)        │   │
│  └─────┬─────┘  └─────┬─────┘  └──────────┬───────────┘   │
│        └──────────────┼────────────────────┘               │
│                       │ HTTPS                              │
│              ┌────────▼────────┐                           │
│              │   API GATEWAY   │                           │
│              │   (Kong/Nginx)  │                           │
│              └────────┬────────┘                           │
├───────────────────────┼───────────────────────────────────┤
│                    SERVICE LAYER                           │
│  ┌──────────┐  ┌──────▼──────┐  ┌──────────────┐        │
│  │  Auth    │  │  Tax Engine  │  │  Optimizer    │        │
│  │  Service │  │  Service     │  │  Service (AI) │        │
│  └──────────┘  └──────┬──────┘  └──────┬───────┘        │
│                       │                │                  │
│  ┌──────────┐  ┌──────▼──────┐  ┌──────▼───────┐        │
│  │  Document│  │  Filing     │  │  Notification │        │
│  │  Service │  │  Service    │  │  Service      │        │
│  └──────────┘  └─────────────┘  └──────────────┘        │
├──────────────────────────────────────────────────────────┤
│                      DATA LAYER                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │PostgreSQL│  │  Redis   │  │  S3/GCS  │  │  Vector  │ │
│  │(tax data)│  │ (cache)  │  │(docs)    │  │  DB (RAG)│ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
└──────────────────────────────────────────────────────────┘
```

### 8.2 Tax Engine Design

The core tax engine must be **deterministic, versioned, and testable**:

```python
# TaxEngine: Immutable, year-versioned
class TaxEngine:
    def __init__(self, tax_year: int):
        self.rules = load_ruleset(tax_year)  # JSON ruleset per tax year
        self.brackets = self.rules["brackets"]
        self.deductions = self.rules["deductions"]
        self.validators = self.rules["validators"]

    def calculate(self, profile: TaxProfile) -> TaxResult:
        # 1. Apply deductions (with eligibility checks)
        # 2. Compute taxable income
        # 3. Apply progressive brackets
        # 4. Return structured result
        pass

    def optimize(self, profile: TaxProfile) -> OptimizationResult:
        # 1. Identify eligible deductions
        # 2. Constraint-based optimization
        # 3. Rank scenarios by tax saved
        # 4. Return top N recommendations
        pass
```

**Rulesets stored as versioned JSON** — One file per tax year (`rules_2024.json`, `rules_2025.json`). This allows:
- Hot-reload when tax laws change
- Historical calculations (recalculate past years)
- A/B testing new rules before law is finalized
- Audit trail: which ruleset was used for which filing

### 8.3 AI/LLM Integration

| AI Capability | Approach | Model |
|--------------|----------|-------|
| Deduction Interview | LLM with structured output + RAG on Thai Revenue Code | GPT-4o / Claude |
| Tax Question Chatbot | Fine-tuned on Thai tax Q&A + RD rulings; RAG on Revenue Code | Fine-tuned Thai LLM (Typhoon/OpenThaiGPT) |
| Deduction Optimizer | Constraint solver (OR-Tools) + LLM for explanation generation | Hybrid: deterministic optimizer + LLM explanations |
| OCR Receipt Scanning | Vision model (Thai receipt trained) + structured extraction | GPT-4o Vision / Claude Vision |
| Personalized Tips | LLM + user profile + bracket analysis | GPT-4o |
| Filing Validation | Rule engine (not LLM — must be 100% accurate) | Deterministic |

**RAG Knowledge Base:**
- Thai Revenue Code (full text, embedded)
- RD Rulings & Ministerial Regulations
- Double Tax Treaties (61 countries)
- BOI Announcements & Activity Catalogs
- Tax Court Decisions (precedent)

### 8.4 Key Technical Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Tax Calculation | Deterministic engine (Python/Go) | Must be 100% accurate; no LLM hallucination risk |
| Deduction Rules | Versioned JSON rulesets | Easy to update for law changes; auditable |
| Optimization | OR-Tools constraint solver | Proven; can handle 30+ variables with complex constraints |
| LLM Role | Explanation + interview + tips | LLM for UX/narrative; deterministic engine for calculation |
| Mobile | PWA + Line Mini App | Thailand mobile-first; Line is the super-app |
| Language | Thai-native + EN toggle | Must serve Thai market first |
| Data Privacy | On-premise / Thai-hosted option | PDPA compliance; sensitivity of tax data |

---

## 9. Monetization & Business Model

### 9.1 Revenue Streams

| Stream | Description | Est. Y1 |
|--------|-------------|--------|
| Individual Subscriptions | ฿299/year Pro plan | ฿2.4M |
| Filing Season Pass | ฿299 one-time (Jan-Apr) | ฿4.5M |
| Business Starter | ฿999/mo SME plan | ฿4.8M |
| Business Pro | ฿1,990/mo enterprise plan | ฿3.6M |
| Affiliate Revenue | Insurance/broker referrals | ฿2-5M |
| **Total (conservative)** | | **฿15-20M** |

### 9.2 Affiliate & Partnership Model

- **Insurance marketplace:** Users who need life/health insurance → partner links to AIA, Muang Thai, Bangkok Insurance (commission: 10-20% of first-year premium)
- **Fund platforms:** RMF/SSF/ThaiESG purchase links → SCB Asset Management, K Asset, BBL Asset Management
- **Accounting firms:** Referral for complex corporate cases → revenue share with partner accounting firms
- **Bank partnerships:** White-label calculator for banking apps → licensing fee

### 9.3 Cost Structure

| Cost Category | Est. Monthly | Annual |
|--------------|-------------|--------|
| LLM API Costs (GPT-4o, Claude) | ฿150,000 | ฿1.8M |
| Cloud Infrastructure (GCP/AWS) | ฿80,000 | ฿960K |
| Engineering (4 FTE) | ฿400,000 | ฿4.8M |
| Tax Expert Consulting | ฿100,000 | ฿1.2M |
| Marketing & Acquisition | ฿200,000 | ฿2.4M |
| **Total** | **฿930,000** | **฿11.16M** |

**Path to profitability:** Month 8-10 at projected growth rates.

---

## 10. Go-to-Market Roadmap

### Phase 1: MVP (Months 1-3)
- [ ] Tax Calculator (full individual)
- [ ] Deduction database (all 30+ deductions)
- [ ] Basic Tax Timeline with filing deadlines
- [ ] Free tier launch + no-login calculator
- [ ] Thai language UI
- [ ] Blog/SEO: "Ultimate Thai Tax Deduction Guide 2025"

### Phase 2: AI Features (Months 4-6)
- [ ] AI Deduction Optimizer
- [ ] Interview wizard
- [ ] What-If Scenario Builder
- [ ] Personalized Tax Tips engine
- [ ] RAG knowledge base (Thai Revenue Code)
- [ ] Paid tier launch (Pro Individual)

### Phase 3: Platform Expansion (Months 7-9)
- [ ] Document Manager with OCR
- [ ] Filing Assistant (PND 90/91)
- [ ] Year-Round Tracker dashboard
- [ ] Line OA integration (reminders)
- [ ] Mobile PWA
- [ ] Affiliate marketplace (insurance, funds)

### Phase 4: Corporate (Months 10-14)
- [ ] Corporate Tax Calculator
- [ ] PND 50/51 filing prep
- [ ] Depreciation scheduler
- [ ] BOI tracker
- [ ] Accounting software integrations
- [ ] Business tier launch

### Phase 5: Scale (Months 15+)
- [ ] Direct RD e-Filing integration
- [ ] Bank/broker data import
- [ ] Transfer pricing assistant
- [ ] White-label partner program
- [ ] Multi-country expansion (Vietnam, Indonesia)

---

## 11. Risk & Compliance

### 11.1 Regulatory Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Tax advice liability | High | Clear disclaimer: "Educational tool, not professional tax advice"; recommend accountant review for complex cases |
| RD e-Filing API changes | Medium | Abstract filing layer; monitor RD announcements; fallback to PDF export |
| PDPA compliance (tax data) | High | Data hosted in Thailand (or Thai DC option); encryption at rest; data retention policy; user data export/delete |
| Incorrect calculation | Critical | Deterministic engine with 10,000+ test cases; audit logging; version rollback |
| BOI rule changes | Medium | Modular ruleset updates; BOI announcement monitoring pipeline |

### 11.2 Product Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Low conversion from free | Medium | Clear upgrade triggers at moments of value (e.g., "See your 3 missing deductions → Upgrade"); time-limited free trial |
| LLM hallucination in tax advice | High | LLM only for explanation/narrative; never for calculation; RAG with Revenue Code for factual grounding |
| Seasonal usage drop (May-Oct) | Medium | Year-Round Tracker feature to maintain engagement; corporate (year-round) to offset individual seasonality |
| Competitor entry | Medium | First-mover advantage in Thai market; build brand trust; network effects from accountant partnerships |

### 11.3 Disclaimers (Required)

```
⚠️ IMPORTANT LEGAL DISCLAIMERS (Must be displayed):

1. LegalAI Tax is an educational and planning tool. It is NOT a substitute
   for professional tax advice from a qualified accountant or tax attorney.

2. Tax calculations are estimates based on information you provide. Final
   tax liability is determined by the Thai Revenue Department.

3. Deduction eligibility depends on specific circumstances and Revenue
   Department interpretation. Consult a professional before claiming.

4. LegalAI is not responsible for tax underpayments, penalties, or audit
   outcomes resulting from use of this tool.

5. Tax laws change frequently. We update our rulesets within 30 days of
   published changes, but always verify with the Revenue Department.
```

---

## 12. Appendix: Data Models

### 12.1 User Tax Profile

```json
{
  "user_id": "uuid",
  "tax_year": 2025,
  "filing_type": "individual",
  "personal_info": {
    "date_of_birth": "1990-05-15",
    "nationality": "TH",
    "resident_since": "1990-01-01"
  },
  "income": {
    "employment": {
      "monthly_salary": 85000,
      "bonus": 150000,
      "total_annual": 1170000
    },
    "freelance": {
      "annual_revenue": 200000,
      "expenses_actual": 50000
    },
    "rental": {
      "annual_rent": 180000
    },
    "investment": {
      "dividends_thai": 15000,
      "interest_bank": 3000
    }
  },
  "family": {
    "marital_status": "married",
    "spouse_has_income": false,
    "children": [
      {"age": 8, "studying": true},
      {"age": 5, "studying": false}
    ],
    "parents_over_60": [
      {"relation": "own", "income": 0},
      {"relation": "own", "income": 15000}
    ]
  },
  "deductions_current": {
    "social_security": 9000,
    "provident_fund": 60000,
    "life_insurance": 80000,
    "health_insurance": 15000,
    "rmf": 100000,
    "ssf": 50000,
    "thaiesg": 0,
    "mortgage_interest": 85000,
    "donations": 5000
  },
  "available_cash": 200000
}
```

### 12.2 Deduction Rule Schema

```json
{
  "deduction_id": "rmf",
  "name_th": "กองทุนรวมเพื่อการเลี้ยงชีพ (RMF)",
  "name_en": "Retirement Mutual Fund (RMF)",
  "tax_year": 2025,
  "category": "investment",
  "max_amount": 500000,
  "max_percent_of_income": 30,
  "conditions": [
    {"field": "age", "operator": "gte", "value": 0},
    {"field": "rmf_units_bought_annually", "operator": "eq", "value": true}
  ],
  "holding_period": "until_age_55",
  "shared_limit_with": ["provident_fund", "pension_insurance", "government_pension"],
  "deadline": "2025-12-31",
  "priority": 8
}
```

### 12.3 Tax Calculation Result

```json
{
  "tax_year": 2025,
  "gross_income": 1170000,
  "total_deductions": 385000,
  "taxable_income": 785000,
  "tax_brackets": [
    {"bracket": "0%", "from": 0, "to": 150000, "amount": 150000, "tax": 0},
    {"bracket": "5%", "from": 150001, "to": 300000, "amount": 150000, "tax": 7500},
    {"bracket": "10%", "from": 300001, "to": 500000, "amount": 200000, "tax": 20000},
    {"bracket": "15%", "from": 500001, "to": 750000, "amount": 250000, "tax": 37500},
    {"bracket": "20%", "from": 750001, "to": 785000, "amount": 35000, "tax": 7000}
  ],
  "total_tax": 72000,
  "effective_rate": 6.15,
  "marginal_rate": 20,
  "withholding_paid": 95000,
  "tax_refund_estimate": 23000,
  "optimization": {
    "potential_savings": 18500,
    "recommendations": [
      {
        "deduction": "rmf",
        "current": 100000,
        "max_possible": 251000,
        "recommended": 151000,
        "tax_saved": 22650,
        "action": "Invest additional ฿51,000 in RMF before Dec 31"
      }
    ]
  }
}
```

---

## Document Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-08-09 | LegalAI Product Team | Initial comprehensive specification |

---

> **Next Steps:**
> 1. Review with tax domain expert (CPA/Thai tax lawyer) for deduction accuracy
> 2. Validate progressive rates and SME brackets against latest RD announcements
> 3. Prototype Tax Calculator UI (Figma)
> 4. Build deduction ruleset JSON for 2024 and 2025 tax years
> 5. Develop MVP scope document based on Phase 1 roadmap
