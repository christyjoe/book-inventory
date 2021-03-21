# Book Inventor

Features:
1. View number of books avaialble in stock.
2. Update the stock of books.
3. Remove a book from the inventory.
4. Search for any book using Google Books Api.
5. Add a new book to the inventory.

Assumptions:
1. If the stock a book reduces to 0, it wont be removed, instead will be marked as Out Of Stock.
2. Maximum stock a book cant exceed 9999.
3. Cant add a book stock directly from search. Stock can be changed only from home page.
4. Google Books Api is limited to 10 books per search.

Implementation:
1. Django framework in Python3
2. SQLlite for database
3. Deployed in Heroku server

Running instructions:
1. git clone
2. pip install -r requirements.txt
3. python3 manage.py makemigrations book
4. python3 manage.py migrate
5. python3 manage.py runserver 8080

Local Home Page:
http://127.0.0.1:8080/home/

Heroku Home Page:
https://guarded-wave-97929.herokuapp.com/home/
