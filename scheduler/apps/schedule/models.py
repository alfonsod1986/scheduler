from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.utils.translation import ugettext as _

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("Fecha de Creción"))
    updated_at = models.DateTimeField(auto_now=True, help_text=_("Fecha de modificación"))

    class Meta:
        abstract = True

class Property(TimeStampMixin):
    title = models.CharField(max_length= 255, verbose_name=_("Título"))
    address = models.TextField(verbose_name=_("Dirección"))
    description = models.TextField(verbose_name=_("Descripción"))
    disabled_at = models.DateTimeField(null=True, blank=True, default=None, help_text=_("Fecha de modificación"))
    status = models.CharField(max_length= 35, verbose_name=_("Status"))


    def __str__(self):
        return "{0} - {1}".format(self.id, self.title)

    class Meta:
        verbose_name = _("Propiedad")
        verbose_name_plural = _("Propiedades")


class Activity(TimeStampMixin):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name=_("Propiedad"))
    schedule = models.DateTimeField(help_text=_("Fecha de agenda"))
    title = models.CharField(max_length= 255, verbose_name=_("Título"))
    status = models.CharField(max_length= 35, verbose_name=_("Status"))

    def __str__(self):
        return "{0} - {1}".format(self.id, self.title)

    class Meta:
        verbose_name = _("Actividad")
        verbose_name_plural = _("Actividades")


class Survey(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=_("Actividad"))
    answers = JSONField(verbose_name=_("Respuestas"))
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("Fecha de Creción"))

    def __str__(self):
        return "{0} - {1}".format(self.id, self.activity_id.title)

    class Meta:
        verbose_name = _("Encuesta")
        verbose_name_plural = _("Encuestas")