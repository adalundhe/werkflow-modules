from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftEventInfoMap(BaseModel):
    EventId: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    EventDescription: StrictStr | None = None
    Severity: StrictStr | None = None
