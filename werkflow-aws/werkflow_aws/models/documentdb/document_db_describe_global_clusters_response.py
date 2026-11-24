from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_global_cluster import DocumentDBGlobalCluster


class DocumentDBDescribeGlobalClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    GlobalClusters: list[DocumentDBGlobalCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
