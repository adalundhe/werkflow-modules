from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSConnection(BaseModel):
    ReplicationInstanceArn: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    Status: StrictStr | None = None
    LastFailureMessage: StrictStr | None = None
    EndpointIdentifier: StrictStr | None = None
    ReplicationInstanceIdentifier: StrictStr | None = None
