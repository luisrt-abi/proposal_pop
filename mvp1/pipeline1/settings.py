from common.countries import countries
from pydantic import BaseModel


class pipeline1_settings(BaseModel):
    country: countries
    add2: int = 2
    add3: int = 3
