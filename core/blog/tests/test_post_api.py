from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User
import pytest
@pytest.fixture
def api_cilent():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email = "admin@admin.com" , password = "123" , is_verified= True)
    return user

@pytest.mark.django_db
class TestPostApi:
    

    def test_get_post_response_200_status(self,common_user,api_cilent):
        url = reverse("blog:api-v1:post-list")
        user= common_user
        api_cilent.force_authenticate(user=user)
        response = api_cilent.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self,api_cilent):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "sony",
            "contact" : "description",
            "status" : True,
            
            "published_date" : datetime.now(),
        }
        response = api_cilent.post(url,data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self,api_cilent,common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "sony",
            "contact" : "description",
            "status" : True,
            
            "published_date" : datetime.now(),
        }
        user= common_user
        api_cilent.force_login(user=user)
        response = api_cilent.post(url,data)
        assert response.status_code == 201


    def test_create_post_invalid_data_response_400_status(self,api_cilent,common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title" : "sony",
            "contact" : "description",
            
        }
        user= common_user
        api_cilent.force_authenticate(user=user)
        response = api_cilent.post(url,data)
        assert response.status_code == 400