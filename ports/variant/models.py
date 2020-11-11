from django.db import models
from django.urls import reverse


class Variant(models.Model):
    port = models.ForeignKey('port.Port', on_delete=models.CASCADE, related_name='variants')
    variant = models.CharField(max_length=100, default='')
    description = models.TextField(null=True)
    requires = models.TextField(null=True)
    conflicts = models.TextField(null=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        app_label = "variant"
        db_table = "variant"
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

    def get_absolute_url(self):
        return reverse('variant', args=[str(self.variant)])
