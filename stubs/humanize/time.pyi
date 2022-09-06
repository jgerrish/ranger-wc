import datetime as dt
import typing
from typing import Union
from enum import Enum

class Unit(Enum):
    MICROSECONDS: int
    MILLISECONDS: int
    SECONDS: int
    MINUTES: int
    HOURS: int
    DAYS: int
    MONTHS: int
    YEARS: int
    def __lt__(self, other: typing.Any) -> typing.Any: ...
    def __ge__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...

def naturaldelta(
    value: Union[dt.timedelta, float],
    months: bool = ...,
    minimum_unit: str = ...,
) -> str: ...
def naturaltime(
    value: Union[dt.datetime, dt.timedelta, float],
    future: bool = ...,
    months: bool = ...,
    minimum_unit: str = ...,
    when: Union[dt.datetime, None] = ...,
) -> str: ...
def naturalday(
    value: Union[dt.date, dt.datetime],
    format: str = ...,
) -> str: ...
def naturaldate(value: Union[dt.date, dt.datetime]) -> str: ...
def precisedelta(
    value: Union[dt.timedelta, int],
    minimum_unit: str = ...,
    suppress: typing.Iterable[str] = ...,
    format: str = ...,
) -> str: ...
