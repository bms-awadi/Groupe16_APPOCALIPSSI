import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DataRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "requested_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("received", "Reçue"),
                            ("in_progress", "En cours de traitement"),
                            ("completed", "Répondue"),
                        ],
                        default="received",
                        max_length=20,
                    ),
                ),
                (
                    "responded_at",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "file_hash",
                    models.CharField(blank=True, max_length=64),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Demande SAR",
                "verbose_name_plural": "Demandes SAR",
                "ordering": ["-requested_at"],
            },
        ),
    ]
