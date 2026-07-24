# HAWC CRM API Documentation

Base URL: `http://hawc.localhost:8000`

All endpoints require authentication (Session cookie or API Key/Secret headers).

---

## 1. Get All Leads
- **Endpoint**: `/api/method/hawc_crm.api.get_all_leads`
- **Method**: `GET`
- **Auth Required**: Yes
- **Sample Response**:
  ```json
  {
    "message": [
      {
        "name": "Lead-001",
        "lead_name": "John Doe",
        "status": "New",
        "assigned_to": "sales@hawc.com"
      }
    ]
  }
  ```

---

## 2. Create Lead
- **Endpoint**: `/api/method/hawc_crm.api.create_lead`
- **Method**: `POST`
- **Auth Required**: Yes
- **Request Body**:
  ```json
  {
    "lead_name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "1234567890",
    "source": "Website",
    "status": "New"
  }
  ```
- **Sample Response**:
  ```json
  {
    "message": "Lead-002"
  }
  ```

---

## 3. Get Pipeline
- **Endpoint**: `/api/method/hawc_crm.api.get_pipeline`
- **Method**: `GET`
- **Auth Required**: Yes
- **Sample Response**:
  ```json
  {
    "message": {
      "Prospecting": [
        {
          "name": "Deal-001",
          "deal_title": "Acme Corp Deal",
          "deal_value": 5000.0,
          "stage": "Prospecting"
        }
      ]
    }
  }
  ```

---

## 4. Convert Lead to Deal
- **Endpoint**: `/api/method/hawc_crm.api.convert_lead_to_deal`
- **Method**: `POST`
- **Auth Required**: Yes
- **Request Body**:
  ```json
  {
    "lead_name": "Lead-001",
    "deal_value": 10000.0,
    "expected_close_date": "2026-12-31"
  }
  ```
- **Sample Response**:
  ```json
  {
    "message": "Deal-002"
  }
  ```

---

## 5. Get Activity Summary
- **Endpoint**: `/api/method/hawc_crm.api.get_activity_summary`
- **Method**: `GET`
- **Auth Required**: Yes
- **Sample Response**:
  ```json
  {
    "message": {
      "Call": 5,
      "Email": 12,
      "Meeting": 3
    }
  }
  ```
