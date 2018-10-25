from django.urls import path
from .views import HomePageView

urlpatterns = [
    #using .as_view because using class based views
    path('', HomePageView.as_view(), name='home'),
]
