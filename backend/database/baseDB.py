import os
from config import DATABASE_PATH

class BaseDatabase:
    db_path = DATABASE_PATH
    def __init__(self) -> None:
        pass