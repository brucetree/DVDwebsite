# Generated by Django 3.2.7 on 2021-11-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0019_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-updated_time', '-created_time'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
