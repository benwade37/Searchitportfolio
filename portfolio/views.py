from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, PortfolioItem, Tag


def home(request):
    query = request.GET.get('q', '').strip()
    category_filter = request.GET.get('category', '').strip()
    tag_filter = request.GET.get('tag', '').strip()

    items = PortfolioItem.objects.select_related('category').prefetch_related('tags')

    if query:
        items = items.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(tags__name__icontains=query)
            | Q(category__name__icontains=query)
        ).distinct()

    if category_filter:
        items = items.filter(category__name=category_filter)

    if tag_filter:
        items = items.filter(tags__name=tag_filter)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'items': items,
        'query': query,
        'category_filter': category_filter,
        'tag_filter': tag_filter,
        'categories': categories,
        'tags': tags,
        'total_results': items.count(),
    }
    return render(request, 'portfolio/home.html', context)


def item_detail(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    related = (
        PortfolioItem.objects.filter(category=item.category)
        .exclude(pk=pk)
        .select_related('category')
        .prefetch_related('tags')[:3]
    )
    context = {
        'item': item,
        'related': related,
    }
    return render(request, 'portfolio/item_detail.html', context)
