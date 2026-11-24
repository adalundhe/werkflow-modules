from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SupportCompletedUpload(BaseModel):
    partIndex: StrictInt
    eTag: StrictStr
