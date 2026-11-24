from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateMitigationActionResponse(BaseModel):
    actionArn: StrictStr | None = None
    actionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
