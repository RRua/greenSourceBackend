from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from urllib.parse import parse_qs
from rest_framework.views import APIView
from repoApp.models.metricsRelated import Metric
from repoApp.serializers.metricRelatedSerializers import MetricSerializer

# Create your views here.
class AllMetricsListView(APIView):
	def get(self, request):
	        query=parse_qs(request.META['QUERY_STRING'])
	        results = Metric.objects.all()
	        if 'metric_name' in query:
	            results=results.filter(metric_name=query['metric_name'][0])
	        if 'metric_category' in query:
	            results=results.filter(metric_category=query['metric_category'][0])
	        if 'metric_type' in query:
	            results=results.filter(metric_type=query['metric_type'][0])
	        serialize = MetricSerializer(results, many=True)
	        return Response(serialize.data, HTTP_200_OK)
