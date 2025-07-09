# Sample Bug Report
___

### Bug: [API_Contract] API allows POST /books with empty body (expected 400, got 200).

| Field         | Value                                                  |
|---------------|--------------------------------------------------------|
| **ID**        | API-CONTRACT-001                                       |
| **Reported by** | Vera Paikina                                         |
| **Priority**  | Major                                                  |
| **Status**    | Open                                                   |
| **Component** | Book API                                               |
| **Environment** | https://fakerestapi.azurewebsites.net/api/v1         |
| **Software Version**| 1.2.3                                             |

---

#### Summary

API allows creation of a book entity when a `POST` request with an empty JSON payload is submitted. 
According to the API contract, such requests should be rejected with **HTTP 400 (Bad Request)**. 
Instead, a new book is created with all fields set to `null`, zero, or default values.

---

#### Steps to Reproduce

1. Send a `POST` request to `/books` endpoint with an empty JSON payload (`{}`).
2. Observe the API response and database state.

---

#### Actual Result

- API returns **HTTP 200 Created** 
- A book is created with all fields set to default values:	
Response body
```json
{
  "id": 0,
  "title": null,
  "description": null,
  "pageCount": 0,
  "excerpt": null,
  "publishDate": "0001-01-01T00:00:00"
}
```
- Automation contract tests are failing (see attachements).

---

#### Expected Result (based on the Acceptance Criteria)
- API must return **HTTP 400 Bad Request** for any POST /books with missing required fields or empty payload.
- No book entity must be created in such case.

___ 

#### Notes
- Issue reproducible on both staging and production environments.
- Validation for missing or empty required fields should be implemented at the API level for all required fields.

---

####  Attachments
- [Allure Report](https://vpaikina.github.io/book-library-api-tests/index.html)

