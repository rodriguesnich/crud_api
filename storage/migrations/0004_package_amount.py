# Generated by Django 3.1.7 on 2021-03-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_package_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
