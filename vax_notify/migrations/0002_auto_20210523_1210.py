# Generated by Django 3.2.3 on 2021-05-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vax_notify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifylist',
            name='Phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifylist',
            name='Pincode',
            field=models.IntegerField(),
        ),
    ]
