# Generated by Django 3.2 on 2023-02-13 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('pub_date',)},
        ),
    ]
