from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_entity_label import ComprehendEntityLabel


class ComprehendContainsPiiEntitiesResponse(BaseModel):
    Labels: list[ComprehendEntityLabel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
