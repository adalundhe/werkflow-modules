from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_dbdb_cluster_snapshot_attribute import DocumentDBDBClusterSnapshotAttribute


class DocumentDBDBClusterSnapshotAttributesResult(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr | None = None
    DBClusterSnapshotAttributes: list[DocumentDBDBClusterSnapshotAttribute] | None = None
