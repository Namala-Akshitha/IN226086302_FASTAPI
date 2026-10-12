# FastAPI Internship – Day 1
## E-Commerce Product API

### Overview
This project is part of FastAPI Internship Training – Day 1. It extends a basic product API with product filtering, stock monitoring, store statistics, product search, and price-based deals.

### Features
- Retrieve all products and their total count.
- Filter products by category.
- Retrieve only in-stock products.
- Display store statistics and available categories.
- Search products by name without case sensitivity.
- Identify the cheapest and most expensive products.

### Technologies Used
- Python
- FastAPI
- Uvicorn
- Swagger UI

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/products` | Retrieve all products |
| GET | `/products/category/{category_name}` | Filter by category |
| GET | `/products/instock` | Retrieve in-stock products |
| GET | `/store/summary` | Display store statistics |
| GET | `/products/search/{keyword}` | Search product names |
| GET | `/products/deals` | Retrieve cheapest and most expensive products |

### How to Run

1. Install the dependencies:

   `pip install fastapi uvicorn`

2. Start the application from the folder containing `main.py`:

   `uvicorn main:app --reload`

3. Open the API documentation:

   `http://127.0.0.1:8000/docs`

4. Test each endpoint using Swagger UI.

### Learning Outcomes
- Creating REST API endpoints using FastAPI.
- Filtering and searching Python lists of dictionaries.
- Working with conditional statements and collections.
- Returning structured JSON responses.
- Testing APIs through Swagger UI.

### Internship Assignment
FastAPI Internship Training – Day 1 Practice Tasks.
