from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import User, Customer, Product, Cart, OrderPlaced
from .forms import CustomerForm
from .forms import RegistrationForm
from django.contrib import messages
from django.http import JsonResponse

class ProductView(View):
    def get(self, request):

        all_products =  Product.objects.get(id=1)




        print("----------------------------------------------")
        data = all_products.__dict__
        print(data, "+++++++++++++++++++++++")
        updated = data.get('pg', 'jjjjjjjjjjjjjjjjjjjjjj')
        
        print(data, "*********************")
        







        electronics = Product.objects.filter(Q(category ="m") | Q(category="l"))
        topwears = Product.objects.filter(category="tw")
        bottomwears = Product.objects.filter(category="bw")



        return render(request, 'app/home.html', {'electronics':electronics, 'topwears':topwears, 'bottomwears':bottomwears})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'app/productdetail.html', {'product':product})


def electronics(request, data = None):
    if data == None:
        electronicsdata = Product.objects.filter(Q(category='m') | Q(category='l'))
    elif data == 'mobile':
        electronicsdata = Product.objects.filter(category='m')    
    elif data == 'laptop':
        electronicsdata = Product.objects.filter(category='l')    
    elif data == 'samsung':
        electronicsdata = Product.objects.filter(brand='samsung')    
    elif data == 'lenovo':
        electronicsdata = Product.objects.filter(brand='lenovo')    
    elif data == 'less':
        electronicsdata = Product.objects.filter(discount_price__lt = 20000)    
    elif data == 'greater':
        electronicsdata = Product.objects.filter(discount_price__gt = 20000)
    else:
        electronicsdata = Product.objects.all()    
    return render(request, 'app/electronics.html', {'electronics': electronicsdata})



class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
        
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registeration Successfull !!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})
        

class Profile(View):

    def get(self, request):
        form = CustomerForm() 
        return render(request, 'app/profile.html', {'form':form, 'pactive':'btn-primary'})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name'] 
            locality = form.cleaned_data['locality'] 
            city = form.cleaned_data['city'] 
            zipcode = form.cleaned_data['zipcode'] 
            state = form.cleaned_data['state'] 
            reg = Customer(user= user,name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            messages.success(request, 'Your profile Updated with New address !!')
            reg.save()
        return render(request, 'app/profile.html', {'form':form, 'pactive':'btn-primary'})


class  Address(View):
    def get(self, request):
        address = Customer.objects.filter(user=request.user)
        return render(request, 'app/address.html', {'address':address, 'aactive':'btn-primary'})



def add_to_cart(request, pk=None):
    if pk:
        product = Product.objects.get(id=pk)
        item = Cart(user=request.user, product=product)
        item.save()
    return render(request, 'app/addtocart.html')

def show_cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user= request.user)
        products_amount= sum([item.product.discount_price for item in cart_items])
        shipping_amount = 70
        total_amount = products_amount + shipping_amount
        return render(request, 'app/addtocart.html', {'cart_items': cart_items,'shipping_amount':shipping_amount, 'products_amount': products_amount, 'total_amount': total_amount })
    else:
        return render(request, 'app/addtocart.html')


def plus_cart(request):    
    print("----------------------")
    if request.method == 'GET':
        id = request.GET['prod_id']
        cart_item = Cart.objects.get(Q(product=id) & Q(user=request.user))
        print("++++++++++++++++", cart_item)
        cart_item.quantity +=1 
        cart_item.save()

    cart_items = Cart.objects.filter(Q(user= request.user) & Q(user=request.user))
    products_amount= sum([item.product.discount_price for item in cart_items])
    shipping_amount = 70
    total_amount = products_amount + shipping_amount
    print("++++++++++++++++++++++++++++++++")
    data = {
            'quantity':cart_item.quantity,
            'products_amount': products_amount,
            'total_amount': total_amount 
            }
    return JsonResponse(data)




def buy_now(request):
 return render(request, 'app/buynow.html')


def orders(request):
 return render(request, 'app/orders.html')



def checkout(request):
 return render(request, 'app/checkout.html')
