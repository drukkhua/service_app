from celery_app import app as celery_app

print(celery_app.log)
__all__ = ('celery_app',)
