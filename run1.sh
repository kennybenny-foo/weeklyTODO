#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$HOME/weeklyTODO"
APP_FILE="weeklyTODO.py"
VENV="$APP_DIR/.venv"
PY="$VENV/bin/python"
LOG="$APP_DIR/log.txt"

cd "$APP_DIR"

echo "==> Syncing code to origin/main..."
git fetch origin
git reset --hard origin/main
git clean -fd   # IMPORTANT: removes leftover untracked files

echo "DEPLOYED COMMIT:"
git log -1 --oneline

echo "==> Ensuring venv exists..."
if [ ! -d "$VENV" ]; then
  python3.12 -m venv "$VENV"
fi

echo "==> Installing deps..."
"$PY" -m pip install -U pip
if [ -f requirements.txt ]; then
  "$PY" -m pip install -r requirements.txt
fi

echo "==> Stopping old server (by port and by script name)..."
# Kill whatever is holding port 5050 (most reliable)
if command -v lsof >/dev/null 2>&1; then
  sudo lsof -t -i:5050 | xargs -r sudo kill -9
else
  pkill -f "weeklyTODO.py" || true
fi

echo "==> Starting new server..."
nohup "$PY" "$APP_FILE" > "$LOG" 2>&1 & disown || true

sleep 1
echo "==> Running processes:"
pgrep -af "weeklyTODO.py" || true

echo "==> Last 40 log lines:"
tail -n 40 "$LOG" || true

echo "==> Done. Tail logs with: tail -n 200 -f $LOG"