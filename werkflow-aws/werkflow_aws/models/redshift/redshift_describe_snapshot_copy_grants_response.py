from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_snapshot_copy_grant import RedshiftSnapshotCopyGrant


class RedshiftDescribeSnapshotCopyGrantsResponse(BaseModel):
    Marker: StrictStr | None = None
    SnapshotCopyGrants: list[RedshiftSnapshotCopyGrant] | None = None
    ResponseMetadata: dict[str, Any] | None = None
