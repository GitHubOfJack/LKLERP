from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/org/', include('apps.org_structure.urls')),
    path('api/holidays/', include('apps.holiday_calendar.urls')),
    path('api/attendance/', include('apps.attendance.urls')),
    path('api/performance/', include('apps.performance.urls')),
    path('api/payroll/', include('apps.payroll.urls')),
    path('api/notifications/', include('apps.notification.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
