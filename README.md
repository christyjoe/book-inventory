# book-inventory
Features:

View number of books avaialble in stock.
Update the stock of books.
Remove a book from the inventory.
Search for any book using Google Books Api.
Add a new book to the inventory.
Assumptions:

If the stock a book reduces to 0, it wont be removed, instead will be marked as Out Of Stock.
Maximum stock a book cant exceed 9999.
Cant add a book stock directly from search. Stock can be changed only from home page.
Google Books Api is limited to 10 books per search.
Implementation:

Django framework in Python3
SQLlite for database
Deployed in Heroku server
Running instructions:

git clone
pip install -r requirements.txt
python3 manage.py makemigrations book
python3 manage.py migrate
python3 manage.py runserver 8080
Local Home Page: http://127.0.0.1:8080/home/

Heroku Home Page: https://guarded-wave-97929.herokuapp.com/home/
