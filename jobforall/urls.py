from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('job/',include('job.urls')),
    path('applier/',include('apply.urls')),
    path('candidate/', include('candidate.urls')),
    path('chat/', include('chat.urls'))

]
