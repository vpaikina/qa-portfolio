#!/bin/bash

# ==============================
# Universal Allure launcher script with Trend support
# - Loads .env if present
# - Prepares environment.properties for Allure
# - Preserves trend/history for Allure
# - Cleans old results (except trend)
# - Runs pytest
# - Copies categories.json if present
# - Generates and opens Allure report with history
# ==============================

# Load .env if present (local usage)
if [ -f ".env" ]; then
  set -a
  source .env
  set +a
fi

RESULTS_DIR="reports/allure-results"
REPORT_DIR="reports/allure-report"

# Preserve previous Allure trend/history (if exists)
if [ -d "${REPORT_DIR}/history" ]; then
  echo "Copying Allure history for trend analytics..."
  mkdir -p "${RESULTS_DIR}"
  cp -r "${REPORT_DIR}/history" "${RESULTS_DIR}/"
fi

# Clean old Allure results, but keep history folder if exists
find "${RESULTS_DIR}" -type f ! -path "${RESULTS_DIR}/history/*" -delete 2>/dev/null || true

# Ensure results directory exists
mkdir -p "${RESULTS_DIR}"

#Copy categories.json for custom error categorization (optional)
if [ -f "config/categories.json" ]; then
  cp config/categories.json "${RESULTS_DIR}/categories.json"
fi

# Run pytest and output Allure results
pytest "$@" --alluredir=${RESULTS_DIR}

# Prepare Allure environment.properties (metadata for report)
{
  echo "ENVIRONMENT=${ENVIRONMENT:-local}"
  echo "BASE_URL=${BASE_URL:-http://localhost:3000}"
  # echo "EXTERNAL_API_URL=${EXTERNAL_API_URL:-https://fakerestapi.azurewebsites.net/api/v1}"
  echo "USER=$(whoami)"
  echo "PYTHON_VERSION=$(python --version 2>&1)"
} > "${RESULTS_DIR}/environment.properties"

# Generate Allure HTML report with trend/history
allure generate "${RESULTS_DIR}" --clean -o "${REPORT_DIR}"

# Automatically open Allure report in browser
allure open "${REPORT_DIR}"

# Optionally: For one-time Allure report in temp dir (no history), comment/uncomment below
# allure serve "${RESULTS_DIR}"
