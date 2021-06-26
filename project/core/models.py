from django.db import models

from django.contrib.postgres.fields import JSONField


class UserActivities(models.Model):
    id_user = models.IntegerField()
    ref_year = models.IntegerField()
    data = JSONField()

    class Meta:
        db_table = "user_activities"
        constraints = [
            models.UniqueConstraint(
                fields=['id_user', 'ref_year'], name='unique_activiti'
            ),
        ]

    def __str__(self):
        return f'User: {self.id_user} - {self.ref_year}'
