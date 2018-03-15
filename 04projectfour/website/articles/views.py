from django.views.generic import ListView

# Create your views here.
from .models import Article

class ArticlListView(ListView):
    model = Article
    template_name = 'home.html'
