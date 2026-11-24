from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDmsReplicationInstanceReplicationSubnetGroupDetails(BaseModel):
    ReplicationSubnetGroupIdentifier: StrictStr | None = None
