from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_entity_display_data import KendraEntityDisplayData


class KendraExperienceEntitiesSummary(BaseModel):
    EntityId: StrictStr | None = None
    EntityType: StrictStr | None = None
    DisplayData: KendraEntityDisplayData | None = None
