from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchGetPackageVersionHistoryRequest(BaseModel):
    PackageID: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
