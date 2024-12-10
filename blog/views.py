from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views import View

def main(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {"blogs": blogs})

def detail(request, pk):
    article = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html',{'article':article})


class Detail(View):
    def get(self, request, pk):
        article = get_object_or_404(Blog, pk=pk)
        return render(request, 'detail.html', {'article': article})
    
    def post(request, form=None):
        pass