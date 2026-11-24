from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSDeleteAccessEntryRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
