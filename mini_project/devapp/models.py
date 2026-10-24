from django.db import models
from datetime import date, timedelta

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Project Name")
    description = models.CharField(max_length=400, verbose_name="Description")
    technologies = models.CharField(max_length=300, verbose_name="Technologies")
    github_link = models.URLField(max_length=300, verbose_name="Github link", default="github.com")
    image = models.ImageField(verbose_name="Image", upload_to="images/", default="placeholder.png")
    date = models.DateField(verbose_name="Date of making")


    def __str__(self):
        return f"{self.name} - {self.description}"


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-date']



class Skill(models.Model):
    name = models.CharField(max_length=200, verbose_name="Skill name")
    skill_category = models.CharField(max_length=200, verbose_name="Skill category")
    level_of_mastery = models.PositiveIntegerField(verbose_name="Skill mastery 1-10")


    def __str__(self):
        return f"{self.name} - {self.skill_category} - {self.level_of_mastery}"


    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['-level_of_mastery']



class Experience(models.Model):
    position = models.CharField(max_length=200, verbose_name="Position name")
    company = models.CharField(max_length=200, verbose_name="Company name")
    time_period = models.CharField(max_length=50, verbose_name="Time (3 years or 20.09.25 - 21.08.26)")
    description = models.CharField(max_length=300, verbose_name="Description")

    def __str__(self):
        return f"{self.position} - {self.company} - {self.time_period}"


    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['-company']