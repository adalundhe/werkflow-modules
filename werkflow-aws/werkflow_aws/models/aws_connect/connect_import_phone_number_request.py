from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectImportPhoneNumberRequest(BaseModel):
    InstanceId: StrictStr
    SourcePhoneNumberArn: StrictStr
    PhoneNumberDescription: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
