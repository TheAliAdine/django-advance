from django import forms
from .models import Post

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class Postform(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< Updated upstream
        fields = [
            "title",
            "contact",
            "status",
            "category",
            "published_date",
        ]
=======
        fields = ["author","title","contact","status","category","published_date"]  

>>>>>>> Stashed changes
