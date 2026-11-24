from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetInstanceSnapshotsRequest(BaseModel):
    pageToken: StrictStr | None = None
