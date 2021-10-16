from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    return render(request,'djWebs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'djWebs/topics.html',context)

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'djWebs/topic.html',context)

def new_topic(request):
    