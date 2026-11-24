from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_query_statistics_for_describe_query import CloudTrailQueryStatisticsForDescribeQuery


class CloudTrailDescribeQueryResponse(BaseModel):
    QueryId: StrictStr | None = None
    QueryString: StrictStr | None = None
    QueryStatus: StrictStr | None = None
    QueryStatistics: CloudTrailQueryStatisticsForDescribeQuery | None = None
    ErrorMessage: StrictStr | None = None
    DeliveryS3Uri: StrictStr | None = None
    DeliveryStatus: StrictStr | None = None
    Prompt: StrictStr | None = None
    EventDataStoreOwnerAccountId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
