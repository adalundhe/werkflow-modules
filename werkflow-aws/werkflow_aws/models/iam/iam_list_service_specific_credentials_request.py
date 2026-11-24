from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IAMListServiceSpecificCredentialsRequest(BaseModel):
    UserName: StrictStr | None = None
    ServiceName: StrictStr | None = None
    AllUsers: StrictBool | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
