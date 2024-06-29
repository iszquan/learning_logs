from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Detail
from .forms import TopicForm, DetailForm



# Create your views here.
def index(request):
    """ 主页 """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    # 确认用户
    if topic.owner != request.user:
        raise Http404

    details = topic.detail_set.order_by('-date_added')   # 降序
    context = {'topic': topic, 'details': details}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """ 添加新主题 """
    if request.method != 'POST' :
        # 创建表单
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_detail(request, topic_id):
    """ 在特定主题新增 """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = DetailForm()
    else:
        form = DetailForm(data=request.POST)
        if form.is_valid():
            # 新增条目
            new_detail = form.save(commit=False)
            new_detail.topic = topic
            new_detail.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_detail.html', context)


@login_required
def edit_detail(request, detail_id):
    """ 编辑已有条目 """
    detail = Detail.objects.get(id=detail_id)
    topic = detail.topic
    # 确认用户
    if request.user != topic.owner:
        raise Http404

    if request.method != 'POST':
        form = DetailForm(instance=detail)
    else:
        form = DetailForm(instance=detail, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'detail': detail, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_detail.html', context)

