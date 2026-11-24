from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_pii_entity import ComprehendPiiEntity


class ComprehendDetectPiiEntitiesResponse(BaseModel):
    Entities: list[ComprehendPiiEntity] | None = None
    ResponseMetadata: dict[str, Any] | None = None
