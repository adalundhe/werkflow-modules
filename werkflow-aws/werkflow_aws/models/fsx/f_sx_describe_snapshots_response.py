from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_snapshot import FSxSnapshot


class FSxDescribeSnapshotsResponse(BaseModel):
    Snapshots: list[FSxSnapshot] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
