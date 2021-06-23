# Generated by Django 3.1.7 on 2021-06-23 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer')),
            ],
        ),
    ]