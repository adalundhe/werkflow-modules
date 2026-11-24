from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerDescribePartnerAppRequest(BaseModel):
    Arn: StrictStr
    IncludeAvailableUpgrade: StrictBool | None = None
