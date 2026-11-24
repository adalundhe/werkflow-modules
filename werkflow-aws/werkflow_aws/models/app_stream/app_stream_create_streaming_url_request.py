from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamCreateStreamingURLRequest(BaseModel):
    StackName: StrictStr
    FleetName: StrictStr
    UserId: StrictStr
    ApplicationId: StrictStr | None = None
    Validity: StrictInt | None = None
    SessionContext: StrictStr | None = None
