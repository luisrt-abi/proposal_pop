from utils.settings_loader import SettingsLoader

# sets loadiong path and reads settings.yaml
fp = "mvp1/settings/CO"
conf_num = 0
sl = SettingsLoader(file_path=fp)
conf = sl.read_yaml(file_name="settings.yaml")
# gets pipeline name and settings from yaml
pipeline_name, pipeline_settings = sl.parse_settings(pipeline_settings=conf[conf_num])
# get registry dictionary
# this instantiates the pipeline, is it needed?
pipeline_registry = sl.get_pipeline_registry(pipeline_name=pipeline_name)
# gets base_model settings
settings_pydantic = sl.get_pipeline_settings(pipeline_name=pipeline_name)
# validates settings instantiating pydantic
valid_settings = settings_pydantic(**pipeline_settings)
# gets pipeline class
pipeline = sl.get_pipeline(pipeline_name=pipeline_name, country=valid_settings.country)
# instantiates pipeline
int_pipeline = pipeline(settings=valid_settings)
print(int_pipeline)
int_pipeline.run()

# #wish
# sl = SettingsLoader(file_path=fp)
# conf = sl.load_setting(file_name="settings.yaml")
# conf.run()