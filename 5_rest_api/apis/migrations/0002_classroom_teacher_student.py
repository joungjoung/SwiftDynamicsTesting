from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_class', models.CharField(max_length=20)),
                ('sub_class', models.CharField(max_length=20)),
                ('school', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='classrooms', to='apis.school')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('classrooms', models.ManyToManyField(blank=True, related_name='teachers', to='apis.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('classroom', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='students', to='apis.classroom')),
            ],
        ),
    ]