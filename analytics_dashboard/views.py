# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Sum,Count
from django.shortcuts import render
from django.shortcuts import render_to_response
from . import models
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='anshul.saxena140890', api_key='r4cdHL7wtJCuQgQNRIAu')
# Create your views here.

def display(request):

  objs = models.AdvData.objects.values('advertiser_name','publisher_name').order_by().annotate(Sum('impression'),Sum('click'),Sum('install'),Sum('purchase'))#,Sum('os'),Count('city')),Count('device_brand'))
  # print(objs)
  paginator = Paginator(objs, 10)

  page = request.GET.get('page')
  
  try:
    objs = paginator.page(page)

  except PageNotAnInteger:
    objs = paginator.page(1)

  except EmptyPage:
    objs = paginator.page(paginator.num_pages)

##############################################################################

  obj2 = models.AdvData.objects.values('device_brand').annotate(Sum('install')).order_by('-install__sum')[:10]

  labels = []
  installs = []

  for i in obj2:
    labels.append(i['device_brand'])
    installs.append(i['install__sum'])

  d = dict(zip(labels,installs))

  fig = {"data": [{"values": installs,"labels": labels,"domain": {"x": [0, .48]},"name": "Device & Installs","hoverinfo":"label+percent+name","hole": .4,"type": "pie"}],"layout": {"title":"Device Specific Installs","annotations": [{"font": {"size": 15},"showarrow": False,"text": "INSTALLS","x": 0.20,"y": 0.5}]}}
  
  obj3 = py.plot(fig)

  print(obj2)

  obj4 = obj3+".embed"

  ##############################################################################



  obj = models.AdvData.objects.values('city').annotate(tot_install=Sum('install'),tot_purchase=Sum('purchase')).order_by('-tot_install','-tot_purchase')[:10]

  cities = []
  installs = []
  purchases = []

  for i in obj:
    cities.append(i['city'])
    installs.append(i['tot_install'])
    purchases.append(i['tot_purchase'])


  trace0 = go.Bar(
    x=cities,
    y=installs,
    name='Primary Product',
    marker=dict(
        color='rgb(49,130,189)'
    )  )

  trace1 = go.Bar(
    x=cities,
    y=purchases,
    name='Secondary Product',
    marker=dict(
        color='rgb(204,204,204)',
    ))


  data = [trace0, trace1]
  layout = go.Layout(
    xaxis=dict(tickangle=-45),
    barmode='group',)

  
  fig = go.Figure(data=data, layout=layout)
  r = py.plot(fig)

  r1 = r+".embed"
  # return r  
    
  return render(request,'visualisations.html', {'objs': objs,'obj4':obj4,'r1':r1})
  


