from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMListAssociationVersionsRequest(BaseModel):
    AssociationId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
