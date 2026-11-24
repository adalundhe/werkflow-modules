from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaGetDurableExecutionStateRequest(BaseModel):
    DurableExecutionArn: StrictStr
    CheckpointToken: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
