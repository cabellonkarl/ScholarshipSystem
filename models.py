from django.db import models
from django.db.models.fields import FloatField

# Create your models here.

class ScholarType(models.Model):
    scholarType_id = models.IntegerField()
    scholarType_name =models.CharField(max_length=100, default='', null=False)

class Scholar(models.Model):
    scholar_id = models.CharField(max_length=100, default='', null=False)
    firstName = models.CharField(max_length=100, default='', null=False)
    middleName = models.CharField(max_length=100, default='', null=False)
    lastName = models.CharField(max_length=100, default='', null=False)
    course = models.CharField(max_length=10, default='', null=False)
    year = models.IntegerField()
    totalFees = models.FloatField()
    scholar_type = models.ForeignKey(ScholarType, on_delete = models.CASCADE)

class Working(models.Model):
    scholar_id = models.ForeignKey(Scholar, on_delete = models.CASCADE)
    officeAssigned = models.CharField(max_length=100, default='', null=False)

class Bank(models.Model):
    bank_id = models.IntegerField
    bank_Name = models.CharField(max_length=100, default='', null=False)

class ScholarshipType(models.Model):
    scholarshipType_id = models.IntegerField()
    scholarshipType_name =models.CharField(max_length=100, default='', null=False)

class Scholarship(models.Model):
    scholarship_id = models.IntegerField()
    scholarship_name = models.CharField(max_length=100, default='', null=False)
    sponsor = models.CharField(max_length=100, default='', null=False)
    accountNumber = models.CharField(max_length=100, default='', null=False)
    bank_id = models.ForeignKey(Bank, on_delete = models.CASCADE)
    totalScholars = models.IntegerField()
    scholarship_type = models.ForeignKey(ScholarshipType, on_delete = models.CASCADE)

class Subsidized(models.Model):
    scholarship_id = models.ForeignKey(Scholarship, on_delete = models.CASCADE)
    subsidy = models.FloatField()

class Percentile(models.Model):
    scholarship_id = models.ForeignKey(Scholarship, on_delete = models.CASCADE)
    percent = models.FloatField()

class NonWorking(models.Model):
    scholar_id = models.ForeignKey(Scholar, on_delete = models.CASCADE,)
    scholarship_id = models.ForeignKey(Scholarship, on_delete = models.CASCADE,)