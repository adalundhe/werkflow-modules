from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster import RedshiftCluster


class RedshiftModifyClusterDbRevisionResponse(BaseModel):
    Cluster: RedshiftCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
