from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetExportSnapshotRecordsRequest(BaseModel):
    pageToken: StrictStr | None = None
