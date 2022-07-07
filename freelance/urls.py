from django.urls import path
from freelance import views

urlpatterns = [
    path('',views.FreelanceJobList.as_view()),
    path('<int:id>',views.FreelanceJobDetail),
    path('add',views.AddFreelanceJob.as_view()),
    path('edit/<int:pk>',views.UpdateFreelanceJob.as_view()),
    path('delete/<int:id>',views.DeleteFreelanceJob),
]
