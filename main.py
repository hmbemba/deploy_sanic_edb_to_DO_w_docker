
from dataclasses import dataclass, field
from math import fabs
from typing import Any, List
from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv
# import os

load_dotenv()

from db.Models.MyModel import TodosModel

TodosModel.insertEntry(printStr=False,
                     _task = "task one from laptop",
                     _completed = False)

# # client_id = os.environ['SPOTIPY_CLIENT_ID']

# @dataclass
# class xx(metaclass=ABCMeta):
#     _: List = field(default_factory=lambda: [])

#     @abstractmethod
# 	def foo(self):
# 		pass

# @dataclass
# class xx:
#     _: List = field(default_factory=lambda: [])
    