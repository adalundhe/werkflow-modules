from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class IoTDetachThingPrincipalResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
