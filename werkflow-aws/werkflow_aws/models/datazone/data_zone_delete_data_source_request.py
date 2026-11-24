from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDeleteDataSourceRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    clientToken: StrictStr | None = None
    retainPermissionsOnRevokeFailure: StrictBool | None = None
