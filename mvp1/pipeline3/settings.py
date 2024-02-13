from common.countries import countries
from pydantic import BaseModel


class pipeline2_settings(BaseModel):
    country: countries
    add1: int = 1
    add2: int = 2
