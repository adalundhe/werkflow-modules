from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDetailsMap(BaseModel):
    ResourceShare: list[StrictStr] | None = None
