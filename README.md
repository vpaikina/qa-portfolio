# 🎯 Vera Paikina | Senior QA Engineer Portfolio 

Welcome! I'm a Senior QA Engineer with 5+ years of experience in both manual and automated testing, specializing in REST API and web applications with microservices architecture.
This portfolio demonstrate my hands-on skills in test automation, bug analysis, structured documentation, CI/CD and more.

---

## 🚀 Tech Stack

### 🔹 Programming & Automation Tools
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pytest](https://img.shields.io/badge/Pytest-3776AB?style=for-the-badge&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-005571?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-158EB5?style=for-the-badge&logo=python&logoColor=white)
![JSON Schema](https://img.shields.io/badge/JSON--Schema-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### ☁️ Cloud & DevOps
![GitHub Actions](https://img.shields.io/badge/GitHub--Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![OpenShift](https://img.shields.io/badge/OpenShift-E00B1C?style=for-the-badge&logo=redhatopenshift&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)


### 🗃️ Data & API Tools
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/ElasticSearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)


### 📁 Test Management & reporting
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![Confluence](https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white)
![Zephyr](https://img.shields.io/badge/Zephyr-233659?style=for-the-badge&logo=zephyr&logoColor=white)
![XRay](https://img.shields.io/badge/XRay-68BC71?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiBmaWxsPSIjNjhCQzcxIi8+PC9zdmc+)
![Allure](https://img.shields.io/badge/Allure-333333?style=for-the-badge&logo=allure&logoColor=white)

---
## 📌 Featured Projects
### 🔹 [Book Library API Automation](./projects/book-library-api-tests/)

- 🔥 Pytest & Requests automation for a real CRUD API (JSON Server)
- 📦 Data-driven tests, Pydantic validation, Faker data generation, custom cleanup
- ⚙️ Configured with **GitHub Actions CI** and beautiful **Allure reports**
- 📘 Follows **best practices** and uses a clean, modular folder structure
- [➡️ View Project](./projects/book-library-api-tests/)

---

## 🔁 Sample CI/CD Integration

The project uses a **modular CI/CD setup** powered by GitHub Actions:

- [`ci.yml`](./projects/book-library-api-tests/.github/workflows/ci.yml) — main workflow logic: triggers smoke and full regression test runs.
- [`workflow-template.yml`](./projects/book-library-api-tests/.github/workflows/workflow-template.yml) — reusable workflow template: contains all core setup and test execution logic, used by `ci.yml` to avoid duplication.

**Every push or pull request triggers the main workflow, which calls the shared template, runs the tests, and generates Allure reports.**  

---

## 📊 Sample Allure Report

Here’s an example of an Allure test report generated from my [API automation project](./projects/book-library-api-tests/). 
This report demonstrates a successful run of all test cases, including detailed summaries, individual test steps, attachments, and analytics.

> **Note:** One test in the suite is intentionally marked as `xfail` (“expected fail”) because of a known API [bug](./assets/sample-bug-report.md).  
> The failing test is included on purpose to showcase real-life reporting, transparent test analysis, and advanced use of Allure features for handling unstable or problematic cases.

[📁 Open Live Allure Report (index.html)](https://vpaikina.github.io/book-library-api-tests/index.html)

> Tip: Right-click → "Open in new tab" for better viewing in browser.

---

## 🧪 Sample Bug Report

- 📝 Presented in a professional format with clear reproduction steps, expected vs actual results, and severity.
- 🚩 This bug is **intentionally included and highlighted** in the project to demonstrate real-world API contract issues and my approach to handling, documenting, and communicating defects.
- 🎯 Shows my attention to detail, structured analysis, and transparency in quality reporting.

[📂 View Bug Report](./assets/sample-bug-report.md)

___

## 🧾 My Resume 

- ✅ ISTQB Certified | 5+ years QA experience in Web testing| API Automation | Hands-on with Python, Pytest, REST API, microservises, Allure, CI/CD.

[📄 View Resume](https://github.com/vpaikina/qa-portfolio/blob/main/resume.md)

---

## 🤝 Let's Connect

📍 Montreal, Canada  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/vera-paykina-qa/)  
📧 paykina.vera@gmail.com

Looking forward to collaborating on impactful QA projects and engineering better quality software together!

