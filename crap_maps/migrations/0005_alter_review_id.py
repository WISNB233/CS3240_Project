# Generated by Django 4.2.6 on 2023-11-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crap_maps', '0004_review_approved_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
