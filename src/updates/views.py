import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update


def update_model_detail_view(request):
    '''
    JsonResponse를 통해서, 사진 타입의 data 변수를 Json 객체로 변환하여
    응답 값을 줄 수 있다.
    '''

    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)


def json_example_view(request):
    data = {
        "count": 1000,
        "content": "some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
