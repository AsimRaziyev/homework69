from django.urls import path

from api_v1.views import add_a_b, subtract_a_b, multiply_a_b, divide_a_b, get_token_view, index

app_name = "api_v1"

urlpatterns = [
    path("index", index, name="index"),
    path('add', add_a_b, name="add"),
    path('subtract', subtract_a_b, name="subtract"),
    path('multiply', multiply_a_b, name="multiply"),
    path('divide', divide_a_b, name="divide"),
    path("get_token", get_token_view)

]
