from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightJoinKeyProperties(BaseModel):
    UniqueKey: StrictBool | None = None
