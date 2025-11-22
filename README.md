# SQL-Connection-with-Python
MySQL Database Connection & Data Fetching Script
This Python script connects to a MySQL database using the mysql-connector-python library and retrieves all rows from a specified table. It includes proper connection handling, error catching, and row-by-row printing of the fetched data.
Features
Connects to a MySQL database using mysql.connector
Checks if the connection is successfully established
Executes a SELECT * query on the table named Name
Fetches all rows with fetchall()
Prints each row in a clean loop
Includes exception handling for MySQL errors

##  Project Structure
```
project-folder/
│── con1.py # Main Python script
│── README.md # Documentation
└── requirements.txt # Dependencies
```
##  Getting Started

Follow the steps below to run this project on your system.

---

### **1. Install MySQL Server**
Make sure MySQL is installed and running on your machine.

For macOS:
- If installed via DMG → Start MySQL from **System Settings → MySQL**
- If installed via Homebrew:
  ```bash
  brew services start mysql

## Installation & Setup
### Step 1: Clone the repository
```
git clone <your-repo-url>
cd <your-project-folder>
```
### Step 2: Install Dependencies

```
pip install -r requirements.txt
```
### Step 3: Run the Python Script
```
python3 con1.py
```


