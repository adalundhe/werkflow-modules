from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESBatchGetMetricDataQuery(BaseModel):
    Id: StrictStr
    Namespace: Literal['VDM']
    Metric: Literal['SEND', 'COMPLAINT', 'PERMANENT_BOUNCE', 'TRANSIENT_BOUNCE', 'OPEN', 'CLICK', 'DELIVERY', 'DELIVERY_OPEN', 'DELIVERY_CLICK', 'DELIVERY_COMPLAINT']
    StartDate: datetime.datetime | StrictStr
    EndDate: datetime.datetime | StrictStr
    Dimensions: dict[Literal['EMAIL_IDENTITY', 'CONFIGURATION_SET', 'ISP', 'TENANT_NAME'], StrictStr] | None = None
