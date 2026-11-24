from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_batch_delete_featured_results_set_error import KendraBatchDeleteFeaturedResultsSetError


class KendraBatchDeleteFeaturedResultsSetResponse(BaseModel):
    Errors: list[KendraBatchDeleteFeaturedResultsSetError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
