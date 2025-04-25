from django.apps import AppConfig


class MedicaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_app'

    def ready(self):
            import web_app.signals  # importa aquí los comandos señanes de Django       
