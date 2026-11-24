from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeDataSharesForProducerRequest(BaseModel):
    ProducerArn: StrictStr | None = None
    Status: Literal['ACTIVE', 'AUTHORIZED', 'PENDING_AUTHORIZATION', 'DEAUTHORIZED', 'REJECTED'] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
