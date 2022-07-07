from django.urls import path
from report import views

urlpatterns = [
    path('',views.ReportList.as_view()),
    path('add',views.CreateReport.as_view()),
    path('delete/<int:id>',views.DeleteReport),

    path('warning', views.WarningList.as_view()),
    path('warning/add', views.CreateWarning.as_view()),

    path('notify', views.NotifyList.as_view()),
    path('notify/add', views.CreateNotify.as_view()),
]
