from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.shortcuts import HttpResponse
from testapp.models import Book

# Create your views here.
class Hello(View):
    def get(self,request):
        return HttpResponse('<h1>Hell world </h1>')

class Helloworld(TemplateView):
    template_name = 'testapp/result.html'

class BookListView(ListView):
    model = Book
    template_name = 'testapp/book.html'
    context_object_name = 'List_of_books'
class BookDetailView(DetailView):
    model = Book
