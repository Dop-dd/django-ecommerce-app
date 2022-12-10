"""
So in order to enable the category link we need to create the context processors file in that file we
can create functions that are used to populate the context when a template is rendered with a request
A context processor is just a python function that takes one argument which is an HTTP Request object.
Each context processor function must return dictionary and it will be available anywhere in your code
Here in the menu links function we return all categories from the database and name links so that we
can use it in our home page.
"""
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links) # make sure context processor is already added in setings