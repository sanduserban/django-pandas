from django_filters import FilterSet
from django_filters.rest_framework import CharFilter

from cdhometask.models import Candidate


class CandidateFilter(FilterSet):
    first_name = CharFilter(field_name="first_name", lookup_expr="icontains")
    last_name = CharFilter(field_name="last_name", lookup_expr="icontains")
    industry = CharFilter(field_name="industry", lookup_expr="icontains")

    class Meta:
        model = Candidate
        fields = (
            "first_name",
            "last_name",
            "industry",
        )
