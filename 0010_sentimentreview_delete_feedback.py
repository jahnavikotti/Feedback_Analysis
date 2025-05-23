# Generated by Django 5.1.5 on 2025-02-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_feedback_user_alter_feedback_sentiment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sentiment', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
