# Generated by Django 4.2.2 on 2023-06-23 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_factura_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='codigo_factura',
            new_name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
    ]
