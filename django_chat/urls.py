from django.conf.urls import url
from django.contrib import admin
from mainapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/$', views.MyLoginView.as_view()),
    url(r'^logout/$', views.MyLogoutView.as_view()),
    url(r'^signup/$', views.SignUpCreateView.as_view()),

]