from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetFormTypeRequest(BaseModel):
    Identifier: StrictStr
