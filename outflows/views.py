from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms, serializers
from rest_framework import generics
from core.metrics import get_sales_metrics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflows
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = get_sales_metrics()

        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflows
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflows'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outflows
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflows'


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflows.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Outflows.objects.all()
    serializer_class = serializers.OutflowSerializer
