from django.db import models
from django.core.validators import MinValueValidator


class Invitee(models.Model):
    SIDE_ALEX = "alex"
    SIDE_DIVYA = "divya"
    SIDE_CHOICES = [
        (SIDE_ALEX, "Alex"),
        (SIDE_DIVYA, "Divya"),
    ]

    RELATION_DIVYA = "divya"
    RELATION_DAISY = "daisy"
    RELATION_DAVIS = "davis"
    RELATION_DIYA = "diya"
    RELATION_ALEX = "alex"
    RELATIONSHIP_CHOICES = [
        (RELATION_DIVYA, "Divya"),
        (RELATION_DAISY, "Daisy"),
        (RELATION_DAVIS, "Davis"),
        (RELATION_DIYA, "Diya"),
        (RELATION_ALEX, "Alex"),
    ]

    EVENT_ALL = "all"
    EVENT_ENGAGEMENT = "engagement"
    EVENT_WEDDING = "wedding"
    EVENT_CHOICES = [
        (EVENT_ALL, "All Events (Engagement & Wedding)"),
        (EVENT_ENGAGEMENT, "Engagement Only"),
        (EVENT_WEDDING, "Wedding Only"),
    ]

    name = models.CharField(max_length=200, help_text="Full name of guest or family group")
    side = models.CharField(max_length=20, choices=SIDE_CHOICES, default=SIDE_DIVYA)
    relationship = models.CharField(
        max_length=20,
        choices=RELATIONSHIP_CHOICES,
        default=RELATION_DIVYA,
        help_text="Primary relationship connection",
    )
    guest_count = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Number of guests",
    )
    events_invited = models.CharField(max_length=30, choices=EVENT_CHOICES, default=EVENT_ALL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Invitee"
        verbose_name_plural = "Invitees"

    def __str__(self):
        return f"{self.name} ({self.get_side_display()} - {self.get_relationship_display()}) [{self.guest_count}]"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "side": self.side,
            "side_display": self.get_side_display(),
            "relationship": self.relationship,
            "relationship_display": self.get_relationship_display(),
            "guest_count": self.guest_count,
            "events_invited": self.events_invited,
            "events_invited_display": self.get_events_invited_display(),
        }
