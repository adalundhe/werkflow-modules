from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTSetDefaultAuthorizerResponse(BaseModel):
    authorizerName: StrictStr | None = None
    authorizerArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
