from django.shortcuts import render
from django.forms import ValidationError
from book.models import Book
from django.views import generic
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import CountForm, SearchForm
from django import forms
import json

class Inventory(generic.ListView):
	def get(self, request):
		form=SearchForm
		books=Book.objects.all()
		return render(request, 'inventory.html', {'book_list': books})

	def post(self, request):
		form = SearchForm(request.POST)
		print ('Entering in')
		if form.is_valid():
			print ('Exiting out')
			searchtext = form.cleaned_data['search']
		else:
			print ("Printing errors")
			print (form.errors)
		return HttpResponse("No Books Found" ++ searchtext, status= 401)

	
	def googleBookAPI(self, searchtext):
		googleapikey = "AIzaSyA7sWY6q7S4-xyZ1edjWtELkVa88dziU6Q"
		parms = {"q":searchtext, 'key':googleapikey}
		searchBooks = []
		try:
			r = requests.get(url="https://www.googleapis.com/books/v1/volumes?q=searchtext&key=googleapikey")
			my_json = r.json()
			for i in my_json["items"]:
				searchBook = {}
				searchBook.title = i['volumeInfo']['title']
				searchBook.previewLink = i["volumeInfo"]["previewLink"]
				try:
				    searchBook.imageThumbnail = i['volumeInfo']["imageLinks"]["thumbnail"]
				except:
				    searchBook.imageThumbnail = '#'
				searchBooks.append(searchBook)
		except:
			searchBooks = []
		return searchBooks





class InventorySearch(generic.TemplateView):
	def get(Self, request, gref):
		# Google api
		return redirect('home')



class InventoryUpdate(generic.TemplateView):
	def get(Self, request, id):
		book=Book.objects.get(pk=id)
		form=CountForm
		return render(request, 'inventory_update.html', {'form':form, 'book':book})

	def post(self, request, id):
		form= CountForm(request.POST)
		if form.is_valid():
			count=form.cleaned_data['count']
			if (count<1 or 9999<count):
				raise forms.ValidationError("Invalid stock. Please check ")
			book=Book.objects.get(pk=id)
			book.count = count
			book.save()
		return redirect('home')


class InventoryRemove(generic.TemplateView):
	def get(Self, request, id):
		book=Book.objects.get(pk=id)
		return render(request, 'inventory_remove.html', {'book':book})

	def post(self, request, id):
		if 'yes' in request.POST:
			book=Book.objects.get(pk=id)
			book.delete()
		return redirect('home')
