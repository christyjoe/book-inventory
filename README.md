# book-inventory
Home Page: https://guarded-wave-97929.herokuapp.com/home/

Features:

1. View number of books available in stock.
2. Update the stock of books.
3. Remove a book from the inventory.
4. Search for any book using Google Books API.
5. Add a new book to the inventory.


Assumptions:

1. If the stock a book goes to 0, it is considered to be "Out Of Stock".
2. Maximum stock a book cant exceed 9999.
3. Wouldn't be able to update a book stock of available book using search.


Implementation:

1. Django framework in Python3
2. SQLlite for database
3. Deployed in Heroku server


Running instructions:

git clone
pip install -r requirements.txt
python3 manage.py makemigrations book
python3 manage.py migrate
python3 manage.py runserver 8080

Note: Google Books API is limited to 10 books per search.

Served locally at http://127.0.0.1:8080/home/
