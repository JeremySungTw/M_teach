from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from . import models
from . import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.forms import formset_factory


# Create your views here.


def hello(request):
    return render(request, 'base.html', locals())


def shop(request):
    shop_obj = models.Shop.objects.all()  # 獲取Shop表所有資料

    if request.method == "GET":
        search = request.GET.get("name", '')
        phone = request.GET.get("phone", '')

        if search and phone:
            shop_obj = shop_obj.filter(name__icontains=search, phone__icontains=phone)
        elif search:
            shop_obj = shop_obj.filter(name__icontains=search)
        elif phone:
            shop_obj = shop_obj.filter(phone__icontains=phone)

        # contact_list = Contacts.objects.all()
        paginator = Paginator(shop_obj, 10)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            shop_obj = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            shop_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            shop_obj = paginator.page(paginator.num_pages)

        return render(request, 'shop/index.html', locals())

    if request.method == "POST":
        pass


def shopcreat(request):
    if request.method == "GET":
        form_obj = forms.ShopForm
        return render(request, 'shop/creat.html', locals())

    if request.method == "POST":
        form_obj = forms.ShopForm(data=request.POST)

        if form_obj.is_valid():
            form_obj.save()
        else:
            print(form_obj.errors)

        return redirect('shop-index')


def shopupdate(request, pk):
    shop_obj = models.Shop.objects.get(id=pk)
    shop_type_obj = shop_obj.type.all()

    ids = ",".join([str(x.id) for x in shop_type_obj])

    type_obj = models.Type.objects.all()

    if request.method == 'GET':
        form_obj = forms.ShopForm(instance=shop_obj)
        # form_type_obj = forms.ShopForm(instance=shop_type)

        return render(request, 'shop/update.html', locals())

    if request.method == 'POST':

        form_obj = forms.ShopForm(instance=shop_obj, data=request.POST)
        print(request.POST)
        # if form_obj.is_valid():
        #     for f in request.POST.getlist('munetype'):
        #         form_obj.changed_data.append(type=f)
        if form_obj.is_valid():
            new_obj = form_obj.save()
            dents = form_obj.cleaned_data.get('type')
            print(dents)
            for dent in dents:
                new_obj.type.add(dent)
        else:
            print(form_obj.errors)

        return redirect('shop-index')


def shopdelete(request, pk):
    shop_obj = models.Shop.objects.get(id=pk)
    shop_obj.delete()

    return HttpResponse("OK")


def order(request):
    order_obj = models.Order.objects.all()  # 獲取Shop表所有資料

    return render(request, 'order/index.html', locals())


def ordercreat(request, pk):
    if request.method == "GET":
        shop_obj = models.Shop.objects.get(id=pk)
        print(shop_obj.id)

        form_obj = forms.OrderForm
        form_obj2 = forms.OrderForm(instance=shop_obj)
        print('form_obj ', form_obj)
        print('form_obj2 ', form_obj2)
        return render(request, 'order/creat.html', locals())

    if request.method == "POST":
        data = request.POST.copy()
        data['shop'] = pk
        form_obj = forms.OrderForm(data=data)

        if form_obj.is_valid():  # 驗證表單

            form_obj.save()
            return redirect('shop-index')
        else:
            print(form_obj.errors)
            return HttpResponse(form_obj.errors)


def orderdetail(request, pk):
    detail_obj = models.Orderdetail.objects.filter(id=pk)

    return render(request, 'order/editorder.html', locals())


def detailcreat(request, pk):
    order_obj = models.Order.objects.filter(id=pk)
    detail_obj = models.Orderdetail.objects.filter(id=pk)

    ord_det_form = forms.OrderdetailForm(pk)

    form_obj = forms.MenuForm
    form_obj = formset_factory(form_obj, extra=3)
    # print(order_obj)
    # print(detail_obj)
    # print(form_obj)
    # print(form_obj2)

    return render(request, 'order/detailcreat.html', locals())
