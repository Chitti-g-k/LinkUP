# Generated by Django 4.1.3 on 2023-05-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("franchisor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fprofile",
            name="estb_Year",
            field=models.IntegerField(default=2022),
        ),
        migrations.AlterField(
            model_name="fprofile",
            name="large_description",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="fprofile",
            name="min_investment",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="fprofile",
            name="no_of_branches",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="fprofile",
            name="small_description",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
