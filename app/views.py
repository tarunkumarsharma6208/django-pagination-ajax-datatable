from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MyModel
from django.views.decorators.http import require_POST

    
@require_POST
def mymodel_json(request):
    columns = ['id', 'name', 'price']

    # Get the necessary parameters from the POST data
    draw = request.POST.get('draw', 1)
    start = int(request.POST.get('start', 0))
    length = int(request.POST.get('length', 10))
    search_value = request.POST.get('search[value]', '')

    # Perform your data querying and filtering based on the received parameters
    queryset = MyModel.objects.all()
    total_records = queryset.count()

    if search_value:
        queryset = queryset.filter(id__icontains=search_value) | \
                   queryset.filter(name__icontains=search_value) | \
                   queryset.filter(price__icontains=search_value)

    filtered_records = queryset.count()
    queryset = queryset[start:start + length]

    # Prepare the data in the required format for DataTables
    data = []
    for record in queryset:
        data.append({
            'id': record.id,
            'name': record.name,
            'price': record.price
        })

    response = {
        'draw': draw,
        'recordsTotal': total_records,
        'recordsFiltered': filtered_records,
        'data': data,
    }

    return JsonResponse(response)


def mymodel_list(request):
    return render(request, 'index.html.j2')




