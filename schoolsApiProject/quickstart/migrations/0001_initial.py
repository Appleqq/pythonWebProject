# Generated by Django 2.2.3 on 2019-07-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(max_length=100)),
                ('province_id', models.CharField(max_length=100)),
                ('max', models.CharField(max_length=100)),
                ('min', models.CharField(max_length=100)),
                ('filing', models.CharField(max_length=100)),
                ('average', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=200)),
                ('min_section', models.CharField(max_length=100)),
                ('add_id', models.CharField(max_length=100)),
                ('local_batch_name', models.CharField(max_length=100)),
                ('proscore', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('school_id',),
            },
        ),
    ]