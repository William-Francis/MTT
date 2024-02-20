from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["user__id"]
    list_display = (
        "id",
        "username",
        "created",
        "modified",
    )
