from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

from pinax.badges.base import Badge, BadgeAwarded
from pinax.badges.registry import badges


class PointsBadge(Badge):
    slug = "points"
    levels = [
        "Bronze",
        "Silver",
        "Gold",
    ]
    events = [
        "points_awarded",
    ]
    multiple = False

    def award(self, **state):
        user = state["user"]
        points = user.profile.points
        if points > 15:
            return BadgeAwarded(level=3)
        elif points > 5:
            return BadgeAwarded(level=2)
        elif points > 0:
            return BadgeAwarded(level=1)


badges.register(PointsBadge)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    points = models.IntegerField(
        default=1
    )

    def award_points(self, points):
        self.points += points
        self.save()
