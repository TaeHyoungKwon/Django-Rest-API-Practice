### django에서 제공하는 기본 직렬화 함수 사용한 직렬화



```python
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
     
```





### 모델 매니저를 이용한 직렬화

```python
import json
from django.core.serializers import serialize
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    '''
    upload_update_image_path
    '''
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):

    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            stuct = json.loads(obj.serialize())
            final_array.append(stuct)
        return json.dumps(final_array)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    '''
    Update Model
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        json_data = serialize(
            "json", [self], fields=('user', 'content', 'image'))
        stuct = json.loads(json_data)
        print(stuct)
        data = json.dumps(stuct[0]['fields'])
        return data

```



```python
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        # 하나의 row object에 대해서, json으로 직렬화 한다.
        #data = serialize("json", [obj, ], fields=('user', 'content'))
        json_data = obj.serialize()

        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        print(qs)
        #data = serialize("json", qs, fields=('user', 'content'))
        json_data = qs.serialize()

        return HttpResponse(json_data, content_type='application/json')

```





### 