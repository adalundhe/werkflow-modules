from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConnectFilterV2StringCondition(BaseModel):
    Comparison: Literal['NOT_EXISTS'] | None = None
