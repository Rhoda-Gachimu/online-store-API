from django.urls import path
# import views model so that we can view the functions in the views.py
from . import views

# map urls to my view model

# URL conf module
# url pattern include the 1.)route 2.) views function
# all routes should end with a forward slash


urlpatterns = [
    path ('hello/', views.say_hello)
]