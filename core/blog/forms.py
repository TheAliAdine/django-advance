from django import forms
from .models import Post

<<<<<<< Updated upstream
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
class Postform(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< Updated upstream
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
=======
        fields = ["author","title","contact","status","category","published_date"]  

>>>>>>> Stashed changes
