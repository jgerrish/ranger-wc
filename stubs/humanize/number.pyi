from .i18n import thousands_separator as thousands_separator
from _typeshed import Incomplete
from typing import Union

# I don't know why this is needed
TYPE_CHECKING: bool

def ordinal(value: Union[float, str], gender: str = ...) -> str: ...
def intcomma(value: Union[float, str], ndigits: Union[int, None] = ...) -> str: ...

powers: Incomplete
human_powers: Incomplete

def intword(value: Union[float, str], format: str = ...) -> str: ...
def apnumber(value: Union[float, str]) -> str: ...
def fractional(value: Union[float, str]) -> str: ...
def scientific(value: Union[float, str], precision: int = ...) -> str: ...
def clamp(
    value: float,
    format: str = ...,
    floor: Union[float, None] = ...,
    ceil: Union[float, None] = ...,
    floor_token: str = ...,
    ceil_token: str = ...,
) -> str: ...
def metric(value: float, unit: str = ..., precision: int = ...) -> str: ...