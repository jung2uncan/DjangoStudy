from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('polls/', include('polls.urls')), # 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 함.
    path('admin/', admin.site.urls)
]