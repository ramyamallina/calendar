# Generated by Django 5.0.4 on 2024-05-27 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=100)),
                ('agent_type', models.CharField(choices=[('Inbound', 'Inbound voice agent'), ('Outbound', 'Outbound voice agent'), ('Batch', 'Batch caller agent')], max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('csv_file', models.FileField(upload_to='csv_files/')),
                ('first_sentence', models.CharField(max_length=20)),
                ('business_info', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
    ]