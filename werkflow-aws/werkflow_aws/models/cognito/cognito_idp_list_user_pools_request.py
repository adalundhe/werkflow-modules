from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPListUserPoolsRequest(BaseModel):
    MaxResults: StrictInt
    NextToken: StrictStr | None = None
