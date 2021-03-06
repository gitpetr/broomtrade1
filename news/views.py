from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from news.models import New
from generic.mixins import CategoryListMixin, PageNumberMixin
from generic.controllers import PageNumberView


class NewsListView(ArchiveIndexView, CategoryListMixin):
  model = New
  exclude = False,
  date_field = "posted"
  template_name = "news_index.html"
  paginate_by = 2
  allow_empty = True
  allow_future = True

class NewDetailView(DetailView, PageNumberMixin):
  model = New
  exclude = False,
  template_name = "new.html"

class NewCreate(SuccessMessageMixin, CreateView, CategoryListMixin):
  model = New
  fields = ['title', 'description', 'content', 'posted']
  template_name = "new_add.html"
  success_url = reverse_lazy("news_index")
  success_message = "Новость успешно создана"

  # def form_valid(self, form):
  #   output = super(NewCreate, self).form_valid(form)
  #   if MailList.objects.exists():
  #     s = "На сайте 'Веник-Торг' появилась новость:\n\n" + form.instance.title + "\n\n" + form.instance.description + "\n\nhttp://localhost:8000" + reverse("news_detail", kwargs = {"pk": form.instance.pk})
  #     letters = []
  #     for maillist_item in MailList.objects.all():
  #       letters = letters + [("Уведомление с сайта 'Веник-Торг'", "Здравствуйте, " + maillist_item.username + "!\n\n" + s, settings.DEFAULT_FROM_EMAIL, [maillist_item.email])]
  #     send_mass_mail(letters, fail_silently = True)
  #   return output

class NewUpdate(SuccessMessageMixin, PageNumberView, UpdateView, PageNumberMixin):
  model = New
  fields = ['title', 'description', 'content', 'posted']
  template_name = "new_edit.html"
  success_url = reverse_lazy("news_index")
  success_message = "Новость успешно изменена"

class NewDelete(PageNumberView, DeleteView, PageNumberMixin):
  model = New
  exclude = False,
  template_name = "new_delete.html"
  success_url = reverse_lazy("news_index")
  def post(self, request, *args, **kwargs):
    messages.add_message(request, messages.SUCCESS, "Новость успешно удалена")
    return super(NewDelete, self).post(request, *args, **kwargs)

