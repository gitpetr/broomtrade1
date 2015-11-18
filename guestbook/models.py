from django.db import models

class Guestbook(models.Model):
  user = models.CharField(max_length = 20, verbose_name = "Пользователь", help_text="имя")
  posted = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = "Опубликовано")
  content = models.TextField(verbose_name = "Содержание", help_text="текст")
  
  class Meta:
    ordering = ["-posted"]
    verbose_name = "запись гостевой книги"
    verbose_name_plural = "записи гостевой книги"
