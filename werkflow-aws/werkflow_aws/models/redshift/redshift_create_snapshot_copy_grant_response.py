from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_snapshot_copy_grant import RedshiftSnapshotCopyGrant


class RedshiftCreateSnapshotCopyGrantResponse(BaseModel):
    SnapshotCopyGrant: RedshiftSnapshotCopyGrant | None = None
    ResponseMetadata: dict[str, Any] | None = None
