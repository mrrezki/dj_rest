# Generated by Django 4.0.4 on 2022-05-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PRoduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=99.99, max_digits=15)),
            ],
        ),
    ]
