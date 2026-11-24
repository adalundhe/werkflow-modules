from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteFleetAdvisorCollectorRequest(BaseModel):
    CollectorReferencedId: StrictStr
