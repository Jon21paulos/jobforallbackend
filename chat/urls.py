from django.urls import path
from chat import views

urlpatterns = [
    path('',views.ChatList.as_view()),
    path('message', views.MessageList.as_view()),
    path('add',views.AddChat.as_view()),
    path('edit/<int:pk>', views.EditChat.as_view()),
    path('message/add', views.AddMessage.as_view()),
    path('delete/<int:id>',views.DeleteChat),
    path('message/delete/<int:id>', views.DeleteMessage),

]
