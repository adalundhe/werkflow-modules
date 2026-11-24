from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteGlossaryTermRequest(BaseModel):
    Identifier: StrictStr
