"""bookshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', name='home'),
    # path('signup/', name='signup'),
    # path('email-verification/', name='email-verification'),
    # path('login/', name='login'),
    # path('logout/', name='logout'),
    # path('password-reset/', name='password-reset'),
    # path('password-reset/confirm/', name='password-reset-confirm'),
    # path('user-details/', name='user-details'),
    # path('password-change/', name='password-change'),


    # this url is used to generate email content
    # path('password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', name='password_reset_confirm'),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('account/', include('allauth.urls')),
    # path('accounts/profile/', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs')

    path('profile/', include('profiles.urls')),
    path('book/', include('books.urls')),
]
