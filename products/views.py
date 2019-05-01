from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
import operator
# Create your views here.

def home(request):
    products=[]
    for object in Product.objects.all():
        products.append(object)
    sorted_products = sorted(products,key= lambda Product: Product.votes_total, reverse=True)
    return render(request, 'products/home.html',{'sorted_products':sorted_products})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.Title = request.POST['title']
            product.Body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.publish_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+str(product.id))
        else:
            return render(request, 'products/create.html',{'error':'All fields necessary!'})
    else:
        return render(request, 'products/create.html')

def detail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total+=1
        product.save()
        return redirect('/products/'+str(product.id))

@login_required(login_url="/accounts/signup")
def add_comment(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        add_comments = request.POST['text']
        product.commentlist.append(add_comments)
        product.save()
        return redirect('/products/'+str(product.id))
