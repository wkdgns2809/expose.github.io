"""newporject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import practiceapp.views
import accountapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',practiceapp.views.first,name='first'),
    path('readtext/<int:post_id>/',practiceapp.views.readtext,name='readtext'),
    path('createplace/',practiceapp.views.createplace,name='createplace'),
    path('update/<int:post_id>/',practiceapp.views.update,name="update"),
    path('delete/<int:post_id>',practiceapp.views.delete,name='delete'),
    path('deleteall/',practiceapp.views.deleteall,name='deleteall'),
    path('search/',practiceapp.views.search,name="search"),
    path('category/',practiceapp.views.category,name="category"),
    path('signup/',accountapp.views.signup,name="signup"),
    path('login/',accountapp.views.login,name="login"),
    path('logout/',accountapp.views.logout,name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
