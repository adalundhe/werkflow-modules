from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationVirtualObject(BaseModel):
    Uri: StrictStr
    ETag: StrictStr | None = None
