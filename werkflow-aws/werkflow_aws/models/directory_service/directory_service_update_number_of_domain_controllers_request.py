from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceUpdateNumberOfDomainControllersRequest(BaseModel):
    DirectoryId: StrictStr
    DesiredNumber: StrictInt
