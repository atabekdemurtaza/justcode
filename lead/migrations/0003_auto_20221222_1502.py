# Generated by Django 3.2 on 2022-12-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_auto_20221218_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
