# Generated by Django 4.2.4 on 2023-08-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_alter_useraccount_account_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='login_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='logout_time',
            field=models.DateTimeField(null=True),
        ),
    ]
