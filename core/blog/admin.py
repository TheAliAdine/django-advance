from django.contrib import admin
<<<<<<< Updated upstream
<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
from .models import Post , Category

class PostAdmin(admin.ModelAdmin):
    list_display = ["author","title","status","category","created_date","published_date"]
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
