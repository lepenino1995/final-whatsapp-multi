# Generated by Django 5.1.4 on 2024-12-21 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('respuesta', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('respondida', models.BooleanField(default=False)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to=settings.AUTH_USER_MODEL)),
                ('jefe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]