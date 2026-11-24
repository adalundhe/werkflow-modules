from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ACMListAcmeAccountsRequest(BaseModel):
    AcmeEndpointArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
