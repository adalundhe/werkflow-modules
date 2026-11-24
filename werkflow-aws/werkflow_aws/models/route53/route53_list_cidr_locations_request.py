from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListCidrLocationsRequest(BaseModel):
    CollectionId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictStr | None = None
