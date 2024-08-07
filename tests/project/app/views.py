from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pydantic import BaseModel

from pactio.decorators import pactio


class EchoModel(BaseModel):
    a_str: str
    an_int: int
    a_bool: bool
    a_float: float
    a_list_of_ints: list[int]


@csrf_exempt
def echo(request, echo_model: EchoModel):
    return JsonResponse(echo_model.model_dump())


@csrf_exempt
@pactio
def decorated_echo(request, echo_model: EchoModel):
    return JsonResponse(echo_model.model_dump())
