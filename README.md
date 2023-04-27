# MiniVi

MiniVi Online Clothes Shop is a Django web application that allows administrators to add new goods and manage existing ones. Users can browse through the available products, and send their purchase requests.

# Features

- Administrator panel for adding and managing products
- User-friendly interface for browsing and ordering products
- Filter by price, size, brand, category, and more
- Navigation by search and categories/brands
- Admin dashboard for viewing orders
- Customer order placement

# Search
Users can search for products by entering a search term into the search bar on the homepage or on the product listing page. The search function supports a variety of search queries, including product name, description, brand, and more. Search results are displayed in real-time as the user types, making it easy to quickly find the desired product.
<br>

![](https://github.com/kaydurgu/minivi_online_shop/blob/main/gif/navigation.gif)

<br>

## Categories and Brands
You can aslo navigate by set of categories and brands that users can use to navigate the product catalog. Categories and brands are displayed prominently on the homepage and product listing page, making it easy for users to quickly filter and browse products by category or brand.

To use the categories and brands navigation feature, simply click on the desired category or brand to view all products that match that criteria. The product listing page will automatically update to show only the products that match the selected category or brand.

The search and categories/brands navigation features make it easy for users to quickly find the products they need, no matter how they prefer to browse the catalog.

# Filter

Filter allows users to easily filter products based on various criteria such as price, size, brand, category, and more. This feature helps users quickly find the products that match their preferences and needs.

To use the filter feature, simply select the desired filter criteria from the available options on the product listing page. The page will automatically update to show only the products that match the selected criteria.

The filter feature is flexible and customizable, allowing users to easily search for specific products that fit their unique needs. Whether you're looking for a specific brand, size, or price range, the filter feature makes it easy to find the perfect product.



![](https://github.com/kaydurgu/minivi_online_shop/blob/main/gif/filter.gif)
<br>



## Admin Dashboard


The administrator panel includes a dashboard that allows administrators to view and manage orders placed by customers. The dashboard provides a quick overview of order , making it easy for administrators to track orders and manage fulfillment.

<br>

![](https://github.com/kaydurgu/minivi_online_shop/blob/main/gif/adminka.gif)

<br>


## Customer Order Placement

The ability for customers to place orders and for administrators to view and manage those orders is a key feature of the MiniVi Online Clothes Shop, providing a streamlined and efficient shopping experience for both parties.
<br>

![](https://github.com/kaydurgu/minivi_online_shop/blob/main/gif/customer%20order%20and%20admin%20dashboard.gif)

<br>

# Admin Panel
The administrator panel provides a centralized location for managing products. Administrators can easily add new products, update existing products, and remove products that are no longer available. The panel includes a user-friendly interface that makes it easy for administrators to manage the product catalog, including adding product images, descriptions, prices, and more.
<br>

![](https://github.com/kaydurgu/minivi_online_shop/blob/main/gif/adminka.gif)

<br>

## Installation

1. Clone this repository using git clone https://github.com/kaydurgu/minivi_online_shop.git
2. Create a virtual environment using virtualenv venv and activate it using source ``venv/bin/activate`` (Linux/Mac) or ``venv\Scripts\activate`` (Windows).
3. Install the requirements using ``pip install -r requirements.txt``.
4. Create a new database by running  ``python manage.py migrate ``.
5. Create a superuser by running ``python manage.py createsuperuser`` and follow the prompts to create a new user.
6. Run the server using python manage.py runserver and visit ``http://localhost:8000`` in your web browser.


 
