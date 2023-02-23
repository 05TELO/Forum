from django.db import migrations


def apply_migration(apps, schema_editor):
    group = apps.get_model("auth", "group")
    group.objects.bulk_create(
        [
            group(name="user"),
            group(name="moderator"),
        ]
    )


def revert_migration(apps, schema_editor):
    group = apps.get_model("auth", "group")
    group.objects.filter(
        name__in=[
            "user",
            "moderator",
        ]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("app_forum", "0005_post_author_topic_author"),
    ]

    operations = [migrations.RunPython(apply_migration, revert_migration)]
