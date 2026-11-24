from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneGetTimeSeriesDataPointRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    identifier: StrictStr
    formName: StrictStr
