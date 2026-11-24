from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationAddObjectInput(BaseModel):
    Uri: StrictStr
    ETag: StrictStr
    Size: StrictInt
    PartitionValues: list[StrictStr] | None = None
