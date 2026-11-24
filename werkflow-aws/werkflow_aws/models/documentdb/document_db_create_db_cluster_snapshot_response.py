from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_cluster_snapshot import DocumentDBDBClusterSnapshot


class DocumentDBCreateDBClusterSnapshotResponse(BaseModel):
    DBClusterSnapshot: DocumentDBDBClusterSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
