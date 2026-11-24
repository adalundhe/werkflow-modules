from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .msk_cluster_operation_info import MSKClusterOperationInfo


class MSKDescribeClusterOperationResponse(BaseModel):
    ClusterOperationInfo: MSKClusterOperationInfo | None = None
    ResponseMetadata: dict[str, Any] | None = None
