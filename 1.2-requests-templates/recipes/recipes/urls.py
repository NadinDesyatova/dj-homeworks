"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from calculator.views import get_omlet_recipe, get_pasta_recipe, get_buter_recipe

urlpatterns = [
    path('omlet/', get_omlet_recipe, name='get_omlet_recipe'),
    path('pasta/', get_pasta_recipe, name='get_pasta_recipe'),
    path('buter/', get_buter_recipe, name='get_buter_recipe'),
]
