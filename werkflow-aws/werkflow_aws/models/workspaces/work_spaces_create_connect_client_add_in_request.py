from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesCreateConnectClientAddInRequest(BaseModel):
    ResourceId: StrictStr
    Name: StrictStr
    URL: StrictStr
