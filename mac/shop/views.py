from django.shortcuts import render
from django.http import HttpResponse
import math
# Now Using database import
from .models import Product,CustomerQuery

# Create your views here.
def index(request):
# ACCESSING THE DATABASE ALL THE PRODUCTS

    allProd=[]
    prod_catogery=Product.objects.values('product_catogery','id')
    cats = { items['product_catogery'] for items in prod_catogery}
    for cat in cats:
        prod=Product.objects.filter(product_catogery=cat)
        n=len(prod)
        nSlides=n//4+math.ceil(n/4-n//4)
        allProd.append([prod,range(1,nSlides),nSlides])


    params={'all_prod':allProd}
   # print(prod)
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name',default="")
        phone=request.POST.get('phone',default="")
        email=request.POST.get('email',default="")
        query=request.POST.get('query',default="")
        data=CustomerQuery(cust_name=name,cust_phone=phone,cust_email=email,cust_query=query)
        data.save()
        

    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def productView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/prodview.html',{'product':product[0]})
def checkout(request):
    return render(request,'shop/checkout.html')


