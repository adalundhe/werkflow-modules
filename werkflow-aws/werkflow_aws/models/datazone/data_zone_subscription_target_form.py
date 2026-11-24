from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscriptionTargetForm(BaseModel):
    formName: StrictStr | None = None
    content: StrictStr | None = None
