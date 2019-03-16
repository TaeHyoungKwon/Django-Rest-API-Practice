from django.http import JsonResponse


class JsonResponseMixin():
    def render_to_json_response(self, context, **reseponse_kwargs):
        return JsonResponse(self.get_data(context), **reseponse_kwargs)

    def get_data(self, context):
        return context
