# Generated by Django 3.2.3 on 2021-05-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vax_notify', '0002_auto_20210523_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifylist',
            name='Phone_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]