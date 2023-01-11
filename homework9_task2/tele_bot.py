import time
import logging
from aiogram import Bot, Dispatcher, executor, types

with open("info.txt", "r") as f:
    text = f.readline()
token = text

