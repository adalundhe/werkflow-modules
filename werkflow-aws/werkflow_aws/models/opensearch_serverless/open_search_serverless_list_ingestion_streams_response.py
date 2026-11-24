from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_ingestion_stream_summary import OpenSearchServerlessIngestionStreamSummary


class OpenSearchServerlessListIngestionStreamsResponse(BaseModel):
    ingestionStreamSummaries: list[OpenSearchServerlessIngestionStreamSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
