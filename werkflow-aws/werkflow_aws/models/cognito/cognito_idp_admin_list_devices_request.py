from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPAdminListDevicesRequest(BaseModel):
    UserPoolId: StrictStr
    Username: StrictStr
    Limit: StrictInt | None = None
    PaginationToken: StrictStr | None = None
