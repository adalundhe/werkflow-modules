from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyIdFormatRequest(BaseModel):
    Resource: StrictStr
    UseLongIds: StrictBool
