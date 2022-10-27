from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
    
    # add this function
    def ready(self):
        from . import signals
        
# post/__init__.py 
default_app_config = 'users.apps.UsersConfig'
