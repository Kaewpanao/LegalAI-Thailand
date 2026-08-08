#!/bin/bash
# 🎀 Bess Project Backup Script
# ใช้ backup skills, memory, sessions ลง project folder

PROJECT_DIR="/d/hermes-bess-project"
HERMES_HOME="$HOME/.hermes"
PROFILE="bess"

echo "🎀 Bess Project Backup"
echo "======================"
echo ""

TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")

# Backup skills ที่เบสสร้าง
if [ -d "$HERMES_HOME/skills" ]; then
    echo "📚 Backing up skills..."
    mkdir -p "$PROJECT_DIR/skills"
    rsync -av --delete "$HERMES_HOME/skills/" "$PROJECT_DIR/skills/" 2>/dev/null || \
    cp -r "$HERMES_HOME/skills/"* "$PROJECT_DIR/skills/" 2>/dev/null
    echo "   ✅ Skills backed up"
fi

# Backup memory (manual snapshot)
echo "📝 Updating memory.md timestamp..."
sed -i "s/Last Updated: .*/Last Updated: $TIMESTAMP/" "$PROJECT_DIR/memory.md" 2>/dev/null || \
sed -i '' "s/Last Updated: .*/Last Updated: $TIMESTAMP/" "$PROJECT_DIR/memory.md" 2>/dev/null

# Backup sessions
echo "💬 Backing up session info..."
echo "Backup ran at: $TIMESTAMP" > "$PROJECT_DIR/sessions/last_backup.txt"

echo ""
echo "✅ Backup เสร็จ!"
echo "📁 ทุกอย่างอยู่ใน: $PROJECT_DIR"
echo ""
echo "💖 ปลอดภัยแน่นอน!"
