## 🔁 Sample CI/CD Integration

The project uses a **modular CI/CD setup** powered by GitHub Actions:

- [`ci.yml`](./projects/book-library-api-tests/.github/workflows/ci.yml) — main workflow logic: triggers smoke and full regression test runs.
- [`workflow-template.yml`](./projects/book-library-api-tests/.github/workflows/workflow-template.yml) — reusable workflow template: contains all core setup and test execution logic, used by `ci.yml` to avoid duplication.

**Every push or pull request triggers the main workflow, which calls the shared template, runs the tests, and generates Allure reports.**  

