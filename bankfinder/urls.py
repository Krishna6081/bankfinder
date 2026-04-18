from django.contrib import admin
from django.urls import include, path

from branches import views as branch_views

admin.site.site_header = "Bank Branch Contact Finder"
admin.site.site_title = "Branch admin"
admin.site.index_title = "Directory administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", branch_views.staff_signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("branches.urls")),
]
