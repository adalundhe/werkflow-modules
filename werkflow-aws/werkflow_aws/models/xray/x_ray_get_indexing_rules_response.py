from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_indexing_rule import XRayIndexingRule


class XRayGetIndexingRulesResponse(BaseModel):
    IndexingRules: list[XRayIndexingRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
