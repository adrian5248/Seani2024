from django.db import models


class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa"
        )
    application_date = models.DateTimeField(
        verbose_name = "Fecha de aplicación")

    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero',
                'marzo', 'abril','mayo','junio',
                'julio','agosto','septiembre', 'octubre',
                'noviembre', 'diciembre']
        return months[self.application_date.month -1]


    def __str__(self):
        return f"{self.stage} - { self.month } { self.year}"

    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
