from django.db import models

# Create your models here.
class approvals(models.Model):
	Category = (
		('capture', 'capture'),
		('utilization', 'utilization'),
		('T&S', 'T&S'),
		('Full Chain', 'Full Chain'),
	)
	
	project=models.CharField(max_length=15)
	country=models.CharField(max_length=15)
	DateStart=models.DateTimeField(default=0)
	DateEnd=models.DateTimeField(default=0)
	budget=models.FloatField(default=0)
	findingSource=models.FloatField(default=0)
	category=models.CharField(max_length=15 ,  choices=Category)
	TRLSart=models.IntegerField(default=0)
	TRLend=models.IntegerField(default=0)
	profit=models.IntegerField(default=0)
	EmissionsDecrease=models.FloatField(default=0)
	

	def __str__(self):
		return f'{self.project}'
