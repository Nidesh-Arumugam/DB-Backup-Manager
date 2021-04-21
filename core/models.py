from django.db import models
from django.contrib import admin
class databases(models.Model):
    DBname= models.CharField(max_length=100)
    IP  = models.GenericIPAddressField(protocol='both', unpack_ipv4=False,null=True)
    Port = models.IntegerField()
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)

    # def __str__(self):
    #     return self.DBname + " "  + self.Password + " " + self.UserName 

class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('DBname', 'IP', 'Port', 'UserName')