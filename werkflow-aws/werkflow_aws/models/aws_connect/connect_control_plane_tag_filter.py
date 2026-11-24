from __future__ import annotations
from pydantic import BaseModel
from .connect_tag_condition import ConnectTagCondition


class ConnectControlPlaneTagFilter(BaseModel):
    OrConditions: list[list[ConnectTagCondition]] | None = None
    AndConditions: list[ConnectTagCondition] | None = None
    TagCondition: ConnectTagCondition | None = None
