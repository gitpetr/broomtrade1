from django.contrib import admin
from news.models import New


class NewAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'posted')
    list_filter = ['posted', 'title']
    search_fields = ['title']
    #exclude = False,
    #field  =  ['title', 'description', 'content', 'posted']

admin.site.register(New, NewAdmin)
