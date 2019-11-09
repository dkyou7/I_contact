from django.shortcuts import render, get_object_or_404, redirect
from .models import Reward
from django.utils import timezone
import pdb
# Create your views here.
def home(request):
    reward = Reward.objects
    return render(request,'home.html',{'rewards':reward})

def reward(request):
    return render(request,'new_reward.html')

def create(request):
    new_r = Reward()
    new_r.title = request.POST['title']
    new_r.date = timezone.datetime.now()
    new_r.body = request.POST['body']
    new_r.save()
    return redirect('/reward/'+str(new_r.id))

def detail(request, reward_id):
    reward_detail = get_object_or_404(Reward, pk = reward_id )
    return render(request, 'detail_reward.html',{'reward':reward_detail})

def new(request):
    return render(request,'new_reward.html')
