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
- [**utils/**](./utils) — API client, resource tracker, cleanup scripts  
- [**schemas/**](./schemas) — Pydantic models for response validation  
- [**tests/**](./tests) — all test cases divided by suites  
- [**config/**](./config) — environment settings and other configs 
- [**run_tests_with_cleanup.sh**](./run_tests_with_cleanup.sh) — universal launcher script
