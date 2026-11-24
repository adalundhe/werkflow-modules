from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeConnectionBodyParameter(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    IsValueSecret: StrictBool | None = None
