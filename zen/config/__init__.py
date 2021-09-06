#!/usr/bin/env python
import configparser as _configparser
from os import path as _path

config_dir = _path.dirname(__file__)

Config = _configparser.ConfigParser()
Config.read(_path.join(config_dir, 'config.ini'))
