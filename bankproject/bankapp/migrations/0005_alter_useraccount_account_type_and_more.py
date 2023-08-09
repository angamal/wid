# Generated by Django 4.2.4 on 2023-08-07 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_alter_useraccount_mail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_type',
            field=models.TextField(choices=[('savings', 'Savings'), ('current', 'Current')], null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='branch',
            field=models.TextField(choices=[('aluva', 'Aluva'), ('edapally', 'edapally'), ('angamaly', 'Angamaly'), ('paravur', 'Paravur')], null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='district',
            field=models.TextField(choices=[('ernakulam', 'Ernamkulam'), ('thrissur', 'Thrissur'), ('kottayam', 'Kottayam'), ('alappuzha', 'Alappuzha'), ('idukki', 'Idukki')], null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.TextField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='materials',
            field=models.TextField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')], null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]