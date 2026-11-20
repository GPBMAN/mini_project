from django.db import models as m

class Task(m.Model):
    name = m.CharField(max_length=100, verbose_name='Name')
    description = m.TextField(max_length=1000, verbose_name='Description')
    creation_date = m.DateField(auto_now_add=True, verbose_name='Time of creation')
    completion_status = m.BooleanField(default=False, verbose_name='Completion')

    def __str__(self):
        return f"{self.name} - {self.creation_date}"

    class Meta():
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
