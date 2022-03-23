from django.contrib import admin
from django.urls import path

from board.views import board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board, name='board')
]
