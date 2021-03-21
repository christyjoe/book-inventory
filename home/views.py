from django.shortcuts import render
from django.forms import ValidationError
from book.models import Book
from django.views import generic
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import CountForm, SearchForm, AddForm
from django import forms
import requests
import json

class Inventory(generic.ListView):
	def get(self, request):
		form=SearchForm
		books=Book.objects.all()
		for i in books:
			if i.count==0:
				i.count = "Out of stock"
		return render(request, 'inventory.html', {'book_list': books})

	def post(self, request):
		form = SearchForm(request.POST)
		print ('Entering in')
		if form.is_valid():
			print ('Exiting out')
			searchtext = form.cleaned_data['searchField']
			return redirect('search/' + searchtext)

		else:
			print ("Printing errors")
			print (form.errors)
		return HttpResponse("No Books Found", status= 401)


class InventorySearch(generic.TemplateView):
	def googleBookAPI(self, searchtext):
		googleapikey = "AIzaSyDgyKmKc1KTpHh8p23jnTOHd-c7LLR4ox8"
		parms = {"q":searchtext, 'key':googleapikey}
		r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
		my_json = r.json()
		bookIds = []
		pos = 0
		booksMap = {}
		for i in my_json["items"]:
			searchBook = {}
			searchBook["title"] = i['volumeInfo']["title"]
			searchBook["google_book_id"] = i['id']
			try:
			    searchBook["thumbnail"] = i['volumeInfo']["imageLinks"]["thumbnail"]
			except:
			    searchBook["thumbnail"] = '#'
			searchBook["count"] = "Not available"
			searchBook["showAdd"] = True
			bookIds.append(i['id'])
			self.searchBooks.append(searchBook)
			booksMap[i['id']] = pos
			pos += 1
		checkBooks = Book.objects.filter(google_book_id__in=bookIds)
		for i in checkBooks:
			self.searchBooks[booksMap[i.google_book_id]]["showAdd"] = False
			self.searchBooks[booksMap[i.google_book_id]]["count"] = i.count
			if(i.count==0):
				self.searchBooks[booksMap[i.google_book_id]]["count"] = "Out of stock"

	def get(self, request, gref):
		self.searchBooks = []
		try:
			self.googleBookAPI(gref)
		except:
			return HttpResponse("No Books Found", status= 401)
		return render(request, 'inventory_search.html', {'book_list':self.searchBooks})


class InventoryAdd(generic.TemplateView):

	def __init__(self):
		self.addBook = {}

	def fetchBook(self, gid):
		r = requests.get(url="https://www.googleapis.com/books/v1/volumes/" + gid)
		my_json = r.json()
		if(my_json):
			self.addBook["title"] = my_json['volumeInfo']["title"]
			self.addBook["google_book_id"] = my_json['id']
			try:
				self.addBook["thumbnail"] = my_json['volumeInfo']["imageLinks"]["thumbnail"]
			except:
				self.addBook["thumbnail"] = '#'

	def get(self, request, gid):
		self.fetchBook(gid)
		form=AddForm
		return render(request, 'inventory_add.html', {'form':form, 'book':self.addBook})

	def post(self, request, gid):
		form = AddForm(request.POST)
		self.fetchBook(gid)
		if form.is_valid():
			count=form.cleaned_data['count']
			if (count<0 or 9999<count):
				raise forms.ValidationError("Invalid stock. Please check ")
			book = Book()
			book.title = self.addBook['title']
			book.count = count
			book.google_book_id = self.addBook['google_book_id']
			book.thumbnail = self.addBook['thumbnail']
			book.save()
		return redirect('home')


class InventoryUpdate(generic.TemplateView):
	def get(self, request, id):
		book=Book.objects.get(pk=id)
		form=CountForm
		return render(request, 'inventory_update.html', {'form':form, 'book':book})

	def post(self, request, id):
		form= CountForm(request.POST)
		if form.is_valid():
			count=form.cleaned_data['count']
			if (count<0 or 9999<count):
				raise forms.ValidationError("Invalid stock. Please check ")
			book=Book.objects.get(pk=id)
			book.count = count
			book.save()
		return redirect('home')


class InventoryRemove(generic.TemplateView):
	def get(self, request, id):
		book=Book.objects.get(pk=id)
		return render(request, 'inventory_remove.html', {'book':book})

	def post(self, request, id):
		if 'yes' in request.POST:
			book=Book.objects.get(pk=id)
			book.delete()
		return redirect('home')
