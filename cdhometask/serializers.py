import copy
from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from cdhometask.models import Candidate


class CandidateListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    class Meta:
        model = Candidate
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')


class CandidateSerializer(CandidateListSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        if not obj.date_of_birth:
            return 0
        return relativedelta(datetime.now().date(), obj.date_of_birth).years

    class Meta(CandidateListSerializer.Meta):
        model = Candidate
        fields = CandidateListSerializer.Meta.fields + ('age', 'industry', 'salary', 'experience')


class CandidateIngestSerializer(CandidateSerializer):
    date_of_birth = serializers.DateField()
    years_of_experience = serializers.IntegerField(source='experience', allow_null=True)

    class Meta(CandidateListSerializer.Meta):
        model = Candidate
        fields = '__all__'
