# Generated by Django 4.1.7 on 2023-03-04 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolioseosnippets_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'Client Name'},
        ),
        migrations.AlterModelOptions(
            name='portfoliocategory',
            options={'verbose_name_plural': 'Project Categories'},
        ),
        migrations.AlterModelOptions(
            name='portfolios',
            options={'verbose_name_plural': 'portfolio Details'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Branch of Team'},
        ),
    ]
