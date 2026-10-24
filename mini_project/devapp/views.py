from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project, Skill, Experience

def all_projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request=request, template_name="all_projects.html", context=context)

def project_detailed(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    return render(request, "project.html", {"project": project})


def pricing_view(request):

    items = [
        {'id': 1, 'name': 'Basic Package', 'price': 50.00, "desc": "Basic package: 3-5 pages, database", 'is_default_selected': True},
        {'id': 2, 'name': 'Extra Routes', 'price': 30.00, "desc": "3-5 extra pages", 'is_default_selected': False},
        {'id': 3, 'name': 'Priority Making', 'price': 20.00, "desc": "Faster production", 'is_default_selected': False},
        {'id': 4, 'name': 'Custom Domain', 'price': 15.00, "desc": "Custom Url", 'is_default_selected': False},
    ]
    
    context = {'items': items}
    return render(request, 'pricing.html', context)

def process_pricing_selection(request):
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        
        
        return HttpResponse(f"Successfully selected item IDs: {selected_item_ids}")
    
    return redirect('pricing_page')

def about_me(request):
    return render(request, "about_me.html")

def home_view(request):
    return render(request, "home.html")