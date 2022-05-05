from django.urls import path
from candidate import views

urlpatterns = [
    path('',views.CandidateList.as_view()),
    # path('<int:id>',views.JobDetail),
    path('add',views.AddCandidate.as_view()),
    # path('edit/<int:id>',views.UpdateJob),
    # path('delete/<int:id>',views.DeleteJob),

]
