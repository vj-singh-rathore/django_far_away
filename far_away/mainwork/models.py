from django.db import models
from django.contrib.auth.models import User


class ItemBook(models.Model):
    itemName = models.CharField(max_length=50)
    itemQty = models.IntegerField()
    isChecked = models.BooleanField(default=False)
    userId = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    def _str_(self):
        return self.itemName;
