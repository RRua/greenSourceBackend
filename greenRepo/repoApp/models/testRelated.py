from django.db import models
from django.utils.timezone import now
from enumfields import EnumField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from repoApp.models.appRelated import *



class TestOrientation(models.Model):
    #test_orientation_id = models.AutoField(primary_key=True)
    def save(self, *args, **kwargs):
        self.test_orientation_designation = self.test_orientation_designation.lower()
        return super(TestOrientation, self).save(*args, **kwargs)
    test_orientation_designation = models.CharField(max_length=20,primary_key=True)

# The testing tool/framework used to test the application
class Tool(models.Model):
    tool_name = models.CharField(max_length=70, primary_key=True)
    def save(self, *args, **kwargs):
        self.tool_name = self.tool_name.lower()
        return super(Tool, self).save(*args, **kwargs)


class ProfilerType(Enum):
    HARDWARE_BASED = 'h'
    MODEL_BASED = 'm'
    SOFTWARE_BASED = 's'

class Profiler(models.Model):
    profiler_name = models.CharField(max_length=70, primary_key=True)
    profiler_type = EnumField(ProfilerType, max_length=1)
    profiler_version = models.FloatField(default=1.0)
    def save(self, *args, **kwargs):
        self.profiler_name = self.profiler_name.lower()
        return super(Profiler, self).save(*args, **kwargs)

#m = Profiler.objects.filter(profiler_type=ProfilerType.HARDWARE_BASED)

class Device(models.Model):
    device_serial_number = models.CharField(max_length=32,primary_key=True)
    device_brand = models.CharField(max_length=32)
    device_model = models.CharField(max_length=32)
    device_ram = models.CharField(max_length=16,default=None,null=True)
    device_cores = models.IntegerField(default=1)
    device_max_cpu_freq = models.CharField(max_length=8)
    def save(self, *args, **kwargs):
        self.device_brand = self.device_brand.lower().replace(" ", "")
        self.device_model = self.device_model.lower().replace(" ", "")
        return super(Device, self).save(*args, **kwargs)



class DeviceState(models.Model):
    class Meta:
        unique_together = (('state_device_id','state_kernel_version'),)
    state_id = models.AutoField(primary_key=True)
    state_date = models.DateTimeField(default=now)
    state_kernel_version = models.CharField(max_length=224,default=None, null=True)
    state_os_version = models.CharField(max_length=16,default=None, null=True)
    state_miui_version = models.CharField(max_length=16, default=None,null=True)
    state_api_version  = models.FloatField(default=None,null=True)
    #state_keyboard = models.CharField(max_length=128,default=None, null=True)
    state_operator = models.CharField(max_length=128,default=None, null=True)
    state_operator_country = models.CharField(max_length=16,default="PT", null=True)
    state_device_id  = models.ForeignKey(Device, related_name='stateOf', on_delete=models.CASCADE)

class Test(models.Model):
    class Meta:
        unique_together = (('test_application', 'test_tool','test_orientation'),)
    test_application = models.ForeignKey(Application, related_name='tested_app', on_delete=models.CASCADE)
    test_tool = models.ForeignKey(Tool, related_name='used_tool', on_delete=models.CASCADE)
    test_orientation = models.ForeignKey(TestOrientation, related_name='test_type', on_delete=models.CASCADE)


class TestResults(models.Model):
    test_results_id = models.AutoField(primary_key=True)
    test_results_unix_timestamp = models.IntegerField(default=1, unique=True)
    test_results_seed = models.CharField(max_length=32, default="", blank=True, null=True)
    test_results_description = models.CharField(max_length=128, default="", blank=True, null=True)
    test_results_test= models.ForeignKey(Test, related_name='test', on_delete=models.CASCADE)
    test_results_profiler= models.ForeignKey(Profiler, related_name='profiledOn', on_delete=models.CASCADE)
    test_results_device_state= models.ForeignKey(DeviceState, related_name='testedOn', on_delete=models.CASCADE)
    #test_results_android_version = models.CharField(max_length=8, default=None, blank=True, null=True)
   

class MethodInvoked(models.Model):
    class Meta:
        unique_together = (('method','test_results'),)
    method = models.ForeignKey(Method, related_name='method', on_delete=models.CASCADE)
    test_results = models.ForeignKey(TestResults, related_name='results', on_delete=models.CASCADE)
    times_invoked = models.IntegerField(default=1)



   