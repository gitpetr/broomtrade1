from django import forms

from guestbook.models import Guestbook

class GuestbookForm(forms.ModelForm):
  class Meta:
    model = Guestbook
    exclude = False,
  user = forms.CharField(max_length = 20, label = "Имя")
  content = forms.CharField(widget = forms.Textarea, label = "Текст")
  honeypot = forms.CharField(required = False, label = "Ловушка для спамеров")
