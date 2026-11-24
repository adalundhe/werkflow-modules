from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KendraPersonasSummary(BaseModel):
    EntityId: StrictStr | None = None
    Persona: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
