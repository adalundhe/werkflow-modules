from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeWebAppCustomizationRequest(BaseModel):
    WebAppId: StrictStr
