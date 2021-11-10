# Generated by Django 3.2.9 on 2021-11-10 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=455)),
                ('remuneration', models.DecimalField(decimal_places=2, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('schooling', models.IntegerField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Ensino Superior')])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
    ]
