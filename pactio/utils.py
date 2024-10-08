import inspect
from dataclasses import dataclass
from typing import Optional, Type, get_args

from pydantic import BaseModel

__author__ = "Bruno Lange"
__email__ = "blangeram@gmail.com"
__license__ = "MIT"


@dataclass
class MaybeModel:
    cls: Type[BaseModel]
    optional: bool


def get_maybe_model(parameter: inspect.Parameter) -> Optional[MaybeModel]:
    cls = parameter.annotation
    if issubclass(cls, BaseModel):
        try:
            return MaybeModel(cls=cls, optional=False)
        except TypeError:
            pass

    # search for Optional[BaseModel]
    try:
        left, right = get_args(cls)
    except ValueError:
        return None

    NoneType = type(None)
    if issubclass(left, BaseModel) and right is NoneType:
        return MaybeModel(cls=left, optional=True)

    return None
