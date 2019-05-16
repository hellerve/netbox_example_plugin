from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core import validators

from extras.models import CustomFieldModel


class Example(CustomFieldModel):
    description = models.TextField(blank=True)
    example = models.IntegerField(
        validators=[
            validators.MinValueValidator(5),
            validators.MaxValueValidator(100)
        ]
    )
    custom_field_values = GenericRelation(
        to='extras.CustomFieldValue',
        content_type_field='obj_type',
        object_id_field='obj_id'
    )

    csv_headers = ['description', 'example']

    class Meta:
        verbose_name = 'Example model'
