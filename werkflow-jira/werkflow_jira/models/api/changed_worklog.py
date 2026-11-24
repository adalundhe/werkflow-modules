from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .entity_property import EntityProperty


class ChangedWorklog(BaseModel):
    properties: list[EntityProperty] | None = None
    updatedTime: StrictInt | None = None
    worklogId: StrictInt | None = None
