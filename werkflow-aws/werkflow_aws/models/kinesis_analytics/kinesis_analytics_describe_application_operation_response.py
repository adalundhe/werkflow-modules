from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_application_operation_info_details import KinesisAnalyticsApplicationOperationInfoDetails


class KinesisAnalyticsDescribeApplicationOperationResponse(BaseModel):
    ApplicationOperationInfoDetails: KinesisAnalyticsApplicationOperationInfoDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
