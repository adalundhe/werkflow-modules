from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListMetricsRequest(BaseModel):
    InstanceId: StrictStr
    Type: Literal['AWS_MANAGED', 'CUSTOMER_MANAGED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
