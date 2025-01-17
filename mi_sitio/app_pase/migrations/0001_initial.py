# Generated by Django 3.1.7 on 2021-03-31 00:21

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(upload_to='')),
                ('latlng', djgeojson.fields.PointField()),
            ],
        ),
    ]
