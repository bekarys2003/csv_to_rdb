# 📦 CSV Importer & Data Mapping Tool
*A flexible CSV-to-Database importer with column mapping, validation, and upsert logic.*

## 🧠 Project Overview
This project is a **full-stack CSV import platform** that allows users to upload CSV files, map CSV columns to database fields through an interactive UI, validate the data, and import it into a target database table.

The system is designed to replicate real-world **data integration workflows**, similar to HRIS → LMS or CRM → Analytics sync pipelines. The goal is to provide a clean, user-friendly interface and a robust backend that handles mapping, validation, transformation, and upserts.

---

## 🎯 Key Features

### **1. CSV Upload & Preview**
- Upload any CSV file.
- Backend automatically detects:
  - Column headers
  - File structure
- UI displays:
  - Headers
  - First N preview rows

---

### **2. Dynamic Column Mapping UI**
- Interactive React interface for mapping CSV columns → database fields.
- Supports:
  - Auto-match suggestions
  - Manual dropdown selection
  - Ignoring unused columns
  - Field-level transforms (trim, lowercase, date formatting, etc.)

---

### **3. Schema-Aware Importing**
- Backend exposes the structure of the target entity (e.g., `User`).
- Each field includes:
  - Data type (string, int, date, boolean)
  - Required/optional
  - Is it a key for upsert logic?

---

### **4. Validation Layer**
Run a validation pass before importing to ensure data quality:
- Type checks
- Missing required fields
- Invalid formats
- Status or enum mismatches

The validation screen shows:
- Total rows checked
- Valid vs invalid
- Sample error messages

---

### **5. Import Modes**
- **Insert Only** – only creates new records
- **Upsert Mode** – updates existing records based on a primary key (e.g., email)

---

### **6. Error Reporting**
All failed rows are saved with:
- Row number
- Error message
- Raw row data

Users can:
- View errors in the app
- Export them as CSV

---

### **7. Import Progress Tracking**
- Real-time job status updates:
  - `draft`, `mapping_pending`, `validating`, `running`, `completed`, `failed`
- Frontend polls backend for progress
- Supports large-file imports and async processing

---

## 🏗️ Tech Stack
**Frontend:** React, TypeScript
**Backend:** Django / Django REST Framework
**Database:** PostgreSQL
**(Optional)** Redis + Celery for background jobs
**Architecture:** Monolithic service with clean separation of concerns (upload → mapping → validation → import)

---

## 🚀 Purpose of the Project
This project demonstrates practical skills in:
- Data ingestion
- Schema-aware mapping
- Validation pipelines
- SQL upsert logic
- Frontend–backend communication
- Error handling and UX design

It simulates the real-world workflows used in enterprise integrations and is perfect for showcasing technical problem-solving abilities.

---
