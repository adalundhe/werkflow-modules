from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .priority_mapping import PriorityMapping


class CreatePrioritySchemeDetails(BaseModel):
    defaultPriorityId: StrictInt | None = None
    description: StrictStr | None = None
    mappings: PriorityMapping | None = None
    name: StrictStr | None = None
    priorityIds: list[StrictInt] | None = None
    projectIds: list[StrictInt] | None = None
