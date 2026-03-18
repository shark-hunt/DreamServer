#!/bin/bash
# Shared installer helpers for platform dispatch.

set -euo pipefail

detect_platform() {
    if [[ -f /proc/version ]] && grep -qi microsoft /proc/version 2>/dev/null; then
        echo "wsl"
    elif [[ "${OSTYPE:-}" == "msys"* || "${OSTYPE:-}" == "cygwin"* || "${OSTYPE:-}" == "win32"* ]]; then
        echo "windows"
    elif [[ "${OSTYPE:-}" == "darwin"* ]]; then
        echo "macos"
    elif [[ "${OSTYPE:-}" == "linux-gnu"* ]]; then
        echo "linux"
    else
        echo "unknown"
    fi
}
