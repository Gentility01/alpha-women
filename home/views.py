from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, ContactForm
from .forms import MyContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import CreatePostForm

# Create your views here.
class homeView(ListView):
    model = Post
    template_name = 'home/index.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5

class PostListView(ListView):
    model = Post
    template_name = 'home/lists.html'
    context_object_name = 'posts'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home/post_form.html'
    # form_class = CreatePostForm
    fields = ('image', 'title', 'cotent')

    def form_valid(self, form) :
        form.instance.Administrators = self.request.user
        return super().form_valid(form)
 
   
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'home/post_form.html'
    # form_class = CreatePostForm
    fields = ('image', 'title', 'cotent')

    def form_valid(self, form) :
        form.instance.Administrators = self.request.user
        return super().form_valid(form)

    def test_func(self):
       post = self.get_object()
       if self.request.user == post.Administrators:
           return True
       return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    context_object_name = 'posts'

    def test_func(self):
       post = self.get_object()
       if self.request.user == post.Administrators:
           return True
       return False
 



def about(request):
    return render(request, 'home/about.html')


def contact(request):
    form = MyContactForm(request.POST)
    if form.is_valid():
        m_contact = ContactForm(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            male=form.cleaned_data['male'],
            female=form.cleaned_data['female'],
            message=form.cleaned_data['message'],
        )
        m_contact.save()
        send_mail(
            "email from " + m_contact.first_name,#header
             m_contact.message+ "\nYou can contact me on " + m_contact.email,#message/body
         
            'douglaschiemela1@gmail.com',#
            ['mastergentility5@gmail.com',],#to the owner email


        )
            
        # messages(request, f'{first_name} your message is sent successfully we will get back to you shortly')
        return redirect('contact')
    context = {
        'form':form
    }
    return render(request, 'home/contact.html', context)
