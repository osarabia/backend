# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from spa_gastos.gastos.models import Gastos
from spa_gastos.gastos.serializers import GastosSerializer
from spa_gastos.gastos.utils import convertToDate, convertToDecimal


class GastosViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage gastos resource
    """

    serializer_class = GastosSerializer

    #filter queryset by user
    def get_queryset(self):
        queryset = Gastos.objects.filter(user_id=self.request.user.pk)

        dt, ok = convertToDate(self.request.query_params.get('fecha', None))
        if ok:
            return queryset.filter(fecha__gte=dt)

        c = self.request.query_params.get('concepto', None)
        if c is not None:
            return queryset.filter(concepto__startswith=c)

        dc, ok = convertToDecimal(self.request.query_params.get('cantidad', None))
        if ok:
            return queryset.filter(cantidad__gte=dc)

        return queryset


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
