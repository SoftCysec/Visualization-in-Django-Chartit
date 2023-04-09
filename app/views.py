import pandas as pd
from django.shortcuts import render
from chartit import DataPool, Chart
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def dashboard(request):
    return render(request, 'dashboard.html')


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        df = pd.read_csv(file)
        columns = list(df.columns)
        context = {
            'columns': columns
        }
        return render(request, 'dashboard.html', context=context)
    else:
        return render(request, 'dashboard.html')


@csrf_exempt
def generate_charts(request):
    if request.method == 'POST':
        file = request.FILES['csv_file']
        df = pd.read_csv(file)

        chart_type = request.POST.get('chart_type')
        x_axis = request.POST.get('x_axis')
        y_axis = request.POST.get('y_axis')
        chart_title = request.POST.get('chart_title')

        if chart_type == 'line':
            ds = DataPool(
                series=[{
                    'options': {
                        'source': df
                    },
                    'terms': [
                        x_axis,
                        y_axis
                    ]
                }]
            )

            line_chart = Chart(
                datasource=ds,
                series_options=[{
                    'options': {
                        'type': 'line',
                        'stacking': False
                    },
                    'terms': {
                        x_axis: [y_axis]
                    }
                }],
                chart_options={
                    'title': {
                        'text': chart_title
                    },
                    'xAxis': {
                        'title': {
                            'text': x_axis
                        }
                    },
                    'yAxis': {
                        'title': {
                            'text': y_axis
                        }
                    }
                }
            )

            bar_chart = None

        elif chart_type == 'bar':
            ds = DataPool(
                series=[{
                    'options': {
                        'source': df
                    },
                    'terms': [
                        x_axis,
                        y_axis
                    ]
                }]
            )

            bar_chart = Chart(
                datasource=ds,
                series_options=[{
                    'options': {
                        'type': 'column',
                        'stacking': False
                    },
                    'terms': {
                        x_axis: [y_axis]
                    }
                }],
                chart_options={
                    'title': {
                        'text': chart_title
                    },
                    'xAxis': {
                        'title': {
                            'text': x_axis
                        }
                    },
                    'yAxis': {
                        'title': {
                            'text': y_axis
                        }
                    }
                }
            )

            line_chart = None

        else:
            line_chart = None
            bar_chart = None

        context = {'line_chart': line_chart, 'bar_chart': bar_chart}
        return render(request, 'dashboard.html', context)

    else:
        return render(request, 'dashboard.html')
