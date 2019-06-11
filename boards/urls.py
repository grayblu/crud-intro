from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new), 해당 get요청이 create 뷰 함수에서 동작
    path('create/', views.create, name='create'),   # GET(new), POST(create)
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/update/', views.update, name='update'),  # GET(edit), POST(create)
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),    # POST
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
