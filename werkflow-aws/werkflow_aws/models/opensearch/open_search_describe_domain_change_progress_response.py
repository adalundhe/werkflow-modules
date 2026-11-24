from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_change_progress_status_details import OpenSearchChangeProgressStatusDetails


class OpenSearchDescribeDomainChangeProgressResponse(BaseModel):
    ChangeProgressStatus: OpenSearchChangeProgressStatusDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
