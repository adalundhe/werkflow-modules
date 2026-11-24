from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_entity import GlueEntity


class GlueListEntitiesResponse(BaseModel):
    Entities: list[GlueEntity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
