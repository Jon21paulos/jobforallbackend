from django.urls import path
from job import views

urlpatterns = [
    path('',views.JobList.as_view()),
    path('<int:id>',views.JobDetail),
    path('add',views.AddJob.as_view()),
    path('edit/<int:pk>',views.UpdateJob.as_view()),
    path('delete/<int:id>',views.DeleteJob),
]
