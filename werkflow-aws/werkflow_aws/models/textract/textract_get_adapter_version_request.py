from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractGetAdapterVersionRequest(BaseModel):
    AdapterId: StrictStr
    AdapterVersion: StrictStr
