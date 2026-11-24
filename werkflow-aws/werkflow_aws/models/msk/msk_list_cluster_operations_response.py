from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_cluster_operation_info import MSKClusterOperationInfo


class MSKListClusterOperationsResponse(BaseModel):
    ClusterOperationInfoList: list[MSKClusterOperationInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
