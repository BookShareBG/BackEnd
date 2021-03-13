from django.urls import path

from .views import CreateProfileView, ListProfileView

urlpatterns = [
    path('create/', CreateProfileView.as_view()),
    path('list/', ListProfileView.as_view()),
]
