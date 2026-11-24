from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LambdaGetDurableExecutionHistoryRequest(BaseModel):
    DurableExecutionArn: StrictStr
    IncludeExecutionData: StrictBool | None = None
    MaxItems: StrictInt | None = None
    Marker: StrictStr | None = None
    ReverseOrder: StrictBool | None = None
