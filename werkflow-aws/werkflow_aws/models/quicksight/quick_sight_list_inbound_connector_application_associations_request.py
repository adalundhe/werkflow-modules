from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListInboundConnectorApplicationAssociationsRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
