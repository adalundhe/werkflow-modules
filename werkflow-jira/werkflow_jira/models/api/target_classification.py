from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TargetClassification(BaseModel):
    classifications: dict[StrictStr, list[StrictStr]] | None = None
    issueType: StrictStr | None = None
    projectKeyOrId: StrictStr | None = None
