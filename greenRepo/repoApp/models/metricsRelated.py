from django.db import models
from enumfields import EnumField, Enum  # Uses Ethan Furman's "enum34" backport
from django.utils.timezone import now
from repoApp.models.appRelated import Application , Method, Class
from repoApp.models.testRelated import TestResults , MethodInvoked

 


class Study(models.Model):
    study_title = models.CharField(max_length=128,primary_key=True)
    study_authors = models.CharField(max_length=128)
    study_publisher = models.CharField(max_length=64)
    study_year = models.IntegerField()
    study_isbn = models.CharField(max_length=64)
    study_organization = models.CharField(max_length=32)
    def save(self, *args, **kwargs):
        self.study_title = self.study_title.lower()
        return super(Study, self).save(*args, **kwargs)


class MetricType(Enum):
    STATIC = 's'
    DYNAMIC = 'd'
    HYBRID = 'h'


class MetricCategory(Enum):
    API = 'a'
    PATTERN = 'p'
    HARDWARE = 'h'
    MEASURABLE = 'm'
    OTHER = 'o'



class Metric(models.Model):
    metric_name = models.CharField(max_length=32,primary_key=True)
    metric_type = models.CharField(max_length=1,choices=[(tag, tag.value) for tag in MetricType])
    metric_category = models.CharField(max_length=1,choices=[(tag, tag.value) for tag in MetricCategory])
    metric_related_study = models.ForeignKey(Study, related_name='accordingto', on_delete=models.CASCADE,default=None,null=True)
    def save(self, *args, **kwargs):
        self.metric_name = self.metric_name.lower()
        return super(Metric, self).save(*args, **kwargs)

class TestMetric(models.Model):
    class Meta:
        unique_together = (('test_results', 'metric'),)
    test_results = models.ForeignKey(TestResults, related_name='res', on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, related_name='metric', on_delete=models.CASCADE)
    #value = models.FloatField()
    value_text = models.CharField(max_length=384, default="")
    coeficient = models.CharField(max_length=16,default="",blank=True , null=True)
    #timestamp = models.DateTimeField(default=now)


class AppMetric(models.Model):
    class Meta:
        unique_together = (('am_app', 'am_metric','am_value_text'),)
    am_app = models.ForeignKey(Application, related_name='aapp', on_delete=models.CASCADE)
    am_metric = models.ForeignKey(Metric, related_name='ahasMetric', on_delete=models.CASCADE)
    #am_value = models.FloatField()
    am_value_text = models.CharField(max_length=384, default="")
    am_coeficient = models.CharField(max_length=16,default="",blank=True , null=True)  
    am_test_result = models.ForeignKey(TestResults, related_name='ammtest', on_delete=models.CASCADE,default=None,null=True)


class ClassMetric(models.Model):
    class Meta:
        unique_together = (('cm_class', 'cm_metric','cm_value_text'),)
    cm_class = models.ForeignKey(Class, related_name='classmetric', on_delete=models.CASCADE)
    cm_metric = models.ForeignKey(Metric, related_name='chasMetric', on_delete=models.CASCADE)
    #cm_value = models.FloatField()
    cm_value_text = models.CharField(max_length=512,default="")
    cm_coeficient = models.CharField(max_length=16,default="",blank=True , null=True)
    #cm_timestamp = models.DateTimeField( default=now)
    cm_test_result = models.ForeignKey(TestResults, related_name='cmmtest', on_delete=models.CASCADE,default=None,null=True)


class MethodMetric(models.Model):
    class Meta:
        unique_together = (('mm_method', 'mm_metric','mm_value_text'),)
    mm_method = models.ForeignKey(Method, related_name='mmmethod', on_delete=models.CASCADE)
    mm_metric = models.ForeignKey(Metric, related_name='mmmethodHasMetric', on_delete=models.CASCADE)
    #mm_value = models.FloatField()
    mm_value_text = models.CharField(max_length=384, default="")
    mm_coeficient = models.CharField(max_length=16,default="",blank=True , null=True)
    #mm_timestamp = models.DateTimeField(default=now)
    mm_test_result = models.ForeignKey(TestResults, related_name='mmmtest', on_delete=models.CASCADE,default=None,null=True)


    #mm_method_invoked = models.ForeignKey(MethodInvoked, related_name='mmmethodHasMetric', on_delete=models.CASCADE,default=None,null=True)

