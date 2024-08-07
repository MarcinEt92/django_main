from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.urls import reverse

from .forms import ItemForm
from .helpers.cookie_prices import CookiePrices
from .models import Order, Item, List


def index(request):
    return render(request, "backEndBase/base.html")


def php_tutorial(request):
    return render(request, "backEndBase/extended.html")


def cookies(request):
    context = {
        "buns": CookiePrices.get_cookie_price("buns"),
        "donuts": CookiePrices.get_cookie_price("donuts"),
    }
    return render(request, "cookies/order.html", context)


def process_order(request):
    data = request.POST
    order = Order.objects.create(
        buns=data.get("buns"),
        donuts=data.get("donuts")
    )

    return redirect(reverse("summary", args=(order.id,)))


def summary(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    bun_price = CookiePrices.get_cookie_price("buns")
    donut_price = CookiePrices.get_cookie_price("donuts")
    final_price = order.buns * bun_price + order.donuts * donut_price
    context = {
        "order": order,
        "buns": CookiePrices.get_cookie_price("buns"),
        "donuts": CookiePrices.get_cookie_price("donuts"),
        "final_price": final_price
    }
    return render(request, "cookies/summary.html", context)


def to_do_list(request):
    return render(request, "toDoList/index.html", {"form": ItemForm()})


def specific_list(request, list_id):
    _list = get_object_or_404(List, pk=list_id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST["text"], list=_list)
            return redirect(_list)
    context = {
        "form": form,
        "list": _list
    }
    return render(request, "toDoList/list.html", context)


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        _list = List.objects.create()
        Item.objects.create(text=request.POST["text"], list=_list)
        return redirect(_list)
    else:
        return render(request, "toDoList/index.html", {"form": form})
