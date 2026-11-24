from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUserPoolReplicaType(BaseModel):
    RegionName: StrictStr | None = None
    Status: StrictStr | None = None
    Role: StrictStr | None = None
    UserPoolArn: StrictStr | None = None
