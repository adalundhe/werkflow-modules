from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgePlacementConstraint(BaseModel):
    type: StrictStr | None = None
    expression: StrictStr | None = None
