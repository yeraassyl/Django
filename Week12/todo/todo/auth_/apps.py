from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth_'

    def ready(self):
        import todo.auth_.signals