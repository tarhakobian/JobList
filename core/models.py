from django.db import models
from django.db.models import deletion


class Post(models.Model):
    id = models.AutoField(editable=False, primary_key=True)
    publisher = models.ForeignKey(on_delete=deletion.CASCADE, to='auth.User', null=True)
    category = models.CharField(max_length=255, default='Mixed', db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    requirements = models.TextField(default='No Requirements', null=True)
    salary = models.CharField(max_length=255, null=True)
    contact_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
