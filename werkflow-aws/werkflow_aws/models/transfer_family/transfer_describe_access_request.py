from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeAccessRequest(BaseModel):
    ServerId: StrictStr
    ExternalId: StrictStr
