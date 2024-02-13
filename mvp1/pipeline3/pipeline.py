from datetime import date

from common.countries import countries
from pipeline2.settings import pipeline2_settings as settings
import pipeline3

class pipeline3:
    df = pipeline1().run
    df = pipeline2(df).run


class co_pipeline2(pipeline2):
    def __init__(self, settings: settings) -> None:
        super().__init__(settings=settings)

    def greet(self):
        print("Im running CO pipeline2...")


pipeline_registry = dict()
pipeline_registry["default"] = pipeline2
pipeline_registry[countries.CO] = co_pipeline2
