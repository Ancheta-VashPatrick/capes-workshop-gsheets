# Generated by Django 3.1.5 on 2022-08-13 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=40)),
                ('status', models.CharField(blank=True, choices=[('New', 'n'), ('Closing Soon', 'c'), ('Expired', 'e')], help_text='Opportunity status', max_length=20, null=True)),
                ('location', models.CharField(choices=[('Local', 'Local'), ('International', 'International')], max_length=40)),
                ('opportunity_type', models.CharField(choices=[('INTERNSHIP', 'INTERNSHIP'), ('ACADEME', 'ACADEME'), ('EMPLOYMENT', 'EMPLOYMENT')], max_length=40)),
                ('duration', models.CharField(max_length=40)),
                ('description', models.TextField(default='Insert description here')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
                'ordering': ['role'],
            },
        ),
    ]
