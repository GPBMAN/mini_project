from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.all_projects, name="projects"),
    path("project/<int:project_id>/", views.project_detailed, name="project"),
    path('pricing/', views.pricing_view, name='pricing_page'),
    path('pricing/process/', views.process_pricing_selection, name='process_selection'),
    path('about_me/', views.about_me, name="about_me_page"),
    path("home_page/", views.home_view, name="home_page")
]