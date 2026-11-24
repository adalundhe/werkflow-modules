from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateEmailAddressMetadataRequest(BaseModel):
    InstanceId: StrictStr
    EmailAddressId: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    ClientToken: StrictStr | None = None
