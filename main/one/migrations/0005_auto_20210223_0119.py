# Generated by Django 3.1.6 on 2021-02-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20210223_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudex',
            name='username',
            field=models.CharField(max_length=150, verbose_name='User name'),
        ),
    ]