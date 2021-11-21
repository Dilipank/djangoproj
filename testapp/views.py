from django.shortcuts import render
from django.views.generic.base import TemplateView
from testapp.models import Collector
import plotly.offline as opy
import plotly.graph_objs as go


class AllDataView(TemplateView):

    template_name = 'all_data.html'

    def get_all_data(self, **kwargs):
        context = super(AllDataView, self).get_context_data(**kwargs)
        data = list(Collector.objects.values_list('company', flat=True))
        price = list(Collector.objects.values_list('price', flat=True))
        bar1 = go.Bar(x=data, y=price)

        data = go.Figure(data=[bar1])
        layout = go.Layout(title="All Data", xaxis={'title': 'data'}, yaxis={'title': 'price'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div
        return context


def homepage_view(request):
    return render(request, 'homepage.html', {})


def all_data(request):
    data = AllDataView().get_all_data()
    return render(request, 'all_data.html', data)




