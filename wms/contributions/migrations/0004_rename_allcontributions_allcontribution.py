# Generated by Django 5.0.1 on 2024-02-02 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0003_alter_allcontributions_cont_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllContributions',
            new_name='AllContribution',
        ),
    ]
