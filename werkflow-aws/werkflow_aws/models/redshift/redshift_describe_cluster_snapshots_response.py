from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_snapshot import RedshiftSnapshot


class RedshiftDescribeClusterSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    Snapshots: list[RedshiftSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
