from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    text = Review.objects.select_related('product').filter(product=pk)
    form = ReviewForm
    if not request.session.get('is_review_exists'):
        request.session['is_review_exists'] = []
    if request.method == 'POST' and (pk not in request.session.get('is_review_exists')):
        # логика для добавления отзыва
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            comment = review_form.save(commit=False)
            comment.product = product
            review_form.save()
            request.session['is_review_exists'].append(pk)
            request.session.modified = True
    if pk in request.session.get('is_review_exists'):
        is_exist = True
    else:
        is_exist = False
    context = {
        'form': form,
        'product': product,
        'reviews': text,
        'is_review_exist': is_exist
    }
    return render(request, template, context)
