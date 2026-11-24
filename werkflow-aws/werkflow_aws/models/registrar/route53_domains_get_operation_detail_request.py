from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsGetOperationDetailRequest(BaseModel):
    OperationId: StrictStr
