from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDeleteSubscriberRequest(BaseModel):
    subscriberId: StrictStr
