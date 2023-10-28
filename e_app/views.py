from django.shortcuts import redirect, render
from .forms import SigninForm, SignupForm
from .models import Product,Cart, CartItem
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    productsM = Product.objects.all()[:4]
    context ={
        'productsM':productsM
    }
    return render(request,'home.html',context)

def signupPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Congrates🎉,You have succesfully become a our proud member')
                return redirect('signin')
            else:
                messages.error(request,'There is a invalid fields')
                return redirect('signup')
        else:
            form = SignupForm()
            return render(request,"signup.html",{'form':form})
    else:
        return redirect('home')

def signinPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SigninForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    name =user.first_name +' '+ user.last_name
                    print(name)
                    messages.success(request,"Welcome MR {}".format(name))
                    return redirect('home')
            else:
                messages.error(request,'Invalid username or password')
                return redirect('signin')
        form = SigninForm()
        return render(request,"signin.html",{'form':form})
    else:
        return redirect('home')

def signout(request):
    logout(request)
    return redirect('signin')

def productList(request):
    productsM = Product.objects.all
    context ={
        'productsM':productsM
    }
    return render(request,'mens/menProduct.html',context)

def productDetails(request,id):
    product = Product.objects.get(id=id)
    return render(request,'productDetails.html',{'product':product})

def cartPage(request,):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request,'cart.html',{'cart_items': cart_items})

def addToCart(request,id):
    productList = []
    product = Product.objects.get(pk=id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('productList')

def removeFromCart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})

def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count
