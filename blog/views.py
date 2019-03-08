from django.shortcuts import render

posts = [
    {
        'author': 'AlanT',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 8, 2019'
    },
    {
        'author': 'JaneD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 9, 2019'
    },
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
