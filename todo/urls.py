from django.urls import path
from .views import TodoListView, DoneView, TodoUpdateDeleteView
urlpatterns = [
    path("list/",TodoListView.as_view()),
    path("list/<pk>/",TodoUpdateDeleteView.as_view()),
    path("done/",DoneView.as_view())
]