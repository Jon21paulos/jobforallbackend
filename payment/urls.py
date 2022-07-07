from django.urls import path
from .views import payment
from payment import views

urlpatterns = [
    path('',payment,name="payment"),
    path('list', views.PaymentList.as_view()),
    path('add', views.AddPayment.as_view()),
    path('edit/<int:pk>', views.UpdatePayment.as_view()),
    path('delete/<int:id>', views.DeletePayment),

]
