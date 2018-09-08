from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from urllib.parse import parse_qs
from repoApp.models.testRelated import *
# from time import gmtime, strftime
from django.db import IntegrityError
import datetime
from repoApp.serializers.testRelatedSerializers import *
from repoApp.serializers.appRelatedSerializers import MethodSerializer
from repoApp.serializers.metricRelatedSerializers import MethodMetricSerializer, TestMetricSerializer

class TestsListView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Test.objects.all()
        if 'test_app' in query:
            print((query['test_app'])[0])
            results=results.filter(test_application=query['app_id'][0])
        if 'test_tool' in query:
            results=results.filter(test_tool=query['test_tool'][0])
        if 'test_orientation' in query:
            try:
                orient=TestOrientation.objects.get(test_orientation_id=query['test_orientation'][0])
                results=results.filter(test_orientation=orient.test_orientation_id)
            except ObjectDoesNotExist:
                pass  
        #results = Test.objects.filter(reduce(and_, q))
        serialize = TestSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TestSerializer(data=data, many=False, partial=True)
        if serializer.is_valid(raise_exception=True):
            try:
                print(serializer.validated_data)
                instance = serializer.create(serializer.validated_data)
                instance.save()
                serialize = TestSerializer(instance, many=False)
                return Response(serialize.data, HTTP_200_OK)
            except IntegrityError as e:
                #already exists
                obj = Test.objects.get(test_application=serializer.validated_data['test_application'],test_tool=serializer.validated_data['test_tool'],test_orientation=serializer.validated_data['test_orientation'])
                serialize = TestSerializer(obj, many=False)
                return Response(serialize.data, HTTP_200_OK)
            
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)


class ResultsTestListView(APIView):
    def get(self, request,testid):
        query=parse_qs(request.META['QUERY_STRING'])
        #TODO
        try:
            res = TestResults.objects.filter(test_results_test=testid)
        except ObjectDoesNotExist as e:
            return Response('The specified time restriction doesnt exist for that space', status=HTTP_400_BAD_REQUEST)
        serializer = TestResultsWithMetricsSerializer(res, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    def post(self, request,testid):
        data = JSONParser().parse(request)
        serializer = TestResultsSerializer(data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.create(serializer.validated_data)
            instance.save()
            serialize = TestResultsSerializer(instance, many=False)
            return Response(serialize.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)

def getMetrics(initial_data):
    metrics = []
    try:
        for x in initial_data:
            print(x)
            metric = x['method_metrics']
            serializer= MethodMetricSerializer (data=metric,many=isinstance(metric,list), partial=True)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.create(serializer.validated_data)
                instance.save()
    except Exception as e:
        raise e
        return

class ResultsListView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = TestResults.objects.all()
        serialize = TestResultsSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MethodMetricSerializer(data=data,many=isinstance(data, list), partial=True)
        #print(serializer)
        if serializer.is_valid(raise_exception=True):
            try:
                instance = serializer.create(serializer.validated_data)
                instance.save()
                return Response("Data saved", HTTP_200_OK)
            except Exception as e:
                raise e
                return Response("Error", HTTP_400_BAD_REQUEST)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)

class TestMetricsListView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = TestMetric.objects.all()
        if 'metric' in query:
            results=results.filter(metric=query['metric'][0])
        if 'value' in query:
            results=results.filter(value=query['value'][0])
        if 'value_text' in query:
            results=results.filter(value_text=query['value_text'][0])
        
        serialize = TestMetricSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TestMetricSerializer(data=data,many=isinstance(data, list), partial=True)
        #print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #erialize = TestResultsSerializer(instance, many=isinstance(data,list))
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)



class TestResultsListView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TestResultsSerializer(data=data, many=isinstance(data,list), partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #erialize = TestResultsSerializer(instance, many=isinstance(data,list))
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)





