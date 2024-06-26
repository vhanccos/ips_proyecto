# Generated by Django 5.0.6 on 2024-06-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0006_remove_patient_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='patient_images/'),
        ),
        migrations.AddField(
            model_name='patient',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='patient_images/'),
        ),
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
