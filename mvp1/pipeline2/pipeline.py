from datetime import date

from common.countries import countries
from pipeline2.settings import pipeline2_settings as settings


class pipeline2:
    def __init__(self, settings: settings) -> None:
        self.date = date.today()
        self.settings = settings
        self.country

    @property
    def country(self):
        return self.settings.country

    def __repr__(self) -> str:
        return f"pipeline2 using date={self.date})"

    def greet(self):
        print(f"Hello from {self.country} pipeline2")

    def run(self):
        self.greet()
        result = self.settings.add1 + self.settings.add2
        return result == 3


class co_pipeline2(pipeline2):
    def __init__(self, settings: settings) -> None:
        super().__init__(settings=settings)

    def greet(self):
        print("Im running CO pipeline2...")


pipeline_registry = dict()
pipeline_registry["default"] = pipeline2
pipeline_registry[countries.CO] = co_pipeline2
