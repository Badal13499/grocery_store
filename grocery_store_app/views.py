from django.views import View
from .models import Customer, Item_data
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    if request.method == 'POST':
        key = request.POST.get('key_value')
        print(request.POST)
        data = Item_data.objects.get(key = key)
        data.delete()
        name = request.POST.get('name')
        quantity = request.POST.get('quant')
        status = request.POST.get('stat')
        date = request.POST.get('date')

        item = Item_data(key=key,customer=request.session['email'], item_name=name, item_quantity=quantity, item_status=status,
                         date=date)
        item.save()
        return redirect('index')

    items = Item_data.objects.filter(customer = request.session['email'])
    context = {
        'items': items
    }
    if items is None:
        return render(request, 'index.html', context)
    else:
        return render(request,'index.html', context)


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        date = request.POST.get('date')
        item = Item_data(customer=request.session['email'],item_name = name, item_quantity = quantity,item_status = status, date = date)
        item.save()
    return redirect('index')


def update(request):
    if request.method == 'POST':
        key = request.POST.get('key_value')
        data = Item_data.objects.get(key=key)
        context = {
            'data': data
        }
        return render(request,'update.html', context)


class Register(View):
    def get(self, request):
        return render(request,'register.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')

        value = {'fname': fname, 'lname': lname, 'phone': phone, 'email': email}

        if password == conpassword:
            customer = Customer(fname=fname, lname=lname, phone=phone, email=email, password=password)
            if customer.isExists():
                error_msg = "Email already registered"
                return render(request, 'register.html', {'flag': error_msg, 'value': value})
            else:
                customer.password = make_password(customer.password)
                customer.register()
                return redirect('login')

        else:
            error_msg = "Password does not match"
            return render(request, 'register.html', {'flag': error_msg, 'value': value})


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer.getCustomerByEmail(email)
        if customer:
            if check_password(password,customer.password):
               request.session['customer_id'] = customer.id
               request.session['email'] = customer.email

               if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
               else:
                   Login.return_url = None
                   return redirect('index')
            else:
                error_msg = "Email or Password invalid!!"
        else:
            error_msg = "Email or Password invalid!!"
        return render(request, 'login.html', {'flag':error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')


def delete(request):
    if request.method == 'POST':
        key = request.POST.get('key_value')
        print(request.POST)
        data = Item_data.objects.get(key = key)
        data.delete()
        return redirect('index')


def filter(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        date = request.POST.get('date')
        if flag:
            data = Item_data.objects.all()
            context = {
                'items': data
            }
            return render(request, 'index.html', context)
        else:

            data = Item_data.objects.filter(date = date)
            context = {
                'items': data
            }
            return render(request,'index.html', context)