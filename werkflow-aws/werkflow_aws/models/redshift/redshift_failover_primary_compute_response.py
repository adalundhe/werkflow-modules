from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_cluster import RedshiftCluster


class RedshiftFailoverPrimaryComputeResponse(BaseModel):
    Cluster: RedshiftCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
