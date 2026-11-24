from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStartBlueprintRunRequest(BaseModel):
    BlueprintName: StrictStr
    RoleArn: StrictStr
    Parameters: StrictStr | None = None
