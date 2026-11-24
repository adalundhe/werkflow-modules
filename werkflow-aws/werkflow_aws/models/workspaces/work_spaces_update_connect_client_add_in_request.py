from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesUpdateConnectClientAddInRequest(BaseModel):
    AddInId: StrictStr
    ResourceId: StrictStr
    Name: StrictStr | None = None
    URL: StrictStr | None = None
