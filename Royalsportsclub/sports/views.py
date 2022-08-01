from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def home(request):
    home = Product.objects.filter(category='hm')
    context = {
        'home' : home,
    }
    return render(request,'sports/home.html',context)

def aboutus(request):
    return render(request,'sports/aboutus.html')

def buynow(request):
    return render(request,'sports/buynow.html')

def badminton(request):
    badminton = Product.objects.filter(category='bd')
    context = {
        'badminton' : badminton,
    }
    return render(request,'sports/badminton.html',context)

def cricket(request):
    cricket = Product.objects.filter(category='ck')
    context = {
        'cricket' : cricket,
    }
    return render(request,'sports/cricket.html',context)

def football(request):
    football = Product.objects.filter(category='fb')
    context = {
        'football' : football,
    }
    return render(request,'sports/football.html',context)

def basketball(request):
    basketball = Product.objects.filter(category='bb')
    context = {
        'basketball' : basketball,
    }
    return render(request,'sports/basketball.html',context)    

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        context = {
            'form':form
        }
        return render(request, 'sports/customerregisteration.html',context)
        
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"User Registered Sucessfully...")
            form.save()
        context = {
            'form':form
        }
        return render(request, 'sports/customerregisteration.html',context) 

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = len(Cart.objects.filter(user=request.user))
        context = {
            'form' : form,
            'totalitem' : totalitem,
            'active' : 'btn-primary'
        }
        return render(request, 'sports/profile.html',context)
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congrulations. Profile Updated Successfully")
        return render(request, 'sports/profile.html',{'form':form,'totalitem':len(Cart.objects.filter(user=request.user)),'active':'btn-primary'})

@login_required
def add_to_cart(request):
    user = request.user
    #product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=request.GET.get('prod_id'))
    Cart(user=user,product=product).save()
    return redirect("/cart")

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)

        if cart:
            amount = 0.0
            shipping_amount = 70.0
            for p in cart:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount = amount + shipping_amount
            totalitem = len(cart)

            context = {
                'carts' : cart,
                'totalamount' : totalamount,
                'amount' : amount,
                'totalitem' : totalitem
            }    
            return render(request, 'sports/addtocart.html',context)
        else:
            return render(request, 'sports/emptycart.html')  

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print("product id",prod_id)

        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        cart = Cart.objects.filter(user=request.user)

        amount = 0.0
        shipping_amount = 70.0
        for p in cart:
            tempamount =(p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount

        data = {
            "quantity" : c.quantity,
            "amount" : amount,
            "totalamount" : totalamount,
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print("product id",prod_id)

        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        cart = Cart.objects.filter(user=request.user)

        amount = 0.0
        shipping_amount = 70.0
        for p in cart:
            tempamount =(p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount

        data = {
            "quantity" : c.quantity,
            "amount" : amount,
            "totalamount" : totalamount,
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print("product id",prod_id)

        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        cart = Cart.objects.filter(user=request.user)

        amount = 0.0
        shipping_amount = 70.0
        for p in cart:
            tempamount =(p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount

        data = {
            "amount" : amount,
            "totalamount" : totalamount,
        }
        return JsonResponse(data)


class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))

        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        context = {
            'product' : product,
            'item_already_in_cart' : item_already_in_cart,
            'totalitem' : totalitem,
        }
        return render(request, 'sports/product-detail.html',context)

def men_accss(request):
    men_accss = Product.objects.filter(category='ma')
    context = {
        'men_accss' : men_accss,
    }
    return render(request,'sports/men_accss.html',context)

def men_cloth(request):
    men_cloth = Product.objects.filter(category='mc')
    context = {
        'men_cloth' : men_cloth,
    }
    return render(request,'sports/mencloth.html',context)

def men_foot(request):
    men_foot = Product.objects.filter(category='mf')
    context = {
        'men_foot' : men_foot,
    }   
    return render(request,'sports/men_foot.html',context)  

def women_accss(request):
    women_accss = Product.objects.filter(category='wa')
    context = {
        'women_accss' : women_accss,
    }   
    return render(request,'sports/women_accss.html',context)

def women_cloth(request):
    women_cloth = Product.objects.filter(category='wc')
    context = {
        'women_cloth' : women_cloth,
    }   
    return render(request,'sports/women_cloth.html',context)

def women_foot(request):
    women_foot = Product.objects.filter(category='wf')
    context = {
        'women_foot' : women_foot,
    }   
    return render(request,'sports/women_foot.html',context)  

def kids_accss(request):
    kids_accss = Product.objects.filter(category='ka')
    context = {
        'kids_accss' : kids_accss,
    }   
    return render(request,'sports/kids_accss.html',context)

def kids_cloth(request):
    kids_cloth = Product.objects.filter(category='kc')
    context = {
        'kids_cloth' : kids_cloth,
    }   
    return render(request,'sports/kids_cloth.html',context)

def kids_foot(request):
    kids_foot = Product.objects.filter(category='kf')
    context = {
        'kids_foot' : kids_foot,
    }   
    return render(request,'sports/kids_foot.html',context)  

def men_info(request):
    return render(request,'sports/men_info.html')  

def women_info(request):
    return render(request,'sports/women_info.html')

def kids_info(request):
    return render(request,'sports/kids_info.html')

def checkout(request): 
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    totalitem = len(cart_items)
    amount = 0.0
    shipping_amount = 70.0
    for p in cart_items:
        tempamount =(p.quantity * p.product.discounted_price)
        amount += tempamount
    totalamount = amount + shipping_amount
    context = {
        'add' : add,
        'totalamount' : totalamount,
        'totalitem' : totalitem,
        'cart_items' : cart_items,
        'amount' : amount
    }
    return render(request, 'sports/checkout.html',context)

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user = request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    context = {
        'order_placed' : op,
        'totalitem' : totalitem,
    }
    return render(request, 'sports/orders.html',context)

def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')

@login_required
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'sports/address.html',{'add':add,'active':'btn-primary'})