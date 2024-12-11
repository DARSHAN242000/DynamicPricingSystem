# Dynamic Pricing and Discount System

## Overview

This project is a **Django REST Framework** application that dynamically calculates product prices, applies discounts (including tiered discounts), and manages orders. It exposes the functionality through RESTful APIs.

---

## Features

1. **Product Management**:
   - Add, update, delete, and retrieve products.
   - Support for various product types:
     - **Base Product**
     - **Seasonal Product** (seasonal discounts)
     - **Bulk Product** (tiered discounts based on quantity)
     - **Premium Product** (fixed markup).
   - Retrieve real-time price for a product based on type and quantity.

2. **Discount Management**:
   - Add, update, delete, and retrieve discounts.
   - Support for discount types:
     - **Percentage Discount**
     - **Fixed Amount Discount**
     - **Tiered Discount** (value- or quantity-based).
   - List active discounts by type.

3. **Order Management**:
   - Create orders with multiple products and discounts.
   - Calculate the total price of an order dynamically.
   - Retrieve detailed order information.

---

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd DynamicPriceSystem
   
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt

4. **Apply Migrations:**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
5. **Run the Development Server:**:
   ```bash
   python manage.py runserver

---

## API Endpoints

### Products

- **List All Products**: `GET /products/products/`
- **Retrieve Product**: `GET /products/products/{id}/`
- **Create Product**: `POST /products/products/`
- **Update Product**: `PUT /products/products/{id}/`
- **Delete Product**: `DELETE /products/products/{id}/`
- **Real-Time Price**: `GET /products/products/{id}/real-time-price/?quantity={quantity}`

### Discounts

- **List All Discounts**: `GET /discounts/discounts/`
- **Retrieve Discount**: `GET /discounts/discounts/{id}/`
- **Create Discount**: `POST /discounts/discounts/`
- **Update Discount**: `PUT /discounts/discounts/{id}/`
- **Delete Discount**: `DELETE /discounts/discounts/{id}/`
- **List Percentage Discounts**: `GET /discounts/percentage-discounts/`
- **List Fixed Amount Discounts**: `GET /discounts/fixed-amount-discounts/`
- **List Tiered Discounts**: `GET /discounts/tiered-discounts/`

### Orders

- **List All Orders**: `GET /orders/orders/`
- **Retrieve Order**: `GET /orders/orders/{id}/`
- **Create Order**: `POST /orders/orders/`
- **Calculate Total**: `GET /orders/orders/{id}/calculate-total/`

---

## Example Workflows

### Create an Order
**Request**:
```json
POST /api/orders/
{
    "products": [
        {"product_id": 1, "quantity": 2},
        {"product_id": 2, "quantity": 1}
    ],
    "discounts": [1]
}
```

## Running Tests

Run the test suite to verify functionality:
```bash
python manage.py test
```

## Directory Structure
```bash
DynamicPriceSystem/
│
├── products/           # Product models, views, serializers, tests
├── discounts/          # Discount models, views, serializers, tests
├── orders/             # Order models, views, serializers, tests
├── DynamicPriceSystem/    # Main project settings and URLs
├── manage.py           # Django project entry point
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

