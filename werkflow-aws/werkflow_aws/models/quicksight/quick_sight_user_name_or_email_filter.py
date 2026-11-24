from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUserNameOrEmailFilter(BaseModel):
    prefix: StrictStr
