from typing import Any, Optional

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class UserSchema(BaseModel):
    """User schema"""
    id: Optional[int] = None
    created: Optional[str] = None
    email: str
    name: str
    surname: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
