from django.shortcuts import render,redirect
from Books.models import CategoryDB, BookDB, UpcomeBk
from Webbooks.models import Checkout, CartDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(arg):
    order=Checkout.objects.all()
    che=CartDB.objects.all()
    return render(arg, 'index.html', {'order':order, 'che':che})

def addcategory(arg):
    return render(arg, 'addcategory.html')

def savecategory(arg):
    if arg.method=='POST':
        cnme=arg.POST.get('c_name')
        cdes=arg.POST.get('b_description')
        cima=arg.FILES['c_image']
        obj=CategoryDB(c_name=cnme, c_description=cdes, c_img=cima)
        obj.save()
        return redirect(addcategory)

def categorylist(arg):
    data=CategoryDB.objects.all()
    return render(arg, 'categorylist.html', {'data':data})

def editcategory(arg, dataid):
    data=CategoryDB.objects.get(id=dataid)
    lists=CategoryDB.objects.all()
    return render(arg, 'editcategory.html', {'data':data, 'lists':lists})

def updatecategory(arg, dataid):
    if arg.method=='POST':
        cnme = arg.POST.get('c_nme')
        cdes = arg.POST.get('b_description')
        try:
            cima = arg.FILES['c_image']
            fs=FileSystemStorage()
            file=fs.save(cima.name, cima)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=dataid).c_img

        CategoryDB.objects.filter(id=dataid).update(c_name=cnme, c_description=cdes, c_img=file)
        return redirect(categorylist)

def categorydelete(arg, dataid):
    data=CategoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(categorylist)

def loginpage(arg):
    return render(arg, 'loginpage.html')

def logindatas(arg):
    if arg.method=='POST':
        unme=arg.POST.get('username')
        pwd=arg.POST.get('password')
        if User.objects.filter(username__contains=unme).exists():
            user=authenticate(username=unme, password=pwd)
            if user is not None:
                login(arg, user)
                arg.session['username']=unme
                arg.session['password']=pwd
                return redirect(index)
            else:
                return redirect(index)
        else:
            return redirect(index)


def logutpage(arg):
    del arg.session['username']
    del arg.session['password']
    return redirect(loginpage)

def addbooks(arg):
    data=CategoryDB.objects.all()
    return render(arg, 'addbooks.html', {'data': data} )

def savebook(arg):
    if arg.method=='POST':
        b_cat=arg.POST.get('c_nme')
        b_nme=arg.POST.get('b_name')
        b_pri=arg.POST.get('b_price')
        b_desc=arg.POST.get('b_description')
        b_aut=arg.POST.get('b_auther')
        b_aut_desc=arg.POST.get('b_auther_descri')
        b_cov=arg.FILES['b_image']
        obj=BookDB(b_category=b_cat, b_name=b_nme, b_price=b_pri, b_description=b_desc, b_auther=b_aut, b_auth_desc=b_aut_desc, b_cover=b_cov )
        obj.save()
        return redirect(addbooks)


def booklist(arg):
    data=BookDB.objects.all()
    return render(arg, 'booklist.html', {'data':data})

def editbook(arg, dataid):
    lists = CategoryDB.objects.all()
    data=BookDB.objects.get(id=dataid)
    return render(arg, 'editbook.html', {'lists':lists, 'data':data})

def updatebook(arg, dataid):
    if arg.method=='POST':
        b_cat = arg.POST.get('c_nme')
        b_nme = arg.POST.get('b_name')
        b_pri = arg.POST.get('b_price')
        b_desc = arg.POST.get('b_description')
        b_aut = arg.POST.get('b_auther')
        b_aut_desc = arg.POST.get('b_auther_descri')
        try:
            b_cov = arg.FILES['b_image']
            fs = FileSystemStorage()
            file = fs.save(b_cov.name, b_cov)
        except MultiValueDictKeyError:
            file = BookDB.objects.get(id=dataid).b_cover
        BookDB.objects.filter(id=dataid).update(b_category=b_cat, b_name=b_nme, b_price=b_pri, b_description=b_desc, b_auther=b_aut, b_auth_desc=b_aut_desc, b_cover=file)
        return redirect(booklist)


def Bookdelete(arg, dataid):
    data=BookDB.objects.filter(id=dataid)
    data.delete()
    return redirect(booklist)


def upcommingbooks(arg):
    return render(arg, 'upcommingbooks.html')

def saveupcomebk(arg):
    if arg.method=='POST':
        b_nme=arg.POST.get('b_name')
        b_desc=arg.POST.get('b_description')
        b_cov=arg.FILES['b_image']
        obj=UpcomeBk(bk_nme=b_nme, bk_des=b_desc, bk_cov=b_cov)
        obj.save()
        return redirect(upcommingbooks)


