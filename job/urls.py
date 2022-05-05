from django.urls import path
from job import views

urlpatterns = [
    path('',views.JobList.as_view()),
    path('<int:id>',views.JobDetail),
    path('add',views.AddJob.as_view()),
    path('edit/<int:id>',views.UpdateJob),
    path('delete/<int:id>',views.DeleteJob),
]
