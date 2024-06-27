# Generated by Django 4.1.13 on 2024-06-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=512, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=512, null=True)),
                ('topic', models.CharField(blank=True, max_length=512, null=True)),
                ('insight', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=512, null=True)),
                ('region', models.CharField(blank=True, max_length=512, null=True)),
                ('start_year', models.CharField(blank=True, max_length=512, null=True)),
                ('impact', models.CharField(blank=True, max_length=512, null=True)),
                ('added', models.CharField(blank=True, max_length=512, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=512, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(blank=True, max_length=512, null=True)),
                ('source', models.CharField(blank=True, max_length=512, null=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
