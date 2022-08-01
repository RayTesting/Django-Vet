# Generated by Django 4.0.6 on 2022-07-28 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='home.customer')),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='services.service')),
            ],
        ),
    ]