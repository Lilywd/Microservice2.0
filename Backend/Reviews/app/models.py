from django.db import models

# Create your models here.

class ProductCommentModel(models.Model):
    userID = models.IntegerField()
    productID = models.IntegerField()
    comment = models.TextField()
    edited = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('userID', 'productID',)
    def __str__(self):
        return f"{self.name}: {self.id}"