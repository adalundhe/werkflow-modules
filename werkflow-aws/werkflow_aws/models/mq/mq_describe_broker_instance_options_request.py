from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MQDescribeBrokerInstanceOptionsRequest(BaseModel):
    EngineType: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    StorageType: StrictStr | None = None
