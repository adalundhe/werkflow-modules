from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSPlacementConstraint(BaseModel):
    type: StrictStr | None = None
    expression: StrictStr | None = None
