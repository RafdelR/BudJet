# BudJet

Simple description of filestructure:

```
.
├── assets/
│   ├── icons/                      # Static files like app icons
│   └── styles/                     # CSS/Styling files for the UI
├── docs/
│   └── README.md                   # Documentation for the project setup and usage
├── pyproject.toml                  # Python packaging file
├── requirements.txt                # Python dependencies
├── src/
│   ├── api/
│   │   ├── bank_integrations/
│   │   │   └── manual_input.py     # Allows manual input of accounts and cash
│   │   ├── file_parser/
│   │   │   ├── csv_excel_parser.py # Extracts transaction data from CSV/Excel files
│   │   │   └── pdf_parser.py       # Extracts transaction data from PDFs
│   │   └── data_synchronization.py # Synchronizes all financial data sources (manual + parsed)
│   ├── models/
│   │   ├── account.py              # Represents user bank accounts
│   │   ├── category.py             # Represents account categories (e.g., Savings, Investments, Cash)
│   │   └── transaction.py          # Represents a financial transaction
│   ├── services/
│   │   ├── balance_calculator.py   # Aggregates and calculates total balance across all accounts
│   │   └── transaction_service.py  # Processes, validates, and manages transactions
│   ├── components/
│   │   ├── dashboard/
│   │   │   ├── dashboard_view.py           # Main dashboard UI
│   │   │   ├── total_balance_component.py  # Displays total balance across all sources
│   │   │   ├── expenses_component.py       # Shows categorized expenses and income
│   │   │   └── transactions_component.py   # Lists all transactions with details
│   │   ├── bank_overview/
│   │   │   ├── bank_view.py                # Visualizes aggregated money per bank
│   │   │   └── account_view.py             # Displays details for individual accounts
│   └── utils/
│       ├── constants.py           # Static constants like default categories and supported file types
│       ├── file_handler.py        # General utilities for handling file uploads and reads
│       └── logger.py              # Logs system events, warnings, and errors
│   ├── app.py                     # Entry point to initialize and run the application
└── tests/
    ├── test_api/
    │   ├── test_csv_parser.py     # Tests for CSV/Excel file parsing
    │   ├── test_pdf_parser.py     # Tests for PDF file parsing
    │   └── test_manual_input.py   # Tests for manual data input functionality
    ├── test_services/
    │   ├── test_balance_calculator.py  # Tests logic for balance aggregation
    │   └── test_transaction_service.py # Tests for processing and managing transactions
    ├── test_models/
    │   ├── test_account.py        # Tests account model behavior
    │   └── test_transaction.py    # Tests transaction model behavior
    └── test_components/
        ├── test_dashboard.py      # Tests for dashboard components
        └── test_bank_view.py      # Tests for bank and account visualizations

```
