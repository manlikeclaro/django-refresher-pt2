from django.urls import path

from challenges import views


urlpatterns = [
    path('<int:month>', views.month_challenge_by_no),
    path('<str:month>', views.month_challenge)
]
