from django.contrib import admin

from .models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("branch_name", "contact_number", "created_at", "updated_at")
    search_fields = ("branch_name", "contact_number", "address")
