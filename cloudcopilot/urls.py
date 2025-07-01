from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),         # login, register, forgot
    path('dashboard/', include('dashboard.urls'))  # home after login
]
