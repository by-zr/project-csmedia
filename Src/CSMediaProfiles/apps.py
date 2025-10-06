from django.apps import AppConfig

class CsmediaprofilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CSMediaProfiles'
    verbose_name = 'CSMedia Profiles'

    def ready(self):
        import CSMediaProfiles.signals

