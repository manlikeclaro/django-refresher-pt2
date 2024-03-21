from django.urls import path

from challenges import views


urlpatterns = [
    path('', views.index),
    path('<int:month>', views.month_challenge_by_no),
    path('<str:month>', views.month_challenge, name='month-challenge')
]
