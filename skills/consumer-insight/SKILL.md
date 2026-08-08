---
name: consumer-insight
description: "Consumer psychology, segmentation, product-market fit."
version: 1.0.0
author: Bess (Hermes Agent)
license: MIT
metadata:
  hermes:
    tags: [consumer-behavior, marketing, psychology, segmentation, product-market-fit, trends]
    related_skills: [polymarket, blogwatcher, xlsx, arxiv, llm-wiki]
---

# 🎀 Consumer Insight — การวิเคราะห์ผู้บริโภค & ตลาดแบบครบวงจร

> **Owner:** เบส (Bess) — Customer Empathy & Trend Analyst
> **DNA:** เข้าใจผู้บริโภค, เทรนด์การซื้อ, จิตวิทยาการซื้อ-ขาย, จิตวิทยากลุ่ม, วิเคราะห์ตลาดรายผลิตภัณฑ์

---

## Overview

Consumer Insight Skill ครอบคลุม 4 เสาหลักของการวิเคราะห์ผู้บริโภคและการตลาด:

| # | เสาหลัก | ครอบคลุม |
|---|---------|---------|
| 🧠 | **จิตวิทยาการซื้อ** | Scarcity, Social Proof, Anchoring, Loss Aversion, Decoy Effect, Reciprocity, Framing |
| 👥 | **จิตวิทยากลุ่ม** | Herd Behavior, Bandwagon, Tribe, In-group/Out-group, Social Influence |
| 📊 | **แบ่งกลุ่มผู้บริโภค** | Demographic, Psychographic (VALS, AIO), Behavioral, Geographic, JTBD |
| 📈 | **Product-Market Fit** | SWOT, Porter's Five Forces, Value Proposition Canvas, JTBD |

---

## When to Use

โหลด skill นี้เมื่อ user ถามเกี่ยวกับ:
- "วิเคราะห์ตลาดผลิตภัณฑ์..."
- "จิตวิทยาการซื้อของ..."
- "ผู้บริโภคกลุ่มนี้คิดยังไง..."
- "ทำไมคนถึงซื้อ/ไม่ซื้อ..."
- "เทรนด์การซื้อตอนนี้..."
- "Product-Market Fit ของ..."
- "แบ่งกลุ่มลูกค้า..."
- "SWOT analysis..."
- "คู่แข่งในตลาด..."

**Don't use for:** การวิเคราะห์ตลาดหุ้น/คริปโต (ใช้ polymarket), การวิเคราะห์ทางการเงิน (P/E, balance sheet — ใช้ web_search)

---

## 🧠 Pillar 1: Buying Psychology (จิตวิทยาการซื้อ)

### Core Principles

| หลักการ | กลไก | ใช้เมื่อ | ตัวอย่าง |
|---------|------|---------|---------|
| **Scarcity** (ความขาดแคลน) | ของมีจำกัด → อยากได้มากขึ้น | สินค้า Limited Edition, Flash Sale | "เหลือ 3 ชิ้นสุดท้าย!" |
| **Social Proof** (การยอมรับทางสังคม) | คนอื่นใช้ → เราก็ใช้ตาม | รีวิว, Testimonials, ยอดขาย | "xxxxx คนซื้อแล้ว" |
| **Anchoring** (การยึดติดราคาแรก) | เห็นราคาแรก → ใช้เป็น基準 | การตั้งราคา, ส่วนลด | "เคย 1,990 ลดเหลือ 990!" |
| **Loss Aversion** (กลัวเสีย > อยากได้) | กลัวพลาดโอกาส | Free Trial → จ่ายเงิน | "หมดเขตพรุ่งนี้!" |
| **Decoy Effect** (ตัวเลือกหลอก) | เพิ่มตัวเลือก → ดันให้เลือกตัวที่แพงกว่า | Pricing Tiers | Small/Medium/Large — Medium ดูดีสุด |
| **Reciprocity** (การตอบแทน) | ได้ของฟรี → รู้สึกต้องซื้อ | Free sample, E-book แจกฟรี | "โหลดคู่มือฟรี → ซื้อคอร์ส" |
| **Framing Effect** (การวางกรอบ) | วิธีนำเสนอเปลี่ยนการตัดสินใจ | การสื่อสารการตลาด | "เนื้อ 90% ไร้ไขมัน" vs "เนื้อไขมัน 10%" |
| **Endowment Effect** | เป็นเจ้าของแล้ว → มูลค่ามากขึ้น | Test Drive, ลองใส่เสื้อ | "ลองขับแล้วรู้สึกว่าเป็นของเรา" |

### Workflow — วิเคราะห์จิตวิทยาการซื้อของผลิตภัณฑ์

① ระบุผลิตภัณฑ์และกลุ่มเป้าหมาย
② เลือก 3-5 หลักการที่เกี่ยวข้องที่สุด
③ วิเคราะห์ว่าหลักการนั้นถูกใช้ยังไงใน marketing ปัจจุบัน
④ ค้นหาเคสจริงด้วย `web_search` — e.g. `"scarcity marketing case study [product]"`
⑤ สรุป insight — จิตวิทยาไหนได้ผล/ไม่ได้ผล, ควรปรับอะไร
⑥ **CRITERION:** output มีอย่างน้อย 3 หลักการ + ตัวอย่างจริง + recommendation

---

## 👥 Pillar 2: Group Psychology (จิตวิทยากลุ่ม)

### Core Principles

| หลักการ | กลไก | การประยุกต์ |
|---------|------|-----------|
| **Herd Behavior** | คนทำตามกลุ่มใหญ่ | แสดงจำนวนผู้ใช้, สร้างกระแส |
| **Bandwagon Effect** | อยากเป็นส่วนหนึ่งของเทรนด์ | ใช้ Influencer, สร้างไวรัล |
| **Tribe Mentality** | ผูกพันกับกลุ่มที่มีอัตลักษณ์ร่วม | Community Building, Brand Loyalty |
| **In-group/Out-group** | ชอบคนกลุ่มเดียวกัน > คนนอก | Target niche communities |
| **Social Comparison** | เปรียบเทียบตัวเองกับคนอื่น | Aspirational Marketing |
| **FOMO** | กลัวตกเทรนด์ | Limited Time Offers |
| **Social Identity** | ซื้อเพื่อแสดงตัวตน | Brand as Status Symbol |
| **Conformity** | ทำตามบรรทัดฐานสังคม | "ทุกคนใช้แบรนด์นี้" |

### Group Psychology Analysis Workflow

① ระบุกลุ่มเป้าหมาย — อายุ, วัฒนธรรม, subculture, community
② วิเคราะห์ social dynamics — ใครเป็น opinion leader? อะไรคือ status symbol?
③ ค้นหาด้วย `web_search` — `"consumer tribe [product category]"`, `"[brand] community culture"`
④ ใช้ `polymarket` ดู prediction เทรนด์กลุ่ม (ถ้ามี market เกี่ยวข้อง)
⑤ Output: Group profile + psychological triggers + community strategy

---

## 📊 Pillar 3: Consumer Segmentation

| Framework | แบ่งตาม | ใช้เมื่อ |
|-----------|---------|---------|
| **Demographic** | อายุ, เพศ, รายได้, การศึกษา, อาชีพ | ตลาดกว้าง, สินค้าทั่วไป |
| **Psychographic (VALS)** | Innovators, Thinkers, Achievers, Experiencers | Lifestyle & values |
| **AIO** | Activities, Interests, Opinions | Content Marketing |
| **Behavioral** | Purchase frequency, usage, loyalty | CRM, Retention |
| **Geographic** | ประเทศ, เมือง, ภูมิอากาศ | Localization |
| **JTBD** | ลูกค้าจ้างผลิตภัณฑ์มาทำ "งาน" อะไร | Innovation |
| **Value-based** | มูลค่าที่ลูกค้าได้รับ vs จ่าย | Pricing |

### Workflow

① เลือก 2-3 frameworks ที่เหมาะกับผลิตภัณฑ์
② Research ด้วย `web_search` — `"consumer segmentation [product] [country]"`
③ สร้าง profile per segment: ชื่อ, pain point, buying trigger, channel, price sensitivity
④ สร้าง spreadsheet ด้วย `xlsx` — sheet ละ 1 segment
⑤ **CRITERION:** ≥ 3 segments, ≥ 5 attributes each

---

## 📈 Pillar 4: Product-Market Analysis

| Framework | วิเคราะห์ | คำถามหลัก |
|-----------|----------|----------|
| **SWOT** | Strengths, Weaknesses, Opportunities, Threats | "เราอยู่ตรงไหน?" |
| **Porter's Five Forces** | Rivalry, Supplier, Buyer, Entry, Substitutes | "แข่งดุแค่ไหน?" |
| **Value Proposition Canvas** | Jobs, Pains, Gains ↔ Relievers, Creators | "แก้ปัญหาอะไร?" |
| **JTBD** | Functional, Emotional, Social Jobs | "จ้างเราทำอะไร?" |
| **Product-Market Fit** | 40% Rule | "ตลาดต้องการจริงไหม?" |
| **Blue Ocean** | สร้างตลาดใหม่ | "แข่งในมิติใหม่?" |

### Workflow

① ระบุผลิตภัณฑ์ + ตลาดเป้าหมาย
② ทำ SWOT — `web_search` หาข้อมูลคู่แข่ง, market size
③ ทำ Porter's Five Forces
④ ทำ Value Proposition Canvas
⑤ `polymarket` เช็ค prediction ถ้ามี
⑥ **CRITERION:** ครบ frameworks, มีแหล่งอ้างอิง, มี actionable recs

---

## 🔧 Tools Integration

| Tool | ใช้ทำอะไร |
|------|----------|
| `web_search` | หาตลาด, trends, เคสศึกษา, คู่แข่ง |
| `web_extract` | Deep-dive reports |
| `blogwatcher` | ติดตาม blogs แบบต่อเนื่อง |
| `polymarket` | Market sentiment, prediction odds |
| `xlsx` | Segmentation spreadsheet |
| `browser` | Visual data, dashboards |
| `arxiv` | Academic papers |
| `llm-wiki` | Knowledge base ถาวร |

---

## 🌏 Cultural Sensitivity

| วัฒนธรรม | ลักษณะเด่น | หลักการที่ได้ผล |
|-----------|-----------|---------------|
| 🇹🇭 ไทย | Collectivist, ราคา敏感 | Social Proof, Reciprocity, Tribe |
| 🇨🇳 จีน | Social Commerce, WeChat | Scarcity, Social Proof, Bandwagon |
| 🇺🇸 อเมริกา | Individualist, Innovation | Loss Aversion, Anchoring |
| 🇪🇺 ยุโรป | Sustainability, Quality | Framing, Endowment Effect |

---

## Common Pitfalls

1. ใช้ framework โดยไม่มีข้อมูลจริง — ต้องมี web_search/web_extract สนับสนุน
2. ลืม cultural context — จิตวิทยาคนไทย ≠ อเมริกัน
3. สรุป vague — ต้องมี actionable recommendation เสมอ
4. ใช้ framework เดียว — cross-validate ≥ 2 frameworks
5. ไม่ถาม user ก่อน — ถ้าไม่ชัดเจน ใช้ `clarify` ถามผลิตภัณฑ์/ตลาด
6. ละเลย polymarket — ถ้ามี prediction market ใช้เพิ่มน้ำหนัก

---

## Verification Checklist

- [ ] ≥ 2 frameworks per analysis
- [ ] ทุก insight มีแหล่งอ้างอิง
- [ ] Cultural context ถูกต้อง
- [ ] มี actionable recommendations
- [ ] Segmentation ≥ 3 segments, ≥ 5 attributes
- [ ] Product analysis ครบ SWOT + Five Forces + Value Proposition
- [ ] Polymarket data ถ้ามี → รวมใน analysis
- [ ] Summary อ่านเข้าใจใน 30 วินาที
