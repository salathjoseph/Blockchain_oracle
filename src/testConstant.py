POST /orders/create
Content-Type: application/json

{
    "customer_name": "John Doe",
    "product_name": "Rice",
    "product_id": "F001",
    "quantity": 10,
    "shop_owner": "Shop A"
}

PUT /orders/update/1
Content-Type: application/json

{
    "status": "Shipped"
}
