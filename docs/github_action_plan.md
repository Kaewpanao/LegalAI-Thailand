# 🔧 GitHub Action Plan — legalai-thailand-citizen

> **สิ่งที่ต้องแก้ไขใน repo** — เรียงตาม priority

---

## 📁 ไฟล์ที่ต้องแก้ไข

| ไฟล์ | Action | รายละเอียด |
|------|:---:|-----------|
| `domain/types.ts` | ✏️ แก้ | เพิ่ม 6 LegalCategory ใหม่ |
| `lib/legal/diagnosis-config.ts` | ✏️ แก้ | เพิ่ม 6 categories + คำถามละเอียด |
| `lib/legal/sources.ts` | ✏️ แก้ | เพิ่ม sources จาก 6 → 38+ |
| `db/schema.ts` | ✏️ แก้ | เพิ่ม enum legal_category |
| `supabase/migrations/` | ➕ เพิ่ม | migration ใหม่สำหรับ enum |
| `lib/legal/fear-calibration.ts` | ➕ สร้าง | ไฟล์ใหม่ — ถามความกลัว |
| `lib/legal/urgency-windows.ts` | ➕ สร้าง | ไฟล์ใหม่ — deadline mapping |
| `lib/mock/categories.ts` | ✏️ แก้ | เพิ่ม 6 หมวดใหม่ใน UI |

---

## 1. `domain/types.ts` — เพิ่ม 6 LegalCategory

```typescript
// ปัจจุบัน (บรรทัด 14-20):
export type LegalCategory =
  | "labour" | "consumer" | "debt" | "housing" | "family" | "accident";

// เปลี่ยนเป็น:
export type LegalCategory =
  | "labour" | "consumer" | "debt" | "housing" | "family" | "accident"
  | "online_fraud"    // 🔴 P0 — beachhead intent #1
  | "crime"           // 🔴 P0 — ถูกทำร้าย, ลักทรัพย์, ข่มขืน
  | "government"      // 🟡 P1 — ร้องเรียนราชการ
  | "insurance"       // 🟡 P1 — เคลมประกัน
  | "defamation"      // 🟡 P1 — หมิ่นประมาท, ภาพหลุด
  | "property";       // 🟢 P2 — ที่ดิน, มรดกที่ดิน
```

---

## 2. `lib/legal/diagnosis-config.ts` — เพิ่ม 6 Categories

### 🔴 P0: `online_fraud` (เร่งด่วนที่สุด!)

```typescript
online_fraud: {
  version: DIAGNOSIS_CONFIG_VERSION,
  category: "online_fraud",
  questions: [
    {
      id: "fraud_type",
      title: "คุณถูกหลอกแบบไหน?",
      rationale: "เลือกข้อที่ใกล้เคียง เพื่อให้เรารู้ว่าต้องรีบแค่ไหน",
      multi: false,
      options: [
        "ซื้อของออนไลน์ไม่ได้ของ",
        "Call Center หลอกโอนเงิน",
        "แอปกู้เงินเถื่อน",
        "Romance Scam / หลอกรัก",
        "แชร์ลูกโซ่ / ลงทุนปลอม",
      ],
    },
    {
      id: "amount",
      title: "โอนเงินไปเท่าไหร่?",
      rationale: "จำนวนเงินมีผลต่อขั้นตอนการอายัดและความเร่งด่วน",
      multi: false,
      options: ["น้อยกว่า 5,000 บาท", "5,000 – 50,000", "50,001 – 200,000", "มากกว่า 200,000"],
    },
    {
      id: "when",
      title: "โอนเงินไปเมื่อไหร่?",
      rationale: "เวลาผ่านไปนานแค่ไหน — ยิ่งเร็วยิ่งมีโอกาสได้เงินคืน",
      multi: false,
      options: ["ภายใน 24 ชม. (รีบที่สุด!)", "1-3 วัน", "3-7 วัน", "เกิน 7 วัน"],
    },
    {
      id: "evidence",
      title: "คุณมีหลักฐานอะไร?",
      rationale: "เลือกทุกอย่างที่มี — หลักฐานคือหัวใจของการตามเงินคืน",
      multi: true,
      options: ["สลิปโอนเงิน", "แชทกับมิจฉาชีพ", "URL/ลิงก์", "เบอร์โทร", "เลขบัญชีปลายทาง"],
    },
  ],
},
```

### 🔴 P0: `crime` (เหยื่ออาชญากรรม)

```typescript
crime: {
  questions: [
    { id: "crime_type", title: "เกิดอะไรขึ้น?", options: ["ถูกทำร้ายร่างกาย", "ถูกลักทรัพย์/ชิงทรัพย์", "ถูกข่มขืน/คุกคามทางเพศ", "ถูกขู่กรรโชก"] },
    { id: "when", title: "เกิดขึ้นเมื่อไหร่?", options: ["กำลังเกิด/เพิ่งเกิด", "ภายใน 24 ชม.", "1-7 วัน", "เกิน 7 วัน"] },
    { id: "evidence", title: "มีหลักฐานอะไร?", options: ["ใบรับรองแพทย์", "ภาพถ่าย", "พยาน", "คลิป/กล้องวงจรปิด"] },
    { id: "reported", title: "แจ้งความแล้วหรือยัง?", options: ["ยัง", "แจ้งแล้ว", "ไม่แน่ใจ"] },
  ],
},
```

### 🟡 P1: `defamation`

```typescript
defamation: {
  questions: [
    { id: "type", title: "เกิดอะไรขึ้น?", options: ["ถูกด่าบนโซเชียล", "ภาพหลุด/แอบถ่าย", "ถูกใส่ความ", "ข้อมูลส่วนตัวรั่วไหล"] },
    { id: "platform", title: "ผ่านช่องทางไหน?", options: ["Facebook", "LINE", "TikTok", "X (Twitter)", "เว็บบอร์ด"] },
    { id: "evidence", title: "มีหลักฐานอะไร?", options: ["แคปหน้าจอ", "URL", "พยาน", "บันทึกแชท"] },
  ],
},
```

### 🟡 P1: `insurance`

```typescript
insurance: {
  questions: [
    { id: "type", title: "ปัญหาประกันอะไร?", options: ["เคลมประกันรถ", "เคลมประกันสุขภาพ", "บริษัทยกเลิกกรมธรรม์", "ประกันไม่จ่ายตามสัญญา"] },
    { id: "evidence", title: "มีหลักฐานอะไร?", options: ["กรมธรรม์", "ใบแจ้งเหตุ", "ใบรับรองแพทย์", "รูปถ่าย"] },
  ],
},
```

### 🟡 P1: `government`

```typescript
government: {
  questions: [
    { id: "type", title: "ปัญหาเกี่ยวกับอะไร?", options: ["ขอทะเบียน/บัตร ปชช.ไม่ได้", "ถูกรัฐละเมิด", "ร้องเรียนแล้วไม่ตอบ", "ถูกเวนคืนที่ดิน"] },
    { id: "duration", title: "รอมานานแค่ไหน?", options: ["น้อยกว่า 30 วัน", "1-3 เดือน", "3-6 เดือน", "เกิน 6 เดือน"] },
  ],
},
```

### 🟢 P2: `property`

```typescript
property: {
  questions: [
    { id: "type", title: "ปัญหาเกี่ยวกับอะไร?", options: ["ที่ดินถูกบุกรุก", "แนวเขตไม่ชัด", "ซื้อขายไม่ได้", "มรดกที่ดิน", "โฉนดหาย"] },
  ],
},
```

---

## 3. `lib/legal/sources.ts` — เพิ่ม Legal Sources

```typescript
// เพิ่ม sources สำหรับ 6 หมวดใหม่ + เติม 2 หมวดที่ว่าง (family, accident):

export const legalSources: Record<string, LegalSource> = {
  // ... existing 6 sources ...

  // 🔴 Online Fraud
  "criminal-code-341": {
    id: "criminal-code-341",
    title: "ประมวลกฎหมายอาญา มาตรา 341 (ฉ้อโกง)",
    jurisdiction: "ประเทศไทย", effectiveDate: "2500-01-01", checkedDate: "2569-08-01",
    url: "https://www.ratchakitcha.soc.go.th", kind: "law",
  },
  "computer-crime-act-2560": {
    id: "computer-crime-act-2560",
    title: "พ.ร.บ. ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ (ฉบับที่ 2) พ.ศ. 2560",
    jurisdiction: "ประเทศไทย", effectiveDate: "2560-05-24", checkedDate: "2569-08-01",
    url: "https://www.ratchakitcha.soc.go.th", kind: "law",
  },
  "amlo-act-2542": {
    id: "amlo-act-2542",
    title: "พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน พ.ศ. 2542",
    jurisdiction: "ประเทศไทย", effectiveDate: "2542-08-19", checkedDate: "2569-08-01",
    url: "https://www.amlo.go.th", kind: "law",
  },

  // 🔴 Crime
  "criminal-code-295": {
    id: "criminal-code-295", title: "ป.อาญา ม.295 (ทำร้ายร่างกาย)", /* ... */ kind: "law",
  },
  "criminal-code-276": {
    id: "criminal-code-276", title: "ป.อาญา ม.276 (ข่มขืนกระทำชำเรา)", /* ... */ kind: "law",
  },

  // 🟡 Defamation
  "criminal-code-326": {
    id: "criminal-code-326", title: "ป.อาญา ม.326 (หมิ่นประมาท)", /* ... */ kind: "law",
  },
  "pdpa-2562": {
    id: "pdpa-2562", title: "พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562", /* ... */ kind: "law",
  },

  // 🟡 Insurance
  "insurance-act-2535": {
    id: "insurance-act-2535", title: "พ.ร.บ. ประกันวินาศภัย พ.ศ. 2535", /* ... */ kind: "law",
  },
  "oic-act-2550": {
    id: "oic-act-2550", title: "พ.ร.บ. คณะกรรมการกำกับและส่งเสริมการประกอบธุรกิจประกันภัย พ.ศ. 2550", /* ... */ kind: "law",
  },

  // 🟡 Government
  "administrative-court-act-2542": {
    id: "admin-court-2542", title: "พ.ร.บ. จัดตั้งศาลปกครองฯ พ.ศ. 2542", /* ... */ kind: "law",
  },

  // 🟢 Property
  "land-code-2497": {
    id: "land-code-2497", title: "ประมวลกฎหมายที่ดิน พ.ศ. 2497", /* ... */ kind: "law",
  },
  "civil-code-property": {
    id: "civil-code-property", title: "ป.พ.พ. บรรพ 4 (ทรัพย์สิน)", /* ... */ kind: "law",
  },

  // Fill missing: family, accident
  "civil-code-family": { id: "civil-code-family", title: "ป.พ.พ. บรรพ 5 (ครอบครัว)", /* ... */ kind: "law" },
  "traffic-act-2522": { id: "traffic-act-2522", title: "พ.ร.บ. จราจรทางบก พ.ศ. 2522", /* ... */ kind: "law" },
};

export function sourcesForCategory(category: string): LegalSource[] {
  const map: Record<string, string[]> = {
    labour: ["labour-protection-act-2541", "labour-court-act-2522"],
    consumer: ["consumer-protection-act-2522"],
    debt: ["civil-commercial-code-debt"],
    housing: ["civil-commercial-code-hire"],
    family: ["civil-code-family"],                    // ⬅ เติม!
    accident: ["traffic-act-2522"],                   // ⬅ เติม!
    online_fraud: ["criminal-code-341", "computer-crime-act-2560", "amlo-act-2542"],  // ⬅ ใหม่
    crime: ["criminal-code-295", "criminal-code-276"],                                 // ⬅ ใหม่
    defamation: ["criminal-code-326", "pdpa-2562"],                                    // ⬅ ใหม่
    insurance: ["insurance-act-2535", "oic-act-2550"],                                 // ⬅ ใหม่
    government: ["admin-court-2542"],                                                   // ⬅ ใหม่
    property: ["land-code-2497", "civil-code-property"],                               // ⬅ ใหม่
  };
  return (map[category] ?? []).map((id) => legalSources[id]).filter(Boolean);
}
```

---

## 4. `db/schema.ts` — เพิ่ม Enum

```typescript
// บรรทัด 43-50: เพิ่มค่าใหม่ใน legal_category enum
export const legalCategory = pgEnum("legal_category", [
  "labour", "consumer", "debt", "housing", "family", "accident",
  "online_fraud",    // ⬅ ใหม่
  "crime",           // ⬅ ใหม่
  "government",      // ⬅ ใหม่
  "insurance",       // ⬅ ใหม่
  "defamation",      // ⬅ ใหม่
  "property",        // ⬅ ใหม่
]);
```

### Migration SQL (`supabase/migrations/0003_add_categories.sql`):

```sql
ALTER TYPE legal_category ADD VALUE 'online_fraud';
ALTER TYPE legal_category ADD VALUE 'crime';
ALTER TYPE legal_category ADD VALUE 'government';
ALTER TYPE legal_category ADD VALUE 'insurance';
ALTER TYPE legal_category ADD VALUE 'defamation';
ALTER TYPE legal_category ADD VALUE 'property';
```

---

## 5. ไฟล์ใหม่ — `lib/legal/fear-calibration.ts`

```typescript
/** Fear Calibration — ถามความกลัวก่อน diagnosis */

export type FearLevel = "panic" | "urgent" | "concerned" | "planning";

export const FEAR_CALIBRATION = {
  question: "คุณรู้สึกยังไงกับเรื่องนี้?",
  rationale: "เราเข้าใจว่าปัญหากฎหมายทำให้เครียด — บอกเราเพื่อให้เราช่วยได้ตรงจุด",
  options: [
    { value: "panic", label: "😰 กลัวมาก — ต้องทำอะไรสักอย่างเดี๋ยวนี้!", urgency: "immediate" },
    { value: "urgent", label: "😟 กังวล — อยากรู้ว่าต้องเริ่มจากตรงไหน", urgency: "days" },
    { value: "concerned", label: "🤔 เป็นห่วง — อยากรู้สิทธิและเตรียมตัว", urgency: "weeks" },
    { value: "planning", label: "📋 วางแผน — ยังไม่รีบ แต่อยากรู้ไว้ก่อน", urgency: "months" },
  ],
};

/** Map fear level → urgency window for Loss Aversion messaging */
export const URGENCY_MESSAGES: Record<FearLevel, string> = {
  panic: "⏰ เร่งด่วน! ทำเลยตอนนี้ — ทุกนาทีมีค่า",
  urgent: "⚡ ควรทำภายใน 1-3 วัน — อย่ารอจนสาย",
  concerned: "📅 ควรทำภายใน 1-2 สัปดาห์",
  planning: "📋 ไม่ต้องรีบ — แต่เริ่มวันนี้ดีกว่าพรุ่งนี้",
};
```

---

## 6. `lib/mock/categories.ts` — เพิ่มหมวดใน UI

```typescript
// เพิ่ม 6 รายการใน categories array:
{ id: "online_fraud", icon: "💻", title: "ภัยออนไลน์", hint: "ถูกโกง · Call Center · แอปเถื่อน" },
{ id: "crime",        icon: "🚨", title: "เหยื่ออาชญากรรม", hint: "ทำร้าย · ลักทรัพย์ · คุกคาม" },
{ id: "government",   icon: "🏛️", title: "เรื่องราชการ", hint: "ทะเบียน · ร้องเรียน · ถูกเวนคืน" },
{ id: "insurance",    icon: "🛡️", title: "ประกันภัย", hint: "เคลม · กรมธรรม์ · สุขภาพ" },
{ id: "defamation",   icon: "📢", title: "หมิ่นประมาท", hint: "ด่าออนไลน์ · ภาพหลุด · PDPA" },
{ id: "property",     icon: "🏠", title: "ที่ดิน/ทรัพย์สิน", hint: "บุกรุก · โฉนด · มรดก" },
```

---

## 📊 Priority Summary

| Priority | งาน | ไฟล์ | Effort |
|:---:|------|------|:---:|
| 🔴 **P0** | เพิ่ม `online_fraud` + `crime` categories | types.ts, diagnosis-config.ts, sources.ts, schema.ts | 2-3 ชม. |
| 🔴 **P0** | เพิ่ม fear calibration | fear-calibration.ts (ใหม่) | 1 ชม. |
| 🔴 **P0** | เติม sources ให้ family + accident | sources.ts | 30 นาที |
| 🟡 **P1** | เพิ่ม `defamation` + `insurance` + `government` | types.ts, diagnosis-config.ts, sources.ts | 2 ชม. |
| 🟡 **P1** | เพิ่ม urgency windows module | urgency-windows.ts (ใหม่) | 1 ชม. |
| 🟢 **P2** | เพิ่ม `property` category | types.ts, diagnosis-config.ts, sources.ts | 1 ชม. |
| 🟢 **P2** | อัปเดต mock categories UI | categories.ts | 30 นาที |
| 🟢 **P2** | Migration SQL | 0003_add_categories.sql | 15 นาที |

> ⏱️ **รวม: ~8-10 ชั่วโมง** — ทำเสร็จภายใน 1-2 วัน!
