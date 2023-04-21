import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True)),
                (
                'publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User', null=True)),
                ('category', models.CharField(db_index=True, default='Mixed', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField(default='No Requirements')),
                ('salary', models.CharField(max_length=255, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
