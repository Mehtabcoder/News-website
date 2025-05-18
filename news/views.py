

# Create your views here.

from django.shortcuts import render
from .models import NewsArticle

def homepage(request):
    print("Homepage view called!")  # <- Add this
    articles = NewsArticle.objects.order_by('-created_at')[:10]
    return render(request, 'news/homepage.html', {'articles': articles})

from django.shortcuts import render, get_object_or_404

def article_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})


