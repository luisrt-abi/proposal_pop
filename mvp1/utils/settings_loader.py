import importlib
from pathlib import PurePath

import yaml
from common.countries import countries


class SettingsLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_yaml(self, file_name: str) -> list:
        file_path = PurePath(self.file_path, file_name)
        with open(file_path, "r") as stream:
            config = yaml.safe_load(stream)
        return config

    def parse_settings(self, pipeline_settings: dict):
        pipeline_name = pipeline_settings["name"]
        pipeline_settings = pipeline_settings["settings"]
        return pipeline_name, pipeline_settings

    def get_pipeline_registry(self, pipeline_name: str):
        imported_module = importlib.import_module(f"{pipeline_name}.pipeline")
        registry = getattr(imported_module, "pipeline_registry")
        return registry

    def get_pipeline_settings(self, pipeline_name: str):
        imported_module = importlib.import_module(f"{pipeline_name}.settings")
        pipeline_settings = getattr(imported_module, f"{pipeline_name}_settings")
        return pipeline_settings

    def get_pipeline(self, pipeline_name: str, country: countries):
        registry = self.get_pipeline_registry(pipeline_name=pipeline_name)
        pipeline = registry.get(country, registry["default"])
        return pipeline

    def valid_settings(self, pipeline_name: str, pipeline_settings: dict):
        settings = self.get_pipeline_settings(pipeline_name=pipeline_name)
        return settings.validate(pipeline_settings)

    def load_pipeline(self, conf: str):
        pipeline_name, pipeline_settings = self.parse_settings(pipeline_settings=conf)
        settings_pydantic = self.get_pipeline_settings(pipeline_name=pipeline_name)
        valid_settings = settings_pydantic(**pipeline_settings)
        pipeline = self.get_pipeline(
            pipeline_name=pipeline_name, country=valid_settings.country
        )
        int_pipeline = pipeline(settings=valid_settings)
        return int_pipeline

    def load(self, config_name: str):
        conf = self.read_yaml(file_name=config_name)
        pipelines = [self.load_pipeline(c) for c in conf]
        return pipelines

    def run(self, pipelines: list):
        for pipeline in pipelines:
            pipeline.run()
        return pipelines
