from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path("fbv", views.index_view, name="index"),
    # path("cbv", TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path("", views.IndexView.as_view(), name="index"),
    # path("go-to-maktab/",RedirectView.as_view(url="https://maktabkhooneh.org/"), name="go-to-index",),
    # path("go-to-index/",RedirectView.as_view(pattern_name="blog:cbv"), name="go-to-index",),
    path(
        "go-to-maktab/<int:pk>",
        views.RedirectToMaktab.as_view(url="https://maktabkhooneh.org/"),
        name="go-to-index",
    ),
    path("post/", views.PostView.as_view(), name="post_view"),
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"
    ),
    path("post/create/", views.PostFormView.as_view(), name="post_contact"),
    path(
        "post/<int:pk>/edit/", views.PostEditView.as_view(), name="post_edit"
    ),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
