from django.urls import path
from board.views import board, post_write

urlpatterns = [
    path('', board, name='board'),
    path('post/write', post_write, name='post_write'),
]