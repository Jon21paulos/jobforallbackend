from django.urls import path
from videochat import views
urlpatterns = [
    path('<int:pk>',views.VchatDetail),
    path('add',views.AddVchat.as_view()),
    path('delete/<int:pk>',views.DeleteVchat),
]
