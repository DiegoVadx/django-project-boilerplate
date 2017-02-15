from django.apps import AppConfig
from apps.utils.print_colors import _orange


class BaseConfig(AppConfig):
    name = 'apps.__base'
    verbose_name = '__base'

    def ready(self):
        print(_orange('Ready Base!'))
        from . import signals