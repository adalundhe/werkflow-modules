from __future__ import annotations
from pydantic import BaseModel
from .connect_tag_condition import ConnectTagCondition


class ConnectCommonAttributeAndCondition(BaseModel):
    TagConditions: list[ConnectTagCondition] | None = None
