from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeletePartnerRequest(BaseModel):
    AccountId: StrictStr
    ClusterIdentifier: StrictStr
    DatabaseName: StrictStr
    PartnerName: StrictStr
