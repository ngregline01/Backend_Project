
# 🏗️ Mechanic Shop Database API

A **RESTful API** for a mechanic shop that manages records related to  **customers** ,  **mechanics** ,  **service tickets** , and  **inventory parts** .

This project demonstrates a modular Flask architecture using  **Blueprints** ,  **SQLAlchemy models** , and **Marshmallow** for serialization and validation.

---

## 🔹 Project Overview

* **General `__init__.py`**

  * Contains the `create_app()` function to initialize and run the Flask application.
  * Registers all **Blueprints** with their corresponding URL prefixes.
  * Initializes extensions such as  **Marshmallow** ,  **Flask-Limiter** ,  **Flask-Caching** , and database connections.
* **`models.py`**

  * Defines all **database models/classes** used in the API, including:
    * `Customers`
    * `Mechanics`
    * `Service_Tickets`
    * `Inventory` → Stores parts and materials used in service tickets
    * `ServicePart` → Many-to-many association table between `Service_Tickets` and `Inventory`
* **`extensions/`**

  * Initializes  **Marshmallow** ,  **Flask-Limiter** , and  **Flask-Caching** .
  * Handles **serialization** and **deserialization** for models.
* **`utils/base/`**

  * Contains utility functions for **encoding and decoding** sensitive data such as passwords and tokens.
* **Blueprint Folders**
  The application is modularized into four main blueprint folders:

  1. **Customers**
  2. **Mechanics**
  3. **Service Tickets**
  4. **Inventory**

  Each folder contains:

  * `__init__.py` → Initializes the blueprint.
  * `schema.py` → Defines **Marshmallow schemas** for request validation and response formatting.
  * `routes.py` → Implements all **CRUD operations** for the resource, including association handling (e.g., assigning parts to service tickets).

---

## ⚙️ Features

* **Customers**
  * Create, read, update, delete, and paginate customers.
  * Token-based authentication for protected routes.
* **Mechanics**
  * Create, read, update, delete, and list mechanics.
  * Query mechanics based on the number of service tickets they have worked on.
* **Service Tickets**
  * Create and read service tickets.
  * Assign and remove mechanics from tickets.
  * Add and track parts used on tickets through the `ServicePart` many-to-many relationship.
* **Inventory**
  * CRUD operations for parts used in service tickets.
  * Track **quantity used** per ticket.
* **Utilities**
  * Password and token  **encoding/decoding** .
  * **Query parameters** for filtering and pagination.
  * **Caching** for frequently accessed routes.
  * **Rate limiting** to prevent abuse.
* **Pagination, Filtering, and Limits**
  * Pagination on list endpoints using query parameters (`page`, `per_page`).
  * Query parameters supported for filtered retrieval.
  * Caching and limiter applied to improve performance and security.

---

## 💻 Technologies Used

* **Python 3.11+**
* **Flask** – Web framework for building REST APIs
* **Flask-SQLAlchemy** – ORM for database modeling
* **Flask-Marshmallow** – Serialization, deserialization, and validation
* **Flask-Caching** – Caching support for routes
* **Flask-Limiter** – Rate limiting for endpoints
* **MySQL** (via `mysqlconnector`) – Database backend
