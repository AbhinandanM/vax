from django.apps import AppConfig


class VaxNotifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vax_notify'

    def ready(self):
            from . import updater
            updater.start()
