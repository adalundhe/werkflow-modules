from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_condition import ConnectCondition


class ConnectListCondition(BaseModel):
    TargetListType: Literal['PROFICIENCIES'] | None = None
    Conditions: list[ConnectCondition] | None = None
