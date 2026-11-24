from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_global_cluster import DocumentDBGlobalCluster


class DocumentDBDeleteGlobalClusterResponse(BaseModel):
    GlobalCluster: DocumentDBGlobalCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
