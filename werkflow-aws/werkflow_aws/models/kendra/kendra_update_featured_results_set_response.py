from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_featured_results_set import KendraFeaturedResultsSet


class KendraUpdateFeaturedResultsSetResponse(BaseModel):
    FeaturedResultsSet: KendraFeaturedResultsSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
