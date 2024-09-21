from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals  # Import signal handlers

