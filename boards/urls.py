from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new), 해당 get요청이 create 뷰 함수에서 동작
    path('create/', views.create, name='create'),   # GET(new), POST(create)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),  # GET(edit), POST(create)
]
