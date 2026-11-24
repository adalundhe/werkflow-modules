from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSResourceIdPreference(BaseModel):
    ResourceIdType: StrictStr | None = None
    Resources: list[StrictStr] | None = None
