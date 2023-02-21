from django.contrib import admin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):  # noqa: F811
    pass
