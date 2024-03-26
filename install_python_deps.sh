#!/usr/bin/env bash
set -eo pipefail

source "$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)/set_vars.sh"

python3 -m venv "$APP_ROOT_PATH"/venv
source "$APP_ROOT_PATH"/venv/bin/activate
pip install -r requirements.txt

python3 connector.py

