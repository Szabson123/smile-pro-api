# Generated by Django 5.1 on 2024-08-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('reception', 'Reception'), ('doctor', 'Doctor'), ('none', 'None')], default='none', max_length=30),
        ),
    ]
