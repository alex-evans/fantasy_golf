# Generated by Django 3.0.4 on 2020-03-12 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Golfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['tournament', 'group_name'],
            },
        ),
        migrations.CreateModel(
            name='GroupGolfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Golfer')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Group')),
            ],
            options={
                'ordering': ['group', 'golfer'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MemberPick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_golfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.GroupGolfer')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Member')),
            ],
            options={
                'ordering': ['member', 'group_golfer'],
            },
        ),
        migrations.AddField(
            model_name='group',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
    ]