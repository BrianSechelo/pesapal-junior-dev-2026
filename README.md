# Pesapal Junior Developer Challenge ’26  
# MiniDB – A Simple Relational Database Engine in Python

This project is a*minimal relational database management system (RDBMS) built from scratch in Python as part of the Pesapal Junior Developer Challenge ’26.

The goal of the project is to demonstrate understanding of core database concepts including table design, CRUD operations, indexing, query execution, and building a simple SQL-like interface with an interactive REPL and a demo web application.

---

## Features

- Table creation with basic data types (`INT`, `TEXT`)
- Primary key and unique key constraints
- Basic indexing for fast uniqueness checks
- SQL-like query execution engine
- Supported queries:
  - `CREATE TABLE`
  - `INSERT INTO`
  - `SELECT * FROM`
- Interactive REPL (Read–Eval–Print Loop)
- Demo REST API built with Flask using the custom DB engine
- Clear separation between engine, storage, REPL, and web layer

---

##  Core Concepts Demonstrated

- Relational table modeling
- Constraint enforcement (PRIMARY KEY, UNIQUE)
- In-memory indexing using hash-based structures
- Simple SQL parsing and execution
- Error handling and validation
- Interactive systems (REPL)
- Backend API integration using a custom database engine

---

## Project Structure
pesapal-junior-dev-2026/
│
├── db/ # Core database engine
│ ├── init.py
│ ├── database.py # Database and table registry
│ ├── table.py # Table, columns, indexing logic
│ ├── engine.py # SQL-like command parser and executor
│ └── repl.py # Interactive REPL
│
├── web/ # Demo web application
│ └── app.py # Flask app using the DB engine
│
├── data/ # (Reserved for future persistence)
├── README.md
└── .venv/ # Virtual environment


---

## Running the Interactive REPL

The REPL allows you to interact with the database using SQL-like commands.

### Start the REPL
```bash
python -m db.repl
Example Session
db > CREATE TABLE users (id INT PRIMARY KEY, email TEXT UNIQUE, name TEXT)
Table 'users' created

db > INSERT INTO users VALUES (1, 'a@b.com', 'Alice')
1 row inserted into 'users'

db > INSERT INTO users VALUES (2, 'b@b.com', 'Bob')
1 row inserted into 'users'

db > SELECT * FROM users
[{'id': 1, 'email': 'a@b.com', 'name': 'Alice'}, {'id': 2, 'email': 'b@b.com', 'name': 'Bob'}]

db > exit
Goodbye 

## Running the Demo Web API
The demo web app shows how the custom database engine can be used in a real application.

#Start the Flask App
python web/app.py

## Available Endpoints
# Create a user
POST /users
Request body (JSON):
{
  "id": 1,
  "email": "a@b.com",
  "name": "Alice"
}

List users
GET /users
[
  {
    "id": 1,
    "email": "a@b.com",
    "name": "Alice"
  }
]

## Indexing Explained

#Basic indexing is implemented using hash-based sets for:

Primary key columns

Unique columns

This allows:

Fast duplicate detection during inserts

Constant-time uniqueness checks

Early error detection without scanning all rows

Indexes are updated automatically on each insert.

## Future Improvements
UPDATE and DELETE support

WHERE clause filtering

JOIN operations

Persistent storage to disk

Query optimization

Type validation and casting

More robust SQL parsing

## Why This Approach?
Instead of using an existing database or ORM, this project focuses on first principles:

How tables work internally

How constraints are enforced

How queries are parsed and executed

How databases expose interfaces (REPL + API)

The emphasis is on clarity of thought, correctness, and extensibility rather than completeness.
Author

Brian Sechelo
Pesapal Junior Developer Challenge ’26

GitHub: https://github.com/BrianSechelo

# License

This project is provided for evaluation and learning purposes.

