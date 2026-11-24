from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictBool
from .icon import Icon


class Status(BaseModel):
    model_config = ConfigDict(extra="allow")

    icon: Icon | None = None
    resolved: StrictBool | None = None
