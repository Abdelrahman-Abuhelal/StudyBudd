# Generated by Django 4.0 on 2021-12-31 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]