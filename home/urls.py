from django.urls import path
from . import views
from.views import PostListView, homeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView    
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('list_view/', PostListView.as_view(), name='list_view'),
    path('create/', PostCreateView.as_view(), name='create_view'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_detail/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post_detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
