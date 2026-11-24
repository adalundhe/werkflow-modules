from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_hsm_cluster import CloudHSMCluster


class CloudHSMDescribeClustersResponse(BaseModel):
    Clusters: list[CloudHSMCluster] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
