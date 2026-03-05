from fastapi import FastAPI
app=FastAPI()
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True },
    {'id': 2, 'name': 'Notebook',       'price':  99,  'category': 'Stationery',  'in_stock': True },
    {'id': 3, 'name': 'USB Hub',         'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set',          'price':  49, 'category': 'Stationery',  'in_stock': True },
]
# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Product API"}
# Get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total_products": len(products)
    }
# Add product
@app.post("/products")
def add_product(product: dict):
    products.append(product)
    return {
        "message": "Product added successfully",
        "product": product
    }
@app.get("/category/{category_name}")
def get_products_by_category(category_name: str):
    result = []
    for product in products:
        if product["category"].lower() == category_name.lower():
            result.append(product)
    if result:
        return result
    else:
        return {"message": "No products found in this category"}
@app.get("/products/instock") 
def get_instock(): 
    available = [p for p in products if p["in_stock"] == True] 
    return {"in_stock_products": available, "count": len(available)}
@app.get("/store/summary") 
def store_summary(): 
    in_stock_count = len([p for p in products if p["in_stock"]]) 
    out_stock_count = len(products) - in_stock_count 
    categories = list(set([p["category"] for p in products])) 
    return { "store_name": "My E-commerce Store", "total_products": len(products), "in_stock": in_stock_count, "out_of_stock": out_stock_count, "categories": categories, }
@app.get("/products/search/{keyword}") 
def search_products(keyword: str): 
    results = [ p for p in products if keyword.lower() in p["name"].lower() ] 
    if not results: 
       return {"message": "No products matched your search"} 
    return {"keyword": keyword, "results": results, "total_matches": len(results)}
@app.get("/products/deals") 
def get_deals(): 
    cheapest = min(products, key=lambda p: p["price"]) 
    expensive = max(products, key=lambda p: p["price"]) 
    return { "best_deal": cheapest, "premium_pick": expensive, }