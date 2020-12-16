from configparser import ConfigParser

__parser = ConfigParser()
__parser.read('properties.ini')


def get_property(domain, key_value):
    return __parser.get(domain, key_value)
