from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('book', views.book, name="book"),
    path('book_detail/<slug:slug>/', views.book_detail, name="book_detail"),
    path('eventsimage', views.eventsimage, name="eventsimage"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)