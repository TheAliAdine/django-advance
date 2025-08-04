from django.contrib import admin
<<<<<<< Updated upstream
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_date",
        "published_date",
    ]

=======
from .models import Post , Category

class PostAdmin(admin.ModelAdmin):
    list_display = ["author","title","status","category","created_date","published_date"]
>>>>>>> Stashed changes

admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
