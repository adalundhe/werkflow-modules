from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_detail import KinesisAnalyticsApplicationDetail


class KinesisAnalyticsUpdateApplicationResponse(BaseModel):
    ApplicationDetail: KinesisAnalyticsApplicationDetail | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
