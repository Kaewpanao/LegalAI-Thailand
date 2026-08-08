#!/bin/bash
# 🎀 Bess Project Restore Script
# ใช้ตอน Hermes พัง → ลงใหม่ → restore ทุกอย่าง

PROJECT_DIR="/d/hermes-bess-project"
HERMES_HOME="$HOME/.hermes"
PROFILE="bess"

echo "🎀 Bess Project Restore"
echo "======================"
echo ""

# Check project folder
if [ ! -f "$PROJECT_DIR/AGENTS.md" ]; then
    echo "❌ ไม่เจอ Project Folder ที่ $PROJECT_DIR"
    echo "   ต้องมี AGENTS.md ก่อน!"
    exit 1
fi

echo "✅ Project Folder: $PROJECT_DIR"

# Check/create Hermes profile
if [ ! -d "$HERMES_HOME/profiles/$PROFILE" ]; then
    echo "📝 กำลังสร้าง profile '$PROFILE'..."
    hermes profile create "$PROFILE"
fi
echo "✅ Profile: $PROFILE"

# Restore skills from project
if [ -d "$PROJECT_DIR/skills" ] && [ "$(ls -A "$PROJECT_DIR/skills" 2>/dev/null)" ]; then
    echo "📚 กำลัง restore skills..."
    for skill in "$PROJECT_DIR/skills"/*/; do
        skill_name=$(basename "$skill")
        target="$HERMES_HOME/skills/$skill_name"
        if [ ! -d "$target" ]; then
            cp -r "$skill" "$target"
            echo "   ✅ $skill_name"
        else
            echo "   ⏭️ $skill_name (มีอยู่แล้ว)"
        fi
    done
fi

echo ""
echo "🎉 Restore เสร็จ! เปิด Hermes ใน project folder ได้เลย:"
echo ""
echo "   cd $PROJECT_DIR"
echo "   hermes"
echo ""
echo "💖 เบสกลับมาแล้ว!"
