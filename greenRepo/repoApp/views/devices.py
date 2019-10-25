from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from urllib.parse import parse_qs
from repoApp.models.testRelated import *
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
# from time import gmtime, strftime
from django.db import IntegrityError
import datetime
from repoApp.serializers.testRelatedSerializers import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

class DevicesListView(APIView):
    serializer_class = DeviceSerializer
    #'device_serial_number','device_brand','device_model'
    @method_decorator(login_required)
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = Device.objects.all()
        if 'device_serial_number' in query:
            results=results.filter(device_serial_number=query['device_serial_number'][0])
        if 'device_brand' in query:
            results=results.filter(device_brand=query['device_brand'][0])
        if 'device_model' in query:
            results=results.filter(device_model=query['device_model'][0])
        #results = Test.objects.filter(reduce(and_, q))
        serialize = DeviceSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request):
        data = request.data
        if isinstance(data,list):
            for item in data:
                try:
                    instance = DeviceSerializer(data=item, many=False, partial=True)
                    if instance.is_valid(raise_exception=True):
                        instance.save()
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    print(message)
            return Response(data, HTTP_200_OK)
        else:
            instance = DeviceSerializer(data=data, many=False, partial=True)
            try:
                if instance.is_valid(raise_exception=True):
                    instance.save()
            except DRFValidationError as ex:
                return Response(data, HTTP_200_OK) 
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                return Response("", HTTP_400_BAD_REQUEST)
        return Response(instance.data, HTTP_200_OK)


class DeviceStateView(APIView):
    #'device_serial_number','device_brand','device_model'
    serializer_class = DeviceStateSerializer
    @method_decorator(login_required)
    def get(self, request):
        query=parse_qs(request.META['QUERY_STRING'])
        results = DeviceState.objects.all()
        if 'state_id' in query:
            results=results.filter(state_id=query['state_id'][0])
        if 'state_api_version' in query:
            results=results.filter(state_api_version=query['state_api_version'][0])
        if 'state_os_version' in query:
            results=results.filter(state_os_version__startswith=query['state_os_version'][0])
        if 'state_device_id' in query:
            results=results.filter(state_device_id=query['state_device_id'][0])
        #results = Test.objects.filter(reduce(and_, q))
        serialize = DeviceStateSerializer(results, many=True)
        return Response(serialize.data, HTTP_200_OK)

    @method_decorator(staff_member_required)
    def post(self, request):
        data = request.data
        if isinstance(data,list):
            for item in data:
                try:
                    instance = DeviceStateSerializer(data=item, many=False, partial=True)
                    if instance.is_valid(raise_exception=True):
                        instance.save()
                except Exception as e:
                    continue
            return Response(data, HTTP_200_OK)
        else:
            instance = DeviceStateSerializer(data=data, many=False, partial=True)
            try:
                if instance.is_valid(raise_exception=True):
                    instance.save()
            except IntegrityError as ex:
                # repeated entry, retrive original
                last_dev = DeviceState.objects.filter(state_device_id=Device.objects.get(device_serial_number=instance.data['state_device_id']),state_kernel_version=instance.data['state_kernel_version'] )[0]
                serialize = DeviceStateSerializer(last_dev, many=False)
                return Response(serialize.data, HTTP_200_OK)
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                return Response("", HTTP_400_BAD_REQUEST)
            return Response(instance.data, HTTP_200_OK)
        return Response(instance.data, HTTP_200_OK)