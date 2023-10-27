from django.shortcuts import render

from e_app.models import MenProduct

# Create your views here.
def home(request):
    productsM = MenProduct.objects.all()[:4]
    context ={
        'productsM':productsM
    }
    return render(request,'home.html',context)

def menProduct(request):
    productsM = MenProduct.objects.all
    context ={
        'productsM':productsM
    }
    return render(request,'mens/menProduct.html',context)

def productDetails(request,id):
    product = MenProduct.objects.get(id=id)
    return render(request,'productDetails.html',{'product':product})