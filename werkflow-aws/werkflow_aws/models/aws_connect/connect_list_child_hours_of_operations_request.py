from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListChildHoursOfOperationsRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
