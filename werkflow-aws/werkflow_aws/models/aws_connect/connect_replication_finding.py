from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectReplicationFinding(BaseModel):
    Arn: StrictStr | None = None
    Id: StrictStr | None = None
    Region: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Name: StrictStr | None = None
    Operation: StrictStr | None = None
    ReferenceCode: StrictStr | None = None
    Message: StrictStr | None = None
