# Generated by Django 4.2.4 on 2023-08-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_survey_rename_question_text_question_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='text',
        ),
    ]