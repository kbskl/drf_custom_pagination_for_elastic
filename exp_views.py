import abc
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.views import APIView
from app_exp.documents import CategoryDocument
from app_exp.serializers import CategorySerializer
from app_exp.util.paginator import DSLPageNumberPagination  # Import pagination


class PaginatedElasticSearchAPIView(APIView, DSLPageNumberPagination):  # Add to here
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            results = self.paginate_queryset(search, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    def generate_q_expression(self, query):
        return Q(
            'multi_match', query=query,
            fields=[
                'name',
                'description',
            ], fuzziness='auto')
