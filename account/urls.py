from django.urls import path
from .views import JobseekerSignupView, EmployerSignupView, JobseekerEditProfileView, JobseekerProfileView, UserView, \
    EmployerEditProfileView, EmployerProfileView

# BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [

    path('<int:pk>', UserView.as_view()),

    path('register/jobseeker/', JobseekerSignupView.as_view()),
    path('jobseeker/profile/edit/<int:pk>', JobseekerEditProfileView.as_view()),
    path('jobseeker/profile/<int:pk>', JobseekerProfileView.as_view()),


    path('register/employer/', EmployerSignupView.as_view()),
    path('employer/profile/edit/<int:pk>', EmployerEditProfileView.as_view()),
    path('employer/profile/<int:pk>', EmployerProfileView.as_view()),

    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
    #      name='blacklist')
]