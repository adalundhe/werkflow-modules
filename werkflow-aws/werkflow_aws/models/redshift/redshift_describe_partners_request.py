from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDescribePartnersRequest(BaseModel):
    AccountId: StrictStr
    ClusterIdentifier: StrictStr
    DatabaseName: StrictStr | None = None
    PartnerName: StrictStr | None = None
