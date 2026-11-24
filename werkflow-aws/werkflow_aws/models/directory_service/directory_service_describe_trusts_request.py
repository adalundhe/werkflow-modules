from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeTrustsRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    TrustIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
