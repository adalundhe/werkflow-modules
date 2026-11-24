from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AvailableWorkflowTriggerTypes(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
