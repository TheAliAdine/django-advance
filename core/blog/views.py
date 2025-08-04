from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
=======
from django.views.generic.edit import FormView ,CreateView,UpdateView,DeleteView
>>>>>>> Stashed changes
=======
from django.views.generic.edit import FormView ,CreateView,UpdateView,DeleteView
>>>>>>> Stashed changes

from .models import Post
from .forms import Postform
from django.shortcuts import get_object_or_404
<<<<<<< Updated upstream
<<<<<<< Updated upstream
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


def index_view(request):
    name = "ali"
    context = {"name": name}
    return render(request, "index.html", context)
=======
=======
>>>>>>> Stashed changes
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


def index_view(request):
    name = 'ali'
    context = {'name':name}
    return render(request,"index.html",context)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


"""
from django.shortcuts import redirect
def redirectmaktab(request):
    return redirect('https://maktabkhooneh/')
"""


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhoneh.org/"
=======
=======
>>>>>>> Stashed changes
        context['name'] = "ali"
        context['posts'] = Post.objects.all()
        return context

'''
from django.shortcuts import redirect
def redirectmaktab(request):
    return redirect('https://maktabkhooneh/')
'''

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhoneh.org/'
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

<<<<<<< Updated upstream
<<<<<<< Updated upstream

class PostView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    queryset = Post.objects.all()
    # model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-id"
=======
=======
>>>>>>> Stashed changes
class PostView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "blog.view_post"
    queryset = Post.objects.all()
    #model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = '-id'
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

<<<<<<< Updated upstream
<<<<<<< Updated upstream

class PostDetailView(DetailView):
    model = Post


# Create your views here.
"""
=======
=======
>>>>>>> Stashed changes
class PostDetailView(DetailView):
    model = Post

# Create your views here.
'''
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
class PostFormView(FormView):
    template_name = "contact.html"
    form_class = Postform
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
"""


class PostFormView(CreateView):
    model = Post
    fields = ["title", "contact", "status", "category", "published_date"]
    # form_class = Postform
=======
=======
>>>>>>> Stashed changes
'''
class PostFormView(CreateView):
    model = Post
    fields = ["title","contact","status","category","published_date"]
    #form_class = Postform
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
<<<<<<< Updated upstream
<<<<<<< Updated upstream


=======
    
>>>>>>> Stashed changes
=======
    
>>>>>>> Stashed changes
class PostEditView(UpdateView):
    model = Post
    form_class = Postform
    success_url = "/blog/post/"

<<<<<<< Updated upstream
<<<<<<< Updated upstream

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
=======
class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
>>>>>>> Stashed changes
=======
class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"
>>>>>>> Stashed changes
