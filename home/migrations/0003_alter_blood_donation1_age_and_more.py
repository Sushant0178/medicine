# Generated by Django 5.1 on 2024-08-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blood_donation1_buy1_equipment_buy1_ngologin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_donation1',
            name='age',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='any_health_issue',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='blood_group',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='email',
            field=models.EmailField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='mobile_no',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='blood_donation1',
            name='weight',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='Manufacturing_date',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='address',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='email',
            field=models.EmailField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='expiry_date',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='medicine_name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='mobile_no',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='buy1',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='equipment_buy1',
            name='Equipment_name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='equipment_buy1',
            name='address',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='equipment_buy1',
            name='email',
            field=models.EmailField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='equipment_buy1',
            name='mobile_no',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='equipment_buy1',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='Username',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='address',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='email',
            field=models.EmailField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='fname',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='mobileno',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='ngo_start_date',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='ngologin',
            name='pass1',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='email',
            field=models.EmailField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='equipment_name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='mobile_no',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_equipment1',
            name='quantity',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='Manufacturing_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='email',
            field=models.EmailField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='expiry_date',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='medicine_name',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='mobile_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='upload_medicine1',
            name='quantity',
            field=models.CharField(max_length=90, null=True),
        ),
    ]