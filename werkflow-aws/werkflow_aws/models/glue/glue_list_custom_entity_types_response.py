from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_custom_entity_type import GlueCustomEntityType


class GlueListCustomEntityTypesResponse(BaseModel):
    CustomEntityTypes: list[GlueCustomEntityType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
