# Generated by Django 4.2.6 on 2024-01-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_countinstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='./static/images/placeholder(640x360).jpg', null=True, upload_to=''),
        ),
    ]
