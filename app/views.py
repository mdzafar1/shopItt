from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerprofileForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptop': laptop})




class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')




def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'iQOO' or 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Google' or 'APPLE':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'OnePlus':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=40000)
    elif data == 'above':        
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=60000)

    return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data=None):
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'Dell' or 'Mi':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'lenovo' or 'accer':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    # elif data == 'OnePlus':
    #     mobiles = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptop = Product.objects.filter(
            category='L').filter(discounted_price__lt=50000)
    elif data == 'above':        
        laptop = Product.objects.filter(
            category='L').filter(discounted_price__gt=50000)

    return render(request, 'app/laptop.html', {'laptop': laptop})

def topwear(request, data=None):
    if data == None:
        topwear = Product.objects.filter(category='TW')
    elif data == 'levis' or 'leecopper':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'wranglar' or 'spyker':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'pappejeans':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwear = Product.objects.filter(
            category='T').filter(discounted_price__lt=50000)
    elif data == 'above':        
        topwear = Product.objects.filter(
            category='T').filter(discounted_price__gt=50000)

    return render(request, 'app/topwear.html', {'topwear': topwear})

def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'levis' or 'leecopper':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'wranglar' or 'spyker':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'pappejeans':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'below':
        bottomwear = Product.objects.filter(
            category='T').filter(discounted_price__lt=50000)
    elif data == 'above':        
        bottomwear = Product.objects.filter(
            category='T').filter(discounted_price__gt=50000)

    return render(request, 'app/bottomwear.html', {'bottomwear': bottomwear})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request,'app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerprofileForm()
        return render(request, 'app/profile.html', {'form':form, 
        'active':'btn-primary'})

    def post(self, request):
        form = CustomerprofileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']   
            locality = form.cleaned_data['locality']    
            city= form.cleaned_data['city']    
            state = form.cleaned_data['state']    
            zipcode = form.cleaned_data['zipcode']    
            reg = Customer(name=name, locality=locality, city=city,
            state=state, zipcode=zipcode ) 