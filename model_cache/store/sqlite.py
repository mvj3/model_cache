# -*- coding: utf-8 -*-

from .base import ModelCacheStore

class ModelCacheStoreSqlite(ModelCacheStore):
    """ BTree查找实现 """

    def __init__(self, name):
        from sqlitedict import SqliteDict
        self.datadict = SqliteDict(name)

    def sync(self): return self.datadict.sync()
    def __getitem__(self, k1): return self.datadict[str(k1)]
