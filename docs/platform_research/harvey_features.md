# Harvey.ai — Complete Feature Catalog

> **Last Updated:** August 2026  
> **Purpose:** Comprehensive feature analysis for LegalAI Thailand competitive benchmarking and adaptation roadmap.  
> **Sources:** harvey.ai (official), ThePlanetTools review, Harvey blog (use cases, security), web research.

---

## Executive Summary

Harvey.ai is the dominant enterprise legal AI platform, built on custom-trained versions of OpenAI GPT-4, Anthropic Claude, and other foundation models. Founded in 2022 by a former O'Melveny & Myers antitrust attorney and a former DeepMind researcher, Harvey was incubated at the OpenAI Startup Fund. As of 2026: **$11B valuation**, ~$190M ARR, **1,300+ law firms**, **100,000+ individual lawyer seats**, deployed in **70+ countries**, used by **75+ of the AmLaw 100**. Reference customers include A&O Shearman, PwC, Paul Weiss, Reed Smith, Ashurst, KPMG, Deutsche Telekom, Repsol, Syngenta, and Merck.

The platform consists of six core product surfaces — **Assistant, Vault, Knowledge, Workflows, Shared Spaces, Command Center** — plus three specialized agents (Immigration, Tax, M&A) and a Deep Research mode. Every output is risk-framed (confidence levels, caveats, jurisdictional notes) and grounded in either public legal sources or the firm's own matter archives.

---

## 1. Legal Research (Knowledge + Assistant)

### 1.1 Natural-Language Legal Research with Citations

**What it does:** Lawyers ask legal questions in plain English (or any supported language) and receive structured memos with pinpoint citations to case law, statutes, regulations, and secondary sources. Harvey's Knowledge module connects Assistant to **500+ legal data sources** globally, including LexisNexis (US case law, statutes, regulations), Wolters Kluwer, Gyldendal Rettsdata, FromCounsel, SCC Online, Otto Schmidt, Lefebvre, and Tirant lo Blanch.

**User flow example:**
1. A litigation associate opens Harvey Assistant and types: *"Summarize Delaware Chancery case law on breach of fiduciary duty by LLC managers since 2020, with pinpoint citations and a note on where the holdings diverge."*
2. Harvey queries its connected legal databases (LexisNexis via partnership), retrieves relevant authorities, and produces a structured memo.
3. The memo includes section headings (Controlling Authority, Divergent Lines of Reasoning, Unsettled Questions), paragraph-level pinpoint citations, and confidence flags where authority is thin.
4. The lawyer clicks through citations to verify source materials before relying on the output.
5. The memo exports directly into a Word document or client email via Harvey for Word/Outlook.

**Pain point solved:** Traditional legal research on Westlaw/Lexis requires constructing Boolean queries, manually reviewing dozens of cases, and synthesizing findings. Harvey collapses research that takes 4–6 hours into 5–20 minutes (Deep Research mode) or under 2 minutes (standard Assistant query).

**LegalAI Thailand adaptation opportunity:**
- Partner with Thai legal database providers (e.g., Thai Supreme Court decisions database, Royal Gazette, Dika Court rulings) to create a Thai legal Knowledge source.
- Focus on Thai Civil and Commercial Code, Criminal Code, Supreme Court precedents (ฎีกา), and regulatory announcements.
- Implement Thai-language natural-language queries with citation grounding to Thai legal sources.
- Build a Thai legal taxonomy that maps Thai legal concepts (e.g., สัญญา, ละเมิด, นิติกรรม) to their doctrinal categories.

---

### 1.2 Multi-Jurisdictional Research

**What it does:** Harvey supports cross-jurisdictional legal questions — a single query can be answered under multiple bodies of law. The Knowledge module connects to sources organized by jurisdiction: US federal/state, EU (EUR-Lex), UK, Germany (Otto Schmidt), France (Lefebvre), Spain (Tirant lo Blanch), Norway (Gyldendal Rettsdata), India (SCC Online), and others. EDGAR integration provides SEC filing analysis at scale.

**User flow example:**
1. An M&A lawyer asks: *"Compare the fiduciary duty standards for directors in a change-of-control transaction under Delaware law, UK Companies Act 2006, and German AktG. Which jurisdiction is most favorable to minority shareholders?"*
2. Harvey's Knowledge pipeline routes the query across the relevant jurisdictional sources.
3. The output is a comparative memo with side-by-side analysis, jurisdiction-specific citations, and a summary recommendation.
4. The lawyer can scope the query to a specific matter for context-aware responses.

**Pain point solved:** Cross-border legal research is traditionally siloed — separate searches in separate databases for each jurisdiction, then manual synthesis. Harvey compresses multi-jurisdiction analysis into a single query.

**LegalAI Thailand adaptation opportunity:**
- Build cross-jurisdictional support for ASEAN legal systems: Thailand, Singapore, Malaysia, Vietnam, Indonesia.
- Focus on cross-border M&A, international trade, and investment law (e.g., ASEAN Comprehensive Investment Agreement).
- Support comparative analysis between Thai law and common law jurisdictions (Singapore, UK) for international clients.
- Integrate Thai BOI (Board of Investment) regulations and double-tax treaties for cross-border structuring work.

---

### 1.3 Deep Research Mode (Agentic Multi-Step Research)

**What it does:** Deep Research is a long-horizon reasoning mode that runs a multi-step agentic pipeline — decompose the question, plan the research strategy, retrieve from relevant sources, cross-check findings, synthesize a structured memo, and cite every claim. Queries typically take 5–20 minutes and produce multi-page memos with full citation trails.

**User flow example:**
1. A partner asks: *"Map the evolving regulatory landscape for AI governance across the EU AI Act, US Executive Orders, and UK's approach. Identify compliance obligations for a multinational deploying AI in HR decision-making."*
2. Deep Research decomposes into sub-questions, retrieves from EUR-Lex, US federal registers, UK parliamentary sources, and secondary analysis.
3. After 15 minutes, the partner receives a 12-page structured memo with jurisdiction-by-jurisdiction analysis, compliance checklist, and risk heat-map.

**Pain point solved:** Novel legal questions with no directly on-point authority require exhaustive multi-source research that junior associates used to spend a full weekend on. Deep Research produces comparable output in under 30 minutes, and the lawyer applies judgment on materiality and strategy.

**LegalAI Thailand adaptation opportunity:**
- Implement a Thai Deep Research mode for complex regulatory questions (e.g., PDPA compliance, digital asset regulation, foreign business license requirements).
- Target use cases: BOI promotion applications, complex tax structuring, cross-border M&A regulatory clearance.

---

### 1.4 Knowledge — Data Partner Ecosystem

Harvey's Knowledge module connects to curated legal databases through formal partnerships:

| Data Partner | Jurisdiction / Coverage | Content Type |
|---|---|---|
| **LexisNexis** | US federal + 50 states | Case law, statutes, regulations, secondary sources |
| **Wolters Kluwer** | Global (multiple jurisdictions) | Legal, tax, regulatory content |
| **Gyldendal Rettsdata** | Norway | Statutes, regulations, case law, commentary |
| **FromCounsel** | UK | Corporate law, precedents, commentary |
| **SCC Online** | India | Supreme Court, High Courts, statutes |
| **Otto Schmidt** | Germany | Legal commentary, journals, precedents |
| **Lefebvre** | France | Codes, jurisprudence, doctrine |
| **Tirant lo Blanch** | Spain | Legislation, case law, doctrinal analysis |
| **Web (Real-time)** | Global | Credible internet sources |
| **EDGAR** | US | SEC filings, public company disclosures |
| **EUR-Lex** | EU | EU treaties, directives, regulations, case law |

Additionally, firms can connect their own **Vault Knowledge Bases** (firm precedents, prior work product, playbooks) and **DMS content** (iManage, NetDocuments, SharePoint) as private knowledge sources.

---

## 2. Contract Analysis (Assistant + Vault + Contract Intelligence)

### 2.1 Clause Flagging and Deviation Detection

**What it does:** Harvey analyzes contracts against firm playbooks (or standard templates) and flags every clause that deviates. The analysis runs inside Microsoft Word (Harvey for Word add-in) or through Vault for batch processing. Flagged clauses are highlighted with tracked changes, annotated with playbook references, and categorized by risk level.

**User flow example:**
1. An in-house counsel receives a 45-page supplier agreement from a vendor.
2. They open the document in Microsoft Word with Harvey for Word active.
3. They click "Review against playbook" — Harvey compares every clause against the firm's supplier agreement playbook.
4. Within 60 seconds, Harvey returns a redlined document with flagged deviations (e.g., "Indemnification cap is $500K — playbook requires $2M minimum," "Governing law is New York — playbook prefers Delaware").
5. The lawyer reviews each flag, accepts/rejects suggested edits, and sends the marked-up document to the counterparty.

**Pain point solved:** Manual contract review against playbooks is tedious, error-prone, and inconsistently applied across associates. Harvey applies the same senior partner's playbook to every contract, eliminating variation and catching deviations a junior associate might miss.

**LegalAI Thailand adaptation opportunity:**
- Build a Thai contract playbook system supporting Thai Civil and Commercial Code provisions (e.g., Section 370 surrogation, Section 453 sale, Section 587 hire of work).
- Flag clauses that violate Thai statutory protections (e.g., unfair contract terms under the Unfair Contract Terms Act B.E. 2540, Consumer Case Procedure Act).
- Support dual-language (Thai/English) clause comparison for international contracts.

---

### 2.2 Risk Scoring

**What it does:** Harvey assigns a risk score to each flagged clause deviation and an aggregate risk score to the entire contract. Scores are based on the playbook's risk taxonomy — clauses that waive core protections score higher than formatting deviations. The risk dashboard gives a partner-level view of a contract's health in under a minute.

**User flow example:**
1. After running contract analysis, Harvey presents a risk dashboard with a color-coded summary (Green/Yellow/Red).
2. High-risk clauses (e.g., unlimited liability, one-sided termination rights, non-standard governing law) are surfaced at the top.
3. The partner can click into any flagged clause to see the specific deviation, the playbook reference, and Harvey's suggested edit.
4. The dashboard includes a "negotiation priorities" summary — which clauses are deal-breakers vs. which can be conceded.

**LegalAI Thailand adaptation opportunity:**
- Score Thai contracts based on risk categories relevant to Thai law: enforceability of liquidated damages (Section 380), validity of non-compete clauses, compliance with the Foreign Business Act B.E. 2542.
- Include PDPA (Personal Data Protection Act B.E. 2562) compliance risk scoring for data processing clauses.

---

### 2.3 Suggested Edits and Automated Redlining

**What it does:** When Harvey flags a clause deviation, it also suggests a replacement clause drawn from the firm's playbook or precedent library. The suggested edit appears as a tracked change in Word, with a comment explaining the rationale. The lawyer can accept, reject, or modify the suggestion with one click.

**User flow example:**
1. Harvey flags a non-standard indemnification clause with unlimited liability.
2. The suggested edit inserts the firm's standard mutual indemnification language with a cap at 2x contract value.
3. The comment reads: *"Replaced unlimited indemnity with firm standard — mutual, capped at 2x fees, excludes gross negligence carve-out per playbook Section 4.2(c)."*
4. The associate reviews, adjusts the cap to 3x based on client instructions, and accepts.

**LegalAI Thailand adaptation opportunity:**
- Build a library of Thai-standard contract clauses in both Thai and English.
- For M&A work: standard Thai share purchase agreement clauses, warranty and indemnity provisions, closing conditions.
- For real estate: standard lease clauses compliant with the Civil and Commercial Code (hire of property, Sections 537–571).

---

### 2.4 Portfolio-Level Contract Intelligence (Vault Review Tables)

**What it does:** Beyond single-contract review, Vault supports portfolio-level analysis across thousands of contracts. A single query can extract structured data across the full set — e.g., "Extract all change-of-control provisions and flag any triggered by the proposed transaction" — and return a table with one row per hit, source citations, and extracted clause text.

**User flow example:**
1. A corporate legal department uploads 5,000 supplier agreements into Vault.
2. The legal ops team runs a review table query: *"For every supplier agreement, extract: governing law, renewal terms, termination-for-convenience provisions, and liability caps. Flag any non-standard provisions."*
3. Harvey returns a sortable table within ~40 minutes.
4. The team filters for "governing law ≠ Delaware" and "no termination-for-convenience" to identify high-risk contracts.
5. Results export to Excel for the procurement team's remediation plan.

**Pain point solved:** Portfolio-level contract review without AI requires a team of paralegals reading thousands of documents over weeks. Vault does it in under an hour with a single query.

**LegalAI Thailand adaptation opportunity:**
- Support bulk analysis of Thai-language contracts in PDF and Word formats.
- Extract key Thai contract metadata: parties (with company registration numbers), governing law, dispute resolution clauses (arbitration vs. Thai court), security/guarantee provisions.
- Portfolio risk assessment for Thai conglomerates with hundreds of subsidiary-level agreements.

---

## 3. Due Diligence (Vault + Workflows)

### 3.1 Batch Document Processing (Vault)

**What it does:** Vault is Harvey's secure document workspace for large-scale review. A single workspace can ingest **up to 100,000 documents** — PDFs, Word files, Excel spreadsheets, scanned images (with OCR), and email archives. Harvey auto-classifies documents (contracts, correspondence, filings, financial statements) and extracts key metadata (parties, dates, governing law, signature status). A mid-sized M&A data room of 40,000 documents typically processes in under 90 minutes.

**User flow example:**
1. An M&A deal team receives a 35,000-document data room from the target company.
2. They upload all files to a matter-scoped Vault workspace (access controls inherited from DMS).
3. Harvey auto-classifies: 12,000 contracts, 8,000 correspondence items, 5,000 financial statements, 10,000 corporate filings.
4. Metadata extraction runs automatically — parties, effective dates, governing law, amendment chains.

**Pain point solved:** Traditional due diligence requires an army of associates manually opening and categorizing thousands of documents. Vault automates classification and metadata extraction, shifting lawyer time from "confirming every document was opened" to "reviewing structured exceptions."

**LegalAI Thailand adaptation opportunity:**
- Support Thai-language document classification (สัญญา, บันทึกข้อตกลง, รายงานการประชุมผู้ถือหุ้น, งบการเงิน).
- Extract Thai-specific metadata: company registration numbers (เลขทะเบียนนิติบุคคล), tax ID numbers, land title deed references (โฉนดที่ดิน).
- Integrate with Thai DBD (Department of Business Development) data for corporate verification.

---

### 3.2 Anomaly Detection and Cross-Document Comparison

**What it does:** Vault supports cross-document reasoning — lawyers can ask questions that compare documents against each other or against a reference template. Example: *"Which of these 120 supply contracts have non-standard termination-for-convenience provisions?"* or *"Compare every indemnification cap across all 800 customer contracts and flag any below $1M."*

**User flow example:**
1. Vault ingests 800 customer agreements from the target company.
2. The diligence lead runs: *"Identify every agreement where the liability cap is below $500K or unlimited. Flag any agreements with one-sided indemnification. Summarize the 10 highest-risk agreements."*
3. Harvey returns a ranked list with extracted clause text and justification for each flag.
4. The team focuses review on the 10 highest-risk contracts, not all 800.

**Pain point solved:** Finding outliers in a document pile is the most painful part of due diligence — "Does anything in this 50,000-document set look unusual?" is a question traditional tools can't answer without pre-defined taxonomies. Vault's open-ended query interface lets lawyers ask any question the matter requires.

**LegalAI Thailand adaptation opportunity:**
- Anomaly detection for Thai corporate filings: flag companies with unusual shareholder structures, missing board resolutions, or non-standard articles of association.
- Cross-document comparison for Thai real estate portfolios: compare lease terms, rental rates, renewal options across properties.

---

### 3.3 End-to-End Due Diligence Workflows

**What it does:** Harvey Workflows codify the entire due diligence process into a repeatable automation. A typical M&A diligence workflow: (1) ingest data room documents, (2) auto-classify, (3) run standard review queries (material contracts, change-of-control, IP assignments, employment agreements), (4) flag exceptions, (5) generate a diligence report. GSK Stockmann (European corporate law firm) partnered with Harvey to co-design an end-to-end GenAI due diligence workflow from scope determination through report delivery. PwC's deal team has documented similar gains across live M&A engagements.

**User flow example:**
1. A partner selects the firm's "Mid-Market M&A Diligence" workflow.
2. They specify the data room location and target company details.
3. The Workflow runs autonomously: ingestion → classification → 12 standard review queries → exception flagging → report generation.
4. After ~2 hours, the partner receives a structured diligence report with an executive summary, risk heat-map, and detailed clause-by-clause analysis.
5. The partner reviews, adjusts, and sends to the client — total elapsed time: 3 hours vs. 2 weeks traditionally.

**Pain point solved:** Due diligence is the same structured process applied to new inputs every time — yet firms reinvent the wheel on each deal. Workflows capture the senior partner's methodology and let any associate run it on every deal.

**LegalAI Thailand adaptation opportunity:**
- Build Thai M&A due diligence workflow: DBD corporate verification, land title verification, IP registration check, labor compliance (Social Security Office), tax clearance (Revenue Department).
- Build property due diligence workflow: title deed chain verification, encumbrance check, zoning compliance, EIA (Environmental Impact Assessment) status.

---

## 4. Litigation Support

### 4.1 Motion Drafting and Brief Writing

**What it does:** Harvey Assistant and Harvey for Word support drafting of briefs, motions, client memos, and deposition outlines. Lawyers can generate first drafts grounded in cited authority, then refine inside Word. Workflow Agents apply firm-specific drafting patterns — argument structure, citation format, jurisdictional conventions — consistently across matters.

**User flow example:**
1. A litigation associate opens Harvey for Word with a blank motion for summary judgment.
2. They prompt: *"Draft the Statement of Facts and Legal Argument sections for a summary judgment motion under FRCP 56. The plaintiff's breach of contract claim fails because the alleged contract lacks consideration under [State] law. Use the attached deposition excerpts and the firm's MSJ template."*
3. Harvey generates a first draft with proper formatting, citations to the deposition record, and case law support.
4. The associate refines the draft, strengthens the argument, and sends to the partner for review.
5. Total drafting time: 90 minutes vs. 6–8 hours traditionally.

**Pain point solved:** Brief writing is the highest-value litigation task but also the most time-consuming. Harvey shifts the work from "writing from a blank page" to "refining a well-structured first draft."

**LegalAI Thailand adaptation opportunity:**
- Support Thai litigation document drafting: คำฟ้อง (plaint), คำให้การ (answer), อุทธรณ์ (appeal), ฎีกา (Dika appeal).
- Ground arguments in Thai Supreme Court precedents (คำพิพากษาฎีกา).
- Format output to match Thai court filing conventions (Thai civil procedure code formatting).

---

### 4.2 Discovery and Document Review

**What it does:** Vault handles discovery productions and large litigation document sets at the same scale as diligence — up to 100,000 documents per project. Review tables extract data points across full document sets, surfacing patterns that document-by-document review would miss. Transcript analysis and analysis of litigation filings run on the same infrastructure.

**User flow example:**
1. A litigation team receives 80,000 documents in discovery from the opposing party.
2. They upload to Vault and run: *"Identify all documents where an executive discusses the pricing strategy for Product X between January 2022 and June 2023. Flag any documents that appear responsive to Plaintiff's Request No. 12 (trade secret misappropriation)."*
3. Harvey returns a prioritized review set with relevance scoring.
4. The team runs privilege screening: *"Flag any documents that appear to contain attorney-client privileged communications based on sender/recipient analysis and content."*

**Pain point solved:** Discovery review is the most expensive phase of US litigation. Harvey's first-pass review and privilege flagging compress the most labor-intensive stage from weeks to days.

**LegalAI Thailand adaptation opportunity:**
- Build Thai-language e-discovery capability for civil and criminal cases.
- Support Thai document review for criminal defense (drug cases, fraud, corruption) and civil disputes (contract, tort, family).
- Privilege screening adapted to Thai legal professional privilege rules (different from US attorney-client privilege).

---

### 4.3 Trial Preparation and Oral Argument

**What it does:** Harvey supports authority analysis, deposition review, exhibit organization, and structured argument synthesis across the full case record. Output is built for active use in trial — with verifiable citations and organization that mirrors trial binders.

**User flow example:**
1. Two weeks before trial, a litigation partner asks Harvey: *"Prepare a witness examination outline for the plaintiff's CEO. For each topic, cite the relevant deposition testimony (with page:line), the key document exhibits, and the legal authority supporting our position."*
2. Harvey produces a tabbed examination outline organized by topic, with cross-references to the trial exhibit list.
3. The partner reviews and practices with the outline — Harvey adjusts based on follow-up queries ("Add impeachment material for Topic 3 based on Document Ex. 47").

**LegalAI Thailand adaptation opportunity:**
- Thai trial preparation support: witness examination outlines, exhibit organization, legal issue trees for civil and criminal trials.
- Support for Thai arbitration proceedings (TCC, TAI) with arbitration-specific document preparation.

---

### 4.4 Regulatory and Advisory Analysis

**What it does:** A substantial share of litigation use is in regulatory and advisory work — reviewing legislation, regulation, and agency guidance, then producing structured analysis of how those authorities apply to specific fact patterns. Harvey Assistant handles this end-to-end with traceable citations.

**User flow example:**
1. A regulatory lawyer asks: *"A fintech client wants to launch a peer-to-peer lending platform in Thailand. Analyze the applicable regulations — Bank of Thailand notifications, SEC regulations on crowdfunding, Ministry of Finance notifications — and identify all licensing requirements, capital requirements, and ongoing compliance obligations."*
2. Harvey queries its Knowledge sources and produces a structured regulatory roadmap.
3. The output includes a compliance checklist, timeline, and risk assessment for each regulatory authority.

**LegalAI Thailand adaptation opportunity:**
- Build Thai regulatory Knowledge sources: Bank of Thailand notifications, SEC regulations, NBTC (telecoms), FDA (healthcare), Ministry of Commerce (foreign business).
- High-value practice areas: fintech, digital assets, data privacy (PDPA), energy, BOI promotions.

---

## 5. Compliance (Regulatory Monitoring + Advisory)

### 5.1 Regulatory Monitoring and Tracking

**What it does:** Harvey Knowledge, combined with Workflow Agents, enables ongoing regulatory monitoring. Firms set up agents that periodically query connected data sources for new developments in defined practice areas and route alerts to subscribed lawyers. The Command Center provides adoption analytics and usage benchmarking so firm leadership can track how teams are using AI for compliance work.

**User flow example:**
1. A firm's regulatory practice group configures a Workflow Agent: *"Every Monday, check for new SEC (US) and FCA (UK) cryptocurrency regulatory announcements. Summarize any new developments and flag those relevant to our 3 active crypto-exchange clients."*
2. The agent runs automatically each Monday, queries Harvey Knowledge sources, and produces a digest.
3. The digest is routed to the relevant partners via Harvey Shared Spaces or email.
4. The Command Center tracks which partners open the digest and which matters are updated based on the insights.

**Pain point solved:** Regulatory change management is currently done through manual monitoring of regulator websites, email newsletters, and law firm alerts — labor-intensive, inconsistent, and easy to miss deadlines. Harvey automates detection, summarization, and routing.

**LegalAI Thailand adaptation opportunity:**
- Build Thai regulatory monitoring agents for: Bank of Thailand circulars, SEC notifications, Revenue Department rulings, Department of Labor regulations, FDA announcements.
- Auto-classify regulatory changes by industry vertical (banking, insurance, energy, pharma, tech).
- Route alerts to lawyers based on client-matter mapping.

---

### 5.2 Compliance Advisory and Risk Assessment

**What it does:** Harvey Assistant supports compliance advisory work — analyzing regulatory requirements, mapping them to client operations, and producing structured compliance assessments. The output is formatted as risk-framed memos with confidence levels and jurisdictional caveats.

**User flow example:**
1. An in-house compliance officer asks: *"Our company processes personal data of employees and customers in Thailand, Singapore, and Vietnam. Map the data protection obligations across the Thai PDPA, Singapore PDPA, and Vietnam's Personal Data Protection Decree. Identify gaps in our current privacy policy against each jurisdiction."*
2. Harvey produces a jurisdiction-by-jurisdiction compliance matrix with gap analysis.
3. The officer uses the output to brief the DPO and prioritize remediation.

**LegalAI Thailand adaptation opportunity:**
- Pre-built compliance frameworks for high-priority Thai regulations: PDPA, Anti-Money Laundering Act, Anti-Corruption Act, Labor Protection Act.
- Sector-specific compliance modules: banking (BOT), securities (SEC), insurance (OIC), data privacy (PDPC).

---

## 6. Document Drafting (Prompt-to-Document)

### 6.1 Prompt-to-Document Generation

**What it does:** Lawyers generate clauses, sections, and full agreement drafts by describing what they need in natural language. Drafting happens inside Microsoft Word (Harvey for Word add-in), with firm precedent and prior work available as context. Drafts are grounded in the firm's playbooks and prior matter archives, not generic boilerplate.

**User flow example:**
1. A transactional associate opens a blank Word document and prompts Harvey: *"Draft an asset purchase agreement for the sale of a manufacturing business in Thailand. Seller is a Thai limited company. Include standard representations on title, environmental compliance, and employee matters. Use the firm's APW template."*
2. Harvey generates a 30-page first draft with the firm's template structure, standard clauses, and placeholders marked [TO BE COMPLETED].
3. The associate fills in deal-specific details (parties, purchase price, assets) and refines.
4. Harvey for Word provides context-aware suggestions as the associate edits — e.g., reminding them to add a specific warranty that the firm's playbook requires for manufacturing deals.

**Pain point solved:** First-draft document creation from scratch is time-consuming and inconsistent. Harvey generates a partner-quality first draft in minutes, with firm standards applied automatically.

**LegalAI Thailand adaptation opportunity:**
- Thai-language document drafting for key Thai legal documents: สัญญาซื้อขาย (sale agreement), สัญญาเช่า (lease agreement), สัญญาจ้างแรงงาน (employment agreement), หนังสือมอบอำนาจ (power of attorney), บันทึกข้อตกลง (MOU).
- Bilingual (Thai/English) drafting for cross-border transactions.
- Thai corporate documents: articles of association (ข้อบังคับ), shareholder resolutions (รายงานการประชุมผู้ถือหุ้น), board resolutions.

---

### 6.2 Workflow Agents for Document Generation

**What it does:** Firms codify document generation patterns into Workflow Agents. Customers have built **more than 25,000 custom Workflow Agents** — drafting and document generation are among the most common patterns. A single Workflow Agent built once runs across every matter that fits the pattern.

**User flow example:**
1. A firm builds a "Lease Agreement Generator" Workflow that: (a) asks the lawyer 15 structured questions (property address, term, rent, deposit, permitted use, etc.), (b) selects the appropriate firm template based on property type (commercial/industrial/residential), (c) generates the lease with jurisdiction-specific clauses, (d) produces a partner-facing summary of key terms.
2. Any real estate associate at the firm runs this workflow on a new lease in under 2 minutes.

**LegalAI Thailand adaptation opportunity:**
- Pre-built Thai document generation workflows: lease agreements, employment contracts, NDAs, service agreements, loan agreements.
- Integration with Thai land office requirements for lease registration.
- Support for Thai-language templates with automatic Civil and Commercial Code compliance checks.

---

## 7. Platform Components (Cross-Cutting Capabilities)

### 7.1 Assistant — Conversational Legal AI

The surface most lawyers encounter first. A legally grounded reasoning system producing risk-framed, citation-backed outputs (memos, not chat paragraphs). Available via web app, Word add-in, Outlook add-in. Matter-aware context scoping.

### 7.2 Vault — Document Workspace at Scale

Secure document ingestion (up to 100,000 docs), auto-classification, metadata extraction, structured review tables, cross-document comparison, privilege screening. Used for M&A diligence, discovery, second requests, portfolio contract analysis.

### 7.3 Knowledge — Grounded Legal Research

Connects Assistant to 500+ legal data sources globally. Includes public sources (LexisNexis, EDGAR, EUR-Lex, Web) and private sources (Vault Knowledge Bases from firm's own work product, DMS content from iManage/NetDocuments/SharePoint).

### 7.4 Workflow Agents + Agent Builder

No-code automation builder for codifying multi-step legal processes. Ships with pre-built templates (NDAs, MSAs, DPAs, leases, diligence checklists). Firms customize/build bespoke workflows. 25,000+ custom agents deployed. Turns partner expertise into firm-wide capability.

### 7.5 Shared Spaces

Secure collaboration environment for working with clients and external parties. Lawyers publish Workflow Agents into Shared Spaces; external collaborators run them on demand without Harvey onboarding. Admin-controlled permissions with scoped access (no full platform access required).

### 7.6 Command Center

Analytics, benchmarking, and agentic insights for firm leadership. Tracks adoption metrics across practice groups, measures time savings, identifies top use cases. Enables data-driven AI transformation management.

### 7.7 Harvey Mobile

Mobile access to the Harvey platform for lawyers on the go. Access Assistant queries, review documents, approve workflows from mobile devices.

---

## 8. Specialized Agents

### 8.1 Immigration Agent

Handles visa strategy, petition drafting (I-140, H-1B, L-1, PERM), RFE responses, and multi-jurisdiction coordination. Trained on country-by-country visa frameworks, USCIS guidance, and consular processing nuances. Compresses petition drafting from days to hours.

**LegalAI Thailand adaptation opportunity:** Thai work permit and visa processing support. Integration with BOI one-stop service requirements, Immigration Bureau procedures, and 90-day reporting rules.

### 8.2 Tax Agent

Handles tax research, structuring memos, cross-border analysis, and Internal Revenue Code section reasoning. Trained on Code sections, Treasury regulations, revenue rulings, private letter rulings, and key tax court decisions. Produces outputs formatted for tax practice — structuring memos, opinion letters, transfer pricing analyses.

**LegalAI Thailand adaptation opportunity:** Thai Revenue Code analysis, double-tax treaty interpretation, BOI tax incentive calculation (corporate income tax exemption periods), transfer pricing documentation for Thai entities.

### 8.3 M&A Agent

Handles due diligence, disclosure schedule review, merger agreement analysis, and deal-process acceleration. Plugged into Vault for document review and Workflows for repeatable diligence. Trained on merger agreement precedents, disclosure schedule conventions, and deal-process playbooks. In a typical mid-market deal, shaves 30–50% off the diligence timeline.

**LegalAI Thailand adaptation opportunity:** Thai M&A deal support — share purchase vs. asset purchase structuring, Foreign Business Act compliance, competition law (Trade Competition Act) review, securities law (SEC takeover rules) compliance.

---

## 9. Multi-Language and Multi-Jurisdictional Support

### 9.1 Language Capabilities

Harvey is deployed in **70+ countries** and supports legal work across multiple languages through its foundation model architecture (GPT-4, Claude). While Harvey does not market a specific "50+ language" feature, its global deployment across civil law and common law jurisdictions implies broad language capability:

- **European languages:** English, German, French, Spanish, Italian, Dutch, Norwegian, Danish, Swedish, Portuguese
- **Asian languages:** Japanese, Korean, Chinese (Simplified/Traditional) — through global firm deployments
- **Middle Eastern languages:** Arabic (via UAE and Middle East law firm customers)
- **Nordic languages:** Full support via Gyldendal Rettsdata (Norway) partnership

The Knowledge module's data partners provide localized content in each jurisdiction's native language. For example, Otto Schmidt provides German-language legal commentary, Lefebvre provides French, and Tirant lo Blanch provides Spanish.

### 9.2 Jurisdictional Coverage

Harvey's Knowledge module covers 500+ legal sources globally organized by jurisdiction:

| Region | Key Jurisdictions & Sources |
|---|---|
| **North America** | US (federal + 50 states via LexisNexis), US SEC (EDGAR) |
| **Europe** | EU (EUR-Lex), UK (FromCounsel), Germany (Otto Schmidt), France (Lefebvre), Spain (Tirant lo Blanch), Norway (Gyldendal Rettsdata) |
| **Asia-Pacific** | India (SCC Online), plus deployments in Japan, Korea, Singapore, Australia |
| **Latin America** | Spain (Tirant lo Blanch) — civil law foundation; Brazilian and Mexican deployments |

**LegalAI Thailand adaptation opportunity:**
- Full Thai-language support with Thai legal terminology understanding.
- ASEAN multi-language support: Thai, Vietnamese, Bahasa Indonesia, Bahasa Malaysia, Burmese, Khmer, Lao.
- Thai legal Knowledge sources: Supreme Court decisions database, Royal Gazette, Council of State legal opinions.
- Cross-jurisdictional comparison: Thai civil law vs. Singapore common law vs. Vietnamese socialist law for regional M&A.

---

## 10. Security and Compliance

### 10.1 Certifications and Standards

Harvey meets the highest enterprise procurement bar:

| Certification | Scope |
|---|---|
| **SOC 2 Type II** | Independently audited security controls — availability, confidentiality, processing integrity, privacy |
| **ISO/IEC 27001** | Information security management system — recognized globally by enterprise procurement |
| **ISO/IEC 27701** | Privacy information management — extension to 27001 for PII processing |
| **ISO/IEC 42001** | Artificial intelligence management system — governance for responsible AI deployment |
| **GDPR** | EU General Data Protection Regulation compliance |
| **CCPA** | California Consumer Privacy Act compliance |

### 10.2 Data Residency and Sovereignty

- **Configurable data residency:** EU (European data centers), Switzerland, US, Australia
- **BYOK (Bring Your Own Key) support:** Firms control encryption keys
- **Data lifecycle management:** Set retention policies, delete data anytime
- **Full data retention control:** Decide which data to upload; delete on demand

### 10.3 Model Training and Data Privacy

- **No training on customer data:** Contractually guaranteed through Harvey's Platform Agreement. Harvey does not use inputs, outputs, or uploaded documents to train underlying models.
- **Customer-chosen model training:** Firms can opt to use their own client data for model training if they choose (custom model fine-tuning).
- **Model abstraction:** Harvey abstracts foundation models (OpenAI, Anthropic, Google) and does not expose the underlying LLM to end users.

### 10.4 Access Controls and Ethical Walls

- **Enterprise SSO:** SAML and OIDC integration with Microsoft Entra ID (Azure AD) and Okta
- **Granular access controls:** Role-based access, matter-level scoping
- **Ethical walls enforcement:** Harvey syncs with the firm's existing ethical wall policies (DMS-sourced), blocking restricted users from accessing or sharing walled content. Harvey never creates, modifies, or deletes walls — the firm's walls provider remains the system of record.
- **IP allow-listing:** Restrict access to permitted IP ranges

### 10.5 Audit and Monitoring

- **Comprehensive audit trails:** Every query, document view, and output is logged with timestamps, user identity, and matter context
- **Third-party penetration testing:** Schellman, NCC Group, Bishop Fox conduct regular independent audits
- **24/7 security monitoring:** In-house security team spanning infrastructure, product, and operations
- **Penetration test reports:** Shared under NDA as part of procurement review

### 10.6 Contractual Protections

- **Security Addendum:** Binding terms on data protection, data access, incident response SLAs
- **Enforceable commitments:** Aligned with SOC 2, ISO, GDPR standards
- **Professional indemnity carve-outs:** Negotiated during procurement

**LegalAI Thailand adaptation opportunity:**
- Target SOC 2 and ISO 27001 certification for enterprise credibility.
- Build PDPA-compliant data handling and data residency within Thailand (per PDPA cross-border transfer restrictions).
- Implement Thai ethical wall equivalents (conflict-of-interest checks per Lawyers Council regulations).
- SSO integration with common Thai enterprise identity systems.

---

## 11. Pricing

### 11.1 Pricing Model

Harvey does **not publish pricing**. Every deal is:

- **Quote-based:** Negotiated through a dedicated enterprise sales process
- **Multi-year firm-wide licenses:** Typically 2–3 year commitments, not monthly subscriptions
- **Three pricing drivers:**
  1. **Seat count** — committed volume; larger firms get better per-seat economics
  2. **Module mix** — Assistant only vs. Assistant + Vault + Workflows + specialized agents (M&A and Tax agents command premium pricing)
  3. **Usage envelope** — committed volume of queries, documents ingested, Deep Research runs; overage pricing above cap

### 11.2 Directional Pricing

Based on industry reports and discussions with firms that have deployed Harvey:

| Firm Size | Annual Range | Typical Scope |
|---|---|---|
| **AmLaw 100 (1,000+ attorneys)** | Seven figures ($1M+) | Firm-wide: Assistant, Vault, Workflows, specialized agents |
| **Mid-market (50–300 attorneys)** | Six figures ($100K–$999K) | Practice-group deployment: Assistant + Vault |
| **Small firms (<50 attorneys)** | Not viable | Economics don't work — Harvey targets AmLaw 200+ |

Earlier reports suggested per-seat pricing in the range of **$399 to $1,200/month per user**, but the current model is firm-wide licensing, not per-seat subscriptions.

### 11.3 Procurement Process

Typical cycle: **3–6 months** from initial contact to signed contract.

1. **Initial engagement** — demo and use-case scoping with Harvey sales team
2. **Security/compliance review** — SOC 2 report, ISO certs, pen test results, data residency
3. **Integration review** — DMS compatibility, identity provider, audit stack
4. **Pilot/POC** — 60–90 days, scoped to a specific practice group, with defined success metrics
5. **Contract negotiation** — pricing, SLAs, data processing terms, indemnity, exit provisions
6. **Firm-wide rollout** — phased deployment with Harvey professional services

### 11.4 ROI Profile

- Average **25+ hours saved per lawyer per month**
- **92% monthly adoption rate** across deployed firms
- M&A Agent: **30–50% reduction in diligence timeline**
- Vault: **40,000-document data room processed in <90 minutes**
- Repsol reported **96% adoption across legal department**

**LegalAI Thailand adaptation opportunity:**
- Consider a more transparent, tiered pricing model appropriate for the Thai market (fewer $1M+ deals).
- Offer modular pricing: per-seat for smaller firms (5–50 lawyers), flat-rate for mid-size (50–200), enterprise for large firms.
- Consider monthly subscription model instead of multi-year commitment for smaller Thai firms.
- Target price point accessible to Thai mid-market firms (e.g., ฿3,000–฿15,000/month per user) vs. Harvey's $399–$1,200/month.

---

## 12. Integrations

### 12.1 Document Management Systems (DMS)

| Integration | Status | Details |
|---|---|---|
| **iManage** | Native connector | Pulls matter content directly into Harvey's matter-scoped context; access controls inherited from DMS permission model |
| **NetDocuments** | Native connector | Same DMS integration pattern as iManage |
| **SharePoint** | Native connector | Microsoft 365 ecosystem integration |
| **Google Drive** | Supported | Available through broader Harvey ecosystem |

### 12.2 Microsoft 365 Ecosystem

| Integration | Details |
|---|---|
| **Microsoft Word add-in** | Draft, redline, and review inside Word; tracked changes; firm precedent available alongside active document |
| **Microsoft Outlook add-in** | Email thread summarization, context-aware response drafting, action item extraction |
| **Microsoft 365 Copilot integration** | Harvey adapts to the M365 Copilot environment — unified AI inside the Microsoft workspace |
| **SharePoint connector** | Matter content pulled from SharePoint document libraries |
| **Microsoft Teams** | Collaboration and notification surface |

### 12.3 Identity and SSO

| Provider | Protocol |
|---|---|
| **Microsoft Entra ID (Azure AD)** | SAML, OIDC |
| **Okta** | SAML, OIDC |
| **Other SAML/OIDC providers** | Enterprise SSO standard |

### 12.4 Additional Integrations

| Integration | Details |
|---|---|
| **Datasite** | Virtual data room integration for M&A diligence |
| **SS&C Intralinks** | VDR integration for deal management |
| **Harvey API** | Available for enterprise customers for custom integrations |
| **LexisNexis (via Knowledge)** | Legal research content integration |

### 12.5 Platform Availability

- **Web:** Full Harvey platform access
- **Microsoft Word:** In-document add-in
- **Microsoft Outlook:** Email add-in
- **Harvey Mobile:** Mobile app for iOS/Android
- **API:** For enterprise custom integrations

**LegalAI Thailand adaptation opportunity:**
- Prioritize Microsoft 365 integration (dominant in Thai enterprise).
- Build connectors for Thai-specific systems: DBD corporate registry API, Land Department title deed database, Revenue Department e-filing.
- Consider Google Workspace integration (popular among Thai startups and SMEs).
- LINE integration for notifications/alerts (LINE is ubiquitous in Thailand).
- Thai-language UI/UX in all integration surfaces.

---

## 13. Competitive Positioning (2026)

### 13.1 How Harvey Compares

| Dimension | Harvey AI | CoCounsel (TR) | Lexis+ AI | Robin AI |
|---|---|---|---|---|
| **Primary strength** | End-to-end platform | Westlaw bundle | Lexis bundle | Contract review |
| **Legal research** | Assistant + Deep Research + 500+ sources | Westlaw-native | Lexis-native | Not a focus |
| **Document review at scale** | Vault (100K docs) | Limited | Limited | Strong (contracts) |
| **Workflow automation** | Native Workflow builder | Limited | Limited | Contract-specific |
| **Specialized agents** | Immigration, Tax, M&A | None | None | Contract-only |
| **DMS integrations** | iManage, NetDocuments, SharePoint | iManage, NetDocuments | iManage, NetDocuments | Limited |
| **Microsoft 365** | Native add-ins + Copilot | Yes | Yes | Partial |
| **Pricing** | Enterprise (quote-based) | Bundled with Westlaw | Bundled with Lexis | Per-seat (transparent) |
| **Install base** | 1,300+ firms, 100K+ lawyers | Westlaw footprint | Lexis footprint | Smaller, focused |
| **Best for** | AmLaw 200, enterprise legal | Westlaw shops | Lexis shops | Transactional/contracts |

### 13.2 Key Differentiators

1. **Platform breadth:** Assistant + Vault + Workflows + Deep Research + specialized agents — no competitor matches the feature surface area.
2. **Scale:** 100,000+ lawyer seats, 25,000+ custom Workflow Agents, 1,300+ firms.
3. **Risk-framed outputs:** Every output is a legal artifact (memo, diligence report, clause analysis), not a chat paragraph.
4. **Matter-aware context:** Outputs scoped to specific matters, clients, and practice groups with access control inheritance.

---

## 14. Summary: LegalAI Thailand Adaptation Roadmap

### 14.1 Immediate Opportunities (Build First)

| Harvey Feature | LegalAI Thailand Adaptation | Priority |
|---|---|---|
| Legal Research (Knowledge) | Thai legal database — Supreme Court precedents, Civil/Commercial Code, Royal Gazette | HIGH |
| Contract Analysis | Thai contract playbook system with bilingual (Thai/English) support | HIGH |
| Document Drafting | Thai legal document templates: sale, lease, employment, MOU, POA | HIGH |
| Multi-language | Full Thai language support + ASEAN languages | HIGH |

### 14.2 Medium-Term Opportunities

| Harvey Feature | LegalAI Thailand Adaptation | Priority |
|---|---|---|
| Due Diligence (Vault) | Thai M&A diligence workflow — DBD, Land Dept, IP, labor, tax | MEDIUM |
| Compliance | Thai regulatory monitoring: BOT, SEC, Revenue Dept, FDA | MEDIUM |
| Integrations | Microsoft 365, DBD API, Land Dept, LINE notifications | MEDIUM |
| Security | SOC 2, ISO 27001, PDPA compliance | MEDIUM |

### 14.3 Long-Term Opportunities

| Harvey Feature | LegalAI Thailand Adaptation | Priority |
|---|---|---|
| Specialized Agents | BOI Agent, Property Agent, Litigation Agent (Thai civil/criminal) | LOWER |
| Workflow Agents | Thai-specific workflows: BOI application, land registration, corporate formation | LOWER |
| Cross-jurisdictional | ASEAN comparative law: Thailand-Singapore-Vietnam-Indonesia | LOWER |

### 14.4 Key Differentiation Opportunities for LegalAI Thailand

1. **Price accessibility:** Harvey is enterprise-only (six-to-seven figures). LegalAI Thailand can capture the entire Thai market below the Harvey threshold — 5–500 lawyer firms.
2. **Thai-first, not Thai-added:** Harvey treats non-US/UK jurisdictions as add-ons. LegalAI Thailand can be Thai-native from day one.
3. **ASEAN hub:** Thailand is the legal hub for ASEAN cross-border work. Build ASEAN comparative law capabilities that no global player offers.
4. **Government integration:** Deep integrations with Thai government systems (DBD, Land Department, Revenue Department) create moats global competitors can't cross.
5. **Local data residency:** Full in-Thailand data hosting compliant with PDPA and Thai government data sovereignty requirements.

---

## Appendix: Key Harvey.ai Metrics

| Metric | Value |
|---|---|
| Valuation (2026) | $11 billion |
| Annual Recurring Revenue (est.) | ~$190 million |
| Law firms deployed | 1,300+ |
| Individual lawyer seats | 100,000+ |
| Organizations using Harvey | 2,400+ |
| Countries deployed | 70+ |
| AmLaw 100 firms | 75+ |
| Average hours saved per lawyer/month | 25+ |
| Monthly adoption rate | 92% |
| Custom Workflow Agents built | 25,000+ |
| Practice groups covered | 500+ |
| Legal data sources (Knowledge) | 500+ |
| Vault document capacity | Up to 100,000 per project |
| Data residency options | EU, Switzerland, US, Australia |
| Certifications | SOC 2 Type II, ISO 27001, ISO 27701, ISO 42001, GDPR, CCPA |
| Foundation models | OpenAI GPT-4 (custom-trained), Anthropic Claude, Google (abstracted) |
| Funding raised | $300M+ total across rounds |
| Founded | 2022 |
| HQ | San Francisco, CA |

---

*Document prepared for LegalAI Thailand competitive analysis. All information sourced from public materials (harvey.ai, ThePlanetTools review, Harvey blog, industry analysis) as of August 2026. Pricing information is directional based on industry reports — Harvey does not publish official pricing.*
