from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_time_range import KendraTimeRange


class KendraGetSnapshotsResponse(BaseModel):
    SnapShotTimeFilter: KendraTimeRange | None = None
    SnapshotsDataHeader: list[StrictStr] | None = None
    SnapshotsData: list[list[StrictStr]] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
