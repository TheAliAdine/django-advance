from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from django.urls import reverse


# User = get_user_model()
class Post(models.Model):
    """
    this is a class to define posts for blog app
    """

    author = models.ForeignKey("accounts.profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    contact = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

User = get_user_model()
class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=250)
    contact = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream

    def get_snippet(self):
        return self.contact[:10]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


=======
    
>>>>>>> Stashed changes
=======
    
>>>>>>> Stashed changes
=======
    
>>>>>>> Stashed changes
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
# Create your models here.
