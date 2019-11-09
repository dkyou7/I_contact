from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from django.utils import timezone

# Create your views here.

<<<<<<< HEAD
def home(request):
    board = Board.objects
    return render(request,'home.html',{'boards':board})
=======
def board(request):
    board = Board.objects
    return render(request,'board.html',{'boards':board})
>>>>>>> 82657cdf38bdc6347256fe7fba9b32b2094f15d0

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk = board_id )
    return render(request, 'detail.html',{'board':board_detail})


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
    return render(request, 'edit.html',{'board':edit_board})

def update(request, board_id):
    update_board = Board.objects.get (id = board_id)
    update_board.title = request.POST['title']
    update_board.body = request.POST['body']
    update_board.save()
    return redirect('/board/'+str(update_board.id))

def delete(request, board_id):
    delete_board = Board.objects.get(id=board_id)
    delete_board.delete()
<<<<<<< HEAD
    return redirect('home')
=======
    return redirect('board')
>>>>>>> 82657cdf38bdc6347256fe7fba9b32b2094f15d0
