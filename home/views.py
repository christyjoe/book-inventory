from django.shortcuts import render
from django.forms import ValidationError
from book.models import Book
from django.views import generic
from django.shortcuts import redirect
from .forms import CountForm
from django import forms

class Inventory(generic.ListView):
	model = Book

	def get(self, request):
		books=Book.objects.all()
		return render(request, 'inventory.html', {'book_list': books})

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
