# 📚 Book Library API Automation – Overview
---

### **Test Suites & Test Cases**

- **The project includes four tests that automate the following scenarios:**
  - `test_book_response_contract` – Verifies API response contract with Pydantic or JSON Schema.
  - `test_post_empty_book_rejected` – Checks the API response for invalid input.
  - `test_book_crud_e2e` – End-to-end test covering book creation, reading, updating, and deletion.
  - `test_post_book_various_payloads` – Data-driven/parameterized test for creating multiple books.

---

### How to Use 

#### **Setup**

#### 1. **Clone the repository:**
```bash
git clone https://github.com/vpaikina/book-library-api-tests.git
cd book-library-api-tests
```

#### 2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

#### 3. **Run local API with JSON Server:**
```bash
docker-compose up -d
```
The API will be available at http://localhost:3000/books.

#### 4. Running Tests
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

#### 5. Reviewing Test Results (not needed if tests were run by run_tests_with_cleanup.sh)
View Allure Report:
```bash
allure serve allure-results
```
The report will open in your browser with detailed test results, step traces, and attachments.
