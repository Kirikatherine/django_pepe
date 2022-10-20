from pydoc_data.topics import topics
from django.shortcuts import render
from .models import Topic, Category
from django.contrib.auth.models import User

def get_all_topics(request):
    all_topics = Topic.objects.all()
    allowed_viewer = User.object.get(pk=1)
    greetings = [
        'hallo',
        'welcome', 
    ]
    simple_html_el = "<h1>Zagolovok</h1>"
    return render(request, 'blog/all_topics.html', {'all_topics': all_topics})


def get_topics_by_category(request, category):
    try: #electronics
        asked_category = Category.objects.get(title=category)
        topics_by_category = Topic.objects.filter(category=asked_category)
        return render(request, 'blog/get_topics_by_category.html', 
        {'topics_by_category': topics_by_category})
    except: #aboba
        return render(request, 'blog/wrong_category.html')