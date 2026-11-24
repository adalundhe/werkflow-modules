from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeDataSharesForConsumerRequest(BaseModel):
    ConsumerArn: StrictStr | None = None
    Status: Literal['ACTIVE', 'AVAILABLE'] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
