from django.shortcuts import redirect, render
from .forms import SigninForm, SignupForm
from .models import Product,Cart, CartItem
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    productsM = Product.objects.filter(catagory= 1)[:4]
    productsF = Product.objects.filter(catagory= 2)[:4]
    productsC = Product.objects.filter(catagory= 3)[:4]
    productsA = Product.objects.filter(catagory= 4)[:4]
    productsT = Product.objects.filter(catagory= 5)[:4]
    context ={
        'maleproduct':productsM,
        'femaleproduct':productsF,
        'childproduct':productsC,
        'accessoryproduct':productsA,
        'toyProducts':productsT,
    }
    return render(request,'home.html',context)

def contactPage(request):

    return render(request,'contact.html')

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

def menProducts(request):
    productsM = Product.objects.filter(catagory= 1)
    context ={
        'maleproduct':productsM
    }
    return render(request,'mens/menProduct.html',context)

def womenProducts(request):
    productsM = Product.objects.filter(catagory= 2)
    context ={
        'femaleproduct':productsM
    }
    return render(request,'women/womenProduct.html',context)

def childProducts(request):
    productsC = Product.objects.filter(catagory= 3)
    context ={
        'childproducts':productsC
    }
    return render(request,'childs/childsProduct.html',context)

def accessoryProducts(request):
    products = Product.objects.filter(catagory= 4)
    context ={
        'products':products
    }
    return render(request,'accessories/accessories.html',context)

def toyProducts(request):
    products = Product.objects.filter(catagory= 5)
    context ={
        'toyProducts':products
    }
    return render(request,'Toys/toys.html',context)

def productDetails(request,id):
    product = Product.objects.get(id=id)
    return render(request,'productDetails.html',{'product':product})

@login_required
def cartPage(request,):
    cart = request.user.cart
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request,'cart.html',{'cart_items': cart_items})

@login_required
def addToCart(request,id):
    product = Product.objects.get(pk=id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
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

@login_required
def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required
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

@login_required
def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})

@login_required
def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count
