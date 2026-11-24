from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceListCertificatesRequest(BaseModel):
    DirectoryId: StrictStr
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
