import importlib
import os


def validate_config(config_file_location):
    '''Confirms that the config file exists and is properly filled in

    If the file exists and is valid, returns a dictionary containing desired
    project parameters. If not, an error is thrown.
    '''
    if os.path.isfile(config_file_location):
        spec = importlib.util.spec_from_file_location(
            "stonehenge.project_config_from_file",
            config_file_location,
        )
        stonehenge_config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(stonehenge_config)
        CONFIG = stonehenge_config.PROJECT_CONFIGURATION
    else:
        raise Exception("Config file not found at {0}".format(config_file_location))

    return CONFIG
