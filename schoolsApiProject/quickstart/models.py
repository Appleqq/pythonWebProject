from django.db import models


class Schools(models.Model):

    school_id = models.CharField(max_length=100)
    province_id = models.CharField(max_length=100)
    max = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    filing = models.CharField(max_length=100)
    average = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    batch = models.CharField(max_length=200)
    min_section = models.CharField(max_length=100)
    add_id = models.CharField(max_length=100)
    local_batch_name = models.CharField(max_length=100)
    proscore = models.CharField(max_length=100)


    class Meta:
        ordering = ('school_id',)