from django.shortcuts import render, redirect
from Books.models import CategoryDB, BookDB, UpcomeBk
from Webbooks.models import UserDB,CartDB, Checkout
# Create your views here.
def homepage(arg):
    cat=CategoryDB.objects.all()
    up=UpcomeBk.objects.all()
    return render(arg, 'homepage.html', {'cat':cat, 'up':up })

def products(arg,cat_nme):
    data=CategoryDB.objects.filter(c_name=cat_nme)
    prod=BookDB.objects.filter(b_category=cat_nme)
    return render(arg, 'product.html', {'data':data, 'prod':prod})


def singleproduct(arg, dataid):
    data=BookDB.objects.get(id=dataid)
    pro=BookDB.objects.filter(b_category=dataid)
    return render(arg, 'singleproduct.html', {'data':data, 'pro':pro})

def reg_login(arg):
    return render(arg, 'reg_login.html')


def usersignin(arg):
    if arg.method=='POST':
        u_nme=arg.POST.get('usernme')
        u_email=arg.POST.get('email')
        u_mobile=arg.POST.get('mob')
        u_pass=arg.POST.get('passwd')
        u_pro=arg.FILES['p_img']
        obj=UserDB(UserName=u_nme, EmailId=u_email, Mobile=u_mobile, PassWord=u_pass, UserImage=u_pro)
        obj.save()
        return redirect(reg_login)

def loginprocess(arg):
    if arg.method=='POST':
        u_nme=arg.POST.get('unme')
        u_pass=arg.POST.get('passwd')
        if UserDB.objects.filter(UserName=u_nme, PassWord=u_pass).exists():
            arg.session['UserName']=u_nme
            arg.session['PassWord']=u_pass
            return redirect(homepage)
        else:
            return redirect(reg_login)

    else:
        return redirect(reg_login)


def logutpage(arg):
    del arg.session['UserName']
    del arg.session['PassWord']
    return redirect(homepage)

def cart(arg):
    crt = CartDB.objects.filter(Username=arg.session['UserName'])
    return render(arg, 'cart.html', {'crt':crt})

def savecart(arg):
    if arg.method=='POST':
        uname=arg.POST.get('unme')
        pnme=arg.POST.get('bnme')
        au_nme=arg.POST.get('auther')
        qty=arg.POST.get('quty')
        pri=arg.POST.get('tlprice')
        obj=CartDB(Username=uname, pro_name=pnme, aut_name= au_nme, Qty=qty, price=pri)
        obj.save()
        return redirect(cart)

def cartdelete(arg, dataid):
    data=CartDB.objects.filter(id=dataid)
    data.delete()
    return redirect(cart)

def checkout(arg):
    crt = CartDB.objects.filter(Username=arg.session['UserName'])
    return render(arg, 'checkout.html', {'crt':crt})


def storecheckout(arg):
    if arg.method == 'POST':
        nme = arg.POST.get('firstname')
        ema = arg.POST.get('email')
        add = arg.POST.get('address')
        cit = arg.POST.get('city')
        sta = arg.POST.get('state')
        sip = arg.POST.get('zip')
        cna = arg.POST.get('cardname')
        cnm = arg.POST.get('cardnumber')
        exp = arg.POST.get('expmonth')
        exy = arg.POST.get('expyear')
        evv = arg.POST.get('cvv')
        obj = Checkout(name=nme, email=ema, address=add, city=cit, State=sta, zip= sip, c_name= cna, c_number= cnm,exp_month= exp, exp_yer=exy, cvv=evv)
        obj.save()
        return redirect(homepage)






