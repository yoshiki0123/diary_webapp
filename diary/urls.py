from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
    
urlpatterns = [
    path('', views.diary_home, name='diary_home'),
    # ログインページ
    path('login/', auth_views.LoginView.as_view(template_name='diary/login.html'), name='login'),
    # ログアウト
    path('logout/', auth_views.LogoutView.as_view(next_page='diary_home'), name='logout'),
    # 日記のURLなど他のパス
    path("user_diary_home", views.user_diary_home, name="user_diary_home"),
    path('user_diary_list/', views.user_diary_list, name='user_diary_list'),
    path("user_diary_create/", views.user_diary_create, name="user_diary_create"),
    path('diary/<int:diary_id>/', views.user_diary_detail, name='user_diary_detail'),  
    path('delete_selected_diaries/', views.delete_selected_diaries, name='delete_selected_diaries'),
]