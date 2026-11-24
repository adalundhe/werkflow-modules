from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneDeleteTimeSeriesDataPointsRequest(BaseModel):
    domainIdentifier: StrictStr
    entityIdentifier: StrictStr
    entityType: Literal['ASSET', 'LISTING']
    formName: StrictStr
    clientToken: StrictStr | None = None
