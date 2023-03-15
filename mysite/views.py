from django.shortcuts import render
from mysite.models import Product,Customer

# Create your views here.
def index(request):
    customer = Customer.objects.all #Select * from customers
    my_dict = {'customers':customer}
    return render(request, 'index.html', context=my_dict)
    
