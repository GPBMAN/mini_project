from django.contrib import admin
from .models import Project, Skill, Experience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'technologies', 'github_link')
    search_fields = ('name', 'description', 'technologies')
    list_filter = ('date',)
    ordering = ('-date',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_category', 'level_of_mastery')
    search_fields = ('name', 'skill_category')
    list_filter = ('skill_category', 'level_of_mastery')
    ordering = ('-level_of_mastery',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'time_period')
    search_fields = ('position', 'company', 'description')
    list_filter = ('company',)
    ordering = ('-company',)