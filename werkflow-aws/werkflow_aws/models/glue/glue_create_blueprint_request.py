from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateBlueprintRequest(BaseModel):
    Name: StrictStr
    BlueprintLocation: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
