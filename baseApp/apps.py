from django.apps import AppConfig



class BaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baseApp'
# baseApp/apps.py


class BaseConfigrest_framework(AppConfig):
    name = 'baseApp'

    def ready(self):

    # Your configuration settings here, if needed
        pass
