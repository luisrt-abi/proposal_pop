from datetime import date

from common.countries import countries
from pipeline1.settings import pipeline1_settings as settings


class pipeline1:
    def __init__(self, settings: settings) -> None:
        self.date = date.today()
        self.settings = settings
        self.country

    @property
    def country(self):
        return self.settings.country

    def __repr__(self) -> str:
        return f"pipeline1 using date={self.date})"

    def greet(self):
        print(f"Hello from {self.country} pipeline1")

    def run(self):
        self.greet()
        result = self.settings.add2 + self.settings.add3
        return result == 5


class mx_pipeline1(pipeline1):
    def __init__(self, settings: settings) -> None:
        super().__init__(settings=settings)

    def run(self):
        print("Im running mx pipeline1...")


pipeline_registry = dict()
pipeline_registry["default"] = pipeline1
pipeline_registry[countries.MX] = mx_pipeline1
