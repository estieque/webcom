# Generated by Django 4.1.7 on 2023-02-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_progressbar_alter_aboutcontentone_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSeoSnippets',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_description', models.CharField(max_length=200)),
                ('meta_keyword', models.CharField(max_length=200)),
            ],
        ),
    ]
