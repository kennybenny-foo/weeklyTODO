#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_FILE="weeklyTODO.py"
LOG_FILE="log.txt"

cd "$APP_DIR"

echo "==> Updating code..."
git fetch --all
git pull --rebase

echo "==> Installing deps if requirements.txt exists..."
if [ -f requirements.txt ]; then
  python3 -m pip install --user -r requirements.txt
fi

echo "==> Stopping old process (if running)..."
pkill -f "python3 .*${APP_FILE}" || true

echo "==> Starting app..."
nohup python3 "$APP_FILE" > "$LOG_FILE" 2>&1 &

echo "==> Verifying app started..."
sleep 1
pgrep -af "python3 .*${APP_FILE}" || (echo "App failed to start. Last 50 log lines:" && tail -n 50 "$LOG_FILE" && exit 1)

echo "==> Done. Last 20 log lines:"
tail -n 20 "$LOG_FILE" || true