from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsDescribeApplicationOperationRequest(BaseModel):
    ApplicationName: StrictStr
    OperationId: StrictStr
