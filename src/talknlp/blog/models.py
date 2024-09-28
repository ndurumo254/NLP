from django.db import models
from pgvector.django import VectorField
# Create your models here.

EMEDDING_MODEL="text-embedding-3-small"
EMEDDING_LENGTH=1536

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField
    timestamp=models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMEDDING_LENGTH, blank=True, null=True)
    
