from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_dbdb_cluster import DocumentDBDBCluster


class DocumentDBDescribeDBClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusters: list[DocumentDBDBCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
