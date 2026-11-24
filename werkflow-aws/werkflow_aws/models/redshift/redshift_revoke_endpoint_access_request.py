from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RedshiftRevokeEndpointAccessRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    Account: StrictStr | None = None
    VpcIds: list[StrictStr] | None = None
    Force: StrictBool | None = None
