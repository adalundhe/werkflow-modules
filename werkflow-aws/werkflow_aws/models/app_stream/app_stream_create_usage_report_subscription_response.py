from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AppStreamCreateUsageReportSubscriptionResponse(BaseModel):
    S3BucketName: StrictStr | None = None
    Schedule: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
