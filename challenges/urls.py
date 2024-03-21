from django.urls import path

from challenges import views


urlpatterns = [
    # path('january', views.index),
    # path('february', views.february),
    path('<month>', views.month_challenge)
]
