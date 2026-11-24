from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftUpdatePartnerStatusRequest(BaseModel):
    AccountId: StrictStr
    ClusterIdentifier: StrictStr
    DatabaseName: StrictStr
    PartnerName: StrictStr
    Status: Literal['Active', 'Inactive', 'RuntimeFailure', 'ConnectionFailure']
    StatusMessage: StrictStr | None = None
