# Generated by Django 2.1.4 on 2019-04-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190430_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Body',
            field=models.TextField(),
        ),
    ]
