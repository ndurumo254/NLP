from django.db import models
from pgvector.django import VectorField
# Create your models here.

EMEDDING_MODEL="text-embedding-3-small"
EMEDDING_LENGTH=1536

class BlogPost(models.Model):
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    _content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMEDDING_LENGTH, blank=True, null=True)
    can_delete = models.BooleanField(default=False, help_text="Use in jupyter notebooks")
    
    def get_embedding_text_raw(self):
        return self.content