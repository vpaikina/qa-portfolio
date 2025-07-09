# 📚 Book Library API Automation – Overview

This project is a robust API automation suite for a simulated Book Library system.  
It demonstrates advanced QA practices including end-to-end CRUD testing, integration scenarios, contract validation using Pydantic, dynamic test data generation, and real reporting with Allure.  
The framework is designed for maintainability, scalability, and clear reporting – ready for real-world usage and CI/CD pipelines.

---

### 2. Project Structure & Test Cases

#### **Test Suites & Test Cases**

- **test_books.py**
  - `test_create_get_update_delete_book` – End-to-end test covering book creation, reading, updating, and deletion.
  - `test_create_book_with_invalid_payload` – Checks the API response for invalid input.
  - `test_update_nonexistent_book` – Ensures proper error handling for updating non-existent resources.
  - `test_delete_book_twice` – Validates behavior on repeated delete requests.
  - `test_get_book_schema_validation` – Verifies API response contract with Pydantic or JSON Schema.
  - `test_bulk_create_books` – Data-driven/parameterized test for creating multiple books.
  - (… другие тесты проекта, если есть – дополни сам)

---

### 3. How to Use 

#### **Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vpaikina/book-library-api-tests.git
   cd book-library-api-tests
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run local API with JSON Server:**
```bash
docker-compose up -d
```
The API will be available at http://localhost:3000/books.

4. Running Tests
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
- Automatically start the local API server (if needed)
- Execute all tests with data cleanup
- Generate and open the Allure report in your default browser 

5. Reviewing Test Results (not needed if tests were run by run_tests_with_cleanup.sh)
View Allure Report:
```bash
allure serve allure-results
```
The report will open in your browser with detailed test results, step traces, and attachments.
