#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GRN31'

# from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
