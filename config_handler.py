import configparser

PROPERTY_FILE = 'configuration_files/properties.ini'


def get_property(section, property):
    config = configparser.ConfigParser()
    config.read(PROPERTY_FILE)
    val = config[section][property]
    return val
