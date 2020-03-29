from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_phone = request.GET.get('sort')
    query = Phone.objects.all()
    if sort_phone == 'name':
        query = query.order_by('name')
    elif sort_phone == 'min_cost':
        query = query.order_by('price')
    elif sort_phone == 'max_cost':
        query = query.order_by('price')[::-1]
    context = {"Phones": query}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    query = Phone.objects.get(slug=slug)
    context = {'Phone': query}
    return render(request, template, context)
