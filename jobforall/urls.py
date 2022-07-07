from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('job/',include('job.urls')),
    path('applier/',include('apply.urls')),
    path('candidate/', include('candidate.urls')),
    path('chat/', include('chat.urls')),
    path('vchat/', include('videochat.urls')),
    path('reports/', include('report.urls')),
    path('freelancejob/', include('freelance.urls')),
    path('feedback/', include('feedback.urls')),
    path('payment/', include('payment.urls')),
    path('serviceseeker/', include('serviceseeker.urls')),

]
