from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render

from django.shortcuts import render

def custom_error_view(request, exception=None, status_code=404):
    error_messages = {
        400: "Bad Request",
        403: "Permission Denied",
        404: "Page Not Found",
        500: "Internal Server Error",
    }
    return render(request, 'error.html', {
        'status_code': status_code,
        'error_message': error_messages.get(status_code, "Unknown Error"),
    }, status=status_code)

def custom_404_view(request, exception):
    return custom_error_view(request, exception, status_code=404)

def custom_500_view(request):
    return custom_error_view(request, status_code=500)

def custom_403_view(request, exception):
    return custom_error_view(request, exception, status_code=403)

def custom_400_view(request, exception):
    return custom_error_view(request, exception, status_code=400)


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("success"))
        return super().get(request, *args, **kwargs)
