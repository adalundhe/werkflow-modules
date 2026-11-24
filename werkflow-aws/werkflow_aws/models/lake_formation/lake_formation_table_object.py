from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationTableObject(BaseModel):
    Uri: StrictStr | None = None
    ETag: StrictStr | None = None
    Size: StrictInt | None = None
