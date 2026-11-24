from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_operation_info import KinesisAnalyticsApplicationOperationInfo


class KinesisAnalyticsListApplicationOperationsResponse(BaseModel):
    ApplicationOperationInfoList: list[KinesisAnalyticsApplicationOperationInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
