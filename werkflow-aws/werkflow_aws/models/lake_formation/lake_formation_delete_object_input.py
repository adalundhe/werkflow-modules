from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeleteObjectInput(BaseModel):
    Uri: StrictStr
    ETag: StrictStr | None = None
    PartitionValues: list[StrictStr] | None = None
