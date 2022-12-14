# Generated by Django 3.0.7 on 2020-06-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20200621_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='College',
            field=models.CharField(choices=[('IITDH', 'IIT Dharwad'), ('IITH', 'IIT Hyderabad'), ('IITGoa', 'IIT Goa'), ('IITBH', 'IIT Bhilai'), ('IITRPR', 'IIT Ropar'), ('IITR', 'IIT Roorkee'), ('IITKGP', 'IIT kharagpur'), ('IITJ', 'IIT Jodhpur'), ('IITTP', 'IIT Tirupati'), ('IITB', 'IIT Bombay'), ('IITP', 'IIT Patna'), ('IIT(ISM)', 'IIT (ISM) Dhanbad'), ('IITK', 'IIT Kanpur'), ('IITGN', 'IIT Gandhinagar'), ('IITM', 'IIT Madras'), ('IITJMU', 'IIT Jammu'), ('IITMandi', 'IIT Mandi'), ('IITD', 'IIT Delhi'), ('IITG', 'IIT Guwahati'), ('IIT (BHU)', 'IIT (BHU) Varanasi'), ('IITBBS', 'IIT Bhubaneswar'), ('IITI', 'IIT Indore'), ('IITPKD', 'IIT Palakkad')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Furniture', 'Furniture'), ('Books&Sports', 'Books&Sports'), ('Bicycle', 'Bicycle'), ('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Others', 'Others'), ('Mobiles', 'Mobiles')], max_length=100),
        ),
    ]
