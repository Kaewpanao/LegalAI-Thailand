import subprocess, json, os

GAPI = r'python "C:\Users\nutsdevs\AppData\Local\hermes\profiles\bess\skills\productivity\google-workspace\scripts\google_api.py"'
DOC_ID = "1GPQbKIO6QADsG6AG3iExYRjh2fPojBSLU5qWr_x08Ss"

with open(r"D:\hermes-bess-project\docs\legalai_revenue_forecast.md", "r", encoding="utf-8") as f:
    content = f.read()

chunks = []
for i in range(0, len(content), 2000):
    chunks.append(content[i:i+2000])

success = 0
for idx, chunk in enumerate(chunks):
    safe = json.dumps(chunk)
    cmd = f'{GAPI} docs append {DOC_ID} --text {safe}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        success += 1
        print(f"Chunk {idx+1}/{len(chunks)} OK")
    else:
        print(f"Chunk {idx+1}/{len(chunks)} FAIL: {result.stderr[:80]}")
        break

print(f"\nDone: {success}/{len(chunks)}")
print(f"https://docs.google.com/document/d/{DOC_ID}/edit")
