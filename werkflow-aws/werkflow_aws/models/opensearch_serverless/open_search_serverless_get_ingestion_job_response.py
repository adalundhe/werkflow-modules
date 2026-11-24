from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_ingestion_job_detail import OpenSearchServerlessIngestionJobDetail


class OpenSearchServerlessGetIngestionJobResponse(BaseModel):
    ingestionJobDetail: OpenSearchServerlessIngestionJobDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
