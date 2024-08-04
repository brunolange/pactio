from django.http import JsonResponse
from pydantic import BaseModel

from pactio.decorators import pactio


class MyModel(BaseModel):
    a_str: str
    an_int: int
    a_bool: bool
    a_float: float
    a_list_of_ints: list[int]


@pactio
def my_view(request, my_model: MyModel):
    return JsonResponse(my_model.model_dump())
