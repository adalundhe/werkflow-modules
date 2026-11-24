from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeConnectionQueryStringParameter(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    IsValueSecret: StrictBool | None = None
