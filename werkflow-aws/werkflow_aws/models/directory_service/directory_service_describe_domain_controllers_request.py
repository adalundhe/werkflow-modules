from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeDomainControllersRequest(BaseModel):
    DirectoryId: StrictStr
    DomainControllerIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
