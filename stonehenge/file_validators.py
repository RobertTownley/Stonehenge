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

    # Validate general settings
    required_fields = ['PROJECT_NAME']
    for field in required_fields:
        if not CONFIG[field]:
            raise Exception("Required field {0} not specified".format(field))

    # Validate local database
    db = CONFIG['DATABASE']['local']
    for key in db.keys():
        if not db[key]:
            raise Exception("Required database field {0} not specified".format(key))

    return CONFIG
