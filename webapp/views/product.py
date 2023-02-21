from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product, Category


def product_add_view(request):
    if request.method == 'GET':
        context = {'categories': Category.objects.all()}
        return render(request, 'product_add.html', context=context)
    product_data = {
        'name': request.POST.get('name'),
        'category': get_object_or_404(Category, category=request.POST.get('category')),
        'description': request.POST.get('description', None),
        'image': request.POST.get('image'),
        'price': request.POST.get('price')
    }
    product = Product.objects.create(**product_data)
    return redirect(f'/')

def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)