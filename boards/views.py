from django.shortcuts import render, redirect
from .models import Board

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
    # new 에서 넘어오는 제목과 내용을 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # orm title과 content에 위에서 넘어온 값을 할당
    board = Board(title=title,
                  content=content)
    # db에 저장
    board.save()

    # create.html 페이지를 render
    return redirect(f'/boards/{board.pk}')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board':board,
    }
    return render(request, 'boards/detail.html', context)
