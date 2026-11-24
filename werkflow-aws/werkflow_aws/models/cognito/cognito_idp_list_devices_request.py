from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListDevicesRequest(BaseModel):
    AccessToken: StrictStr
    Limit: StrictInt | None = None
    PaginationToken: StrictStr | None = None
