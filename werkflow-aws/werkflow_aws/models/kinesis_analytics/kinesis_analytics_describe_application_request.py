from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KinesisAnalyticsDescribeApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    IncludeAdditionalDetails: StrictBool | None = None
