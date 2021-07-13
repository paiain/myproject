
from django.urls import path
from Blog.views import index

urlpatterns = [
    path('', index)
]