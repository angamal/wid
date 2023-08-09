from django.db import models


# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=150,unique=True,null=True)
    password = models.CharField(max_length=128,null=True)
    name = models.CharField(max_length=255,null=True)
    dob = models.DateField(null=True)
    age = models.IntegerField(null=True)
    gender = models.TextField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')],null=True)
    phone_number = models.CharField(max_length=250,null=True)
    address = models.TextField(null=True)
    mail_id = models.EmailField(null=True)
    account_type = models.TextField(choices=[('savings', 'Savings'), ('current', 'Current')],null=True)
    district = models.TextField(choices=[('ernakulam', 'Ernamkulam'),('thrissur', 'Thrissur'),  ('kottayam', 'Kottayam'), ('alappuzha', 'Alappuzha'),('idukki' ,'Idukki')],null=True)
    branch = models.TextField(choices=[('aluva','Aluva'),('edapally','edapally'),('angamaly','Angamaly'),('paravur','Paravur')],null=True)
    materials = models.TextField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')],null=True)


    def __str__(self):
        return self.username