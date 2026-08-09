# 🐛 LegalAI Thailand — Bug Fix Plan (QA Findings)
> **Generated:** 9 ส.ค. 2569 | **Repo:** `D:\legalai-citizen-check` | **Total Issues:** 17 (11 broken buttons + 6 missing documents)

---

## 📊 Summary

| Priority | Count | Description |
|----------|-------|-------------|
| 🔴 P0 — Critical | 3 | Case tabs broken, missing /terms, missing /privacy |
| 🟡 P1 — High | 7 | Settings, consent, sort, filters, share, links, disclaimers |
| 🟢 P2 — Low | 4 | Mark-read, save-lawyer, assistant menu, pricing page |

---

# SECTION 1: Fix Plan by Priority

---

## 🔴 P0 — Critical (วิกฤติ)

### P0-1: Case Tabs มี `href="#"` — ต้องเปลี่ยนเป็น route จริง

- **ไฟล์:** `app/cases/[caseId]/timeline/page.tsx` (line 63-79)
- **ปัญหา:** แท็บ "ภาพรวม / ไทม์ไลน์ / หลักฐาน / เอกสาร" ทุกแท็บใช้ `href="#"` พร้อม `e.preventDefault()` — คลิกแล้วไม่ไปไหน
- **Code Fix:**

```tsx
// BEFORE (line 63-79):
<nav className="case-tabs" aria-label="แท็บเคส">
  {tabs.map((t) => (
    <Link
      key={t.label}
      href="#"
      className={t.active ? "active" : ""}
      aria-current={t.active ? "page" : undefined}
      onClick={(e) => {
        e.preventDefault();
        recordEvent({ type: "search_submitted", category: "labour" });
      }}
    >
      {t.label}
      {t.count ? <i>{t.count}</i> : null}
    </Link>
  ))}
</nav>

// AFTER:
<nav className="case-tabs" aria-label="แท็บเคส">
  {tabs.map((t) => {
    const tabHref =
      t.label === "ภาพรวม"   ? `/cases/${caseId}/timeline` :
      t.label === "ไทม์ไลน์"  ? `/cases/${caseId}/timeline` :
      t.label === "หลักฐาน"   ? `/cases/${caseId}/evidence` :
      t.label === "เอกสาร"    ? "/documents" :
      "#";
    return (
      <Link
        key={t.label}
        href={tabHref}
        className={t.active ? "active" : ""}
        aria-current={t.active ? "page" : undefined}
        onClick={() =>
          recordEvent({ type: "search_submitted", category: "labour" })
        }
      >
        {t.label}
        {t.count ? <i>{t.count}</i> : null}
      </Link>
    );
  })}
</nav>
```

- **Verification:** 
  1. ไปที่ `/cases/case-1/timeline`
  2. คลิกแท็บ "หลักฐาน" → ต้องไป `/cases/case-1/evidence`
  3. คลิกแท็บ "เอกสาร" → ต้องไป `/documents`
  4. คลิกแท็บ "ภาพรวม" / "ไทม์ไลน์" → อยู่หน้าเดิม

---

### P0-2: สร้างหน้า `/terms` (ข้อกำหนดการใช้บริการ)

- **ไฟล์ใหม่:** `app/terms/page.tsx`
- **ปัญหา:** ไม่มีหน้า Terms of Service เลย — ถ้าผู้ใช้คลิกลิงก์ไป `/terms` จะได้ 404
- **Code Fix:** สร้างไฟล์ใหม่

```tsx
import type { Metadata } from "next";
import { PageHead, LegalDisclaimer } from "@/components/ui/primitives";
import Link from "next/link";

export const metadata: Metadata = {
  title: "ข้อกำหนดการใช้บริการ — LegalAI Thailand",
};

export default function TermsPage() {
  return (
    <>
      <PageHead
        backHref="/"
        title="ข้อกำหนดการใช้บริการ"
        subtitle="Terms of Service — อ่านทำความเข้าใจก่อนใช้งาน"
      />
      <article className="legal-page">
        <section>
          <h2>1. การยอมรับข้อกำหนด</h2>
          <p>
            การเข้าใช้งานเว็บไซต์และบริการของ LegalAI Thailand ถือว่าคุณยอมรับข้อกำหนด
            และเงื่อนไขทั้งหมดนี้ หากคุณไม่ยอมรับ โปรดหยุดใช้งานทันที
          </p>
        </section>

        <section>
          <h2>2. ลักษณะของบริการ</h2>
          <p>
            LegalAI Thailand เป็นเครื่องมือช่วยค้นหาข้อมูลกฎหมายเบื้องต้นด้วย AI
            <strong>ไม่ใช่การให้คำปรึกษาทางกฎหมาย</strong> และ
            <strong>ไม่ใช่ทนายความ</strong> ข้อมูลที่ได้จากระบบเป็นเพียงแนวทางเบื้องต้นเท่านั้น
          </p>
        </section>

        <section>
          <h2>3. ข้อจำกัดความรับผิด</h2>
          <ul>
            <li>เราไม่รับประกันความถูกต้อง ครบถ้วน หรือทันสมัยของข้อมูลกฎหมาย</li>
            <li>ผลลัพธ์จาก AI อาจคลาดเคลื่อน — ควรตรวจสอบกับผู้เชี่ยวชาญก่อนดำเนินการ</li>
            <li>เราไม่รับผิดต่อความเสียหายที่เกิดจากการใช้หรือการเชื่อถือข้อมูลในระบบ</li>
          </ul>
        </section>

        <section>
          <h2>4. ทรัพย์สินทางปัญญา</h2>
          <p>
            เนื้อหา โลโก้ การออกแบบ และซอร์สโค้ดทั้งหมดเป็นกรรมสิทธิ์ของ LegalAI Thailand
            ห้ามทำซ้ำ ดัดแปลง หรือเผยแพร่โดยไม่ได้รับอนุญาต
          </p>
        </section>

        <section>
          <h2>5. การยกเลิกการใช้งาน</h2>
          <p>
            เราขอสงวนสิทธิ์ในการระงับหรือยกเลิกการให้บริการแก่ผู้ใช้ที่ละเมิดข้อกำหนด
            โดยไม่ต้องแจ้งล่วงหน้า
          </p>
        </section>

        <section>
          <h2>6. การเปลี่ยนแปลงข้อกำหนด</h2>
          <p>
            เราอาจปรับปรุงข้อกำหนดนี้เป็นครั้งคราว โดยจะแจ้งให้ทราบผ่านทางเว็บไซต์
            การใช้งานต่อหลังจากมีการเปลี่ยนแปลงถือว่าคุณยอมรับข้อกำหนดใหม่
          </p>
        </section>

        <section>
          <h2>7. กฎหมายที่ใช้บังคับ</h2>
          <p>
            ข้อกำหนดนี้อยู่ภายใต้บังคับของกฎหมายไทย และให้ตีความตามกฎหมายไทย
            ข้อพิพาทใดๆ ให้อยู่ในเขตอำนาจศาลไทย
          </p>
        </section>

        <p className="legal-updated">อัปเดตล่าสุด: 9 สิงหาคม 2569</p>
      </article>
      <LegalDisclaimer>
        ⓘ หากมีคำถามเกี่ยวกับข้อกำหนดการใช้บริการ กรุณาติดต่อเราที่ legal@legalai.th
      </LegalDisclaimer>
    </>
  );
}
```

- **Verification:**
  1. เปิด `/terms` ใน browser
  2. ต้องเห็นเนื้อหาครบ 7 sections
  3. ที่ด้านล่างมี disclaimer
  4. ปุ่มย้อนกลับ (‹) ทำงานได้

---

### P0-3: สร้างหน้า `/privacy` (นโยบายความเป็นส่วนตัว — PDPA)

- **ไฟล์ใหม่:** `app/privacy/page.tsx`
- **ปัญหา:** ไม่มีหน้า Privacy Policy — เสี่ยงผิด PDPA/พรบ.คุ้มครองข้อมูลส่วนบุคคล
- **Code Fix:** สร้างไฟล์ใหม่

```tsx
import type { Metadata } from "next";
import { PageHead, LegalDisclaimer } from "@/components/ui/primitives";

export const metadata: Metadata = {
  title: "นโยบายความเป็นส่วนตัว — LegalAI Thailand",
};

export default function PrivacyPage() {
  return (
    <>
      <PageHead
        backHref="/"
        title="นโยบายความเป็นส่วนตัว"
        subtitle="Privacy Policy — ตามพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA)"
      />
      <article className="legal-page">
        <section>
          <h2>1. ข้อมูลที่เราเก็บรวบรวม</h2>
          <p>เราเก็บรวบรวมข้อมูลดังต่อไปนี้:</p>
          <ul>
            <li><strong>ข้อมูลส่วนตัว:</strong> ชื่อ, อีเมล, เบอร์โทรศัพท์ (เมื่อคุณลงทะเบียน)</li>
            <li><strong>ข้อมูลเคส:</strong> รายละเอียดปัญหากฎหมาย, หลักฐานที่อัปโหลด, ผลการวิเคราะห์</li>
            <li><strong>ข้อมูลการใช้งาน:</strong> หน้าเว็บที่เข้าชม, การคลิก, เวลาที่ใช้ในระบบ</li>
            <li><strong>ข้อมูลเทคนิค:</strong> IP address, ประเภท browser, ระบบปฏิบัติการ</li>
          </ul>
        </section>

        <section>
          <h2>2. วัตถุประสงค์ในการเก็บข้อมูล</h2>
          <p>เราใช้ข้อมูลของคุณเพื่อ:</p>
          <ul>
            <li>ให้บริการวิเคราะห์กฎหมายและสร้างเอกสาร</li>
            <li>ปรับปรุงความแม่นยำของ AI</li>
            <li>ส่งการแจ้งเตือนเกี่ยวกับเคสของคุณ</li>
            <li>ปฏิบัติตามกฎหมาย (PDPA, กฎหมายไทย)</li>
          </ul>
        </section>

        <section>
          <h2>3. ฐานกฎหมายในการประมวลผล (PDPA)</h2>
          <p>เราประมวลผลข้อมูลของคุณภายใต้ฐานกฎหมายดังนี้:</p>
          <ul>
            <li><strong>ความยินยอม (Consent):</strong> สำหรับการส่งข่าวสารการตลาด</li>
            <li><strong>การปฏิบัติตามสัญญา (Contract):</strong> เพื่อให้บริการวิเคราะห์เคส</li>
            <li><strong>ประโยชน์โดยชอบด้วยกฎหมาย (Legitimate Interest):</strong> การปรับปรุงบริการ</li>
          </ul>
        </section>

        <section>
          <h2>4. การเก็บรักษาและความปลอดภัย</h2>
          <p>
            ข้อมูลของคุณถูกเก็บในเซิร์ฟเวอร์ที่เข้ารหัสตามมาตรฐานสากล (AES-256)
            เราเก็บข้อมูลเคสเป็นเวลา 5 ปีนับจากวันที่เคสเสร็จสิ้น
            หลังจากนั้นจะลบหรือทำให้นิรนาม
          </p>
        </section>

        <section>
          <h2>5. การเปิดเผยข้อมูลแก่บุคคลภายนอก</h2>
          <p>เรา<strong>ไม่ขาย</strong>ข้อมูลของคุณให้บุคคลภายนอก เราอาจเปิดเผยข้อมูลเมื่อ:</p>
          <ul>
            <li>คุณร้องขอให้แชร์เคสกับทนายความ</li>
            <li>มีคำสั่งศาลหรือหมายศาลที่ถูกต้องตามกฎหมาย</li>
            <li>จำเป็นต้องใช้ผู้ให้บริการคลาวด์ (Cloud Provider) เพื่อให้บริการ — ซึ่งผูกพันตามสัญญาประมวลผลข้อมูล</li>
          </ul>
        </section>

        <section>
          <h2>6. สิทธิของคุณภายใต้ PDPA</h2>
          <p>คุณมีสิทธิตามกฎหมายดังต่อไปนี้:</p>
          <ul>
            <li><strong>สิทธิขอเข้าถึง:</strong> ขอสำเนาข้อมูลของคุณ</li>
            <li><strong>สิทธิขอแก้ไข:</strong> แก้ไขข้อมูลที่ไม่ถูกต้อง</li>
            <li><strong>สิทธิขอลบ:</strong> ขอลบข้อมูลของคุณ (Right to be Forgotten)</li>
            <li><strong>สิทธิขอถอนความยินยอม:</strong> ถอน consent ได้ทุกเมื่อ</li>
            <li><strong>สิทธิคัดค้าน:</strong> คัดค้านการประมวลผลข้อมูล</li>
            <li><strong>สิทธิขอโอนย้าย:</strong> ขอข้อมูลในรูปแบบที่อ่านได้ด้วยเครื่อง</li>
          </ul>
        </section>

        <section>
          <h2>7. การใช้คุกกี้</h2>
          <p>
            เราใช้คุกกี้ที่จำเป็นต่อการทำงานของระบบเท่านั้น (Essential Cookies)
            ไม่มีการใช้คุกกี้เพื่อการโฆษณาหรือติดตามพฤติกรรม
          </p>
        </section>

        <section>
          <h2>8. ติดต่อเจ้าหน้าที่คุ้มครองข้อมูล (DPO)</h2>
          <p>
            หากมีคำถามเกี่ยวกับนโยบายนี้ หรือต้องการใช้สิทธิตาม PDPA:
            <br />
            📧 dpo@legalai.th
            <br />
            📞 02-XXX-XXXX
          </p>
        </section>

        <p className="legal-updated">อัปเดตล่าสุด: 9 สิงหาคม 2569</p>
      </article>
      <LegalDisclaimer>
        ⓘ นโยบายนี้เป็นไปตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA)
      </LegalDisclaimer>
    </>
  );
}
```

- **Verification:**
  1. เปิด `/privacy` ใน browser
  2. ต้องเห็น 8 sections ครบถ้วน
  3. ต้องกล่าวถึง PDPA และสิทธิของผู้ใช้
  4. มีช่องทางติดต่อ DPO

---

## 🟡 P1 — High (สูง)

### P1-1: Settings Tabs — เพิ่ม useState + conditional render

- **ไฟล์:** `app/profile/page.tsx` (line 19-71, 74-148)
- **ปัญหา:** แถบตั้งค่า (ข้อมูลส่วนตัว, การแจ้งเตือน, ความเป็นส่วนตัว, ฯลฯ) เป็นปุ่มที่คลิกแล้วไม่เปลี่ยนหน้า — ต้องใช้ useState เพื่อ switch แสดงเนื้อหาตามแท็บที่เลือก
- **Code Fix:**

```tsx
// BEFORE (line 19-26):
const SETTINGS_NAV = [
  { label: "○ ข้อมูลส่วนตัว", active: true },
  { label: "♧ การแจ้งเตือน", active: false },
  { label: "⌾ ความเป็นส่วนตัว", active: false },
  { label: "◫ การแสดงผล", active: false },
  { label: "฿ แพ็กเกจและการชำระเงิน", active: false },
  { label: "ⓘ ช่วยเหลือ", active: false },
];

// AFTER:
const SETTINGS_NAV = [
  { label: "○ ข้อมูลส่วนตัว", key: "personal" },
  { label: "♧ การแจ้งเตือน", key: "notifications" },
  { label: "⌾ ความเป็นส่วนตัว", key: "privacy" },
  { label: "◫ การแสดงผล", key: "display" },
  { label: "฿ แพ็กเกจและการชำระเงิน", key: "billing" },
  { label: "ⓘ ช่วยเหลือ", key: "help" },
] as const;
```

```tsx
// BEFORE (line 28 — only line + toggleLine state):
export default function ProfilePage() {
  const notify = useToast();
  const [line, setLine] = useState(true);

// AFTER — add activeTab state:
export default function ProfilePage() {
  const notify = useToast();
  const [line, setLine] = useState(true);
  const [activeTab, setActiveTab] = useState<string>("personal");
```

```tsx
// BEFORE (line 63-71 — sidebar buttons, all static):
<aside>
  {SETTINGS_NAV.map((item) => (
    <button
      key={item.label}
      className={item.active ? "active" : ""}
      type="button"
    >
      {item.label}
    </button>
  ))}
</aside>

// AFTER:
<aside>
  {SETTINGS_NAV.map((item) => (
    <button
      key={item.key}
      className={activeTab === item.key ? "active" : ""}
      type="button"
      onClick={() => setActiveTab(item.key)}
    >
      {item.label}
    </button>
  ))}
</aside>
```

```tsx
// BEFORE (line 74-148 — always shows all sections):
<section>
  <div className="settings-card"> ... ข้อมูลส่วนตัว ... </div>
  <div className="settings-card"> ... บัญชีที่เชื่อมต่อ ... </div>
  <div className="settings-card"> ... ภาษาและการแสดงผล ... </div>
</section>

// AFTER — conditional render:
<section>
  {activeTab === "personal" && (
    <>
      <div className="settings-card">
        <h3>ข้อมูลส่วนตัว</h3>
        <div className="form-grid">
          <label>ชื่อ<input defaultValue="นภัสสร" /></label>
          <label>นามสกุล<input defaultValue="วัฒนะ" /></label>
          <label>อีเมล<input defaultValue="napassorn@example.com" /></label>
          <label>เบอร์โทรศัพท์<input defaultValue="089 123 4567" /></label>
        </div>
        <button className="primary" type="button" onClick={() => notify("บันทึกข้อมูลส่วนตัวแล้ว")}>
          บันทึกการเปลี่ยนแปลง
        </button>
      </div>

      <div className="settings-card">
        <h3>บัญชีที่เชื่อมต่อ</h3>
        <div className="connection">
          <span className="line-logo">LINE</span>
          <div>
            <strong>LINE</strong>
            <small>{line ? "เชื่อมต่อแล้ว • รับการแจ้งเตือนผ่าน LINE" : "ยังไม่ได้เชื่อมต่อ"}</small>
          </div>
          <Pill tone={line ? "green" : "gray"}>{line ? "เชื่อมต่อแล้ว" : "ยังไม่เชื่อมต่อ"}</Pill>
          <button type="button" onClick={toggleLine}>{line ? "ยกเลิก" : "เชื่อมต่อ"}</button>
        </div>
      </div>
    </>
  )}

  {activeTab === "notifications" && (
    <div className="settings-card">
      <h3>การแจ้งเตือน</h3>
      <p>เลือกช่องทางรับการแจ้งเตือน</p>
      <div className="select-row">
        <div><strong>อีเมล</strong><small>รับสรุปเคสรายสัปดาห์</small></div>
        <input type="checkbox" defaultChecked />
      </div>
      <div className="select-row">
        <div><strong>LINE</strong><small>แจ้งเตือนกำหนดการสำคัญ</small></div>
        <input type="checkbox" defaultChecked />
      </div>
      <div className="select-row">
        <div><strong>ในแอป</strong><small>อัปเดตความคืบหน้าเคส</small></div>
        <input type="checkbox" defaultChecked />
      </div>
    </div>
  )}

  {activeTab === "privacy" && (
    <div className="settings-card">
      <h3>ความเป็นส่วนตัวและการยินยอม</h3>
      {/* P1-2 content goes here — see next fix */}
      <PrivacyConsentSection />
    </div>
  )}

  {activeTab === "display" && (
    <div className="settings-card">
      <h3>ภาษาและการแสดงผล</h3>
      <div className="select-row">
        <div><strong>ภาษา</strong><small>ภาษาที่ใช้ในแอปและเอกสาร</small></div>
        <select defaultValue="ไทย"><option>ไทย</option><option>English</option></select>
      </div>
      <div className="select-row">
        <div><strong>ขนาดตัวอักษร</strong><small>ปรับให้อ่านง่ายขึ้น</small></div>
        <select defaultValue="มาตรฐาน"><option>มาตรฐาน</option><option>ใหญ่</option></select>
      </div>
    </div>
  )}

  {activeTab === "billing" && (
    <div className="settings-card">
      <h3>แพ็กเกจและการชำระเงิน</h3>
      <p>แพ็กเกจปัจจุบัน: <strong>พื้นฐาน (ฟรี)</strong></p>
      <p>อัปเกรดเพื่อรับสิทธิ์เพิ่มเติม:</p>
      <ul>
        <li>✓ วิเคราะห์เคสไม่จำกัด</li>
        <li>✓ สร้างเอกสารกฎหมาย</li>
        <li>✓ ปรึกษาทนายออนไลน์</li>
      </ul>
      <button className="primary" onClick={() => notify("กำลังไปยังหน้าแพ็กเกจ")}>ดูแพ็กเกจทั้งหมด →</button>
    </div>
  )}

  {activeTab === "help" && (
    <div className="settings-card">
      <h3>ช่วยเหลือ</h3>
      <p>คู่มือการใช้งาน:</p>
      <ul>
        <li><a href="/terms">ข้อกำหนดการใช้บริการ</a></li>
        <li><a href="/privacy">นโยบายความเป็นส่วนตัว</a></li>
        <li>📧 ติดต่อ: help@legalai.th</li>
        <li>📞 โทร: 02-XXX-XXXX (จ-ศ 9:00-17:00)</li>
      </ul>
    </div>
  )}
</section>
```

- **Verification:**
  1. ไปที่ `/profile`
  2. คลิก "♧ การแจ้งเตือน" → ต้องเห็น toggle อีเมล/ LINE/ ในแอป
  3. คลิก "⌾ ความเป็นส่วนตัว" → ต้องเห็น privacy section
  4. คลิก "฿ แพ็กเกจและการชำระเงิน" → ต้องเห็น billing section
  5. คลิก "ⓘ ช่วยเหลือ" → ต้องเห็นลิงก์ /terms และ /privacy

---

### P1-2: AI Consent — Toggle + Delete Data + Export

- **ไฟล์:** `app/profile/page.tsx` (เพิ่มใน privacy tab จาก P1-1)
- **ปัญหา:** ไม่มี UI สำหรับ toggle consent AI, ลบข้อมูล, export ข้อมูล — จำเป็นตาม PDPA
- **Code Fix:** เพิ่ม component ในไฟล์เดียวกัน

```tsx
// Add this component INSIDE the same file (before or after ProfilePage):

function PrivacyConsentSection() {
  const notify = useToast();
  const [aiConsent, setAiConsent] = useState(true);
  const [marketingConsent, setMarketingConsent] = useState(false);
  const [deleting, setDeleting] = useState(false);

  function handleExport() {
    notify("กำลังเตรียมข้อมูลของคุณเพื่อดาวน์โหลด...");
    recordEvent({ type: "data_export_requested" as any });
    // TODO: wire to real API
  }

  function handleDelete() {
    if (!window.confirm("คุณแน่ใจหรือไม่ที่จะลบข้อมูลทั้งหมด?\nการดำเนินการนี้ไม่สามารถย้อนกลับได้")) return;
    setDeleting(true);
    notify("กำลังดำเนินการลบข้อมูลของคุณ...");
    // TODO: wire to real API
    setTimeout(() => {
      setDeleting(false);
      notify("ลบข้อมูลของคุณเรียบร้อยแล้ว");
    }, 1500);
  }

  return (
    <>
      <h3>ความเป็นส่วนตัวและการยินยอม</h3>

      <div className="select-row">
        <div>
          <strong>ยินยอมให้ AI วิเคราะห์ข้อมูล</strong>
          <small>อนุญาตให้ AI ประมวลผลข้อมูลเคสเพื่อวิเคราะห์</small>
        </div>
        <button
          type="button"
          className={aiConsent ? "toggle on" : "toggle"}
          onClick={() => {
            setAiConsent(!aiConsent);
            notify(aiConsent ? "ปิดการใช้ AI วิเคราะห์แล้ว" : "เปิดการใช้ AI วิเคราะห์แล้ว");
          }}
          aria-pressed={aiConsent}
        >
          {aiConsent ? "開啟" : "ปิด"}
        </button>
      </div>

      <div className="select-row">
        <div>
          <strong>ยินยอมรับข่าวสารการตลาด</strong>
          <small>รับอีเมลเกี่ยวกับบริการใหม่และโปรโมชัน</small>
        </div>
        <button
          type="button"
          className={marketingConsent ? "toggle on" : "toggle"}
          onClick={() => {
            setMarketingConsent(!marketingConsent);
            notify(marketingConsent ? "ยกเลิกรับข่าวสารแล้ว" : "สมัครรับข่าวสารแล้ว");
          }}
          aria-pressed={marketingConsent}
        >
          {marketingConsent ? "開啟" : "ปิด"}
        </button>
      </div>

      <div style={{ display: "flex", gap: 12, marginTop: 18 }}>
        <button className="outline" onClick={handleExport}>
          📥 ส่งออกข้อมูลของฉัน
        </button>
        <button
          className="outline danger"
          onClick={handleDelete}
          disabled={deleting}
        >
          {deleting ? "กำลังลบ..." : "🗑 ลบข้อมูลของฉัน"}
        </button>
      </div>
    </>
  );
}
```

- **Verification:**
  1. ไปที่ `/profile` → คลิก "⌾ ความเป็นส่วนตัว"
  2. Toggle "AI วิเคราะห์" — ต้องเห็น toast
  3. คลิก "ส่งออกข้อมูลของฉัน" — ต้องเห็น toast
  4. คลิก "ลบข้อมูลของฉัน" — ต้องมี confirm dialog → toast

---

### P1-3: Sort Dropdown — เปลี่ยนจาก static button เป็น select menu

- **ไฟล์:** `app/search/page.tsx` (line 61)
- **ปัญหา:** ปุ่ม "เกี่ยวข้องมากที่สุด⌄" เป็น static — ไม่เปลี่ยนการเรียง
- **Code Fix:**

```tsx
// BEFORE (line 59-62):
<div className="result-meta">
  <span>พบ 8 ผลลัพธ์ที่เกี่ยวข้อง</span>
  <button type="button">เกี่ยวข้องมากที่สุด⌄</button>
</div>

// AFTER:
const [sortBy, setSortBy] = useState("relevant");

// ... in JSX:
<div className="result-meta">
  <span>พบ 8 ผลลัพธ์ที่เกี่ยวข้อง</span>
  <select
    value={sortBy}
    onChange={(e) => {
      setSortBy(e.target.value);
      recordEvent({ type: "search_submitted" as any });
    }}
    aria-label="เรียงลำดับผลลัพธ์"
  >
    <option value="relevant">เกี่ยวข้องมากที่สุด</option>
    <option value="newest">ใหม่ที่สุด</option>
    <option value="oldest">เก่าที่สุด</option>
  </select>
</div>
```

- **Verification:**
  1. ไปที่ `/search?q=เลิกจ้าง`
  2. คลิก dropdown → ต้องเห็น 3 ตัวเลือก
  3. เลือก "ใหม่ที่สุด" → dropdown ต้องเปลี่ยนค่า

---

### P1-4: Filter Tabs — เพิ่ม useState ใน 3 หน้า

- **ไฟล์:** `app/notifications/page.tsx` (line 17-22, 37-47) + `app/lawyers/page.tsx` (line 59-66, 101-107) — `app/cases/page.tsx` filters ทำงานแล้ว
- **ปัญหา:** Notification tabs และ Lawyer filter chips ไม่มี state — คลิกแล้วไม่กรอง

#### 4a. Notifications Filter

```tsx
// BEFORE (line 17-22):
const TABS: { label: string; count?: number; active?: boolean }[] = [
  { label: "ทั้งหมด", count: 3, active: true },
  { label: "เคสของฉัน" },
  { label: "เอกสาร" },
  { label: "ระบบ" },
];

// AFTER:
const TABS = [
  { label: "ทั้งหมด", key: "all" },
  { label: "เคสของฉัน", key: "cases" },
  { label: "เอกสาร", key: "documents" },
  { label: "ระบบ", key: "system" },
] as const;
```

```tsx
// BEFORE — server component, no client state:
export default function NotificationsPage() {

// AFTER — make it a client component:
"use client";
import { useState } from "react";

export default function NotificationsPage() {
  const [activeFilter, setActiveFilter] = useState("all");

  // Filter notifications (sample data)
  const filtered =
    activeFilter === "all"
      ? sampleNotifications
      : activeFilter === "cases"
      ? sampleNotifications.filter((n) => n.nextRoute?.includes("/cases"))
      : activeFilter === "documents"
      ? sampleNotifications.filter((n) => n.nextRoute?.includes("/documents"))
      : sampleNotifications.filter(
          (n) =>
            !n.nextRoute?.includes("/cases") &&
            !n.nextRoute?.includes("/documents")
        );
```

```tsx
// BEFORE (line 37-47):
<div className="notification-tabs">
  {TABS.map((t) => (
    <button key={t.label} className={t.active ? "active" : ""} type="button">
      {t.label} {typeof t.count === "number" ? <i>{t.count}</i> : null}
    </button>
  ))}
</div>

// AFTER:
<div className="notification-tabs">
  {TABS.map((t) => (
    <button
      key={t.key}
      className={activeFilter === t.key ? "active" : ""}
      type="button"
      onClick={() => setActiveFilter(t.key)}
    >
      {t.label}
    </button>
  ))}
</div>

{/* Replace sampleNotifications.map with filtered.map */}
<section className="notification-list">
  {filtered.map((n) => ( /* ... same as before ... */ ))}
</section>
```

#### 4b. Lawyers Filter

```tsx
// BEFORE (line 59-66):
const filterChips = [
  "ทั้งหมด",
  "กฎหมายแรงงาน",
  "ครอบครัว",
  "อสังหาริมทรัพย์",
  "ผู้บริโภค",
  "ออนไลน์วันนี้",
];

// AFTER — unchanged data, add state:
const filterChips = [ /* same as before */ ];

// Inside LawyersPage:
const [activeChip, setActiveChip] = useState(0);

// Filter logic:
const filteredLawyers =
  activeChip === 0
    ? lawyers
    : activeChip === 1
    ? lawyers.filter((l) => l.specialty.includes("แรงงาน"))
    : activeChip === 2
    ? lawyers.filter((l) => l.specialty.includes("ครอบครัว"))
    : activeChip === 3
    ? lawyers.filter((l) => l.specialty.includes("อสังหา"))
    : activeChip === 4
    ? lawyers.filter((l) => l.specialty.includes("ผู้บริโภค"))
    : lawyers; // "ออนไลน์วันนี้" — all for now
```

```tsx
// BEFORE (line 101-107):
<div className="filter-chips">
  {filterChips.map((chip, i) => (
    <button key={chip} className={i === 0 ? "active" : ""}>
      {chip}
    </button>
  ))}
</div>

// AFTER:
<div className="filter-chips">
  {filterChips.map((chip, i) => (
    <button
      key={chip}
      className={activeChip === i ? "active" : ""}
      onClick={() => setActiveChip(i)}
    >
      {chip}
    </button>
  ))}
</div>
```

- **Verification:**
  1. `/notifications` → คลิก "เคสของฉัน" → ต้องกรองเฉพาะ notifications ที่เกี่ยวกับเคส
  2. `/lawyers` → คลิก "ครอบครัว" → ต้องกรอง lawyers
  3. `/cases` → filters ทำงานอยู่แล้ว (ยืนยัน)

---

### P1-5: Share Button — เพิ่ม `navigator.share()`

- **ไฟล์:** `app/search/page.tsx` (line 102)
- **ปัญหา:** ปุ่ม "↗ แชร์" ไม่มี onClick
- **Code Fix:**

```tsx
// BEFORE (line 99-103):
<button type="button" onClick={() => setSaved(!saved)}>
  {saved ? "✓ บันทึกแล้ว" : "♡ บันทึก"}
</button>
<button type="button">↗ แชร์</button>

// AFTER:
<button type="button" onClick={() => setSaved(!saved)}>
  {saved ? "✓ บันทึกแล้ว" : "♡ บันทึก"}
</button>
<button
  type="button"
  onClick={() => {
    const shareData = {
      title: "LegalAI Thailand — ผลการค้นหากฎหมาย",
      text: `"${query}" — ดูคำแนะนำทางกฎหมายจาก LegalAI`,
      url: window.location.href,
    };
    if (navigator.share) {
      navigator.share(shareData).catch(() => {});
    } else {
      // Fallback: copy URL to clipboard
      navigator.clipboard.writeText(window.location.href).then(() => {
        // Could show toast if useToast is available
      }).catch(() => {});
    }
  }}
>
  ↗ แชร์
</button>
```

- **Verification:**
  1. ไปที่ `/search?q=เลิกจ้าง`
  2. คลิก "↗ แชร์" → ต้องเห็น native share dialog (mobile) หรือ copy URL (desktop)

---

### P1-6: Search Article/Topic Links — ทำให้คลิกได้

- **ไฟล์:** `app/search/page.tsx` (line 118-129 articles, line 143-147 topics)
- **ปัญหา:** ปุ่มบทความและหัวข้อเป็น `<button>` ที่ไม่มี navigation
- **Code Fix:**

```tsx
// BEFORE (line 117-129):
<h3 className="subhead">บทความที่เกี่ยวข้อง</h3>
{articles.map((x, i) => (
  <button className="article-row" key={x} type="button">
    <span aria-hidden><DocIcon size={18} /></span>
    <div>
      <strong>{x}</strong>
      <small>อ่าน {4 + i} นาที • ตรวจสอบโดยทนาย</small>
    </div>
    <i aria-hidden>›</i>
  </button>
))}

// AFTER:
<h3 className="subhead">บทความที่เกี่ยวข้อง</h3>
{articles.map((x, i) => (
  <Link
    className="article-row"
    key={x}
    href={`/search?q=${encodeURIComponent(x)}`}
  >
    <span aria-hidden><DocIcon size={18} /></span>
    <div>
      <strong>{x}</strong>
      <small>อ่าน {4 + i} นาที • ตรวจสอบโดยทนาย</small>
    </div>
    <i aria-hidden>›</i>
  </Link>
))}
```

```tsx
// BEFORE (line 141-148):
<div className="aside-card">
  <h3>หัวข้อที่เกี่ยวข้อง</h3>
  {["ค่าชดเชยเลิกจ้าง", "ค่าจ้างแทนการบอกกล่าว", "แจ้งกรมสวัสดิการฯ", "ศาลแรงงาน"].map((x) => (
    <button key={x} type="button">
      #{x}
    </button>
  ))}
</div>

// AFTER:
<div className="aside-card">
  <h3>หัวข้อที่เกี่ยวข้อง</h3>
  {["ค่าชดเชยเลิกจ้าง", "ค่าจ้างแทนการบอกกล่าว", "แจ้งกรมสวัสดิการฯ", "ศาลแรงงาน"].map((x) => (
    <Link key={x} href={`/search?q=${encodeURIComponent(x)}`}>
      #{x}
    </Link>
  ))}
</div>
```

- **Verification:**
  1. ไปที่ `/search?q=เลิกจ้าง`
  2. คลิกบทความ "ลูกจ้างมีสิทธิอะไรบ้างเมื่อถูกเลิกจ้าง" → ต้อง search คำนั้น
  3. คลิกหัวข้อ "#ค่าชดเชยเลิกจ้าง" → ต้อง search คำนั้น

---

### P1-7: Disclaimers — เพิ่มใน 3 หน้าที่ขาด

- **ไฟล์:** 3 หน้า — `app/search/page.tsx`, `app/diagnosis/page.tsx`, `app/profile/page.tsx`
- **ปัญหา:** หน้าสำคัญไม่มีข้อความปฏิเสธความรับผิด (legal disclaimer) ตามข้อกำหนด AI Safety
- **Code Fix:**

**7a. Search page** — เพิ่มที่ด้านล่างก่อน closing tag:

```tsx
// Add import:
import { LegalDisclaimer } from "@/components/ui/primitives";

// Add before closing </> at line 151:
<LegalDisclaimer>
  ⓘ ข้อมูลการค้นหาเป็นคำแนะนำเบื้องต้นจาก AI ไม่ใช่คำปรึกษาทางกฎหมาย
  โปรดตรวจสอบข้อมูลสำคัญกับทนายความหรือผู้เชี่ยวชาญก่อนดำเนินการ
</LegalDisclaimer>
```

**7b. Diagnosis page** — privacy note มีอยู่แล้วที่ line 323-326 แต่ยังไม่ใช่ disclaimer แบบเต็ม:

```tsx
// Add import (already may be available):
import { LegalDisclaimer } from "@/components/ui/primitives";

// REPLACE line 323-325:
// BEFORE:
<p className="privacy-note">
  ⌾ คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น คุณลบหรือแก้ไขได้เสมอ
</p>

// AFTER:
<LegalDisclaimer>
  ⓘ การวิเคราะห์นี้ใช้ AI เป็นผู้ช่วยเบื้องต้นเท่านั้น ไม่ใช่การรับรองผลทางกฎหมาย
  ข้อมูลที่ได้ควรปรึกษาทนายความก่อนนำไปใช้จริง • คำตอบใช้เพื่อจัดทำแผนของเคสนี้เท่านั้น
  คุณลบหรือแก้ไขได้เสมอ
</LegalDisclaimer>
```

**7c. Profile page** — เพิ่มที่ด้านล่าง privacy tab หรือ footer:

```tsx
// Add import:
import { LegalDisclaimer } from "@/components/ui/primitives";

// Add after closing </div> of settings-layout, before closing </>:
<LegalDisclaimer>
  ⓘ ข้อมูลส่วนตัวของคุณได้รับการปกป้องตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562
  ดูรายละเอียดเพิ่มเติมที่ <Link href="/privacy">นโยบายความเป็นส่วนตัว</Link>
</LegalDisclaimer>
```

- **Verification:**
  1. `/search` → ต้องเห็น disclaimer ที่ด้านล่าง
  2. `/diagnosis` → ต้องเห็น disclaimer แทน privacy-note เดิม
  3. `/profile` (privacy tab) → ต้องเห็น disclaimer

---

## 🟢 P2 — Low (ต่ำ)

### P2-1: Mark All Read — เพิ่ม toast

- **ไฟล์:** `app/notifications/page.tsx` (line 30-33)
- **ปัญหา:** ปุ่ม "✓ อ่านทั้งหมดแล้ว" ไม่มี onClick
- **Code Fix:**

```tsx
// First, convert to client component:
"use client";
import { useState } from "react";
import { useToast } from "@/components/layout/app-providers";

// Inside the component:
export default function NotificationsPage() {
  const notify = useToast();
  // ...existing code...

  // BEFORE (line 30-33):
  action={
    <button className="ghost" type="button">
      ✓ อ่านทั้งหมดแล้ว
    </button>
  }

  // AFTER:
  action={
    <button
      className="ghost"
      type="button"
      onClick={() => {
        // In production: call API to mark all as read
        notify("ทำเครื่องหมายว่าอ่านทั้งหมดแล้ว");
        recordEvent({ type: "search_submitted" as any });
      }}
    >
      ✓ อ่านทั้งหมดแล้ว
    </button>
  }
```

- **Verification:**
  1. ไปที่ `/notifications`
  2. คลิก "✓ อ่านทั้งหมดแล้ว" → ต้องเห็น toast "ทำเครื่องหมายว่าอ่านทั้งหมดแล้ว"

---

### P2-2: Save Lawyer — เพิ่ม toast

- **ไฟล์:** `app/lawyers/page.tsx` (line 139)
- **ปัญหา:** ปุ่ม "♡ บันทึก" สำหรับแต่ละทนายไม่มี onClick
- **Code Fix:**

```tsx
// BEFORE (line 139):
<button>♡ บันทึก</button>

// AFTER:
const [savedLawyers, setSavedLawyers] = useState<Record<string, boolean>>({});

// In the map:
<button
  onClick={() => {
    const isSaved = savedLawyers[x.name];
    setSavedLawyers((prev) => ({ ...prev, [x.name]: !isSaved }));
    notify(isSaved ? `ยกเลิกบันทึก ${x.name}` : `บันทึก ${x.name} แล้ว`);
    recordEvent({ type: "consultation_requested" as any, lawyerId: x.name });
  }}
>
  {savedLawyers[x.name] ? "✓ บันทึกแล้ว" : "♡ บันทึก"}
</button>
```

- **Verification:**
  1. ไปที่ `/lawyers`
  2. คลิก "♡ บันทึก" ของทนายคนแรก → ต้องเปลี่ยนเป็น "✓ บันทึกแล้ว" + toast
  3. คลิกซ้ำ → ต้องเปลี่ยนกลับเป็น "♡ บันทึก"

---

### P2-3: Assistant Menu — เพิ่ม onClick handlers

- **ไฟล์:** `app/assistant/page.tsx` (line 156, 167)
- **ปัญหา:** ปุ่ม "•••" (more options) และ "เปลี่ยน" (switch case) ไม่มี handler
- **Code Fix:**

```tsx
// Add import:
import { useToast } from "@/components/layout/app-providers";

// Inside AssistantPage:
const notify = useToast();

// BEFORE (line 156):
<button aria-label="ตัวเลือกเพิ่มเติม">•••</button>

// AFTER:
<button
  aria-label="ตัวเลือกเพิ่มเติม"
  onClick={() => {
    // Show options: clear chat, export, etc.
    if (window.confirm("ล้างประวัติแชททั้งหมด?")) {
      setMessages([WELCOME]);
      notify("ล้างประวัติแชทแล้ว");
    }
  }}
>
  •••
</button>
```

```tsx
// BEFORE (line 167):
<button>เปลี่ยน</button>

// AFTER:
<button
  onClick={() => {
    notify("กรุณาเลือกเคสที่ต้องการ — ฟีเจอร์กำลังพัฒนา");
    // Future: open case selector dialog
  }}
>
  เปลี่ยน
</button>
```

- **Verification:**
  1. ไปที่ `/assistant`
  2. คลิก "•••" → ต้องมี confirm dialog ล้างแชท → toast
  3. คลิก "เปลี่ยน" → ต้องเห็น toast

---

### P2-4: Pricing Page — สร้างหน้า `/pricing`

- **ไฟล์ใหม่:** `app/pricing/page.tsx`
- **ปัญหา:** ไม่มีหน้าแสดงแพ็กเกจราคา
- **Code Fix:**

```tsx
"use client";

import type { Metadata } from "next";
import { PageHead, Pill, LegalDisclaimer } from "@/components/ui/primitives";
import { useToast } from "@/components/layout/app-providers";
import Link from "next/link";

const plans = [
  {
    name: "พื้นฐาน",
    price: "ฟรี",
    period: "ตลอดชีพ",
    features: [
      "วิเคราะห์เคส 3 ครั้ง/เดือน",
      "สร้างเอกสาร 1 ฉบับ/เดือน",
      "ค้นหาข้อมูลกฎหมาย",
      "การแจ้งเตือนพื้นฐาน",
    ],
    cta: "แพ็กเกจปัจจุบัน",
    active: true,
  },
  {
    name: "โปร",
    price: "฿299",
    period: "/เดือน",
    features: [
      "วิเคราะห์เคสไม่จำกัด",
      "สร้างเอกสารไม่จำกัด",
      "ปรึกษาทนายออนไลน์ 2 ครั้ง/เดือน",
      "ส่งออกเอกสาร PDF/Word",
      "LINE แจ้งเตือน",
      "สนับสนุนลำดับความสำคัญ",
    ],
    cta: "อัปเกรด",
    active: false,
    highlight: true,
  },
  {
    name: "องค์กร",
    price: "฿999",
    period: "/เดือน",
    features: [
      "ทุกฟีเจอร์ในแพ็กเกจโปร",
      "ผู้ใช้สูงสุด 10 คน",
      "ปรึกษาทนายไม่จำกัด",
      "Dashboard สำหรับองค์กร",
      "รายงานรายเดือน",
      "API access",
      "ผู้จัดการบัญชีส่วนตัว",
    ],
    cta: "ติดต่อเรา",
    active: false,
  },
];

export default function PricingPage() {
  const notify = useToast();

  return (
    <>
      <PageHead
        backHref="/profile"
        title="แพ็กเกจและราคา"
        subtitle="เลือกแพ็กเกจที่เหมาะกับคุณ — เริ่มต้นฟรี ไม่มีค่าใช้จ่ายแอบแฝง"
      />

      <div className="pricing-grid">
        {plans.map((plan) => (
          <div
            key={plan.name}
            className={`pricing-card${plan.highlight ? " highlight" : ""}${plan.active ? " active" : ""}`}
          >
            {plan.highlight && <Pill tone="blue">ยอดนิยม</Pill>}
            <h2>{plan.name}</h2>
            <div className="price">
              <strong>{plan.price}</strong>
              <small>{plan.period}</small>
            </div>
            <ul>
              {plan.features.map((f) => (
                <li key={f}>✓ {f}</li>
              ))}
            </ul>
            <button
              className={plan.active ? "ghost" : "primary full"}
              disabled={plan.active}
              onClick={() => {
                if (plan.name === "องค์กร") {
                  notify("กำลังส่งคำขอ — ทีมงานจะติดต่อกลับภายใน 24 ชม.");
                } else if (!plan.active) {
                  notify(`เริ่มอัปเกรดเป็นแพ็กเกจ ${plan.name}`);
                }
              }}
            >
              {plan.cta}
            </button>
          </div>
        ))}
      </div>

      <LegalDisclaimer>
        ⓘ ราคาอาจมีการเปลี่ยนแปลง • อ่านรายละเอียดเพิ่มเติมที่{" "}
        <Link href="/terms">ข้อกำหนดการใช้บริการ</Link>
      </LegalDisclaimer>
    </>
  );
}
```

**CSS additions needed** (add to `app/globals.css`):

```css
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 24px;
}
.pricing-card {
  background: var(--card-bg, #fff);
  border: 1px solid var(--border, #e5e7eb);
  border-radius: 16px;
  padding: 28px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
}
.pricing-card.highlight {
  border-color: var(--accent, #3b82f6);
  box-shadow: 0 0 0 2px var(--accent, #3b82f6);
}
.pricing-card .price strong {
  font-size: 32px;
  font-weight: 700;
}
.pricing-card .price small {
  color: var(--muted, #6b7280);
  margin-left: 4px;
}
.pricing-card ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.pricing-card ul li {
  font-size: 14px;
  color: var(--text, #1f2937);
}
.legal-page {
  max-width: 720px;
  margin: 0 auto;
  padding: 24px 0;
}
.legal-page section {
  margin-bottom: 28px;
}
.legal-page h2 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
}
.legal-page p, .legal-page li {
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-secondary, #4b5563);
}
.legal-page ul {
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.legal-updated {
  font-size: 13px;
  color: var(--muted, #9ca3af);
  margin-top: 32px;
}
.toggle {
  padding: 6px 16px;
  border-radius: 20px;
  border: 1px solid var(--border);
  background: var(--bg-secondary);
  cursor: pointer;
  font-size: 13px;
}
.toggle.on {
  background: var(--accent, #3b82f6);
  color: #fff;
  border-color: var(--accent, #3b82f6);
}
```

- **Verification:**
  1. เปิด `/pricing` ใน browser
  2. ต้องเห็น 3 แพ็กเกจ: พื้นฐาน / โปร / องค์กร
  3. แพ็กเกจ "โปร" มีขอบ highlight สีน้ำเงิน
  4. ปุ่มของแพ็กเกจปัจจุบันเป็น disabled
  5. คลิกปุ่มอัปเกรด → ต้องเห็น toast

---

# SECTION 2: Execution Order (ลำดับการแก้ไข)

## Step-by-Step Fix Sequence

```
ลำดับที่ 1: P0-1  Case Tabs href="#" → real routes         (app/cases/[caseId]/timeline/page.tsx)
ลำดับที่ 2: P0-2  Create /terms page                        (app/terms/page.tsx)
ลำดับที่ 3: P0-3  Create /privacy page                      (app/privacy/page.tsx)
ลำดับที่ 4: P1-1  Settings tabs → useState                  (app/profile/page.tsx)
ลำดับที่ 5: P1-2  AI consent → toggle + delete + export      (app/profile/page.tsx — same file as P1-1)
ลำดับที่ 6: P1-7  Disclaimers → 3 pages                     (app/search/page.tsx, app/diagnosis/page.tsx, app/profile/page.tsx)
ลำดับที่ 7: P1-3  Sort dropdown → select menu               (app/search/page.tsx)
ลำดับที่ 8: P1-6  Search article/topic → clickable           (app/search/page.tsx — same file as P1-3)
ลำดับที่ 9: P1-5  Share button → navigator.share            (app/search/page.tsx — same file as above)
ลำดับที่ 10: P1-4  Filter tabs → 3 pages                    (app/notifications/page.tsx, app/lawyers/page.tsx)
ลำดับที่ 11: P2-1  Mark all read → toast                    (app/notifications/page.tsx — same file as P1-4a)
ลำดับที่ 12: P2-2  Save lawyer → toast                      (app/lawyers/page.tsx — same file as P1-4b)
ลำดับที่ 13: P2-3  Assistant menu → handlers                (app/assistant/page.tsx)
ลำดับที่ 14: P2-4  Create /pricing page                     (app/pricing/page.tsx)
```

## Dependencies

| Fix | ต้องทำก่อน | เหตุผล |
|-----|-----------|--------|
| P1-2 (AI consent) | P1-1 (Settings tabs) | P1-2 เพิ่มใน privacy tab ที่สร้างใน P1-1 |
| P1-7c (Profile disclaimer) | P1-1 | เพิ่มใน profile page ที่แก้ไขแล้ว |
| P1-5, P1-6, P1-3 (Search) | — | แก้ไฟล์เดียวกัน — ทำพร้อมกันได้ |
| P2-1 (Mark read) | P1-4a (Notifications filter) | ไฟล์เดียวกัน |
| P2-2 (Save lawyer) | P1-4b (Lawyers filter) | ไฟล์เดียวกัน |
| P0-2, P0-3 (Terms/Privacy) | — | ไฟล์ใหม่ — ทำได้ทุกเมื่อ |

## Batch Groups (แก้พร้อมกันได้)

**Batch A** (ไฟล์ใหม่ — ไม่ depend กัน):
- P0-2: `/terms`
- P0-3: `/privacy`
- P2-4: `/pricing`

**Batch B** (timeline):
- P0-1: Case tabs fix

**Batch C** (profile — ไฟล์เดียว 3 fixes):
- P1-1: Settings tabs
- P1-2: AI consent
- P1-7c: Profile disclaimer

**Batch D** (search — ไฟล์เดียว 4 fixes):
- P1-3: Sort dropdown
- P1-5: Share button
- P1-6: Article/topic links
- P1-7a: Search disclaimer

**Batch E** (diagnosis):
- P1-7b: Diagnosis disclaimer

**Batch F** (notifications — ไฟล์เดียว 2 fixes):
- P1-4a: Filter tabs
- P2-1: Mark all read

**Batch G** (lawyers — ไฟล์เดียว 2 fixes):
- P1-4b: Filter tabs
- P2-2: Save lawyer

**Batch H** (assistant):
- P2-3: Menu handlers

**Execution flow:** A → B → C → D → E → F → G → H

---

# SECTION 3: Verification Checklist (ตรวจสอบทีละขั้น)

## After Each Fix

```
✅ P0-1: /cases/case-1/timeline → คลิกแท็บ "หลักฐาน" ไป /cases/case-1/evidence
✅ P0-2: /terms → แสดงข้อกำหนด 7 sections
✅ P0-3: /privacy → แสดงนโยบาย 8 sections + PDPA
✅ P1-1: /profile → คลิกแท็บ settings แต่ละอัน เปลี่ยนเนื้อหา
✅ P1-2: /profile → privacy tab → toggle AI + export + delete
✅ P1-3: /search → dropdown เรียงลำดับเปลี่ยนค่าได้
✅ P1-4: /notifications → filter tabs กรองข้อมูลได้
✅ P1-4: /lawyers → filter chips กรองทนายได้
✅ P1-5: /search → ปุ่มแชร์ เรียก native share
✅ P1-6: /search → คลิกบทความ/hashtag ไป search
✅ P1-7: /search, /diagnosis, /profile → มี disclaimer
✅ P2-1: /notifications → mark all read → toast
✅ P2-2: /lawyers → save lawyer → toggle + toast
✅ P2-3: /assistant → ••• (clear) + เปลี่ยน (toast)
✅ P2-4: /pricing → แสดง 3 แพ็กเกจ
```

## Browser Size Verification

| Route | 375×812 (iPhone) | 320×700 (small) | 1440×900 (desktop) |
|-------|------------------|-----------------|---------------------|
| `/cases/case-1/timeline` | Tabs เลื่อนได้ / ซ้อน wrap | Tab เล็กสุดยังกดได้ | Tabs เรียงปกติ |
| `/terms` | อ่าน scroll ได้ปกติ | ตัวหนังสือไม่ล้น | แสดงเต็มจอ |
| `/privacy` | อ่าน scroll ได้ปกติ | ตัวหนังสือไม่ล้น | แสดงเต็มจอ |
| `/profile` | Settings tabs scroll แนวนอน | Settings tabs ซ้อน wrap | Sidebar + content |
| `/search` | Results + aside stack | Dropdown ไม่ล้น | Layout 2 columns |
| `/notifications` | Tabs scroll ได้ | Tabs ซ้อน wrap | Tabs เรียงปกติ |
| `/lawyers` | Cards stack แนวตั้ง | Filter chips wrap | Cards + aside |
| `/assistant` | Chat fills viewport | Input area ไม่ล้น | Chat มี max-width |
| `/pricing` | Cards stack แนวตั้ง | Cards ซ้อน | 3 columns |

## URL Routes to Verify

| Route | Expected | Status |
|-------|----------|--------|
| `/` | Home page with search + categories | ✅ existing |
| `/cases` | Cases list with filters | ✅ existing |
| `/cases/case-1/timeline` | Timeline with working tabs | 🔧 P0-1 fix |
| `/cases/case-1/evidence` | Evidence tracker | ✅ existing |
| `/search?q=เลิกจ้าง` | Results + share + links | 🔧 P1-3,5,6,7 fixes |
| `/diagnosis` | Diagnosis wizard + disclaimer | 🔧 P1-7b fix |
| `/documents` | Document generator | ✅ existing |
| `/lawyers` | Lawyer marketplace | 🔧 P1-4b, P2-2 fixes |
| `/notifications` | Notifications + filters | 🔧 P1-4a, P2-1 fixes |
| `/assistant` | AI chat | 🔧 P2-3 fix |
| `/profile` | Settings + privacy | 🔧 P1-1,2,7c fixes |
| `/terms` | Terms of Service | 🆕 P0-2 |
| `/privacy` | Privacy Policy (PDPA) | 🆕 P0-3 |
| `/pricing` | Pricing plans | 🆕 P2-4 |
| `/analysis/case-1` | Analysis results | ✅ existing |
| `/auth/signin` | Sign in page | ✅ existing |

## Expected Behavior Summary

1. **Navigation:** ทุกปุ่ม/ลิงก์ต้องพาไปที่ URL จริง — ไม่มี `#` หรือ no-op click
2. **Tabs & Filters:** ทุก tab/chip ต้องมี active state และกรอง/เปลี่ยนเนื้อหาได้
3. **Legal Compliance:** `/terms` และ `/privacy` ต้องมีเนื้อหาครบถ้วน — PDPA พร้อม
4. **Consent:** ผู้ใช้ต้อง toggle AI consent, ขอ export, ขอลบข้อมูลได้
5. **Share:** ปุ่มแชร์ใช้ Web Share API บน mobile, clipboard fallback บน desktop
6. **Disclaimers:** ทุกหน้าที่มี AI-generated content ต้องมี disclaimer
7. **Feedback:** ทุก interaction (mark read, save lawyer, upgrade plan) ต้องมี toast

---

## 📝 สรุปจำนวนไฟล์ที่ต้องแก้ไข/สร้าง

| การดำเนินการ | จำนวน |
|-------------|-------|
| ไฟล์ที่ต้องสร้างใหม่ | 3 (`terms`, `privacy`, `pricing`) |
| ไฟล์ที่ต้องแก้ไข | 7 (`timeline`, `profile`, `search`, `notifications`, `lawyers`, `assistant`, `diagnosis`) |
| CSS ที่ต้องเพิ่ม | 1 (`globals.css` — pricing + legal + toggle styles) |
| **รวม** | **11 ไฟล์** |

---

*End of Bug Fix Plan — พร้อมเริ่มแก้ไข*
