from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailAddOn(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    snapshotTimeOfDay: StrictStr | None = None
    nextSnapshotTimeOfDay: StrictStr | None = None
    threshold: StrictStr | None = None
    duration: StrictStr | None = None
