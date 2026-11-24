from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_cluster_status import EMRClusterStatus


class EMRClusterSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Status: EMRClusterStatus | None = None
    NormalizedInstanceHours: StrictInt | None = None
    ClusterArn: StrictStr | None = None
    OutpostArn: StrictStr | None = None
