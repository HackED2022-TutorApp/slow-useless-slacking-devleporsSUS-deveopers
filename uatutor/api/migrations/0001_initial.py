# Generated by Django 4.0.1 on 2022-01-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('description', models.TextField(max_length=150)),
                ('degree', models.CharField(choices=[('Ba/BSc.', 'Bachelors'), ('MSc', 'Master'), ('Phd', 'Doctoral')], max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('minor', models.CharField(blank=True, max_length=20, null=True)),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
    ]
