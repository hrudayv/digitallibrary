from django.shortcuts import render,redirect
from django.http import HttpResponse
from books.models import book
from books.forms import addnew,checkoutb,SearchForm
from django.contrib import messages
from django.core.paginator import Paginator
from django import forms
# Create your views here.
def addbooks(request):
    if request.method == "POST" :
        form = addnew(request.POST or None)
        #print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request,("New Book added successfully!!!"))
        else:
            messages.success(request,("Couldnt add Book :/"))
        return redirect('addbooks')

    else:
        allbooks = book.objects.order_by('booknum')
        paginator = Paginator(allbooks,20)
        page = request.GET.get('pg')
        allbooks = paginator.get_page(page)

        return render(request,'addbooks.html',{'allbooks': allbooks})

def checkout1(request):
    if request.method=="POST":
        form = checkoutb(request.POST or None)
        if form.is_valid():
            b=form.cleaned_data['booknum']
            c=form.cleaned_data['noc']
            bookchan = book.objects.get(booknum=b)
            if bookchan.stockavail >= c:
                bookchan.stockavail = bookchan.stockavail - c
                bookchan.save(update_fields=['stockavail'])
                messages.success(request,("Checkedout Successfully!!!"))
                return redirect('checkout')
            else:
                messages.success(request,("Couldn't Checkout!!!"))
                return redirect('checkout')
        else:
            ViewBooks=book.objects.order_by('booknum')
            paginator = Paginator(ViewBooks,20)
            page = request.GET.get('pg')
            ViewBooks = paginator.get_page(page)
            return render(request,'studentview.html',{'ViewBooks': ViewBooks})

    else:
        ViewBooks=book.objects.order_by('booknum')
        paginator = Paginator(ViewBooks,20)
        page = request.GET.get('pg')
        ViewBooks = paginator.get_page(page)
        return render(request,'studentview.html',{'ViewBooks': ViewBooks})


def checkout(request):
    objects1=book.objects.order_by('booknum')
    paginator = Paginator(objects1,20)
    page = request.GET.get('pg')
    objects1 = paginator.get_page(page)
    context = {
    'checkoutext':'Welcome to Checkout Page',
    'objects2': objects1,
    }
    return render(request,'checkout.html',context)

def returnbooks1(request):
    if request.method=="POST":
        form = checkoutb(request.POST or None)
        if form.is_valid():
            b=form.cleaned_data['booknum']
            c=form.cleaned_data['noc']
            bookchan = book.objects.get(booknum=b)
            bookchan.stockavail = bookchan.stockavail + c
            bookchan.save(update_fields=['stockavail'])
            messages.success(request,("Returned Successfully!!!"))
            return redirect('returnbooks')
        else:
            ViewBooks=book.objects.order_by('booknum')
            paginator = Paginator(ViewBooks,20)
            page = request.GET.get('pg')
            ViewBooks = paginator.get_page(page)
            return render(request,'studentview.html',{'ViewBooks': ViewBooks})

    else:
        ViewBooks=book.objects.order_by('booknum')
        paginator = Paginator(ViewBooks,20)
        page = request.GET.get('pg')
        ViewBooks = paginator.get_page(page)
        return render(request,'studentview.html',{'ViewBooks': ViewBooks})




def returnbooks(request):
    objects1=book.objects.order_by('booknum')
    paginator = Paginator(objects1,20)
    page = request.GET.get('pg')
    objects1 = paginator.get_page(page)
    context = {'returnbookstext':'Welcome to Return Page','objects2': objects1,}
    return render(request,'return.html',context)


def viewbooks(request):

    if request.method=="GET":
        query = request.GET.get('q')
        print(type(query))
        if query:
            a = book.objects.filter(bookname__icontains=query)
            b = book.objects.filter(authorname__icontains=query)
            if hasNumbers(query):
                c = book.objects.get(booknum = int(query))
                d = book.objects.filter(booknum__icontains=c.booknum)
                ViewBooks = a|b|d
            else:
                ViewBooks = a|b

        else:
            ViewBooks=book.objects.order_by('booknum')
            paginator = Paginator(ViewBooks,20)
            page = request.GET.get('pg')
            ViewBooks = paginator.get_page(page)

    return render(request,'studentview.html',{'ViewBooks': ViewBooks})

def removebooks(request,book_num):
    rb = book.objects.get(booknum=book_num)
    rb.delete()
    return redirect('addbooks')

def viewbooks2(request):

    if request.method=="GET":
        query = request.GET.get('q')
        print(type(query))
        if query:
            a = book.objects.filter(bookname__icontains=query)
            b = book.objects.filter(authorname__icontains=query)
            if hasNumbers(query):
                c = book.objects.get(booknum = int(query))
                d = book.objects.filter(booknum__icontains=c.booknum)
                ViewBooks = a|b|d
            else:
                ViewBooks = a|b

        else:
            ViewBooks=book.objects.order_by('booknum')
            paginator = Paginator(ViewBooks,20)
            page = request.GET.get('pg')
            ViewBooks = paginator.get_page(page)

    return render(request,'studentview2.html',{'ViewBooks': ViewBooks})


def hasNumbers(inputString):
    c = len(inputString)
    d : int = 0
    for char in inputString:
        if char.isdigit():
            d = d + 1
    if d == c :
        return True
    else:
        return False
