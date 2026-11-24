from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteBlueprintRequest(BaseModel):
    Name: StrictStr
