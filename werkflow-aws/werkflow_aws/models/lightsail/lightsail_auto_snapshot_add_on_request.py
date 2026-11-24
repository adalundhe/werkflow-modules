from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAutoSnapshotAddOnRequest(BaseModel):
    snapshotTimeOfDay: StrictStr | None = None
