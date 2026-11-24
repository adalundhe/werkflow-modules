from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBlueprintDetails(BaseModel):
    BlueprintName: StrictStr | None = None
    RunId: StrictStr | None = None
