from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Diary
from .forms import DiaryForm
from django.db.models import Q

def diary_home(request):
    return render(request, "diary/diary_home.html")

def user_diary_home(request):
    # ログインユーザーの日記から最新5件を取得
    diaries = Diary.objects.filter(author=request.user).order_by('-created_at')[:10]

    return render(request, 'diary/user_diary_home.html', {'diaries': diaries})

@login_required
def user_diary_create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)#commit=False:モデルのインスタンスを一時的に作成
            diary.author = request.user  
            diary.save() #Diaryインスタンスをデータベースに保存
            return redirect('user_diary_list')
    else:
        form = DiaryForm()
        return render(request, 'diary/user_diary_create.html', {'form': form})

@login_required
def user_diary_list(request):
    query = request.GET.get('q')#検索の値を取得
    if query:
        diaries = Diary.objects.filter(
            Q(title__icontains=query) | Q(created_at__icontains=query),#icontainsは、大文字小文字を区別せずに部分一致検索
            author=request.user
        )
    else:
        diaries = Diary.objects.filter(author=request.user) 

    return render(request, 'diary/user_diary_list.html', {'diaries': diaries})
    
@login_required
def user_diary_detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id, author=request.user)
    return render(request, 'diary/user_diary_detail.html', {'diary': diary})

@login_required
def delete_selected_diaries(request):
    if request.method == 'POST':
        # フォームから選択された日記のIDを取得
        diary_ids = request.POST.getlist('diary_ids')
        
        # ログイン中のユーザーが作成した日記のみ削除
        if diary_ids:
            Diary.objects.filter(id__in=diary_ids, author=request.user).delete()
    
    # 日記一覧にリダイレクト
    return redirect('user_diary_list')