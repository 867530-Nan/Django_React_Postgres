# Generated by Django 2.1.4 on 2019-01-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_grams', '0002_auto_20190103_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('document', models.FileField(upload_to='document_upload/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
