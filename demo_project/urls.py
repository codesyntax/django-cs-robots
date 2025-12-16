from django.contrib import admin
from django.urls import path, include
from cs_robots.views import serve_robots_txt

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/tools/", include("cs_robots.urls")),
    path("admin/", admin.site.urls),
    # Add the URL for the admin editor
    path("robots.txt", serve_robots_txt, name="robots_txt"),
]
