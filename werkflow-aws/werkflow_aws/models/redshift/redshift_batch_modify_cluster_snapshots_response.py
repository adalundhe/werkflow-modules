from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_snapshot_error_message import RedshiftSnapshotErrorMessage


class RedshiftBatchModifyClusterSnapshotsResponse(BaseModel):
    Resources: list[StrictStr] | None = None
    Errors: list[RedshiftSnapshotErrorMessage] | None = None
    ResponseMetadata: dict[str, Any] | None = None
