""" Models package initialization"""
from .base_model import BaseModel
from .engine.file_storage import  FileStorage

storage = FileStorage()
storage.reload()

__all__ = [BaseModel, storage]
