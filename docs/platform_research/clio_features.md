# Clio Feature Catalog

> **Platform**: Clio (clio.com) — World's largest cloud-based legal practice management platform  
> **Users**: 400,000+ legal professionals globally  
> **Founded**: 2008 | **HQ**: Burnaby, BC, Canada  
> **Model**: SaaS, cloud-native, multi-tenant  
> **Last Updated**: August 2026

---

## Table of Contents

1. [Clio Manage — Core Practice Management](#1-clio-manage--core-practice-management)
2. [Clio Grow — Client Intake & CRM](#2-clio-grow--client-intake--crm)
3. [Clio Draft — Document Automation](#3-clio-draft--document-automation)
4. [Clio Accounting — Financial Management](#4-clio-accounting--financial-management)
5. [Clio Duo — AI Across the Platform](#5-clio-duo--ai-across-the-platform)
6. [Client Portal — Secure Client Collaboration](#6-client-portal--secure-client-collaboration)
7. [Mobile App — Law Firm on the Go](#7-mobile-app--law-firm-on-the-go)
8. [Clio for Clients — Client-Side App](#8-clio-for-clients--client-side-app)
9. [App Integrations Marketplace](#9-app-integrations-marketplace)
10. [Pricing Tiers](#10-pricing-tiers)

---

## 1. Clio Manage — Core Practice Management

Clio Manage is the flagship product — a unified cloud-based practice management platform that centralizes every aspect of running a law firm. It is the hub into which all other Clio modules plug.

### 1.1 Case & Matter Management

**What it does**: Provides a centralized, structured repository for every legal matter the firm handles. Each matter has its own dashboard/profile containing all related data — client info, opposing parties, case type, practice area, status, deadlines, documents, time entries, expenses, communications, tasks, and notes.

**Detailed features**:
- **Matter Dashboard**: Single-pane view of every open/closed matter with key metadata (case number, court, judge, practice area, status, dates, assigned attorney)
- **Matter Types & Custom Fields**: Configurable matter types (litigation, transactional, family law, immigration, etc.) with unlimited custom fields to capture practice-area-specific data
- **Matter Status Tracking**: Configurable workflow stages (Intake → Active → Settlement → Trial → Closed) with filtering and reporting
- **Related Contacts**: Link clients, opposing counsel, judges, experts, witnesses, and other parties to each matter
- **Matter Notes & Timeline**: Chronological activity log capturing every event, communication, and update
- **Conflict Checking**: Built-in conflict-of-interest search across all contacts and matters before accepting new clients
- **Bulk Actions**: Merge matters, reassign attorneys, change statuses in bulk
- **Matter Import/Export**: Migration tools for importing data from other systems

**User flow**:
1. Create a new matter (or convert from Clio Grow lead)
2. Assign practice area, responsible attorney, and status
3. Add parties (client, opposing counsel, judge, etc.)
4. Populate custom fields relevant to the practice area
5. Throughout the matter lifecycle: log time, upload documents, schedule deadlines, record communications
6. Close the matter with final billing and archiving

**Pain point solved**: Lawyers previously managed case details across spreadsheets, paper files, email folders, and disparate systems. No single source of truth existed, leading to missed deadlines, lost information, and inefficient handoffs between staff.

### 1.2 Contact Management

**What it does**: A full CRM-like contact database for everyone the firm interacts with — clients, prospects, opposing counsel, judges, experts, witnesses, vendors, and referral sources.

**Detailed features**:
- **Unified Contact Records**: Each contact has a profile with contact details, associated matters, communications history, documents, and billing history
- **Contact Roles**: Assign multiple roles per contact (e.g., a person can be both a client in one matter and a witness in another)
- **Relationship Mapping**: Link contacts to each other (spouse, employer, opposing party)
- **Contact Import**: Bulk import from CSV, Outlook, Gmail, or other systems
- **Custom Fields**: Practice-area-specific fields on contact records
- **Contact Notes**: Internal notes on each contact
- **Duplicate Detection & Merge**

**User flow**:
1. Add contact manually or via import/integration
2. Link to matters, assign roles
3. All communications with that contact are logged automatically (via email integration)
4. View full history — matters, bills, documents, communications — from the contact record

**Pain point solved**: Contact information scattered across attorneys' personal address books, email clients, and paper Rolodexes. No firm-wide visibility into who knew whom or what communications had occurred.

### 1.3 Calendaring

**What it does**: Shared firm calendar with legal-specific features including court rules-based date calculation, deadline tracking, and calendar synchronization.

**Detailed features**:
- **Shared Firm Calendar**: Multi-user calendar with color-coding by attorney, matter, or event type
- **Court Rules-Based Scheduling**: Automatic deadline calculation based on jurisdiction-specific court rules (e.g., response due 30 days after service, accounting for weekends/holidays)
- **Calendar Sync**: Two-way sync with Google Calendar, Outlook/Office 365, and Apple Calendar
- **Event Types**: Appointments, court dates, deadlines, tasks, reminders
- **Matter-Linked Events**: Every event is tied to a matter for context
- **Recurring Events**: Weekly staff meetings, monthly billing runs
- **Calendar Rules**: Automated workflows (e.g., when a trial date is set, auto-create all pre-trial deadlines)
- **Calendar Sharing**: Share availability with clients for self-scheduling (via Clio Grow)
- **Reminders & Notifications**: Email and in-app reminders

**User flow**:
1. Enter a trigger date (e.g., complaint filed, trial set)
2. Clio calculates all downstream deadlines per court rules
3. Deadlines populate the shared firm calendar
4. Reminders fire as deadlines approach
5. Any changes to the trigger date cascade updates

**Pain point solved**: Attorneys manually calculating deadlines from court rules (error-prone, risking malpractice). Calendars siloed per attorney with no firm-wide visibility into who is available or what deadlines are approaching.

### 1.4 Task Management

**What it does**: Assign, track, and complete tasks across the firm with matter context.

**Detailed features**:
- **Task Creation**: Create tasks linked to matters with assignee, due date, priority, and description
- **Task Lists & Kanban Boards**: View tasks as lists or Kanban boards by status
- **Matter Task Templates**: Pre-built task checklists per practice area (e.g., "Divorce Filing Checklist" with 40 steps)
- **Automated Task Creation**: Trigger task generation from calendar events, matter stage changes, or intake completion
- **Task Dependencies**: Link tasks as prerequisites
- **My Tasks Dashboard**: Personal view of all assigned tasks across matters
- **Delegation & Reassignment**
- **Time Tracking from Tasks**: Convert completed tasks into billable time entries

**User flow**:
1. Create a task template for a practice area (or use a pre-built one)
2. Apply template to new matter → all tasks auto-generated
3. Team members see their tasks on their dashboard
4. Mark tasks complete; time entries optionally created
5. Track matter progress via task completion percentage

**Pain point solved**: No systematic way to ensure every step of a legal process is completed. Checklists existed in attorneys' heads or on paper. Tasks fell through cracks when staff changed or workloads spiked.

### 1.5 Document Management

**What it does**: Cloud-based document storage, organization, and collaboration with version control.

**Detailed features**:
- **Unlimited Document Storage**: All plans include unlimited storage
- **Folder Organization**: Matter-based folder structure with sub-folders
- **Document Upload**: Drag-and-drop, email-to-matter, mobile scan, bulk upload
- **Version Control**: Track document versions; revert to previous versions
- **Full-Text Search**: Search across all document contents
- **Document Tagging & Categorization**
- **Document Merge**: Auto-populate templates with matter data
- **Integration**: Sync with Dropbox, Box, Google Drive, OneDrive, NetDocuments
- **Annotation & Redaction**: Mark up and redact documents
- **Document Sharing**: Secure sharing with clients via the portal (with permissions)

**User flow**:
1. Upload document to a matter (drag-and-drop, email, scan, or integration sync)
2. Document is indexed for full-text search
3. Team members can view, annotate, download, or share
4. New versions replace or supplement the original
5. Share securely with client via portal link

**Pain point solved**: Documents stored on local servers, individual PCs, or email attachments. No version control meant staff worked from outdated drafts. No search capability meant hunting through folders.

---

## 2. Clio Grow — Client Intake & CRM

Clio Grow is the firm's growth engine — handling everything from first contact to signed engagement letter. It is a legal-specific CRM and intake automation platform.

### 2.1 Client Intake

**What it does**: Automates the entire client intake process from initial inquiry to signed retainer, replacing paper forms and manual data entry.

**Detailed features**:
- **Online Intake Forms**: Customizable, mobile-responsive web forms that prospects fill out; data flows directly into Clio
- **Conditional Logic Forms**: Forms that adapt based on answers (e.g., "If divorce, show child custody questions")
- **E-Signature on Intake Forms**: Clients sign intake documents electronically
- **Automated Conflict Checks**: Run conflict-of-interest checks automatically when a new intake comes in
- **Engagement Letter Generation**: Auto-generate engagement letters populated with intake data
- **Document Upload Collection**: Request and receive documents from prospects during intake
- **Intake Status Pipeline**: Visual pipeline tracking each lead through intake stages (New → Contacted → Consult Scheduled → Retainer Sent → Signed → Converted)
- **Intake Checklists**: Automated task lists per matter type triggered by intake completion

**User flow**:
1. Firm creates branded intake form(s) for each practice area
2. Form is embedded on firm website, shared via link, or sent via email
3. Prospect completes form → data flows into Clio Grow
4. Automated conflict check runs; if clear, lead advances
5. Engagement letter auto-generates and is sent for e-signature
6. Upon signing, the lead converts to a Clio Manage matter with all data intact

**Pain point solved**: Intake previously required phone tag, paper forms, manual data entry, and stacks of paper. Leads were lost in the gap between inquiry and engagement. Conflict checks were done ad hoc (or forgotten). Converting an intake to a matter required re-entering all data.

### 2.2 Lead Tracking & Pipeline Management

**What it does**: A legal-specific CRM for tracking every potential client from first contact through conversion (or loss), with pipeline visibility and analytics.

**Detailed features**:
- **Lead Capture**: Collect leads from website forms, phone calls, email, Google Local Services Ads, and integrations
- **Visual Pipeline**: Kanban-style pipeline view showing leads at each stage
- **Custom Pipeline Stages**: Configure stages per practice area
- **Lead Scoring & Tagging**: Tag leads by source, practice area, urgency, value
- **Activity Tracking**: Log calls, emails, meetings per lead
- **Automated Follow-ups**: Trigger email sequences based on lead stage or inactivity
- **Lead Source Attribution**: Track which marketing channel generated each lead
- **Conversion Analytics**: Pipeline reports showing conversion rates, time-to-convert, and lead source ROI
- **Lead Assignment**: Auto-assign or manually route leads to specific attorneys

**User flow**:
1. Lead enters system (form, phone, referral, ad)
2. Lead is tagged, scored, and placed in pipeline
3. Automated email sequence begins (acknowledgment, education, consultation booking)
4. Staff log interactions and advance the lead through stages
5. Converted leads become Clio Manage matters; lost leads are archived with reason codes
6. Analytics dashboard shows pipeline health and conversion metrics

**Pain point solved**: Law firms had no systematic way to track prospects. Leads lived in attorneys' email inboxes or on sticky notes. No visibility into conversion rates, pipeline value, or which marketing channels actually produced clients.

### 2.3 Client Relationship Management (CRM)

**What it does**: Ongoing relationship management for existing and past clients — not just leads — for referrals and repeat business.

**Detailed features**:
- **Client Database**: All clients (active and past) with full interaction history
- **Referral Source Tracking**: Track who referred each client; identify top referral sources
- **Birthday & Anniversary Reminders**: Automated touchpoint opportunities
- **Email Campaigns**: Send newsletters, holiday greetings, legal updates to client segments
- **Client Satisfaction Surveys**: Automated post-matter NPS/satisfaction surveys
- **Review Generation**: Encourage and collect Google/Facebook reviews from happy clients
- **Cross-Sell Identification**: Flag opportunities for additional services based on client profile

**User flow**:
1. Past clients remain in the CRM after matter closure
2. Automated touchpoints fire (birthday, matter anniversary, annual check-in)
3. Firm sends segmented email campaigns (estate planning updates to all clients over 50, etc.)
4. Referral sources are tracked and nurtured
5. Repeat business and referrals are attributed back to source

**Pain point solved**: Law firms treated clients as one-and-done. No systematic nurturing for repeat business or referrals. The "hidden practice" of past clients who would return or refer was left entirely to chance.

### 2.4 Email Marketing

**What it does**: Built-in email marketing for legal practices — newsletters, drip campaigns, and automated sequences.

**Detailed features**:
- **Email Campaign Builder**: Drag-and-drop email builder with legal-specific templates
- **Contact Segmentation**: Segment by practice area, matter type, location, custom tags
- **Automated Sequences**: Drip campaigns triggered by lead stage, time elapsed, or client action
- **Email Templates**: Library of pre-built legal email templates (consultation follow-up, retainer reminder, holiday greeting)
- **Open/Click Tracking**: Analytics on email performance
- **CAN-SPAM Compliance**: Built-in unsubscribe and compliance features
- **Integration with Intake**: Auto-enroll leads in nurture sequences from the moment they submit an intake form

**User flow**:
1. Create email template or sequence
2. Define trigger (e.g., 1 day after intake submission, 30 days after matter close)
3. Segment defines who receives it
4. Emails send automatically
5. Track opens, clicks, and resulting consultations

**Pain point solved**: Most small/medium law firms do zero marketing. Those that try use Mailchimp or Constant Contact disconnected from their case data, so they can't target by practice area or matter stage. No automated nurture meant leads went cold.

### 2.5 Appointment Scheduling

**What it does**: Self-service appointment booking that eliminates "calendar tennis" (back-and-forth emails to find a time).

**Detailed features**:
- **Booking Page**: Public-facing scheduling page showing attorney availability
- **Calendar Integration**: Syncs with Clio Manage calendar and external calendars (Google, Outlook)
- **Automated Reminders**: Email/SMS reminders before appointments
- **Intake Form Pre-Consultation**: Require intake form completion before booking
- **Buffer Times & Availability Rules**: Set per-attorney availability, meeting durations, and buffer times
- **Video Conferencing Links**: Auto-generate Zoom/Google Meet links for virtual consultations

**User flow**:
1. Lead receives link to booking page (via email, website, or intake form)
2. Lead selects service type, attorney (if applicable), and available time slot
3. Appointment is confirmed; both parties receive calendar invite with video link
4. Automated reminders fire 24h and 1h before
5. Before appointment, attorney reviews the lead's intake form data

**Pain point solved**: The average law firm exchanges 4-6 emails to schedule a single consultation. Staff time wasted on scheduling. Leads dropped off during the scheduling dance.

---

## 3. Clio Draft — Document Automation

Clio Draft (formerly Lawyaw, acquired by Clio) is a document automation platform that turns static legal documents into intelligent, data-driven templates. It is available as an add-on to Clio Manage.

### 3.1 Intelligent Document Automation

**What it does**: Converts Microsoft Word documents and PDFs into fillable, logic-driven templates that auto-populate with Clio matter and contact data.

**Detailed features**:
- **Word-to-Template Conversion**: Upload an existing Word document; Clio Draft identifies fields and converts them into template variables — no coding required
- **Conditional Logic**: Templates can show/hide sections based on answers (e.g., "If children = yes, include custody provisions")
- **Repeatable Sections**: Create loops for multiple parties, assets, children, etc.
- **Calculated Fields**: Auto-compute values (dates, amounts, formulas)
- **Clio Data Merge**: Auto-populate templates with client name, address, matter number, opposing party, court info, and any custom field from Clio Manage
- **Template Library**: Pre-built starter templates for common practice areas
- **Multi-Party Document Sets**: Generate entire document packages from a single questionnaire (e.g., divorce petition + financial affidavit + parenting plan)
- **Version Control**: Track template versions; update once, regenerate all documents
- **E-Signature Integration**: Send generated documents for e-signature directly

**User flow**:
1. Upload a Word document or select from the template library
2. Tag variable fields (or let AI suggest them)
3. Add conditional logic and calculations as needed
4. Save template to firm library
5. From a Clio matter, select the template; fill out a questionnaire (or data auto-populates from Clio)
6. Document generates instantly with all data merged
7. Review, finalize, and send for e-signature

**Pain point solved**: Legal documents are highly repetitive but require meticulous accuracy. Attorneys spend hours copying/pasting client data between documents, introducing errors. Paralegals maintain multiple versions of "standard" documents that drift apart over time. A single document set (e.g., estate plan) can take 3-5 hours of manual assembly.

### 3.2 Court Forms Library

**What it does**: Cloud-based access to official, fillable court forms for all 50 U.S. states plus U.S. immigration forms — kept current with court updates.

**Detailed features**:
- **50-State Coverage**: Official court forms for every U.S. state jurisdiction
- **Immigration Forms**: USCIS and EOIR immigration forms
- **Auto-Population**: Fill court forms with data from Clio Manage (client info, case details)
- **Auto-Update**: Clio maintains form currency; when courts update forms, templates update automatically
- **Form Sets**: Group related forms for common filings (e.g., "California Divorce — Initial Filing Set")
- **Form Preview & Validation**: Preview completed forms; flag missing required fields before filing
- **Electronic Filing Ready**: Output forms in court-acceptable formats for e-filing

**User flow**:
1. Select jurisdiction and form type from the library
2. Link to a Clio matter; form auto-populates with known data
3. Complete remaining fields via questionnaire
4. Preview and validate
5. Download/print for filing or e-file integration

**Pain point solved**: Court forms change frequently; firms using static PDFs or paper forms risk using outdated versions (leading to rejected filings). Manually filling the same client information across dozens of court forms is tedious and error-prone. Finding, downloading, and maintaining form libraries per jurisdiction is a full-time overhead.

### 3.3 Clio Draft Pricing

- **Cloud-Based Court Forms**: ~$70/user/month
- **Intelligent Document Automation**: ~$110/user/month
- Both available as add-ons to Clio Manage subscriptions

---

## 4. Clio Accounting — Financial Management

Clio Accounting is a legal-specific accounting solution built directly into Clio Manage, eliminating the need for separate accounting software and the reconciliation headaches between practice management and accounting systems.

### 4.1 Time Tracking

**What it does**: Capture billable and non-billable time from anywhere — desktop, mobile, or within workflow.

**Detailed features**:
- **Multiple Timer Modes**: Running timers (start/stop), manual entry, and bulk time entry
- **Matter-Linked Time Entries**: Every time entry is tied to a matter and activity type
- **Activity Codes**: Standard UTBMS/LEDES codes for corporate legal billing
- **Time Entries from Calendar**: Convert calendar events to time entries
- **Time Entries from Tasks**: Convert completed tasks to billable time
- **Time Entries from Email**: Log time from Outlook/Gmail integration
- **Mobile Time Tracking**: Capture time from iOS/Android app (including offline)
- **Minimum Time Increments**: Enforce billing increments (e.g., 0.1 hour / 6-minute minimum)
- **Non-Billable Time Tracking**: Track admin, pro bono, and firm development time
- **Time Approval Workflows**: Require supervisor approval before billing
- **Time Entry Notes**: Required or optional narrative fields per firm policy
- **Billable Hour Goals**: Set and track against individual billable hour targets

**User flow**:
1. Attorney clicks "Start Timer" on a matter or from the global timer
2. Works on the matter; timer runs in background
3. Stops timer; adds activity code and narrative
4. Alternatively: logs time in batch at end of day/week
5. Time entries flow to billing for invoice generation

**Pain point solved**: Attorneys are notorious for under-capturing billable time. Studies show lawyers lose 10-30% of billable hours due to delayed or forgotten time entry. Paper timesheets and post-it-note tracking resulted in lost revenue and billing disputes.

### 4.2 Billing & Invoicing

**What it does**: Generate, customize, and send legal invoices in multiple formats with flexible billing arrangements.

**Detailed features**:
- **Invoice Generation**: Auto-generate invoices from unbilled time and expenses
- **Multiple Billing Types**: Hourly, flat fee, contingency, and hybrid arrangements
- **Split Billing**: Divide invoices across multiple parties (client + employer + insurance)
- **Payment Plans**: Create and track installment payment schedules
- **LEDES Billing**: Generate LEDES-format invoices for corporate legal clients (LEDES 1998B, 1998BI, etc.)
- **Custom Invoice Templates**: Brand invoices with firm logo, custom fields, and messaging
- **Bulk Billing**: Generate invoices for multiple matters in one batch
- **Pre-Bill Review**: Review and adjust draft invoices before sending
- **Interest on Late Payments**: Auto-calculate and apply interest charges
- **Write-Offs & Adjustments**: Write down time/expenses before or after billing
- **Invoice History**: Full audit trail of all invoices, payments, and adjustments

**User flow**:
1. Review unbilled time and expenses for a matter
2. Adjust as needed (write off, edit narrative, reorder)
3. Generate draft invoice
4. Review and finalize
5. Send to client via email (with payment link) or client portal
6. Alternatively: generate LEDES file for corporate e-billing system

**Pain point solved**: Legal billing is complex — multiple fee arrangements, split billing, trust accounting compliance, and corporate e-billing requirements. Manual invoicing in Word/Excel was error-prone, non-compliant, and slow. Firms waited 60-90 days for payment because invoices were hard to pay.

### 4.3 Trust Accounting

**What it does**: Full IOLTA/trust account management with three-way reconciliation, compliant with state bar requirements.

**Detailed features**:
- **Trust Account Ledgers**: Separate ledgers per client trust account
- **Three-Way Reconciliation**: Reconcile trust bank balance ↔ trust ledger balance ↔ sum of individual client trust ledgers — the gold standard for bar compliance
- **IOLTA Compliance**: Built-in rules preventing trust account overdrafts and commingling
- **Trust Deposits & Disbursements**: Record trust transactions with required documentation
- **Trust-to-Operating Transfers**: Transfer earned fees from trust to operating with proper documentation
- **Trust Checks**: Print trust account checks
- **Trust Reports**: Generate trust liability reports, reconciliation reports, and transaction histories
- **Audit Trail**: Complete, immutable record of all trust account activity
- **State Bar Compliance**: Reports formatted for common state bar audit requirements

**User flow**:
1. Receive client retainer → deposit into trust account → record in Clio
2. Funds appear in client's trust ledger
3. As work is performed and billed, transfer earned fees from trust to operating account
4. Monthly: run three-way reconciliation
5. Generate trust reports for internal review and bar compliance
6. At matter close: return any remaining trust balance to client

**Pain point solved**: Trust accounting violations are the #1 cause of attorney discipline nationwide. Manual trust accounting in Excel or general-purpose accounting software does not enforce IOLTA rules and makes three-way reconciliation extremely difficult. A single error can result in bar complaints, license suspension, or disbarment.

### 4.4 Online Payments (Clio Payments)

**What it does**: Built-in payment processing that lets clients pay legal bills online — powered by Clio's own payment gateway.

**Detailed features**:
- **Clio Payments**: Native payment processing (no third-party gateway required)
- **Credit/Debit Card Payments**: Visa, Mastercard, American Express, Discover
- **eCheck/ACH Payments**: Bank account transfer payments
- **Payment Links in Invoices**: Every invoice includes a "Pay Now" button
- **Client Portal Payments**: Clients view and pay bills through the secure portal
- **Payment Plans**: Set up recurring/scheduled payments for installment arrangements
- **Trust-Compliant Processing**: Separate workflows for operating account and trust account payments
- **Surcharge Management**: Optionally pass credit card processing fees to clients (where legal)
- **Payment Reconciliation**: Auto-match payments to invoices and sync with accounting
- **Payment Tracking**: Real-time dashboard showing paid, pending, and overdue invoices

**User flow**:
1. Invoice is sent with embedded "Pay Now" link
2. Client clicks link, enters payment details
3. Payment processes; funds settle to operating or trust account (as appropriate)
4. Invoice is marked paid in Clio
5. Transaction syncs to Clio Accounting general ledger

**Pain point solved**: Law firms historically collected 60-70% of invoices within 60 days. Paper checks required manual handling, trips to the bank, and reconciliation. Clients had friction to pay (write check, find stamp, mail). Online payments reduce collection time to days, not months.

### 4.5 Financial Reporting

**What it does**: Legal-specific financial reports for firm management, profitability analysis, and compliance.

**Detailed features**:
- **General Ledger**: Full double-entry accounting with chart of accounts
- **Accounts Payable & Receivable**: Track what the firm owes and is owed
- **Profit & Loss (P&L)**: Firm income statement by period
- **Balance Sheet**: Assets, liabilities, and equity
- **Trust Account Reports**: Trust liability, reconciliation, and transaction reports
- **Revenue by Practice Area**: Profitability analysis per practice area
- **Revenue by Attorney**: Individual attorney performance
- **Realization & Collection Rates**: Hours billed vs. hours collected; invoice amounts vs. amounts collected
- **Aging Reports**: Accounts receivable aging (30/60/90+ days)
- **Expense Tracking**: Firm expenses by category
- **Tax Preparation Reports**: Data export for CPA/tax preparer
- **Cash vs. Accrual Accounting**: Support for both methods
- **Bank Reconciliation**: Reconcile operating and trust accounts against bank statements

**User flow**:
1. Firm sets up chart of accounts (or uses legal-specific default)
2. All financial activity (time, expenses, payments, trust transactions) flows into the general ledger
3. Monthly: reconcile bank accounts
4. Generate P&L, balance sheet, and AR aging reports
5. Review firm financial health; identify profitable/unprofitable practice areas
6. Year-end: export data for tax preparation

**Pain point solved**: Law firms using QuickBooks or Xero had to manually sync data between practice management and accounting — a source of constant errors and reconciliation headaches. General-purpose accounting software lacks trust accounting, doesn't understand legal billing, and can't produce legal-specific reports like realization rates.

---

## 5. Clio Duo — AI Across the Platform

Clio Duo is Clio's proprietary generative AI layer embedded throughout the platform. Think of it as an AI-powered legal partner that understands the firm's data, the law, and legal workflows. Launched October 2024 at the Clio Cloud Conference.

### 5.1 Core AI Capabilities

**What it does**: A conversational AI assistant that can answer questions about the firm's matters, draft documents, summarize information, and surface insights — all grounded in the firm's actual Clio data.

**Key features**:

**Matter Q&A / Natural Language Search**:
- Ask Duo questions about any matter: "What's the status of the Smith divorce case?" "When is the next deadline in the Johnson litigation?" "Who is the opposing counsel on the Brown matter?"
- Duo answers using real-time matter data — deadlines, contacts, recent activity, documents
- Eliminates the need to navigate through multiple screens to find information

**Matter & Document Summarization**:
- Summarize lengthy case notes, call logs, opposing counsel correspondence, deposition transcripts
- Get a quick "catch me up" summary of any matter's recent activity
- Summarize long documents — contracts, briefs, discovery responses — highlighting key points

**AI-Powered Drafting**:
- Generate first drafts of emails, letters, memos, and simple motions based on matter context
- Draft client update emails summarizing case progress
- Draft demand letters, engagement letters, and routine correspondence
- All output is grounded in the specific facts and data of the matter

**Matter Insights & Recommendations**:
- Surface upcoming deadlines and priorities across all matters
- Flag stalled matters that need attention
- Identify billing opportunities (unbilled time, approaching retainer depletion)
- Recommend next actions based on matter stage and practice area norms

**Calendar & Deadline Intelligence**:
- Ask "What do I have this week?" for an AI-curated briefing
- "What deadlines are coming up across all my cases?"
- "Which matters haven't had activity in 30 days?"

**Document Analysis**:
- Upload a document (opposing counsel's brief, discovery response, contract) and ask questions
- "What are the key arguments in this motion?"
- "What deadlines does this scheduling order set?"
- "Are there any concerning clauses in this contract?"

**Global Legal Knowledge**:
- Clio Duo is trained on a corpus of over a billion legal documents from 100+ countries
- Can answer general legal questions in addition to firm-specific ones

**User flow**:
1. Click the blue "D" (Duo icon) from anywhere in Clio
2. Chat interface opens; ask a question in natural language
3. Duo responds with information drawn from the firm's Clio data and/or its legal knowledge base
4. For drafting: ask Duo to draft something → review and edit the output → send or save

**Pain point solved**: Lawyers spend 40-60% of their time on non-billable administrative tasks — searching for information, summarizing documents, drafting routine correspondence. Duo compresses hours of these activities into minutes. It eliminates the "hunt and peck" through multiple screens to answer a simple question about a matter. It serves as a junior associate or paralegal for routine work product generation.

### 5.2 Duo Availability & Pricing

- Available to all Clio Manage subscribers (functionality varies by plan tier)
- Included in higher-tier plans; available as an add-on for lower tiers
- Powered by Clio's proprietary AI models, purpose-built for legal use cases

---

## 6. Client Portal — Secure Client Collaboration

The Client Portal (historically called Clio Connect) is the secure, client-facing web interface where clients can communicate with their lawyer, access documents, view bills, and sign documents.

### 6.1 Secure Messaging

**What it does**: Encrypted, attorney-client privileged communication channel that replaces unsecured email for case communications.

**Detailed features**:
- **Encrypted Messaging**: End-to-end encrypted messages between attorney and client
- **Matter-Linked Conversations**: Each conversation is tied to a specific matter for context
- **File Attachments**: Send and receive documents within messages
- **Read Receipts**: Know when your client has read a message
- **Notifications**: Email/push notifications when new messages arrive
- **Message Templates**: Pre-written message templates for common communications
- **Audit Trail**: Complete log of all client communications for the file

**User flow**:
1. Attorney invites client to the portal (via email)
2. Client creates a password and logs in
3. Both parties can send messages, share documents, and collaborate
4. All communications are automatically logged to the matter

**Pain point solved**: Attorney-client communications via regular email are not encrypted and are vulnerable to interception. Sensitive case information, settlement discussions, and privileged materials sent over unsecured email create malpractice exposure and potential waiver of privilege.

### 6.2 Document Sharing

**What it does**: Secure, permissioned document exchange between firm and client.

**Detailed features**:
- **Secure File Sharing**: Upload documents for client access; client uploads documents for attorney review
- **Folder Organization**: Matter-based folder structure visible to client
- **Permission Controls**: Granular control over what each client can see, download, or upload
- **Document Requests**: Request specific documents from clients with automated reminders
- **Bulk Download**: Clients can download all case documents as a zip
- **File Size Support**: Large file support for evidence, video depositions, etc.
- **Version Visibility**: Clients see only the latest shared versions (internal drafts stay private)

**User flow**:
1. Attorney uploads or designates documents for client sharing
2. Client receives notification of new documents
3. Client views, downloads, or uploads responsive documents
4. Attorney is notified of client uploads

**Pain point solved**: Email attachment size limits block sharing of large legal documents. Multiple email chains with attachments create version confusion — which draft is current? No audit trail exists for what was shared with whom and when.

### 6.3 E-Signatures

**What it does**: Built-in electronic signature capability for engagement letters, retainer agreements, settlement agreements, and other client-facing documents.

**Detailed features**:
- **E-Signature Requests**: Send documents for e-signature directly from Clio
- **Multi-Party Signing**: Route documents to multiple signers in sequence or parallel
- **Signer Authentication**: Email verification, access codes
- **Signature Placement**: Drag-and-drop signature, date, and initial fields onto documents
- **In-Person Signing**: Support for in-person e-signature capture on a tablet
- **Signature Tracking**: Real-time status of pending, viewed, and completed signatures
- **Completed Certificate**: Auto-generated signature certificate with audit trail
- **Document Storage**: Signed documents automatically saved to the matter

**User flow**:
1. Generate or upload the document requiring signature
2. Add signature fields and signer emails
3. Send for signature
4. Signers receive email with link; review and sign
5. All parties receive signed copy; certificate generated
6. Signed document auto-saved to matter

**Pain point solved**: Print-sign-scan-email is a 4-step friction cycle that delays matter progression. Physical signatures require in-person visits or postal mail — adding days or weeks. Wet signatures on paper documents are easily lost and difficult to track.

### 6.4 Bill Viewing & Payment

**What it does**: Clients can view their outstanding and paid invoices through the portal and pay online.

**Detailed features**:
- **Invoice Viewing**: Clients see all invoices, both paid and outstanding
- **Online Payment**: Pay directly through the portal via credit card or ACH
- **Payment History**: Full payment history with receipts
- **Trust Balance Viewing**: (optional) Clients can see their trust retainer balance

---

## 7. Mobile App — Law Firm on the Go

Clio's mobile app (iOS and Android) brings practice management to attorneys' phones and tablets.

### 7.1 Core Mobile Features

**What it does**: Full-featured mobile companion to Clio Manage for attorneys and staff who need to work from court, client meetings, or on the go.

**Detailed features**:

**Time & Expense Tracking**:
- Start/stop timers from mobile
- Log time entries with matter, activity code, and narrative
- Capture expenses with photo receipts
- Offline time tracking (syncs when reconnected)

**Matter Access**:
- View matter details, contacts, notes, and custom fields
- Search across all matters
- View recent activity and communications

**Calendar**:
- View personal and firm-wide calendars
- See matter-linked events and deadlines
- Create and edit events

**Document Access**:
- View, download, and share documents
- Upload documents via phone camera (scan-to-PDF) or file picker
- Annotate documents

**Contact Management**:
- View and search contacts
- Call, text, or email contacts directly from the app
- Add new contacts

**Communications**:
- Secure messaging with clients via the portal
- View communication history

**Billing**:
- View invoice statuses
- Accept payments (with card reader integration)

**Notifications**:
- Push notifications for new messages, deadline reminders, and task assignments

### 7.2 Mobile-Specific Features

- **Document Scanner**: Use phone camera as a document scanner with auto-crop, enhance, and PDF conversion
- **Photo Receipt Capture**: Photograph receipts for automatic expense entry
- **Offline Mode**: Core features work without internet; sync when connection restores
- **Biometric Lock**: Fingerprint/Face ID security for app access
- **Widget Support**: iOS/Android widgets for quick time tracking and today's calendar

**Pain point solved**: Attorneys working from court, depositions, or client sites had no access to case files, couldn't log time, and couldn't respond to client questions without returning to the office. The mobile app ensures billable time is captured as it happens (not reconstructed from memory later) and provides case information wherever the attorney is.

---

## 8. Clio for Clients — Client-Side App

Clio for Clients is a separate, free mobile app (iOS and Android) designed specifically for law firm clients to interact with their attorney through Clio.

### 8.1 Client-Side Features

**What it does**: A branded mobile experience where clients can communicate securely with their lawyer, access case documents, view bills, make payments, and stay informed about their case — all from their phone.

**Detailed features**:

**Secure Messaging**:
- Send and receive encrypted messages with the attorney
- Push notifications when attorney sends a message
- Matter-organized conversations

**Document Sharing**:
- View documents shared by the attorney
- Upload documents using the built-in scanner or camera roll
- Scan multi-page documents with the phone camera directly into the app

**Bill Management**:
- View outstanding and paid invoices
- Pay bills directly from the app via credit card or ACH
- View payment history and download receipts

**Case Information**:
- View matter status and key case details
- See upcoming appointments and deadlines
- Access shared calendar events

**Appointment Management**:
- View upcoming appointments
- Receive appointment reminders

**Multi-Firm Support**:
- If a client has matters with multiple Clio-using firms, they can switch between firms in the app

**Security**:
- Biometric authentication (fingerprint/face unlock)
- Encrypted data in transit and at rest
- No client data stored on device unless explicitly downloaded

**User flow**:
1. Attorney invites client to Clio for Clients
2. Client downloads the app and creates an account
3. Client sees their matters, can message the attorney, upload documents, view and pay bills
4. Push notifications keep the client informed of new messages, documents, and bills

**Pain point solved**: Legal clients often feel in the dark about their case status. They resort to calling the office for updates, which generates non-billable interrupt work for attorneys and staff. Providing a consumer-grade mobile experience (like their banking app) for legal matters improves client satisfaction, reduces status-check calls, and speeds up document exchange and payment.

---

## 9. App Integrations Marketplace

Clio's App Directory is one of the largest integration marketplaces in legal technology, with 250-300+ third-party applications that extend Clio's functionality.

### 9.1 Marketplace Overview

**What it does**: A curated directory of third-party applications that integrate with Clio, covering every aspect of legal practice. Integrations range from simple data sync to deep two-way workflow integrations.

**Scale**: 250-300+ apps across 40+ pages in the directory, organized by category.

### 9.2 Integration Categories

| Category | Examples | What They Do |
|---|---|---|
| **Accounting** | QuickBooks Online, Xero | Sync invoices, payments, and trust transactions with general accounting |
| **Document Management** | NetDocuments, Dropbox, Google Drive, Box, OneDrive | Sync documents between Clio and cloud storage platforms |
| **Email & Calendar** | Outlook, Gmail, Google Calendar, Office 365 | Two-way sync of email, contacts, and calendar events |
| **E-Signatures** | DocuSign, Adobe Sign, HelloSign | Send documents for signature with more advanced routing |
| **Payments** | LawPay, Headnote | Alternative payment processing options |
| **Communication** | Zoom, Microsoft Teams, RingCentral | Video conferencing and VoIP phone integration |
| **Court Filing** | File & Serve, One Legal, InfoTrack | E-file court documents directly from Clio |
| **Legal Research** | Fastcase, Westlaw, LexisNexis | Research integration with matter context |
| **Marketing & Intake** | Google Ads, Facebook, CallRail | Lead capture and marketing attribution |
| **Data Migration** | Lexicata, various migration tools | Import data from legacy systems |
| **Business Intelligence** | Power BI, Tableau, Lawmatics | Advanced analytics and reporting |
| **Productivity** | Zapier, Microsoft Power Automate | Connect Clio to 5000+ other apps via automation workflows |
| **Phone Systems** | Dialpad, RingCentral, Vonage | Click-to-call, call logging, and auto-time-entry from phone calls |
| **Website & Forms** | WordPress, Gravity Forms, Jotform | Website integration for intake and lead capture |
| **Practice-Specific** | Docketwise (immigration), Smokeball, various niche tools | Deep integrations for specific practice areas |

### 9.3 Key Integration Examples

**QuickBooks Online Integration**:
- Sync contacts (clients), invoices, payments, and trust transactions
- Eliminate double data entry between practice management and accounting

**Microsoft 365 / Outlook Integration**:
- Save emails to matters with one click
- Sync contacts and calendar events bidirectionally
- Log billable time from email activity

**Google Workspace Integration**:
- Sync with Gmail, Google Calendar, and Google Drive
- Save emails to matters; sync calendar events

**Dropbox / Box / OneDrive / Google Drive**:
- Auto-sync matter folders with cloud storage
- Access Clio documents through familiar file systems

**Zoom Integration**:
- Auto-generate Zoom links for calendar events
- Log meeting attendance to matters

**LawPay Integration**:
- Alternative payment gateway with legal-specific compliance features
- Trust account-compliant credit card processing

**Zapier**:
- Connect Clio to 5,000+ apps for custom automations
- Examples: Auto-create Clio matters from Typeform submissions, send Slack notifications for new matters, sync Clio contacts with Mailchimp

### 9.4 Clio's API

- RESTful API available for custom integrations
- Developer portal with documentation, SDKs, and sandbox environment
- Webhooks for event-driven integrations
- Used by integration partners and firms building custom solutions

**Pain point solved**: No single platform can do everything a law firm needs. Before integration marketplaces, firms either (a) used disconnected tools with manual data transfer, (b) paid for expensive custom integrations, or (c) forced their workflows into a single-vendor tool that didn't fit. Clio's marketplace provides a "best of breed" approach — Clio as the hub, with specialized tools connected as spokes.

---

## 10. Pricing Tiers

Clio uses a per-user-per-month subscription model with annual and monthly billing options. Pricing below reflects U.S. market rates as of 2026. All plans include unlimited document storage, bank-grade security, 99.9% uptime SLA, and 24/5 support.

### 10.1 Clio Manage Plans

| Plan | Monthly Price (per user) | Annual Price (per user) | Key Features |
|---|---|---|---|
| **Starter** | $49 | $39 | Case management, contact management, basic calendaring, basic document management, time tracking, basic billing (3 e-signatures), limited integrations. Best for: solo practitioners. |
| **Core** (formerly Boutique) | $69 | $59 | Everything in Starter + task management, client portal, advanced reporting, more integrations, e-signatures. Best for: small firms (2-5 users). |
| **Signature** (formerly Elite) | $99 | $79 | Everything in Core + advanced document management, court rules-based calendaring, LEDES billing, trust accounting, Clio Duo AI (limited), custom fields and workflows. Best for: growing firms (5-15 users). |
| **Elite** | $129+ | $109+ | Everything in Signature + full Clio Duo AI, advanced reporting & analytics, priority support, custom onboarding, dedicated account manager. Best for: established firms (15+ users). |

> Note: Plan names and pricing have evolved. Historical plan names in parentheses. Pricing is approximate and may vary by region and promotion.

### 10.2 Clio Grow Plans

| Plan | Monthly Price (per user) | Key Features |
|---|---|---|
| **Grow** | ~$59 | Client intake forms, lead pipeline, CRM, email marketing, appointment scheduling, e-signatures on intake docs |

### 10.3 Clio Draft (Add-on)

| Product | Monthly Price (per user) | Key Features |
|---|---|---|
| **Cloud-Based Court Forms** | ~$70 | State and immigration court forms library |
| **Intelligent Document Automation** | ~$110 | Word-to-template conversion, conditional logic, automated document generation |

### 10.4 Clio Accounting (Add-on)

- Pricing typically bundled with higher-tier Clio Manage plans or available as an add-on
- Specific pricing not publicly listed; contact sales

### 10.5 Clio Duo AI

- Included in Elite plan
- Available as an add-on for lower-tier plans
- Specific add-on pricing: contact sales

### 10.6 Bundle Savings

Clio offers bundle discounts when subscribing to multiple products (Manage + Grow + Draft). Bundles save 15%+ compared to individual subscriptions.

### 10.7 Free Trial

- 7-day free trial available for all products
- No credit card required

---

## Appendix: Cross-Cutting Platform Attributes

### Security & Compliance

- **SOC 2 Type II** certified
- **Bank-grade encryption** (AES-256 at rest, TLS 1.2+ in transit)
- **Two-factor authentication** (2FA) standard on all plans
- **Role-based access control** with granular permissions
- **Audit logs** tracking all user activity
- **Data residency** options for international firms
- **HIPAA compliance** available (Business Associate Agreement)
- **GDPR compliant** for EU/UK firms
- **Regular penetration testing** and vulnerability scanning

### Platform Architecture

- Cloud-native, multi-tenant SaaS
- 99.9% uptime SLA
- Automatic backups
- Web-based (any modern browser) + native mobile apps
- REST API for integrations
- Continuous deployment (multiple releases per week)

### Support

- 24/5 phone, email, and chat support (Monday-Friday)
- Extended hours for Elite plan
- Dedicated account manager for Elite plan
- Comprehensive help center with articles, videos, and webinars
- Clio Academy for training and certification
- Migration assistance for firms switching from other systems

### User Base & Market Position

- 400,000+ legal professionals across 100+ countries
- Used by firms from solo practitioners to Am Law 200 firms
- #1 rated legal practice management software by G2, Capterra, and TrustRadius
- 2024 LegalTech Breakthrough Award winner
- Backed by TCV, JMI Equity, and other top-tier investors (valued at $3B+ as of 2024)

---

*This document was compiled from Clio's official website (clio.com), product documentation (help.clio.com), third-party reviews (Lawyerist, Capterra, G2, Software Advice, TrustRadius), and Clio's public product announcements through August 2026. Feature availability may vary by plan tier and geographic region.*
