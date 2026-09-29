# Design & Documentation

## 1. Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | Add an expense with name, amount, category, date and note. |
| FR2 | View, update and delete saved expenses. |
| FR3 | Search expenses by category or keyword. |
| FR4 | Set a spending budget for a category. |
| FR5 | Calculate total and category-wise spending. |
| FR6 | Compare category spending with budgets. |
| FR7 | Export expense records to CSV. |

## 2. Non-Functional Requirements

- **Usability:** menu-driven console interface with clear prompts.
- **Reliability:** JSON writes use a temporary file before replacement.
- **Maintainability:** responsibilities are separated into modules/classes.
- **Performance:** local JSON processing is suitable for a small student expense dataset.
- **Error handling:** invalid numeric, date and text inputs are validated.
- **Resource efficiency:** no external services or database server are required.

## 3. Architecture Diagram

```mermaid
flowchart TD
    U[Student / User] --> UI[Console UI]
    UI --> ES[Expense Service]
    UI --> BS[Budget Service]
    UI --> RS[Report Service]
    ES --> V[Validators]
    BS --> V
    ES --> S[JSON Storage]
    BS --> S
    RS --> ES
    RS --> BS
    S --> D[(JSON Data Files)]
```

## 4. Workflow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Display Menu]
    B --> C{Select Operation}
    C -->|Add/Update| D[Validate Input]
    C -->|View/Search| E[Read Expenses]
    C -->|Budget| F[Set Budget]
    C -->|Reports| G[Calculate Summaries]
    C -->|Export| H[Create CSV]
    D --> I[Save JSON]
    E --> B
    F --> I
    G --> B
    H --> B
    I --> B
    C -->|Exit| J[End]
```

## 5. Use Case Diagram

```mermaid
flowchart LR
    Student((Student))
    Add[Add Expense]
    View[View Expenses]
    Update[Update Expense]
    Delete[Delete Expense]
    Search[Search Expenses]
    Budget[Set Budget]
    Report[View Reports]
    Export[Export CSV]
    Student --> Add
    Student --> View
    Student --> Update
    Student --> Delete
    Student --> Search
    Student --> Budget
    Student --> Report
    Student --> Export
```

## 6. Class / Component Diagram

```mermaid
classDiagram
    class ExpenseService
    class BudgetService
    class ReportService
    class JsonStorage
    class ConsoleUI
    class Expense
    class Budget
    ConsoleUI --> ExpenseService
    ConsoleUI --> BudgetService
    ConsoleUI --> ReportService
    ExpenseService --> JsonStorage
    BudgetService --> JsonStorage
    ReportService --> ExpenseService
    ReportService --> BudgetService
    ExpenseService --> Expense
    BudgetService --> Budget
```

## 7. Sequence Diagram — Add Expense

```mermaid
sequenceDiagram
    actor Student
    participant UI as ConsoleUI
    participant ES as ExpenseService
    participant V as Validators
    participant S as JsonStorage
    Student->>UI: Enter expense details
    UI->>ES: add(details)
    ES->>V: Validate fields
    V-->>ES: Valid data
    ES->>S: Write expense list
    S-->>ES: Saved
    ES-->>UI: New Expense
    UI-->>Student: Confirmation
```

## 8. Storage / Schema Design

`expenses.json` records:

| Field | Type | Description |
|---|---|---|
| id | integer | Unique expense identifier |
| name | string | Expense name |
| amount | number | Expense amount |
| category | string | Expense category |
| date | string | YYYY-MM-DD date |
| note | string | Optional note |

`budgets.json` records:

| Field | Type | Description |
|---|---|---|
| category | string | Budget category |
| limit | number | Maximum planned spending |

## 9. Design Decisions

JSON was retained because the original project already used local JSON storage and the project is intended to remain simple to run without an external database. Business logic is separated from storage and user-interface code so that individual components can be tested independently.
