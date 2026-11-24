from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_cluster_v2 import MSKClusterV2


class MSKListClustersV2Response(BaseModel):
    ClusterInfoList: list[MSKClusterV2] | None = None
    NextToken: StrictStr | None = None
