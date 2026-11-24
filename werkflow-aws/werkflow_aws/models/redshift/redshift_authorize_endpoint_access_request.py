from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAuthorizeEndpointAccessRequest(BaseModel):
    Account: StrictStr
    ClusterIdentifier: StrictStr | None = None
    VpcIds: list[StrictStr] | None = None
