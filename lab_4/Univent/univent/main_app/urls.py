from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', cache_page(10)(views.index), name='index'),
    path('posters/', views.Posters.as_view(), name='posters'),
    path('personal_account/', views.personal_account, name='personal_account'),
    path('poster_redactor/', views.poster_redactor, name='poster_redactor'),
    path('registration_page/', views.registration_page, name='registration_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('posters/<slug:post_slug>/', views.poster, name='poster'),
    path('submit_application/', views.submit_application, name='submit_application'),
]
