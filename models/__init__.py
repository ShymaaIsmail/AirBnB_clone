""" Models package initialization"""
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
