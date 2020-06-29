from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(selfs):
        import accounts.signals
