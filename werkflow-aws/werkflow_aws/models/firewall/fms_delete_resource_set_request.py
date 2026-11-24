from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSDeleteResourceSetRequest(BaseModel):
    Identifier: StrictStr
