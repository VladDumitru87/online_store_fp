from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
    # also to __init__.py add following line:
    # default_app_config ='accounts.apps.AccountsConfig'
