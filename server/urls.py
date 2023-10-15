from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/education',views.Education.as_view()),
    path('portfolio/certifications',views.Certification.as_view()),
    path('portfolio/experience',views.Experience.as_view()),
    path('portfolio/project',views.Project.as_view()),
    path('portfolio/skills',views.Skills.as_view()),
    path('contact',views.ContactData.as_view()),
    path('download',views.Download.as_view())  
]


