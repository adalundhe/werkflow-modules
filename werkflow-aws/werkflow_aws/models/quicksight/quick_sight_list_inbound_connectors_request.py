from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListInboundConnectorsRequest(BaseModel):
    AwsAccountId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Type: list[Literal['QUICK_DESKTOP']] | None = None
