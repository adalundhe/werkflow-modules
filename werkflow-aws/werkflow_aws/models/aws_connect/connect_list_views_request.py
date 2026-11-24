from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListViewsRequest(BaseModel):
    InstanceId: StrictStr
    Type: Literal['CUSTOMER_MANAGED', 'AWS_MANAGED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
