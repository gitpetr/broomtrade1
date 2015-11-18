from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'broomtrade.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', "django.contrib.auth.views.login", name = "login"),
    url(r'^logout/', "django.contrib.auth.views.logout", name = "logout"),
    url(r'^$', include('main.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^imagepool/', include('imagepool.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
