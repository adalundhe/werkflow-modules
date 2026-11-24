from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_suggester_status import CloudSearchSuggesterStatus


class CloudSearchDescribeSuggestersResponse(BaseModel):
    Suggesters: list[CloudSearchSuggesterStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
