from django.urls import path
from django.conf.urls import url , include
from .views import login_page, submit

app_name = "login_page"

urlpatterns = [
    url(r'^$', login_page, name="login"),
    url(r'^submit/', submit, name="submit")
]