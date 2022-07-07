from django.urls import path
from serviceseeker import views

urlpatterns = [
    path('',views.ServiceSeekerList.as_view()),
    path('<int:id>',views.ServiceSeekerDetail),
    path('add',views.AddServiceSeeker.as_view()),
    path('edit/<int:pk>',views.UpdateServiceSeeker.as_view()),
    path('delete/<int:id>',views.DeleteServiceSeeker),

    path('request',views.RequestServiceSeekerList.as_view()),
    path('request/add',views.AddRequestServiceSeeker.as_view()),
    path('request/delete/<int:id>',views.DeleteRequestServiceSeeker),

]
