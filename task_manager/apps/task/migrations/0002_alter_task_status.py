# Generated by Django 4.0.5 on 2022-08-31 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='status', to='status.status', verbose_name='status'),
        ),
    ]
