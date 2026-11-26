from django.apps import AppConfig


class ShopAppConfig(AppConfig):
    name = 'shop_app'

    def ready(self):
        from . import signals
