from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field as PydanticField


class FieldUpdateOperation(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    add: Any = None
    copy_: Any = PydanticField(default=None, alias='copy')
    edit: Any = None
    remove: Any = None
    set: Any = None
