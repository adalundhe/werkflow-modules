from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class IoTCreateStreamResponse(BaseModel):
    streamId: StrictStr | None = None
    streamArn: StrictStr | None = None
    description: StrictStr | None = None
    streamVersion: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
