from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from urllib.parse import parse_qs
from repoApp.models.testRelated import *
from repoApp.models.appRelated import *
from repoApp.models.metricsRelated import *
# from time import gmtime, strftime
from django.db import IntegrityError
from django.core.exceptions import ValidationError
import datetime
from repoApp.serializers.testRelatedSerializers import *
from repoApp.serializers.appRelatedSerializers import *
from repoApp.serializers.metricRelatedSerializers import *


class AppsListView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Application.objects.all()
        if 'id' in query:
            results=results.filter(app_id=query['id'][0])
        if 'language' in query:
            results=results.filter(app_language=query['language'][0])
        if 'build_tool' in query:
            results=results.filter(app_build_tool=query['build_tool'][0])
        if 'version' in query:
            results=results.filter(app_version=query['version'][0])
        if 'flavor' in query:
            results=results.filter(app_flavor=query['flavor'][0])
        serialize = ApplicationSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


    def post(self, request):
        data = JSONParser().parse(request)
        try: 
            serializer = ApplicationSerializer(data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
    
                instance = serializer.create(serializer.validated_data)
                instance.save()
                serialize = ApplicationSerializer(instance, many=False)
                return Response(serialize.data, HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)
        

class AppsDetailView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        try:
            results = Application.objects.get(app_id=appid)
        except ObjectDoesNotExist:
             return Response("Application not present in database", HTTP_400_BAD_REQUEST)  
        serialize = ApplicationSerializer(results, many=False)
        return Response(serialize.data, HTTP_200_OK)

class AppsTestsView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Test.objects.filter(test_application=appid)
        if 'test_tool' in query:
            results=results.filter(test_tool=query['test_tool'][0].lower())
        if 'test_orientation' in query:
            results=results.filter(test_orientation=query['test_orientation'][0].lower())
        serialize = TestSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


class AppsTestResultsView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        tests = Test.objects.filter(test_application=appid)
        if 'test_tool' in query:
            tests=tests.filter(test_tool=query['test_tool'][0].lower())
        if 'test_orientation' in query:
            tests=tests.filter(test_orientation=query['test_orientation'][0].lower())
        results = TestResults.objects.filter(test_results_test__in=tests.values('id'))
        if 'device' in query:
            results=results.filter(test_results_device=query['device'][0])
        if 'profiler' in query:
            results=results.filter(test_results_profiler=query['profiler'][0])
        if 'seed' in query:
            results=results.filter(test_results_seed=query['seed'][0])
        serialize = TestResultsWithMetricsSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)


class AppsClassListView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Class.objects.filter(class_app=appid)
        if 'package' in query:
            results=results.filter(class_package=query['package'][0].lower())
        if 'name' in query:
            results=results.filter(class_name=query['name'][0].lower())
        if 'class_non_acc_mod' in query:
            results=results.filter(class_class_non_acc_mod=query['class_non_acc_mod'][0])
        if 'superclass' in query:
            results=results.filter(class_superclass=query['superclass'][0])
        serialize = ClassSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    def post(self, request,appid):
        data = JSONParser().parse(request)
        serializer = ClassSerializer(data=data, many=isinstance(data,list), partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                if isinstance(data,list):
                    for item in data:
                        try:
                            print("ulha")
                            print(item)
                            instance = ClassSerializer(data=item, many=False, partial=True)
                            if instance.is_valid(raise_exception=True):
                                instance.save()
                            #serializer = TestSerializer(instance, many=isinstance(data,list))
                        except Exception as e:
                            print(e)
                            continue
                    return Response(serializer.data, HTTP_200_OK)
                else:
                    try:
                        instance = serializer.create(serializer.validated_data)
                        instance.save()
                        print("seixo")
                    except Exception as e:
                         Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)
            return Response(serializer.data, HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.data, HTTP_200_OK)


class ResultsTestListView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        try:
            res = AppMetric.objects.filter(am_app=appid)
        except ObjectDoesNotExist as e:
            return Response('The specified time restriction doesnt exist for that space', status=HTTP_400_BAD_REQUEST)
        serializer = TestResultsFullSerializer(res, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


    def post(self, request):
        return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)


class AppsMethodsListView(APIView):
    def get(self, request,appid):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Method.objects.all()
        classes = Class.objects.filter(class_app=appid)
        if 'class_name' in query:
            classes=classes.filter(class_name=query['class_name'][0])
        if 'method_name' in query:
            results=results.filter(method_name=query['method_name'][0])
        results = results.filter(method_class__in=classes.values('class_id'))
        serialize = MethodSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

class AppsMethodsDetailView(APIView):
    def get(self, request,appid,methodid):
        query=parse_qs(request.META['QUERY_STRING'])
        classes = Class.objects.filter(class_app=appid)
        results = Method.objects.filter(method_class__in=classes.values('class_id'))
        results = results.filter(method_name=methodid)
        serialize = MethodWithMetricsSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)



class MethodsListView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Method.objects.all()
        metrics=MethodMetric.objects.all()
        if 'class' in query:
            results=results.filter(method_class=query['class'][0])
        if 'method' in query:
            results=results.filter(method_name=query['method'][0])
        if 'metric' in query:
            try:
                metrics=metrics.filter(mm_method__in=results.values('method_id'),mm_metric=query['metric'][0])
                results=results.filter(method_id__in=metrics.values('mm_method'))
            except ObjectDoesNotExist:
                pass
        if 'metric_value' in query:
            try:
                metrics=metrics.filter(mm_method__in=results.values('method_id'),mm_value=query['metric_value'][0])
                results=results.filter(method_id__in=metrics.values('mm_method'))
            except ObjectDoesNotExist:
                pass 
        if 'metric_value_gte' in query:
            try:
                metrics=metrics.filter(mm_method__in=results.values('method_id'),mm_value__gte=query['metric_value_gte'][0])
                results=results.filter(method_id__in=metrics.values('mm_method'))
            except ObjectDoesNotExist:
                pass  
        serialize = MethodSerializer(results, many=True)
        if 'metric_value_lte' in query:
            try:
                metrics=metrics.filter(mm_method__in=results.values('method_id'),mm_value__lte=query['metric_value_lte'][0])
                results=results.filter(method_id__in=metrics.values('mm_method'))
            except ObjectDoesNotExist:
                pass  
        serialize = MethodWithMetricsSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MethodSerializer(data=data, many=isinstance(data,list), partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                if isinstance(data,list):
                    for item in data:
                        try:
                            instance = MethodSerializer(data=item, many=False, partial=True)
                            if instance.is_valid(raise_exception=True):
                                instance.save()
                            #serializer = TestSerializer(instance, many=isinstance(data,list))
                        except Exception as e:
                            print(e)
                            continue
                return Response(serializer.data, HTTP_200_OK)
            else:
                return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.data, HTTP_200_OK)


class MethodMetricsView(APIView):
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Method.objects.all()
        if 'app_id' in query:
            results=results.filter(application=query['app_id'][0])
        if 'permission' in query:
            results=results.filter(permission=query['permission'][0].lower())
        serialize = MethodWithMetricsSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        #print(data)
        serializer = MethodMetricSerializer(data=data,many=isinstance(data, list), partial=True)
        if serializer.is_valid(raise_exception=True):
            if isinstance(data,list):
                for item in data:
                    try:
                        instance = MethodMetricSerializer(data=item, many=False, partial=True)
                        if instance.is_valid(raise_exception=True):
                            instance.save()
                        #serializer = TestSerializer(instance, many=isinstance(data,list))
                    except IntegrityError as e:
                        continue
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)


class MethodInvokedListView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MethodInvokedSerializer(data=data, many=isinstance(data,list), partial=True)
        if serializer.is_valid(raise_exception=True):
            if isinstance(data,list):
                for item in data:
                    try:
                        instance = MethodInvokedSerializer(data=item, many=False, partial=True)
                        if instance.is_valid(raise_exception=True):
                            instance.save()
                        #serializer = TestSerializer(instance, many=isinstance(data,list))
                    except IntegrityError as e:
                        continue
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)




class AppHasPermissionListView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = AppHasPermissionSerializer(data=data, many=isinstance(data,list), partial=True)
        if serializer.is_valid(raise_exception=True):
            if isinstance(data,list):
                for item in data:
                    try:
                        instance = AppHasPermissionSerializer(data=item, many=False, partial=True)
                        if instance.is_valid(raise_exception=True):
                            instance.save()
                        #serializer = TestSerializer(instance, many=isinstance(data,list))
                    except IntegrityError as e:
                        continue
            return Response(serializer.data, HTTP_200_OK)
        else:
            return Response('Internal error or malformed JSON ', HTTP_400_BAD_REQUEST)

    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = AppHasPermission.objects.all()
        if 'app_id' in query:
            results=results.filter(application=query['app_id'][0])
        if 'permission' in query:
            results=results.filter(permission=query['permission'][0].lower())
        serialize = AppHasPermissionSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

