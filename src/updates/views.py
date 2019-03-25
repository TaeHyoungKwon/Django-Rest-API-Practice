import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from config.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize


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


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # 하나의 row object에 대해서, json으로 직렬화 한다.
        data = serialize("json", [obj, ], fields=('user', 'content'))
        json_data = data
        print(data)
        '''
        data = {
            "user": obj.user.username,
            "content": obj.content
        }
        json_data = json.dumps(data)
        '''

        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        print(qs)
        data = serialize("json", qs, fields=('user', 'content'))
        json_data = data
        print(data)
        print("kwontaehyoung")
        '''
        data = {
            "user": obj.user.username,
            "content": obj.content
        }
        json_data = json.dumps(data)
        '''

        return HttpResponse(json_data, content_type='application/json')
