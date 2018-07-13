from django.db import models
from django.utils.encoding import smart_text
from datetime import datetime
# Create your models here.
class employee(models.Model):
	first_name=models.CharField(max_length=20,null=False)
	last_name=models.CharField(max_length=20,null=False)
	joining_date=models.DateTimeField(default=datetime.now)
	salary=models.IntegerField(null=True)
	email=models.EmailField(max_length=50,null=False)

	def __str__(self):
		return self.first_name


class Meta:
	verbose_name_plural="Employees"


	
