import datetime

from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# As model field:
from django_currentuser.db.models import CurrentUserField
from author.decorators import with_author
from django.utils.translation import gettext_lazy as _

class CommonFields(models.Model):
    # Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = CurrentUserField(on_update=True, related_name='+')


    # Meta
    class Meta:
        abstract = True