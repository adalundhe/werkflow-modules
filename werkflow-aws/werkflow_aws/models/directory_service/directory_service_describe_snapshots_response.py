from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_snapshot import DirectoryServiceSnapshot


class DirectoryServiceDescribeSnapshotsResponse(BaseModel):
    Snapshots: list[DirectoryServiceSnapshot] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
