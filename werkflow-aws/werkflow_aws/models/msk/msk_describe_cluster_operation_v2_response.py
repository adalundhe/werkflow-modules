from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .msk_cluster_operation_v2 import MSKClusterOperationV2


class MSKDescribeClusterOperationV2Response(BaseModel):
    ClusterOperationInfo: MSKClusterOperationV2 | None = None
    ResponseMetadata: dict[str, Any] | None = None
