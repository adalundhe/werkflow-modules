from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_snapshot import FSxSnapshot


class FSxUpdateSnapshotResponse(BaseModel):
    Snapshot: FSxSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
