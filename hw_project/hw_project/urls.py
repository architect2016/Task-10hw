from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("users/", include("users.urls")),
    path("", include("quotes.urls")),
    path('admin/', admin.site.urls),
]