from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    #using .as_view because using class based views
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
