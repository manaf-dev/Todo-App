# Generated by Django 5.0.2 on 2024-02-26 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0013_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
    ]