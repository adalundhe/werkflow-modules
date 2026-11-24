from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_cluster_operation_v2_summary import MSKClusterOperationV2Summary


class MSKListClusterOperationsV2Response(BaseModel):
    ClusterOperationInfoList: list[MSKClusterOperationV2Summary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
