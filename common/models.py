from django.db import models

class Job(models.Model):
    jobid = models.CharField(max_length=100)
    areaCodeText = models.CharField(max_length=100, default=None, blank=True, null=True)
    webUrl = models.CharField(max_length=200, default=None, blank=True, null=True)
    telecommuteOption = models.BooleanField(default=False)
    jobLength = models.CharField(max_length=50, default=None, blank=True, null=True)
    postedDate = models.DateField(default=None, blank=True, null=True)    
    freshnessDate = models.DateField(default=None, blank=True, null=True)
    creationDate = models.DateField(default=None, blank=True, null=True)
    firstActiveDate = models.DateField(default=None, blank=True, null=True)
    skills = models.CharField(max_length=500, default=None, blank=True, null=True)
    payRate = models.CharField(max_length=100, default=None, blank=True, null=True)
    travelRequiredMiles = models.CharField(max_length=100, default=None, blank=True, null=True)
    href = models.CharField(max_length=200, default=None, blank=True, null=True)
    compURL = models.CharField(max_length=200, default=None, blank=True, null=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    country = models.CharField(max_length=100, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    region = models.CharField(max_length=100, default=None, blank=True, null=True)
    postalCode = models.CharField(max_length=10, default=None, blank=True, null=True)


    def __unicode__(self):
        return self.name + "--" + self.title

    class Meta:
        db_table = "job"


