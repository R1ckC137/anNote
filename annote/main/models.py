from django.db import models
import random
import string


class Annote(models.Model):
    objects = None
    link = models.TextField()
    annote = models.TextField('annote')
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'anNote'
        verbose_name_plural = 'anNotes'

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        super(Annote, self).save(*args, **kwargs)
