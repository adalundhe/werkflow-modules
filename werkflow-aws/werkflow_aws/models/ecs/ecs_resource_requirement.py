from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_sharing_strategy import ECSSharingStrategy


class ECSResourceRequirement(BaseModel):
    value: StrictStr | None = None
    type: StrictStr | None = None
    sharingStrategy: ECSSharingStrategy | None = None
