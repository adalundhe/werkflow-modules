from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_cluster_snapshot_attributes_result import DocumentDBDBClusterSnapshotAttributesResult


class DocumentDBModifyDBClusterSnapshotAttributeResponse(BaseModel):
    DBClusterSnapshotAttributesResult: DocumentDBDBClusterSnapshotAttributesResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
