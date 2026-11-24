from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BatchEksPersistentVolumeClaim(BaseModel):
    claimName: StrictStr | None = None
    readOnly: StrictBool | None = None
