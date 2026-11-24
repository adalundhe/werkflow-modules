from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsResultAttribute(BaseModel):
    TypeName: StrictStr
