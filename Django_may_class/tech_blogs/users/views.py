from django.shortcuts import render
from .models import Account, Category, Post
# Create your views here.
def home(request):
    account = Account.objects.prefetch_related('post')
    category = Category.objects.select_related('post_category').select_related("account")
    post = Post.objects.select_related('author').order_by('-created_at')

    return render(request, 'index.html', {"accounts": account, "posts": post, "categories": category})
