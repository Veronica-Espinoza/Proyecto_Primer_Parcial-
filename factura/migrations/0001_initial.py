# Generated by Django 4.2.2 on 2023-06-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_factura', models.IntegerField(null=True)),
                ('fecha', models.DateField(null=True)),
            ],
        ),
    ]
