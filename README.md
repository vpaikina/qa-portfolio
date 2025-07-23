# 📚 Book Library API Tests
> Portfolio project with REST API Automated tests for a fictional Book Library service.
The project demonstrates QA automation proficiency in using best practices of automated API tests development using Python, Pytest, Requests, Allure, GitHub Actions CI and data-driven tests which cover real-world contract API and e2e scenarios.

✅ Realistic CRUD test suite for a local JSON-based REST API.

- 🔍 Fully automated API tests using **Python**, **Pytest**, **Pydantic**, **Faker**, and **Allure**
- 📦 Includes **data generation**, **contract validation**, **e2e scenarios**, and **resource cleanup**
- ⚙️ Configured with **GitHub Actions CI** and beautiful Allure HTML reports
- 📘 Follows **best practices** and uses a clean, modular folder structure


## 🚀 Key Features

- **Full CRUD E2E API coverage** (create, read, update, delete books)
- **Contract validation** with Pydantic schemas
- **Parameterized tests** for validating multiple payload variations with minimal code duplication 
- **Advanced test data management** (tracked resource creation and cleanup)


## 📁 Project Structure

- [**data/**](./data) — payload generators  
- [**steps/**](./steps) — contains readable, reusable step functions (DSL) for CRUD and validation operations, used in tests to improve clarity and maintainability.
- [**utils/**](./utils) — API client, custom assertion helpers, resource tracker, cleanup scripts and endpoints 
- [**schemas/**](./schemas) — Pydantic models for response validation  
- [**tests/**](./tests) — all test cases divided by suites  
- [**config/**](./config) — environment settings and other configs 
- [**run_tests_with_cleanup.sh**](./run_tests_with_cleanup.sh) — universal launcher script
- [**docs/**](./docs) — Allure report included for demonstration purposes only

## 🗂️ Test Suites
**The project includes four tests that automate the following scenarios:**
  - `test_book_response_contract` – Verifies API response contract with Pydantic or JSON Schema.
  - `test_post_empty_book_rejected` – Checks the API response for invalid input. This test fails on validation and is intentionally included for demonstration purposes.
  - `test_book_crud_e2e` – End-to-end test covering book creation, reading, updating, and deletion.
  - `test_post_book_various_payloads` – Data-driven/parameterized test for creating multiple books.

### 🧹 Code Style & Linting

We use [Flake8](https://flake8.pycqa.org/) for code style and linting.  

- **Black** and **Ruff** are enforced via [pre-commit](https://pre-commit.com/).  
- All code is automatically formatted (Black) and linted (Ruff) before commit and in CI.  
- To activate locally, run:

```bash
pip install pre-commit black ruff flake8
pre-commit install 
flake8 .
black .
ruff check . --fix
```

## 📘 How to Use 

### 1. **Setup**
**Clone the repository:**
```bash
  git clone https://github.com/vpaikina/book-library-api-tests.git
  cd book-library-api-tests
```

### 2. **Install dependencies:**
```bash
  pip install -r requirements.txt
```

### 3. **Run local API with JSON Server:**
```bash
  docker-compose up -d
```
The API will be available at http://localhost:3000/books.

### 4. Running Tests
- Run all tests:
```bash
  pytest -v
```
- Run with generating Allure report:
```bash
  pytest --alluredir=allure-results
```
- Run automated test suite with cleanup and open Allure report (recommended):

```bash
  ./run_tests_with_cleanup.sh
```
This script will:
- Execute all tests with data cleanup
- Generate and open the Allure report in your default browser 

### 5. Reviewing Test Results (not needed if tests were run by run_tests_with_cleanup.sh)
View Allure Report:
```bash
  allure serve allure-results
```
The report will open in your browser with detailed test results, step traces, and attachments.

