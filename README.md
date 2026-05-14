# Smart Inventory Demo

A full-stack inventory management web app built with Python, Flask, and SQLite. Features a normalized database schema, RESTful CRUD API, real-time low-stock alerts, and a live analytics dashboard.

## Features

- **Dashboard** — total products, inventory value, low-stock count, out-of-stock count
- **Low-stock alert engine** — flags items at or below configurable reorder threshold
- **CRUD operations** — add products, log restocks and sales via REST API
- **Transaction history** — audit log of all inventory movements
- **Search** — filter products in real time
- **REST API** — full JSON API for products and transactions

## Tech Stack

- Python 3.x
- Flask (web framework)
- SQLite (normalized relational database)
- HTML5 / CSS3 / Vanilla JavaScript (frontend)

## Installation

```bash
git clone https://github.com/Ysalapu24/smart-inventory-demo.git
cd smart-inventory-demo
pip install flask
python app.py
```

Then open your browser to: `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products` | List all products |
| POST | `/api/products` | Add a new product |
| PUT | `/api/products/<id>` | Update a product |
| DELETE | `/api/products/<id>` | Delete a product |
| POST | `/api/transaction` | Log a sale or restock |
| GET | `/api/alerts` | Get low-stock alerts |

## Database Schema
## Author

**Yeshwanth Salapu**  
B.S. Computer Science — University of North Texas  
[LinkedIn](https://www.linkedin.com/in/yeshwanth-salapu-a257b7291/) | [GitHub](https://github.com/Ysalapu24)
