from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'creado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
        
    )
    
    class Meta:
        abstract = True

