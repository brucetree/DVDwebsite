# Generated by Django 3.2.7 on 2021-10-28 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_rename_title_score_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ('-created_time',), 'verbose_name': 'score'},
        ),
        migrations.AddField(
            model_name='score',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
