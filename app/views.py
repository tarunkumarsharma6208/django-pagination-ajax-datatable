from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MyModel
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.http import require_POST


# class MyModelListView(BaseDatatableView):
#     model = MyModel
#     columns = ['id', 'name', 'price']

#     def render_column(self, row, column):
#         # Customize how each column is rendered if needed
#         if column == 'name':
#             return row.name
#         elif column == 'price':
#             return row.price
#         return super().render_column(row, column)
    
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

# def my_model_list(request):
#     queryset = MyModel.objects.all()
#     paginator = Paginator(queryset, 10)  # Show 10 items per page

#     page_number = request.POST.get('start')  # DataTables sends the starting index of the page
#     page_obj = paginator.get_page(page_number // 10 + 1)  # Calculate the page number based on the starting index

#     data = []
#     for obj in page_obj:
#         data.append({
#             'id': obj.id,
#             'name': obj.name,
#             'price': obj.price
#         })

#     return JsonResponse({'draw': int(request.POST.get('draw', 0)), 'recordsTotal': queryset.count(), 'recordsFiltered': queryset.count(), 'data': data})


# def display_latestnews(request):
#     newsdata = MyModel.objects.all()
#     # articles per page
#     per_page = 4
#     # Paginator in a view function to paginate a queryset
#     # show 4 news per page
#     obj_paginator = Paginator(newsdata, per_page)

#     context = {
#         'obj_paginator': obj_paginator,
#     }

#     if request.method == 'POST':
#         # getting page number
#         page_no = request.POST.get('page_no', None)
#         try:
#             requested_page = obj_paginator.page(page_no)
#         except (PageNotAnInteger, EmptyPage):
#             requested_page = obj_paginator.page(1)

#         results = list(requested_page.object_list.values('id', 'name', 'price'))
#         return JsonResponse({"results": results})

#     first_page = obj_paginator.page(1)
#     page_range = obj_paginator.page_range

#     context['first_page'] = first_page
#     context['page_range'] = page_range

#     return render(request, 'index.html.j2', context)


