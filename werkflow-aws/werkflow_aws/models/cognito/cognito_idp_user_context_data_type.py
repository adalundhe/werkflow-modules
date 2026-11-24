from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUserContextDataType(BaseModel):
    IpAddress: StrictStr | None = None
    EncodedData: StrictStr | None = None
