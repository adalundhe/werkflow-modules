from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_snapshot_policy import FSxSnapshotPolicy


class FSxUpdateSnapshotPolicyResponse(BaseModel):
    SnapshotPolicy: FSxSnapshotPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
