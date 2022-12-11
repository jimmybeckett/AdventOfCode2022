import os

import git
import requests
from secrets import session_cookie
import pathlib


base_path = f'{git.Repo(".", search_parent_directories=True).working_tree_dir}/temp'


def input_path(year, day):
    return f'{base_path}/data/{year}/{day}.dat'


def scratch_path():
    return f"{base_path}/scratch.txt"


def input_url(year, day):
    return f'https://adventofcode.com/{year}/day/{day}/input'


def get_input(year, day):
    path = input_path(year, day)
    if not os.path.exists(path):
        data = requests.get(input_url(year, day), cookies={'session': session_cookie})
        pathlib.Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        with open(path, 'w+') as f:
            f.write(data.text)
    return open(path)


def get_scratch_input():
    return open(scratch_path(), "r")
