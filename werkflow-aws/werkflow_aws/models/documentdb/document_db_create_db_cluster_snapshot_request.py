from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCreateDBClusterSnapshotRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
    DBClusterIdentifier: StrictStr
    Tags: list[DocumentDBTag] | None = None
