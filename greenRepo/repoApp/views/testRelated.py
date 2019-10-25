from django.core.exceptions import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from urllib.parse import parse_qs
from repoApp.models.testRelated import *
# from time import gmtime, strftime
from django.db import IntegrityError
import datetime
from rest_framework.exceptions import ValidationError as DRFValidationError

from repoApp.serializers.testRelatedSerializers import *
from repoApp.serializers.appRelatedSerializers import MethodSerializer
from repoApp.serializers.metricRelatedSerializers import MethodMetricSerializer, TestMetricSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from repoApp.models.models import TokenModel
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# /tests/
class TestsListView(APIView):
    serializer_class = TestSerializer
    @method_decorator(login_required)
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Test.objects.all()
        if 'test_application' in query:
            results=results.filter(test_application=query['test_application'][0])
        if 'test_tool' in query:
            results=results.filter(test_tool=query['test_tool'][0])
        if 'test_orientation' in query:
            try:
                orient=TestOrientation.objects.get(test_orientation_designation=query['test_orientation'][0])
                results=results.filter(test_orientation=orient.test_orientation_designation)
            except ObjectDoesNotExist:
                pass  
        #results = Test.objects.filter(reduce(and_, q)) 
        serialize = TestSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request):
        data = request.data
        if isinstance(data,list):
            ids_to_retrieve = []
            for item in data:
                serializer = TestSerializer(data=item, many=False, partial=True)
                if serializer.is_valid(raise_exception=True):
                    try:
                        instance = serializer.create(serializer.validated_data)
                        xx = instance.save()
                        ids_to_retrieve.append(xx.id)
                    except IntegrityError as e:
                        obj = Test.objects.get(test_application=serializer.validated_data['test_application'],test_tool=serializer.validated_data['test_tool'],test_orientation=serializer.validated_data['test_orientation'])
                        ids_to_retrieve.append(obj.id)
                    except Exception as ex:
                        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                        message = template.format(type(ex).__name__, ex.args)
                        print(message)
                        continue
                else:
                    return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)
            objs = Test.objects.filter(id__in=ids_to_retrieve)
            total=TestSerializer(objs,many=True)
            return Response(total.data, HTTP_200_OK)
            if total.is_valid(raise_exception=True):
                return Response(total, HTTP_200_OK)
            else:
                return Response(status=HTTP_400_BAD_REQUEST)
        else:
            serializer = TestSerializer(data=data, many=False, partial=True)
            if serializer.is_valid(raise_exception=True):
                try:
                    instance = serializer.create(serializer.validated_data)
                    instance.save()
                    return Response(TestSerializer(instance, many=False).data, HTTP_200_OK)
                except IntegrityError as e:
                    obj = Test.objects.get(test_application=serializer.validated_data['test_application'],test_tool=serializer.validated_data['test_tool'],test_orientation=serializer.validated_data['test_orientation'])
                    return Response(TestSerializer(obj, many=False).data, HTTP_200_OK)     
        return Response('Internal error or malformed JSON ', HTTP_200_OK)

# /tests/<test_id>/results/
class ResultsTestListView(APIView):
    serializer_class = TestResultsWithMetricsSerializer
    @method_decorator(login_required)
    def get(self, request,testid):
        query=parse_qs(request.META['QUERY_STRING'])
        results = TestResults.objects.all()
        if 'test_results_seed' in query:
            results=results.filter(test_results_seed=query['test_results_seed'][0])
        if 'test_results_id' in query:
            results=results.filter(test_results_id=query['test_results_id'][0])
        if 'test_results_profiler' in query:
            results=results.filter(test_results_profiler=query['test_results_profiler'][0])
        if 'test_results_device_state' in query:
            results=results.filter(test_results_device_state=query['test_results_device_state'][0])
        if 'test_results_description' in query:
            results=results.filter(test_results_description__contains=query['test_results_description'][0])
        serializer = TestResultsWithMetricsSerializer(results, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request,testid):
        data = request.data 
        if isinstance(data,list):
            for item in data:
                try:
                    instance = TestResultsSerializer(data=item, many=False, partial=True)
                    if instance.is_valid(raise_exception=True):
                        instance.save()
                except Exception as e:
                    continue
            return Response(data, HTTP_200_OK)
        else:
            instance = TestResultsSerializer(data=data, many=False, partial=True)
            try:
                if instance.is_valid(raise_exception=True):
                    instance.save()
            except Exception as e:
                pass
            return Response(instance.data, HTTP_200_OK)
        return Response(instance.data, HTTP_200_OK)


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


# /
class ResultsListView(APIView):
    serializer_class = TestResultsSerializer
    @method_decorator(login_required)
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = TestResults.objects.all()
        if 'test_results_seed' in query:
            results=results.filter(test_results_seed=query['test_results_seed'][0])
        if 'test_results_id' in query:
            results=results.filter(test_results_id=query['test_results_id'][0])
        if 'test_results_profiler' in query:
            results=results.filter(test_results_profiler=query['test_results_profiler'][0])
        if 'test_results_device' in query:
            results=results.filter(test_results_device=query['test_results_device'][0])
        if 'test_results_description' in query:
            results=results.filter(test_results_description__contains=query['test_results_description'][0])
        serializer = TestResultsSerializer(results, many=True)
        return Response(serializer.data, HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MethodMetricSerializer(data=data,many=isinstance(data, list), partial=True)
        if isinstance(data,list):
            for item in data:
                try:
                    #item['metric']=item['metric'].lower()
                    instance = TestResultsSerializer(data=item, many=False, partial=True)
                    if instance.is_valid(raise_exception=True):
                        instance.save()
                except Exception as e:
                    continue
            return Response(data, HTTP_200_OK)
        else:
            instance = TestResultsSerializer(data=data, many=False, partial=True)
            if instance.is_valid(raise_exception=True):
                instance.save()
                Response(instance.data, HTTP_200_OK)
            return Response(instance.data, HTTP_200_OK)

# tests/metrics/
class TestMetricsListView(APIView):
    serializer_class = TestMetricSerializer
    @method_decorator(login_required)
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = TestMetric.objects.all()
        if 'test_metric' in query:
            results=results.filter(metric=query['test_metric'][0])
        if 'test_value_text' in query:
            results=results.filter(value_text=query['test_value_text'][0])
        if 'test_results' in query:
            results=results.filter(test_results=query['test_results'][0])
        serialize = TestMetricSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request):
        data = request.data
        if isinstance(data,list):
            for item in data:
                try:
                    item['metric']= item['metric'].lower()
                    instance = TestMetricSerializer(data=item, many=False, partial=True)
                    if instance.is_valid(raise_exception=True):
                        instance.save() 
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
                    continue
            return Response(data, HTTP_200_OK)
        else:
            instance = TestMetricSerializer(data=data, many=False, partial=True)
            try:
                if instance.is_valid(raise_exception=True):
                    instance.save()
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                pass
            return Response(instance.data, HTTP_200_OK)
        return Response(instance.data, HTTP_200_OK)


# /tests/results/
class TestResultsListView(APIView):
    serializer_class = TestResultsSerializer
    @method_decorator(staff_member_required)
    def post(self, request):
        data = request.data
        serializer = TestResultsSerializer(data=data, many=isinstance(data,list), partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                #erialize = TestResultsSerializer(instance, many=isinstance(data,list))
                return Response(serializer.data, HTTP_200_OK)
            else:
                return Response('Internal error or malformed JSON ', HTTP_200_OK)
        except DRFValidationError as ex:
            # already exists
            print(data)
            result = TestResults.objects.get(test_results_unix_timestamp=data["test_results_unix_timestamp"])
            serialize = TestResultsSerializer(result, many=False)
            return  Response(serialize.data, HTTP_200_OK)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return Response('Internal error or malformed JSON ', HTTP_200_OK)
            




