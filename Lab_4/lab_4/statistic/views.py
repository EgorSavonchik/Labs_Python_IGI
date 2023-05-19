from django.shortcuts import render
from order.models import Order
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from store.models import Product
from .forms import StatisticForm
import os
from django.conf import settings
# Create your views here.

def statistic_show(request) :
    form = StatisticForm()
    pt = dict()

    x = []
    y = []

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.'+str(ord.created.month)+'.'+str(ord.created.day)] = 0

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.'+str(ord.created.month)+'.'+str(ord.created.day)] += 1

    for tmp in pt:
        x.append(tmp)
        y.append(pt[tmp])

    plt.plot(x,y, 'ro')

    if(request.method == "GET"):

        plt.savefig(os.path.join(settings.MEDIA_ROOT, 'schedule.jpg'), format='jpg')
        plt.clf()
        return render(request, 'statistic/statistic.html')

def tables_show(request):
    arr = list(Product.objects.all())
    arr.sort(key = lambda x:x.purchase_count, reverse=True)

    return render(request, 'statistic/tables.html', context={'product_table':arr})
