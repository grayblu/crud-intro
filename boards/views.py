from django.shortcuts import render, redirect
from .models import Board
from IPython import embed


# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {
        'boards':boards,
        }
    return render(request, 'boards/index.html', context)


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    if request.method == 'POST':
        # new 에서 넘어오는 제목과 내용을 저장
        title = request.POST.get('title')
        content = request.POST.get('content')
        # orm title과 content에 위에서 넘어온 값을 할당
        board = Board(title=title, content=content)
        # db에 저장
        board.save()

        # create.html 페이지를 render
        # return redirect(f'/boards/{board.pk}')
        return redirect('boards:detail', board.pk)
    # new
    else:
        return render(request, 'boards/create.html')


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board':board,
    }
    return render(request, 'boards/detail.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)


def update(request, pk):
    # POST => UPDATE / GET => EDIT
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board, }
        return render(request, 'boards/update.html', context)
