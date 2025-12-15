#!/usr/bin/env bash
# Simple local server launcher for testing PWA/SW
PORT=${1:-8080}
PUBLIC_DIR="$(cd "$(dirname "$0")/../public" && pwd)"

echo "Serving $PUBLIC_DIR on http://localhost:${PORT}/"

if command -v python3 >/dev/null 2>&1; then
  python3 -m http.server "$PORT" --directory "$PUBLIC_DIR"
elif command -v python >/dev/null 2>&1; then
  python -m http.server "$PORT" --directory "$PUBLIC_DIR"
elif command -v npx >/dev/null 2>&1; then
  npx serve "$PUBLIC_DIR" -l "$PORT"
else
  echo "Install Python 3 or npm (serve) to run the local server." >&2
  exit 1
fi
