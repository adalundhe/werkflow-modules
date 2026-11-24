from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_cluster_node import RedshiftClusterNode


class RedshiftSecondaryClusterInfo(BaseModel):
    AvailabilityZone: StrictStr | None = None
    ClusterNodes: list[RedshiftClusterNode] | None = None
