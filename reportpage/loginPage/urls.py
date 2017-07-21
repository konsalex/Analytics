from django.conf.urls import url
from loginPage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
