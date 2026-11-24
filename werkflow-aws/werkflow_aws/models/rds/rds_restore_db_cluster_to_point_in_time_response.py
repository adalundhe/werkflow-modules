from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_cluster_model import RDSDBClusterModel


class RDSRestoreDBClusterToPointInTimeResponse(BaseModel):
    DBCluster: RDSDBClusterModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
