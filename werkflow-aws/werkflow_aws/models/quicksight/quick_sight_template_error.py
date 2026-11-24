from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_entity import QuickSightEntity


class QuickSightTemplateError(BaseModel):
    Type: StrictStr | None = None
    Message: StrictStr | None = None
    ViolatedEntities: list[QuickSightEntity] | None = None
