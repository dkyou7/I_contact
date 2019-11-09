from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from login.models import Profile
from django.contrib.auth.models import User

# Create your views here.

def board(request):
    board = Board.objects
    return render(request,'board.html',{'boards':board})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk = board_id )
    comments = Comments.objects.filter(post = board_id)
    user = request.user
    if user.is_authenticated: 
        profile = get_object_or_404(Profile, user = user)
        return render(request, 'detail.html',{'board':board_detail,'comments':comments, 'profile':profile, 'like_count':board_detail.total_likes})
    else:
        return render(request, 'detail.html',{'board':board_detail,'comments':comments, 'profile':'anonymous'})
        

def new(request):
    return render(request,'new.html')

def create(request):
    new_board = Board()
    new_board.title = request.POST['title']
    new_board.date = timezone.datetime.now()
    new_board.body = request.POST['body']
    new_board.save()
    return redirect('/board/'+str(new_board.id))

def edit(request,board_id):
    edit_board = Board.objects.get(id=board_id)
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    if edit_board.writer == profile:
        return render(request, 'edit.html',{'board':edit_board})
    else:
        return redirect('detail',board_id)

def update(request, board_id):
    update_board = Board.objects.get (id = board_id)
    update_board.title = request.POST['title']
    update_board.body = request.POST['body']
    update_board.save()
    return redirect('/board/'+str(update_board.id))

def delete(request, board_id):
    delete_board = Board.objects.get(id=board_id)
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    if delete_board.writer == profile:
        delete_board.delete()
        return redirect('board')
    else:
        return redirect('detail',board_id)

def new_comment(request, detail_id):
    comment = Comments()
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    comment.writer = profile
    comment.content = request.POST['content']
    comment.post = get_object_or_404( Board, pk= detail_id)
    comment.save()
    return redirect('detail',detail_id)

def delete_comment(request, comment_id):
    d_comment = Comments.objects.get(id=comment_id) 
    user = request.user
    profile = get_object_or_404(Profile, user = user)
    if d_comment.writer == profile:
        d_comment.delete()

    return redirect('detail',d_comment.post.pk)

def like(request,board_id):
    board =get_object_or_404(Board, pk = board_id)
    if board.user.filter(username=request.user.username).exists():
        board.user.remove(request.user)    
    else:
        board.user.add(request.user)
       
    board.save()
    return redirect('detail', board_id)
