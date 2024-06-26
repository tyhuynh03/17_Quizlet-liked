# Generated by Django 5.0.1 on 2024-04-21 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0003_alter_topic_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="audio",
            field=models.FileField(blank=True, null=True, upload_to="question_audios/"),
        ),
        migrations.AddField(
            model_name="question",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="question_images/"
            ),
        ),
    ]
