# Generated by Django 4.1.3 on 2022-11-13 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('descriptions', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='guruh',
            name='descriptions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='guruh',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='talabalar', to='crmapp.guruh'),
        ),
        migrations.CreateModel(
            name='Mavzu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('soat', models.CharField(max_length=10)),
                ('fan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fanlar', to='crmapp.fan')),
            ],
        ),
    ]
