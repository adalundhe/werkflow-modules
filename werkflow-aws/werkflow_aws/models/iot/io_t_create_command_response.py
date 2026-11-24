from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateCommandResponse(BaseModel):
    commandId: StrictStr | None = None
    commandArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
