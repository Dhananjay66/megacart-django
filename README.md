## 🛒 GreatCart — Django eCommerce Platform

**GreatCart** is a Django-based eCommerce web application that supports:

* User authentication and roles (Admin, Seller, Customer)
* Product management by sellers
* Category and variation (e.g. size, color) support
* Dynamic formset for adding multiple product variations at once
* Cart and order functionality

---

## 🚀 Features

* ✅ Role-based user system (Admin, Seller, Customer)
* ✅ Product CRUD for sellers
* ✅ Product variations (size, color)
* ✅ Dynamic add-more-variations using JavaScript
* ✅ Cart management
* ✅ Order processing and checkout
* ✅ Review and rating system
* ✅ Bootstrap-based responsive UI

---

## 📁 Folder Structure

```
greatcart/
├── accounts/         # User management
├── carts/            # Shopping cart
├── category/         # Product categories
├── orders/           # Order processing
├── store/            # Product and variation management
├── templates/        # HTML templates (Bootstrap styled)
├── static/           # CSS, JS, fonts, images
└── media/            # Uploaded files (images)
```

---

## 🖥️ Screenshots

* 🛍️ Product add page with dynamic variation fields
* 👤 Seller dashboard to manage products
* 🛒 Cart and checkout flow

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/greatcart.git
cd greatcart
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Now open `http://127.0.0.1:8000` in your browser.

---

## ✨ How to Add Product with Variations

* Navigate to `/store/add-product/`
* Fill out product details
* Use `+ Add More Variations` to add unlimited size/color entries
* Submit to save both product and all its variations

---

## 📦 Technologies Used

* Python 3.13 / Django 5.2
* Bootstrap 5
* SQLite (default DB)
* JavaScript (for dynamic formsets)
* Pillow (for image uploads)

---

## 📌 To Do / Ideas

* [ ] AJAX variation add/remove
* [ ] Wishlist feature
* [ ] Payment gateway integration (e.g. Razorpay, Stripe)
* [ ] Product search and filter

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---
