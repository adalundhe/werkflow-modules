from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetBlueprintRunRequest(BaseModel):
    BlueprintName: StrictStr
    RunId: StrictStr
