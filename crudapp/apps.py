from django.apps import AppConfig


class CrudappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crudapp'
    def ready(self):
        import crudapp.signals