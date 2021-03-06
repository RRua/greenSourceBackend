from rest_framework import serializers
from repoApp.models.testRelated import *
from django.utils import timezone
from repoApp.serializers.metricRelatedSerializers import TestMetricSerializer
from repoApp.models.metricsRelated import TestMetric

class TestListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        tm = [Test(**item) for item in validated_data]
        return Test.objects.bulk_create(tm)

class TestSerializer(serializers.ModelSerializer):
    test_orientation = serializers.PrimaryKeyRelatedField(queryset=TestOrientation.objects.all())
    class Meta:
        model = Test
        list_serializer_class = TestListSerializer
        fields = ('id','test_application', 'test_tool', 'test_orientation')
        validators = []

class TestResultsListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        tm = [TestResults(**item) for item in validated_data]
        return TestResults.objects.bulk_create(tm)


class TestResultsWithMetricsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(TestResultsWithMetricsSerializer, self).__init__(*args, **kwargs)
        self.fields['test_metrics'] = serializers.SerializerMethodField()
        #self.fields['test_state_init'] = serializers.SerializerMethodField()
        #self.fields['test_state_end'] = serializers.SerializerMethodField()
     
    def get_test_metrics(self, test):
        met = TestMetric.objects.filter(test_results=test.test_results_id)
        return TestMetricSerializer(instance=met,  many=True).data  

    #def get_test_state_init(self, test):
     #   met = DeviceState.objects.get(device_state_id=test.test_results_device_begin_state.device_state_id)
     #   return DeviceStateSerializer(instance=met,  many=False).data  

    #def get_test_state_end(self, test):
    #    met = DeviceState.objects.get(device_state_id=test.test_results_device_end_state.device_state_id)
    #    return DeviceStateSerializer(instance=met,  many=False).data  

    class Meta:
        model = TestResults
        fields = ('test_results_id', 'test_results_unix_timestamp', 'test_results_seed', 
            'test_results_description', 'test_results_test', 'test_results_profiler',
            'test_results_device_state' )#, 'test_results_api_level' ,'test_results_android_version' ) #'test_init_mem', 'test_init_cpu_free',
           # 'test_init_nr_processes_running','test_end_mem', 'test_end_cpu_free',
           # 'test_end_nr_processes_running','test_results_api_level','test_results_android_version')
        validators = []

class TestResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResults
        list_serializer_class = TestResultsListSerializer
        fields = ('test_results_id', 'test_results_unix_timestamp', 'test_results_seed', 
            'test_results_description', 'test_results_test', 'test_results_profiler',
            'test_results_device_state' )
        validators = []

class TestOrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestOrientation
        fields = ('test_orientation_id', 'test_orientation_designation')


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ('tool_name')

class MethodInvokedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodInvoked
        fields = ('method','test_results', "times_invoked")
        validators = []

class ProfilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiler
        fields = ('profiler_name', 'profiler_type')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_serial_number','device_brand','device_model', 'device_cores','device_ram', 'device_max_cpu_freq')
        validators = []

class DeviceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceState
        fields = ('state_id','state_os_version','state_date','state_miui_version', 'state_kernel_version','state_api_version','state_device_id','state_operator','state_operator_country', 'state_nr_installed_apps')
        validators = []

#class DeviceStateSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = DeviceState
#        fields = ('device_state_id', 'device_state_mem', 'device_state_cpu_free','device_state_cpu_free','device_state_nr_processes_running','device_state_api_level','device_state_android_version')
