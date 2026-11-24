from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAddPartnerRequest(BaseModel):
    AccountId: StrictStr
    ClusterIdentifier: StrictStr
    DatabaseName: StrictStr
    PartnerName: StrictStr
