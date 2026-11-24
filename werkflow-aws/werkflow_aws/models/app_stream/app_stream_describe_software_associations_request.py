from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeSoftwareAssociationsRequest(BaseModel):
    AssociatedResource: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
