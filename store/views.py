from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request, category_slug=None):
    # use category slug to retrieve the corresponding category object
    # assign vanlue to a variable called category_page
    category_page = None
    products = None
    if category_slug !=None:
        category_page = get_object_or_404(Category, slug=category_slug)
        # retieve product objects in DB based on category_pag variable
        # use filter to narrow down the query result based on the category_page parameter
        products = Product.objects.filter(category=category_page, available=True)
    else:
        # display all projects on the home page
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': category_page, 'products': products})
        #  next to to urlpatterns and update it


def productPage(request):
     return render(request, 'product.html')