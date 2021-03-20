from django.shortcuts import render
from book.models import Book
from django.views import generic

# Create your views here.
class Inventory(generic.ListView):
	model = Book
	template_name = 'inventory.html'

	def get(self, request):
		books=Book.objects.all()
		return render(request, self.template_name, {'book_list': books})
