from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

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
