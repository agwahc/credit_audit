import os
from kivy.lang import Builder

find = os.path.dirname(__file__)


def file(source):
    return find + '%s' %source