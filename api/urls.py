from django.urls import path
from .views import receive_post

urlpatterns = [
    path('post/', receive_post), # <-- 여기에 동작코드를 작성하세요(2점)
]