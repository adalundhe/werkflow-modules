from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_indexing_rule import XRayIndexingRule


class XRayUpdateIndexingRuleResponse(BaseModel):
    IndexingRule: XRayIndexingRule | None = None
    ResponseMetadata: dict[str, Any] | None = None
