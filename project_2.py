import tempfile
import os
import argparse
import json


def function():
    """Working with Python Console."""
    objects_all = argparse.ArgumentParser()         # создан объект;
    objects_all.add_argument('--key', type=str, help = 'Return key\'s dictionary')        # описание переменной, которую планируется запсиать
    objects_all.add_argument('--value',type=str, help = 'Return values\'s dictionary')

    arguments = objects_all.parse_args()            # то, что мы предали(key, value) станет свойствами объекта arg

    if arguments.value is None:
        pass
    elif arguments.key is None:
        print('Error, key can not be None!')

    __key = arguments.key
    __value = arguments.value
    function_0(__key, __value)



def function_0(key, value, name_of_file='storage.data'):
    """The function for recording information in time-file."""

    storage_path = os.path.join(tempfile.gettempdir(), name_of_file)

    with open(storage_path, 'w+') as name_of_file:
        mean = {'keys :': list(),'value :':dict()}
        json.dump(mean, name_of_file)


function()