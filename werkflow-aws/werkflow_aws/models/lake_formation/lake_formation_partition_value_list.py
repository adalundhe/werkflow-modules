from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationPartitionValueList(BaseModel):
    Values: list[StrictStr]
