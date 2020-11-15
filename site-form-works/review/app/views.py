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
    text = Review.objects.select_related('product')
    form = ReviewForm
    if request.method == 'POST' and ('is_review_exist' not in request.session):
        # логика для добавления отзыва
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            comment = review_form.save(commit=False)
            comment.product = Product.objects.get(id=pk)
            review_form.save()
            request.session.set_expiry(60)
            request.session['is_review_exist'] = True
    is_review_exist = request.session.get('is_review_exist')
    context = {
        'form': form,
        'product': product,
        'reviews': text,
        'is_review_exist': is_review_exist
    }
    return render(request, template, context)
