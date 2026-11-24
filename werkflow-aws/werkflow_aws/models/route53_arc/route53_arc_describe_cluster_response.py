from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_arc_cluster import Route53ARCCluster


class Route53ARCDescribeClusterResponse(BaseModel):
    Cluster: Route53ARCCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
