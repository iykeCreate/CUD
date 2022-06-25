from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic. ListView import
from django.views.generic. CreateView import'
from django.views.generic. UpdateView import
from django.views.generic. DeleteView import
from django.views.generic. DetailView import



# Create your views here.
Class PostListView(ListView):
model  = Post

Class PostCreateView(ListView):
model  = Post
fields="__all__"
Success_url='/'
reverse_lazy("blog:all")

Class PostDetailView(DetailView):
model  = Post
fields="__all__"
Success_url='/'
reverse_lazy("blog:all")

Class PostUpdateView(UpdateView):
model  = Post
fields="__all__"
Success_url='/'
reverse_lazy("blog:all")

Class PostDeleteView(DeleteView):
model  = Post
fields="__all__"
Success_url='/'
reverse_lazy("blog:all")

