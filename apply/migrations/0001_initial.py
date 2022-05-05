# Generated by Django 2.2.24 on 2022-04-25 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('ApplyId', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ApplierId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applierId', to='account.Jobseeker')),
                ('EmployerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employerId', to='account.Employer')),
                ('PostId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.Jobs')),
            ],
        ),
    ]