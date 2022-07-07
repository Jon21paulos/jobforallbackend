from django.urls import path
from feedback import views

urlpatterns = [
    path('testimonial', views.TestimonialList.as_view()),
    path('testimonial/add',views.AddTestimonial.as_view()),
    path('rating', views.RatingList.as_view()),
    path('rating/add', views.AddRating.as_view()),
    path('testimonial/delete/<int:id>',views.DeleteTestimonial),
    path('rating/delete/<int:id>', views.DeleteRating),

]
