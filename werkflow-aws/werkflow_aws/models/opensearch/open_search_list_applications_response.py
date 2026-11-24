from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_application_summary import OpenSearchApplicationSummary


class OpenSearchListApplicationsResponse(BaseModel):
    ApplicationSummaries: list[OpenSearchApplicationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
