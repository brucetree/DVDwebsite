# Generated by Django 3.2.7 on 2021-10-10 10:12

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_time',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=mdeditor.fields.MDTextField(),
        ),
    ]