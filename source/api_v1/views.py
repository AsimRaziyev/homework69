import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def index(request):
    return render(request, 'index.html', )


def add_a_b(request):  # сложить
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            a = int(body.get("A"))
            b = int(body.get("B"))
            if a == 0 or b == 0:
                err = {
                    "error": "Division by zero!"
                }
                return JsonResponse(err, status=400)
            result = (a + b)
            sum_add = {
                "answer": result
            }
            return JsonResponse(sum_add)
        except:
            err = {
                "error": "Division by zero!"
            }
            return JsonResponse(err, status=400)


def subtract_a_b(request):  # вычесть
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            a = int(body.get("A"))
            b = int(body.get("B"))
            if a == 0 or b == 0:
                err = {
                    "error": "Division by zero!"
                }
                return JsonResponse(err, status=400)
            result = (a - b)
            sum_subtract = {
                "answer": result
            }
            return JsonResponse(sum_subtract)
        except:
            err = {
                "error": "Division by zero!"
            }
            return JsonResponse(err, status=400)


def multiply_a_b(request):  # умножить
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            a = int(body.get("A"))
            b = int(body.get("B"))
            if a == 0 or b == 0:
                err = {
                    "error": "Division by zero!"
                }
                return JsonResponse(err, status=400)
            result = (a * b)
            sum_multiply = {
                "answer": result
            }
            return JsonResponse(sum_multiply)
        except:
            err = {
                "error": "Division by zero!"
            }
            return JsonResponse(err, status=400)


def divide_a_b(request):  # разделить
    if request.method == 'POST':
        body = json.loads(request.body)
        try:
            a = int(body.get("A"))
            b = int(body.get("B"))
            if a == 0 or b == 0:
                err = {
                    "error": "Division by zero!"
                }
                return JsonResponse(err, status=400)
            result = (a // b)
            sum_divide = {
                "answer": result
            }
            return JsonResponse(sum_divide)
        except:
            err = {
                "error": "Division by zero!"
            }
            return JsonResponse(err, status=400)
