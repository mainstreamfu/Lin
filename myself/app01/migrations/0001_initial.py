# Generated by Django 2.2.2 on 2019-06-26 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('memo', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=32)),
                ('cid', models.ManyToManyField(null=True, to='app01.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=16)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app01.Class')),
                ('detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.StudentDetail')),
            ],
        ),
    ]