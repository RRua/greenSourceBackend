from rest_framework import serializers

from repoApp.models.appRelated import *
from repoApp.models.metricsRelated import *
from repoApp.serializers.metricRelatedSerializers import MethodMetricSerializer
from django.utils import timezone

class ApplicationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        obj = Application.objects.create(**validated_data)
        obj.app_build_tool= obj.app_build_tool.lower()
        obj.save()
        return obj
    class Meta:
        model = Application
        fields = ('app_id', 'app_location', 'app_description', 'app_language','app_build_tool','app_version','app_flavor','app_build_type')
        validators = []


#class ProjectTypeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = ProjectType
#        fields = ('project_type_id', 'project_type_designation')


class AppPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPermission
        fields = ('name')

class ImportClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportClass
        fields = ('import_name', 'import_class')



class AppPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPermission
        fields = ('name')



class ClassListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        tm = [Class(**item) for item in validated_data]
        return Class.objects.bulk_create(tm)



class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        list_serializer_class =ClassListSerializer
        fields = ('class_id', 'class_name', 'class_package', 'class_non_acc_mod',
            'class_app', 'class_acc_modifier', 'class_superclass', 'class_is_interface' ,'class_implemented_ifaces')
        validators = []

#TODO classwithImportsSerializer

class ClassWithImportsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ClassWithImportsSerializer, self).__init__(*args, **kwargs) 
        self.fields['class_imports'] = serializers.SerializerMethodField()
     
    def get_class_imports(self, classe):
        met = ImportClass.objects.filter(import_class=classe.import_class)
        return ImportClassSerializer(instance=met,  many=True).data  

    class Meta:
        model = Class
        list_serializer_class =ClassListSerializer
        fields = ('class_id', 'class_name', 'class_package', 'class_non_acc_mod',
            'class_app', 'class_acc_modifier', 'class_superclass', 'class_is_interface' ,'class_implemented_ifaces')
        validators = []

class AppHasPermissionListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        perms=[]
        for item in validated_data:
            try:
                m = AppHasPermission(**item)
                perms.append(m)
            except Exception as e:
                continue
        return AppHasPermission.objects.bulk_create(perms)


class AppHasPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = AppHasPermissionListSerializer
        model = AppHasPermission
        fields = ('application', 'permission')
        validators = []

#class TestCaseSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = TestCase
#        fields = ('test_case_id', 'test_case_name', 'test_case_framework', 'test_case_version', 'test_file')




class MethodListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        methods = []
        for item in validated_data:
            try:
                m = Method(**item)
                m.save()
            except Exception as e:
                continue
        return True


class MethodWithMetricsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(MethodWithMetricsSerializer, self).__init__(*args, **kwargs) 
        self.fields['method_metrics'] = serializers.SerializerMethodField()
     
    def get_method_metrics(self, method):
        met = MethodMetric.objects.filter(mm_method=method.method_id)
        return MethodMetricSerializer(instance=met,  many=True).data  

    class Meta:
        model = Method
        #list_serializer_class = MethodListSerializer
        fields = ('method_id', 'method_name','method_acc_modifier', 'method_non_acc_mod','method_class')
        validators = []


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        list_serializer_class = MethodListSerializer
        fields = ('method_id', 'method_name', 'method_class','method_acc_modifier', 'method_non_acc_mod')
        validators = []

