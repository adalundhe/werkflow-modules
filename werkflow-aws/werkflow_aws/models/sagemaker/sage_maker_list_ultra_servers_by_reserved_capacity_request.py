from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListUltraServersByReservedCapacityRequest(BaseModel):
    ReservedCapacityArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
