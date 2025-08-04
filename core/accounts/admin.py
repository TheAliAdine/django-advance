from django.contrib import admin
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
from django.contrib.auth.admin import UserAdmin  
from .models import User ,Profile
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("import date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "is_superuser",
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",) 
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
# Register your models here.
