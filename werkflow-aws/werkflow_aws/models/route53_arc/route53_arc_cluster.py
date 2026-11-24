from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_arc_cluster_endpoint import Route53ARCClusterEndpoint


class Route53ARCCluster(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterEndpoints: list[Route53ARCClusterEndpoint] | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Owner: StrictStr | None = None
    NetworkType: StrictStr | None = None
