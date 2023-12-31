# Generated by Django 4.2.2 on 2023-06-15 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purrfect', '0003_rename_categoria_id_producto_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purrfect.cargo')),
            ],
        ),
    ]
