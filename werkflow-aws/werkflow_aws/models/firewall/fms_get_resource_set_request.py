from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSGetResourceSetRequest(BaseModel):
    Identifier: StrictStr
