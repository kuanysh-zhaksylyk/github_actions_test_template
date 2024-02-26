#!/usr/bin/env bash
set -eo pipefail

APP_ROOT_PATH=$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd .. && pwd)

export APP_ROOT_PATH="${APP_ROOT_PATH}"
export PLATFORM_REPO="https://github.com/ostis-ai/ostis-web-platform.git"
export PLATFORM_BRANCH="0.9.0-Unlock"
export PLATFORM_COMMIT="0.9.0-Unlock"
export PLATFORM_PATH="${APP_ROOT_PATH}/ostis-web-platform"
export SC_MACHINE_BRANCH="prerelease/0.10.0"
export SC_MACHINE_COMMIT="60ef946ffd633cb245a4ba2a0849aa16eb4a1156"
export SC_WEB_BRANCH="0.8.1-Unlock"
export SC_WEB_COMMIT="8ee7340f86e017d4af770d8a43ba28d144d663a6"
export ROOT_CMAKE_PATH="${APP_ROOT_PATH}"
export PROBLEM_SOLVER_PATH="${APP_ROOT_PATH}/problem-solver"
export INTERFACE_PATH="${APP_ROOT_PATH}/interface/health-care-ui"
export REPO_PATH_FILE="${APP_ROOT_PATH}/repo.path"
export SCRIPTS_PATH="${APP_ROOT_PATH}/scripts"
export KB_PATH="${APP_ROOT_PATH}/kb"
export EXTENSION_KB_REPO="git@github.com:SemSystemsInternal/health-care-kb-extension.git"
export CONFIG_PATH="${APP_ROOT_PATH}/health-care.ini"

if [ -d "${PLATFORM_PATH}" ];
then
  source "${PLATFORM_PATH}/scripts/set_vars.sh"
fi
