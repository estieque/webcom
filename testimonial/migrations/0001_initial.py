# Generated by Django 4.1.7 on 2023-03-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('tmo_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('client_designatiion', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='clients/')),
                ('client_message', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]
