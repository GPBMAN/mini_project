from django.apps import AppConfig


class DevappConfig(AppConfig):
    name = 'devapp'

    def ready(self):
        import devapp.signals
