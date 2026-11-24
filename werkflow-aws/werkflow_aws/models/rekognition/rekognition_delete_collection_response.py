from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class RekognitionDeleteCollectionResponse(BaseModel):
    StatusCode: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
