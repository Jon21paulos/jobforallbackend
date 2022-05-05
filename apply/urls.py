from django.urls import path
from apply import views

urlpatterns = [
    path('',views.ApplyList.as_view()),
    # path('<int:pk>',views.ApplyList.as_view()),
    path('add',views.AddApplier.as_view()),
    # path('edit/<int:id>',views.UpdateJob),
    path('delete/<int:id>',views.DeleteApply),
]



