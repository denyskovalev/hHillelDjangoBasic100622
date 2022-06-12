

from django.urls import path

from shop.views import hello_page, dog, cat

urlpatterns = [
    path('hello/', hello_page),
    path('/dog', dog),
    path('cat/', cat),
]
