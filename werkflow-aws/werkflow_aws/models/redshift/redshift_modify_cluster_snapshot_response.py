from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_snapshot import RedshiftSnapshot


class RedshiftModifyClusterSnapshotResponse(BaseModel):
    Snapshot: RedshiftSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
