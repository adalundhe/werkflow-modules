from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDiskSnapshotsRequest(BaseModel):
    pageToken: StrictStr | None = None
