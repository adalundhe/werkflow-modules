from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_ingestion_job_summary import OpenSearchServerlessIngestionJobSummary


class OpenSearchServerlessListIngestionJobsResponse(BaseModel):
    ingestionJobSummaries: list[OpenSearchServerlessIngestionJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
