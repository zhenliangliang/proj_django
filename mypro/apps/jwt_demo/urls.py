
from django.urls import path, include
from . import views


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'login/', views.LoginView.as_view()),
    path(r'order/', views.OrderView.as_view()),
    path(r'jwtlogin/', views.JwtLoginView.as_view()),
    path(r'jwtorder/', views.JwtOrderView.as_view()),

]

