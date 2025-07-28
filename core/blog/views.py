from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView ,CreateView,UpdateView,DeleteView

from .models import Post
from .forms import Postform
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


def index_view(request):
    name = 'ali'
    context = {'name':name}
    return render(request,"index.html",context)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "blog.view_post"
    queryset = Post.objects.all()
    #model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostDetailView(DetailView):
    model = Post

# Create your views here.
'''
class PostFormView(FormView):
    template_name = "contact.html"
    form_class = Postform
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''
class PostFormView(CreateView):
    model = Post
    fields = ["title","contact","status","category","published_date"]
    #form_class = Postform
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    form_class = Postform
    success_url = "/blog/post/"

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/post/"