from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LambdaListEventSourceMappingsRequest(BaseModel):
    EventSourceArn: StrictStr | None = None
    FunctionName: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
