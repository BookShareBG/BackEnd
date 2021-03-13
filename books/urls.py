from django.urls import path

from .views import CreateBookView, ListBookView

urlpatterns = [
    path('create/', CreateBookView.as_view()),
    path('list/', ListBookView.as_view()),
]
