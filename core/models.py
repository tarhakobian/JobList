import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    # publisher = models.ForeignKey(, on_delete=CASCADE, )
    category = models.CharField(max_length=255, default='Mixed', db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    requirements = models.TextField(default='No Requirements', null=True)
    salary = models.CharField(max_length=255, null=True)
    contact_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
