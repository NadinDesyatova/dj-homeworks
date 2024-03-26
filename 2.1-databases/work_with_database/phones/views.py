from operator import itemgetter
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    # phone_objects = Phone.objects.all()
    # phones = [
    #     {
    #         'name': p.name,
    #         'slug': p.slug,
    #         'image': p.image,
    #         'price': p.price
    #     }
    #     for p in phone_objects
    # ]

    # sort_parameter = request.GET.get("sort")

    # if sort_parameter is not None:
    #     if 'min' in sort_parameter:
    #         phones.sort(key=itemgetter('price'))
    #     elif 'max' in sort_parameter:
    #         phones.sort(key=itemgetter('price'), reverse=True)
    #     else:
    #         phones.sort(key=itemgetter('name'))

    phones = Phone.objects.all()

    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    sort = request.GET.get('sort')
    if sort is not None:
        phones = phones.order_by(SORT_MAP[sort])

    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    current_phone = Phone.objects.filter(slug__contains=slug).first()
    context = {
        'phone': current_phone
    }
    return render(request, template, context)


