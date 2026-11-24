from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetBlueprintRequest(BaseModel):
    Name: StrictStr
    IncludeBlueprint: StrictBool | None = None
    IncludeParameterSpec: StrictBool | None = None
