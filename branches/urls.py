from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/branches/search/", views.branch_search_api, name="branch_search_api"),
    path("api/branches/detail/", views.branch_detail_api, name="branch_detail_api"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/branches/add/", views.branch_add, name="branch_add"),
    path("dashboard/branches/<int:pk>/edit/", views.branch_edit, name="branch_edit"),
    path("dashboard/branches/<int:pk>/delete/", views.branch_delete, name="branch_delete"),
    path("dashboard/export/", views.export_branches_excel, name="branch_export"),
    path("dashboard/import/", views.import_branches, name="branch_import"),
]
