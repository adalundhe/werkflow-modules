from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SNSGetSMSAttributesResponse(BaseModel):
    attributes: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
