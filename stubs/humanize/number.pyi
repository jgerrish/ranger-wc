from .i18n import thousands_separator as thousands_separator
from _typeshed import Incomplete
from typing import TypeAlias, Union

# I don't know why this is needed
TYPE_CHECKING: bool

NumberOrString: TypeAlias = Union[float, str]

def ordinal(value: NumberOrString, gender: str = ...) -> str: ...
def intcomma(value: NumberOrString, ndigits: Union[int, None] = ...) -> str: ...

powers: Incomplete
human_powers: Incomplete

def intword(value: NumberOrString, format: str = ...) -> str: ...
def apnumber(value: NumberOrString) -> str: ...
def fractional(value: NumberOrString) -> str: ...
def scientific(value: NumberOrString, precision: int = ...) -> str: ...
def clamp(
    value: float,
    format: str = ...,
    floor: Union[float, None] = ...,
    ceil: Union[float, None] = ...,
    floor_token: str = ...,
    ceil_token: str = ...,
) -> str: ...
def metric(value: float, unit: str = ..., precision: int = ...) -> str: ...
