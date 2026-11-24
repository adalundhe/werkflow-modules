from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_dbdb_cluster import DocumentDBDBCluster


class DocumentDBDeleteDBClusterResponse(BaseModel):
    DBCluster: DocumentDBDBCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
