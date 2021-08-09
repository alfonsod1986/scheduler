from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    name = 'scheduler.apps.schedule'

    def ready(self):
        import scheduler.apps.schedule.signals