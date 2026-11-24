from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeWebAppRequest(BaseModel):
    WebAppId: StrictStr
