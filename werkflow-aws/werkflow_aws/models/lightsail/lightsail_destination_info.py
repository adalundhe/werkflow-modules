from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDestinationInfo(BaseModel):
    id: StrictStr | None = None
    service: StrictStr | None = None
