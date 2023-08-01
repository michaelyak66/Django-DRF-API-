from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('bookdel/<int:pk>', views.SingleBookDelete.as_view()),

]