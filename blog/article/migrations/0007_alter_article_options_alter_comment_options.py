# Generated by Django 5.1.1 on 2024-11-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
