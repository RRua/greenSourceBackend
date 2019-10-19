from django.core.management import call_command
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from repoApp.models.appRelated import *
from repoApp.models.metricsRelated import *
from repoApp.models.testRelated import *
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage


class PopulateDummyTest(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            a = AndroidProject()
            a.project_id="xxxx-dummy-xxxx-project-test"
            a.project_desc="dumb"
            a.project_build_tool="gradle"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Application()
            a.app_id="dummy_app"
            a.app_location="/Users/dummyUser/apps/dummyApp"
            a.app_description="dumb"
            a.app_language="java"
            a.app_version=1.1
            a.app_flavor="demo"
            a.app_project=AndroidProject.objects.get(project_id="xxxx-dummy-xxxx-project-test")
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Application()
            a.app_id="dummy_app2"
            a.app_location="/Users/dummyUser/apps/dummyApp2"
            a.app_description="dumb"
            a.app_language="java"
            a.app_version=1.1
            a.app_flavor="demo"
            a.app_project=AndroidProject.objects.get(project_id="xxxx-dummy-xxxx-project-test")
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Class()
            a.class_id="com.dummy.dummyapp.DummyActivity"
            a.class_name="DummyActivity"
            a.class_package="com.dummy.dummyapp"
            a.class_non_acc_mod=""
            a.class_app=Application.objects.get(app_id="dummy_app")
            a.class_acc_modifier="public"
            a.class_superclass="Activity"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = ImportClass()
            a.import_name="java.util.TreeMap"
            a.import_class=Class.objects.get(class_id="com.dummy.dummyapp.DummyActivity")
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Method()
            a.method_id="com.dummy.dummyapp.DummyActivity.dummyMethod"
            a.method_name="dummyMethod"
            a.method_non_acc_mod="static"
            a.method_class=Class.objects.get(class_id="com.dummy.dummyapp.DummyActivity")
            a.method_acc_modifier="public"
            a.method_args="int#String[]"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Method()
            a.method_id="com.dummy.dummyapp.DummyActivity.dummyMethod"
            a.method_name="dummyMethod"
            a.method_non_acc_mod="static"
            a.method_class=Class.objects.get(class_id="com.dummy.dummyapp.DummyActivity")
            a.method_acc_modifier="public"
            a.method_args="int#String[]"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Method()
            a.method_id="com.dummy.dummyapp.DummyActivity.dummyMethod2"
            a.method_name="dummyMethod2"
            a.method_non_acc_mod=""
            a.method_class=Class.objects.get(class_id="com.dummy.dummyapp.DummyActivity")
            a.method_acc_modifier="private"
            a.method_args="int#double"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Test()
            a.test_application=Application.objects.get(app_id="dummy_app")
            a.test_tool= Tool.objects.get(tool_name="monkey")
            a.test_orientation=TestOrientation.objects.get(test_orientation_designation="testoriented")
            a.save()
        except Exception as e:
            print(e)
        try:
            a = TestResults()
            a.test_results_seed="1893"
            a.test_results_description="dd"
            a.test_results_test=Test.objects.get(id=1)
            a.test_results_profiler=Profiler.objects.get(profiler_name="trepn")
            a.test_results_device=Device.objects.get(device_serial_number="X2222")
            a.test_results_device_begin_state=DeviceState.objects.get(device_state_id=1)
            a.test_results_device_end_state=DeviceState.objects.get(device_state_id=2)
            a.save()
        except Exception as e:
            print(e)
        try:
            a = TestMetric()
            a.test_results=TestResults.objects.get(test_results_id=1)
            a.metric=Metric.objects.get(metric_name="wifistate")
            a.value=1
            a.value_text="used"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = ClassMetric()
            a.cm_class=Class.objects.get(class_id="com.dummy.dummyapp.DummyActivity")
            a.cm_metric=Metric.objects.get(metric_name="totalenergy")
            a.cm_value=13
            a.cm_value_text="totalmethods"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = MethodMetric()
            a.mm_method=Method.objects.get(method_id="com.dummy.dummyapp.DummyActivity.dummyMethod")
            a.mm_metric=Metric.objects.get(metric_name="totalenergy")
            a.mm_value=13
            a.mm_value_text=""
            a.save()
        except Exception as e:
            print(e)
        try:
            a = AppMetric()
            a.am_app= Application.objects.get(app_id="dummy_app")
            a.am_metric=Metric.objects.get(metric_name="totalenergy")
            a.am_value=131
            a.am_value_text=""
            a.save()
        except Exception as e:
            print(e)

        return Response("DB Populated with dummy examples", HTTP_200_OK)



class PopulationReset(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            AppMetric.objects.all().delete()
            MethodMetric.objects.all().delete()
            ClassMetric.objects.all().delete()
            TestMetric.objects.all().delete()
            TestResults.objects.all().delete()
            Test.objects.all().delete()
            Method.objects.all().delete()
            ImportClass.objects.all().delete()
            Class.objects.all().delete()
            Application.objects.all().delete()
            AndroidProject.objects.all().delete()
            Metric.objects.all().delete()
            Application.objects.all().delete()
            AppPermission.objects.all().delete()
            DeviceState.objects.all().delete()            
            Device.objects.all().delete()
            #TestOrientation.objects.all().delete()
            #Profiler.objects.all().delete()
            pv = PopulateView()
            pv.post(request)
            #ptm = PopulateTestMetrics()
            #ptm.post(request)
        except Exception as e:
            print ("Error deleting previous models")
            print(e)

        return Response("DB reseted", HTTP_200_OK)



def saveMetric(name, tipo, category):
    # type = static(s), dynamic(d), hybrid (h)
    #API = 'a' , PATTERN = 'p ,HARDWARE = 'h' , MEASURABLE = 'm' ,OTHER = 'o'
    try:
        a = Metric()
        a.metric_name=name
        a.metric_type=tipo
        a.metric_category=category
        a.save()
    except Exception as e:
        print(e)




class PopulateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # method metrics
        saveMetric("api", 's', 'a')
        saveMetric("locals", 's', 'o')
        saveMetric("field", 's', 'o')
        saveMetric("length", 's', 'o')
        saveMetric("nr_instructions", 's', 'o')
        # class metrics
        saveMetric("implements", 's', 'o')
        saveMetric("superclass", 's', 'o')
        saveMetric("nr_methods", 's', 'o')
        
        #test metrics
        #trepn
        saveMetric("cpuloadnormalized", 'd', 'm')
        saveMetric("cpuload", 'd', 'm')
        saveMetric("cpu1load", 'd', 'm')
        saveMetric("cpu2load", 'd', 'm')
        saveMetric("cpu3load", 'd', 'm')
        saveMetric("cpu4load", 'd', 'm')
        saveMetric("cpu5load", 'd', 'm')
        saveMetric("cpu6load", 'd', 'm')
        saveMetric("cpu7load", 'd', 'm')
        saveMetric("cpu8load", 'd', 'm')
        saveMetric("cpufrequency", 'd', 'm')
        saveMetric("cpu1frequency", 'd', 'm')
        saveMetric("cpu2frequency", 'd', 'm')
        saveMetric("cpu3frequency", 'd', 'm')
        saveMetric("cpu4frequency", 'd', 'm')
        saveMetric("cpu5frequency", 'd', 'm')
        saveMetric("cpu6frequency", 'd', 'm')
        saveMetric("cpu7frequency", 'd', 'm')
        saveMetric("cpu8frequency", 'd', 'm')
        saveMetric("gpuload", 'h', 'm')
        saveMetric("gpufrequency", 'h', 'm')
        saveMetric("batteryremaining", 'd', 'm')
        saveMetric("batterypower", 'd', 'm')
        saveMetric("batterypowerdelta", 'd', 'm')
        saveMetric("BatteryStatus",'d','h')
        saveMetric("BatteryCharging",'d','h')
        saveMetric("screenstate",'d','h')
        saveMetric("screenbrightness", 'd', 'm')
        saveMetric("BluetoothState",'d','h')
        saveMetric("memoryusage", 'd', 'm')
        saveMetric("WifiRSSILevel",'d','h')
        saveMetric("WifiState",'d','h')
        saveMetric("MobileDataState",'d','m')
        saveMetric("gpsstate",'d','m')
        #anadroid
        saveMetric("elapsedtime",'d','m')
        saveMetric("energyconsumed",'d','m')
        saveMetric("begin_used_cpu",'d','m')
        #   init_test
        saveMetric("begin_used_cpu",'d','m')
        saveMetric("begin_used_mem_pss",'d','m')
        saveMetric("begin_used_mem_kernel",'d','m')
        saveMetric("begin_nr_procceses",'d','m')
        saveMetric("begin_ischarging",'d','m')
        saveMetric("begin_battery_level",'d','m')
        saveMetric("begin_battery_temperature",'d','m')
        saveMetric("begin_battery_voltage",'d','m')
        saveMetric("begin_keyboard",'d','m')
        #   end_test
        saveMetric("end_used_cpu",'d','m')
        saveMetric("end_used_mem_pss",'d','m')
        saveMetric("end_used_mem_kernel",'d','m')
        saveMetric("end_nr_procceses",'d','m')
        saveMetric("end_ischarging",'d','m')
        saveMetric("end_battery_level",'d','m')
        saveMetric("end_battery_temperature",'d','m')
        saveMetric("end_battery_voltage",'d','m')
        saveMetric("end_keyboard",'d','m')

        ######## TestOrientation
        try:
            a = TestOrientation()
            a.test_orientation_designation="methodoriented"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = TestOrientation()
            a.test_orientation_designation="testoriented"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = TestOrientation()
            a.test_orientation_designation="applicationtoriented"
            a.save()
        except Exception as e:
            print(e)
        ######## Tools
        try:
            a = Tool()
            a.tool_name="Junit"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Tool()
            a.tool_name="monkey"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Tool()
            a.tool_name="robotium"
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Tool()
            a.tool_name="monkeyrunner"
            a.save()
        except Exception as e:
            print(e)
        ######### Profiler
        try:
            a = Profiler()
            a.profiler_name="monsoon"
            a.profiler_type='h'
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Profiler()
            a.profiler_name="trepn"
            a.profiler_type='s'
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Profiler()
            a.profiler_name="odroid"
            a.profiler_type='h'
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Profiler()
            a.profiler_name="greendroid"
            a.profiler_type='s'
            a.save()
        except Exception as e:
            print(e)
        try:
            a = Profiler()
            a.profiler_name="power Tutor"
            a.profiler_type='m'
            a.save()
        except Exception as e:
            print(e)
        ########### Devices
        ########### Device
        ######## load all Permissions
        p = staticfiles_storage.path('all_permissions.txt')
        f = open(p, "r")
        content = f.readlines()
        for line in content: 
            new_line=line.lower().strip() #.replace("android.permission.","").lower().strip()
            try:
                a = AppPermission()
                a.name=new_line
                a.save()
            except Exception as e:
                print(e)

        return Response("nice", HTTP_200_OK)
       




