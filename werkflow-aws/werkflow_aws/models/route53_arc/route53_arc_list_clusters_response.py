from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_arc_cluster import Route53ARCCluster


class Route53ARCListClustersResponse(BaseModel):
    Clusters: list[Route53ARCCluster] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
