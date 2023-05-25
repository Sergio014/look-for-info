from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page_view(request, url_path):
    print(Page.objects.all())
    page = get_object_or_404(Page, url_path=url_path)
    if page:
        return render(request, 'index.html', context={'page': page})
    