from django.db import models
from django.contrib.auth.models import User  # Userモデルをインポート

class Diary(models.Model):
    title = models.CharField(max_length=200)  # 日記のタイトル
    content = models.TextField()  # 日記の内容
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 誰が書いたか（ユーザーと紐づけ）

    def __str__(self):
        return self.title
