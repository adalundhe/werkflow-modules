from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class SESPutEmailIdentityDkimAttributesResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
