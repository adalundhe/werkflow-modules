from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteGlossaryRequest(BaseModel):
    Identifier: StrictStr
