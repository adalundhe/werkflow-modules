from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_dbdb_cluster_snapshot import DocumentDBDBClusterSnapshot


class DocumentDBDescribeDBClusterSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterSnapshots: list[DocumentDBDBClusterSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
