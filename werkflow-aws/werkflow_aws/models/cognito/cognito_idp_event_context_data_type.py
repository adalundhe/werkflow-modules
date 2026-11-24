from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPEventContextDataType(BaseModel):
    IpAddress: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Timezone: StrictStr | None = None
    City: StrictStr | None = None
    Country: StrictStr | None = None
