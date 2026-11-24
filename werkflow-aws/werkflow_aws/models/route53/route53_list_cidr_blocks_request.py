from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListCidrBlocksRequest(BaseModel):
    CollectionId: StrictStr
    LocationName: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictStr | None = None
