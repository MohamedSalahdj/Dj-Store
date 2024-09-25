# Dj-Store

Dj-Store is a Django-based E-commerce project designed to enhance the user experience by providing an easy-to-navigate platform for exploring brands and products. The platform offers a seamless shopping experience with modern features aimed at improving user engagement and interaction with the store's catalog.

## Features

### Products and Brands:
- **Product Listings:** Display a list of products with pagination to improve loading time and user experience.
- **Product Detail Pages:** View detailed product information along with reviews and related items.
- **Brand Listings:** Display brands with product count annotations.
- **Brand Detail Pages:** View all products associated with a specific brand.

### Shopping Cart and Orders:
- **Add to Cart:** Allow users to add products to their cart, specifying quantities, with validation to ensure the stock quantity is available.
- **Increase/Decrease Quantity:** Users can easily adjust the quantity of products in their cart.
- **Remove from Cart:** Option to remove products from the cart.
- **Checkout Page:** Summarize items in the cart with an option to proceed to checkout.

### User Accounts:
- **User Registration and Activation:** New users can register an account and receive an email for activation.
- **User Profile:** Registered users can view and edit their profile, contact numbers, and addresses.
- **Login and Logout:** Standard Django authentication for login/logout.
- **Password Reset:** Django's built-in password reset mechanism.
  
### Reviews:
- **Add Reviews:** Authenticated users can add reviews for products they’ve purchased.
- **Real-time Review Updates:** Product reviews are dynamically updated without requiring a full page refresh.

### Queryset Debugging and Performance:
- **Efficient Querysets:** The platform uses optimized queryset techniques such as `select_related`, `prefetch_related`, and aggregation functions like `Sum`, `Avg`, and `Count` for improved performance.
- **Annotated Querysets:** Additional information, such as price with discounts, is calculated on the fly using Django’s `F` expressions and annotations.
- **Complex Querying:** Support for filtering with complex conditions using Django's `Q` objects (e.g., `Q(price__lt=1000) & Q(quantity__gt=10)`).

### Coupons:
- **Coupon Integration:** Users can apply discount coupons to their orders during checkout (if available).
  
### i18n and Localization:
- **Internationalization (i18n):** The project supports (`Arabic`, `English`)languages with built-in translation features.
- **Rosetta Integration:** A user-friendly interface for managing and editing translations.

### REST API Integration:
- **REST Authentication:** The project integrates with `dj-rest-auth` to provide token-based authentication for the API.
- **User Registration via API:** Allow users to register and log in using API endpoints, supporting both session-based and token-based authentication.

### Additional Tools:
- **Debug Toolbar:** Django Debug Toolbar is enabled for development to profile and optimize queries.
- **Admin Panel:** Django's built-in admin panel provides a backend interface to manage products, orders, and users.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MohamedSalahdj/Dj-Store.git
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up your `.env` file with the necessary environment variables (e.g., database settings, API keys).

6. Run migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:
    ```bash
    python manage.py runserver
    ```

9. Access the app by visiting `http://127.0.0.1:8000/`.

- ## API Endpoints

  ### Authentication

  - **Login:** `/dj-rest-auth/login/`
  - **Logout:** `/dj-rest-auth/logout/`
  - **Register:** `/dj-rest-auth/registration/`

## Environment Variables

The project requires an `.env` file for sensitive data and configuration. The following variables need to be defined:

```env
EMAIL_HOST_USER=email_username
EMAIL_HOST_PASSWORD=email_password
```
