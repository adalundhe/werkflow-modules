from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeOptimizationObjective(BaseModel):
    itemAttribute: StrictStr | None = None
    objectiveSensitivity: StrictStr | None = None
