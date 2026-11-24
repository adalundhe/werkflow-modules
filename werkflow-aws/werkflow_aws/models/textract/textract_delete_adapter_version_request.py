from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractDeleteAdapterVersionRequest(BaseModel):
    AdapterId: StrictStr
    AdapterVersion: StrictStr
