from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateEmailAddressRequest(BaseModel):
    InstanceId: StrictStr
    EmailAddress: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
