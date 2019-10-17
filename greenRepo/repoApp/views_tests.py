from django.test import TestCase
#import unittest
from repoApp.models.appRelated import *
from repoApp.models.metricsRelated import *
from repoApp.models.testRelated import *
from repoApp.views.appRelated import AppsListView
from repoApp.serializers.appRelatedSerializers import *
from rest_framework.parsers import JSONParser
import json


def deleteAllModels():
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
    except Exception as e:
        print ("Error deleting previous models")
        print(e)



# /apps/
class ApplicationViewTestCase(TestCase):
    """ /apps/ """
    def __init__(self, arg):
        super(ApplicationViewTestCase, self).__init__()
        self.test_url="http://localhost:8000/apps/"
        self.json_project_str="""
            {
                "project_description":"",
                "project_id":"FutExam",
                "project_build_tool":"gradle",
                "project_location":"namek"
            }
        """
        self.json_app_str= """
             {
                "app_id": "FutExam--714809332",
                "app_package": "com.ruirua.futexam",
                "app_description": null,
                "app_version": "0.0",
                "app_flavor": null,
                "app_build_type": null,
                "app_project": "FutExam"
            }       
        """
        deleteAllModels()

    def setUp(self):
        json_proj_obj=json.loads(self.json_project_str)
        serialized_proj_obj = AndroidProjectSerializer(data=json_proj_obj, many=False)
        if serialized_proj_obj.is_valid(raise_exception=True):
            serialized_proj_obj.save()
        json_app_obj=json.loads(self.json_app_str)
        serialized_obj = ApplicationSerializer(data=json_app_obj, many=False)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
    
    def tearDown(self):
        json_obj=json.loads(self.json_app_str)
        serialized_obj = ApplicationSerializer(data=json_obj, many=False)
        #Application.objects.delete(app_id=serialized_obj['app_id'])        

    def test_app_return(self):
        response = self.client.get(self.test_url, follow=True)
        serialized_response_obj = ApplicationSerializer(data=response.data[0], many=False)
        serialized_obj = ApplicationSerializer(data=json.loads(self.json_app_str), many=False)
        self.assertEqual(serialized_response_obj.initial_data, serialized_obj.initial_data)
    
    def runTest(self):
        self.test_app_return()
        
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ApplicationViewTestCase)
    unittest.TextTestRunner().run(suite)