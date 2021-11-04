import json
from datetime import datetime

import pandas
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter
from cdhometask.filters import CandidateFilter
from cdhometask.models import Candidate
from cdhometask.serializers import CandidateSerializer, CandidateListSerializer, CandidateIngestSerializer


class CandidateViewSet(DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Candidate.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CandidateFilter
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'list':
            return CandidateListSerializer
        return CandidateSerializer

    @action(detail=False, methods=['post'])
    def ingest(self, request):
        serializer = CandidateIngestSerializer(data=request.data, many=True)
        for item in serializer.initial_data:
            item['date_of_birth'] = datetime.strptime(item['date_of_birth'], '%d/%m/%Y').date()

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.validated_data)

    @action(detail=False)
    def average(self, request):
        group = request.GET.get('group')
        average = request.GET.get('average')
        serializer = self.get_serializer(self.queryset, many=True)
        dataframe = pandas.DataFrame(serializer.data)
        average = dataframe.groupby(group)[average].mean()
        return Response(json.loads(average.to_json()))
