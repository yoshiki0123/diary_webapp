from django.contrib import admin
from .models import Diary

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 管理画面で表示するフィールドを指定
    search_fields = ('title', 'content')  # タイトルと内容を検索できるようにする
    list_filter = ('author', 'created_at')  # フィルタ機能を追加（ユーザーと作成日でフィルタ）