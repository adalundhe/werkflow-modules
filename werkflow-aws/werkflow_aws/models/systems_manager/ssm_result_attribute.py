from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMResultAttribute(BaseModel):
    TypeName: StrictStr
