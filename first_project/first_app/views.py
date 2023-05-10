from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
# 'request' name is convention. It can be some other name too.

from first_app import views

clicked = 1
def index(request) :
  fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
  my_dict = { 'fruit_list': fruits }
  return render(request, 'index.html', my_dict)

def help(request):
  return render(request, 'help.html')