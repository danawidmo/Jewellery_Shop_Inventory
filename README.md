# Jewellery Shop Inventory App
Jewellery Shop Inventory App is an example of a fullstack application written in python. It runs on flask and uses psycopg with PostgreSQL database. It allows the user to manage their shop inventory.

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

## Usage

![Inventory home page](https://github.com/DanaVarahi/screenshots/blob/main/Screenshot%202020-11-15%20at%2010.46.40.png)

Jewellery Shop Inventory App allows the user to view all products, sort them by designer and by type. 

![Inventory sorted by type](https://github.com/DanaVarahi/screenshots/blob/main/sort-by-type.png)

User can add and edit products. 

![Add Product](https://github.com/DanaVarahi/screenshots/blob/main/add-product.png)

Jewellery Shop Inventory App displayes all designers.

![All designers](https://github.com/DanaVarahi/screenshots/blob/main/designers.png)

User can also edit designer detail and mark designers as inactive so that they will not appear in the designer selection for new products.

![Edit designer detail](https://github.com/DanaVarahi/screenshots/blob/main/edit-designer.png)

The app calculates markup on product price automatically and displays it to the user. It also alerts the user to low and out of stock items.

![Low and out of stock](https://github.com/DanaVarahi/screenshots/blob/main/low-stock.png)

Jewellery Shop Inventory App is responsive and can be viewed on mobile devices.

![Mobile view](https://github.com/DanaVarahi/screenshots/blob/main/mobile.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
