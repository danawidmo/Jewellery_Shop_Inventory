# Jewellery Shop Inventory App

## Tracks inventory products, filters products by designer and type, alerts to low and out of stock items, adds products and designers, displays markup on prices and marks inactive designers.

Jewellery Shop Inventory App is a full stack application for my solo CodeClan project. It is written in python, runs on Flask and uses psycopg with PostgreSQL database. It allows the user to manage their shop inventory. Building this app consolidated knowledge and skills taught during the first module at CodeClan. 

## Possible new features and improvements

* Search feature
* Filtering by type and designer using dropdown
* Allowing products to have many types
* Sorting products alphabetically

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install falsk
```
```bash
pip install psycopg
```
To download this project create a local directory and clone this project into it.

```bash
git clone git@github.com:DanaVarahi/Jewellery_Shop_Inventory.git
```
You will have to create the database
```bash
createdb jewellery_shop
```
Now create your tables by running the following command:
```bash
psql -d jewellery_shop -f db/jewellery_shop.sql
```
You will want to populate the tables with initial data.
```bash
python3 console.py
```
You are ready to start the server.
```bash
flask run
```
You should see something similar to this:

![flask server running](https://github.com/DanaVarahi/screenshots/blob/main/flask.png)

Click on the http link to view the app in a browser. 
Your app is ready and running.

## Screenshots

### Inventory
![Inventory home page](https://github.com/DanaVarahi/screenshots/blob/main/Screenshot%202020-11-15%20at%2010.46.40.png)

### Inventory filtered by type: ring 
![Inventory sorted by type](https://github.com/DanaVarahi/screenshots/blob/main/sort-by-type.png)

### Adding new product
![Add Product](https://github.com/DanaVarahi/screenshots/blob/main/add-product.png)

### Designers
![All designers](https://github.com/DanaVarahi/screenshots/blob/main/designers.png)

### Updating a designer
![Edit designer detail](https://github.com/DanaVarahi/screenshots/blob/main/edit-designer.png)

### Markup on products price and low and out of stock warning.
![Low and out of stock](https://github.com/DanaVarahi/screenshots/blob/main/low-stock.png)

### Mobile view
![Mobile view](https://github.com/DanaVarahi/screenshots/blob/main/mobile.png)


## License
[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
