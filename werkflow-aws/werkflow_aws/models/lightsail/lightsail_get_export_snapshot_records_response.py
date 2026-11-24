from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_export_snapshot_record import LightsailExportSnapshotRecord


class LightsailGetExportSnapshotRecordsResponse(BaseModel):
    exportSnapshotRecords: list[LightsailExportSnapshotRecord] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
