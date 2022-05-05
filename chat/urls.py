from django.urls import path
from chat import views

urlpatterns = [
    path('',views.ChatList.as_view()),
    path('add',views.AddChat.as_view()),
    path('delete/<int:id>',views.DeleteChat),
]
