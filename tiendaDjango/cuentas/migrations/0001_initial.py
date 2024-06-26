# Generated by Django 5.0.4 on 2024-04-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreproducto', models.CharField(max_length=100)),
                ('descripcionproducto', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('especificaciones', models.TextField()),
                ('imagenes', models.ImageField(upload_to='productos/')),
            ],
        ),
    ]
