from django.db import models


class CreatedModel(models.Model):

    """
    Model with created_at field.

    This is abstract model use it with models.Model.
    """

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel(CreatedModel, models.Model):
    """
    Model with created_at and updated_at fields.

    This is abstract model use it with models.Model.
    """

    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
