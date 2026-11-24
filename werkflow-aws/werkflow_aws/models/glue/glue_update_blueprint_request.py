from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateBlueprintRequest(BaseModel):
    Name: StrictStr
    BlueprintLocation: StrictStr
    Description: StrictStr | None = None
